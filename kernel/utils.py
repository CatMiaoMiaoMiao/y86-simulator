__author__ = 'rockyRocky'

# Utility
def str_to_byte(s):
    assert len(s) == 2, 'str_to_byte: s("%s") has length other than 2' % s
    high = int(s[0],16)
    low = int(s[1],16)
    return high*16 + low

def str_to_bytes(s):
    assert len(s) % 2 == 0, 'str_to_bytes: s(%s)" has odd length' %s
    return [ str_to_byte(s[i:i+2]) for i in range(0,len(s),2)]

def int_to_4_bytes(v):
    return [ (v>>(8*i))%(1<<8) for i in range(0,4) ]

def bytes_to_int(bytes): # already little endian
    r = sum( bytes[i]<<(8*i) for i in range(len(bytes)) )
    if (r >= 1<<31):
        return r-(1<<32)
    else:
        return r

def byte_pack(hi,lo):
    return ((hi&0xf)<<4) | (lo&0xf)

def hi4(p):
    return (p>>4)&0xf

def lo4(p):
    return p&0xf

def unsign(v):
    if v < 0:
        v += 2**32
    return v

def int_to_hexStr(x, m = 0):
    if x < 0:
        x = (~(-x) + 1) & 0xffffffff
    if m == 0:
        return "%x" % (x)
    else:
        return "%.*x" % (m, x)

def endianInt(s, isBigEndian=False):
    x = 0
    if isBigEndian:
        x = int(s, 16)
    else:
        x = int('%c%c%c%c%c%c%c%c' % (s[6], s[7], s[4], s[5], \
                                         s[2], s[3], s[0], s[1]), 16)
    if x > 0x7fffffff:
        x = -((~x + 1) & 0xffffffff)
    return x
