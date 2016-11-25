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
                return IntLiteral(str(int(float(l.val)) + int(float(r.val))))
            elif node.op.val == "*":
                return IntLiteral(str(int(float(l.val)) * int(float(r.val))))
            elif node.op.val == "-":
                return IntLiteral(str(int(float(l.val)) - int(float(r.val))))
            elif node.op.val == "/":
                return IntLiteral(str(int(float(l.val)) / int(float(r.val))))
        if isinstance(l, FloatLiteral) and isinstance(r, FloatLiteral):
            if node.op.val == "+":
                return FloatLiteral(str(float(l.val) + float(r.val)))
            elif node.op.val == "*":
                return FloatLiteral(str(float(l.val) * float(r.val)))
            elif node.op.val == "-":
                return FloatLiteral(str(float(l.val) - float(r.val)))
            elif node.op.val == "/":
                return FloatLiteral(str(float(l.val) / float(r.val)))
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
    else:
        for c in node.children():
            foldingAST(c)
        return node
