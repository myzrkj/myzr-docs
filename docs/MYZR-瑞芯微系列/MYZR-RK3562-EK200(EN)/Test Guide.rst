.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Test Guide
==========

LED Test
--------

Interface Silkscreen: LED4, LED5

Test Description: Control LED on/off for testing

Test Operations:

Execute the following command to turn off LED4:

.. code-block:: shell

   echo 0 > /sys/class/leds/heartbeat/brightness

Execute the following command to turn on LED4:

.. code-block:: shell

   echo 1 > /sys/class/leds/heartbeat/brightness

Execute the following command to turn on LED5:

.. code-block:: shell

   echo 1 > /sys/class/leds/disk/brightness

Execute the following command to turn off LED5:

.. code-block:: shell

   echo 0 > /sys/class/leds/disk/brightness

Button Test
-----------

Interface Silkscreen: KEY1: RESET KEY2: MASKROM KEY3: USER1

Test Description: The baseboard includes 1 system reset button RESET, 1 Maskrom button Maskrom, and 1 user input button USER1. Check the event number corresponding to the input button, execute the od command, and press the corresponding button for testing.

Test Operations:

* System Reset Button Test

Power on the evaluation board, press the system reset button RESET (KEY1). The core board onboard LED1 will stop blinking. After releasing the button, the system will restart.

* Maskrom Button Test

.. code-block:: text

   =====> Input:
   od -x /dev/input/event1
   =====> Output:
   0000000 00ad 0000 0000 0000 2ce3 0007 0000 0000
   0000020 0001 0094 0001 0000 00ad 0000 0000 0000
   0000040 2ce3 0007 0000 0000 0000 0000 0000 0000
   0000060 00ad 0000 0000 0000 5423 000a 0000 0000
   0000100 0001 0094 0000 0000 00ad 0000 0000 0000
   0000120 5423 000a 0000 0000 0000 0000 0000 0000
   ^C

* USER1 Button Test

.. code-block:: text

   =====> Input:
   od -x /dev/input/event2
   =====> Output:
   0000000 00d6 0000 0000 0000 bbdd 0004 0000 0000
   0000020 0001 0094 0001 0000 00d6 0000 0000 0000
   0000040 bbdd 0004 0000 0000 0000 0000 0000 0000
   0000060 00d6 0000 0000 0000 4f7e 0006 0000 0000
   0000100 0001 0094 0000 0000 00d6 0000 0000 0000
   0000120 4f7e 0006 0000 0000 0000 0000 0000 0000
   ^C

Ethernet Port Test
------------------

Ethernet Port 1
~~~~~~~~~~~~~~~

Interface Silkscreen: J13

System Interface: eth0

Test Description: Test by sending ICMP packets from the development board to the PC.

Test Operations:

* Configure the PC's wired network card IP to 192.168.137.99

* Use an Ethernet cable to connect the development board Ethernet port and the PC's Ethernet port. The serial port will display:

.. code-block:: shell

   [  275.170629] rk_gmac-dwmac fe1c0000.ethernet eth0: Link is Up - 1Gbps/

* View the development board Ethernet port 1 information by entering the following command:

.. code-block:: shell

   ifconfig eth0

* Configure the IPv4 IP of Ethernet port 1 by entering the following command:

.. code-block:: shell

   ifconfig eth0 192.168.137.81 netmask 255.255.255.0

* Check the development board Ethernet port 1 information again to confirm whether the IPv4 address has been successfully configured. If not, restart from step 4. Enter the following command:

.. code-block:: shell

   ifconfig eth0

* Enter the following command to verify Ethernet port 1:

.. code-block:: shell

   ping -I eth0 192.168.137.99 -c 2 -w 4

"0% packet loss" indicates the test passed.

If "100% packet loss" appears, first confirm that the PC's firewall is completely disabled.

Ethernet Port 2
~~~~~~~~~~~~~~~

Interface Silkscreen: J14

System Interface: eth1

Test Description: Test by sending ICMP packets from the development board to the PC.

Test Operations:

* Configure the PC's wired network card IP to 192.168.137.99

* Use an Ethernet cable to connect the development board Ethernet port and the PC's Ethernet port. The serial port will display:

.. code-block:: shell

   [  528.550794] IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready

* View the development board Ethernet port 2 information by entering the following command:

.. code-block:: shell

   ifconfig eth1

* By default, the IP is obtained automatically. For testing, configure a static IP. The specific configuration command is as follows:

.. code-block:: shell

   ifconfig eth1 192.168.137.81 netmask 255.255.255.0

* Check the development board Ethernet port 2 information again to confirm whether the IPv4 address has been successfully configured. If not, restart from step 4. Enter the following command:

.. code-block:: shell

   ifconfig eth1

* Enter the following command to verify Ethernet port 2:

.. code-block:: shell

   ping -I eth1 192.168.137.99 -c 2 -w 4

"0% packet loss" indicates the test passed.

If "100% packet loss" appears, first confirm that the PC's firewall is completely disabled.

GPIO Test
---------

Test Description:

Use the GPIO sysfs interface to control IO. Taking GPIO1_C1 as an example, if you need to test other GPIOs, please modify the corresponding PIN value according to the following table.

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;
       word-wrap: break-word;
   }
   </style>

+-----------+--------+
| GPIO Pin  | PIN    |
+-----------+--------+
| GPIO3\_A0 | 96     |
+-----------+--------+
| GPIO3\_A1 | 97     |
+-----------+--------+
| GPIO1\_C1 | 49     |
+-----------+--------+
| GPIO1\_C2 | 50     |
+-----------+--------+
| GPIO1\_C3 | 51     |
+-----------+--------+
| GPIO1\_C4 | 52     |
+-----------+--------+
| GPIO1\_C5 | 53     |
+-----------+--------+
| GPIO1\_C6 | 54     |
+-----------+--------+
| GPIO4\_B6 | 142    |
+-----------+--------+
| GPIO3\_D2 | 122    |
+-----------+--------+
| GPIO3\_D3 | 123    |
+-----------+--------+
| GPIO3\_B7 | 111    |
+-----------+--------+
| GPIO3\_C0 | 112    |
+-----------+--------+

Test Operations

Enter the following command to set GPIO1_C1 to low level:

.. code-block:: shell

   echo 49 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio49/direction
   echo 0 > /sys/class/gpio/gpio49/value
   cat /sys/class/gpio/gpio49/value

The output information is similar to:

.. code-block:: shell

   0

Enter the following command to set GPIO1_C1 to high level:

.. code-block:: shell

   echo 1 > /sys/class/gpio/gpio49/value
   cat /sys/class/gpio/gpio49/value

The output information is similar to:

.. code-block:: shell

   1

UART Test
---------

Interface Silkscreen: J8

Test Description: Test using UART loopback (self-transmit and self-receive) method.

Test Operations

* Short the J8-7 (UART6_TX_M0) and J8-9 (UART6_RX_M0) pins.

* In the /test_app directory, enter the following command for send/receive testing:

.. code-block:: shell

   ./test_app/serial_test.out /dev/ttyS6 "myzr"

The output information is similar to:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d          Character: m 
   ASCII: 0x79          Character: y 
   ASCII: 0x7a          Character: z 
   ASCII: 0x72          Character: r 
   ASCII: 0x0           Character:

The output shows the same ASCII characters sent and received, with no error messages, indicating the UART test passed. Press 'Ctrl + C' to exit.

SPI Interface Test
------------------

Interface Silkscreen: J9

Test Description: Test using SPI loopback (self-transmit and self-receive) method.

Test Operations

* Short the J9-17 (GPIO3_B7) and J9-19 (GPIO3_C0) pins.

* In the /test_app directory, enter the following command for send/receive testing:

.. code-block:: shell

   ./test_app/spidev_test.out -D /dev/spidev0.0

The output information is similar to:

.. code-block:: shell

   spi mode: 0
   bits per word: 8
   max speed: 500000 Hz (500 KHz)
   00 24 00 00 00 00 
   00 3F FC 00 00 00 
   7F F8 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 0F 87 D0 7E 1F 
   87 F8

After executing the test command, the terminal displays the above output information with no error messages, indicating the SPI test passed.

Audio Playback Test
-------------------

Interface Silkscreen: CON10

