# setup.py
from distutils.core import setup  
import sys,os 
import py2exe  
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))+'\\compiler')
import assemble, start
import highlighter 

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))+'\\kernel')
from Simulator import *
from Memory import CACHESIZE, MEMSIZE, VMSIZE

Mydata_files = [('', ['E:\\github\\y86-simulator\\gui\\ps8.jpg'])]
setup(  
      windows=['y86.py'], 
	data_files = Mydata_files,	  
      options = {           
      "py2exe":  
       {"dll_excludes": ["MSVCP90.dll","ole32.dll","OLEAUT32.dll","USER32.dll","ADVAPI32.dll","SHELL32.dll","USER32.dll",
                                             "COMDLG32.dll","WSOCK32.dll","COMCTL32.dll","WSOCK32.dll","OLEAUT32.dll","WS2_32.dll","KERNEL32.dll",
                                             "GDI32.dll","RPCRT4.dll","KERNEL32.dll","ole32.dll","WINSPOOL.DRV","gdiplus.dll","WINMM.dll","ADVAPI32.dll",'IMM32.dll'],
	   "includes":["sip"]}  
       }  
) 

