
MYZR-IMX6-EK200 Linux-3.0.35 Test Manual
==========================================

Preparation before test
--------------------------

|  1）Please refer to "connection of device"->"Linux fast boot" in 《Linux fast boot manual》 for the connection.
|  2）Please refer to "booting device" ->"Linux fast boot" in 《Linux fast boot manual》 for the booting.

Test item
-----------

Lan port test
~~~~~~~~~~~~~~~~

|  MYZR-I.MX6 evalution board support dual lan port（two 100-Mbps ethernet lan ports2）.

**Test instruction**

|  The first ethernet lan port is “P4”on front view of base board，the second one is “P5”on front view of base board.
|  Defauted lan port is the first one after system boot,with defauted IP as 192.168.3.104.

**Test method**

1.  Test the first ethernet lan port

- Connect lan line：connect “P4”on evaluation board with computer lan port through network
- Set computer IP：set computer lan port IP as 192.168.3.9

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.1.2.1.png
   :alt: MY-IMX6-EK200_L3035_2.1.2.1.png

- Run test command ：$ ping -I eth0 192.168.3.9 -c 2 -w 4
- Observe test result：system will output following information：

.. code-block:: shell

   --- 192.168.3.9 ping statistics ---
   2packets transmitted, 2 packets received, 0% packet loss

- Test result：“0% packet loss”represent test passing.

2.  Test the second ethernet lan port.

- Connect lan line：take out lan line from the first lan port then plug in “P5”on evaluation board，another end of lan line is kept in connection with lan port of computer.
- Set computer IP：set computer lan port IP as 192.168.3.9（If the setting was already done then go direclty into next step）.
- Set the second lan port IP：$ ifconfig eth1 192.168.3.18，after the setting system will output working condition of the second lan port, as below：

.. code-block:: shell

   smsc95xx 2-1.1:1.0: eth1: link up, 100Mbps, full-duplex, lpa 0xCDE1

- Run test command：

.. code-block:: shell

   $ ping -I eth1 192.168.3.9 -c 2 -w 4

- Observe test result：system will output the following message.

.. code-block:: shell

   --- 192.168.3.9 ping statistics ---
   2packets transmitted, 2 packets received, 0% packet loss

- Test result：“0% packet loss”represent test passing.

**reference symbols**

|  Instruction：

 | The first red frame is test command for lan port 1.
 | The second red frame is test result for lan port1.
 | The third red frame is IP configuration for lan port2.
 | The fourth red frame is status information for lan port2.
 | The fifth red frame is test command for lan port2.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.1.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.1.3.1.png

USB test
~~~~~~~~~~

**Test Instruction**

|  MYZR-I.MX6 V2.5 评估板有2个USB HOST接口，位于底板正面“J8”。

**Test method**

1. Start test

|  Plug USB device in USB port in base board，system will output the following message：

.. code-block:: shell

   usb *-*.*: new high speed USB device number * using fsl-ehci
   ……

2. Test end

|  Take out USB device from the base board，system will output the following message：

.. code-block:: shell

   usb *-*.*: USB disconnect, device number *

**reference symbols**

|  Instruction：

 | The first red frame in image is message outputed by system when insert U disk.
 | The second red frame in image is message outputed by system when take out U disk.
 | The third red frame in image is message outputed by system when insert USB mouse.
 | The fourth red frame in image is message outputed by system when take out USB mouse.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.2.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.2.3.1.png

SD card interface test
~~~~~~~~~~~~~~~~~~~~~~~

**Test Instruction**

|  SD card interface is in“J25”in rear view of base board.

**Start test**

1. Insert device in SD card slot.

|  Insert SD card in SD card port in base board, system will output following message(see attached image),e.g.SD port is normal：

.. code-block:: shell

   mmc*: new high speed SD card at address ****
   mmcblk*: mmcx:xxxx SA**G *.**GiB
   mmcblk*: p*

2. Pop-up device from SD card slot.

|  Press again SD card in SD card slot，base board will pop-up SD cardsystem will output following message(see attached image),e.g.function of SD card port pop-up is normal：

.. code-block:: shell

   mmc*: card **** removed

3. End test

