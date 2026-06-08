MYZR-RZFIVE-EK200 Test Manual
===============================

Ethernet Testing
------------------

Ethernet Port 1 Testing
~~~~~~~~~~~~~~~~~~~~~~~~~

|   【Test Description】: Test by sending ICMP packets from the development board to the PC
|   【Interface Identification】: 10M/100M/1000M Ethernet-1
|   【System Interface】: eth0

**Test Operations**

|   Configure the IP address of the PC's wired network card to 192.168.137.99.
|   Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.
|   Configure the Ethernet port of the development board:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# ifconfig eth1 down
    root@myzr-rzfive:~# ifconfig eth0 192.168.137.81

|   Test the Ethernet port:

.. code-block:: shell

    =====> Enter command:
    ping 192.168.137.99 -c 2 -w 4 

    =====> Output information:
    PING 192.168.137.99 (192.168.137.99): 56 data bytes
    64 bytes from 192.168.137.99: seq=0 ttl=128 time=0.927 ms
    64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.765 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.765/0.846/0.927 ms

**Test Result**

|   "0% packet loss" indicates the test is passed.

Ethernet Port 2 Testing
--------------------------

|   【Test Description】: Test by sending ICMP packets from the development board to the PC
|   【Interface Identification】: 10M/100M/1000M Ethernet-2
|   【System Interface】: eth1

**Test Operations**

|   Configure the IP address of the PC's wired network card to 192.168.137.99.
|   Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.
|   Configure the Ethernet port of the development board:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# ifconfig eth0 down
    root@myzr-rzfive:~# ifconfig eth1 192.168.137.82

    =====> Output information:
    [  394.660011] RTL8211F Gigabit Ethernet 11c30000.ethernet-ffffffff:01: attached PHY driver [RTL8211F Gigabit Ethernet] (mii_bus:phy_addr=11c30000.ethernet-ffffffff:01, irq=178)
    root@myzr-rzfive:~# [  399.044603] ravb 11c30000.ethernet eth1: Link is Up - 1Gbps/Full - flow control off

|   Test the Ethernet port:

.. code-block:: shell

    =====> Enter command:
    ping 192.168.137.99 -c 2 -w 4 

    =====> Output information:
    PING 192.168.137.99 (192.168.137.99): 56 data bytes
    64 bytes from 192.168.137.99: seq=0 ttl=128 time=1.831 ms
    64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.610 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.610/1.220/1.831 ms

**Test Result**

|   "0% packet loss" indicates the test is passed.

USB Interface Testing
-----------------------

|   【Test Description】: Test by plugging and unplugging a USB storage device (USB flash drive)
|   【Interface Identification】: USB HOST
|   【System Interface】: /dev/sd*

**Test Method**

|   Insert the USB device into the USB interface of the baseboard, and the system will output information similar to the following:

.. code-block:: shell

    [  548.085779] usb 1-1.1: new high-speed USB device number 4 using ehci-platform
    [  548.762436] usb-storage 1-1.1:1.0: USB Mass Storage device detected
    [  548.781918] scsi host0: usb-storage 1-1.1:1.0
    [  551.099373] scsi 0:0:0:0: Direct-Access              aigo U330        PMAP PQ: 0 ANSI: 6
    [  551.115142] sd 0:0:0:0: [sda] 30924800 512-byte logical blocks: (15.8 GB/14.7 GiB)
    [  551.130652] sd 0:0:0:0: [sda] Write Protect is off
    [  551.143403] sd 0:0:0:0: [sda] No Caching mode page found
    [  551.157939] sd 0:0:0:0: [sda] Assuming drive cache: write through
    [  551.214240]  sda: sda1
    [  551.229828] sd 0:0:0:0: [sda] Attached SCSI removable disk

|   Unplug the USB device from the baseboard, and the system will output information similar to the following:

.. code-block:: shell

    [  582.421825] usb 1-1.1: USB disconnect, device number 4

**Test Result**

|   The system outputs information similar to the above when the USB storage device is plugged in or unplugged, which indicates normal operation.

SD Card Interface Testing
---------------------------

|   【Test Description】: Test by inserting and recognizing a TF card
|   【Interface Identification】: SD3
|   【System Interface】: /dev/mmcblk1

**Test Method**

|   Insert the SD card into this interface:

.. code-block:: shell

    =====> Output information:
    [   28.038307] mmc1: new high speed SDHC card at address 0001
    [   28.050565] mmcblk1: mmc1:0001 TF 4G 3.68 GiB 
    [   28.061692]  mmcblk1: p1 p2

