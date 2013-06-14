'''
Created on 2013-6-9

@author: rockyRocky
'''
__ver__ = '1.0.1'

import getopt
import binascii
import os
import sys
import thread
import termios

from kernel.Simulator import *

def showUsage():
    print('''Usage: %s [options] [y86 binary object]

Options:
  -h, --help            show this help message and exit
  -s, --second          use decoding rules in csapp 2nd edition. (default
                        using 1st editon rules)
  -m MAXCYCLE, --maxcycle=MAXCYCLE
                        set limit of running cycles. 0 means no limit.
                        (default is 32767)
  -g, --guimode         set log output syntax for GUI. (default is disabled)
  -n, --nologfile       print log to stdout instead of writing to file.
                        (default is disabled)
  -p, --print           print log on screen
  -l, --logfile=LOGFILE customize a new logfile. (default using input name
                        with .txt suffix)
  -d, --debug           begin debug mode (not done yet) 
''' % os.path.basename(sys.argv[0]))
    sys.exit(1)
  
def showDebugUsage():  
  print ('''[command]
  
Command:
    c, continue         run till the end/breakpoint
    s, step, n, next    step into next cycle
    b, back             back to last cycle
    h, help             show this help
    q, quit             quit
while running:
    p                   pause
    c                   continue
    +                   speed up
    -                   slow down 
    q                   quit running mode 
''')
  
def main():
    global simulator
    simulator = Simulator()
    isDebugMode = False
    fout = None
    print ('='*51)
    print '|'+' '*49+' '+'|'
    print '|'+('  Y86-Simulator ics course pj %s  ' % __ver__).center(50)+'|'
    print '|'+('  Copyright(c) 2013 CatMiaoMiaoMiao  ').center(50)+'|'    
    print '|'+('  Kernel version: %s  ' % simulator.__ver__).center(50)+'|'
    print '|'+' '*49+' '+'|'
    print ('='*51)
    
# parse opts
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'bsm:gnpl:dh', \
                ['bigendian', 'second', 'maxcycle', 'guimode', 'nologfile', \
                 'print', 'logfile', 'debug', 'help'])
        if len(opts) == 0 and len(args) != 1:
            if len(args) == 0:
                print("Error: missing input file")
            else:
                print("Error: only one input file allowed")
            showUsage()
        for o, a in opts:
            if o in ("-b", "--bigendian"):
                simulator.isBigEndian = True
            if o in ("-s", "--second"):
                simulator.isSecond = True
                print('Warning: using csapp 2nd edition rules')
            if o in ("-m", "--maxcycle="):
                try:
                    simulator.maxCycle = int(a)
                except ValueError:
                    print('Error: invalied cycle number')
                    sys.exit(1)
            if o in ("-g", "--guimode"):
                simulator.isGuimode = True
            if o in ("-n", "--nologfile"):
                if simulator.logfile!=None:
                    print ('Switch conflict: want a logfile or not?')
                    sys.exit(1)
                simulator.isNoLogFile = True
            if o in ("-p", "--print"):
                simulator.isOnScreen = True
            if o in ("-l", "--logfile="):
                if simulator.isNoLogFile:
                    print ('Switch conflict: want a logfile or not?')
                    sys.exit(1)
                try:
                    fout = open(a, 'w')
                except:
                    print ('Error: cannot open a logfile to write')
                    sys.exit(1)
            if o in ('-d', '--debug'):
                isDebugMode = True
            if o in ('-h', '--help'):
                showUsage()
    except getopt.GetoptError:
        print("Error: illegal option")
        showUsage()
    
    # prepare simulator input/output file
    inputName = args[0]
    # TODO: accept both binary and non-binary
    try:
        fin = open(inputName, 'r')
    except:
        print('Error: cannot open binary: %s' % inputName)
        sys.exit(1)
    simulator.load(fin, fout)
    fin.close()
    
    # to check if it is run under debug mode
    if isDebugMode:
        simulator.isOnScreen = True
        simulator.isGoing = False
        thread.start_new_thread(simulator.run, ())
        cmd = ''
        while not simulator.isTerminated:
            tmp = raw_input("(ydb) ")
            cmd = tmp if tmp!='' else cmd
            if (cmd=='c' or cmd=='continue'):
                runSimulator()
            elif (cmd=='b' or cmd=='back'):
                simulator.back()
            elif (cmd=='s' or cmd=='step' or cmd=='n' or cmd=='step'):
                if not simulator.step():
                    break
            elif (cmd=='h' or cmd=='help'):
                showDebugUsage()
            elif (cmd=='q' or cmd=='quit'):
                print ('bye')
                sys.exit(1)
            else:
                print ('no such command')
                print ('type \'help\' or \'h\' for help')
    else:
        # Automatic pipeline run
        try:       
            simulator.interval = 0
            simulator.isGoing = True
            simulator.run()
            
        except IOError:
            print('Warning: cannot create logfile')
        except Exception, e:
            print e
            print('Error: cannot identify binary: %s' % (inputName))
    
    # finish    
    print('Simulation finished\n')

def runSimulator():
    global simulator
    simulator.isGoing = True
    while (not simulator.isTerminated):
        c = getkey()
        if c=='+':
            simulator.interval /= 2.0
        elif c=='-':
            simulator.interval *= 2.0
        elif c=='p':
            simulator.isGoing = False
        elif c=='c':
            simulator.isGoing = True
        elif c=='q':
            simulator.isGoing = False
            time.sleep(0.1)
            break
        pass
    
def getkey():
    term = open("/dev/tty", "r")
    fd = term.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] &= ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
        term.close()
    return c

if __name__ == '__main__':
    main()