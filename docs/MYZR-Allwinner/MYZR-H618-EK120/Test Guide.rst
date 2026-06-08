Test Guide
=============

|  Note: Since some commands or file modifications during testing require root privileges, it is recommended to switch to the root user using the following command before starting the test.

.. code-block:: shell

   su -

GPIO Test
------------

|  Before testing a pin, you need to know the corresponding pin number. AllwinnerPin is a pin number calculator software for Allwinner chips.
|  Let's take the PH6 pin of the J11 pin header as an example. First, input PH6 into AllwinnerPin and click calculate.

.. figure:: /image/MYZR-全志系列/MYZR-H618-EK120/测试1.png
   :alt: Test1.png

|  You can get the pin number and control the pin using commands:

.. code-block:: shell

   echo 230 > /sys/class/gpio/export # Export the pin
   echo out > /sys/class/gpio/gpio230/direction # Set to output mode
   echo 1 > /sys/class/gpio/gpio230/value # Set to high level

|  At this point, use the command:

.. code-block:: shell

   cat /sys/class/gpio/gpio230/value

|  It should return 1, indicating that the pin has been set to high level, or use a multimeter to measure PH6, and the pin voltage should be 3.3V.

Ethernet Test
----------------

|  Interface silkscreen: J6
|  System interface: eth0
|  Test description: Test by sending ICMP packets from the development board to the PC
|  Test operation

1. Configure the computer's wired network card IP to 192.168.137.99
2. Connect the development board's Ethernet port to the computer's Ethernet port with a network cable
3. Check the information of the development board's Ethernet port 1 by entering the following command:

.. code-block:: shell

   ifconfig eth0

4. Configure the IPv4 address for Ethernet port 1 by entering the following command:

.. code-block:: shell

   ifconfig eth0 192.168.137.18 netmask 255.255.255.0

5. Check the information of the development board's Ethernet port 1 again to confirm whether the IPv4 address is successfully configured. If not, re-execute from step 4 by entering the following command:

.. code-block:: shell

   ifconfig eth0

6. Enter the following command to verify Ethernet port 1:

.. code-block:: shell

   ping -I eth0 192.168.137.99 -c 3

|  "0% packet loss" indicates the test passed.


USB Test
-----------

|  Interface silkscreen: J4
|  Test description: Test by plugging and unplugging a USB storage device (USB flash drive)
|  Test operation

1. Insert the USB flash drive into the USB interface of the base board

|  Enter the command:

.. code-block:: shell

   lsblk -d -o NAME,SIZE,MODEL,VENDOR,TRAN | grep -v "loop\|mmcblk"

|  You can see similar return information as follows, indicating that the USB interface is successfully recognized:

.. code-block:: shell

   NAME           SIZE MODEL VENDOR   TRAN
   sda            7.5G UDisk General  usb

Audio Playback Test
----------------------

|  Interface silkscreen: P1
|  Test description: Verify the audio playback function of the development board by playing an audio file
|  Test operation

1. Connect headphones or speakers to the interface corresponding to the silkscreen
2. Enter the following command for testing:

.. code-block:: shell

   aplay /mytest.wav

|  Sound output from the headphones indicates that the audio playback test passed.


UART Test
------------

|  Interface silkscreen: J11
|  Test description: Test using UART self-transmit and self-receive
|  Preparation before test: After the development board starts, modify the /boot/uEnv.txt file and add

.. code-block:: shell

   overlays=h618-myzr-uart5-overlay.dtbo

|  Then save and exit, and restart the development board.
|  Test operation

1. Short-circuit the J11-PH2 (UART5_TX) and J11-PH3 (UART5_RX) pins (please refer to the silkscreen diagram)
2. Enter the following command for transceiving test:

.. code-block:: shell

   /serial_test /dev/ttyAS5 "myzr"

|  After executing the test command, output similar to the following indicates that the UART test passed. Press 'Ctrl + C' to exit.

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d          Character: m 
   ASCII: 0x79          Character: y 
   ASCII: 0x7a          Character: z 
   ASCII: 0x72          Character: r 
   ASCII: 0x0          Character:  


SPI Test
-----------

|  Interface silkscreen: J11
|  Test description: Test using SPI self-transmit and self-receive
|  Preparation before test: After the development board starts, modify the /boot/uEnv.txt file and add

.. code-block:: shell

   overlays=h618-myzr-spi1-overlay.dtbo

|  Then save and exit, and restart the development board.
|  Test operation