Test Description: Play audio files to verify the evaluation board's audio playback function.

Test Operations

* Plug headphones into the interface corresponding to the silkscreen.

* Enter the following command for testing:

.. code-block:: shell

   amixer -c 0 cset name='Playback Path' 'HP'
   amixer -c 0 cset name='Playback Volume' 255
   aplay  /usr/share/sounds/alsa/Rear_Center.wav

* Result: Sound output from the headphones indicates the audio playback test passed.

SPEAKER Test
------------

Interface Silkscreen: J1

Test Description: The interface has 2 pins. Connect the speaker to the interface corresponding to silkscreen J1.

Test Operations

* Enter the following command:

.. code-block:: shell

   amixer -c 0 cset name='Playback Path' 'SPK'
   amixer -c 0 cset name='Playback Volume' 255
   aplay /usr/share/sounds/alsa/Rear_Center.wav

Sound output from the speaker indicates the test passed.

Recording Test
--------------

Interface Silkscreen: J2

Test Description: Record and play back the recording file for testing.

Test Operations

* Insert a microphone into the interface corresponding to the silkscreen.

* Enter the following command for a 10-second recording:

.. code-block:: shell

   amixer -c 0 cset name='Capture MIC Path' 'Main Mic'
   amixer -c 0 cset name='Capture Volume' 255
   arecord -c 1 -f S16_LE -r 44100 -d 10 -t wav /userdata/test.wav

* Connect headphones or speakers to the interfaces corresponding to silkscreen CON10 and J2 to play the recorded audio file. Enter the following command:

.. code-block:: shell

   aplay /userdata/test.wav

Hearing the recorded sound from the headphones or speakers indicates the recording test passed.

SD Interface Test
-----------------

Interface Silkscreen: CON5

Test Description: Test by inserting and removing a TF card.

Test Operations:

* Insert the TF card into the SD interface. The development board will output the following information:

