
MYZR-IMX6-EK200 Linux-4.1.15 Test Manual v2.0
================================================

Part I ：Testing Instructions
--------------------------------

Test Environment
~~~~~~~~~~~~~~~~~~

|  【Development board model】：MYZR-IMX6-EK200-6Q-1G
|  【Kernel version】：Linux-4.1.15
|  【File system】：L4115-fsl-image-qt5-myimx6a9.tar.bz2
|  【Tool version】：MfgTool-MYIMX6A9-L4.1.15-Patch.svn297.rar
|  Note：In order to ensure the test is correct, the recommended version of the burning tool should be no less than svn297

Interface identification map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/1275px-Myimx6ek200_front.jpg
   :alt: 1275px-Myimx6ek200_front.jpg

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/963px-Myimx6ek200_rear_view.jpg
   :alt: 963px-Myimx6ek200_rear_view.jpg

Part II Interface Testing
-----------------------------

Network port test
~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Test the way that the development board sends ICMP packets to the PC.
|  【Interface identifier】：10M/100M Ethernet-1
|  【System interface】：eth0

**Test operation**

|  Configure the computer wired network card IP to 192.168.137.99.
|  Connect the network port of the development board with the network cable and the computer network port.
|  Configure the development board network port:

.. code-block:: shell

   =====> Enter the command:
   ifconfig eth1 down
   ifconfig eth0 192.168.137.81

|  Test network port:

.. code-block:: shell

   =====> Enter the command:
   ping 192.168.137.99 -c 2 -w 4 

   =====> Output information:
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=0.570 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.365 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.365/0.467/0.570/0.104 ms

**Test Results**

|  “0% packet loss”means the test passed.

Network port two test
~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Test the way that the development board sends ICMP packets to the PC.
|  【Interface identifier】：10M/100M Ethernet-2
|  【System interface】：eth1

**Test operation**

|  Configure the computer wired network card IP to 192.168.137.99.
|  Connect the network port of the development board with the network cable and the computer network port.
|  Configure the development board network port:

.. code-block:: shell

   =====> Enter the command:
   ifconfig eth0 down
   ifconfig eth1 192.168.137.82 

|  Test network port:

.. code-block:: shell

   =====> Enter the command:
   ping 192.168.137.99 -c 2 -w 4 

   =====> Output information:
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=1.38 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.627 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1001ms
   rtt min/avg/max/mdev = 0.627/1.003/1.380/0.377 ms

**Test Results**

|  “0% packet loss”means the test passed.

USB interface test
~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Test by plugging and unplugging a USB storage device (U disk)
|  【Interface identifier】：USB HOST
|  【System interface】：/sys/bus/usb/

**Test Methods**

|  Insert the USB device into the backplane USB interface and the system will output a message similar to the following:

.. code-block:: shell

   usb 1-1.2: new high-speed USB device number 5 using ci_hdrc
   usb-storage 1-1.2:1.0: USB Mass Storage device detected
   scsi host1: usb-storage 1-1.2:1.0
   scsi 1:0:0:0: Direct-Access     Mass     Storage Device   1.00 PQ: 0 ANSI: 0 CCS
   sd 1:0:0:0: Attached scsi generic sg0 type 0
   sd 1:0:0:0: [sda] 60776448 512-byte logical blocks: (31.1 GB/28.9 GiB)
   sd 1:0:0:0: [sda] Write Protect is off
   sd 1:0:0:0: [sda] No Caching mode page found
   sd 1:0:0:0: [sda] Assuming drive cache: write through
    sda: sda1
   sd 1:0:0:0: [sda] Attached SCSI removable disk

|  Pull the USB device out of the backplane and the system will output a message similar to the following:

.. code-block:: shell

   usb 1-1.2: USB disconnect, device number 5

**Test Results**

|  When the USB storage device is plugged and unplugged, the system outputs the above information to indicate normal.

SD interface test
~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Test by inserting and identifying a TF card
|  【Interface identifier】：SD3
|  【System interface】：/sys/bus/mmc/

**Test Methods**

|  Insert the SD card into this interface:

.. code-block:: shell

   =====> Output information:
   mmc2: new high speed SDHC card at address 1234
   mmcblk2: mmc2:1234 SA32G 28.9 GiB 
    mmcblk2: p1

|  Pop up the SD card:

.. code-block:: shell

   =====> Output information:
   mmc2: card 1234 removed

