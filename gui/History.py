'''
Created on 2013-6-10

@author: rockyRocky
'''

import copy

from Simulator import *

class History:
    def __init__(self, maxSize=100):
        self.maxSize = maxSize
        self.list = [None]*maxSize
        self.size = 0
        
    def record(self, simulator):
        self.size += 1 if self.size<self.maxSize else 0
        self.list[simulator.cycle % self.maxSize] = copy.copy(simulator)
        
    def back(self, current):
        if self.size>0:
            self.size -= 1
            return copy.copy(self.list[(current-1) % self.maxSize])
        else:
            return False