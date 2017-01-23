"""module for constant folding of the AST"""

from ast import \
    Program, \
    VarDecl, \
    Function, \
    Identifier, \
    Type, \
    Block, \
    AssignStmt, \
    IfStmt, \
    WhileStmt, \
    ReturnStmt, \
    LValue, \
    IntLiteral, \
    FloatLiteral, \
    Operator, \
    ArithExpr, \
    FuncCall, \
    CondExpr

import numpy as np

and64 = 0xffffffffffffffff

def foldingAST(node):
    if isinstance(node, IntLiteral) \
            or isinstance(node, FloatLiteral):
        return node
    elif isinstance(node, ArithExpr):
        l = foldingAST(node.left)
        r = foldingAST(node.right)
        if isinstance(l, IntLiteral) and isinstance(r, IntLiteral):
            if node.op.val == "+":
                return IntLiteral(str(np.int64(int(l.val.split('.')[0])) + np.int64(int(r.val.split('.')[0]))))
            elif node.op.val == "*":
                return IntLiteral(str(np.int64(int(l.val.split('.')[0])) * np.int64(int(r.val.split('.')[0]))))
            elif node.op.val == "-":
                return IntLiteral(str(np.int64(int(l.val.split('.')[0])) - np.int64(int(r.val.split('.')[0]))))
            elif node.op.val == "/":
                return IntLiteral(str(int(np.int64(int(l.val.split('.')[0])) // np.int64(int(r.val.split('.')[0])))))
        if isinstance(l, FloatLiteral) and isinstance(r, FloatLiteral):
            if node.op.val == "+":
                return FloatLiteral(str((np.float64(float(l.val)) + np.float64(float(r.val)))))
            elif node.op.val == "*":
                return FloatLiteral(str((np.float64(float(l.val)) * np.float64(float(r.val)))))
            elif node.op.val == "-":
                return FloatLiteral(str((np.float64(float(l.val)) - np.float64(float(r.val)))))
            elif node.op.val == "/":
                return FloatLiteral(str((np.float64(float(l.val)) // np.float64(float(r.val)))))
        node.left = l
        node.right = r
        return node
    elif isinstance(node, ReturnStmt):
        node.expr = foldingAST(node.expr)
        return node
    elif isinstance(node, AssignStmt):
        node.expr = foldingAST(node.expr)
        return node
    elif isinstance(node, CondExpr):
        node.left = foldingAST(node.left)
        node.right = foldingAST(node.right)
        return node
    elif isinstance(node, VarDecl):
        new_list = []
        for x in node.array:
            new_list.append(foldingAST(x))
        node.array = new_list
        return node
    elif isinstance(node, FuncCall):
        foldingAST(node.func_name)
        new_list = []
        for c in node.par_list:
            new_list.append(foldingAST(c))
        node.par_list = new_list
        return node
    else:
        for c in node.children():
            foldingAST(c)
        return node