|  Take out SD card after SD card pop-up,to end the test.

**reference symbols**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.3.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.3.3.1.png

A/V test
~~~~~~~~~~~

**Test Instruction**

|  This test is to verify the function of video & audio of evaluation board by playing vocal video.

**Test method**

1. Prepare test

|  Connect audio output device to audio element in front view of base board,audio element is “J20”in front view of base board，silkscreened as“HP”.

2. Execute test

|  Play a video with gplay，commanded as below：

.. code-block:: shell

   $ gplay /app_test/arm.flv

|  The above command will play a file designated by command with gplay.

3. Test result

|  You can see the vedeo played on display screen of evaluation board and hear the voices outputed by audio device.

**reference symbols**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.4.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.4.3.1.png

LED（GPIO）test
~~~~~~~~~~~~~~~~

**Test Instruction**

|  CPU pin used in LED（GPIO）test is“NANDF_CS0” ，connect to “no.4 pin of J4 ”，GPIO will be controled by test programs to output high and low ectrical level after running test program,interval between high and low electrical level is 1 second.
|  Tip: LED (GPIO) testing requires a multimeter, and users without a multimeter can skip the next test.

**Test method**

1. Execute test program

|  Enter command in terminal to run the test program，example as below：

.. code-block:: shell
   
   $ /app_test/led

|  At this hour GPIO will be controled by test programs to output high and low ectrical level,and output message similar to below.

.. code-block:: shell

   Write=0
   Write=1
   ……

2. Check test result.

|  Connect ground of multimeter with ground of development board，another line of multimeter is connected to no.4 pin of J4，voltage of multimeter will jump.

3. End test

|  Press“Ctrl”+“C”on computer,to end the key test program.

**reference symbols**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.3.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.3.3.1.png

Key test
~~~~~~~~~

**Test Instruction**