**Test Results**

|  When the SD storage device is plugged and unplugged, the system outputs the above information to indicate normal.

Standard GPIO test
~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Control the output level of the GPIO
|  【Interface identifier】：GPIO/SD2
|  【System interface】：/sys/class/gpio/

**IO available for MYZR-IMX6-EK200**

.. code-block:: shell

   J4:3(15),  J4:5(14),  J4:7(10), J4:9(13),   J4:11(12),  J4:13(11)  
   J4:4(LED), J4:6(LED), J4:8(20), J4:10(LED), J4:12(LED), J4:14(NC)  

**GPIO output low level test**

|  Configure J4:8 to output low level operation method:

.. code-block:: shell

   =====> Enter the command:
   OUT_IO_OUT_NUM=20
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 

|  Test the pin J4:8 with a multimeter, the voltage is 0V, it means OK

**GPIO output high level test**

|  Configure J4:7 to output high level operation method:

.. code-block:: shell

   =====> Enter the command:
   OUT_IO_OUT_NUM=10 
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  Test the pin J4:7 with a multimeter, the voltage is 3.3V, it means OK

**Other**

|  Instructions to control GPIO output low level:

.. code-block:: shell

   =====> Enter the command:
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value  

|  Instructions to control GPIO output high level:

.. code-block:: shell

   =====> Enter the command:
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 

GPIO-LED Test（leds-heartbeat）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Observe the leds of leds-heartbeat
|  【Interface identifier】：GPIO-LED
|  【System interface】：/sys/class/leds/leds-heartbeat/

**Test operation**

|  No need for any operation.

**Test Results**

|  After the system is started, you can see that D7 is flashing regularly, which means it should function normally.

GPIO-LED Test（leds-mmc3）
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Write data to eMMC while observing LEDs of leds-mmc3
|  【Interface identifier】：GPIO-LED
|  【System interface】：/sys/class/leds/leds-mmc3/

**Test operation**

.. code-block:: shell

   =====> Enter the command:
   dd if=/dev/zero of=/home/root/test bs=1024k count=128

**Test Results**

|  You can see that when you write data to eMMC, D8 is bright.

GPIO-LED Test（leds-timer）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Observe led-time LEDs
|  【Test instruction】：Control the lighting time of led-time(LED)
|  【Interface identifier】：GPIO-LED
|  【System interface】：/sys/class/leds/leds-timer/

**Test operation**

|  Change the time of led-time(D9) extinction

.. code-block:: shell

   =====> Enter the command:
   echo 1000 > /sys/class/leds/leds-timer/delay_off  

|  Change the time that led-timer (D9) is on

.. code-block:: shell

   =====> Enter the command:
   echo 2000 > /sys/class/leds/leds-timer/delay_on 

**Test Results**

|  After executing the instruction, it is observed that the proportion of time for the corresponding LED to be on and off is basically 2:1.

GPIO-LED Test（leds-gpio）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Control the on and off time of ledss-gpio (LED)
|  【Interface identifier】：LED
|  【System interface】：/sys/class/leds/leds-gpio/

**Test operation**

|  Make the light (D10) off：

.. code-block:: shell

   =====> Enter the command:
   echo 0 > /sys/class/leds/leds-gpio/brightness  

|  Turn the light(D10) on：

.. code-block:: shell

   =====> Enter the command:
   echo 1 > /sys/class/leds/leds-gpio/brightness  

**Test Results**

|  After executing the instruction, it is found that the state of the corresponding LED changes with the function of the instruction.

GPIO-KEY test
~~~~~~~~~~~~~~

|  【Test instruction】：Use evtest for testing
|  【Interface identifier】：KEY3, KEY2, KEY1
|  【System interface】：/dev/input/eventX

**Test operation**

|  Run evtest to prepare for testing

.. code-block:: shell

   =====> Enter the command:
   evtest 

   =====> Output information:
   No device specified, trying to scan all of /dev/input/event*
   Available devices:
   /dev/input/event0:  WM8962 Beep Generator
   /dev/input/event1:  gpio-keys
   Select the device event number [0-1]:

|  Select the serial number corresponding to gpio-keys

