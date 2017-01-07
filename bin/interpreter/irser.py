"""serialization module"""

import json
from ir import ConstValue, Operand, \
    Register, HardwareRegister, VirtualRegister, IRProgram, IRFunction, \
    IRVariable, CASSGN, CI2R, CR2I, CADD, CSUB, CMUL, CDIV,\
    CBRA, CBEQ, CBNE, CBLT, CBGT, CBLE, CBGE, CTarget, CBinary,\
    CSingle, CBranch, CCondBranch, CLOAD, CSTORE, CCALL, CPUSH, \
    CLABEL, CRET, CUnary, CPHI

from common import Type, InternalError


class IRJSONEncoder(json.JSONEncoder):
    """helper class for encoding"""
    def __init__(self, *args, **kwargs):
        super(IRJSONEncoder, self).__init__(*args, **kwargs)
        self.IRJSONEncoder_regid = 0
        self.IRJSONEncoder_varid = 0
        self.identifiers = set()

    def addType(self, obj, _type):
        """add type to json object"""
        obj['type'] = self.default(_type)
        return obj

    # pylint: disable=method-hidden
    def default(self, o):
        """default encoding method"""
        # pylint: disable=too-many-return-statements,too-many-branches
        if isinstance(o, ConstValue):
            x = {'classtype': o.__class__.__name__,
                 'const': str(o.val)}
            self.addType(x, o.type)
            return x
        elif isinstance(o, Operand):
            if isinstance(o.val, ConstValue):
                return self.default(o.val)
            return o.val.name
        elif isinstance(o, Register):
            x = {'classtype': o.__class__.__name__,
                 'name': o.name}
            self.addType(x, o.type)
            return x
        elif isinstance(o, Type):
            # pylint: disable=protected-access
            x = {'basetype': o.getBaseType()._name}
            if o.isArray():
                x['dims'] = [int(d) for d in o.getSimpleDimList()]
            return x
        elif isinstance(o, IRVariable):
            x = {'classtype': o.__class__.__name__,
                 'name': o.name}
            self.addType(x, o.type)
            return x
        elif isinstance(o, IRProgram):
            return {'funcs': [self.default(f) for f in o.functions
                              if not f.isPredefined],
                    'globals': [self.default(f) for f in o.variables]}
        elif isinstance(o, IRFunction):
            x = {'name': o.name}
            x['params'] = [self.default(o.params[pn]) for pn in o.params]
            x['locals'] = [self.default(o.vars[pn]) for pn in o.vars]
            x['virtRegs'] = [self.default(o.virtRegs[pn]) for pn in o.virtRegs]
            x['code'] = [self.default(instr) for instr in o.instrs()]
            x['returnType'] = self.default(o.returnType)
            return x
        elif isinstance(o, CTarget):
            x = {'classtype': o.__class__.__name__,
                 'target': self.default(o.target)}
            if isinstance(o, CBinary):
                x['left'] = self.default(o.left)
                x['right'] = self.default(o.right)
                return x
            elif isinstance(o, CUnary):
                x['operand'] = self.default(o.source)
                return x
            elif isinstance(o, CCALL):
                x['name'] = o.name
                return x
            elif isinstance(o, CLOAD):
                x['base'] = self.default(o.base)
                x['offset'] = self.default(o.offset)
                return x
            elif isinstance(o, CPHI):
                x['sources'] = [self.default(k) for k in o.sources]
                return x
        elif isinstance(o, CSingle):
            return {'classtype': o.__class__.__name__,
                    'op': self.default(o.source)}
        elif isinstance(o, CLABEL):
            return {'classtype': o.__class__.__name__,
                    'id': o.id}
        elif isinstance(o, CBranch):
            if isinstance(o, CCondBranch):
                return {'classtype': o.__class__.__name__,
                        'left': self.default(o.left),
                        'right': self.default(o.right),
                        'tgt': o.label.id}
            elif isinstance(o, CBRA):
                return {'classtype': o.__class__.__name__,
                        'tgt': o.label.id}
        elif isinstance(o, CSTORE):
            return {'classtype': o.__class__.__name__,
                    'base': self.default(o.target),
                    'offset': self.default(o.offset),
                    'value': self.default(o.value)}
        return super(IRJSONEncoder, self).default(o)


def serialize(program):
    """serialization function. returns a string containing
    a JSON-serialized version of program"""
    e = IRJSONEncoder(indent=2)
    return e.encode(program)


