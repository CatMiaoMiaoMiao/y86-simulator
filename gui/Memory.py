__author__ = 'rockyRocky'

from utils import *

CACHESIZE = 1000; # 1KB
MEMSIZE = 32*1000; # 32KB
VMSIZE = 1000*1000 # 1MB

class Memory:
    def __init__(self, size=MEMSIZE):
        self.mem = [0]*size

# api
# getters
    def getByte(self, addr):
        if addr<0 or addr>=len(self.mem):
            self.handleBadAccess()
        else:
            return self.mem[addr]

    def getBytes(self, addr, length):
        return [self.getByte(addr+i) for i in range(length)]

    def getWord(self, addr):
        return bytes_to_int(self.getBytes(addr, 4))

# setters
    def setByte(self, addr, byte):
        if addr<0 or addr>=len(self.mem):
            self.handleBadAccess()
        else:
            self.mem[addr] = byte

    def setBytes(self, addr, bytes):
        for (i, byte) in enumerate(bytes):
            self.setByte(addr+i, byte)

    def setWord(self, addr, word):
        self.setBytes(addr, int_to_4_bytes(word))
        
# exception handler
    def handleBadAccess(self):
        # TODO:
        return