|  There are 4 keys on MYZR-I.MX6 base board，three of them are custom function keys(SW2：WAKE UP，SW3:V+，SW4:V-），and one reset key（SW1：nRE）test program key_test can test these 3 function keys.

**Test method**

1. Test method

|  Execute test program.

.. code-block:: shell

   $ /app_test/key_test

2. Proceed with interactive test.

|  Press separately SW4、SW3、SW2，system will output corresponding message as below：

.. code-block:: shell

   key*** Pressed
   key*** Released

|  Message of“key*** Pressed”is outputed with press of key，message of“key*** Released”is outputed with release of key.

3. End test

|  Press “Ctrl”+“C”on computer to send the test program for keys.
|  Note：press SW1（system will reset and reboot）.

**reference symbols**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.6.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.6.3.1.png

Serial port test
~~~~~~~~~~~~~~~~~~

|  There are 5 serial ports in MYZR-I.MX6 evaluation board，4 are user serial ports（in “J1”in front view of base board，silkscreened as“TTL_UART”），one is debug serial port（in “P2”in front view of base board）.

**Test Instruction**

|  Instruction of system device file：

- Device file for debug serial port in the system is ttymxc0，device file for user serial port are ttymxc1、ttymxc2、ttymxc3、ttymxc4.

|  Instruction for transceiver pin of serial ports and their corresponding device file：

- UART2：send 7，receive 9，ttymxc1
- UART3：send 11，receive 13，ttymxc2
- UART4：send 17，receive 15，ttymxc3
- UART5：send 18，receive 16，ttymxc4

|  Tips：transceiver pins of serial port are listed here,but please refer to schematic for definition of all pins of serial port.

**Test method**

|  Adopt method of self-sending & self-receiving of serial port.
|  Tips：here take serial port 5 as example,please refer to serial port test method for the test of the other 3 user serial ports.

1. Prepare test

|  Short connect sending pin and receiving pin of serial port 5（no.16 and no.18 pin of J1）.

2. Execute test.

.. code-block:: shell

   $ ~/my-demo/linux-3.0.35/uart_test.out /dev/ttymxc4 "www.myzr.com.cn"

3. Test result.

|  If serial port is normal,terminal will reveal similar message as below：

.. code-block:: shell

   Read Test Data finished,Read Test Data is-------www.myzr.com.cn

**reference symbols**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.7.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.7.3.1.png

RTC test
~~~~~~~~~~

**Test Instruction**

|  Due to restrictions in transportation，MYZR-I.MX6 evaluation board doesn't contatin battery in deliverybefore RTC test please prepare button cell to install on “BT1”in rear view of base board（beside silkscreened name of“RTC”）.

**Test method**

1. Power off then reboot device,to check the time of system and hardware.

|  Command to check clock of current system as below：

.. code-block:: shell

   $ date

|  Message outputed by system as below：

.. code-block:: shell

   Thu Jan 1 00:00:59 UTC 1970

|  Command to check clock of RTC chip as below：

.. code-block:: shell

   $ hwclock

|  Message outputed by system as below：

.. code-block:: shell

   Tue Nov 30 00:00:00 1999 0.000000 seconds

2. Set system clock and synchronously set to RTC chip.

|  Command to set system clock are with below reference：

.. code-block:: shell

   $ date -s "2015-04-27 12:34:56"

|  Command to write system clock into hardware as below：

.. code-block:: shell

   $ hwclock -w

3. Power off and reboot evaluation board，to check current system clock and hardware clock.

|  Please refer to step 1.

4. Test result.

|  It will be a newly-set clock after execution until step 3.

**reference symbols**

|  Below image is screenshots for step1 and step 2 in the test.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.8.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.8.3.1.png

|  Below image is the screenshots for step3 in the test.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.8.3.2.png
   :alt: MY-IMX6-EK200_L3035_2.8.3.2.png

WatchDog test
~~~~~~~~~~~~~~~~

**Test Instruction**

|  WatchDog test includes two items：one is reset test，the other is feed dog test.

**Reset test**

1. Test instruction

|  Reset test will boot WatchDog，but doesn't feed dog，system will reset after 60 seconds.

2. Execution test

|  Run /app_test/watdogrestart，instanced command as below：

.. code-block:: shell

   $ /app_test/watdogrestart

3. 测试结果

|  Wait for 60 seconds after running of test command，WatchDog timeout，system is resettedyou can see message outputed by system rebooting on terminal.

**Dog feeding test**

1. Test instruction

|  Feeding dog test will boot WatchDog，and feed dog once a second，system won't reset because of WatchDog timeout.

2. Execute test

|  Run /app_test/watdogtest &，instanced example as below：.

.. code-block:: shell
   
   $ /app_test/watdogtest &

3. Test result

|  After run the test command,system still works normally and won't reset because of WatchDog timeout.

4. figure

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.9.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.9.3.1.png

SPI test
~~~~~~~~~

|  There are a group of SPI ports on MYZR-I.MX6 V2.5 base board，located on“J7”，silkscreened as “SPI”.

**Test Instruction**

|  MISO pin and MOSI pin of SPI port will be used for the testSMISO pin of SPI port is “no.8 of J7”on the base board，and MOSI pin is “no.10 of J7”.

**Test method**

|  Adopt way of SPI self-sending（output）self-receiving（input).

1. Prepare test

|  Short connect MISO pin and MISO pin of SPI port，e.g.short connect pin no.8 and pin no.10 of J7 on the base board.

2. Execute test

.. code-block:: shell

   $ ~/my-demo/linux-3.0.35/spidev_test.out -D /dev/spidev1.0

3. Test result

|  If SPI is normal，you can see on terminal the following charaters：

.. code-block:: shell

   FF FF FF FF FF FF
   40 00 00 00 00 95
   FF FF FF FF FF FF
   FF FF FF FF FF FF
   FF FF FF FF FF FF
   DE AD BE EF BA AD
   F0 0D

**Figured**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.10.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.10.3.1.png

CAN interface test
~~~~~~~~~~~~~~~~~~~~~

**Test Instruction**

|  Oscilloscope will be used for CAN test，please skip this step for users who don't have oscilloscope.

**Test method**

1. Configuration CAN0.

|  Instanced example as below：

.. code-block:: shell

   $ ip link set can0 up type can bitrate 250000

2. Configuration of link for oscilloscope

