MYZR-IMX8MM-EK240-8MM Linux-4.14.98 Test Manual
==================================================

Network interface test (ETH1)
--------------------------------

|  【Test instructions】: The development board is used to send ICMP message to the PC for testing
|  【Interface logo】: Ethernet
|  【Interface screen printing】: J9
|  【 System interface 】 : eth0

**Test operation**

|  Configure the computer wired network card IP for 192.168.137.99. Connect the development board ETH1 to the computer with an Ethernet cable. Configuration development board network port:
|  =====> input:

.. code-block:: shell

      ifconfig eth0 192.168.137.81

|  test ETH1（eth0）
|  =====> input:

.. code-block:: shell

   ping 192.168.137.99 -c 2 -w 4

|  =====> output：

.. code-block:: shell

   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.685 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.374 ms 
   192.168.137.99 ping statistics 
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.374/0.529/0.685/0.157 ms

**Test result**

|  “0% packet loss”Indicates successful test.

USB test
-----------

|  【Test instructions】: USB storage device (U disk) is used for testing
|  【Interface logo】: USB3.0/USB2.0
|  【Interface screen printing】: J5

**Test method**

|  Insert the USB device into the USB interface of the backplane, and the output of the system is similar to the following information.
|  ====> output :

.. code-block:: shell

   usb 1-1.3: new high-speed USB device number 4 using ci_hdrc
   usb-storage 1-1.3:1.0: USB Mass Storage device detected
   scsi host0: usb-storage 1-1.3:1.0
   scsi 0:0:0:0: Direct-Access   Generic  STORAGE DEVICE  1532 PQ: 0 ANSI: 6
   sd 0:0:0:0: [sda] 60776448 512-byte logical blocks: (31.1 GB/29.0 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn\'t support DPO or FUA
   sda: sda1
   sd 0:0:0:0: [sda] Attached SCSI removable disk
   FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|  Unplug the USB device from the bottom plate.
|  =====> output：

.. code-block:: shell

   usb 1-1.3: USB disconnect, device number 4

**Test result**

|  The SDA1 device can be viewed when the USB storage device is inserted.

SD interface testing
-----------------------

|  【Test instructions】: Insert and identify the TF card for the test
|  【Interface Logo】 : MicroSD
|  【Interface screen printing】: J10

**Test method**

|  To disconnect the development board, install the TF card to the SD interface.
|  =====> input:

.. code-block:: shell

   df

|  =====> output：

.. code-block:: shell

   /dev/mmcblk1p1   30379712  665216  29714496  3% /run/media/mmcblk1p1

**Test result**

|  After input instruction, the system output similar information as above indicates normal.

Standard GPIO testing
------------------------

|  【Test description】: Control the output level of GPIO
|  【Interface Logo】:
|  【Interface screen printing】: J7
|  【System interface】: /sys/class/ GPIo /

**GPIO output low level test**

|  Operation method to configure J7:15 to output low level:

.. code-block:: shell

   =====> input:

   OUT_IO_OUT_NUM=8
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
   Test pin J7:15 with a multimeter and the voltage is 0V, indicating OK

**GPIO output high level test**

|  How to configure J7:15 to output high level:
|  =====> input:

.. code-block:: shell
   
   <echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  Test pin J5:5 with a multimeter and the voltage is 3.3V, indicating OK **GPIO input test**
|  Control GPIO for input low level method: Dupont wire connects J5:5 to the ground
|  =====> input:

.. code-block:: shell

   echo "in" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction

   cat /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  Control GPIO to input high level Method: Dupont line connects J5:5 and J5:1 pin:
|  =====> input:

.. code-block:: shell

   cat /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  You can see that the corresponding levels are 0 and 1, respectively

CPU temperature test
----------------------

|  【Test instructions】 : Check the CPU temperature
|  【Interface identification】: None
|  【system】: / sys/class/thermal/thermal_zone0 / temp

**Test operation**

|  =====> input:

.. code-block:: shell

   echo $[$(cat /sys/class/thermal/thermal_zone0/temp)/1000]

|  =====> output：

.. code-block:: shell
   
   47

**Test result**

|  47 indicates that the CPU temperature is 47°

Audio playback test
---------------------

|  【Test instructions】: Verify the audio playback function of the evaluation board by playing audio files.
|  【Interface location】: P4
|  【System Equipment】: WM8524-Audio

**Test operation**

|  Plug the headphones into the P5 port on the development board. Execute test instructions:
|  =====> input:

.. code-block:: shell

   aplay /unit_tests/ASRC/audio8k16S.wav

|  =====> output：

.. code-block:: shell

   Playing WAVE '/unit_tests/ASRC/audio8k16S.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Stereo

**Test result**

|  After executing the above test command, you will hear the audio device output.

Mipi-DSI display test
-------------------------

|  【Test instructions】: Observe the display function of the development board by connecting the Mipi screen.
|  【Interface location】: J2
|  【System equipment】: /dev/fb0

**Test operation**

|  In case of power failure of development board, connect MIPI display screen and development board with FPC wiring.

**Test result**

|  The U-boot Logo can be seen during the Boot stage; The kernel Logo can be seen during the kernel startup stage. You can see the OpenEmbedded Logo on the file system startup stage. When the system boots up, you will see a simple GUI.

Mipi-CSI display test
------------------------

|  【Test instructions】: Check the miPI-CSI interface of the development board by connecting the Mipi camera. 
|  【Interface location】: J1 
|  【System equipment】: /dev/video0

**Test operation**

|  To disconnect the development board, connect the MIPI camera to the development board using FPC wiring.

.. code-block:: shell

   gst-launch-1.0 v4l2src ! video/x-raw,format=YUY2,width=640,height=480 ! queue max-size-time=0 ! waylandsink enable-tile=true sync=false

**Test result**

|  You can see what the camera captures on the screen

Test for WIFI module (RTL8723DU)
-----------------------------------

|  【Test instructions】: After WIFI is connected to AP, the development board sends ICMP message to the external network to verify the normal connection.
|  【Interface screen printing】: E1, U6
|  【System equipment】: WLAN0

**Test operation**

1. Make sure there is a paste module in the "U6" screen print, otherwise there is no need to test.
2. Connect the antenna to the interface of "E1" screen printing.
3. WPA PSK file for SSID generation

|  Command format: wPA_passphrase [Passphrase]*
|  =====> input:

.. code-block:: shell

   wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf
   pkill wpa_supplicant

4. connect

|  =====> input:

.. code-block:: shell

   wpa_supplicant -B -i wlan0 -D wext -c /etc/wpa_supplicant.conf

|  =====> output：

.. code-block:: shell

   Successfully initialized wpa_supplicant
   rfkill: Cannot open RFKILL control device
   ioctl[SIOCSIWAP]: Operation not permitted

5. get IP

|  =====> input:

.. code-block:: shell

   udhcpc -i wlan0

|  =====> output：

.. code-block:: shell

   udhcpc (v1.23.2) started
   Sending discover...
   Sending select for 192.168.43.99...
   Lease of 192.168.43.99 obtained, lease time 3600
   /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

6. test connection

|  =====> input:

.. code-block:: shell

   ping -I wlan0 www.baidu.com -c 2 -w 4

|  =====> output：

.. code-block:: shell

   PING www.baidu.com (14.215.177.38): 56 data bytes
   64 bytes from 14.215.177.38: seq=0 ttl=49 time=15.753 ms
   64 bytes from 14.215.177.38: seq=1 ttl=49 time=11.835 ms
   --- www.baidu.com ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 11.835/13.794/15.753 ms

**Test result**

|  “0% packet loss”Indicates that WIFI connection is normal.

Bluetooth test (RTL8723DU)
----------------------------

|  【Test instructions】: After scanning the Bluetooth device, send L2CAP to respond to the request and receive the answer.
|  【Interface screen printing】: E1, U6
|  【System equipment】: HCI0

**Test operation**

1. Make sure there is a paste module in the "U6" screen print, otherwise there is no need to test.
2. Connect the antenna to the interface of "E1" screen printing.
3. Configure the Bluetooth system interface

|  =====> input:

.. code-block:: shell

   hciconfig hci0 up
   hciconfig hci0 piscan
   hciconfig -a

|  =====> output：

.. code-block:: shell

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

4. Check the bluetooth device information of the board

|  =====> input:

.. code-block:: shell

   hcitool dev

|  =====> output：

.. code-block:: shell

   Devices:
   hci0    76:5E:F9:C6:B5:86

5. Scan for external Bluetooth devices

|  =====> input:

.. code-block:: shell

   hcitool scan

|  =====> output：

.. code-block:: shell

   Scanning ...
   ......
   E4:B2:FB:DA:39:1D   iPhone

6. Send send L2CAP package test

|  =====> input:

.. code-block:: shell

   l2ping E4:B2:FB:DA:39:1D -c 2

|  =====> output：

.. code-block:: shell

   Ping: E4:B2:FB:DA:39:1D from 76:5E:F9:C6:B5:86 (data size 44) ...
   0 bytes from E4:B2:FB:DA:39:1D id 0 time 7.10ms
   0 bytes from E4:B2:FB:DA:39:1D id 1 time 103.84ms
   2 sent, 2 received, 0% loss

**Test result**

|  0% Packet Loss represents normal Bluetooth connection

CAN test
----------

|  Test description The test USES two CAN interfaces Test command: Configuration CAN:
|  =====> input:

.. code-block:: shell

   ip link set can0 up type can bitrate 125000

|  Set CAN background receive:
|  =====> input:

.. code-block:: shell

   candump can0 &

|  Set CAN to send data:
|  =====> input:

.. code-block:: shell

   cansend can0 1F334455#1122334455667788

232 Serial port test
-----------------------

- Test description

|  Test method description: TX1 and RX1 are shorted by serial lines. Execute the following command:

.. code-block:: shell

   /unit_tests/UART/serial_test.out /dev/ttyXRUSB1 "www.myzr.com.cn"

|  The serial port line shorts TX2 and RX2 directly. Execute the following command:

.. code-block:: shell

   /unit_tests/UART/serial_test.out /dev/ttyXRUSB2 "www.myzr.com.cn"

Test for 485 serial port1
---------------------------

|  The test shows that

-  Test method description:

|  Use the serial port line to connect the development board through RS485 to 232 module to test serial port A1, B1 and computer, and login with SSH client.

|  UART test

- Execute the sending command on the SSH side, and you can receive the information sent from the serial port on the computer:

.. code-block:: shell

   echo “myzr” > /dev/ttyXRUSB3

- Test result description: The SSH client sends a string to the serial port, which receives the string.
- Execute the receive command at the SSH side:

.. code-block:: shell

   cat /dev/ttyXRUSB3

- Test result description:

|  The SSH client receives the string by sending it to the SSH client via serial port.

485 serial port 2 test 2
---------------------------

|  The test shows that

- Test method description:

|  Use the serial port line to connect the development board through RS485 to 232 module to test serial Port A2, B2 and computer, and login with SSH client.

|  UART test

- Execute the sending command on the SSH side, and you can receive the information sent from the serial port on the computer:

.. code-block:: shell

   echo “myzr” > /dev/ttyXRUSB0

- Test result description: The SSH client sends a string to the serial port, which receives the string.
- Execute the receive command at the SSH side:

.. code-block:: shell

   cat /dev/ttyXRUSB0

- Test result description:

|  The SSH client receives the string by sending it to the SSH client via serial port.

EC20 module test
------------------

|  【Test instructions】: After the 4G connection is successful, the development board sends ICMP message to the external network to verify the normal connection.
|  【System equipment】: PPP0

**Test operation**

1. Power off the development board, connect the 4G module, connect the antenna and start the evaluation board after inserting THE SIM card.
2. Network connection with instructions:

|  =====> input:

.. code-block:: shell

    /etc/ppp/peers/quectel-CM

|  ====> output information:

.. code-block:: shell

   abort on (DELAYED)
   abort on (BUSY)
   abort on (ERROR)
   abort on (NO DIALTONE)
   abort on (NO CARRIER)
   send (AT^M)
   expect (OK)
   AT^M^M
   OK
   -- got it
   send (ATS0=0^M)
   expect (OK)
   ^M
   ATS0=0^M^M
   OK
   -- got it
   send (ATE0V1^M)
   expect (OK)
   ^M
   ATE0V1^M^M
   OK
   -- got it
   send (AT+CGDCONT=1,"IP","CMNET"^M)
   expect (OK)
   ^M
   ^M
   OK
   -- got it
   send (ATD*99***1#^M)
   expect (CONNECT)
   ^M
   ^M
   CONNECT
   -- got it
   Serial connection established.
   using channel 1
   Using interface ppp0
   Connect: ppp0 <--> /dev/ttyUSB3
   sent [LCP ConfReq id=0x1 <asyncmap 0x0> <magic 0x65fd5ad6> <pcomp> <accomp>]
   rcvd [LCP ConfReq id=0x0 <asyncmap 0x0> <auth pap> <magic 0x60de49b9> <pcomp> <accomp>]
   No auth is possible
   sent [LCP ConfRej id=0x0 <auth pap>]
   rcvd [LCP ConfAck id=0x1 <asyncmap 0x0> <magic 0x65fd5ad6> <pcomp> <accomp>]
   rcvd [LCP ConfReq id=0x1 <asyncmap 0x0> <magic 0x60de49b9> <pcomp> <accomp>]
   sent [LCP ConfAck id=0x1 <asyncmap 0x0> <magic 0x60de49b9> <pcomp> <accomp>]
   sent [LCP EchoReq id=0x0 magic=0x65fd5ad6]
   sent [CCP ConfReq id=0x1 <deflate 15> <deflate(old#) 15> <bsd v1 15>]
   sent [IPCP ConfReq id=0x1 <compress VJ 0f 01> <addr 0.0.0.0> <ms-dns1 0.0.0.0> <ms-dns3 0.0.0.0>]
   rcvd [LCP DiscReq id=0x2 magic=0x60de49b9]
   rcvd [LCP EchoRep id=0x0 magic=0x60de49b9 65 fd 5a d6]
   rcvd [LCP ProtRej id=0x3 80 fd 01 01 00 0f 1a 04 78 00 18 04 78 00 15 03 2f]
   Protocol-Reject for 'Compression Control Protocol' (0x80fd) received
   rcvd [IPCP ConfReq id=0x0]
   sent [IPCP ConfNak id=0x0 <addr 0.0.0.0>]
   rcvd [IPCP ConfRej id=0x1 <compress VJ 0f 01>]
   sent [IPCP ConfReq id=0x2 <addr 0.0.0.0> <ms-dns1 0.0.0.0> <ms-dns3 0.0.0.0>]
   rcvd [IPCP ConfReq id=0x1]
   sent [IPCP ConfAck id=0x1]
   rcvd [IPCP ConfNak id=0x2 <addr 10.77.19.81> <ms-dns1 221.179.38.7> <ms-dns3 120.196.165.7>]
   sent [IPCP ConfReq id=0x3 <addr 10.77.19.81> <ms-dns1 221.179.38.7> <ms-dns3 120.196.165.7>]
   rcvd [IPCP ConfAck id=0x3 <addr 10.77.19.81> <ms-dns1 221.179.38.7> <ms-dns3 120.196.165.7>]
   Could not determine remote IP address: defaulting to 10.64.64.64
   local  IP address 10.77.19.81
   remote IP address 10.64.64.64
   primary   DNS address 221.179.38.7
   secondary DNS address 120.196.165.7

|  Test connection:
|  =====> input:

.. code-block:: shell

   ping -I usb0 www.baidu.com -c 2 -w 4

|  =====> output：

.. code-block:: shell

   PING www.a.shifen.com (163.177.151.109) from 192.168.225.52 usb0: 56(84) bytes of data.
   64 bytes from 163.177.151.109: icmp_seq=1 ttl=55 time=158 ms
   --- www.a.shifen.com ping statistics ---
   1 packets transmitted, 1 received, 0% packet loss, time 0ms
   rtt min/avg/max/mdev = 158.529/158.529/158.529/0.000 ms

**Test result**

|  0% Packet Loss means WIFI connection is working.

TFTP update image
-------------------

|  【Test instructions】 : DTB, zImage can be updated

**Test operation**

|  1.TFTPD address is set to the directory where the files to be replaced are located. 
|  2.Connect the development board port to the computer port with a cable. 
|  3.Go to the U-boot command line.

1. Set the IP

|  =====> input:

.. code-block:: shell

   Set development board IP: Setenv IPaddr 192.168.137.9
   Set up computer IP: Setenv Serverip 192.168.137.99
   Set MAC address: Setenv ethaddr 00:00:00:00:00:03
   Test network: Ping 192.168.137.99

|  =====> output：

.. code-block:: shell

   ethernet@30be0000 Waiting for PHY auto negotiation to complete.... done
   Using ethernet@30be0000 device
   The host 192.168.137.99 is alive

2. Set environment variables

|  =====> input:

.. code-block:: shell

   setenv update_dtb 'if tftpboot ${loadaddr} ${fdt_file}; then '\
   'fatwrite mmc ${mmcdev}:${mmcpart} ${loadaddr} ${fdt_file} ${filesize}; fi;'
   setenv update_kern 'if tftpboot ${loadaddr} ${image}; then '\
   'fatwrite mmc ${mmcdev}:${mmcpart} ${loadaddr} ${image} ${filesize}; fi;'
   saveenv

3. The burning DTB

|  =====> input:

.. code-block:: shell

   run update_dtb

|  =====> output：

.. code-block:: shell

   Using ethernet@30be0000 device
   TFTP from server 192.168.137.99;Our IP Address is 192.168.137.9
   Filename 'myimx8mmek240-8mm.dtb'.
   Load address: 0x40480000
   Loading: ###
           610.4 KiB/s
   done
   Bytes transferred = 41910 (a3b6 hex)
   writing myimx8mmek240-8mm.dtb
   41910 bytes written

4. Write zImage burn

|  =====> input:

.. code-block:: shell

   run update_kern

|  =====> output：

.. code-block:: shell

   Using ethernet@30be0000 device
   TFTP from server 192.168.137.99;Our IP Address is 192.168.137.9
   Filename 'Image'.
   Load address: 0x40480000
   Loading: #############################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    ##########################################
        1.2 MiB/s 

   done
   Bytes transferred = 23509504 (166ba00 hex)
   writing Image
   23509504 bytes written


Copy the update image
-------------------------

|  【Test instructions】 : DTB, zImage and Kernel-Modules can be updated

**Test operation**

1. Copy the corresponding file to the current directory of the development board, taking TFTP as an example TFTPD address is set to the directory where the files to be replaced are located. Connect the development board port to the computer port with a cable. 
2. Test the connection

|  =====> input:

.. code-block:: shell

   ping 192.168.137.99 -c 2 -w 4 

|  =====> output：

.. code-block:: shell

   PING 192.168.137.99 (192.168.137.99) 56(84) Bytes of data.
   64 Bytes from 192.168.137.99: ICmp_seq =1 TTL =64 time=0.522 ms
   64 Bytes from 192.168.137.99: ICmp_seq =2 TTL =64 time= 0.415ms
   -- 192.168.137.99 Ping Statistics --
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/ Max /mdev = 0.415/0.468/0.522/0.057ms

|  "0% Packet Loss" represents a normal connection.

3. Transfer files

|  =====> input:

.. code-block:: shell

   tftp -g 192.168.137.99 -r Image

   tftp -g 192.168.137.99 -r myimx8mmek240-8mm.dtb
   tftp -g 192.168.137.99 -r kernel-modules.tar.bz2

4. Copy the corresponding file to /run/media/ mmcBLk1p1 / directory and replace the original file.

|  =====> input:

.. code-block:: shell

   cp Image /run/media/mmcblk1p1/
   cp myimx8mmek240-8mm.dtb /run/media/mmcblk1p1/

5. Unzip and update the kernel module

|  =====> input:

.. code-block:: shell

   tar xjvf kernel-modules.tar.bz2 -C /

6. Save and restart

|  =====> input:

.. code-block:: shell

   reboot