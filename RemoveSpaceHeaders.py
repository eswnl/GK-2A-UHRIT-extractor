#!/usr/bin/env python3
import re
import mmap
import sys
import os



#CP_PDU
PRIMARY_SPACE_HEADER = b'\xA8' 
SPACE_HEADER_LENGTH = 14
SPACE_PACKET_CHECKBYTES = 4
EPOCH = b'\x23\x68' #"#h"
		

#Remove Space Headers
with open("test3.bin",'rb') as cp_pdu:
    byteData = cp_pdu.read()
    #Get uhrit file name by position
    uhritFileNamePos = byteData.find(b'IMG_')
    
    cp_pdu.seek(uhritFileNamePos)
    uhritFileName = cp_pdu.read(41)
    
    if os.path.exists(uhritFileName.decode('utf-8')):
      os.remove(uhritFileName.decode('utf-8'))
	
    NewFile = open(uhritFileName,'xb')
    print('creating '+ uhritFileName.decode('utf-8'))
    #cp_pdu.seek(0)
    cp_pdu.seek(8)
	
    i=1
    while i<1400:
      
        CopyData = cp_pdu.read(16372)
        
        NewFile.write(CopyData)
        cp_pdu.seek(SPACE_HEADER_LENGTH+SPACE_PACKET_CHECKBYTES,1) #start at current pos
		
        i=i+1
	
    NewFile.close()
	
	#Trim and begin primary header at 0th byte
with open(uhritFileName,'rb') as NewFile:    
    byteData = NewFile.read()
    HeaderStartPos = byteData.find(b'\x33\x47\x45\x4F\x53',0,100) - 27
    NewFile.seek(HeaderStartPos)
    CopyData = NewFile.read()
    NewFile = open(uhritFileName,'wb')
    NewFile.write(CopyData)	  