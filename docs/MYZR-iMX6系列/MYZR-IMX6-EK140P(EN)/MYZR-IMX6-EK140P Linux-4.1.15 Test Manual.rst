MYZR-IMX6-EK140P Linux-4.1.15 Test Manual
============================================

Test Environment
-------------------

- Development board model：MYZR-IMX6-EK140P-6Y-512M-4G
- Kernel version：Linux-4.1.15
- File system：L4115-core-image-base-myimx6a7.tar.bz2

Preparation before test
-------------------------

|  1）Please connect following the path of :doc:`《Linux fast boot manual》<MYZR-IMX6-EK140P Quick Start>` -> “Linux fast boot” -> “device connection”.
|  2）Please boot following the path of :doc:`《Linux fast boot manual》<MYZR-IMX6-EK140P Quick Start>` -> “Linux fast boot” -> “device booting”.

Test item
-----------

Network inferface test
~~~~~~~~~~~~~~~~~~~~~~~~~

|  MYZR-IMX6-EK140P support two 100 Mbps ethernet interfaces.

**Interface property**

|  Eth0 Interface position：P10
|  Eth1 Interface position：：P8

**Test method**

|  1）Configure computer IP
|  Set wired network card IP of computer as 192.168.137.99
|  2）Eth0 connect test
|  Connect lan line: connect “eth0”on evaluation board with corresponding wired network card interface on computer with lan line.
|  Note: check jumper cap to ensure it is attached.

- Set evaluation board IP：

.. code-block:: shell

   # ifconfig eth0 192.168.137.81

|  Execute test command：

.. code-block:: shell

   # ifconfig eth1 down 
   # ping 192.168.137.99 -c 2 -w 4 

- Observe test result：system will output message like following:

.. code-block:: shell

   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.685 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.374 ms 
   
   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.374/0.529/0.685/0.157 ms  

- Test result：“0% packet loss”represent test passing.

|  3）Eth1 connect test
|  Connect lan line: connect “eth1”on evaluation board with corresponding wired network card interface on computer with lan line.
|  Note: check jumper cap to ensure it is attached.

- Set the second network port IP:

.. code-block:: shell

   # ifconfig eth1 192.168.137.82

- After setting, the system will output the working status information of the second network port:

.. code-block:: shell

   fec 20b4000.ethernet eth1: Freescale FEC PHY driver [Generic PHY] (mii_bus:phy_addr=20b4000.ethernet:01, irq=-1)
   IPv6: ADDRCONF(NETDEV_UP): eth1: link is not ready
   fec 20b4000.ethernet eth1: Link is Up - 100Mbps/Full - flow control rx/tx
   IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready 

- Execute test command：

.. code-block:: shell

   # ifconfig eth0 down
   # ping 192.168.137.99 -c 2 -w 4

- Observe test result：system will output message like following:

.. code-block:: shell

   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.705 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.386 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.386/0.545/0.705/0.161 ms

- Test result：“0% packet loss”represent test passing.

USB Test
---------

**Interface property**

|  Interface position：P20

**Test Method**

|  1）Start test
|  Insert USB device into USB port on base board，system will output message like following：

.. code-block:: shell

   usb 1-1.4: new high-speed USB device number 4 using ci_hdrc  
   usb-storage 1-1.4:1.0: USB Mass Storage device detected  
   scsi host0: usb-storage 1-1.4:1.0  
   scsi 0:0:0:0: Direct-Access     Mass     Storage Device   1.00 PQ: 0 ANSI: 0 CCS  
   sd 0:0:0:0: [sda] 7716864 512-byte logical blocks: (3.95 GB/3.67 GiB)  
   sd 0:0:0:0: [sda] Write Protect is off  
   sd 0:0:0:0: [sda] No Caching mode page found  
   sd 0:0:0:0: [sda] Assuming drive cache: write through  
    sda: sda1 sda2  
   sd 0:0:0:0: [sda] Attached SCSI removable disk  

|  2）Test over Take out USB device from base board，system will output message like following：

.. code-block:: shell

   usb 1-1.4: USB disconnect, device number 4  

TF Card Test
--------------

**Interface properties**

|  Interface position：P13
|  Interface type: MicroSD

**Test method**

|  1）Start test
|  Insert the equipment into the card slot, and insert the card into the card interface on the card board.
|  Enter the following command:

.. code-block:: shell

   # dmesg | grep mmc0

|  The system will output the following information，that means the TF interface is normal:

.. code-block:: shell

   mmc0: SDHCI controller on 2190000.usdhc [2190000.usdhc] using ADMA  
   mmc0: host does not support reading read-only switch, assuming write-enable  
   mmc0: new high speed SDHC card at address 1234  
   mmcblk0: mmc0:1234 SA04G 3.67 GiB  

|  2）View the system's TF card equipment Enter the following command:

.. code-block:: shell

   # ls /dev/mmcblk0* 

|  The system will output the following information:

.. code-block:: shell

   /dev/mmcblk0    /dev/mmcblk0p1  /dev/mmcblk0p2  

Standard GPIO testing
------------------------

**Interface property**

|  Interface position : P21
|  1）GPIO output test
|  The test of standard GPIO takes P21:35 and P21:36 as examples. Other GPIO tests can refer to this test method.

- Configure P21:35 for output

|  Enter the following command:

.. code-block:: shell

   # OUT_IO_OUT_NUM=4 
   # echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
   # echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   # echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  Note: configure P21:35 to output low level and measure by multimeter. If pin P21:35 voltage is 0V, configure OK.

- Configure P21:36 for output

|  Enter the following command:

.. code-block:: shell

   # OUT_IO_OUT_NUM=3  
   # echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
   # echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   # echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  Note: configure P21:36 to output low level and measure by multimeter. If pin P21:35 voltage is 3.3V, configure OK.

|  2）Control the output level
|  Enter the following command:

.. code-block:: shell

   # echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value   
   # echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  Control output level can be achieved.

- Other available GPIO: P21:33,34,23;The corresponding IO serial Number is: 2,1,110

GPIO-LED test
----------------

**led-heartbeat**

- led-heartbeat Connect to the indicator D12, and you can see the D12 flashing regularly after the system starts.

**led-timer**

- led-timer Connect to the indicator D8, and you can see the D8 flashing regularly after the system starts.
- Control high&low electrical time

|  1）Change the time of extinction

.. code-block:: shell

   # echo 1000 > /sys/class/leds/led-timer/delay_off

|  2）Change the lighting time

.. code-block:: shell

   # echo 2000 > /sys/class/leds/led-timer/delay_on

**led-default**

- led-default connect to D11, and the default state will be constant after system startup.

|  1）Make the D11 normally on
|  Default - on can be controlled by brightness, Default - on the implementation of the state is the initial trigger to on, after the initial trigger for the high level.
|  Enter the following command:

.. code-block:: shell

   # echo 1 > /sys/class/leds/default/brightness

|  2）Destroy the D11
|  To write 0 brightness can detect low level.
|  Enter the following command:

.. code-block:: shell

   # echo 0 > /sys/class/leds/default/brightness

PWM Test
----------

**PWM-LED**

|  Enter the following command:

.. code-block:: shell

   # PWM_DEV=pwmchip4
   # echo 0 > /sys/class/pwm/$PWM_DEV/export 
   # echo 1000000000 > /sys/class/pwm/$PWM_DEV/pwm0/period
   # echo 100000000 > /sys/class/pwm/$PWM_DEV/pwm0/duty_cycle
   # echo 1 > /sys/class/pwm/$PWM_DEV/pwm0/enable

- Note: the LED(D7) can be seen flashing once in 1 second (1000000000 ns) (high level duration is 100000000 ns = 0.1 s).

**PWM-Buzzer**

|  Enter the following command:

.. code-block:: shell

   # PWM_DEV=pwmchip1
   # echo 0 > /sys/class/pwm/$PWM_DEV/export 
   # echo 1000000000 > /sys/class/pwm/$PWM_DEV/pwm0/period
   # echo 100000000 > /sys/class/pwm/$PWM_DEV/pwm0/duty_cycle
   # echo 1 > /sys/class/pwm/$PWM_DEV/pwm0/enable

|  Note: the buzzer can be heard once in 1 second (1000000000 ns) (high level duration: 100000000 ns = 0.1 s).

Serial port test
-------------------

|  Test instruction: adopt the test of serial port.

UART2
~~~~~~~

**Interface property**

- Interface position :P21:27,28
- Device：/dev/ttymxc1