.. code-block:: shell

   =====> Enter the command:
   1

   =====> Output information:
   Input driver version is 1.0.1
   Input device ID: bus 0x19 vendor 0x1 product 0x1 version 0x100
   Input device name: "gpio-keys"
   Supported events:
     Event type 0 (EV_SYN)
     Event type 1 (EV_KEY)
       Event code 114 (KEY_VOLUMEDOWN)
       Event code 115 (KEY_VOLUMEUP)
       Event code 116 (KEY_POWER)
   Properties:
   Testing ... (interrupt to exit)

|  Press the button on the development board

.. code-block:: shell

   Event: time 1537921332.815219, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 1
   Event: time 1537921332.815219, -------------- SYN_REPORT ------------
   Event: time 1537921332.985211, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 0
   Event: time 1537921332.985211, -------------- SYN_REPORT ------------
   Event: time 1537921335.355204, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 1
   Event: time 1537921335.355204, -------------- SYN_REPORT ------------
   Event: time 1537921335.535203, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 0
   Event: time 1537921335.535203, -------------- SYN_REPORT ------------
   Event: time 1537921337.375207, type 1 (EV_KEY), code 116 (KEY_POWER), value 1
   Event: time 1537921337.375207, -------------- SYN_REPORT ------------
   Event: time 1537921337.535204, type 1 (EV_KEY), code 116 (KEY_POWER), value 0
   Event: time 1537921337.535204, -------------- SYN_REPORT ------------

**Test Results**

|  When a button is pressed, evtest will output the corresponding information.

Serial test（UART2）
~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Test by serial port self-receiving
|  【Interface identifier】：UART2/3/4/5_TTL
|  【System equipment】：/dev/ttymxc1

**Test operation**

|  Short the serial port 2 transmit and receive pin (J1 pins 7 and 9)
|  Execute test instructions:

.. code-block:: shell

   =====> Enter the command:
   /my-demo/gcc-linaro-5.3-arm/serial_test.out /dev/ttymxc1 "www.myzr.com.cn"  
   
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
   ASCII: 0x0       Character:   

**Test Results**

|  After executing the test command, the application output is similar to the above information.

Serial test（UART3）
~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Test by serial port self-receiving
|  【Interface identifier】：UART2/3/4/5_TTL
|  【System equipment】：/dev/ttymxc2

**Test operation**

|  Short-circuit the transmit and receive pins of serial port 3 (pins 11 and 13 of J1)
|  Execute test instructions:

.. code-block:: shell

   =====> Enter the command:
   /my-demo/gcc-linaro-5.3-arm/serial_test.out /dev/ttymxc2 "www.myzr.com.cn"  

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
   ASCII: 0x0       Character:   

**Test Results**

|  After executing the test instruction, the application output similar information as above is normal.

Serial test（UART4）
~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Test by serial port self-receiving
|  【Interface identifier】：UART2/3/4/5_TTL
|  【System equipment】：/dev/ttymxc3

**Test operation**

|  Short-circuit the transmit and receive pins of serial port 4 (pins 15 and 17 of J1)
|  Execute test instructions:

.. code-block:: shell

   =====> Enter the command:
   /my-demo/gcc-linaro-5.3-arm/serial_test.out /dev/ttymxc3 "www.myzr.com.cn"  

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
   ASCII: 0x0       Character:   

**Test Results**

|  After executing the test instruction, the application output similar information as above is normal.

串口测试（UART5）
~~~~~~~~~~~~~~~~~~

|  【Test instruction】：The serial port self - collecting method was used to test
|  【Interface identifier】：UART2/3/4/5_TTL
|  【System equipment】：/dev/ttymxc4

**Test operation**

|  Short-circuit the transmit and receive pins of serial port 5 (pins 16 and 18 of J1)
|  Execute test instructions:

.. code-block:: shell

   =====> Enter the command:
   /my-demo/gcc-linaro-5.3-arm/serial_test.out /dev/ttymxc4 "www.myzr.com.cn"  

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
   ASCII: 0x0       Character:  

**Test Results**

|  After executing the test instruction, the application output similar information as above is normal.

CAN test
~~~~~~~~~

|  【Test instruction】：CAN1 sending and CAN0 receiving are adopted.
|  【Interface identifier】：CAN1，CAN2
|  【System interface】：can0，can1

**测试准备**

|  Connect CAN_L of CAN1 to CAN_L of CAN2.
|  Connect CAN_H of CAN1 to CAN_H of CAN2.

**测试命令**

|  Configure CAN1（can0）：

.. code-block:: shell

   =====> Enter the command:
   ip link set can0 up type can bitrate 125000

