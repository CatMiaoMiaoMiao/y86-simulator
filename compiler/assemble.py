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
error = ''    
    
def addconverthex(number):      #convert lineaddress to hex to display
    number = str(hex(number))
    number = number[2:]
    while len(number) < 8:
        number = '0' + number
    return '0x' + number    

def instrconverthex(instruction):   #convert instruct bytes(valc) to hex to display
    if len(instruction) <= 4 or len(instruction) == 10:
        return instruction
    else:
        valC = int(instruction[4:])
        if valC < 0:
            valC = hex(0xffffffff + valC + 1)[2:10]
        else:
            valC = hex(valC)[2:]
        while len(valC) < 8:
            valC = '0' + valC
        result = ''
        for i in reversed(range(0,8,2)):
            result = result + valC[i:i+2] 
        return instruction[:4]+result
        
def noconverthex(instruction):  #convert jump/call address to hex to display
    add = int(instruction)
    add = hex(add)[2:]
    while len(add) < 8:
        add = '0' + add
    result = ''
    for i in reversed(range(0,8,2)):
        result = result + add[i:i+2] 
    return result

def assemble(INFILE, OUTFILE):
    global error
    error=''
    binpos = 0
    linepos = 0
    alignment = 0
    labels = {}
    strippedline = {}
    origline = []
    lineaddress = {}
    for reline in INFILE:
        origline.append(reline)   #save origin lines
        linepos += 1
        reline = re.sub(r'#.*$', '', reline)      #comment like     #...
        reline = re.sub(r'/\*.*\*/', '', reline)  #comment like     /*...*/
        reline = re.sub(r'//.*$', '', reline)     #comment like     //...
        reline = re.sub(r'\s*,\s*', ',', reline)  #explcit blanks    
        if reline.find(':') != -1:
            lab = re.compile('([^\s]+):')
            labmatch = lab.search(reline)
            reline = lab.sub('', reline)
            if labmatch != None:
                labelname = labmatch.group(1)
            else:
                error += 'Line %d: %s\n' % (linepos, 'Label error.')
                continue
            if labelname in labels:
                error += 'Line %d: %s\n' % (linepos, 'Label repeated error.')
                continue
            else:
                labels[labelname] = binpos
                lineaddress[linepos] = binpos
        linecontent = []
        for element in reline.split(' '):
            ele = element.replace('\t', '').replace('\n', '').replace('\r', '')
            if ele != '':
                linecontent.append(ele)
        if linecontent == []:
            continue
        posindex = str(linepos)
        strippedline[posindex] = linecontent
        try:
            if linecontent[0] in instbyte:
                alignment = 0
                lineaddress[linepos] = binpos
                binpos += instbyte[linecontent[0]]
            elif linecontent[0] == '.pos':
                binpos = int(linecontent[1], 0)
                lineaddress[linepos] = binpos
            elif linecontent[0] == '.align':
                alignment = int(linecontent[1], 0)
                if binpos % alignment != 0:
                    binpos += alignment - binpos % alignment
                lineaddress[linepos] = binpos
            elif linecontent[0] in ('.long', '.word', '.byte'):
                lineaddress[linepos] = binpos
                if alignment != 0:
                    binpos += alignment
                else:
                    binpos += bytelen[linecontent[0]]
            else:
                error += 'Line %d: Instruction "%s" not defined.\n' % (linepos, linecontent[0])
                continue
        except:
            error += 'Line %d: Instruction error.\n' % linepos
            continue
    try:
        INFILE.close()
    except IOError:
        pass
    if error != '':
        print('Error: assembly failed:\n%s' % error)
        return
    
    #convert
    allbinline={}
    for line in strippedline:
        binline=''
        linepos = int(line)
        linecontent=strippedline[line]
        if not linecontent:
            allbinline[linepos] = []
            continue
        try:
            if linecontent[0] not in instr:
                label = linecontent[0]
                align = linecontent[1]
                if label == '.align':
                    alignment = int(align)
                elif label in ('.long', '.word', '.byte'):
                    if alignment != 0:
                        length = alignment
                    else:
                        length = bytelen[label]                    
                elif label != '.pos':
                    error += 'Line %d: invalid align label\n' % (linepos)
            else:
                ins_s = linecontent[0]
                try:
                    reg_s = linecontent[1]
                except:
                    pass
                if ins_s in ('nop', 'halt', 'ret', 'leave'):
                    binline = instr[ins_s]
                elif ins_s in ('addl', 'subl', 'andl', 'xorl', 'rrmovl'):
                    registers = reg_s.split(',')
                    binline =  instr[ins_s] +  regs[registers[0]] +  regs[registers[1]]
                elif ins_s in ('pushl', 'popl'):
                    binline = instr[ins_s] + regs[reg_s] + regs["rnone"]
                elif ins_s.startswith('j') or ins_s == 'call':
                    binline = instr[ins_s]
                    if reg_s in labels:
                        binline +=  noconverthex(labels[reg_s])
                    else: 
                        binline +=  noconverthex(reg_s)
                elif ins_s in ('irmovl', 'iaddl'):
                    registers = reg_s.split(',')  
                    if registers[0] in labels:
                        valC =  labels[registers[0]]
                    else:
                        valC =  int(registers[0].replace('$', ''), 0)
                    binline =  instr[ins_s] +  regs["rnone"] + regs[registers[1]] + str(valC)
                elif ins_s == 'rmmovl':
                    string = str(reg_s[reg_s.find('(')-1:reg_s.find('(')])
                    if reg_s.find('-') != -1:
                        string = '-'+ string
                    binline =  instr[ins_s] +  regs[reg_s.split(',')[0]] + \
                              regs[reg_s[reg_s.find('(')+1:reg_s.find(')')]] + string   
                elif ins_s == 'mrmovl':
                    string = str(reg_s[reg_s.find('(')-1:reg_s.find('(')])
                    if reg_s.find('-') != -1:
                        string = '-'+ string
                    binline =  instr[ins_s] +  regs[reg_s.split(',')[1]] + \
                              regs[reg_s[reg_s.find('(')+1:reg_s.find(')')]] + string

                else:
                    error += 'Line %d: Instruction "%s" not defined.\n' % (linepos, ins_s)
                    continue         
        except:
            error += 'Line %d: Invalid syntax.\n' % (linepos)    
        allbinline[linepos] = binline
        
    #write
    length = len(origline)
    for lineno in range(1, length):
        line=''
        try:
            line += addconverthex(lineaddress[lineno])
            line += ' : '
        except:
            pass
        try:
            line += instrconverthex(allbinline[lineno])
        except:
            pass
        while len(line) < 30:
            line += ' '
        line += '| '
        line += origline[lineno-1]
        OUTFILE.write(line)
    OUTFILE.close()

def main():
    print('Y86 compiler')
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
        dir = sys.argv[1].replace('.ys', '.yo')
        OUTFILE = open(dir, 'w')
    except:
        print ('invalid input file type')

    assemble(INFILE, OUTFILE)
    print 'compile success!'

if __name__ == '__main__':
    main()