|  Connect CH1 and CH2 with “R83”of evaluation board（the green stand on topside on front view of base board）.
|  Configure oscilloscope（for users who don't know how to use oscilloscope ,please ask hardware engineers for assistance ）.

3. Execute test command.

.. code-block:: shell

   $ /app_test/client_test

|  4. Rest result.

|  When exectue the test command,you can see a waving change on oscilloscope.

**reference symbols**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.11.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.11.3.1.png

PCIE interface test
~~~~~~~~~~~~~~~~~~~~

**Test Instruction**

|  System is already added with drivers for PCI port，in booting system will check out devices on PCI-E interface.

**Test method**

|  Reset system，observe the message outputed by system booting.

1. PCI-E driving program output messages.

|  In the course of system booting, if there is outputed message as below,e.g PCI-E interface load is normal：

.. code-block:: shell

   iMX6 PCIe PCIe RC mode imx_pcie_pltfm_probe entering.
   PCIE: imx_pcie_pltfm_probe start link up.

2. Message outputed without link of PCI-E device.

|  In the course of system booting，it there is not a valid device linked with PCI-E interface，system will prompt“link down!”on PCI-E port，something as below：

.. code-block:: shell

   link up failed, DB_R0:0x00361900, DB_R1:0x08200000!
   IMX PCIe port: link down!

3. Message outputed when there is a valid PCI-E device linked（here take Intel 4965AGN as an example）

|  In the course of system booting，if PCI-E port detect a valid device and the device module is normal，system will prompt“link up”on PCI-E port，as below：

.. code-block:: shell

   IMX PCIe port: link up.

4. Linux test command：$ lspci.

|  If a valid PCI-E device is inserted on PCI-E port,information related to the module will be gained with lspci，something like this（what is linked is Intel 4965AGN in this case）：

.. code-block:: shell

   00:00.0 Class 0604: 16c3:abcd
   01:00.0 Class 0280: 8086:4229

|  If there is not device linked with PCI-E port，lspci system won't output any message.

**reference symbols**

|  Following figure is message outputed by system without a link with PCI-E device.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.12.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.12.3.1.png

|  The following figure is message ouputed by system with a link to Intel 4965AGN.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.12.3.2.png
   :alt: MY-IMX6-EK200_L3035_2.12.3.2.png

|  Following figure is message by use of lspci after entering system on the condition of a link with Intel 4965AGN.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.12.3.3.png
   :alt: MY-IMX6-EK200_L3035_2.12.3.3.png

WIFI test
~~~~~~~~~~

**Test Instruction**

|  Model no. of WIFI chip ussed for MYZR-I.MX6 evaluation board is RTL8188EUS.

**测试方法(test method)**

1. Load WIFI module driver

|  Instanced command as below：

.. code-block:: shell

   $ insmod /lib/modules/wifi/wlan.ko

2. Generate WIFI config file.

|  Refered command as below：

.. code-block:: shell

   $ wpa_passphrase MYZR_TP-LINK myzrd2302 > /etc/wpa_supplicant.conf

|  Both name and password of WIFI designated by this command are “MYZR_TP-LINK myzrd2302”，need to replace with your own linkable WIFI name and password.

3. Link WIFI network.

|  Instanced command as below：.

.. code-block:: shell

   $ wpa_supplicant -B –c /etc/wpa_supplicant.conf -iwlan0

4. Automaically gain IP.

|  Instanced command as below：

.. code-block:: shell

   $ udhcpc -i wlan0

|  Note：need to ensure a DHCP function opened for WIFI network in use.

5. Test WIFI network link.

|  Instanced command as below：

.. code-block:: shell

   $ ping -I wlan0 www.baidu.com -c 2

6. Test result

|  Execute step 5 if ok, e.g. WIFI module is normal to work.

**reference symbols**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.13.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.13.3.1.png

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.13.3.2.png
   :alt: MY-IMX6-EK200_L3035_2.13.3.2.png

IPU test
~~~~~~~~~~

**Test Instruction**

|  The whole IPU test will take over ten minutes .

**Test method**

1. Execute test

|  Enter directory where test program is located（must enter directory where test program is locased for a normal test script）.

.. code-block:: shell

   $ cd /unit_tests/

