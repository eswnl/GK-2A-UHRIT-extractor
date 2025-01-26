# GK-2A-UHRIT-extractor
Use these files to extract images from CADU and BBFRAMES from UHRIT transmissions.
# Introduction
GK-2A is a Korean Weather Satellite. It sends images every 10 minutes on L and X bands. L-band carries the LRIT and HRIT and X-band carries the UHRIT containing all 16 channels. The UHRIT encapsulates the data into BBFRAMES and sends them down as DVB-S2. The modulation parameters:<br>
![uhrit](https://github.com/user-attachments/assets/7c35c882-6073-4152-954f-cb345af9dbba)

# Methods for getting DVB-S2
There are 2 methods to get the DVB-S2 signal:
1. SDR<br>
   SatDump can demodulate DVB-S2. See: https://www.satdump.org/
2. Using a commercial DVB-S2 receiver. The advantage is that a hardware DVB-S2 receiver can afford the user to smaller dishes due to better lock at lower SNR. If using laptop you will need a PCI to SmartExpress socket (if your laptop has one)<p>
   ![image](https://github.com/user-attachments/assets/92f19a46-60df-4a15-94b2-1e21b97f5998)
# Methods for decoding images
1. SatDump - decoder is work in progress
2. Python scripts - this is the method we will look at here. These simple scripts will simply locate the image portions without any error checking. But if your SNR is plenty and the DVB-S2 is doing its error correction, this method should be able to get images with no problem.
# Equipment needed
1. 1.5m or larger prime dish. A mesh dish with holes no larger 4mm will also work (1/10 lambda rule).
2. X-band feed. Make one or buy commercial version + teflon for circular polarisation.<br>
   See: https://www.a-centauri.com/articoli/an-x-band-primer
4. LNA (30-40 dB) - buy from used sellers like ebay.
5. X-band downconverter to L-band<br>
   My version is from https://m0kds.com/
7. TBS6903x or later: Receivers with USB will not be able to transport the frames.<br>
   If using laptop you will need a PCI to SmartExpress socket (if your laptop has one)
   

9. PC running EBSPro or BBFRAME collector. Make sure your card supports BBFRAMES and set this in the ini file. In EBSPro, the line in the ini file needs to say:
   `FrameMode=1`<p>
    ![tbs6903x_4](https://github.com/user-attachments/assets/52d2771d-7deb-4aa5-94a5-ce1048592547)

# Video
Watch this video to get an overview:<br>
https://youtu.be/yJCwNY3K8kQ
# How to extract from BBFRAMES
BBFrames is the first layer output by the TBS6903x. The UHRIT files are located directly inside. Infact, you can see the bbframe headers when you inspect the output.<p>
![BBheader](https://github.com/user-attachments/assets/115ec0f4-57ef-48aa-ad3f-1d8759176d04)
<p>The first task is to remove the bbheaders and join them. Make a folder for your work e.g. `E:\SDR\GK-2A\UHRIT`. Copy the python files `new.py` and `RemoveSpaceHeaders.py` to this folder. Next is to purge the headers for bbframes and the CADU.
Open `new.py` and insert the name of your bbframes as shown.

   ![image](https://github.com/user-attachments/assets/22fa663f-b05f-48f4-b26f-4dc5aa0a3cf8)



   

