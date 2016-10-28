Hinweise zur Benutzung der Testsuite
====================================

Diese Testsuite wird mit dem hier befindlichen Makefile ausgeführt.
Die COMPILEROPTS - Variable legt fest, welche Kommandozeilenoptionen
ihr E-Compiler bekommt, wenn die Testsuite ausgeführt wird.

Wenn Ihr Computer zu langsam ist, tragen Sie ggf einen größeren Wert
in die TIMEOUT-Variable ein; diese legt fest, nach wievielen Sekunden
ein Testprogramm (mit einem Fehler) abgebrochen wird.

Sie koennen mit der Testsuite feststellen, ob ihr Compiler laut
Sprachspezifikation korrekte Programme akzeptiert und alle anderen
Programme als fehlerhaft abweist.  Dazu muss ihr Compiler sich bei
alle korrekten Programme mit Exit-Status 0, und bei allen fehlerhaften
Programmen mit Exit-Status 1 beenden.

Fuer jedes Testprogramm X.e gibt es eine Datei X.e.ces. Letztere
enthaelt den erwarteten Exit-Code, den der Compiler fuer diesen
Testfall ausgeben soll.

Falls der Kompiliervorgang erfolgreich ist, gibt es für das
entstehende Programm einen oder mehrere Testcases. Jeder Testcase hat
eine .out Datei, in der der erwartete Output des Programms steht, eine
.res Datei, in der der erwartete Exit-Status des Programms steht (also
der Returnwert der Main-Methode des Programms), und gegebenenfalls
eine .in Datei, in der der Input steht, den das Programm während
dieses speziellen Testcases erhält. 

Beispiel:
Vorgegebene Dateien:
    brainfuck.e       - Quellcode in E
    brainfuck.e.ces   - Erwarteter Exitstatus des E-Compilers
    brainfuck.e.1.in  - Input für den 1. Test
    brainfuck.e.1.out - Erwarteter Output des 1. Tests
    brainfuck.e.1.res - Erwarteter Exitstatus des 1. Tests
    brainfuck.e.2.in  - Input für den 2. Test			  
    brainfuck.e.2.out - Erwarteter Output des 2. Tests	  
    brainfuck.e.2.res - Erwarteter Exitstatus des 2. Tests
	
Generierte Dateien:
    brainfuck.e.run       - Lauffähiges Programm
	brainfuck.e.ces.tmp   - Tatsächlicher Exitstatus des E-Compilers
	brainfuck.e.compstamp - Leere Datei, wird angelegt wenn brainfuck.e.ces
	                        und brainfuck.e.ces.tmp den gleichen Inhalt haben.
	brainfuck.e.1.out.tmp - Tatsächlicher Output des Programms beim 1. Test
	brainfuck.e.1.res.tmp - Tatsächlicher Exitstatus des Programms beim 1. Test
	brainfuck.e.2.out.tmp - Tatsächlicher Output des Programms beim 2. Test
	brainfuck.e.2.res.tmp - Tatsächlicher Exitstatus des Programms beim 2. Test
	brainfuck.e.runstamp  - Leere Datei, wird angelegt wenn für alle Tests der
						    Output gleich dem erwarteten Output ist und der Exitstatus
							gleich dem erwarteten Exitstatus ist.


Das Makefile hat ausser dem Default-Target die folgenden Targets:

  compile  - Kompiliert alle Quelltextdateien (bis auf die,
  		   	 die Gleitkommazahlen verwenden)
  run      - Lässt alle Testcases laufen
  clean    - Räumt die Kompilate, temporären Dateien und Stamp-Dateien weg
  uebung01 - kompiliert alle Programme die nach Übung 1 kompilieren sollen
  uebung02 - kompiliert alle Programme die nach Übung 2 kompilieren sollen
  uebung03 - kompiliert alle Programme die nach Übung 3 kompilieren sollen
  help     - eine kleine Hilfe
  
Das Default-Target startet zuerst das Target "compile" und dann das
Target "run".

Wir werden Ihren Compiler gegen diese und andere Programme
bzw. Testcases testen; falls Ihr Compiler von den in diesen Testcases
beschriebenen Verhalten abweichen sollte und Sie dies sinnvoll
begründen können, so bitten wir darum dies auch zu tun.