[  380.723829] dwmmc_rockchip fe2c0000.mmc: could not set regulator OCR (-22)[  380.723921] dwmmc_rockchip fe2c0000.mmc: failed to enable vmmc regulator
[  380.736730] mmc_host mmc1: Bus speed (slot 0) = 400000Hz (slot req 400000Hz, actual 400000HZ div = 0)[  380.892477] mmc_host mmc1: Bus speed (slot 0) = 49500000Hz (slot req 50000000Hz, actual 49500000HZ div = 0)[  380.892687] mmc1: new high speed SDHC card at address 0001[  380.894512] mmcblk1: mmc1:0001 TF 4G 3.68 GiB
[  380.896321]  mmcblk1: p1
[  381.134266] FAT-fs (mmcblk1p1): utf8 is not a recommended IO charset for FAT filesystems, filesystem will be case sensitive!
[  381.140831] FAT-fs (mmcblk1p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

Result: The output information after the operation matches the expected result, indicating the TF card has been correctly recognized.

* Remove the TF card. The output information is as follows:

[  376.270975] mmc1: card 0001 removed

USB Test
--------

Interface Silkscreen: CON7

Test Description: Test by inserting and removing a USB storage device (USB flash drive).

Test Operations:

* Insert the USB device into the baseboard USB interface. The system will output information similar to:

[ 2649.580746] usb 2-1.1: new high-speed USB device number 3 using ehci-platform

[ 2649.735676] usb-storage 2-1.1:1.0: USB Mass Storage device detected

[ 2649.752030] scsi host0: usb-storage 2-1.1:1.0

[ 2649.951147] usbcore: registered new interface driver uas

[ 2650.801744] scsi 0:0:0:0: Direct-Access     aigo     U330             2.00 PQ: 0 ANSI: 4

[ 2650.822371] sd 0:0:0:0: [sda] 61440000 512-byte logical blocks: (31.5 GB/29.3 GiB)

[ 2650.830508] sd 0:0:0:0: Attached scsi generic sg0 type 0

[ 2650.851173] sd 0:0:0:0: [sda] Write Protect is off

[ 2650.871241] sd 0:0:0:0: [sda] No Caching mode page found

[ 2650.875217] sd 0:0:0:0: [sda] Assuming drive cache: write through

[ 2650.896991]  sda: sda1

[ 2650.916261] sd 0:0:0:0: [sda] Attached SCSI removable disk

* Remove the USB device from the baseboard. The system will output information similar to:

[ 2690.764161] usb 2-1.1: USB disconnect, device number 3

Display Screen
--------------

Interface Silkscreen: CON14

Test Description: Check whether the display screen shows normally when the development board starts up.

Test Operations

* Connect an HDMI display to the HDMI interface on the development board and start the development board.

The display showing normally indicates the test passed.

Multi-Video Playback Test
-------------------------

Test Description:

Open multivideoplayer on the HDMI interface and loop-play 9 videos.

GPU Test
--------

Test Description:

On the lower left corner of the HDMI interface, open the application with the 3D icon. After opening, the CPU temperature will rise.

After the test is complete, the following information will be displayed:
*=======================================================
glmark2 Score: 2281
*=======================================================

child 1905 exited

MPP Test
--------

Test Operations

* Video decoding: Enter the following command in the serial terminal:

.. code-block:: shell

   mpi_dec_test -i /oem/200frames_count.h264 -t 7 -n 250 -o /test.yuv -w 640 -h 480

Convert h264 to yuv, generating test.yuv in the current directory.

* Video encoding: Enter the following command in the serial terminal:

.. code-block:: shell

   mpi_enc_test -i /test.yuv -t 7 -n 250 -o /test.h264 -w 640 -h 480 -fps 25

Convert yuv to h264, generating test.h264 in the current directory.

Backlight Test
--------------

The backlight brightness setting range is (0--255), where 255 indicates maximum brightness and 0 indicates backlight off. After entering the system, enter the following commands in the terminal for backlight testing.

Enter the following command to view the current screen backlight value:

.. code-block:: shell

   cat /sys/class/backlight/ffb10000.dsi.0/brightness

The output information is similar to:

.. code-block:: shell

   200

Enter the following command to turn off the backlight:

.. code-block:: shell

   echo 0 > /sys/class/backlight/ffb10000.dsi.0/brightness

Enter the following command to turn on the backlight:

.. code-block:: shell

   echo 200 > /sys/class/backlight/ffb10000.dsi.0/brightness

USB Camera Test
---------------

Test Description: The camera feed is displayed on the screen to verify camera functionality.

Test Operations

* Connect a USB camera to one of the USB interfaces.

* Check the camera device:

.. code-block:: shell

   v4l2-ctl --list-devices

Bottom of output information:

.. code-block:: shell

   Full HD webcam: Full HD webcam (usb-xhci-hcd.10.auto-1):
       /dev/video36
       /dev/video37
       /dev/media4

* Check camera format command:

.. code-block:: shell

   v4l2-ctl --list-formats-ext -d /dev/video36

* Camera capture format query command:

.. code-block:: shell

   v4l2-ctl -V -d /dev/video36

* Playback camera feed command, using video36 node as an example:

.. code-block:: shell

   gst-launch-1.0 v4l2src device=/dev/video36 \
   ! 'image/jpeg,width=1920,height=1080,framerate=30/1' \
   ! jpegdec \
   ! videoconvert \
   ! autovideosink

The following information is output:

.. code-block:: shell

   Setting pipeline to PAUSED ...
   Pipeline is live and does not need PREROLL ...
   Pipeline is PREROLLED ...
   Setting pipeline to PLAYING ...
   New clock: GstSystemClock
   Redistribute latency...
   0:00:07.6 / 99:99:99.

The camera feed will appear on the HDMI interface.

EMMC Test
---------

Simple test of eMMC read/write speed, using read/write to ext4 file system as an example.

Enter the command to test write speed:

.. code-block:: shell

   dd if=/dev/zero of=/test bs=1M count=500 conv=fsync

The following information is output:

.. code-block:: shell

   500+0 records in
   500+0 records out
   524288000 bytes (524 MB, 500 MiB) copied, 14.2694 s, 36.7 MB/s

Enter the command to test read speed:

.. code-block:: shell

   dd if=/test of=/dev/null bs=1000M

The following information is output:

.. code-block:: shell

   0+1 records in
   0+1 records out
   524288000 bytes (524 MB, 500 MiB) copied, 0.819405 s, 640 MB/s

SARADC Interface Test
---------------------

Interface Silkscreen: J9

Test Description: Test by obtaining voltage values. This operation uses pin3 (SARADC0_IN2) of the EXPORT1 (J9) interface as an example. For testing other channels, please modify the corresponding device node according to the following table.

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;
       word-wrap: break-word;
   }
   </style>

