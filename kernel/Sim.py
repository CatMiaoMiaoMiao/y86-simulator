'''
Created on 2013-6-17

@author: rockyRocky
'''

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

class Sim:
    def __init__(self):
        self.__ver__ = '0.0.1'
    # Pipeline self.register F
        self.F_predPC = 0
        self.F_stat = 'BUB'
        self.F_stall = False
        self.F_currentPC = -1

    # Intermediate Values in Fetch Stage
        self.f_icode = INOP
        self.f_ifun = FNONE
        self.f_valC = 0x0
        self.f_valP = 0x0
        self.f_rA = RNONE
        self.f_rB = RNONE
        self.f_predPC = 0
        self.f_stat = 'BUB'

    # Pipeline self.register D
        self.D_stat = 'BUB'
        self.D_icode = INOP
        self.D_ifun = FNONE
        self.D_rA = RNONE
        self.D_rB = RNONE
        self.D_valP = 0x0
        self.D_valC = 0x0
        self.D_bub = False
        self.D_stall = False
        self.D_currentPC = -1

    # Intermediate Values in Decode Stage
        self.d_srcA = RNONE
        self.d_srcB = RNONE
        self.d_dstE = RNONE
        self.d_dstM = RNONE
        self.d_valA = 0x0
        self.d_valB = 0x0

    # Pipeline self.register E
        self.E_stat = 'BUB'
        self.E_icode = INOP
        self.E_ifun = FNONE
        self.E_valC = 0x0
        self.E_srcA = RNONE
        self.E_valA = 0x0
        self.E_srcB = RNONE
        self.E_valB = 0x0
        self.E_dstE = RNONE
        self.E_dstM = RNONE
        self.E_bub = False
        self.E_currentPC = -1

    # Intermediate Values in Execute Stage
        self.e_valE = 0x0
        self.e_dstE = RNONE
        self.e_Cnd = False
        self.e_setcc = False

    # Pipeline self.register M
        self.M_stat = 'BUB'
        self.M_icode = INOP
        self.M_ifun = FNONE
        self.M_valA = 0x0
        self.M_dstE = RNONE
        self.M_valE = 0x0
        self.M_dstM = RNONE
        self.M_Cnd = False
        self.M_currentPC = -1

    # Intermediate Values in Memory Stage
        self.m_valM = 0x0
        self.m_stat = 'BUB'
        self.mem_addr = 0x0
        self.m_read = False
        self.dmem_error = False

    # Pipeline self.register W
        self.W_stat = 'BUB'
        self.W_icode = INOP
        self.W_ifun = FNONE
        self.W_dstE = RNONE
        self.W_valE = 0x0
        self.W_dstM = RNONE
        self.W_valM = 0x0
        self.W_currentPC = -1

    # self.registers
        self.register = {
            0x0: 0,
            0x1: 0,
            0x2: 0,
            0x3: 0,
            0x4: 0,
            0x5: 0,
            0x6: 0,
            0x7: 0,
            0x8: 0,
            0xf: 0
        }

    # CC code
        self.condcode = {
            'ZF': 1,
            'SF': 0,
            'OF': 0
        }
    # memory
        self.memory = Memory()

    # Global variables
        self.isBigEndian = False
        self.isSecond = False
        self.isGuimode = False
        self.isNoLogFile = False
        self.maxCycle = 32767
        self.cycle = 0
        self.cpustat = 'AOK'
        self.yasbin = ''
        self.isBin = False
        self.binlen = 0
        self.addrlen = 3
        self.logfile = None
        self.isOnScreen = False
        
        self.isGoing = True
        self.interval = 0.1
        self.isTerminated = False
        
    def copy(self, tmp):
            # Pipeline self.register F
        self.F_predPC = tmp.F_predPC
        self.F_stat = tmp.F_stat
        self.F_stall = tmp.F_stall
        self.F_currentPC = tmp.F_currentPC

    # Intermediate Values in Fetch Stage
        self.f_icode = tmp.f_icode
        self.f_ifun = tmp.f_ifun
        self.f_valC = tmp.f_valC
        self.f_valP = tmp.f_valP
        self.f_rA = tmp.f_rA
        self.f_rB = tmp.f_rB
        self.f_predPC = tmp.f_predPC
        self.f_stat = tmp.f_stat

    # Pipeline self.register D
        self.D_stat = tmp.D_stat
        self.D_icode = tmp.D_icode
        self.D_ifun = tmp.D_ifun
        self.D_rA = tmp.D_rA
        self.D_rB = tmp.D_rB
        self.D_valP = tmp.D_valP
        self.D_valC = tmp.D_valC
        self.D_bub = tmp.D_bub
        self.D_stall = tmp.D_stall
        self.D_currentPC = tmp.D_currentPC

    # Intermediate Values in Decode Stage
        self.d_srcA = tmp.d_srcA
        self.d_srcB = tmp.d_srcB
        self.d_dstE = tmp.d_dstE
        self.d_dstM = tmp.d_dstM
        self.d_valA = tmp.d_valA
        self.d_valB = tmp.d_valB

    # Pipeline self.register E
        self.E_stat = tmp.E_stat
        self.E_icode = tmp.E_icode
        self.E_ifun = tmp.E_ifun
        self.E_valC = tmp.E_valC
        self.E_srcA = tmp.E_srcA
        self.E_valA = tmp.E_valA
        self.E_srcB = tmp.E_srcB
        self.E_valB = tmp.E_valB
        self.E_dstE = tmp.E_dstE
        self.E_dstM = tmp.E_dstM
        self.E_bub = tmp.E_bub
        self.E_currentPC = tmp.E_currentPC

    # Intermediate Values in Execute Stage
        self.e_valE = tmp.e_valE
        self.e_dstE = tmp.e_dstE
        self.e_Cnd = tmp.e_Cnd
        self.e_setcc = tmp.e_setcc

    # Pipeline self.register M
        self.M_stat = tmp.M_stat
        self.M_icode = tmp.M_icode
        self.M_ifun = tmp.M_ifun
        self.M_valA = tmp.M_valA
        self.M_dstE = tmp.M_dstE
        self.M_valE = tmp.M_valE
        self.M_dstM = tmp.M_dstM
        self.M_Cnd = tmp.M_Cnd
        self.M_currentPC = tmp.M_currentPC

    # Intermediate Values in Memory Stage
        self.m_valM = tmp.m_valM
        self.m_stat = tmp.m_stat
        self.mem_addr = tmp.mem_addr
        self.m_read = tmp.m_read
        self.dmem_error = tmp.dmem_error

    # Pipeline self.register W
        self.W_stat = tmp.W_stat
        self.W_icode = tmp.W_icode
        self.W_ifun = tmp.W_ifun
        self.W_dstE = tmp.W_dstE
        self.W_valE = tmp.W_valE
        self.W_dstM = tmp.W_dstM
        self.W_valM = tmp.W_valM
        self.W_currentPC = tmp.W_currentPC

    # self.registers
        self.register = copy.copy(tmp.register)

    # CC code
        self.condcode = copy.copy(tmp.condcode)
    # memory
        self.memory = copy.deepcopy(tmp.memory)
        
    # Global variables
        self.isBigEndian = tmp.isBigEndian
        self.isSecond = tmp.isSecond
        self.isGuimode = tmp.isGuimode
        self.isNoLogFile = tmp.isNoLogFile
        self.maxCycle = tmp.maxCycle
        self.cycle = tmp.cycle
        self.cpustat = tmp.cpustat
        self.yasbin = tmp.yasbin
        self.isBin = tmp.isBin
        self.binlen = tmp.binlen
        self.addrlen = tmp.addrlen
        self.logfile = tmp.logfile
        self.isOnScreen = tmp.isOnScreen
        
        self.isGoing = False
        self.interval = tmp.interval
        self.isTerminated = tmp.isTerminated
                    

        
