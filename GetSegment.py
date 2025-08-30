#!/usr/bin/env python3
import re
import mmap
import sys
import os
import argparse
import io
import glob

argparser = argparse.ArgumentParser(description="Input the desired segment")
argparser.add_argument("INPUT", action="store", help="the segment to process")
args = argparser.parse_args()
SegmentId = args.INPUT

if os.path.exists("test3.bin"):
   os.remove("test3.bin")
print(SegmentId)

   
with open("test2.bin",'rb') as t:
    
    u = t.read()
    pos = u.find(SegmentId.encode("utf-8"))
    
   
    pos = u.rfind("3GEOS".encode("utf-8"),0,pos)
        
    t.seek(pos-45)
    
    if ("VI005") in SegmentId:
      size = 22000001
	  #CopyData = t.read(22000001) #VI005, VI008
    elif ("VI008") in SegmentId:
      size = 22000001
    else:
      size = 22000000
      #CopyData = t.read(22000000) #VI004, VI006, NR016, WV073, SW038, NR013, NR016, WV063, WV069, WV073, IR087, IR096, IR105, IR112, IR123, IR133
    
    
    CopyData = t.read(size)
    #print(size)
    
    if os.path.exists("test3.bin"):
      os.remove("test3.bin")
	  
    NewFile = open("test3.bin",'xb')
    NewFile.write(CopyData)
    NewFile.close()
	
#RemoveNullBytes
for x in range(7):
  with open("test3.bin",'rb') as v:    
    w = v.read()
    StartOfNullBytesPos = w.find(b'\00\x00\x00\x00\x00\x00\x00\x00\x00\x00\00\x00\x00\x00\x00\x00\x00\x00\x00\x00\00\x00\x00\x00\x00\x00\x00\x00\x00\x00\00\x00\x00\x00\x00\x00\x00')
    if StartOfNullBytesPos > 0:
      
      print("Found null byte block - deleting!")
      
      v.seek(StartOfNullBytesPos)
      i = 0
      byteValue = v.read(1)
      while byteValue == b'\x00':
        i=i+1
        v.seek(StartOfNullBytesPos+i)
        byteValue = v.read(1)
      
      EndOfNullBytesPos = StartOfNullBytesPos+i
     
      v.seek(0)
      CopyDataA = v.read(StartOfNullBytesPos)
      v.seek(EndOfNullBytesPos)
	  
      
	  
      CopyDataB = v.read(-1)
      v.close()
	  
      with open("test3.bin",'wb') as v:	  
      
        v.write(CopyDataA+CopyDataB)     
	   #add padding bytes
        v.seek(0, 2)
        v.write(bytes(size-v.tell()))
		