|  Configure CAN2（can1）：

.. code-block:: shell

   =====> Enter the command:
   ip link set can1 up type can bitrate 125000

|  CAN1 (can0) background reception ：

.. code-block:: shell

   =====> Enter the command:
   candump can0 &  

|  CAN2（can1）send data:

.. code-block:: shell

   =====> Enter the command:
   cansend can1 1F334455#1122334455667788 

   =====> Output information:
   can0  1F334455   [8]  11 22 33 44 55 66 77 88

**Test Results**

|  After CAN2 (can1) transmits data, CAN1 (can0) will output the received data, such as: 11 22 33 44 55 66 77 88

SPI test（ECSPI1）
~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Tested by spontaneous self-receiving.
|  【Interface identifier】：SPI1/2
|  【System equipment】：/dev/spidev0.1

**Test operation**

|  Short the 7 and 9 pins of J7.
|  Execute test instruction

.. code-block:: shell

   =====> Enter the command:
   /my-demo/gcc-linaro-5.3-arm/spidev_test.out -D /dev/spidev0.1   

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

**Test Results**

|  After executing the test instruction, the application output similar information as above is normal.

SPI测试（ECSPI2）
~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Tested by spontaneous self-receiving.
|  【Interface identifier】：SPI1/2
|  【System equipment】：/dev/spidev1.0

**Test operation**

|  Short the 8 and 10 pins of the J7.
|  Execute test instructions

.. code-block:: shell

   =====> Enter the command:
   /my-demo/gcc-linaro-5.3-arm/spidev_test.out -D /dev/spidev1.0   

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

**Test Results**

|  After Execute test instructions, the application output is similar to the above information.

Watchdog 超时复位测试
~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Turn on the watchdog and wait for the watchdog to time out, generating a reset.
|  【Interface identifier】：None
|  【System equipment】：/dev/watchdog

**Test operation**

|  Run the watchdog program：

.. code-block:: shell

   =====> Enter the command:
   /unit_tests/wdt_driver_test.out 10 15 1  
   
   =====> Output information:
   Starting wdt_driver (timeout: 10, sleep: 15, test: write)
   Trying to set timeout value=10 seconds
   The actual timeout was set to 10 seconds
   Now reading back -- The timeout is 10 seconds

**Test Results**

|  After running the test command for 10 seconds, WatchDog times out and the system is reset. The information that will see the system restart output at the terminal is similar to the following:

.. code-block:: shell

   U-Boot 2016.03-svn351 (Jan 25 2019 - 10:13:51 +0800)

   CPU:   Freescale i.MX6Q rev1.5 996 MHz (running at 792 MHz)
   CPU:   Extended Commercial temperature grade (-20C to 105C) at 48C
   Reset cause: WDOG
   Board: MYZR i.MX6 Evaluation Kit
   Model: MY-IMX6-EK200-6Q-1G

Watchdog Feeding dog test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Turn on the watchdog and feed the app to the dog.
|  【Interface identifier】：None
|  【System equipment】：/dev/watchdog

**Test operation**

|  Run the watchdog program and set the timeout to 4 seconds and the dog interval to 2 seconds:

.. code-block:: shell

   =====> Enter the command:
   /unit_tests/wdt_driver_test.out 4 2 1 &  
   
   =====> Output information:
   [1] 1026
   Starting wdt_driver (timeout: 4, sleep: 2, test: write)
   Trying to set timeout value=4 seconds
   The actual timeout was set to 4 seconds
   Now reading back -- The timeout is 4 seconds

RTC test
~~~~~~~~~~

|  【Test instruction】：Read and set the time, check the time is correct after power off and restart
|  【Interface identifier】：None
|  【System equipment】：/sys/class/rtc/rtc0/

**Test operation**

1. Power off and restart the device to check the current system time and hardware time:

.. code-block:: shell

   =====> Enter the command: 
   date

   =====> Output information:
   Tue Sep 25 22:47:03 UTC 2018

2. View the current RTC chip clock:

.. code-block:: shell

   =====> Enter the command: 
   hwclock 

   =====> Output information:
   Tue Sep 25 22:47:18 2018  0.000000 seconds

3. Set the system clock and sync to the RTC chip

.. code-block:: shell

   =====> Enter the command: 
   date -s "2019-01-14 12:34:56"  

   =====> Output information:
   Mon Jan 14 12:34:56 UTC 2019

