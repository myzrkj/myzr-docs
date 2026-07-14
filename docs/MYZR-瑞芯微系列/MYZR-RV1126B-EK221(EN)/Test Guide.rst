.. raw:: html

   <style>
   h1 {
       color: green;
   }
   </style>

Test Guide
==========

USB Test
--------

Interface Silk Screen:

* USB 2.0 : J1

* USB 3.0 : USB 3.0

Test Description: Test by plugging and unplugging USB storage devices (USB flash drive).

Test Operations:

1. Insert the USB device into the USB port on the baseboard. The system will output similar information as follows:

.. code-block:: shell

   [   19.961327 ] usb 1-1.1: new high-speed USB device number 4 using ehci-
   platform
   [   20.072318 ] usb 1-1.1: New USB device found, idVendor=ffff, idProduct=5678,
   bcdDevice= 2.00
   [   20.072353 ] usb 1-1.1: New USB device strings: Mfr=1, Product=2,
   SerialNumber=3
   [   20.072372 ] usb 1-1.1: Product: Disk 2.0
   [   20.072386 ] usb 1-1.1: Manufacturer: USB
   [   20.072400 ] usb 1-1.1: SerialNumber: 5299291115661588161
   [   20.073438 ] usb-storage 1-1.1:1.0: USB Mass Storage device detected
   [   20.074332 ] scsi host0: usb-storage 1-1.1 :1.0
   [   21.082808 ] scsi 0:0:0:0: Direct-Access     VendorCo ProductCode      2.00
   PQ: 0 ANSI: 4
   [   21.085385 ] sd 0:0:0:0:  [sda] 31129600 512-byte logical blocks: (15.9
   GB/14.8 GiB)
   [   21.086132 ] sd 0:0:0:0:  [sda] Write Protect is off
   [   21.086877 ] sd 0:0:0:0:  [sda] No Caching mode page found
   [   21.086889 ] sd 0:0:0:0:  [sda] Assuming drive cache: write through
   [   21.091631 ]  sda: sda1
   [   21.092478 ] sd 0:0:0:0:  [sda] Attached SCSI removable disk
   [   21.321373 ] FAT-fs (sda1): utf8 is not a recommended IO charset for FAT
   filesystems, filesystem will be case sensitive!
   [   21.325508 ] FAT-fs (sda1): Volume was not properly unmounted. Some data may
   be corrupt. Please run fsck.

2. Remove the USB device from the USB port on the baseboard. The system will output similar information as follows:

.. code-block:: shell

   [   90.139509] usb 1-1.1: USB disconnect, device number 4

SD Card Interface Test
----------------------

Interface Silk Screen: TF

Test Description: Test by plugging and unplugging TF card.

Test Operations:

1. Insert the TF card into the TF card slot on the baseboard. The system will output similar information as follows:

.. code-block:: shell

   [  432.796162] mmc_host mmc1: Bus speed (slot 0) = 400000Hz (slot req
   400000Hz, actual 400000HZ div = 0)
   [  432.881908] mmc_host mmc1: Bus speed (slot 0) = 50000000Hz (slot req
   50000000Hz, actual 50000000HZ div = 0)
   [  432.881993] mmc1: new high speed SDHC card at address 1234
   [  432.883524] mmcblk1: mmc1:1234 SA08G 7.21 GiB
   [  432.885458]  mmcblk1: p1
   [  433.089059] FAT-fs (mmcblk1p1): utf8 is not a recommended IO charset for
   FAT filesystems, filesystem will be case sensitive!
   [  433.097212] FAT-fs (mmcblk1p1): Volume was not properly unmounted. Some
   data may be corrupt. Please run fsck.

2. Remove the TF card from the TF card slot on the baseboard. The system will output similar information as follows:

.. code-block:: shell

   [  518.934035] mmc1: card 1234 removed

Ethernet Port Test
------------------

Ethernet Port 1
~~~~~~~~~~~~~~

Interface Silk Screen: 100M

System Interface: eth0

Test Description: Test by sending ICMP packets from the development board to the PC.

Test Operations:

1. Configure the PC's wired network adapter IP to 192.168.137.99.

2. Connect the development board's Ethernet port to the PC's Ethernet port using an Ethernet cable. The serial port will display:

.. code-block:: shell

   [  975.297225] rk_gmac-dwmac 21c70000.ethernet eth0: Link is Up - 100Mbps/Full
   - flow control rx/tx
   [  975.297294] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready

3. By default, the IP address is obtained automatically, but for testing, configure a static IP using the following commands:

.. code-block:: shell

   ifconfig eth0 up
   ifconfig eth0 192.168.137.81

4. Enter the following command to verify Ethernet Port 1:

.. code-block:: shell

   ping -I eth0 192.168.137.99 -c 2 -w 4

5. The system will output similar information as follows:

.. code-block:: shell

   PING 192.168.137.99  (192.168.137.99 ) from 192.168.137.17  eth0: 56(84) bytes  of
   data.
   64 bytes from 192.168.137.99 : icmp_seq= 1 ttl= 128 time= 1.28 ms
   64 bytes from 192.168.137.99 : icmp_seq= 2 ttl= 128 time= 0.378  ms
   --- 192.168.137.99  ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1002ms
   rtt min/avg/ max/mdev = 0.378 /0.829 /1.280 /0.451  ms

Ethernet Port 2
~~~~~~~~~~~~~~

Interface Silk Screen: 1000

System Interface: eth0

Test Description: Test by sending ICMP packets from the development board to the PC.

Test Operations:

1. Configure the PC's wired network adapter IP to 192.168.137.99.

2. Connect the development board's Ethernet port to the PC's Ethernet port using an Ethernet cable. The serial port will display:

.. code-block:: shell

   [  975.297225] rk_gmac-dwmac 21c70000.ethernet eth0: Link is Up - 1Gbps/Full -
   flow control rx/tx
   [  975.297294] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready

3. By default, the IP address is obtained automatically, but for testing, configure a static IP using the following commands:

.. code-block:: shell

   ifconfig eth0 up
   ifconfig eth0 192.168.137.81

4. Enter the following command to verify Ethernet Port 2:

.. code-block:: shell

   ping -I eth0 192.168.137.99 -c 2 -w 4

5. The system will output similar information as follows:

.. code-block:: shell

   PING 192.168.137.99  (192.168.137.99 ) from 192.168.137.17  eth0: 56(84) bytes  of
   data.
   64 bytes from 192.168.137.99 : icmp_seq= 1 ttl= 128 time= 1.28 ms
   64 bytes from 192.168.137.99 : icmp_seq= 2 ttl= 128 time= 0.378  ms
   --- 192.168.137.99  ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1002ms
   rtt min/avg/ max/mdev = 0.378 /0.829 /1.280 /0.451  ms

WIFI Test
---------

Interface Silk Screen: WIFI/BT

System Interface: wlan0

Test Description: After connecting WIFI to an AP, the development board sends ICMP packets to the external network to verify the connection is normal.

Test Operations:

1. Connect the WIFI antenna to the U17 interface.

2. Enter the following commands to generate the WPAPSK file for the SSID.

.. code-block:: shell

   ### wpa_passphrase command format: wpa_passphrase + wifi name + wifi password > /etc/wpa_supplicant.conf
   wpa_passphrase realme fgew5678 > /etc/wpa_supplicant.conf
   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

3. The system will output similar information as follows:

.. code-block:: shell

   Successfully initialized wpa_supplicantt -B -i wlan0 -c
   /etc/wpa_supplicant.conf
   [   19.936696] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready

4. Obtain IP address automatically

.. code-block:: shell

   udhcpc -i wlan0

5. The system will output similar information as follows:

.. code-block:: shell

   udhcpc: started, v1.36.1
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.66.26, server 192.168.66.130
   udhcpc: lease of 192.168.66.26 obtained from 192.168.66.130, lease time 3600
   deleting routers
   adding dns 192.168.66.130

6. Test the connection by entering the following command:

.. code-block:: shell

   ping -I wlan0 www.baidu.com -c 2 -w 4

Output:

.. code-block:: shell

   PING www.baidu.com ( 183.2.172.177 ) from 192.168.66.26  wlan0: 56(84) bytes  of
   data.
   64 bytes from 183.2.172.177 : icmp_seq= 1 ttl= 53 time= 224 ms
   64 bytes from 183.2.172.177 : icmp_seq= 2 ttl= 53 time= 217 ms
   --- www.baidu.com ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1002ms
   rtt min/avg/ max/mdev = 216.994 /220.289 /223.584 /3.295  ms

Bluetooth Test
--------------

