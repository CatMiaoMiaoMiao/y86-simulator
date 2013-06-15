__author__ = 'rockyRocky'

from utils import *
from Cache import *

CACHESIZE = 1024; # 1KB
MEMSIZE = 32*1024; # 32KB
VMSIZE = 1024*1024 # 1MB

# using write-back cache

class Memory:
    def __init__(self, size=MEMSIZE):
        self.size = size
        self.mem = [0]*size
        self.cache = Cache()
    
    def setCache(self, S, E, B, m):
        self.mem.extend([0]*((1>>m)-self.size))
#         self.cache.S = S
#         self.cache.E = E
#         self.cache.B = B
#         self.cache.m = m
        self.cache = Cache(S, E, B, m)
        
    def handleCacheMiss(self, addr):   
        blockOffset = self.cache.b # block offset
        blockSize = self.cache.B
        blockAddr = (addr >> blockOffset) << blockOffset
        # try fetching old blockAddr
        oldBlockAddr, oldBlock, isDirty = self.cache.setBlock(blockAddr, \
                                    [self.mem[blockAddr+i] for i in range(blockSize)])
        # if dirty
        if isDirty:  
            # get blockAddr, block, blockOffset, setOffset from line
            for (i, byte) in enumerate(oldBlock):
                self.mem[oldBlockAddr+i] = byte     
        
# api
# getters
    def getByte(self, addr):
        # bad access
        if addr<0 or addr>=len(self.mem):
            self.handleBadAccess()
            return False
        byte, isHit = self.cache.getByte(addr)
        # cache hit
        if isHit:
            return byte
        # cache miss
        self.handleCacheMiss(addr)
            # if not dirty, simply return the byte    
        byte, isHit = self.cache.getByte(addr)
        return byte

    def getBytes(self, addr, length):
        return [self.getByte(addr+i) for i in range(length)]

    def getWord(self, addr):
        return bytes_to_int(self.getBytes(addr, 4))

#############
# strategy of setting byte is
# to check it whether it is in cache
# if it is, 1 modify it in the cache, 2 set the dirty flag
# if not,  

# setters
    def setByte(self, addr, byte):
        if addr<0 or addr>=len(self.mem):
            self.handleBadAccess()
            return False
        isHit = self.cache.setByte(addr, byte)
        if not isHit:
            self.handleCacheMiss(addr)
            self.cache.setByte(addr, byte)

    def setBytes(self, addr, bytes):
        for (i, byte) in enumerate(bytes):
            self.setByte(addr+i, byte)

    def setWord(self, addr, word):
        self.setBytes(addr, int_to_4_bytes(word))

#### no cache version ####
       
    def setByteThrough(self, addr, byte):
        if addr<0 or addr>=len(self.mem):
            self.handleBadAccess()
            return False
        self.mem[addr] = byte 
        
    def setBytesThrough(self, addr, bytes):
        for (i, byte) in enumerate(bytes):
            self.setByteThrough(addr+i, byte)
        
# exception handler
    def handleBadAccess(self):
        # TODO:
        return