4. Write the system clock to the hardware clock

.. code-block:: shell

   =====> Enter the command:
   hwclock -w  

**Test Results**

1. Power off the evaluation board to view the current system clock and hardware clock

.. code-block:: shell

   =====> Enter the command:
   date

   =====> Output information:
   Mon Jan 14 12:36:22 UTC 2019

2. View the current RTC chip clock

.. code-block:: shell

   =====> Enter the command:
   hwclock  

   =====> Output information:
   Mon Jan 14 12:36:40 2019  0.000000 seconds

|  It can be seen that the time we get is basically the same as the time set.

WakeAlarm Wake up test
~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Set the wakealarm event, then put the system to sleep and wait for the wakealarm event to wake up.
|  【Interface identifier】：None
|  【System equipment】：Such as /sys/class/rtc/rtc1/wakealarm

**Test operation**

1. Set rtc1 to generate a wakealarm event after 10 seconds

.. code-block:: shell

   =====> Enter the command:
   echo +10 > /sys/class/rtc/rtc1/wakealarm 

2. Put the device to sleep

.. code-block:: shell

   =====> Enter the command:
   echo mem > /sys/power/state

   =====> Output information:
   PM: Syncing filesystems ... done.
   Freezing user space processes ... (elapsed 0.001 seconds) done.
   Freezing remaining freezable tasks ... (elapsed 0.001 seconds) done.
   Suspending console(s) (use no_console_suspend to debug)

**Test Results**

1. You can see that the LEDs of the development board except the power indicator are off.
2. The state of the LED is restored again within 10 seconds, and the system outputs something like the following:

.. code-block:: shell

   PM: suspend of devices complete after 90.667 msecs
   PM: suspend devices took 0.090 seconds
   PM: late suspend of devices complete after 1.286 msecs
   PM: noirq suspend of devices complete after 1.272 msecs
   Disabling non-boot CPUs ...
   CPU1: shutdown
   CPU2: shutdown
   CPU3: shutdown
   Enabling non-boot CPUs ...
   CPU1 is up
   CPU2 is up
   CPU3 is up
   PM: noirq resume of devices complete after 1.140 msecs
   PM: early resume of devices complete after 1.114 msecs
   PM: resume of devices complete after 760.379 msecs
   PM: resume devices took 0.760 seconds
   Restarting tasks ... done.

Audio playback test
~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Verify the audio playback of the EV kit by playing an audio file.
|  【Interface identifier】：EAR
|  【System equipment】：wm8960-audio

**Test operation**

|  Plug the headset into the "EAR" port of the board.
|  Execute the test command:

.. code-block:: shell

   =====> Enter the command:
   aplay /unit_tests/audio8k16S.wav   

   =====> Output information:
   Playing WAVE '/unit_tests/audio8k16S.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Stereo

**Test Results**

|  After the above test command is executed, the sound output from the audio device will be heard.

Audio recording test
~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Verify the audio recording function of the EV kit by recording and playing the recording file.
|  【Interface identifier】：MIC
|  【System equipment】：wm8960-audio

**Test operation**

1. Plug the headset with the MIC into the “MIC” port of the development board.
2. Execute the recording command:

.. code-block:: shell

   =====> Enter the command:
   arecord -d 5 -f S16_LE -t wav foobar.wav

   =====> Output information:
   Recording WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

3. 执行录音命令：

.. code-block:: shell

   =====> Enter the command:
   aplay foobar.wav

   =====> Output information:
   Playing WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

**Test Results**

|  The recorded recording will be heard after executing the above test command.

Part III Display function test
----------------------------------

Operating instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

**Each display function test needs to restart the system to enter the u-boot command line and execute the command under the u-boot command line.**

Single screen display
~~~~~~~~~~~~~~~~~~~~~~~

- LVDS1 display

|  Note: The default is LVDS1 display, that is, LVDS1 is the display device when it is not intervened after power-on. Explicitly configure LVDS1 as the display method:

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds1; saveenv; boot

- LVDS0 display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds0; saveenv; boot

- HDMI display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_hdmi; saveenv; boot

- LCD(RGB) display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lcd; saveenv; boot

Dual LVDS screen display
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- LVDS1 + LVDS0 Dual screen sync display

.. code-block:: shell

   run load_scr; source; setenv display $disp_lvds_dul; saveenv; boot

