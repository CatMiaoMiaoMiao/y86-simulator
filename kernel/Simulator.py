__author__ = 'rockyRocky'

import os
import re
import binascii
import copy
import time

from utils import *
from constants import *
from Memory import *
from History import *
from Sim import *

class Simulator(Sim):
    def __init__(self):
        Sim.__init__(self)
        self.history = History()
                    
    def handleErr(self, desc): # TODO:
        return
    
    def simLog(self, s):
        if self.isGuimode:
            return
        if self.logfile != None:
            self.logfile.write("%s\n" % (s))
        if self.isOnScreen or self.logfile == None:
            print s
            return

    def showStatTitle(self):  
        if self.isGuimode:
            return
        self.simLog('Cycle_%d' % self.cycle)
        self.simLog('--------------------')
        
    def showStat(self):
        if self.isGuimode:
            return
        self.simLog('FETCH:')
        self.simLog('\tF_predPC \t= 0x%s\n' % int_to_hexStr(self.F_predPC, 8))
        
        self.simLog('DECODE:')
        self.simLog('\tD_icode  \t= 0x%s' % int_to_hexStr(self.D_icode))
        self.simLog('\tD_ifun   \t= 0x%s' % int_to_hexStr(self.D_ifun))
        self.simLog('\tD_rA     \t= 0x%s' % int_to_hexStr(self.D_rA))
        self.simLog('\tD_rB     \t= 0x%s' % int_to_hexStr(self.D_rB))
        self.simLog('\tD_valC   \t= 0x%s' % int_to_hexStr(self.D_valC, 8))
        self.simLog('\tD_valP   \t= 0x%s\n' % int_to_hexStr(self.D_valP, 8))
        
        self.simLog('EXECUTE:')
        self.simLog('\tE_icode  \t= 0x%s' % int_to_hexStr(self.E_icode))
        self.simLog('\tE_ifun   \t= 0x%s' % int_to_hexStr(self.E_ifun))
        self.simLog('\tE_valC   \t= 0x%s' % int_to_hexStr(self.E_valC, 8))
        self.simLog('\tE_valA   \t= 0x%s' % int_to_hexStr(self.E_valA, 8))
        self.simLog('\tE_valB   \t= 0x%s' % int_to_hexStr(self.E_valB, 8))
        self.simLog('\tE_dstE   \t= 0x%s' % int_to_hexStr(self.E_dstE))
        self.simLog('\tE_dstM   \t= 0x%s' % int_to_hexStr(self.E_dstM))
        self.simLog('\tE_srcA   \t= 0x%s' % int_to_hexStr(self.E_srcA))
        self.simLog('\tE_srcB   \t= 0x%s\n' % int_to_hexStr(self.E_srcB))
        
        self.simLog('MEMORY:')
        self.simLog('\tM_icode  \t= 0x%s' % int_to_hexStr(self.M_icode))
        self.simLog('\tM_Bch    \t= %s' % self.M_Cnd)
        self.simLog('\tM_valE   \t= 0x%s' % int_to_hexStr(self.M_valE, 8))
        self.simLog('\tM_valA   \t= 0x%s' % int_to_hexStr(self.M_valA, 8))
        self.simLog('\tM_dstE   \t= 0x%s' % int_to_hexStr(self.M_dstE))
        self.simLog('\tM_dstM   \t= 0x%s\n' % int_to_hexStr(self.M_dstM))
        
        self.simLog('WRITE BACK:')
        self.simLog('\tW_icode  \t= 0x%s' % int_to_hexStr(self.W_icode))
        self.simLog('\tW_valE   \t= 0x%s' % int_to_hexStr(self.W_valE, 8))
        self.simLog('\tW_valM   \t= 0x%s' % int_to_hexStr(self.W_valM, 8))
        self.simLog('\tW_dstE   \t= 0x%s' % int_to_hexStr(self.W_dstE))
        self.simLog('\tW_dstM   \t= 0x%s\n' % int_to_hexStr(self.W_dstM))
    
    def pipeCtr(self):
        # F_stall
        if IRET in (self.D_icode, self.E_icode, self.M_icode) or \
            (self.E_icode in (IMRMOVL, IPOPL) and \
            self.E_dstM in (self.d_srcA, self.d_srcB)):
            self.F_stall = True
            
        # D_stall and D_bub
        if self.E_icode in (IMRMOVL, IPOPL) and self.E_dstM in (self.d_srcA, self.d_srcB):
            self.D_stall = True # stall
        elif (self.E_icode==IJXX and not self.e_Cnd) or \
            not (self.E_icode in (IMRMOVL, IPOPL) and self.E_dstM in (self.d_srcA, self.d_srcB)) \
            and IRET in (self.D_icode, self.E_icode, self.M_icode):
            self.D_bub = True
            
        # E_bub
        if (self.E_icode == IJXX and not self.e_Cnd) or \
            self.E_icode in (IMRMOVL, IPOPL) and \
            self.E_dstM in (self.d_srcA, self.d_srcB):
            self.E_bub = True
    
    def writeF(self):
        if self.F_stall:
            self.F_stall = False
            return  # stall
        self.F_currentPC = self.F_predPC
        self.F_predPC = self.f_predPC
        self.F_stat = 'AOK'

    def stageF(self):
        f_pc = self.F_predPC

        if self.M_icode == IJXX and not self.M_Cnd:
            f_pc = self.M_valA
        elif self.W_icode == IRET:
            f_pc = self.W_valM
        old_pc = f_pc
        pcstart = f_pc * 2
        imem_error = False
        instr = self.memory.getByte(f_pc)
        imem_icode = hi4(instr)
        imem_ifun = lo4(instr)
        if self.isSecond:
            if imem_icode == 0x1:
                imem_icode = INOP
            elif imem_icode == 0x0:
                imem_icode = IHALT
        pcstart += 2
        f_pc += 1
        self.f_icode = INOP if imem_error else imem_icode
        self.f_ifun = FNONE if imem_error else imem_ifun
        instr_valid =  self.f_icode in (INOP, IHALT, IRRMOVL, IIRMOVL, IRMMOVL, IMRMOVL, \
                                   IOPL, IJXX, ICALL, IRET, IPUSHL, IPOPL, IIADDL, ILEAVE)
        if instr_valid:
            try:
                if self.f_icode in (IRRMOVL, IOPL, IPUSHL, IPOPL, \
                               IIRMOVL, IRMMOVL, IMRMOVL, IIADDL):
                    regids = self.memory.getByte(f_pc)
                    self.f_rA = hi4(regids)
                    self.f_rB = lo4(regids)
                    if self.isSecond:
                        if self.f_rA == 0xf:
                            self.f_rA = RNONE
                        if self.f_rB == 0xf:
                            self.f_rB = RNONE
                    pcstart += 2
                    f_pc += 1
                else:
                    self.f_rA = RNONE
                    self.f_rB = RNONE
                if (self.f_rA not in regname.keys() and self.f_rA != RNONE) or \
                    (self.f_rB not in regname.keys() and self.f_rB != RNONE):
                    imem_error = True
            except:
                imem_error = True
            self.f_valC = 0x0
            try:
                if self.f_icode in (IIRMOVL, IRMMOVL, IMRMOVL, IJXX, ICALL, IIADDL):
                    self.f_valC = self.memory.getWord(f_pc)
                    pcstart += 8
                    f_pc += 4
            except:
                imem_error = True
        if not instr_valid:
            self.handleErr({'what':'instr-not-valid', 'imem_icode':imem_icode, \
                            'imem_ifun':imem_ifun})
        self.f_valP = f_pc
        self.f_predPC = self.f_valC if self.f_icode in (IJXX, ICALL) else self.f_valP         
        self.f_stat = 'AOK'
        if imem_error:
            self.f_stat = 'ADR'
        if not instr_valid:
            self.f_stat = 'INS'
        if self.f_icode == IHALT:
            self.f_stat = 'HLT'

    def writeD(self):
        if self.D_stall:
            self.D_stall = False
            return
        if self.D_bub:
            self.D_bub = False
            self.D_icode = INOP
            self.D_ifun = FNONE
            self.D_rA = RNONE
            self.D_rB = RNONE
            self.D_valC = 0x0
            self.D_valP = 0x0
            self.D_stat = 'BUB'
            return
        self.D_stat = self.f_stat
        self.D_icode = self.f_icode
        self.D_ifun = self.f_ifun
        self.D_rA = self.f_rA
        self.D_rB = self.f_rB
        self.D_valC = self.f_valC
        self.D_valP = self.f_valP
        self.D_currentPC = self.F_currentPC

    def stageD(self):
        self.d_srcA = RNONE
        if self.D_icode in (IRRMOVL, IRMMOVL, IOPL, IPUSHL):
            self.d_srcA = self.D_rA
        elif self.D_icode in (IPOPL, IRET):
            self.d_srcA = RESP
        elif self.D_icode == ILEAVE:
            self.d_srcA = REBP
        self.d_srcB = RNONE
        if self.D_icode in (IOPL, IRMMOVL, IMRMOVL, IIADDL):
            self.d_srcB = self.D_rB
        elif self.D_icode in (IPUSHL, IPOPL, ICALL, IRET):
            self.d_srcB = RESP
        self.d_dstE = RNONE
        if self.D_icode in (IRRMOVL, IIRMOVL, IOPL, IIADDL):
            self.d_dstE = self.D_rB
        elif self.D_icode in (IPUSHL, IPOPL, ICALL, IRET, ILEAVE):
            self.d_dstE = RESP
        self.d_dstM = RNONE
        if self.D_icode in (IMRMOVL, IPOPL):
            self.d_dstM = self.D_rA
        elif self.D_icode == ILEAVE:
            self.d_dstM = REBP
        self.d_valA = self.register[self.d_srcA]
        if self.D_icode in (ICALL, IJXX):
            self.d_valA = self.D_valP
        elif self.d_srcA == self.e_dstE:
            self.d_valA = self.e_valE
        elif self.d_srcA == self.M_dstM:
            self.d_valA = self.m_valM
        elif self.d_srcA == self.M_dstE:
            self.d_valA = self.M_valE
        elif self.d_srcA == self.W_dstM:
            self.d_valA = self.W_valM
        elif self.d_srcA == self.W_dstE:
            self.d_valA = self.W_valE
        self.d_valB = self.register[self.d_srcB]
        if self.d_srcB == self.e_dstE:
            self.d_valB = self.e_valE
        elif self.d_srcB == self.M_dstM:
            self.d_valB = self.m_valM
        elif self.d_srcB == self.M_dstE:
            self.d_valB = self.M_valE
        elif self.d_srcB == self.W_dstM:
            self.d_valB = self.W_valM
        elif self.d_srcB == self.W_dstE:
            self.d_valB = self.W_valE

    def writeE(self):
        if self.E_bub:
            self.E_bub = False
            self.E_icode = INOP
            self.E_ifun = FNONE
            self.E_valC = 0x0
            self.E_valA = 0x0
            self.E_valB = 0x0
            self.E_dstE = RNONE
            self.E_dstM = RNONE
            self.E_srcA = RNONE
            self.E_srcB = RNONE
            self.E_stat = 'BUB'
            return
        self.E_stat = self.D_stat
        self.E_icode = self.D_icode
        self.E_ifun = self.D_ifun
        self.E_valC = self.D_valC
        self.E_valA = self.d_valA
        self.E_valB = self.d_valB
        self.E_dstE = self.d_dstE
        self.E_dstM = self.d_dstM
        self.E_srcA = self.d_srcA
        self.E_srcB = self.d_srcB
        self.E_currentPC = self.D_currentPC

    def stageE(self):
        aluA = 0
        if self.E_icode in (IRRMOVL, IOPL, ILEAVE):
            aluA = self.E_valA
        elif self.E_icode in (IIRMOVL, IRMMOVL, IMRMOVL, IIADDL):
            aluA = self.E_valC
        elif self.E_icode in (ICALL, IPUSHL):
            aluA = -4
        elif self.E_icode in (IRET, IPOPL):
            aluA = 4
        aluB = 0
        if self.E_icode in (IRMMOVL, IMRMOVL, IOPL, ICALL, \
                       IPUSHL, IRET, IPOPL, IIADDL):
            aluB = self.E_valB
        elif self.E_icode == ILEAVE:
            aluB = 4
        alufun = self.E_ifun if self.E_icode == IOPL else ALUADD
        alures = 0
        aluchar = '+'
        if alufun == ALUADD:
            alures = aluB + aluA
            aluchar = '+'
        elif alufun == ALUSUB:
            alures = aluB - aluA
            aluchar = '-'
        elif alufun == ALUAND:
            alures = aluB & aluA
            aluchar = '&'
        elif alufun == ALUXOR:
            alures = aluB ^ aluA
            aluchar = '^'
        self.e_setcc =  self.E_icode in (IOPL, IIADDL) and \
                   self.m_stat not in ('ADR', 'INS', 'HLT') and \
                   self.W_stat not in ('ADR', 'INS', 'HLT')
        if self.e_setcc:
            self.condcode['ZF'] = 1 if alures == 0 else 0
            self.condcode['SF'] = 1 if alures < 0 else 0
            self.condcode['OF'] = 0
            if (self.E_ifun == ALUADD) and \
                ((aluB > 0 and aluA > 0 and alures < 0) or \
                  aluB < 0 and aluB < 0 and alures > 0):
                self.condcode['OF'] = 1
            if (self.E_ifun == ALUSUB) and \
                ((aluB > 0 and aluA < 0 and alures < 0) or \
                  aluB < 0 and aluB > 0 and alures > 0):
                self.condcode['OF'] = 1
        self.e_Cnd = False
        if self.E_icode == IJXX or self.E_icode == IRRMOVL:
            zf = self.condcode['ZF']
            sf = self.condcode['SF']
            of = self.condcode['OF']
            if self.E_ifun == FJMP:
                self.e_Cnd = True
            elif self.E_ifun == FJLE and (sf ^ of) | zf == 1:
                self.e_Cnd = True
            elif self.E_ifun == FJL and sf ^ of == 1:
                self.e_Cnd = True
            elif self.E_ifun == FJE and zf == 1:
                self.e_Cnd = True
            elif self.E_ifun == FJNE and zf == 0:
                self.e_Cnd = True
            elif self.E_ifun == FJGE and sf ^ of == 0:
                self.e_Cnd = True
            elif self.E_ifun == FJG and (sf ^ of) | zf == 0:
                self.e_Cnd = True
        self.e_valE = alures
        self.e_dstE = self.E_dstE
        if self.E_icode == IRRMOVL and not self.e_Cnd:
            self.e_dstE = RNONE

    def writeM(self):
        if self.m_stat in ('ADR', 'INS', 'HLT') or \
            self.W_stat in ('ADR', 'INS', 'HLT'):
            self.M_stat = 'BUB'
            self.M_icode = INOP
            self.M_ifun = FNONE
            self.M_Cnd = False
            self.M_valE = 0x0
            self.M_valA = 0x0
            self.M_dstE = RNONE
            self.M_dstM = RNONE
            return
        self.M_stat = self.E_stat
        self.M_icode = self.E_icode
        self.M_ifun = self.E_ifun
        self.M_Cnd = self.e_Cnd
        self.M_valE = self.e_valE
        self.M_valA = self.E_valA
        self.M_dstE = self.e_dstE
        self.M_dstM = self.E_dstM
        self.M_currentPC = self.E_currentPC

    def stageM(self):
        self.m_valM = 0
        self.mem_addr = 0
        self.dmem_error = False
        if self.M_icode in (IRMMOVL, IPUSHL, ICALL, IMRMOVL): # write
            self.mem_addr = self.M_valE
        elif self.M_icode in (IPOPL, IRET, ILEAVE): # read, get addr
            self.mem_addr = self.M_valA
        if self.M_icode in (IMRMOVL, IPOPL, IRET, ILEAVE): # read
            try:
                self.m_valM = self.memory.getWord(self.mem_addr)
                self.m_read = True
            except:
                self.dmem_error = True
        if self.M_icode in (IRMMOVL, IPUSHL, ICALL): # write
            try:
                self.memory.setWord(self.mem_addr, self.M_valA)
            except:
                self.dmem_error = True
        self.m_stat = 'ADR' if self.dmem_error else self.M_stat

    def writeW(self):
        if self.W_stat in ('ADR', 'INS', 'HLT'):
            return
        self.W_stat = self.m_stat
        self.W_icode = self.M_icode
        self.W_ifun = self.M_ifun
        self.W_valE = self.M_valE
        self.W_valM = self.m_valM
        self.W_dstE = self.M_dstE
        self.W_dstM = self.M_dstM
        self.W_currentPC = self.M_currentPC

    def stageW(self):
        if self.W_dstE != RNONE:
            self.register[self.W_dstE] = self.W_valE
        if self.W_dstM != RNONE:
            self.register[self.W_dstM] = self.W_valM
        self.cpustat = 'AOK' if self.W_stat == 'BUB' else self.W_stat

    def step(self):
        if self.maxCycle != 0 and self.cycle > self.maxCycle:
            self.simLog('Reach Max Cycle')
            self.cpustat = 'HLT'
            return       
        self.showStatTitle()
        self.pipeCtr()
        
        self.writeW() # take care of orders if u wanna save some intermediate vals
        self.writeM()
        self.writeE()
        self.writeD()
        self.writeF()
        
        self.stageW()
        self.stageM()
        self.stageE()
        self.stageD()
        self.stageF()
        self.showStat()
        self.history.record(self)
        self.cycle += 1
        
        if self.cpustat != 'AOK' and self.cpustat != 'BUB':
            self.isTerminated = True
            return False
        else: 
            return True
    
    def back(self):
        tmp = self.history.back(self.cycle-1)
        if tmp==False or tmp==None:
            self.simLog('out of history\'s reach')
            return
        else:
            self.isTerminated = False
            self.copy(tmp)
            self.showStatTitle()
            self.showStat()
            self.cycle += 1
            
        
    def load(self, fin, fout=None):
        # prepare    
        self.cycle = 0
        self.yasbin = ''
        inputName = fin.name
        prefixName = os.path.splitext(inputName)[0]
        if fout==None and not self.isNoLogFile:
            outputName = prefixName + '.txt'
            try:
                self.logfile = open(outputName, 'w')
            except IOError:
                self.handleErr({'what':'cannot open a logfile to write'})
                raise
        else:
            self.logfile = fout
            outputName = fout.name
        if not self.isNoLogFile and not self.isGuimode:
            print('Log file: %s' % (outputName))
            
        # load    
        # TODO: how to load both bin and non-bin
        for str_line in fin.readlines():
            str_valid = str_line
            str_valid = re.sub(r'\|.*','',str_valid)
            str_valid = str_valid.strip(' \n\r\t')
            if str_valid == '':
                continue
            tokens = str_valid.split(':')
            if tokens[1] == '':
                continue
            addr = int(tokens[0].strip(' '), 16)
            content_str = tokens[1].strip(' ')
            self.yasbin += content_str
            content_bytes = str_to_bytes(content_str)
            self.memory.setBytesThrough( addr, content_bytes)
        self.binlen = len(self.yasbin)   
        
    def run(self):
        try:       
            while True:
                if self.isGoing:
                    if not self.step():
                        break
                    time.sleep(self.interval)
            self.logfile.close()
        except:
            self.simLog('Error: bad input binary file')
            self.logfile.close()
            raise
        
    def getMemory(self, addr):
        return self.memory.mem[addr]
    
    def getMemoryChange(self):
        return self.memory.memChange    
            
    def getCache(self, setIndex, lineIndex):
        entrySize = self.memory.cache.E
        line = self.memory.cache.set[setIndex*entrySize+lineIndex]
        return line.isValid, line.isDirty, line.tag, line.block

    def setCacheParams(self, S, E, B, m):
        self.memory.setCache(S, E, B, m)
        
    '''''''''''''''''
    '    trivial    '
    '''''''''''''''''        

        