|  1）Test preparation
|  Send and receive pin of short serial port 2 (pin no. 27 and no. 28 of P21).
|  2）Test conducted
|  Enter the following command:

.. code-block:: shell

   # /my-demo/linux-4.1.15/MY_SERIAL_TEST_L4115_MYIMX6A7.out /dev/ttymxc1 "www.myzr.com.cn"  

|  The system will output similar information:

.. code-block:: shell

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

UART3
~~~~~~~

**Interface property**

- Interface position ：P21: 25,26
- Device：/dev/ttymxc2

|  1）Test preparation
|  Send and receive pin of short serial port 3 (no. 25 and no. 26 pin of P21).
|  2）Test conducted
|  Enter the following command:

.. code-block:: shell

   # /my-demo/linux-4.1.15/MY_SERIAL_TEST_L4115_MYIMX6A7.out /dev/ttymxc2 "www.myzr.com.cn"  

|  The system will output similar information:

.. code-block:: shell

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

CAN Test
----------

|  Test instructions: My-imx6-ek140p has two groups of CAN interfaces, which are sent by CAN1 and received by CAN0.

**Interface property**

|  Interface position :CAN1 P7:1,2
|  Interface position :CAN2 P9:1,2

|  1）Test preparation
|  Connect CAN_L (p7:1) of CAN1 to CAN_L (p9:1) of CAN2;Connect CAN_H (p7:2) of CAN1 to CAN_H (p9:2) of CAN2.
|  2）Enter the following command

- Configure CAN1 (can0)

.. code-block:: shell

   # ip link set can0 up type can bitrate 125000

|  The system will output similar information:

.. code-block:: shell

   flexcan 2090000.can can0: writing ctrl=0x0e312005
   IPv6: ADDRCONF(NETDEV_CHANGE): can0: link becomes ready、

- Configure CAN2 (can1)

.. code-block:: shell

   # ip link set can1 up type can bitrate 125000

|  The system will output similar information:

.. code-block:: shell

   flexcan 2094000.can can1: writing ctrl=0x0e312005
   IPv6: ADDRCONF(NETDEV_CHANGE): can1: link becomes ready

- CAN1 (can0) background to receive

.. code-block:: shell

   # candump can0 &

|  The system will output similar information:

.. code-block:: shell

   [1] 589

- CAN2 (can1) send data

.. code-block:: shell

   # cansend can1 1F334455#1122334455667788

- The system will output similar information:

.. code-block:: shell

   can0  1F334455   [8]  11 22 33 44 55 66 77 88

SPI test
----------

|  Test instructions;There are two paths for SPI on the assessment board.

ECSPI1 test
~~~~~~~~~~~~~

**Interface property**

- Interface position ：P21: 3,4
- Test Device：/dev/spidev0.0

|  1）Test preparation Short P21 on 3 and 4 pin.
|  2）Enter the following command :

.. code-block:: shell

   # /my-demo/linux-4.1.15/MY_SPIDEV_TEST_L4115_MYIMX6A7.out -D /dev/spidev0.0

|  The test results are similar to the following output, indicating that the test passed:

.. code-block:: shell

   spi mode: 0
   bits per word: 8
   max speed: 500000 Hz (500 KHz)

   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00
 
ECSPI2 test
~~~~~~~~~~~~

**Interface property**

- Interface position ：P21: 9,10
- Test Device：/dev/spidev1.0

|  1）Test preparation
|  Short P21 9 and 10 pin.
|  2）Enter the following command :

.. code-block:: shell

   # /my-demo/linux-4.1.15/MY_SPIDEV_TEST_L4115_MYIMX6A7.out -D /dev/spidev1.0

|  The test results are similar to the following output, indicating that the test passed:

.. code-block:: shell

   spi mode: 0
   bits per word: 8
   max speed: 500000 Hz (500 KHz)

   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00

Watchdog Test
----------------

|  Test instructions: WatchDog test includes 2 items: reset test and feeding dog test.

Timeout reset test
~~~~~~~~~~~~~~~~~~~~

|  1）Test instructions
|  The reset test will start the WatchDog, but without feeding the dog, the system will reset after the timeout.
|  2）Enter the following command :

.. code-block:: shell

   # /unit_tests/wdt_driver_test.out 10 15 1

|  After waiting for 10 seconds after running the test command, the WatchDog timed out and the system was reset.
|  The system restart output information will be seen in the terminal as follows:

.. code-block:: shell

   Starting wdt_driver (timeout: 10, sleep: 15, test: write)
   Trying to set timeout value=10 seconds
   The actual timeout was set to 10 seconds
   Now reading back -- The timeout is 10 seconds
   random: nonblocking pool is initialized


   U-Boot 2016.03-svn270 (Oct 08 2018 - 16:52:53 +0800)

   CPU:   Freescale i.MX6ULL rev1.0 528 MHz (running at 396 MHz)
   CPU:   Industrial temperature grade (-40C to 105C) at 51C
   Reset cause: WDOG
   Board: MYIMX6EK140P-6Y

Feed the dog test
~~~~~~~~~~~~~~~~~~~~

|  1）Test instructions The dog feeding test will start the WatchDog and feed the dog once every 2 seconds, and the system will reset within the timeout (in this case 4 seconds).
|  2）Input test instruction

.. code-block:: shell

   # /unit_tests/wdt_driver_test.out 4 2 1 &  

|  The test results are similar to the following output, indicating that the test passed:

.. code-block:: shell

   [1] 585
   Starting wdt_driver (timeout: 4, sleep: 2, test: write)
   Trying to set timeout value=4 seconds
   The actual timeout was set to 4 seconds
   Now reading back -- The timeout is 4 seconds

RTC Test
-----------

|  1）Test instructions
|  Restart Device after power outage, check current system time and hardware time

- Check the current system clock command as follows:

.. code-block:: shell

   # date

|  The system will output similar information:

.. code-block:: shell

   Wed Sep 19 17:39:19 UTC 2018

|  2）View the current RTC chip clock
|  The order is as follows:

.. code-block:: shell

   # hwclock

|  The system will output similar information:

.. code-block:: shell

   Wed Sep 19 17:40:05 2018  0.000000 seconds

|  3）Set the system clock and synchronize to the RTC chip
|  The order is as follows:

.. code-block:: shell

   # date -s "2018-09-21 12:34:56"

|  The system will output similar information:

.. code-block:: shell

   Fri Sep 21 12:34:56 UTC 2018

|  4）Writes the system clock to the hardware clock

.. code-block:: shell

   # hwclock -w

|  5）Power outage restart assessment board to view the current system clock and hardware clock
|  The order is as follows:

.. code-block:: shell

   # date

|  The system will output similar information:

.. code-block:: shell

   Fri Sep 21 12:36:02 UTC 2018

|  6）View the current RTC chip clock The order is as follows:

.. code-block:: shell

   # hwclock  

|  The system will output similar information:

.. code-block:: shell

   Fri Sep 21 12:36:12 2018  0.000000 seconds

Timed wake-up test
---------------------

|  1）Set to wake up event 10 seconds later

.. code-block:: shell

   # echo +10 > /sys/class/rtc/rtc1/wakealarm

|  2）Put the Device in

.. code-block:: shell

   # echo mem > /sys/power/state

|  3）Sleep information

.. code-block:: shell

   PM: Syncing filesystems ... done.
   Freezing user space processes ... 
   Freezing remaining freezable tasks ... (elapsed 0.006 seconds) done.
   Suspending console(s) (use no_console_suspend to debug)

|  4）Wake up the information

.. code-block:: shell

   (elapsed 0.001 seconds) done.
   PM: suspend of devices complete after 708.601 msecs
   PM: suspend devices took 0.710 seconds
   PM: late suspend of devices complete after 2.543 msecs
   PM: noirq suspend of devices complete after 2.410 msecs
   Disabling non-boot CPUs ...
   PM: noirq resume of devices complete after 1.494 msecs
   PM: early resume of devices complete after 1.571 msecs
   PM: resume of devices complete after 223.182 msecs
   PM: resume devices took 0.230 seconds
   Restarting tasks ... done.

Audio test
-------------

**Playback of audio**

|  Test instructions：This test is to verify the audio function of the evaluation board by playing the audio file.
|  1）Test preparation
|  2）Execute test command

.. code-block:: shell

   # aplay /unit_tests/audio8k16S.wav

|  3）After executing the above test command, you will hear the voice output from the audio Device. The system will output similar information:

.. code-block:: shell

   Playing WAVE '/unit_tests/audio8k16S.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Stereo  

**The audio recording**

|  1）Test preparation
|  2）Enter the following command