Interface Silk Screen: WIFI/BT

Test Description: After scanning for Bluetooth devices, send L2CAP echo requests and receive responses.

Test Operations:

1. Connect the antenna to the U17 interface.

2. Enter the command to start Bluetooth:

.. code-block:: shell

   hciconfig hci0 up

3. Enter the command to scan for external Bluetooth devices:

.. code-block:: shell

   hcitool scan

4. The system will print similar information as follows:

.. code-block:: shell

   Scanning ...
   E4:33:AE:6D:77:96        n/a
   DC:0D:30:5C:4C:93        XP-236B-L

5. Enter the command to send L2CAP ping test:

.. code-block:: shell

   l2ping DC:0D:30:5C:4C:93

Output:

.. code-block:: shell

   Ping: DC:0D: 30:5C:4C: 93 from 94:BA:06: 78:1B:33 (data size 44) ...
   0 bytes from DC:0D: 30:5C:4C: 93 id 0 time 3.89ms
   0 bytes from DC:0D: 30:5C:4C: 93 id 1 time 24.91 ms
   0 bytes from DC:0D: 30:5C:4C: 93 id 2 time 48.93 ms
   0 bytes from DC:0D: 30:5C:4C: 93 id 3 time 37.43 ms
   0 bytes from DC:0D: 30:5C:4C: 93 id 4 time 27.48 ms
   5 sent, 5 received, 0% loss

Audio Playback Test
-------------------

Interface Silk Screen: Audio

Test Description: Verify the audio playback function of the evaluation board by playing audio files.

Test Operations:

1. Connect the speaker to the corresponding interface marked by the silk screen.

2. Enter the following commands to perform the playback test:

Check the sound card and its number:

.. code-block:: shell

   aplay -l

Specify the playback device and audio file:

.. code-block:: shell

   aplay -D hw:0,0 sample-9s.wav

If sound is output from the speaker, the audio playback function is working properly.

MIPI DSI Test
-------------

Interface Silk Screen: DSI

Test Operations:

1. Power off the development board. Connect the MIPI display to the MIPI_DSI interface on the baseboard using a flexible cable, then restart the development board.

2. After the development board starts up, you can see the boot log and system interface displayed on the MIPI screen.

MIPI CSI Test
-------------

CSI0
~~~~

Interface Silk Screen: CSI0

Test Operations:

1. Power off the development board. Install the camera facing the notch, then restart the development board.

2. Enter the command to check if the video device is detected:

.. code-block:: shell

   v4l2-ctl --list-devices

Output similar information as follows:

.. code-block:: shell

   rkisp_mainpath (platform:rkisp-vir0):
   /dev/video23
   /dev/video24
   /dev/video25
   /dev/video26
   /dev/video27
   /dev/video30
   /dev/media3
   rkisp_mainpath (platform:rkisp-vir1):
   /dev/video31
   /dev/video32
   /dev/video33
   /dev/video34
   /dev/video35
   /dev/video38
   /dev/media4

3. Enter the command to start the camera.

.. code-block:: shell

   gst-launch-1.0 v4l2src device=/dev/video23 ! 'video/x-
   raw,format=NV12,width=800,height=1280,framerate=30/1'  ! autovideosink

Output:

.. code-block:: shell

   Setting pipeline to PAUSED ...
   Using mplane plugin for capture
   Pipeline is live and does not need PREROLL ...
   Pipeline is PREROLLED ...
   Setting pipeline to PLAYING ...
   New clock: GstSystemClock
   [  173.556450 ] rkisp_hw 21d00000.isp: set isp clk = 297000000Hz
   [  173.556583 ] rkcif-mipi-lvds: stream[0] start streaming
   [  173.556841 ] rockchip-mipi-csi2 mipi0-csi2: stream on, src_sd:
   0000000001c7d66b, sd_name:rockchip-csi2-dphy0
   [  173.556853 ] rockchip-mipi-csi2 mipi0-csi2: stream ON
   [  173.556891 ] rockchip-csi2-dphy0: dphy0, data_rate_mbps 840
   [  173.556918 ] rockchip-csi2-dphy csi2-dphy0: csi2_dphy_s_stream stream on:1,
   dphy1, ret 0
   Redistribute latency...
   0:00:04.2 / 99:99:99.

You can see the real-time image captured by the camera on the screen.

CSI1
~~~~

