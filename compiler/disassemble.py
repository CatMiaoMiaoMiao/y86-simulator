import re
import os, sys
regs = {"%eax": "0","%ecx": "1","%edx": "2","%ebx": "3","%esp": "4",
        "%ebp": "5","%esi": "6","%edi": "7","rnone": "8"}
instr = {
        "nop": "00",
        "halt": "10",
        "rrmovl": "20",
        "irmovl": "30",
        "rmmovl": "40",
        "mrmovl": "50",
        "addl": "60",
        "subl": "61",
        "andl": "62",
        "xorl": "63",
        "jmp": "70",
        "jle": "71",
        "jl": "72",
        "je": "73",
        "jne": "74",
        "jge": "75",
        "jg": "76",
        "call": "80",
        "ret": "90",
        "pushl": "a0",
        "popl": "b0",
        "iaddl": "c0",
        "leave": "d0"
			}
instbyte = {
        "nop": 1,
        "halt": 1,
        "rrmovl": 2,
        "irmovl": 6,
        "rmmovl": 6,
        "mrmovl": 6,
        "addl": 2,
        "subl": 2,
        "andl": 2,
        "xorl": 2,
        "jmp": 5,
        "jle": 5,
        "jl": 5,
        "je": 5,
        "jne": 5,
        "jge": 5,
        "jg": 5,
        "call": 5,
        "ret": 1,
        "pushl": 2,
        "popl": 2,
        "iaddl": 6,
        "leave": 1
			}
bytelen = {'.long': 4,'.word': 2,'.byte': 1}

def dictreverse(dict):
    d = {}
    for item in dict:
        d[dict[item]] = item
    return d

def hexreverse(number):
    result = ''
    flag = 0x80000000
    for i in reversed(range(0,8,2)):
        result = result + number[i:i+2] 
    value = int(result, 16)
    if value & flag == 0:        
        a = int(result, 16)
        a = int(a)
        return str(a)
    value = 0xffffffff + 1 - value
    value = int(str(value))
    return '-' + str(value)     
    
    
def disassemble(INFILE, OUTFILE):
    curraddress = 0
    errors = []
    global regs, instr
    regs =  dictreverse(regs)
    instr = dictreverse(instr)
    for reline in INFILE:
        reline = re.sub(r'\|.*$', '', reline)      #comment like     |...
        reline = re.sub(r'\s*,\s*', ',', reline)  #explcit blanks  
        items = reline.split(':')
        add = items[0]
        try:
            ins = items[1]
        except:
            continue
        add = add.replace(' ', '')
        ins = ins.replace(' ', '')
        ins = ins.replace('\n', '')
        
        add = int(add, 16)
        if add != curraddress:
            OUTFILE.write('.pos 0x%x\n' % (add))
            curraddress = add
        if ins == '':
            continue
        if ins in ('00','10','90','d0'):
            OUTFILE.write(instr[ins] + '\n')
            curraddress += instbyte[instr[ins]]
        elif ins[:2] in ('60', '61', '62', '63', '20'):
            instruction = ins[:2]
            register = ins[2:4]
            string = instr[instruction] + ' ' + regs[register[0]] + ',' + regs[register[1]] + '\n'
            OUTFILE.write(string)
            curraddress += instbyte[instr[instruction]]
        elif ins[:2] in ('a0', 'b0'):
            instruction = ins[:2]
            register = ins[2]
            string = instr[instruction] + ' ' + regs[register] + '\n'
            OUTFILE.write(string)
            curraddress += instbyte[instr[instruction]]
        elif ins[:2] == '80' or ins[0] == '7':
            instruction = ins[:2]
            valC = ins[2:10]
            string = instr[instruction] + ' ' + hexreverse(valC) + '\n'
            OUTFILE.write(string)
            curraddress += instbyte[instr[instruction]]
        elif ins[:2] in ('30', 'c0'):
            instruction = ins[:2]
            register = ins[3]
            valC = ins[4:12]
            string = instr[instruction] + ' ' + '$' + hexreverse(valC) + ',' + regs[register] + '\n'
            OUTFILE.write(string)
            curraddress += instbyte[instr[instruction]]
        elif ins[:2] == '40':
            instruction = ins[:2]
            register = ins[2:4]
            valC = ins[4:12]
            string = instr[instruction] + ' ' + regs[register[0]] + ', ' + hexreverse(valC) + \
                '(' + regs[register[1]] + ')'  + '\n'
            OUTFILE.write(string)
            curraddress += instbyte[instr[instruction]]
        elif ins[:2] == '50':
            instruction = ins[:2]
            register = ins[2:4]
            valC = ins[4:12]
            string = instr[instruction] + ' ' + hexreverse(valC) + \
                '(' + regs[register[1]] + '), ' + regs[register[0]]  + '\n'
            OUTFILE.write(string)
            curraddress += instbyte[instr[instruction]]



def main():
    print('Y86 deassembler')
    print('Usage: inputfile [outputfile]')
    try:
        INFILE = open(sys.argv[1])
    except IOError:
        print('Error: cannot open input file: %s' % sys.argv[0])
        sys.exit(1)
    except IndexError:
        sys.exit(0)
    try:
        OUTFILE = open(sys.argv[2], 'w')
    except IOError:
        print('Error: cannot open output file: %s' % sys.argv[1])
        sys.exit(1)
    except IndexError:
        dir = sys.argv[1].replace('.yo', '.ys')
        OUTFILE = open(dir, 'w')
    except:
        print ('invalid input file type')

    disassemble(INFILE, OUTFILE)
    print 'disassemble success!'

if __name__ == '__main__':
    main()

