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

3. Using a commercial DVB-S2 receiver. The advantage is that a hardware DVB-S2 receiver can afford the user smaller dishes due to better lock at lower SNR. If using laptop you will need a PCI to ExpressCard (if your laptop has one).<p>
   ![image](https://github.com/user-attachments/assets/92f19a46-60df-4a15-94b2-1e21b97f5998)
# Methods for decoding images
1. SatDump - in progress. A beta version is in progress.
2. Python scripts - this is the method we will look at here. These simple scripts will simply locate the image portions without any error checking. But if your SNR is plenty and the DVB-S2 is doing its error correction, this method should be able to get images with no problem.
# Equipment needed
<img width="532" height="400" alt="image" src="https://github.com/user-attachments/assets/3d7f23d3-a21d-4d87-9eaf-36583dcfd65e" />

1. 1.5m or larger prime dish. A mesh dish with holes no larger than 4mm will also work (1/10 lambda rule).
2. X-band feed. Make one or buy commercial version + teflon for circular polarisation.<br>
   See: https://www.a-centauri.com/articoli/an-x-band-primer
4. LNA (30-40 dB) - buy from used sellers like ebay.
5. X-band downconverter to L-band<br>
   My version is from https://m0kds.com/
7. TBS6903x or later: It must be over PCI. Receivers with USB output will not be able to transport the frames.<br>
   If using laptop you will need a PCI to ExpressCard socket (if your laptop has one).   

8. PC running EBSPro. Make sure your card supports BBFRAMES and set this in the `streamreader.ini` file in the EBSPro folder:
   <br><br>`FrameMode=1`<br><br>Also make sure the card can recieve the frequency output by the downconverter. In my case, the downconverter oscillator is set to 7000 MHz meaning the output frequency is 1070 MHz (8070 - 7000).

9. Upon successful lock by the receiver, the parameters will show. Signal lock can be achieved down to 6.6 dB, but try to aim for an SNR of 7.0 dB or above.
   
      ![tbs6903x_4](https://github.com/user-attachments/assets/52d2771d-7deb-4aa5-94a5-ce1048592547)
<p>The constellation in Crazyscan:</p>
<img width="556" height="650" alt="constellation2" src="https://github.com/user-attachments/assets/462d7f38-f1b6-40ef-a559-77942dead091" />

<br>10. Put the LNA next to the feed and if possible, the downconverter as well. If you are going to use coax, use low loss semi rigid coax on the high frequency side. The output of the downconverter will likely be in the L-band, so coax is not too critical here. You need to decide how your LNA and downconverter is going to get power, but be aware that receiver cards for satellite will have option to output DC to power an LNB, which may or may not be needed.

# Software needed
1. GIMP for editing images
2. Python - download from https://www.python.org/downloads/
3. EBS-pro or receiver software compatible with TBS6903x / SatDump if you are using SDR.

# Video
Watch this video to get an overview:<br>
https://youtu.be/yJCwNY3K8kQ

# Preparation
1. Create a folder called UHRIT, e.g. E:\SDR\GK-2A\UHRIT
2. Copy the scripts: RemoveSpaceHeaders.py , new.py, Getsegment.py to this folder
3. Copy the batch script "make.bat" and "make-halfscale.bat" to this folder

## Recording
A DVB-S2 stream for a full disk containing all 16 channels begins transmission at every 7th minute of the hour (e.g. xx:07, xx:17) and lasts for about 6 minutes. This requires about 2 GB of disk space.

## Image and decryption
Files are created under the extension ".uhrit". To convert to images requires lrit-img.py which is available from VKSDR and the github site here: https://github.com/sam210723/xrit-rx<br>
Download the release "xrit-rx.zip" and extract to the folder you created.
Rename the folder "xrit-rx" to "uhrit-rx".
Place your decryption key message file (.bin.dec) into the uhrit-rx folder. As in uhrit-rx\xxxx.bin.dec

Images are saved under jpeg2000. Go into the "tools" folder under uhrit-rx and open "lrit-img.py" and adjust it in the following places:
![image](https://github.com/user-attachments/assets/88f30293-bfc5-40a2-9e55-c21197c10481)
![image](https://github.com/user-attachments/assets/f45f1945-7675-4a39-b6ee-313aa9790ef7)

Save this to another file called "uhrit-img.py" in the same location.

The "#img=img.resize((img.width // 2, img.height // 2)) #for half scale" is for creating half the full resolution. Useful for VI006 to reduce it down to 1km from 0.5km to combine with VI004,VI005.

Un-comment this out (delete the #) and save this to another file called "uhrit-img-halfscale.py" in the same location.

# Create BBFRAMES file only.
The BBFrames from the TBS6903x are misaligned so cannot be input just yet. To correct them you need to run the following:
`python new_bbframe_only.py "location\0.0E_1070.011_H_15622_(2025-04-12 16.16.48)_dump.ts"`

You should get an output "bbframe_output.bin" which can be input into any BBFrame decoder e.g. SatDump

# How to extract the uhrit from BBFRAMES
BBFrames is the first layer output by the TBS6903x. The UHRIT files are located directly inside. Infact, you can see the bbframe headers when you inspect the output.<p>
![BBheader](https://github.com/user-attachments/assets/115ec0f4-57ef-48aa-ad3f-1d8759176d04)
The first task is to remove the bbheaders and join the frames.  

<br>Goto DOS prompt and run `python new.py "path and name to the transport stream.ts"` which will produce an output file `test2.bin` in your folder. For example:
`E:\SDR\GK-2A\UHRIT>python new.py "location\0.0E_1070.011_H_15622_(2025-04-12 16.16.48)_dump.ts"`
<br>

## How to extract the uhrit from CADU
If are using an SDR and software (e.g. Satdump) that receives and demodulates the DVB-S2 signal, or skips the BBFRAMES and outputs the CADU directly, the above code will also work. You just need to type:
`python new.py "location\file.cadu"`



# Build the image

Goto a hexeditor and open `test2.bin`. This contains all 23 segments per channel for which there are 16.<br>You need to find the channel you want, e.g. IMG_FD_052_VI004_20240914_084736. This is subdivided into segments 1-23. Make a note of this.

Execute "make.bat" and enter the channel name, e.g. IMG_FD_052_VI004_20240914_084736 (if you want other channels replace VI004 with e.g. VI005 etc). Then enter the segments 1 through 23.

`E:\SDR\GK-2A\UHRIT>make.bat`<br>
`Channel?IMG_FD_052_VI004_20240914_084736`<br>
`FirstSegment(1-23)?1`<br>
`LastSegment(1-23)?23`<br>

If you enter `make-halfscale.bat`, this will create the images at half their full resolution.

Go into explorer and you will find the created image segments.
![image](https://github.com/user-attachments/assets/748594e3-4cb5-433d-8a94-f46c36367fd9)


# GIMP 2 plugins
(<b>Warning: These plugins only work in GIMP2, not GIMP3. For using with GIMP 3, see below.</b>)

To join the segments together, you will need GIMP. Install the plugins to the following folder in GIMP:<br>

![image](https://github.com/user-attachments/assets/8c0a3709-7143-402f-8733-baaa9d137cdb)

Open GIMP and check that the plugins appear. There are 3 types - 0.5km, 1km and 2km resolutions.
![image](https://github.com/user-attachments/assets/963b835f-c595-4941-b0d7-ae2d8467ac68)
![dataSet](https://github.com/user-attachments/assets/9e8bafc4-4684-47f1-8096-47b6f1ff1784)

# GIMP 3 plugins
Download the plugins for GIMP 3 above.<br>
You need to save the plugins, each in their own folder with the same name. The location is in your user folder - app data. If successful, the GK-2A menu should appear.
<p><img width="490" height="217" alt="image" src="https://github.com/user-attachments/assets/82e7d934-3265-4026-b6d4-13dee1e968db" /></p>
<p><img width="1305" height="835" alt="image" src="https://github.com/user-attachments/assets/df33dacb-cc23-45b0-95a6-ebc87f8dad54" /></p>


# Building complete disks in GIMP
1. Open the desired segments as layers under File -> open as layers
2. Reverse layer order (under layer -> stack) and check the layers go up in ascending order.
3. Goto to layer menu and select GK-2A submenu (or GK-2A at the top for GIMP 3) and choose the option for joining.
4. Resize the canvas under image -> fit canvas to layers.
5. Then merge the layers.

You should get a full image. 

# Results

## Editing tips:
The primary image you get when you combine the `VI006`,`VI005`,`VI004` images is as follows:<p>
<img width="685" height="685" alt="image" src="https://github.com/user-attachments/assets/3bd3baa5-8062-48fa-8dc8-b636d7aac843" />
</p>

The uncorrected image makes it difficult to see the land and the atmosphere scatters a lot of blue light. In GIMP, we can try and enhance the image.

## To get an enhanced image
The best method I found was to adjust the GIMP colour curves. You can find this under `colors` and `curves`. Before adjusting, it is best to exclude the black area surrounding the disk. Click `select` then `by color` and then click on the black area. Then under the same menu, click `invert`. This will select and isolate the disk portion in the image.<p>
<img width="685" height="687" alt="image" src="https://github.com/user-attachments/assets/311de79d-1049-4061-a56b-9827f757ce8a" />
</p>

### White balance
First thing we notice is the image is very dark. Go to `colors` - `Auto` - `White balance`<p>
<img width="677" height="679" alt="image" src="https://github.com/user-attachments/assets/d6e02343-f5ae-441d-9b52-12031825e146" />
</p>

### Colours
Now go to the `Hue-chroma` under `colors`. Increase hue by 20 points.
<p><img width="683" height="689" alt="image" src="https://github.com/user-attachments/assets/823fb9d9-334b-4543-81c3-1743a0929883" /></p>

The next step is to adjust each of the red, green and blue channels individually under `color` and `curves`. 
<p><img width="542" height="580" alt="image" src="https://github.com/user-attachments/assets/e7e6bd68-2746-4089-af6e-00673e5ef827" /></p>

When you select a colour channel, its histogram will display where the lines are. The corresponding line for that channel will be available for adjustment. 

### Example
An example setting that gives similar appearance to the official satellite images can be downloaded from the `curves` folder above. Copy the text and add it to your `GimpCurvesConfig.settings` under the `filters` folder in your App data, similar to the plugins.

### Final image
<img width="681" height="681" alt="image" src="https://github.com/user-attachments/assets/29ce4b1a-d1d2-44c0-8ca8-8e7c18f189eb" />



### References
https://medium.com/@robsimmon/making-sense-of-satellite-data-an-open-source-workflow-color-correction-with-gimp-7ddae0360fea


## Natural colour
This is used for emphasising land/vegetation and low temperature cloud tops.<br>
Red = `NR016`<br>
Green = `VI008`<br>
Blue = `VI006`<br>

![image](https://github.com/user-attachments/assets/eed05f50-1810-4a9f-aa68-915ca2960663)

## Fire hotspots
Used to show fire hotspots. This makes use of the 3.9um band that is sensitive to the radiation from the fire.<br>
Red = `SW038 (inverted)`<br>
Green = `VI008`<br>
Blue = `VI006`<br>

<img width="1335" height="870" alt="image" src="https://github.com/user-attachments/assets/d1c6d173-2c8d-48f0-b249-df443d77868c" />

## Getting full (22k) resolution RGB.
The UHRIT data contains 1 channel at 22k resolution (VI006). A technique used in LandSat imagery allows you full 22k resolution RGB images, if the high resolution channel is mapped onto the lower resolution RGB image. The advantage is that you only need one channel to be at high resolution.
See the following website for more information:<br>
https://earthobservatory.nasa.gov/blogs/earthmatters/2017/06/13/how-to-pan-sharpen-landsat-imagery/

## Hybrid green
Red = `VI006`<br>
Green = About 8% `VI008`added to `VI005` 92%<br>
Blue = `VI004`<br>
<br>

Both Himawari and GK-2A green sensors are not true green shown by the spectral response. 
<img width="701" height="573" alt="image" src="https://github.com/user-attachments/assets/c8872f44-32c0-413e-bffe-133457b3e134" />
<br>Source: https://www.data.jma.go.jp/mscweb/en/aomsuc6_data/oral/s02-04.pdf<br><br>

This produces land that is too red. To correct this, you need to mix some of the NIR (VI008) to the green (VI005). This can be done in GIMP using the levels option.<br><br>

<img width="1370" height="784" alt="image" src="https://github.com/user-attachments/assets/0cf0b798-f041-4a63-900d-551c3922ff24" />



