'''
Created on 2013-6-8

@author: rockyRocky
'''

from utils import *

# Signals
INOP = 0x0
IHALT = 0x1
IRRMOVL = 0x2
IIRMOVL = 0x3
IRMMOVL = 0x4
IMRMOVL= 0x5
IOPL = 0x6
IJXX = 0x7
ICALL = 0x8
IRET = 0x9
IPUSHL = 0xa
IPOPL = 0xb
IIADDL = 0xc
ILEAVE = 0xd
FNONE = 0x0
RESP = 0x4
REBP = 0x5
RNONE = 0x8
ALUADD = 0x0
ALUSUB = 0x1
ALUAND = 0x2
ALUXOR = 0x3
FJMP = 0x0
FJLE = 0x1
FJL = 0x2
FJE = 0x3
FJNE = 0x4
FJGE = 0x5
FJG = 0x6

# Registers encode
regname = {
    0x0: "%eax",
    0x1: "%ecx",
    0x2: "%edx",
    0x3: "%ebx",
    0x4: "%esp",
    0x5: "%ebp",
    0x6: "%esi",
    0x7: "%edi"
}

def getRegName(x):
        if x == RNONE:
            return '----'
        else:
            return regname[x]

instrname = {
    "00": "nop",
    "10": "halt",
    "20": "rrmovl",
    "21": "cmovle",
    "22": "cmovl",
    "23": "cmove",
    "24": "cmovne",
    "25": "cmovge",
    "26": "cmovg",
    "30": "irmovl",
    "40": "rmmovl",
    "50": "mrmovl",
    "60": "addl",
    "61": "subl",
    "62": "andl",
    "63": "xorl",
    "70": "jmp",
    "71": "jle",
    "72": "jl",
    "73": "je",
    "74": "jne",
    "75": "jge",
    "76": "jg",
    "80": "call",
    "90": "ret",
    "a0": "pushl",
    "b0": "popl",
    "c0": "iaddl",
    "d0": "leave"
}

def getInstrName(icode, ifun):
    s = int_to_hexStr(icode) + int_to_hexStr(ifun)
    if s in instrname:
        return instrname[s]
    return 'INS'

