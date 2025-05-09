# GK-2A-UHRIT-extractor
Use these files to extract images from CADU and BBFRAMES from UHRIT transmissions.
# Introduction
GK-2A is a Korean Weather Satellite. It sends images every 10 minutes on L and X bands. L-band carries the LRIT and HRIT and X-band carries the UHRIT containing all 16 channels. The UHRIT encapsulates the data into BBFRAMES and sends them down as DVB-S2. The modulation parameters:<br>
![uhrit](https://github.com/user-attachments/assets/7c35c882-6073-4152-954f-cb345af9dbba)

# Methods for getting DVB-S2
There are 2 methods to get the DVB-S2 signal:
1. SDR<br>
   SatDump can demodulate DVB-S2. See: https://www.satdump.org/
   ![SatDump](https://github.com/user-attachments/assets/31bf75a3-d5ca-4e62-ad80-0b38b10400e9)

3. Using a commercial DVB-S2 receiver. The advantage is that a hardware DVB-S2 receiver can afford the user smaller dishes due to better lock at lower SNR. If using laptop you will need a PCI to SmartExpress socket (if your laptop has one)<p>
   ![image](https://github.com/user-attachments/assets/92f19a46-60df-4a15-94b2-1e21b97f5998)
# Methods for decoding images
1. SatDump - no decoder available
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
The first task is to remove the bbheaders and join the frames. Make a folder for your work e.g. `E:\SDR\GK-2A\UHRIT`. Copy the python files `new.py` and `RemoveSpaceHeaders.py` to this folder. 

<br>Goto DOS prompt and run `python new.py "path and name to the transport stream.ts"` which will produce an output file `test2.bin` in your folder. For example:
`E:\SDR\GK-2A\UHRIT>python new.py "E:\DVB_stream\0.0E_1070.011_H_15622_(2025-04-12 16.16.48)_dump.ts"`
<br>
Goto a hexeditor and open `test2.bin`. This contains all 23 segments per channel for which there are 16.<br>
## How to extract from CADU
If are using an SDR and software (e.g. Satdump) that receives and demodulates the DVB-S2 signal, or skips the BBFRAMES and outputs the CADU directly, the above code will also work. You just need to type:
`E:\SDR\GK-2A\UHRIT>python new.py "E:\file.cadu"`

# Get the segment
Goto the beginning of the segment ("3GEOS" marks the start, so always search this). Put the cursor after the "÷" sign.
Then from here select all the bytes until you reach the null bytes (the dots) preceeding the next segment. Note the "3GEOS" marking the start of the next segment.<br>
<br>
![image](https://github.com/user-attachments/assets/0dcd07c9-4881-43cc-890e-10324de94c87)
![image](https://github.com/user-attachments/assets/52fc925f-169f-450c-a134-4b5363c926cd)

Note I use HxD hex editor (https://mh-nexus.de/en/hxd/). There are some useful shortcuts, e.g. 
1. Alt+Insert copies the current offset position.
2. Ctrl+E allows you to select data range using that offset as a starting point (paste in the offset)<br>

![image](https://github.com/user-attachments/assets/c97266f6-4028-48e1-8480-d135e3b8d5a9)

Copy the selection and paste in a new file. Save as "test3.bin" to the usual folder.
Goto dos prompt and run `python removespaceheaders.py`. It should output a uhrit file such as:
`IMG_FD_043_VI004_20250412_071736_18.uhrit`

# Decryption and image
At this point, you can use Sam's (VKSDR) code to produce the output images in a similar fashion to LRIT and HRIT. Unfortunately, SatDump cannot work with .xrit files, so this process needs to be done manually.
<br>See the github site:
https://github.com/sam210723/xrit-rx<br>
1. Open `lrit-img.py` and change the image format. UHRIT image format uses jpeg2000 format. If you open "lrit-img.py" and edit the part as follows.<br>
![image](https://github.com/user-attachments/assets/3b305359-aad4-4544-96f5-ff932a461fae)
1. Run `python xrit-decrypt.py` to decrypt the uhrit file.<br>
   The command is `python xrit-decrypt.py <decrypted key message name(file.bin.dec)> <uhrit file(.uhrit)>`
3. Run `python lrit-img.py` to output the image file.<br>
   The command is `python lrit-img.py <decrypted uhrit file (uhrit.dec)>`
# Results
The above procedure will result in just one segment. If you have the time, you can decode all 23 segments in a channel. Unfortunately I have not managed to automate this part. <br>Also if you want full RGB images, you will need the VI004, VI005, VI006 channel contributions.<br>
The below images have been produced using 2 segments - which is good enough to get high resolution images.<br>
![lab-compose3](https://github.com/user-attachments/assets/68579833-3bc5-4cfa-9de9-abc7273a8683)<p>
![image](https://github.com/user-attachments/assets/d313bdad-8e7a-46a6-a971-248e67d46237)<p>
![image](https://github.com/user-attachments/assets/5e6a076f-022b-4765-930d-c72e0da298f0)<p>
![image](https://github.com/user-attachments/assets/5cfb1861-a25d-4ff9-aa56-d57da0c89528)<p>
![image](https://github.com/user-attachments/assets/eed05f50-1810-4a9f-aa68-915ca2960663)<p>
![image](https://github.com/user-attachments/assets/e60a1876-a401-4f73-8956-64492ec53154)<p>



## Getting full (22k) resolution RGB.
The UHRIT data contains 1 channel at 22k resolution (VI006). A technique used in LandSat imagery allows you full 22k resolution RGB images, if the high resolution channel is mapped onto the lower resolution RGB image. The advantage is that you only need one channel to be at high resolution.