|  Execute test script

.. code-block:: shell

   $ ./autorun-ipu.sh

2. Test result

|  In the whole test process，you can see a constant change of content on the display screen.
|  After test is over，you can see on terminal the following message：

.. code-block:: shell

   test stop at Thu Jan 1 00:33:38 UTC 1970

**reference symbols**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.14.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.14.3.1.png

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.14.3.2.png
   :alt: MY-IMX6-EK200_L3035_2.14.3.2.png

GPU test
~~~~~~~~~~

**Test Instruction**

|  Please follow /unit_tests/gpu.sh file for the details of test.

**Test method**

1. Execute test

|  Enter directory where test program is located（must enter directory where test program is locased for a normal test script）.

.. code-block:: shell

   $ cd /unit_tests/

|  Execute test script.

.. code-block:: shell

   $ ./gpu.sh

2. Test process.

|  In the whole test process，you can see a constant change of content on the display screen.

3. Exit test.

|  Terminal output“press ESC to escape...”，press ESC to exit test.

**reference symbols**

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.15.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.15.3.1.png

VPU test
~~~~~~~~~~~

**Test Instruction**

|  In the test,vedio file will be decoded with VPU and outputed to the display device.

**Test method**

1. Execute test

|  Enter directory where test program is located（must enter directory where test program is locased for a normal test script）.

.. code-block:: shell

   $ cd /unit_tests/

|  Execute test script.

.. code-block:: shell

   $ ./autorun-vpu.sh

2. Test process

|  In the whole test process，you can see the vedio decoded by VPU on the display screen.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/MY-IMX6-EK200_L3035_2.16.3.1.png
   :alt: MY-IMX6-EK200_L3035_2.16.3.1.png

Reveal function test
----------------------

- Special notes:

.. code-block:: shell

   When  u-boot  version u-boot-2016.03 svn315 and above
         Kernel  version Linux -3.0.35 svn31 and above
                         Linux -3.14.52 svn369 and above
                         Linux -3.14.52 svn368 and above
         Burning tool MfgTool-MYIMX6A9-L* svn181 and above 