- LVDS1 + LVDS0(fb4) Dual screen asynchronous display

.. code-block:: shell

   run load_scr; source; setenv display $disp_lvds_sep; saveenv; boot

Dual screen asynchronous display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- LVDS1 + HDMI Dual screen asynchronous display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds1 $disp_fb1_hdmi; saveenv; boot

- LVDS1 + LCD(RGB) Dual screen asynchronous display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds1 $disp_fb1_lcd; saveenv; boot

- LVDS0 + HDMI Dual screen asynchronous display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds0 $disp_fb1_hdmi; saveenv; boot

- LVDS0 + LCD(RGB) Dual screen asynchronous display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds0 $disp_fb1_lcd; saveenv; boot

- HDMI + LVDS1 Dual screen asynchronous display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_hdmi $disp_fb1_lvds1; saveenv; boot

- HDMI + LVDS0 Dual screen asynchronous display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_hdmi $disp_fb1_lvds0; saveenv; boot

- LCD(RGB) + LVDS1 Dual screen asynchronous display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lcd $disp_fb1_lvds1; saveenv; boot

- LCD(RGB) + LVDS0 Dual screen asynchronous display

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lcd $disp_fb1_lvds0; saveenv; boot


Part IV Expansion Module Function Demo
------------------------------------------

RTL8188 Module function demonstration（WIFI Client）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Connect to the WIFI AP using the RTL8188 as a wireless network card.
|  【Interface identifier】：WIFI、WIFI_ANT
|  【System equipment】：wlan0

**Test operation**

1. Make sure that the WIFI module is attached to the “WIFI” logo, otherwise no testing is required.
2. Connect the WIFI antenna to the interface labeled "WIFI_ANT".
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

   =====> Output information:
   Successfully initialized wpa_supplicant
   rfkill: Cannot open RFKILL control device
   ==> rtl8188e_iol_efuse_patch 
   IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
   ......

5. Get IP

.. code-block:: shell

   =====> Enter the command:
   udhcpc -i wlan0

   =====> Output information:
   udhcpc (v1.23.1) started
   Sending discover...
   Sending select for 192.168.43.121...
   Lease of 192.168.43.121 obtained, lease time 3600
   /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

6. Test connection

.. code-block:: shell

   =====> Enter the command:
   ping -I wlan0 192.168.43.1 -c 2 -w 4

   =====> Output information:
   PING 192.168.43.1 (192.168.43.1) from 192.168.43.130 wlan0: 56(84) bytes of data.
   64 bytes from 192.168.43.1: icmp_seq=1 ttl=64 time=5.66 ms
   64 bytes from 192.168.43.1: icmp_seq=2 ttl=64 time=9.22 ms

   --- 192.168.43.1 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1000ms
   rtt min/avg/max/mdev = 5.663/7.444/9.226/1.783 ms

**Test Results**

|  “0% packet loss” means WIFI connection is normal.


RTL8188 Module function demonstration（WIFI AP mode）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instruction】：Use RTL8188 as the WIFI AP and connect your phone to this AP.
|  【Interface identifier】：WIFI、WIFI_ANT
|  【System equipment】：wlan0

**Test operation**

1. Make sure that the WIFI module is attached to the “WIFI” logo, otherwise no testing is required.
2. Connect the WIFI antenna to the interface labeled "WIFI_ANT".
3. Configure IP for wlan0:

.. code-block:: shell

   =====> Enter the command:
   ifconfig wlan0 192.168.99.1

   =====> Output information:
   ==> rtl8188e_iol_efuse_patch
   IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready

4. Enable the DHCP service for wlan0:

.. code-block:: shell

   =====> Enter the command:
   touch /var/lib/misc/udhcpd.leases
   udhcpd -f /etc/my_udhcpd.conf &

   =====> Output information:
   [1] 469
   udhcpd (v1.23.1) started

5. Enable Host-AP feature for wlan0

.. code-block:: shell

   =====> Enter the command:
   hostapd /etc/my_hostapd.conf -B

   =====> Output information:
   Configuration file: /etc/my_hostapd.conf
   rfkill: Cannot open RFKILL control device
   Using interface wlan0 with hwaddr e0:b9:4d:7f:e4:40 and ssid "MY_HOSTAP_V25"
   RTL871X: set group key camid:1, addr:00:00:00:00:00:00, kid:1, type:AES
   wlan0: interface state UNINITIALIZED->ENABLED
   wlan0: AP-ENABLED

