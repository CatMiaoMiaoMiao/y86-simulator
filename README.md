y86-simulator
=============

Copyright (c) 2013 rockyRocky,LumiG,vv.

ics 2012-2 Final Project 
Presented by CatMiaoMiaoMiao,FDU
version 1.0  
 
This is a project including a y86-simulator as described in CMU's CSAPP and a set of assemble and disassemble environment for y86 programming, each with an excellent GUI support.
The project is written in Python and can be used under all platforms with a python environment. To run it, you should first have python installed in your computer. They can be found in http://www.python.org/download/. At least python2.6 is needed and it does not compatible with python3. Our GUI mode for the tools are written in PyQT4. To enjoy them, you just need to download the PyQT4 utilities here in http://www.riverbankcomputing.com/software/pyqt/download. The project is open-source and not for commercial purpose. You can modify it or use it in any part of your own software as you like.


Pipelined Y86 Simulator:
=============
The commandline version can be called by python main.py in the root directory. Type -h to see the help text of it. Only .yo standard input files are supported. To use the GUI version of the simulator, try switching to the GUI directory and run python y86.py. Both .ys and .yo files are supported. If an invalid .ys file is loaded, the program will automatically called the GUI version of the assembler to help you fix the problems.

Features:

1.Support all the instuctions described in CMU CSAPP 1st edition. iaddl and leave instrucions are extended as described in lab4 of the book.

2.In the command lines, you can get into the debug mode with -d option to enjoy the ydb tool. It is sometimes sensitive to the ketboard

3.The memory and cache system are used in the simulator and are presented in the GUI mode.

4.Other amazing fuctions.

Assemble/Disassemble Environment
=============
The tools can be found in folder compiler. This directory includes assemble/disassemble tools for Y86 programing. To use them in the commandlines, you can try python assemble.py or python disassemble.py . To use the GUI mode, just try python start.py . The assembling/disassembling tools follow the rules as described in CSAPP 1st editon except that the disassembling tool does not support .long or .byte instruction. Every time it finds the address of an instuction not match its length, the .pos instrucion will be applied to fix it. In the GUI mode, hit run to test your code in our simulator easily. 

Have fun!