|   Eject the SD card:

.. code-block:: shell

    =====> Output information:
    [  164.986044] mmc1: card 0001 removed

**Test Result**

|   The system outputs information similar to the above when the SD storage device is plugged in or unplugged, which indicates normal operation.

Standard GPIO Testing
-----------------------

|   【Test Description】: Control the output level of GPIO
|   【Interface Identification】: GPIO/SD2
|   【System Interface】: /sys/class/gpio/

**Available IOs for MYZR-RZFIVE-MB200**

.. code-block:: shell

    GPIO6_0(408),  GPIO11_0(448),  GPIO11_1(449), GPIO11_3(451),   GPIO13_0(464),   GPIO13_2(466), GPIO13_4(468), GPIO0_3(363), GPIO10_1(441)

|   Pin calculation formula: **GPIO_ID = GPIO_port * 8 + GPIO_pin + 360.**

**GPIO Output Low Level Test**

|   Method to configure GPIO11_0 to output low level:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# OUT_IO_OUT_NUM=448
    root@myzr-rzfive:~# echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
    root@myzr-rzfive:~# echo "out" > /sys/class/gpio/P11_0/direction  
    root@myzr-rzfive:~# echo 0 > /sys/class/gpio/P11_0/value 

|   Test the GPIO11_0 pin with a multimeter. If the voltage is 0V, it indicates normal operation.

**GPIO Output High Level Test**

|   Method to configure GPIO11_0 to output high level:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# OUT_IO_OUT_NUM=448
    root@myzr-rzfive:~# echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
    root@myzr-rzfive:~# echo "out" > /sys/class/gpio/P11_0/direction  
    root@myzr-rzfive:~# echo 1 > /sys/class/gpio/P11_0/value 

|   Test the GPIO11_0 pin with a multimeter. If the voltage is 3.3V, it indicates normal operation.

**GPIO Input Test**

|   Control GPIO input test:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# OUT_IO_OUT_NUM=448
    root@myzr-rzfive:~# echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
    root@myzr-rzfive:~# echo "in" > /sys/class/gpio/P11_0/direction  
    root@myzr-rzfive:~# cat /sys/class/gpio/P11_0/value   

UART Serial Port Testing
--------------------------

|   【Test Description】: Test by means of serial port self-transmission and self-reception
|   【Interface Identification】: TX0/1/3/4, RX0/1/3/4
|   【System Device】: /dev/ttySC0/1/3/4

**Test Operations**

|   Take Serial Port 3 as an example: short-circuit the transmit and receive pins of Serial Port 3 (pins 8 and 10 of P2)
|   Execute the test command:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:/# /my-demo/serial_test.out /dev/ttySC3 "www.myzr.com.cn" 

    =====> Output information:
    Starting send data...finish
    Starting receive data:
    ASCII: 0x77      Character: w 
    ASCII: 0x77      Character: w 
    ASCII: 0x77      Character: w 
    ASCII: 0x2e      Character: . 
    ASCII: 0x6d      Character: m 
    ASCII: 0x79      Character: y 
    ASCII: 0x7a      Character: z 
    ASCII: 0x72      Character: r 
    ASCII: 0x2e      Character: . 
    ASCII: 0x63      Character: c 
    ASCII: 0x6f      Character: o 
    ASCII: 0x6d      Character: m 
    ASCII: 0x2e      Character: . 
    ASCII: 0x63      Character: c 
    ASCII: 0x6e      Character: n 
    ASCII: 0x0   Character:  

**Test Result**

|   After executing the test command, if the application outputs information similar to the above, it indicates normal operation.

SPI Testing
-------------

|   【Test Description】: Test by means of self-transmission and self-reception.
|   【Interface Identification】: SPI1
|   【System Device】: /dev/spidev1.0

**Test Operations**

|   Short-circuit pins 2 and 5 of U18. Execute the test command:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# /my-demo/spidev_test.out -D /dev/spidev1.0  

    =====> Output information:
    spi mode: 0
    bits per word: 8
    max speed: 500000 Hz (500 KHz)

    FF FF FF FF FF FF 
    40 00 00 00 00 95 
    FF FF FF FF FF FF 
    FF FF FF FF FF FF 
    FF FF FF FF FF FF 
    DE AD BE EF BA AD 
    F0 0D 

**Test Result**

|   After executing the test command, if the application outputs information similar to the above, it indicates normal operation.