6. Client device connected to Host-AP

|  At this point, the development board's Host-AP function is enabled, the client device can search for "MY_HOSTAP_V25" and connect to this AP with the password "myzr2012".

**Test Results**

1. Information generated when the device is successfully connected

.. code-block:: shell

   =====> Output information:
   Sending OFFER of 192.168.12.20
   Sending OFFER of 192.168.12.20
   Sending ACK to 192.168.12.20

2. Information generated when a device is disconnected

.. code-block:: shell

   =====> Output information:
   RTL871X: OnDeAuth(wlan0) reason=3, ta=b4:0b:44:f5:64:2f
   RTL871X: clear key for addr:b4:0b:44:f5:64:2f, camid:4

EC20 Module test
~~~~~~~~~~~~~~~~~~

|  【Test instruction】：After the 4G connection is successful, the development board sends an ICMP packet to the external network to verify that the connection is normal.
|  【Interface identifier】：MINI_PCIE
|  【System equipment】：eth2

**Test operation**

1. The development board is powered off, connected to the 4G module, connected to the antenna and inserted into the SIM card to start the evaluation board.
2. Use the instructions to make a network connection:

.. code-block:: shell

   =====> Enter the command:
   /my-demo/gcc-linaro-5.3-arm/quectel-CM &

   =====> Output information:
   [1] 540
   [12-18_03:17:06:719] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
   [12-18_03:17:06:720] /my-demo/gcc-linaro-5.3-arm/quectel-CM profile[1] = (null)/(null)/(null)/0, pincode = (null)
   [12-18_03:17:06:723] Find /sys/bus/usb/devices/1-1.2 idVendor=2c7c idProduct=0125
   [12-18_03:17:06:723] Find /sys/bus/usb/devices/1-1.2:1.4/net/eth2
   [12-18_03:17:06:723] Find usbnet_adapter = eth2
   [12-18_03:17:06:723] Find /sys/bus/usb/devices/1-1.2:1.4/GobiQMI/qcqmi2
   [12-18_03:17:06:724] Find qmichannel = /dev/qcqmi2
   [12-18_03:17:06:794] Get clientWDS = 7
   [12-18_03:17:06:826] Get clientDMS = 8
   [12-18_03:17:06:858] Get clientNAS = 9
   [12-18_03:17:06:890] Get clientUIM = 10
   [12-18_03:17:06:922] Get clientWDA = 11
   [12-18_03:17:06:954] requestBaseBandVersion EC20CEFAR02A10M4G
   [12-18_03:17:07:050] requestGetSIMStatus SIMStatus: SIM_READY
   [12-18_03:17:07:082] requestGetProfile[1] cmnet///0
   [12-18_03:17:07:114] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [12-18_03:17:07:146] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
   [12-18_03:17:07:223] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [12-18_03:17:07:274] requestSetupDataCall WdsConnectionIPv4Handle: 0x8777e7a0
   [12-18_03:17:07:370] requestQueryDataCall IPv4ConnectionStatus: CONNECTED
   [12-18_03:17:07:403] ifconfig eth2 up
   [12-18_03:17:07:452] busybox udhcpc -f -n -q -t 5 -i eth2
   [12-18_03:17:07:492] udhcpc (v1.23.1) started
   [12-18_03:17:07:656] Sending discover...
   [12-18_03:17:07:706] Sending select for 10.25.154.46...
   [12-18_03:17:07:766] Lease of 10.25.154.46 obtained, lease time 7200
   [12-18_03:17:07:888] /etc/udhcpc.d/50default: Adding DNS 211.136.17.107
   [12-18_03:17:07:888] /etc/udhcpc.d/50default: Adding DNS 211.136.20.203

3. Test connection

.. code-block:: shell

   =====> Enter the command:
   ping -I eth2 www.baidu.com -c 2 -w 4

   =====> Output information:
   PING www.baidu.com (14.215.177.38): 56 data bytes
   64 bytes from 14.215.177.38: seq=0 ttl=49 time=15.753 ms
   64 bytes from 14.215.177.38: seq=1 ttl=49 time=11.835 ms

   --- www.baidu.com ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 11.835/13.794/15.753 ms

**Test Results**

|  “0% packet loss”Indicates that the WIFI connection is normal.