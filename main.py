'''
Created on 2013-6-9

@author: rockyRocky
'''

__ver__ = '1.0.1'

import getopt
import binascii
import os
import sys

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
''' % os.path.basename(sys.argv[0]))
    sys.exit(1)
    
def main():
    simulator = Simulator()
    print('Y86-Simulator ics course pj %s\nCopyright (c) 2013 CatMiaoMiaoMiao' % __ver__)
    print ('Kernel version: %s\n' % simulator.__ver__)
    
# parse opts
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'bsm:gnh', \
                ['bigendian', 'second', 'maxcycle', 'guimode', 'nologfile', 'help'])
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
                simulator.isNoLogFile = True
            if o in ('-h', '--help'):
                showUsage()
    except getopt.GetoptError:
        print("Error: illegal option")
        showUsage()
    inputName = args[0]
# accept both binary and non-binary
    try:
        fin = open(inputName, 'r')
    except:
        print('Error: cannot open binary: %s' % inputName)
        sys.exit(1)
        
    # Automatic pipeline run
    try:
        simulator.run(fin)
        fin.close()
    except IOError:
        print('Warning: cannot create log file')
    except:
        print('Error: cannot identify binary: %s' % (inputName))
        
    print('Simulation finished')
     
if __name__ == '__main__':
    main()