@echo off
SET /p input= Channel?
Rem Input segments
SET /p m= FirstSegment(1-23)?
SET /p LastSegment= LastSegment(1-23)?
setlocal EnableDelayedExpansion
rem SET m=!FirstSegment!
set /a NoOfLoops = 1 + LastSegment - m
FOR /L %%i IN (1,1,!NoOfLoops!) DO (
if !m! LSS 10 (set n=0!m!) else (set n=!m!)
python GetSegment.py !input!_!n!.uhrit
python removespaceheaders.py
cd uhrit-rx\tools
python xrit-decrypt.py "%~dp0\uhrit-rx\EncryptionKeyMessage_001F2904C905.bin.dec" "%~dp0\!input!_!n!.uhrit"
python uhrit-img.py %~dp0\!input!_!n!.uhrit.dec"
set /a m+=1
cd..
cd..
)

del /s /q  %~dp0\*.uhrit
del /s /q  %~dp0\*.uhrit.dec