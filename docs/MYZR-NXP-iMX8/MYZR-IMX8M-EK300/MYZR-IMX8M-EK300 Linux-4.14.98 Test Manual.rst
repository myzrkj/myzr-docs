
MYZR-IMX8M-EK300 Linux-4.14.98 Test Manual
=============================================

Test environment
-------------------

|  [Development board model]: MYZR-IMX8M-EK300
|  [Kernel Version]: Linux-4.14.98
|  [File system]: fsl-image-validation-myimx8m.tar.bz2
|  [Tool version]: UUU-MYIMX8M-L4.14.98
|  Description: In order to ensure that the test is correct, the version of the flashing tool to be used should be no less than 20190903


Interface identification diagram
------------------------------------

.. image:: /image/MYZR-iMX8系列/MYZR-IMX8M-EK300/1800px-IMX8MEK300-interface.jpg
   :alt: 1800px-IMX8MEK300-interface.jpg

Network port test（ETH1）
---------------------------

|  [Test description]: Use the development board to send ICMP messages to the PC for testing
|  [Interface ID]: Ethernet
|  [Interface silk screen ]: J16
|  [System interface]: eth0

**Test operation**

|  Configure the computer's wired network card IP as 192.168.137.99.
|  Connect the ETH1 of the development board and the computer with a network cable.
|  Configure the development board network port:

.. code-block:: shell
   
   =====> Enter the command:
   ifconfig eth0 192.168.137.81
  
|  Test ETH1 (eth0):

.. code-block:: shell

   =====> Enter the instruction:
   ping 192.168.137.99 -c 2 -w 4 

   =====> Output information:
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.685 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.374 ms 
   
   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.374/0.529/0.685/0.157 ms     

**Test Results**

|  "0% packet loss" means the test passed.


USB Test
---------

|  [Test description]: USB memory device (U disk) is used for testing
|  [Interface identification ]: USB3.0 / USB2.0
|  [Interface silk screen ]： J18

**Test Methods**

|  Plug the USB device into the USB interface of the backplane, and the system output is similar to the following information.