def deserialize(string):
    # pylint: disable=too-many-locals, too-many-branches
    """deserialization function. given a string, returns a
    IRProgram object"""

    p = None
    known = {}
    labelCache = {}
    undefinedLabels = set()
    highestlabel = -1
    constructorUnary = {'CASSGN': CASSGN,
                        'CI2R': CI2R,
                        'CR2I': CR2I}
    constructorBinary = {'CADD': CADD, 'CSUB': CSUB,
                         'CMUL': CMUL, 'CDIV': CDIV}
    constructorCondBranch = {'CBGE': CBGE, 'CBGT': CBGT,
                             'CBLT': CBLT, 'CBLE': CBLE,
                             'CBEQ': CBEQ, 'CBNE': CBNE}
    constructorSingle = {'CPUSH': CPUSH, 'CRET': CRET}

    def genLabel(x, isCreate):
        """helper function to define/use a label"""
        if isCreate:
            undefinedLabels.discard(x)
        nonlocal highestlabel
        assert isinstance(x, int)
        highestlabel = max(highestlabel, x)
        if x in labelCache:
            return labelCache[x]
        ll = CLABEL(x)
        labelCache[x] = ll
        if not isCreate:
            undefinedLabels.add(x)
        return ll
        
    def getVar(obj, isGlobal = False):
        """helper function to generate a register"""
        if isinstance(obj, str):
            return known[obj]
        x = None
        vname = obj['name']
        assert not (vname in known)
        vtype = genType(obj)
        vctype = obj['classtype']
        if vctype == 'VirtualRegister':
            x = VirtualRegister(vname, vtype)
        elif vctype == 'HardwareRegister':
            x = HardwareRegister(vname, vtype)
        elif vctype == 'IRVariable':
            x = IRVariable(vname, vtype, isGlobal)
        else:
            raise Exception("unknown class type: " + str(vctype))
        known[vname] = x
        p.registerUsedName(vname)
        return x

    def genOperand(o):
        """helper function to generate an operand"""
        if isinstance(o, str):
            return getVar(o)
        assert o['classtype'] == 'ConstValue'
        return ConstValue(o['const'], genType(o))

    def genInstr(v):
        """helper function to generate an instruction"""
        # pylint: disable=too-many-return-statements
        t = v['classtype']
        if t in constructorBinary:
            return constructorBinary[t](genOperand(v['target']),
                                        genOperand(v['left']),
                                        genOperand(v['right']))
        if t in constructorUnary:
            return constructorUnary[t](genOperand(v['target']),
                                       genOperand(v['operand']))
        if t in constructorCondBranch:
            return constructorCondBranch[t](genLabel(v['tgt'], False),
                                            genOperand(v['left']),
                                            genOperand(v['right']))
        if t == 'CBRA':
            return CBRA(genLabel(v['tgt'], False))
        if t == 'CLABEL':
            return genLabel(v['id'], True)
        if t == 'CLOAD':
            return CLOAD(genOperand(v['target']),
                         genOperand(v['base']),
                         genOperand(v['offset']))
        if t == 'CPHI':
            return CPHI(genOperand(v['target']),
                        [genOperand(x) for x in v['sources']])
        if t == 'CSTORE':
            return CSTORE(genOperand(v['base']),
                          genOperand(v['offset']),
                          genOperand(v['value']))
        if t in constructorSingle:
            return constructorSingle[t](genOperand(v['op']))
        if t == 'CCALL':
            return CCALL(genOperand(v['target']), v['name'])
        raise InternalError('cannot deserialize ' + repr(v))

    def genIRFunction(f):
        """helper function to generate an IRFunction"""
        labelCache.clear()
        ff = IRFunction(f['name'], p)
        for g in f['params']:
            ff.addParam(getVar(g))
        for g in f['locals']:
            ff.addVar(getVar(g))
        for g in f['virtRegs']:
            xx = getVar(g)
            ff.virtRegs[xx.name] = xx
        for x in f['code']:
            ff.addInstr(genInstr(x))
        ff.isPredefined = f.get('isPredefined', False)
        ff.returnType = genType(f['returnType'])
        if len(undefinedLabels) != 0:
            raise InternalError("use of undefined label(s) " + str(undefinedLabels))
        return ff

    def genType(t):
        """helper function to generate a type"""
        if "type" not in t:
            return Type.getIntType()
        t = t['type']
        if t['basetype'] == 'int':
            x = Type.getIntType()
        elif t['basetype'] == 'real':
            x = Type.getRealType()
        else:
            raise Exception("unknown type: " + t['basetype'])
        if 'dims' in t:
            for dd in t['dims']:
                x = Type.getArrayType(x, str(dd))
        return x

    o = json.JSONDecoder().decode(string)
    p = IRProgram()
    for g in o['globals']:
        p.variables.append(getVar(g, isGlobal=True))
    for g in o['funcs']:
        p.functions.append(genIRFunction(g))
    # pylint: disable=protected-access
    p._nextlabelid = highestlabel + 1
    return p
