#!/usr/bin/env python3
import re
import mmap
import sys
import os
import argparse
import io
import glob

argparser = argparse.ArgumentParser(description="Convert the bbframes or cadu")
argparser.add_argument("INPUT", action="store", help="the file to process")
args = argparser.parse_args()

BBFRAME_HEADER_LEN = 10
BBFRAME_HEADER = b'\x71\x00\x00\x00\xA7\xD0\xFF\x00\x00\xC9'
SYNC = b'\x1A\xCF\xFC\x1D'
SYNC_LEN = 4
CADU_LEN = 2048

print("Purging bbframes/cadu - may take a while")
if os.path.exists("test.bin"):
   os.remove("test.bin")

#Remove bbheaders
with open(args.INPUT,'rb') as stream:
#with open(r'E:\DVB_stream\PluggerLocketGK-2AUHRIT.bin','rb') as stream:
    s = stream.read()
    pos = s.find(BBFRAME_HEADER)
    if pos < 0:
        print("No bbframes found - purging cadu")
        NewFile= open ("test.bin",'xb')	
        NewFile.write(s)
        NewFile.close()
    else:
        stream.seek(pos+BBFRAME_HEADER_LEN)
        CopyData = stream.read(5370)
		
        
		
		
        NewFile= open ("test.bin",'xb')	
        NewFile.write(CopyData)
		
        while pos >0:
          pos = s.find(BBFRAME_HEADER,pos+BBFRAME_HEADER_LEN)
          if pos <0:
            NewFile.close()
            break
          stream.seek(pos+BBFRAME_HEADER_LEN)
          CopyData = stream.read(5370)
          NewFile.write(CopyData)
		  
	  
#Remove sync + 2CRC
with open("test.bin",'rb') as t:
    u = t.read()
    pos = u.find(SYNC)
    
    t.seek(pos+SYNC_LEN+8)
    CopyData = t.read(2034)
	
    if os.path.exists("test2.bin"):
      os.remove("test2.bin")
	
	
    
    NewFile2= open("test2.bin",'xb')
    NewFile2.write(CopyData)
	
    while pos >0:
      pos = u.find(SYNC,pos+SYNC_LEN)
      if pos<0:
       NewFile2.close()
       break
      
      t.seek(pos+SYNC_LEN+8)
      CopyData = t.read(2034)
      NewFile2.write(CopyData)
      
print("Purging complete")	
	