Watchdog Timeout Reset Test
-----------------------------

|   【Test Description】: Enable the watchdog, wait for the watchdog timeout, and trigger a reset.
|   【Interface Identification】: None
|   【System Device】: /dev/watchdog0

**Test Operations**

|   Run the watchdog program:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# /my-demo/wdt_driver_test.out 10 15 1 
    
    =====> Output information:
    Starting wdt_driver (timeout: 10, sleep: 15, test: write)
    Trying to set timeout value=10 seconds
    The actual timeout was set to 10 seconds
    Now reading back -- The timeout is 10 seconds

**Test Result**

|   Ten seconds after running the test command, the WatchDog times out, and the system is reset. You will see information similar to the following output on the terminal when the system restarts:

.. code-block:: shell

    U-Boot SPL 2020.10 (Jan 11 2023 - 03:22:42 +0000)
    Trying to boot from MMC1
    board_mmc_init
    þ
    
    U-Boot 2020.10 (Jan 11 2023 - 03:22:42 +0000)
    
    CPU:   rv64imafdc
    Model: myzr-rzfive
    DRAM:  dram_init

Watchdog Feeding Test
-----------------------

|   【Test Description】: Enable the watchdog and make the application feed the watchdog.
|   【Interface Identification】: None
|   【System Device】: /dev/watchdog0

**Test Operations**

|   Run the watchdog program, set the timeout period to 4 seconds, and the watchdog feeding interval to 2 seconds:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# /my-demo/wdt_driver_test.out 4 2 1 &  
    
    =====> Output information:
    [1] 206
    Starting wdt_driver (timeout: 4, sleep: 2, test: write)
    Trying to set timeout value=4 seconds
    The actual timeout was set to 4 seconds
    Now reading back -- The timeout is 4 seconds


RTC Testing
-------------

|   【Test Description】: Read and set the time, then check if the time is correct after power-off and restart.
|   【Interface Identification】: None
|   【System Device】: /dev/rtc0

**Test Operations**

1. Power off and restart the device, then check the current system time and hardware time:

.. code-block:: shell

    =====> Enter command: 
    root@myzr-rzfive:~# date

    =====> Output Information:
    Fri Dec 16 05:41:21 UTC 2022

2. Check the current RTC chip clock:

.. code-block:: shell

    =====> Enter command: 
    root@myzr-rzfive:~# date -s "2023-01-14 12:34:56"

    =====> Output Information:
    hwclock: ioctl(RTC_RD_TIME) to /dev/rtc0 to read the time failed: Invalid argument

3. Set the system clock and synchronize it to the RTC chip

.. code-block:: shell

    =====> Enter command: 
    date -s "2023-01-14 12:34:56"  

    =====> Output Information:
    Sat Jan 14 12:34:56 UTC 2023

4. Write the system clock to the hardware clock

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# hwclock -w

**Test Result**

1. Power off and restart the evaluation board, then check the current system clock and hardware clock

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# date

    =====> Output Information:
    Sat Jan 14 12:36:34 UTC 2023

2. Check the current RTC chip clock

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# hwclock

    =====> Output Information:
    2023-01-14 12:37:06.057566+00:00

|   It can be seen that the obtained time is basically the same as the set time.

Audio Playback Testing
-------------------------

|   【Test Description】: Verify the audio playback function of the evaluation board by playing audio files.
|   【Interface Identification】: P1
|   【System Device】: wm8960-audio

**Test Operations**

|   Insert the earphone into the "EAR" port of the development board.
|   Execute the test command:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# aplay /my-demo/Rear_Center.wav   

    =====> Output Information:
    Playing WAVE '/my-demo/Rear_Center.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

**Test Result**

|   After executing the above test command, you will hear the sound output from the audio device.

Audio Recording Testing
--------------------------

|   【Test Description】: Verify the audio recording function of the evaluation board by recording and playing back the recorded file.
|   【Interface Identification】: P1
|   【System Device】: wm8960-audio

**Test Operations**

1. Insert the earphone with MIC into the "MIC" port of the development board.
2. Execute the recording command:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# arecord -d 5 -c 2 -r 48000 -f S16_LE record.wav

    =====> Output Information:
    Recording WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

3. Play back the recording

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# aplay record.wav

    =====> Output Information:
    Playing WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

**Test Result**

|   After executing the above test command, you will hear the played-back recording.

USB Recognized as Ethernet Port Testing
------------------------------------------

