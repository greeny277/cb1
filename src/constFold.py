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


def foldingAST(node):
    if isinstance(node, IntLiteral) \
            or isinstance(node, FloatLiteral):
        return node
    elif isinstance(node, ArithExpr):
        l = foldingAST(node.left)
        r = foldingAST(node.right)
        if isinstance(l, IntLiteral) and isinstance(r, IntLiteral):
            if node.op.val == "+":
                node = IntLiteral(str(float(l.val) + float(r.val)))
                return node
            elif node.op.val == "*":
                node = IntLiteral(str(float(l.val) * float(r.val)))
                return node
            elif node.op.val == "-":
                node = IntLiteral(str(float(l.val) - float(r.val)))
                return node
            else:
                node = IntLiteral(str(float(l.val) / float(r.val)))
                return node
        if isinstance(l, FloatLiteral) and isinstance(r, FloatLiteral):
            if node.op.val == "+":
                node = FloatLiteral(str(float(l.val) + float(r.val)))
                return node
            elif node.op.val == "*":
                node = FloatLiteral(str(float(l.val) * float(r.val)))
                return node
            elif node.op.val == "-":
                node = FloatLiteral(str(float(l.val) - float(r.val)))
                return node
            else:
                node = FloatLiteral(str(float(l.val) / float(r.val)))
                return node
    else:
        for c in node.children():
            foldingAST(c)