|  Please refer to 《[MYZR-IMX6-A9 series: display functional tests》my-imx6-a9 series: display function test for testing

- In general, it is tested as follows:

|  Instruction：need to re-boot system to enter u-boot command line for each reveal function test，enter command and press Enter key.
|  Example as below：.

Single screen display
~~~~~~~~~~~~~~~~~~~~~~~

|  Instruction：enter command and press Enter key，observe the displayed content on screen in the course of system booting，Linux Logo can be seen.

**LVDS1**

|  Insert ribbon cable for screen to LVDS1（in “J22”on front view of base board，silkscreened as“LVDS1”），boot system，enter u-boot command line，enter the following commands and press Enter key：
|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**LVDS0**

|  Insert ribbon cable for screen to LVDS0（in“J24”on front view of base board，silkscreened as“LVDS0”）,run system to enter u-boot command line，enter the following commands and press Enter key：
|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**HDMI**

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm
|  Tips：there is not reveal of Linux Logo on screen for HDMI display in bootingvedio can be played with gplay command after entering system，vedio transfered can be seen on display screen.
|  Example for vedio playing command as below：

.. code-block:: shell

   $ gplay /unit_tests/akiyo.mp4

**RGB**

|  Enter u-boot command line，enter the following commands and press Enter key：
|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=lcd,SEIKO-WVGA,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

Dual screens synchronous display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Instruction：enter command and press Enter key，Linux Logo is displayed on the two screens in kernel booting，and other operations to screen is also displayed on the two screens.

**LVDS1+LVDS0 synchronous display**

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=dul0 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

Dual screen asynchronous display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Test commands probably to be used**

- Turn on backlight of main display screen.

.. code-block:: shell

   $ echo 0 > /sys/class/graphics/fb0/blank

- Turn on backlight of the second display screen.

.. code-block:: shell

   $ echo 0 > /sys/class/graphics/fb2/blank

- Play the designated vedio file to vedio device（here video17 is related to main screen）.

.. code-block:: shell

   $ gst-launch playbin2 uri=file:///unit_tests/akiyo.mp4 video-sink="mfw_v4lsink device=/dev/video17"

- Play the designated vedio file to vedio device（here video18 is related to the second screen）.

.. code-block:: shell

   $ gst-launch playbin2 uri=file:///unit_tests/akiyo.mp4 video-sink="mfw_v4lsink device=/dev/video18"

**Instruction of test method**

|  1）Enter u-boot command line and enter commands then press Enter key and wait until booting is over.
|  Example as below：
|  2）Execute command turn on backlight of corresponding display screen.
|  Example as below:
|  3）Execute vedio playing command to play the vedio to display screen.
|  Example as below：.
|  Instruction：in the mode of dual screen asynchronous display ，the backlight defaut of the second screen is closed after system boot，so need to execute step2）.

**LVDS1 as main screen**

- LVDS1+LVDS0 dual screen asynchronous display.

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- LVDS1+RGB dual screen asynchronous display.

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 video=mxcfb1:dev=lcd, SEIKO-WVGA,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- LVDS1+HDMI dual screen asynchronous display.

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 video=mxcfb1:dev=hdmi,1920x1080M@60,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**LVDS0 as main screen**

- LVDS0+LVDS1 dual screen asynchronous display：

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sep0 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- LVDS0+RGB dual screen asynchronous display.

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0 video=mxcfb1:dev=lcd,SEIKO-WVGA,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- LVDS0+HDMI dual screen asynchronous display.

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0 video=mxcfb1:dev=hdmi,1920x1080M@60,if=RGB24; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**RGB as main screen**

- RGB+LVDS1 dual screen asynchronous display：

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=lcd,SEIKO-WVGA,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- RGB+LVDS0 dual screen asynchronous display：

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=lcd,SEIKO-WVGA,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

**HDMI as main screen**

- HDMI+LVDS1 dual screen asynchronous display

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

- HDMI+LVDS0 dual screen asynchronous display

|  setenv bootargs console=ttymxc0,115200 ip=none root=/dev/mmcblk0p1 rootwait video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666 ldb=sin0; mmc dev 2; mmc read 0x10800000 0x800 0x2000; bootm

Instruction about environment variables
------------------------------------------

Features of environment variables of MYZR-IMX6 series of development board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Environment variables of MYZR-IMX6 series of development board feature as below：
|  1. medium leading kernel includes：eMMC、network（tftp）
|  2. medium leading file system includes：eMMC、network（NFS）
|  3. configuration for display device includes: LVDS0、LVDS1、HDMI、RGB，and different combinations of dual screens
|  In this case,if environment variables combine the three features mentioned above ，there will be at least 60 bootcmd environment variables,so we conduct abstract separation and recombination for environment variables.
|  Since bootargs environment variables include parameter such as console、video、ip、root ，so each kind of bootcmd rely a lot on bootargs ，plus a big difference among different kinds of bootcmd,it is no question that bootargs are not universial.

Bootcmd_xxx environment variables procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  We abstract bootcmd and bootargs based on guided device，after abstraction bootcmd_xxx procedure like this：
|  1. Re-build bootargs through bootargs_base，to ensure no conflict among bootargs；
|  2. Parameters corresponding to guided device are added after bootargs through bootargs_xxx；
|  As to “;”in bootcmd_xxx ,the following will be easily understood.

Correct way to set environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  As to the correct ways to set environment variables：
|  Must be noted that setting to bootargs in normal condition is invalid，because bootargs_base will re-set bootargs.
|  Need to write the setting of bootargs to the commands of bootargs_base .
|  Bootargs_base contains only console and video，other parameters should be written to bootargs_mmc or bootcmd_tftp or bootargs_nfs .

Example for correct way of environment variables setting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  If need to set “HDMI+LVDS1 dual screen asynchronous display”and reserve environment variables，then：
|  1. setenv bootargs_base 'setenv bootargs console=ttymxc0,115200 video=mxcfb0:dev=hdmi,1920x1080M@60,if=RGB24 video=mxcfb1:dev=ldb,LDB-1024X600,if=RGB666'
|  2. saveenv
|  The above two commands are applied.