1. Short-circuit the J11-PH7 (SPI1.0_MOSI) and J11-PH8 (SPI1.0_MISO) pins
2. Enter the following command for transceiving test:

.. code-block:: shell

   /spidev_test -D /dev/spidev1.0

|  After executing the test command, output similar to the following indicates that the SPI test passed:

.. code-block:: shell

   spi mode: 0
   bits per word: 8
   max speed: 100000 Hz (100 KHz)

   FF FF FF FF FF FF 
   40 00 00 00 00 95 
   FF FF FF FF FF FF 
   FF FF FF FF FF FF 
   FF FF FF FF FF FF 
   DE AD BE EF BA AD 
   F0 0D 

|  Note: The only difference between the spidev1.0 and spidev1.1 interfaces is their corresponding chip select signals.


Infrared Test
----------------

|  Interface silkscreen: J8
|  Test description: Receive infrared information and print the corresponding data
|  Test operation

1. Use the phone's infrared remote control app and select the Hisense TV remote control
2. Turn on the relevant print switch by entering the following command:

.. code-block:: shell

   hexdump /dev/input/event0

3. Aim the remote control at the infrared interface and press any button
4. The development board successfully receives if it displays relevant button information. You can see similar return information as follows:

.. code-block:: shell

   0000000 a71e 6899 0000 0000 1280 0007 0000 0000
   0000010 0004 0004 000d 01bf a71e 6899 0000 0000
   0000020 1280 0007 0000 0000 0000 0000 0000 0000
   0000030 a71e 6899 0000 0000 5e17 000a 0000 0000
   0000040 0004 0004 000d 00bf a71e 6899 0000 0000
   0000050 5e17 000a 0000 0000 0000 0000 0000 0000
 

WiFi Test
-----------

|  Antenna interface silkscreen: CN1
|  Test description: An antenna needs to be connected before testing. After the WiFi is connected to the AP, the development board sends ICMP packets to the external network to verify normal connection.
|  Test operation
|  Generate the WPA PSK file for SSID by entering:

.. code-block:: shell

   wpa_passphrase MY-WIFI My202412 > /etc/wpa_supplicant.conf

|  Connect:

.. code-block:: shell

   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

|  Obtain IP:

.. code-block:: shell

   dhclient -v wlan0 

|  Test connection:

.. code-block:: shell

   ping 8.8.8.8

|  After executing the test command, output similar to the following indicates that the WiFi test passed. Press 'Ctrl + C' to exit.

.. code-block:: shell

   PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
   64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=182 ms
   64 bytes from 8.8.8.8: icmp_seq=4 ttl=115 time=41.6 ms
   64 bytes from 8.8.8.8: icmp_seq=7 ttl=115 time=47.7 ms
   64 bytes from 8.8.8.8: icmp_seq=8 ttl=115 time=98.3 ms

Bluetooth Test
----------------

|  Antenna interface silkscreen: CN1
|  Test description: An antenna needs to be connected before testing. After scanning for Bluetooth devices, send an L2CAP echo request and receive a response.
|  The system has a built-in bluetoothctl command-line tool. Enter commands directly to start and connect Bluetooth:

.. code-block:: shell

   # 1. Enter Bluetooth control terminal
   bluetoothctl

   # 2. Turn on Bluetooth and initialize (execute line by line)
   [bluetooth]# power on
   [bluetooth]# agent on
   [bluetooth]# default-agent

   # 3. Scan for surrounding devices (for 10 seconds)
   [bluetooth]# scan on
   # Wait for the target device to appear (e.g.: 60:C7:BE:27:3E:CE myzr)
   # Press Ctrl+C to stop scanning

   # 4. Pair and connect the device (replace with actual MAC)
   [bluetooth]# trust 60:C7:BE:27:3E:CE
   [bluetooth]# pair 60:C7:BE:27:3E:CE
   # Confirm the pairing code on the mobile phone (enter yes in the serial terminal)

   # 5. Verify connection status
   [bluetooth]# info 60:C7:BE:27:3E:CE
   # Check "Connected: yes" and "Paired: yes"

   # 6. Disconnect
   [bluetooth]# disconnect 60:C7:BE:27:3E:CE
   [bluetooth]# remove 60:C7:BE:27:3E:CE
   [bluetooth]# exit


Display Screen
----------------

|  Interface silkscreen: J5
|  Test description: Check if the display screen shows normally when the development board is powered on and starts up
|  Test operation
|  Connect an HDMI screen to the HDMI interface on the development board and start the development board
|  Normal display on the screen indicates the test passed.