+--------------+--------------+-----------------------------------------------------+
| ADC Channel  | ADC Pin (J9) | Device Node                                         |
+==============+==============+=====================================================+
| SARADC0\_IN2 | pin3         | /sys/bus/iio/devices/iio\:device0/in\_voltage2\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC0\_IN3 | pin5         | /sys/bus/iio/devices/iio\:device0/in\_voltage3\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC0\_IN4 | pin7         | /sys/bus/iio/devices/iio\:device0/in\_voltage4\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC0\_IN5 | pin9         | /sys/bus/iio/devices/iio\:device0/in\_voltage5\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC0\_IN6 | pin11        | /sys/bus/iio/devices/iio\:device0/in\_voltage6\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC0\_IN7 | pin13        | /sys/bus/iio/devices/iio\:device0/in\_voltage7\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC1\_IN0 | pin4         | /sys/bus/iio/devices/iio\:device1/in\_voltage0\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC1\_IN1 | pin6         | /sys/bus/iio/devices/iio\:device1/in\_voltage1\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC1\_IN2 | pin8         | /sys/bus/iio/devices/iio\:device1/in\_voltage2\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC1\_IN3 | pin10        | /sys/bus/iio/devices/iio\:device1/in\_voltage3\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC1\_IN4 | pin12        | /sys/bus/iio/devices/iio\:device1/in\_voltage4\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC1\_IN5 | pin14        | /sys/bus/iio/devices/iio\:device1/in\_voltage5\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC1\_IN6 | pin16        | /sys/bus/iio/devices/iio\:device1/in\_voltage6\_raw |
+--------------+--------------+-----------------------------------------------------+
| SARADC1\_IN7 | pin18        | /sys/bus/iio/devices/iio\:device1/in\_voltage7\_raw |
+--------------+--------------+-----------------------------------------------------+

Test Operations

a) Use a jumper wire to connect pin3 (SARADC0_IN2) of the board's EXPORT1 (J9) interface to pin1 (VDD_1V8_MAIN, level 1.8V).

b) Enter the board's file system and execute the following command for input voltage testing:

.. code-block:: shell

   cat /sys/bus/iio/devices/iio\:device0/in_voltage2_raw

The output information is similar to:

.. code-block:: shell

   1023

c) Power off the board. Use a jumper wire to connect pin3 (SARADC0_IN2) of the evaluation board's EXPORT1 (J9) interface to pin2 (GND).

d) Enter the board's file system and execute the following command for ground testing:

.. code-block:: shell

   cat /sys/bus/iio/devices/iio\:device0/in_voltage2_raw

The output information is similar to:

.. code-block:: shell

   0

Actual input voltage value Vin = 1023 x [1.8 / (2^10 - 1)] ≈ 1.79V, which is close to the input voltage. The voltage test output information around 1000 and the ground test output information of 0 indicate the test passed.

MIPI CSI Interface Test
-----------------------

Interface Silkscreen: J5, J6

Test Description: Test by using a camera and displaying the camera feed on the monitor.

Test Operations:

1. Connect the camera to the corresponding interface on the development board via the FPC cable. Be careful not to connect it in reverse.

2. Copy the script files and ISP parameter files from the camera directory in the cloud drive to the corresponding directory on the development board.

.. code-block:: shell

   # 1. Transfer files to the development board via adb
   adb push ov13850_RK-CMK-8M-2-v1_CK8401.json/etc/iqfiles
   adb push two_camera_ov13850.sh /
   
   # 2. Convert characters and reboot
   dos2unix /etc/iqfiles/ov13850_RK-CMK-8M-2-v1_CK8401.json
   reboot
   
   # Grant permissions and execute the script
   chmoda+xtwo_camera_ov13850.sh
   ./two_camera_ov13850.sh