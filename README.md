# GK-2A-UHRIT-extractor
Use these files to extract images from UHRIT CADU and BBFRAMES from UHRIT transmissions.
# Introduction
GK-2A is a Korean Weather Satellite. It sends images every 10 minutes on L and X bands. L-band carries the LRIT and HRIT and X-band carries the UHRIT containing all 16 channels. The UHRIT encapsulates the data into BBFRAMES and sends them down as DVB-S2.
# Methods
There are 2 methods to get the DVB-S2 signal:
1. SDR<br>
   Later to be implemented, SatDump can demodulate and output the CADUs.
2. Using a commercial DVB-S2 receiver:<br>
   This is the method we will focus on here.
# Equipment needed
1. 1.5 - 1.8m dish
2. X-band feed
3. LNA (30-40 dB)
4. X-band downconverter to L-band
5. TBS6903x or later: Cards with USB will not transport the frames.
6. PC running EBSPro or BBFRAME collector.