|   【Test Description】: Recognize USB as an Ethernet port via a mini USB cable.
|   【Interface Identification】: J5
|   【System Device】: usb0

**Test Operations**

1. Load the module

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# modprobe g_ether

    =====> Output Information:
    [ 1142.930290] using random self ethernet address
    [ 1142.934837] using random host ethernet address
    [ 1142.963949] usb0: HOST MAC 02:07:67:c9:1c:71
    [ 1142.981727] usb0: MAC 4e:76:dc:e4:13:cf
    [ 1142.998101] using random self ethernet address
    [ 1143.018416] using random host ethernet address
    [ 1143.030241] g_ether gadget: Ethernet Gadget, version: Memorial Day 2008
    [ 1143.046032] g_ether gadget: g_ether ready

2. Set the IP address

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# ifconfig usb0 192.168.7.2
    Set the IP address of the RNDIS local connection recognized by the PC to 192.168.7.8

3. Test the Ethernet port

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# ping 192.168.7.7 -c 2 -w 4
    =====> Output Information:
    PING 192.168.7.7 (192.168.7.7): 56 data bytes
    64 bytes from 192.168.7.7: seq=0 ttl=128 time=0.555 ms
    64 bytes from 192.168.7.7: seq=1 ttl=128 time=0.521 ms

    --- 192.168.7.7 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.521/0.538/0.555 ms

**Test Result**

|   "0% packet loss" indicates the test is passed.
|   Note: If Windows 10 recognizes RNDIS as a COM port, you need to download the driver "kindle_rndis.inf_amd64-v1.0.0.1.zip", unzip it, execute "5-runasadmin_register-CA-cer.cmd" with administrator privileges, then double-click the COM port and search for the unzipped driver in the computer. After that, the RNDIS network will be available.

USB Recognized as USB Flash Drive Testing
-------------------------------------------

|   【Test Description】: Recognize the development board as a USB flash drive on the PC via a mini USB cable.
|   【Interface Identification】: J5
|   【System Device】: devtmpfs

**Test Operations**

1. Create a 10MB file

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# dd if=/dev/zero of=/dev/shm/disk bs=1024 count=10240

    =====> Output Information:
    10240+0 records in
    10240+0 records out
    10485760 bytes (10 MB, 10 MiB) copied, 0.0959887 s, 109 MB/s

2. Load the module

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# modprobe g_mass_storage stall=0 file=/dev/shm/disk removable=1

    =====> Output Information:
    [  113.101409] Mass Storage Function, version: 2009/09/11
    [  113.106701] LUN: removable file: (no medium)
    [  113.114166] LUN: removable file: /dev/shm/disk
    [  113.118655] Number of LUNs=1
    [  113.121708] g_mass_storage gadget: Mass Storage Gadget, version: 2009/09/11
    [  113.130701] g_mass_storage gadget: userspace failed to provide iSerialNumber
    [  113.138667] g_mass_storage gadget: g_mass_storage ready

3. Recognize the USB flash drive

|   At this point, a USB flash drive drive letter will appear in "My Computer" on the PC. After formatting it, you can read and write to it.

4. Mount the drive

.. code-block:: shell

    root@myzr-rzfive:~# mount /dev/shm/disk /mnt

**Test Result**

|   The files written on the PC can be seen under the "/mnt/" directory. After writing files on the development board, re-plug the mini USB cable, and the new files written on the development board can be seen on the PC.

CPU Temperature Testing
-------------------------

|   【Test Description】: Check the CPU temperature.
|   【Interface Identification】: None
|   【System Device】: /sys/class/thermal/thermal_zone0/temp

**Test Operations**

|   Enter the command

.. code-block:: shell

    =====> Enter command:
    echo $[$(cat /sys/class/thermal/thermal_zone0/temp)/1000]
    =====> Output Information:
    36

**Test Result**

|   The value "36" indicates that the CPU temperature is 36°C.

WIFI Module Testing
---------------------

|   【Test Description】: After the WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal.
|   【Interface Identification】: WIFI&BT
|   【Interface Silkscreen】: E2
|   【System Device】: wlan0

**Test Operations**

1. Connect the WIFI antenna to the "E1" interface.
2. Generate a WPA PSK file for the SSID |   

|   Command format: `wpa_passphrase [SSID] [passphrase]`

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf 

3. Connect to the WIFI:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf 

    =====> Output Information:
    Successfully initialized wpa_supplicant
    nl80211: kernel reports: Authentication algorithm number required
    rfkill: Cannot open RFKILL control device
    。。。。。。

