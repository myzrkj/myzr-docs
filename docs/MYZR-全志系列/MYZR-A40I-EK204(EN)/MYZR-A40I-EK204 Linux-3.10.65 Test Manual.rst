MYZR-A40I-EK204 Linux-3.10.65 Test Manual
===========================================

Ethernet Port Test
--------------------

| 【Test Description】: Test by having the development board send ICMP packets to the PC
| 【Interface Identification】: 10M/100M Ethernet-1
| 【System Interface】: eth0

**Test Operations**

|  Configure the IP address of the PC's wired network card to 192.168.137.99.
|  Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.
|  Configure the Ethernet port of the development board:

.. code-block:: shell

   =====> Enter command:
   ifconfig eth0 192.168.137.81

|  Test the Ethernet port:

.. code-block:: shell

   =====> Enter command:
   ping 192.168.137.99 -c 2 -w 4 
   =====> Output information:
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=0.570 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.365 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.365/0.467/0.570/0.104 ms

**Test Result**

|  "0% packet loss" indicates the test is passed.


USB Interface Test
--------------------

| 【Test Description】: Test by plugging and unplugging a USB storage device (USB flash drive)
| 【Interface Identification】: USB HOST
| 【System Interface】: /sys/bus/usb/

**Test Method**

|  Insert the USB device into the USB interface of the base board, and the system will output information similar to the following:

.. code-block:: 

   root@TinaLinux:/# [  795.551264] ehci_irq: highspeed device connect
   [  795.910089] usb 1-1: new high-speed USB device number 4 using sunxi-ehci
   [  796.081676] usb-storage 1-1:1.0: USB Mass Storage device detected
   [  796.110678] scsi1 : usb-storage 1-1:1.0
   [  797.111474] scsi 1:0:0:0: Direct-Access     Kingston DataTraveler 3.0 PMAP PQ: 0 ANSI: 6
   [  797.140157] sd 1:0:0:0: [sda] 60604416 512-byte logical blocks: (31.0 GB/28.8 GiB)
   [  797.156371] sd 1:0:0:0: [sda] Write Protect is off
   [  797.161892] sd 1:0:0:0: [sda] Mode Sense: 45 00 00 00
   [  797.169966] sd 1:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
   [  797.251578]  sda: sda1
   [  797.260467] CPU1: Booted secondary processor
   [  797.271003] sd 1:0:0:0: [sda] Attached SCSI removable disk
   [  797.489583]  sda: sda1
   [  797.622161] FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
   [  797.860430] CPU2: Booted secondary processor
   [  797.974464] FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|  Unplug the USB device from the base board, and the system will output information similar to the following:

.. code-block:: shell

   [  810.557018] ehci_irq: highspeed device disconnect
   [  810.562361] usb 1-1: USB disconnect, device number 4
   [  810.670680] udevd[2861]: inotify_add_watch(6, /dev/sda, 10) failed: No such file or directory

**Test Result**

|  The system is functioning normally if it outputs information similar to the above when the USB storage device is plugged in or unplugged.


TF Interface Test
-------------------

| 【Test Description】: Test by inserting and recognizing a TF card
| 【Interface Identification】: SD3
| 【System Interface】: /sys/bus/mmc/

**Test Method**

|  Insert the TF card into this interface:

.. code-block:: shell

   =====> Output information:
   root@TinaLinux:/# [   80.560114] sunxi-mmc sdc0: sdc set ios: clk 0Hz bm PP pm UP vdd 22 width 1 timing LEGACY(SDR12) dt B
   [   80.590139] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 22 width 1 timing LEGACY(SDR12) dt B
   [   80.620937] sunxi-mmc sdc0: smc 1 p0 err, cmd 52, RTO !!
   [   80.627845] sunxi-mmc sdc0: smc 1 p0 err, cmd 52, RTO !!
   [   80.634740] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 22 width 1 timing LEGACY(SDR12) dt B
   [   80.653529] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 22 width 1 timing LEGACY(SDR12) dt B
   [   80.670770] sunxi-mmc sdc0: smc 1 p0 err, cmd 5, RTO !!
   [   80.677415] sunxi-mmc sdc0: smc 1 p0 err, cmd 5, RTO !!
   [   80.687485] sunxi-mmc sdc0: smc 1 p0 err, cmd 5, RTO !!
   [   80.694393] sunxi-mmc sdc0: smc 1 p0 err, cmd 5, RTO !!
   [   80.702493] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 15 width 1 timing LEGACY(SDR12) dt B
   [   80.714629] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 15 width 1 timing LEGACY(SDR12) dt B
   [   80.733353] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 15 width 1 timing LEGACY(SDR12) dt B
   [   80.750809] CPU1: Booted secondary processor
   [   80.943958] mmc1: host does not support reading read-only switch. assuming write-enable.
   [   80.958125] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 15 width 1 timing SD-HS(SDR25) dt B
   [   80.970520] sunxi-mmc sdc0: sdc set ios: clk 50000000Hz bm PP pm ON vdd 15 width 1 timing SD-HS(SDR25) dt B
   [   80.982111] sunxi-mmc sdc0: sdc set ios: clk 50000000Hz bm PP pm ON vdd 15 width 4 timing SD-HS(SDR25) dt B
   [   80.993313] mmc1: new high speed SDHC card at address aaaa
   [   80.999904] mmcblk1: mmc1:aaaa SC16G 14.8 GiB 
   [   81.013518]  mmcblk1:
   [   81.016702] sndhdmi sndhdmi: ASoC: CPU DAI (null) not registered
   [   81.023541] sndhdmi sndhdmi: snd_soc_register_card() failed: -517
   [   81.030614] platform sndhdmi: Driver sndhdmi requests probe deferral
   [   81.103148] FAT-fs (mmcblk1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|  Eject the TF card:

.. code-block:: shell

   =====> Output information:
   root@TinaLinux:/# [  147.600144] sunxi-mmc sdc0: smc 1 p0 err, cmd 13, RTO !!
   [  147.606083] sunxi-mmc sdc0: smc 1 p0 err, cmd 13, RTO !!
   [  147.612251] sunxi-mmc sdc0: smc 1 p0 err, cmd 13, RTO !!
   [  147.618180] sunxi-mmc sdc0: smc 1 p0 err, cmd 13, RTO !!
   [  147.624573] mmc1: card aaaa removed
   [  147.637669] sunxi-mmc sdc0: sdc set ios: clk 0Hz bm OD pm OFF vdd 0 width 1 timing LEGACY(SDR12) dt B

|  The system is functioning normally if it outputs information similar to the above when the TF storage device is plugged in or unplugged.


Standard GPIO Test
--------------------

| 【Test Description】: Control the output level of GPIO
| 【Interface Identification】: GPIO/SD2
| 【System Interface】: /sys/class/gpio/


GPIO Low-Level Output Test
----------------------------

|  Method to configure P26:2 for low-level output:

.. code-block:: shell

   =====> Enter command:
   OUT_IO_OUT_NUM=270
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 

|  Test pin P26:2 with a multimeter. If the voltage is 0V, it indicates normal operation.


GPIO High-Level Output Test
-----------------------------

|  Method to configure P26:2 for high-level output:

.. code-block:: shell

   =====> Enter command:
   OUT_IO_OUT_NUM=270
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  Test pin P26:2 with a multimeter. If the voltage is 3.3V, it indicates normal operation.

**Others**

|  Command to control GPIO for low-level output:

.. code-block:: shell

   =====> Enter command:
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value   

|  Command to control GPIO for high-level output:

.. code-block:: shell

   =====> Enter command:
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 


GPIO-LED Test
---------------

| 【Test Description】: Control the LED
| 【Interface Identification】: LED
| 【System Interface】: /sys/class/leds/led*

**Test Operations**

|  Control the LED to turn off:

.. code-block:: shell

   echo 1 > /sys/class/leds/led1/brightness
   echo 1 > /sys/class/leds/led2/brightness
   echo 1 > /sys/class/leds/led3/brightness

|  Control the LED to turn on:

.. code-block:: shell

   echo 0 > /sys/class/leds/led1/brightness
   echo 0 > /sys/class/leds/led2/brightness
   echo 0 > /sys/class/leds/led3/brightness



GPIO-KEY Test
----------------

|  [Test Description]: Test with evtest
|  [Interface Identification]: KEY4, KEY4, KEY3, KEY2, KEY1
|  [System Interface]: /dev/input/event0

**Test Operation**

|  Run evtest to prepare for testing

.. code-block:: shell

   =====> Input command:
   evtest 

   =====> Output information:
   No device specified, trying to scan all of /dev/input/event*
   Available devices:
   /dev/input/event0:  sunxi-keyboard
   /dev/input/event1:  sunxi-ir
   /dev/input/event2:  axp22-powerkey
   Select the device event number [0-2]: 

|  Select the number corresponding to sunxi-keyboard

.. code-block:: shell

   =====> Input command:
   0

   =====> Output information:
   Input driver version is 1.0.1
   Input device ID: bus 0x19 vendor 0x1 product 0x1 version 0x100
   Input device name: "sunxi-keyboard"
   Supported events:
     Event type 0 (EV_SYN)
     Event type 1 (EV_KEY)
       Event code 28 (KEY_ENTER)
       Event code 102 (KEY_HOME)
       Event code 114 (KEY_VOLUMEDOWN)
       Event code 115 (KEY_VOLUMEUP)
       Event code 139 (KEY_MENU)
   Properties:
   Testing ... (interrupt to exit)

|  Press the buttons on the development board

.. code-block:: shell

   Event: time 1262304222.998060, type 1 (EV_KEY), code 102 (KEY_HOME), value 1
   Event: time 1262304222.998060, -------------- SYN_REPORT ------------
   Event: time 1262304223.162092, type 1 (EV_KEY), code 102 (KEY_HOME), value 0
   Event: time 1262304223.162092, -------------- SYN_REPORT ------------
   Event: time 1262304223.533178, type 1 (EV_KEY), code 28 (KEY_ENTER), value 1
   Event: time 1262304223.533178, -------------- SYN_REPORT ------------
   Event: time 1262304223.697226, type 1 (EV_KEY), code 28 (KEY_ENTER), value 0
   Event: time 1262304223.697226, -------------- SYN_REPORT ------------
   Event: time 1262304224.622976, type 1 (EV_KEY), code 139 (KEY_MENU), value 1
   Event: time 1262304224.622976, -------------- SYN_REPORT ------------
   Event: time 1262304224.923742, type 1 (EV_KEY), code 139 (KEY_MENU), value 0
   Event: time 1262304224.923742, -------------- SYN_REPORT ------------
   Event: time 1262304225.818243, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 1
   Event: time 1262304225.818243, -------------- SYN_REPORT ------------
   Event: time 1262304226.083851, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 0
   Event: time 1262304226.083851, -------------- SYN_REPORT ------------
   Event: time 1262304227.911909, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 1
   Event: time 1262304227.911909, -------------- SYN_REPORT ------------
   Event: time 1262304228.165801, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 0
   Event: time 1262304228.165801, -------------- SYN_REPORT ------------

**Test Result**

|  When a key is pressed, evtest will output the corresponding information.


Serial Port Test (RS232)
---------------------------

|  [Test Description]: Test using the serial port self-transmit and self-receive method
|  [Interface Identification]: UART
|  [System Device]: /dev/ttyS4

**Test Operation**

|  Short-circuit the transmit and receive pins of Serial Port 4 (TX and RX pins of RS232)
|  Execute the test command:

.. code-block:: shell

   =====> Input command:
   serial_test /dev/ttyS4 "www.myzr.com.cn"

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


Serial Port Test (RS485)
--------------------------

|  [Test Description]: Test using the serial port self-transmit and self-receive method
|  [Interface Identification]: UART
|  [System Device]: /dev/ttyS5/7

**Test Operation**

|  Short-circuit the transmit pin of Serial Port 5 with the receive pin of Serial Port 7 (TX pin of 485-1 and RX pin of 485-2)
|  Short-circuit the transmit pin of Serial Port 7 with the receive pin of Serial Port 5 (TX pin of 485-2 and RX pin of 485-1)
|  Execute the test command:

.. code-block:: shell

   =====> Input command:
   cat /dev/ttyS5 &
   echo www.myzr.com.cn > /dev/ttyS7
   =====> Output information:
   www.myzr.com.cn

   =====> Input command:
   killall cat
   cat /dev/ttyS7 &
   echo www.myzr.com.cn > /dev/ttyS5
   =====> Output information:
   www.myzr.com.cn


RTC Test
----------

|  [Test Description]: Read and set the time, then check if the time is correct after power-off and restart
|  [Interface Identification]: None
|  [System Device]: /sys/class/rtc/

**Test Operation**

1. Power off and restart the device, then check the current system time and hardware time:

.. code-block:: shell

   =====> Input command: 
   date

   =====> Output information:
   Fri Jan  1 08:00:29 CST 2010

2. Check the current RTC chip clock:

.. code-block:: shell

   =====> Input command: 
   hwclock 

   =====> Output information:
   Fri Jan  1 00:00:41 2010  0.000000 seconds

3. Set the system clock and synchronize it to the RTC chip

.. code-block:: shell

   =====> Input command: 
   date -s "2021-05-14 12:34:56" 

   =====> Output information:
   Fri May 14 12:34:59 CST 2021

4. Write the system clock to the hardware clock

.. code-block:: shell

   =====> Input command:
   hwclock -w

**Test Result**

   1. Power off and restart the evaluation board, then check the current system clock and hardware clock

.. code-block:: shell

   =====> Input command:
   date

   =====> Output information:
   Fri May 14 12:35:34 2021  0.000000 seconds
   2. Check the current RTC chip clock

   =====> Input command:
   hwclock  

   =====> Output information:
   Fri May 14 12:35:37 2021  0.000000 seconds

|  It can be seen that the obtained time is basically the same as the set time.


Audio Playback Test
----------------------

|  [Test Description]: Verify the audio playback function of the evaluation board by playing audio files.

**Test Operation**

|   Insert headphones into the audio jack of the development board.
|   Execute the test command:

.. code-block:: shell

   =====> Input command:
   aplay /test/test.wav 
   =====> Output information：
   Playing WAVE 'test.wav' : Signed 16 bit Little Endian, Rate 16000 Hz, Mono

**Test Result**

|  After executing the above test command, you will hear the sound output from the audio device.


Audio Recording Test
-----------------------

|  [Test Description]: Verify the audio recording function of the evaluation board by recording and playing the recorded file.
|  [Interface Identification]: MIC

**Test Operation**

|  Execute the test command:

.. code-block:: shell

   =====> Input command:
   arecord -d 5 -f S16_LE -t wav foobar.wav
   =====> Output information:
   Recording WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

|  Play the recording:

.. code-block:: shell

   =====> Input command:
   aplay foobar.wav

   =====> Output information:
   Playing WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

**Test Result**

|  After executing the above test command, you will hear the played recording.


Display Test
--------------

|  [Test Description]: Execute the display program.
|  [Interface Identification]: lvds/lcd/dsi
|  [System Device]: fb0

**Test Operation**

1. Connect the display after shutting down the device
2. Execute the command

.. code-block:: shell

   df_andi

WIFI Test
------------

|  [Test Description]: Use RTL8723du as a wireless network card to connect to the WIFI AP.
|  [Interface Identification]: WIFI, WIFI_ANT
|  [System Device]: wlan0

**Test Operation**

1. Confirm that a WIFI module is attached at the "WIFI" mark; otherwise, no need to perform the test.
2. Connect the WIFI antenna to the interface marked "WIFI_ANT".

.. code-block:: shell

   =====> Input command:
   wifi_connect_ap_test MYZR-WIFI myzr2012

|  MYZR-WIFI is the WIFI name and myzr2012 is the password
|  Test the connection

.. code-block:: shell

   =====> Input command:
   ping -I wlan0 www.baidu.com -c 2 -w 4

   =====> Output information:
   PING www.baidu.com (163.177.151.109): 56 data bytes
   64 bytes from 163.177.151.109: seq=0 ttl=56 time=9.776 ms
   64 bytes from 163.177.151.109: seq=1 ttl=56 time=9.620 ms

   --- www.baidu.com ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 9.620/9.698/9.776 ms

**Test Result**

|  "0% packet loss" indicates that the WIFI connection is normal.


Bluetooth Test
----------------

|  [Test Description]: After scanning for Bluetooth devices, send an L2CAP response request and receive the reply.
|  [System Device]: hci0

1. Confirm that a WIFI module is attached at the "WIFI" mark; otherwise, no need to perform the test.
2. Connect the WIFI antenna to the interface marked "WIFI_ANT".

|  Configure the Bluetooth system interface

.. code-block:: shell

   =====> Input command:
   hciconfig hci0 up
   hciconfig hci0 piscan
   hciconfig -a
   hci0:   Type: BR/EDR  Bus: USB
       BD Address: 74:EE:2A:45:64:EC  ACL MTU: 1021:8  SCO MTU: 255:12
       UP RUNNING PSCAN ISCAN 
       RX bytes:1403 acl:0 sco:0 events:59 errors:0
       TX bytes:786 acl:0 sco:0 commands:59 errors:0
       Features: 0xff 0xff 0xff 0xfa 0xdb 0xbd 0x7b 0x87
       Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3 
       Link policy: RSWITCH HOLD SNIFF PARK 
       Link mode: SLAVE ACCEPT 
       Name: 'RTK_BT_4.1'
       Class: 0x000000
       Service Classes: Unspecified
       Device Class: Miscellaneous, 
       HCI Version: 4.1 (0x7)  Revision: 0x82a8
       LMP Version: 4.1 (0x7)  Subversion: 0x2df4
       Manufacturer: Realtek Semiconductor Corporation (93)
       [   54.305172] rtk_btcoex: BTCOEX hci_rev 0x82a8
       [   54.311358] rtk_btcoex: BTCOEX lmp_subver 0x2df4

|  Check the Bluetooth device information of the board

.. code-block:: shell

   =====> Input command:

      hcitool dev
   =====> Output information:

      Devices:
      hci0    74:EE:2A:45:64:EC

2. Scan for external Bluetooth devices

.. code-block:: shell

   =====> Input command:

      hcitool scan
   =====> Output information:

      Scanning ...
      ......
      7C:2A:DB:08:EF:70    Redmi K30 Pro

3. Send an L2CAP packet for testing

.. code-block:: shell

   =====> Input command:

      l2ping  7C:2A:DB:08:EF:70 -c 2
   =====> Output information:

   Ping: 7C:2A:DB:08:EF:70 from 74:EE:2A:45:64:EC (data size 44) ...
   44 bytes from 7C:2A:DB:08:EF:70 id 0 time 7.89ms
   44 bytes from 7C:2A:DB:08:EF:70 id 1 time 24.88ms
   44 bytes from 7C:2A:DB:08:EF:70 id 2 time 9.80ms
   ^C3 sent, 3 received, 0% loss

**Test Result**

|  "0% packet loss" indicates that the Bluetooth connection is normal.


EC20 Module Test
------------------

|  [Test Description]: After successful 4G connection, the development board sends ICMP packets to the external network to verify that the connection is normal.
|  [System Device]: usb0

**Test Operations**

1. Power off the development board, connect the 4G module, connect the antenna and insert the SIM card, then start the evaluation board.
2. Use the command to establish a network connection:

.. code-block:: shell

   =====> Enter command:

      /etc/quectel-CM

|  Test connection:

.. code-block:: shell

   =====> Enter command:

      ping www.baidu.com -c 2 -w 4
   =====> Output information:

   PING www.a.shifen.com (183.232.231.172) from 10.77.19.81 ppp0: 56(84) bytes of data.
   64 bytes from 183.232.231.172: icmp_seq=1 ttl=56 time=197 ms
   --- www.a.shifen.com ping statistics ---
   1 packets transmitted, 1 received, 0% packet loss, time 0ms
   rtt min/avg/max/mdev = 197.497/197.497/197.497/0.000 ms

**Test Result** 　

|  "0% packet loss" indicates that the WIFI connection is normal.