Interface Silk Screen: CSI1

Test Operations:

1. Power off the development board. Install the camera facing the notch, then restart the development board.

2. Enter the command to check if the video device is detected:

.. code-block:: shell

   v4l2-ctl --list-devices

Output similar information as follows:

.. code-block:: shell

   rkisp_mainpath (platform:rkisp-vir0):
   /dev/video23
   /dev/video24
   /dev/video25
   /dev/video26
   /dev/video27
   /dev/video30
   /dev/media3
   rkisp_mainpath (platform:rkisp-vir1):
   /dev/video31
   /dev/video32
   /dev/video33
   /dev/video34
   /dev/video35
   /dev/video38
   /dev/media4

3. Enter the command to start the camera.

.. code-block:: shell

   gst-launch-1.0 v4l2src device=/dev/video31 ! 'video/x-
   raw,format=NV12,width=800,height=1280,framerate=30/1'  ! autovideosink

Output:

.. code-block:: shell

   Setting pipeline to PAUSED ...
   Using mplane plugin for capture
   Pipeline is live and does not need PREROLL ...
   Pipeline is PREROLLED ...
   Setting pipeline to PLAYING ...
   New clock: GstSystemClock
   [   19.709846 ] rkisp_hw 21d00000.isp: set isp clk = 297000000Hz
   [   19.709977 ] rkcif-mipi-lvds2: stream[0] start streaming
   [   19.710234 ] rockchip-mipi-csi2 mipi2-csi2: stream on, src_sd:
   0000000061a9e163, sd_name:rockchip-csi2-dphy3
   [   19.710247 ] rockchip-mipi-csi2 mipi2-csi2: stream ON
   [   19.710280 ] rockchip-csi2-dphy3: dphy4, data_rate_mbps 840
   [   19.710307 ] rockchip-csi2-dphy csi2-dphy3: csi2_dphy_s_stream stream on:1,
   dphy4, ret 0
   Redistribute latency...
   0:00:02.6 / 99:99:99.

You can see the real-time image captured by the camera on the screen.

RS232 Test
----------

Interface Silk Screen: RS232

Test Description: Perform send and receive tests by connecting to a PC using a 232-USB converter.

Test Operations:

1. Connect the development board to the PC using a 485-USB converter.

2. Open the corresponding serial port using Xshell, set the baud rate to 115200, data bits to 8, and stop bits to 1.

3. Enter the following command:

.. code-block:: shell

   ./usr/serial_test.out /dev/ttyS2 "MYZR"

You can see "MYZR" output on the RS232 serial terminal, then it enters receive mode.

4. On the RS232 serial terminal, directly enter "123" (not displayed), the board will output:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x31          Character: 1
   ASCII: 0x32          Character: 2
   ASCII: 0x33          Character: 3

RS485 Test
----------

Interface Silk Screen: RS485

Test Description: Perform send and receive tests by connecting to a PC using a 485-USB converter.

Test Operations:

1. Connect the development board to the PC using a 485-USB converter. The triangle mark on the edge of the board is pin 1 (B), corresponding to the converter's B, and pin 2 (A) corresponds to A.

2. Open the corresponding serial port using Xshell, set the baud rate to 115200, data bits to 8, and stop bits to 1.

3. Enter the following command:

.. code-block:: shell

   ./usr/serial_test.out /dev/ttyS1 "MYZR"

You can see "MYZR" output on the RS485 serial terminal, then it enters receive mode.

4. On the RS485 serial terminal, directly enter "123" (not displayed), the board will output:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x31          Character: 1
   ASCII: 0x32          Character: 2
   ASCII: 0x33          Character: 3

CAN Test
--------

Interface Silk Screen: CAN

Test Description: Connect two sets of CAN buses using jumper wires and test by sending and receiving data between them.

Test Operations:

1. Connect the two CAN interfaces to each other using jumper wires.

2. Enter the following commands in the terminal to configure the CAN interface:

.. code-block:: shell

   ip link set can0 type can bitrate 500000 dbitrate 2000000 fd on
   ip link set can0 up

3. You will see similar information output in the terminal, indicating successful activation:

.. code-block:: shell

   link becomes ready

4. Enter the following command in the terminal to enable the CAN interface to receive in the background, and enter the command in the serial terminal to send test data through the CAN interface:

.. code-block:: shell

   candump can0 &
   cansend can0 123 #11223344