4. Obtain the IP address:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# udhcpc -i wlan0

    =====> Output Information:
    udhcpc: started, v1.31.1
    udhcpc: sending discover
    udhcpc: sending discover
    udhcpc: sending select for 192.168.43.204
    udhcpc: lease of 192.168.43.204 obtained, lease time 3600
    /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

5. Test the connection:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# ping -I wlan0 www.baidu.com -c 2 -w 4

    =====> Output Information:
    PING www.baidu.com (163.177.151.110): 56 data bytes
    64 bytes from 163.177.151.110: seq=0 ttl=55 time=34.722 ms
    64 bytes from 163.177.151.110: seq=1 ttl=55 time=31.935 ms

    --- www.baidu.com ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 31.935/33.328/34.722 ms

Bluetooth Testing
--------------------

|   【Test Description】: After scanning a Bluetooth device, send an L2CAP response request and receive the reply.
|   【Interface Identification】: WIFI&BT
|   【Interface Silkscreen】: E2
|   【System Device】: hci0

**Test Operations**

1. Connect the antenna to the "E1" interface.
2. Start Bluetooth:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# hciconfig hci0 up
    root@myzr-rzfive:~# hciconfig

    =====> Output Information:
    hci0:   Type: Primary  Bus: USB
        BD Address: 30:7B:C9:6E:F6:43  ACL MTU: 1021:8  SCO MTU: 255:12
        UP RUNNING PSCAN 
        RX bytes:1250 acl:0 sco:0 events:72 errors:0
        TX bytes:1090 acl:0 sco:0 commands:72 errors:0

3. Scan external Bluetooth devices:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~#  hcitool scan

    =====> Output Information:
    Scanning ...
        A5:7C:A2:26:9F:F8   Luxury Smart Massage Chair
        1C:D1:07:D7:65:EC   Realme GT Neo Flash Edition

4. Send an L2CAP packet for testing:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# l2ping 1C:D1:07:D7:65:EC

    =====> Output Information:
    Ping: 1C:D1:07:D7:65:EC from 30:7B:C9:6E:F6:43 (data size 44) ...
    44 bytes from 1C:D1:07:D7:65:EC id 0 time 6.07ms
    44 bytes from 1C:D1:07:D7:65:EC id 1 time 24.67ms
    44 bytes from 1C:D1:07:D7:65:EC id 2 time 26.03ms
    44 bytes from 1C:D1:07:D7:65:EC id 3 time 72.35ms
    44 bytes from 1C:D1:07:D7:65:EC id 4 time 72.37ms
    44 bytes from 1C:D1:07:D7:65:EC id 5 time 62.30ms
    ^C6 sent, 6 received, 0% loss

|   "0% packet loss" indicates that the Bluetooth connection is normal.


EC20 Module Testing
---------------------

|   【Test Description】: After successful 4G connection, the development board sends ICMP packets to the external network to verify normal connection.
|   【Interface Identification】: J9
|   【System Device】: usb0 or usb1

**Test Operations**

1. Power off the development board, connect the 4G module, attach the antenna and insert the SIM card, then start the evaluation board.
2. Use the command to establish network connection:

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# /my-demo/quectel-CM &

    =====> Output information:
    [1] 231
    [12-16_05:31:07:561] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
    [12-16_05:31:07:561] ./quectel-CM profile[1] = (null)/(null)/(null)/0, pincode = (null)
    [12-16_05:31:07:564] Find /sys/bus/usb/devices/1-1.4 idVendor=2c7c idProduct=0125
    [12-16_05:31:07:564] Find /sys/bus/usb/devices/1-1.4:1.4/net/usb0
    [12-16_05:31:07:564] Find usbnet_adapter = usb0
    [12-16_05:31:07:564] Find /sys/bus/usb/devices/1-1.4:1.4/GobiQMI/qcqmi0
    [12-16_05:31:07:564] Find qmichannel = /dev/qcqmi0
    [12-16_05:31:07:598] Get clientWDS = 7
    root@myzr-rzfive:~# [12-16_05:31:07:631] Get clientDMS = 8
    [12-16_05:31:07:661] Get clientNAS = 9
    [12-16_05:31:07:694] Get clientUIM = 10
    [12-16_05:31:07:726] Get clientWDA = 11
    [12-16_05:31:07:759] requestBaseBandVersion EC20CEHCLGR06A04M1G
    [12-16_05:31:07:854] requestGetSIMStatus SIMStatus: SIM_READY
    [12-16_05:31:07:886] requestGetProfile[1] ctnet///0
    [12-16_05:31:07:917] requestRegistrationState2 MCC: 460, MNC: 11, PS: Attached, DataCap: LTE
    [12-16_05:31:07:951] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
    [12-16_05:31:08:015] requestRegistrationState2 MCC: 460, MNC: 11, PS: Attached, DataCap: LTE
    [12-16_05:31:08:046] requestSetupDataCall WdsConnectionIPv4Handle: 0xe174f930
    [12-16_05:31:08:143] requestQueryDataCall IPv4ConnectionStatus: CONNECTED
    [12-16_05:31:08:174] ifconfig usb0 up
    [12-16_05:31:08:208] busybox udhcpc -f -n -q -t 5 -i usb0
    udhcpc: started, v1.31.1
    udhcpc: sending discover
    udhcpc: sending select for 10.26.232.226
    udhcpc: lease of 10.26.232.226 obtained, lease time 7200
    [12-16_05:31:08:451] /etc/udhcpc.d/50default: Adding DNS 202.96.128.86
    [12-16_05:31:08:451] /etc/udhcpc.d/50default: Adding DNS 202.96.134.133