- Recording

.. code-block:: shell

   # arecord -d 5 -f S16_LE -t wav foobar.wav

- Play recording

.. code-block:: shell

   # aplay foobar.wav

|  3）After executing the above test command, you will hear a recording played by the audio Device.

4G Module EC20(optional) test
-------------------------------

|  Interface position : P19
|  Test instructions：When the power is cut off, access the 4G module, connect the antenna and insert the SIM card, then start the evaluation board.
|  Enter the following command:

.. code-block:: shell

   # /my-demo/linux-4.1.15/MY_EC20_QuectelCM_L4115_MYIMX6A7.out &

|  The system will output similar information:

.. code-block:: shell

   [1] 607
   [09-21_13:36:14:352] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
   [09-21_13:36:14:353] /my-demo/linux-4.1.15/MY_EC20_QuectelCM_L4115_MYIMX6A7.out profile[1] = (null)/(null)/(null)/0, pincode = (null)
   [09-21_13:36:14:356] Find /sys/bus/usb/devices/1-1.2 idVendor=2c7c idProduct=0125
   [09-21_13:36:14:356] Find /sys/bus/usb/devices/1-1.2:1.4/net/eth2
   [09-21_13:36:14:356] Find usbnet_adapter = eth2
   [09-21_13:36:14:356] Find /sys/bus/usb/devices/1-1.2:1.4/GobiQMI/qcqmi2
   [09-21_13:36:14:357] Find qmichannel = /dev/qcqmi2
   [09-21_13:36:14:403] Get clientWDS = 7
   [09-21_13:36:14:435] Get clientDMS = 8
   [09-21_13:36:14:467] Get clientNAS = 9
   [09-21_13:36:14:499] Get clientUIM = 10
   [09-21_13:36:14:532] Get clientWDA = 11
   [09-21_13:36:14:563] requestBaseBandVersion EC20CEFAR02A10M4G
   [09-21_13:36:14:659] requestGetSIMStatus SIMStatus: SIM_READY
   [09-21_13:36:14:692] requestGetProfile[1] cmnet///0
   [09-21_13:36:14:724] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [09-21_13:36:14:755] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
   [09-21_13:36:14:819] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [09-21_13:36:16:036] requestSetupDataCall WdsConnectionIPv4Handle: 0x87756f40
   [09-21_13:36:16:132] requestQueryDataCall IPv4ConnectionStatus: CONNECTED
   [09-21_13:36:16:163] ifconfig eth2 up
   [09-21_13:36:16:193] busybox udhcpc -f -n -q -t 5 -i eth2
   [09-21_13:36:16:211] udhcpc (v1.24.1) started
   [09-21_13:36:16:318] Sending discover...
   [09-21_13:36:16:378] Sending select for 10.151.159.101...
   [09-21_13:36:16:438] Lease of 10.151.159.101 obtained, lease time 7200
   [09-21_13:36:16:522] /etc/udhcpc.d/50default: Adding DNS 221.179.38.7
   [09-21_13:36:16:522] /etc/udhcpc.d/50default: Adding DNS 120.196.165.7

Display (optional) test
--------------------------

|  During the system startup, you can see the Linux penguin and OpenEmbedded startup scene.

FXLS8471 Display (optional) test
----------------------------------

- Make the sensor Enable

.. code-block:: shell

   # echo 1 > /sys/class/misc/FreescaleAccelerometer/enable

- View sensor data

.. code-block:: shell

   # cat /sys/class/misc/FreescaleAccelerometer/data

MAG3110 (optional) test
--------------------------

- Make the sensor Enalbe

.. code-block:: shell

   # echo 1 > /sys/class/misc/FreescaleGyroscope/enable  

- Test

.. code-block:: shell

   # evtest  

|  The system will output similar information:

.. code-block:: shell

   No device specified, trying to scan all of /dev/input/event*
   Available devices:
   /dev/input/event0:      20cc000.snvs:snvs-powerkey
   Select the device event number [0-0]:  

FXAS2100 (optional) test
---------------------------

- Test

.. code-block:: shell

   # evtest

|  The system will output similar information:

.. code-block:: shell

   No device specified, trying to scan all of /dev/input/event*
   Available devices:
   /dev/input/event0:      20cc000.snvs:snvs-powerkey
   Select the device event number [0-0]:  