.. code-block:: 

   =====> Output information: 
   usb 1-1.1: new high-speed USB device number 3 using xhci-hcd
   usb-storage 1-1.1:1.0: USB Mass Storage device detected
   scsi host0: usb-storage 1-1.1:1.0
   scsi 0:0:0:0: Direct-Access     Generic  STORAGE DEVICE   1402 PQ: 0 ANSI: 6
   sd 0:0:0:0: [sda] 7774208 512-byte logical blocks: (3.98 GB/3.71 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
    sda: sda1
   sd 0:0:0:0: [sda] Attached SCSI removable disk
   FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|  Unplug the USB device from the backplane.

.. code-block:: shell

   =====> Output information： 
   usb 1-1.1: USB disconnect, device number 3 

**Test Results**

|  When the USB storage device is inserted, the sda1 device can be viewed.


SD interface test
-------------------

|  [Test description]: Test by inserting and identifying TF card
|  [Interface identification ]: MicroSD
|  [Interface silk screen]: J9

**Test Methods**

|  To power off the development board, install the TF card to the SD interface.

.. code-block:: shell

   =====> Enter the instruction:
   dmesg | grep -E "mmc1|mmcblk1" 

   =====> Output information: 
   mmc1: SDHCI controller on 30b50000.usdhc [30b50000.usdhc] using ADMA
   mmc1: host does not support reading read-only switch, assuming write-enable
   mmc1: new high speed SDHC card at address 1234
   mmcblk1: mmc1:1234 SA04G 3.71 GiB 
    mmcblk1: p1

**Test Results**

|  When the SD storage device is inserted or removed, the system outputs similar information as above, which indicates normal.

Audio playback test
---------------------

|  [Test description ]: Verify the audio playback function of the evaluation board by playing audio files.
|  [Interface Identification ]: HP
|  [Interface position ]: P1
|  [System equipment ]: wm8524-audio

**Test operation**

|  Plug the headset into the "HP" port of the development board.
|  Execute test instructions:

.. code-block:: shell

   =====> Enter the instruction:aplay /unit_tests/ASRC/audio8k16S.wav    

   =====> Output information:
   Playing WAVE '/unit_tests/ASRC/audio8k16S.wav' : Signed 16 bit Little 
   Endian, Rate 8000 Hz, Stereo

**Test Results**

|  After executing the above test command, you will hear the sound from the audio device.

HDMI Display test
--------------------

|  [Test description ]: Observe the display function of the development board by connecting the HDMI display.
|  [Interface Identification ]: HDMI
|  [Interface position ]: J12
|  [System equipment ]: / dev / fb0

**Test operation**

|  To power off the development board, use an HDMI cable to connect the HDMI display and development board, and power the HDMI display.
|  It is recommended to use the HDMI interface display, instead of other interfaces to HDMI.
|  It is recommended to use an HDMI display with 1920x1080 resolution.

**Test Results**

|  UU-Boot Logo can be seen during the U-Boot startup phase;
|  Kernel Logo can be seen during the kernel startup phase;
|  OpenOpenEmbedded Logo can be seen during the file system startup phase;
|  You can see a simple GUI after system startup is complete.

WIFI module (AP6354) test
----------------------------

|  [Test description ]: After WIFI is connected to the AP, the development board sends ICMP messages to the Internet to verify that the connection is normal.
|  [Interface ID ]: WIFI & BT, WIFI_ANT
|  [Interface silk screen ]: U3, ANT1 / ANT2 / ANT3
|  [System equipment ]: wlan0

**Test operation**

1. Make sure there is a module attached to the “WIFI + BT” sign, otherwise no test is required.
2. Connect the WIFI antenna to the interface marked “WIFI_ANT”.
3. Generate WPA PSK file for SSID

|  Command format: wpa_passphrase <ssid> [passphrase]

.. code-block:: shell

   =====> Enter the command:
   wpa_passphrase MY-TEST-AP myzr2012 > /etc/wpa_supplicant.conf
   pkill wpa_supplicant

4. connection

.. code-block:: shell

   =====> Enter the command:
   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

   =====> Output information：
   Successfully initialized wpa_supplicant
   rfkill: Cannot open RFKILL control device
   ioctl[SIOCSIWAP]: Operation not permitted

5. get IP

.. code-block:: shell

   =====> Enter the command:
   udhcpc -i wlan0

   =====> Output information：
   udhcpc (v1.23.2) started
   Sending discover...
   Sending select for 192.168.43.99...
   Lease of 192.168.43.99 obtained, lease time 3600
   /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

6. Test connection

.. code-block:: shell

   =====> Enter the command:
   ping -I wlan0 www.baidu.com -c 2 -w 4

   =====> Output information：
   PING www.baidu.com (14.215.177.38): 56 data bytes
   64 bytes from 14.215.177.38: seq=0 ttl=49 time=15.753 ms
   64 bytes from 14.215.177.38: seq=1 ttl=49 time=11.835 ms

   --- www.baidu.com ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 11.835/13.794/15.753 ms

**Test Results**

|  "0% packet loss" indicates that the WIFI connection is normal.

Bluetooth test(AP6354)
------------------------

|  [Test description]: After scanning the Bluetooth device, send the L2CAP response request and receive the response.
|  [Interface identification]: WIFI + BT, BL_ANT
|  [Interface silk screen]: U24, E1
|  [System equipment]: hci0

**Test operation**

1. Make sure there is a module attached to the “WIFI + BT” sign, otherwise no test is required.
2. Connect the Bluetooth antenna to the interface marked “BL_ANT”.
3. Connect to BlueZ stack via UART HCI

.. code-block:: shell

   =====> Enter the command:
   hciattach /dev/ttymxc2 bcm43xx 2000000 flow

   =====> Output information：
   bcm43xx_init
   Patch not found, continue anyway
   Set Controller UART speed to 2000000 bit/s
   Setting TTY to N_HCI line discipline
   Device setup complete

4. Configure the Bluetooth system interface

.. code-block:: shell

   =====> Enter the command:
   hciconfig hci0 up
   hciconfig hci0 piscan
   hciconfig -a


   =====> Output information：
   hci0:   Type: Primary  Bus: UART
       BD Address: 76:5E:F9:C6:B5:86  ACL MTU: 1021:8  SCO MTU: 64:1
       UP RUNNING PSCAN ISCAN 
       RX bytes:1381 acl:0 sco:0 events:75 errors:0
       TX bytes:1210 acl:0 sco:0 commands:75 errors:0
       Features: 0xbf 0xfe 0xcf 0xfe 0xdb 0xff 0x7b 0x87
       Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3 
       Link policy: RSWITCH SNIFF 
       Link mode: SLAVE ACCEPT 
       Name: 'imx8mqevk'
       Class: 0x200000
       Service Classes: Audio
       Device Class: Miscellaneous, 
       HCI Version: 4.0 (0x6)  Revision: 0x1000
       LMP Version: 4.0 (0x6)  Subversion: 0x610c
       Manufacturer: Broadcom Corporation (15)

5. View board Bluetooth device information

.. code-block:: shell

   =====> Enter the command:
   hcitool dev  

   =====> Output information：
   Devices:
       hci0    76:5E:F9:C6:B5:86

6. Scan for external Bluetooth devices

.. code-block:: shell

   =====> Enter the command:
   hcitool scan  

   =====> Output information：
   Scanning ...
       ......
       E4:B2:FB:DA:39:1D   iPhone

7. Send L2CAP packet test

.. code-block:: shell

   =====> Enter the command:
   l2ping E4:B2:FB:DA:39:1D -c 2
   =====> Output information：
   Ping: E4:B2:FB:DA:39:1D from 76:5E:F9:C6:B5:86 (data size 44) ...
   0 bytes from E4:B2:FB:DA:39:1D id 0 time 7.10ms
   0 bytes from E4:B2:FB:DA:39:1D id 1 time 103.84ms
   2 sent, 2 received, 0% loss

**Test Results**

|  "0% packet loss" indicates that the Bluetooth connection is normal.