**Test Connection**

.. code-block:: shell

    =====> Enter command:
    root@myzr-rzfive:~# ping -I usb0 www.baidu.com -c 2 -w 4

    =====> Output information:
    PING www.baidu.com (14.215.177.39): 56 data bytes
    64 bytes from 14.215.177.39: seq=0 ttl=54 time=43.305 ms
    64 bytes from 14.215.177.39: seq=1 ttl=54 time=28.630 ms

    --- www.baidu.com ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 28.630/35.967/43.305 ms

Copy and Update Image
------------------------

|   【Test Description】: Can update dtb, Image, kernel-modules.tar.bz2
|   【Interface Identification】: None
|   【System Device】: None

**Test Operations**

1. Copy the corresponding files to the current directory of the development board, taking tftp as an example

|   Open the tftpd software on the computer and set the address to the directory where the files to be replaced are located.
|   Connect this network port of the development board to the computer's network port with a network cable.

2. Test connection

.. code-block:: shell

    =====> Enter command:
    ping 192.168.137.99 -c 2 -w 4 
    =====> Output information:
    root@myzr-rzfive:~# ping 192.168.137.99 -c 2 -w 4
    PING 192.168.137.99 (192.168.137.99): 56 data bytes
    64 bytes from 192.168.137.99: seq=0 ttl=128 time=1.061 ms
    64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.546 ms

    --- 192.168.137.1 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.546/0.803/1.061 ms

|   "0% packet loss" indicates normal connection.

3. Transfer files

.. code-block:: shell

    =====> Enter command:
    tftp -gr kernel-image.tar.bz2 192.168.137.99
    tftp -gr kernel-modules.tar.bz2 192.168.137.99

4. Check if the system automatically mounts the partition

.. code-block:: shell

    =====> Enter command:
    ls /run/media/mmcblk0p1/
    =====> Output information:
    Image             kernel-modules.tar.bz2  ramsys.img
    kernel-image.tar.bz2  myzr-rzfive-2g.dtb      rootfs.tar.bz2

5. Update kernel and dtb files

.. code-block:: shell

    =====> Enter command:
    tar jxvf kernel-image.tar.bz2 -C /run/media/mmcblk0p1/
    =====> Output information:
    root@myzr-rzfive:~# tar jxvf kernel-image.tar.bz2 -C /run/media/mmcblk0p1/
    Image
    myzr-rzfive-2g.dtb

6. Update kernel modules

.. code-block:: shell

    =====> Enter command:
    tar jxvf kernel-modules.tar.bz2 -C /
    =====> Output information:
    root@myzr-rzfive:~# tar jxvf kernel-modules.tar.bz2 -C /
    lib/
    lib/modules/
    lib/modules/5.10.145-cip17-riscv-renesas/
    lib/modules/5.10.145-cip17-riscv-renesas/modules.softdep
    lib/modules/5.10.145-cip17-riscv-renesas/modules.order
    lib/modules/5.10.145-cip17-riscv-renesas/modules.symbols.bin
    lib/modules/5.10.145-cip17-riscv-renesas/modules.builtin
    lib/modules/5.10.145-cip17-riscv-renesas/modules.devname
    lib/modules/5.10.145-cip17-riscv-renesas/source