'''
Created on 2013-6-13

@author: rockyRocky
'''

import math

from utils import *

class CacheLine:
    def __init__(self, cache):
        self.isValid = False
        self.isDirty = False
        self.tag = 0
        self.block = [0]*cache.b
        
class Cache:
    def __init__(self, S=64, E=1, B=16, m=15):
        assert m<=32
        self.S = S
        self.E = E
        self.B = B
        self.m = m
        self.s = int(math.log(S, 2))
        self.e = int(math.log(E, 2))
        self.b = int(math.log(B, 2))
        self.t = self.m - self.s - self.b
# don't simply use []*?, cause it simply copy the same address
        self.set = []
        for i in range(self.E*self.S):
            self.set.append(CacheLine(self))
# bad support for nested-loop list

#######
# api #
#######
    def getLine(self, si, ei):
        line = self.set[si*self.E+ei]
        return line.isValid, line.isDirty, line.tag, line.block
# end #    
#######
    def getSetIndex(self, addr):
        return extractBits(addr, self.t+32-self.m, self.b)
    
    def getTag(self, addr):
        return extractBits(addr, 32-self.m, self.b+self.s)    
    
    def getBlockOffset(self, addr):
        return extractBits(addr, 32-self.m+self.t+self.s, 0)
    
# placement policy is addr mod E    
    
    # if hit, return the byte; if miss, return False
    def getByte(self, addr):
        setIndex = self.getSetIndex(addr)
        entrySize = self.E
        tag = self.getTag(addr)
        blockOffset = self.getBlockOffset(addr)
        lineIndex = addr % self.E
        line = self.set[setIndex*entrySize+lineIndex]
        if (line.isValid and line.tag==tag):
            return line.block[blockOffset], True
        return False, False
    
    # if write hit, set byte, set dirty and return True
    # else return False
    def setByte(self, addr, byte):
        setIndex = self.getSetIndex(addr)
        entrySize = self.E
        lineIndex = addr % self.E
        tag = self.getTag(addr)
        blockOffset = self.getBlockOffset(addr)
        oldLine = self.set[setIndex*entrySize+lineIndex]
        # if conflict, replace and set dirty flag
        if (oldLine.isValid and oldLine.tag==tag):
            self.set[setIndex*entrySize+lineIndex].block[blockOffset] = byte
            self.set[setIndex*entrySize+lineIndex].isDirty = True
            return True # hit
        # not conflict, if not dirty than replace and return False
        # else replace and return block
        else:
            return False

    # if conflict and dirty return the addr of old line in mem
    # else return False
    def setBlock(self, addr, block):
        # find it first
        setIndex = self.getSetIndex(addr)
        entrySize = self.E
        lineIndex = addr % self.E
        tag = self.getTag(addr)
        blockOffset = self.getBlockOffset(addr)
        oldLine = self.set[setIndex*entrySize+lineIndex]
        if (oldLine.isValid and oldLine.isDirty): # if dirty
            # old with different tag only
            oldAddr = (oldLine.tag<<(self.s+self.b)) + (setIndex<<self.b)
            oldBlock = oldLine.block
            # update
            self.set[setIndex*entrySize+lineIndex].isValid = True
            self.set[setIndex*entrySize+lineIndex].isDirty = False
            self.set[setIndex*entrySize+lineIndex].tag = tag
            self.set[setIndex*entrySize+lineIndex].block = block
            return oldAddr, oldBlock, True
        else:
            self.set[setIndex*entrySize+lineIndex].isValid = True
            self.set[setIndex*entrySize+lineIndex].isDirty = False
            self.set[setIndex*entrySize+lineIndex].tag = tag
            self.set[setIndex*entrySize+lineIndex].block = block
            return False, False, False