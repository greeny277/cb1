Python-Vorlage für Übersetzerbau 1. Die Vorlage sollte mit Python 3.4
funktionieren - falls nicht, bitte ich um Fehlermeldungen.

Dateien/Verzeichnisse und ihr Inhalt:
 - ast.py                     : Enthält die Klassen des AST.
 - common.py                  : Enthält kleinere Hilfsklassen (Typen, Exceptions etc.)
 - dumpAST.py                 : Enthält eine Methode, den AST auszugeben
 - e_lexer.py, e_parser.py    : Lexer und Parser für E
 - main.py                    : Enthält die Hauptroutine, mit Argumentparsing etc.
 - ply                        : Enthält den Quellcode für den Parser/Lexer. Kann ignoriert werden.

Der verwendete Lexer/Parser heisst PLY und ist unter
    http://www.dabeaz.com/ply/
ausführlich dokumentiert.

Die Klassenhierarchie und die Docstrings können mit help() angezeigt werden:

    $ python
    Python 2.7.3 (default, Jan  2 2013, 13:56:14) 
    [GCC 4.7.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import ast
    >>> help(ast)
    ...

Hilfreiche Tools:

pep8 : 
     Style Guide Checker. 
     Erhöht die Lesbarkeit, um Verwendung wird gebeten.

pylint : 
     Statischer Quellcode-Checker für Python. 
     Verwendung wird empfohlen; typische Kommandozeile:
           pylint -i y -r n --disable invalid-name *.py

pudb, winpdb: 
     Debugger für Python, je für Konsole und für GUI.
 
Zum Testen sei auf die Datei testsuite/README.txt verwiesen.
