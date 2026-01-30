Test Manual
=============

Ethernet Port 0 Test
-----------------------

1. Connect the host to Ethernet Port 1 of the development board with a network cable, and set the host IP address to the same network segment as the gateway, e.g., 192.168.131.99

.. figure:: /image/MYZR-其他/网关/GW510/测试手册1.png
   :alt: 测试手册1.png
   :width: 90%

2. Open a serial terminal such as Xhell, enter the default gateway IP address 192.168.131.81, select SSH as the protocol, and click Connect at last

.. figure:: /image/MYZR-其他/网关/GW510/测试手册2.png
   :alt: 测试手册2.png
   :width: 90%

3. After a successful connection, the following message pops up to receive the host key, click to receive and save it

.. figure:: /image/MYZR-其他/网关/GW510/测试手册3.png
   :alt: 测试手册3.png
   :width: 90%

4. After saving, the following interface pops up, enter the username **root** and click OK

.. figure:: /image/MYZR-其他/网关/GW510/测试手册4.png
   :alt: 测试手册4.png
   :width: 90%

5. Successful access to the system indicates that the SSH login via the Ethernet port is successful

.. figure:: /image/MYZR-其他/网关/GW510/测试手册5.png
   :alt: 测试手册5.png
   :width: 90%

Ethernet Port 1 Test
-----------------------

|  **Test Description**: Test by sending ICMP packets from the development board to the PC
|  **Interface Identifier**: J2
|  **System Device**: /dev/eth1
|  **Test Operations**:

1. Connect the Ethernet port of the development board to the Ethernet port of the PC with a network cable, the serial port displays the information:

.. code-block:: shell

   [emac_phy_link_adjust] EMAC Link Up

2. Obtain the IP address of Ethernet Port 1, enter the following command:

.. code-block:: shell

   udhcpc -i eth1

3. The output information is as follows:

.. code-block:: shell

   udhcpc: started, v1.37.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.128.194, server 192.168.128.1
   udhcpc: lease of 192.168.128.194 obtained from 192.168.128.1, lease time 300
   deleting routers
   adding dns 192.168.128.1

4. Verify the network of Ethernet Port 1, enter the following command:

.. code-block:: shell

   ping -I eth1 www.baidu.com -c 3

5. The output information is as follows: **0% packet loss** indicates the test is passed

.. code-block:: shell

   PING www.baidu.com (183.2.172.177): 56 data bytes
   64 bytes from 183.2.172.177: seq=0 ttl=54 time=6.859 ms
   64 bytes from 183.2.172.177: seq=1 ttl=54 time=6.508 ms
   64 bytes from 183.2.172.177: seq=2 ttl=54 time=6.886 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 packets received, 0% packet loss
   round-trip min/avg/max = 6.508/6.751/6.886 ms

SD Interface Test
--------------------

|  **Test Description**: Insert a TF card.
|  **Interface Identifier**: U19
|  **System Device**: /dev/mmcblk0 mmcblk0p1
|  **Test Operations**:

1. Install the TF card into the SD interface, the development board outputs the following information:

.. code-block:: shell

   >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] HS mode. <<

2. Enter the following command to view the SD card information:

.. code-block:: shell

   fdisk -l

|  The information is as follows:

.. code-block:: shell

   Disk /dev/mmcblk0: 7388 MB, 7746879488 bytes, 15130624 sectors
   938 cylinders, 256 heads, 63 sectors/track
   Units: sectors of 1 * 512 = 512 bytes

   Device       Boot StartCHS    EndCHS        StartLBA     EndLBA    Sectors  Size Id Type
   /dev/mmcblk0p1 *  1023,255,63 1023,255,63       2048   15130623   15128576 7387M  c Win95 FAT32 (LBA)
   Partition 1 has different physical/logical start (non-Linux?):
        phys=(1023,255,63) logical=(0,32,33)
   Partition 1 has different physical/logical end:
        phys=(1023,255,63) logical=(938,40,40)

3. Pull out the TF card, the output information is as follows:

.. code-block:: shell

|  SDMMC0 >> [Hal_CARD_SetBustiming] LS mode. <<
|  SDMMC0 >> [Hal_CARD_SetBustiming] DEFS mode. <<

|  **Result**: The phenomenon during operation is in line with the expected correct behavior, indicating normal hot plug of the TF card.

RTC Test
----------

|  **Test Description**: Read and set the time, check if the time is correct after power off and restart
|  **Interface Identifier**: CON1
|  **System Device**: /dev/rtc0
|  **Test Operations**:

1. Power on the device, view the current system clock, enter the following command:

.. code-block:: shell

   date

|  Output information:

.. code-block:: shell

   Sat Jan  1 00:26:33 UTC 2000

2. View the RTC clock, enter the following command:

.. code-block:: shell

   hwclock

|  Output information:

.. code-block:: shell

   Sat Jan  1 00:26:54 2000  0.000000 seconds

3. Set the system time, enter the following command:

.. code-block:: shell

   date -s "2026-1-29 9:30:00"

4. Write the system time to RTC and check it, enter the following commands:

.. code-block:: shell

   hwclock -w
   hwclock

5. Power off the device and check if the time is successfully written, enter the following command:

.. code-block:: shell

   hwclock

|  Output information:

.. code-block:: shell

   Thu Jan 29 09:32:10 2026  0.000000 seconds

|  **Result**: The time is approximately the same as the system time and keeps running, indicating the time is successfully written to RTC.

RS232 Test
-------------

|  **Test Description**: Short-circuit 232_TX1 & 232_RX1, 232_TX2 & 232_RX2 for self-transmission and reception test
|  **Interface Identifier**: 232_TX1,232_RX1  232_TX2,232_RX2
|  **System Device**: /dev/ttyS4,ttyS5
|  **Test Operations**:

1. Short-circuit 232_TX1 and 232_RX1 with a Dupont wire
2. Enter the test directory, enter the following command:

.. code-block:: shell

   cd /customer/app/

3. Run the test program, enter the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS4 "www.myzr.com.cn"

|  The output information is as follows:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x77          Character: w 
   ASCII: 0x77          Character: w 
   ASCII: 0x77          Character: w 
   ASCII: 0x2e          Character: . 
   ASCII: 0x6d          Character: m 
   ASCII: 0x79          Character: y 
   ASCII: 0x7a          Character: z 
   ASCII: 0x72          Character: r 
   ASCII: 0x2e          Character: . 
   ASCII: 0x63          Character: c 
   ASCII: 0x6f          Character: o 
   ASCII: 0x6d          Character: m 
   ASCII: 0x2e          Character: . 
   ASCII: 0x63          Character: c 
   ASCII: 0x6e          Character: n 
   ASCII: 0x0          Character:  

4. Short-circuit 232_TX2 and 232_RX2 with a Dupont wire
5. Enter the test directory, enter the following command:

.. code-block:: shell

   cd /customer/app/

6. Run the test program, enter the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS5 "www.myzr.com.cn"

|  The output information is as follows:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x77          Character: w 
   ASCII: 0x77          Character: w 
   ASCII: 0x77          Character: w 
   ASCII: 0x2e          Character: . 
   ASCII: 0x6d          Character: m 
   ASCII: 0x79          Character: y 
   ASCII: 0x7a          Character: z 
   ASCII: 0x72          Character: r 
   ASCII: 0x2e          Character: . 
   ASCII: 0x63          Character: c 
   ASCII: 0x6f          Character: o 
   ASCII: 0x6d          Character: m 
   ASCII: 0x2e          Character: . 
   ASCII: 0x63          Character: c 
   ASCII: 0x6e          Character: n 
   ASCII: 0x0          Character:  

RS485 Test
-------------

|  **Test Description**: Interconnect with the PC via a 485-USB converter for transmission and reception test
|  **Interface Identifier**: 485_A1,485_B1,485_A2,485_B2,485_A3,485_B3
|  **System Device**: /dev/ttyS2，/dev/ttyS6，/dev/ttyS7
|  **Test Operations**:

1. Connect the development board to the PC with a 485-USB converter (A to A, B to B)
2. Open the corresponding serial port with Xshell, set the baud rate to 115200, 8 data bits, 1 stop bit
3. Enter the test directory, enter the following command:

.. code-block:: shell

   cd /customer/app/

4. Run the test, enter the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS2 "www.myzr.com.cn"

|  The result can be seen from the output of the 485 serial terminal:

.. code-block:: shell

   www.myzr.com.cn

5. Enter **123** (without display) in the 485 serial terminal, and **123** can be seen in the board terminal

.. code-block:: shell

   root@myzr:/customer/app# ./serial_test.out /dev/ttyS6 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0xbf          Character: ¿ 
   ASCII: 0x7f          Character: 
   ASCII: 0xfb          Character: 
   ASCII: 0xbf          Character: ¿ 
   ASCII: 0xfe          Character: þ 
   ASCII: 0xbf          Character: ¿ 
   ASCII: 0xbe          Character: ¾ 
   ASCII: 0x80          Character:  
   ASCII: 0x31          Character: 1 
   ASCII: 0x32          Character: 2 
   ASCII: 0x33          Character: 3 
   ASCII: 0xd           Character: 

6. 485_A2 & 485_B2 correspond to ttyS6, 485_A3 & 485_B3 correspond to ttyS7, the test method is the same as above.

Relay Test
-------------

|  **Test Description**: Set high and low levels for GPIO pins to test the pull-in of the relay
|  **Interface Identifier**: J8,J9
|  **System Device**:
|  **Test Operations**:

1. Enter the following commands to set high and low levels for the GPIO pin (J8 relay) to test its pull-in:

.. code-block:: shell

   echo 121 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio121/direction
   echo 1 > /sys/class/gpio/gpio121/value
   echo 0 > /sys/class/gpio/gpio121/value

|  **Result**: The pull-in sound of the relay can be heard.

2. Enter the following commands to set high and low levels for the GPIO pin (J9 relay) to test its pull-in:

.. code-block:: shell

   echo 122 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio122/direction
   echo 1 > /sys/class/gpio/gpio122/value
   echo 0 > /sys/class/gpio/gpio122/value

|  **Result**: The pull-in sound of the relay can be heard.

LED Test
-----------

|  **Test Description**: Set high and low levels for GPIO pins to test the on and off of the LED
|  **Interface Identifier**: P3
|  **System Device**: LED
|  **Test Operations**:

1. Enter the following commands to set a high level for the GPIO pin (middle LED) to test the light-on function:

.. code-block:: shell

   echo 98 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio98/direction
   echo 1 > /sys/class/gpio/gpio98/value

|  **Result**: Normal if the middle LED is on.

2. Enter the following command to set a low level for the GPIO pin (middle LED) to test the light-off function:

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio98/value

|  **Result**: Normal if the middle LED is off.

3. Enter the following commands to set a high level for the GPIO pin (bottom LED) to test the light-on function:

.. code-block:: shell

   echo 82 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio82/direction
   echo 1 > /sys/class/gpio/gpio82/value

|  **Result**: Normal if the bottom LED is on.

4. Enter the following command to set a low level for the GPIO pin (bottom LED) to test the light-off function:

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio82/value

|  **Result**: Normal if the bottom LED is off.

4G Test
---------

|  **Test Description**: After the 4G connection is successful, the development board sends ICMP packets to the external network to verify the normal connection
|  **Interface Identifier**: U38
|  **System Device**: /dev/ttyUSB1，usb0
|  **Test Operations**:

1. Connect the 4G antenna to the **U3** interface and insert the SIM card into the **J3** card slot
2. Set a high level for the 4G_PWRKEY1 pin to power on the 4G module, enter the following commands:

.. code-block:: shell

   echo 98 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio98/direction
   echo 1 > /sys/class/gpio/gpio98/value
   echo 64 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio64/direction
   echo 1 > /sys/class/gpio/gpio64/value

3. Enter the following command to adapt and start the 4G module:

.. code-block:: shell

   echo -e "AT+QNETDEVCTL=3,1,1\r\n" > /dev/ttyUSB1

4. Enter the following command to check if the 4G module is started successfully:

.. code-block:: shell

   lsusb

|  The output information is as follows, the appearance of **Quectel EC801E-CN** indicates success; wait for 1 minute if it does not appear:

.. code-block:: shell

   Bus 001 Device 001: ID 1d6b:0002 Linux 6.1.111-rt42 ehci_hcd EHCI Host Controller
   Bus 001 Device 003: ID 0bda:d723 Realtek 802.11n WLAN Adapter
   Bus 001 Device 002: ID 1a40:0101 USB 2.0 Hub
   Bus 001 Device 005: ID 2c7c:0903 Quectel EC801E-CN

5. Enter the following command to obtain an IP address:

.. code-block:: shell

   udhcpc -i usb0

|  The output information is as follows:

.. code-block:: shell

   udhcpc: started, v1.37.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.43.100, server 192.168.43.1
   udhcpc: lease of 192.168.43.100 obtained from 192.168.43.1, lease time 86400
   deleting routers
   adding dns 192.168.43.2
   adding dns 192.168.43.3

6. Enter the following command to verify the 4G connection:

.. code-block:: shell

   ping -I usb0 www.baidu.com -c 3

|  The output information is as follows: **0% packet loss** indicates the test is passed

.. code-block:: shell

   PING www.baidu.com (183.240.99.224): 56 data bytes
   64 bytes from 183.240.99.224: seq=0 ttl=51 time=56.363 ms
   64 bytes from 183.240.99.224: seq=1 ttl=51 time=56.105 ms
   64 bytes from 183.240.99.224: seq=2 ttl=51 time=55.599 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 packets received, 0% packet loss
   round-trip min/avg/max = 55.599/56.022/56.363 ms

WiFi STA Test
----------------

|  **Test Description**: After the WiFi connection is successful, the development board sends ICMP packets to the external network to verify the normal connection
|  **Interface Identifier**: U41
|  **System Device**: wlan0
|  **Test Operations**:

1. Connect the WiFi antenna to the **U40** interface
2. Generate a WPA PSK file for the SSID, where **MY-WIFI** is the WiFi name and **My202412** is the password, enter the following commands:

.. code-block:: shell

   wpa_passphrase MY-WIFI My202412 > /etc/wpa_supplicant.conf
   wpa_passphrase MYZR-WiFi-5G Myzr2012 > /etc/wpa_supplicant.conf

4. Establish the connection, enter the following command:

.. code-block:: shell

   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

5. Output information:

.. code-block:: shell

   Successfully initialized wpa_supplicant
   nl80211: kernel reports: Authentication algorithm number required
   [  266.744713] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready

6. Obtain an IP address, enter the following command:

.. code-block:: shell

   udhcpc -i wlan0

|  Output information:

.. code-block:: shell

   udhcpc: started, v1.36.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.43.35, server 192.
   udhcpc: lease of 192.168.43.35 obtained from 192.168.43.1, lease time 3600
   deleting routers
   adding dns 192.168.43.1

7. Test the connection, enter the following command:

.. code-block:: shell

   ping -I wlan0 www.baidu.com -c 3

|  Output information: **0% packet loss** indicates the WiFi connection is normal

.. code-block:: shell

   PING www.baidu.com (183.2.172.177) from 192.168.61.73 wlan0: 56(84) bytes of data.
   64 bytes from 183.2.172.177: icmp_seq=1 ttl=54 time=10.0 ms
   64 bytes from 183.2.172.177: icmp_seq=2 ttl=54 time=13.2 ms
   64 bytes from 183.2.172.177: icmp_seq=3 ttl=54 time=14.5 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 10.031/12.576/14.482/1.872 ms

Bluetooth
------------

|  **Test Description**: After the gateway connection is successful, the gateway and the node perform transmission and reception to verify the normal connection
|  **Interface Identifier**: U53
|  **System Device**: /dev/ttyS3
|  **Test Operations**:

**Connect two development boards, one with the Bluetooth module set as G(mesh) (gateway) and the other as N(mesh) (node)**

1. Enter the test application directory on both terminals, enter the following command:

.. code-block:: shell

   cd /customer/app

2. Enter the following command on the gateway terminal:

.. code-block:: shell

   ./wg

|  The output information is as follows, indicating the gateway has connected to the node:

.. code-block:: shell

   ===== Bluetooth Gateway Config Tool (Linux) =====
   Serial port /dev/ttyS3 opened successfully (Baudrate: 4098)

   ===== Step 1: Read Gateway Info =====
   Send: E9 FF 0C 
   Recv: 1C 00 91 8B 01 AE 24 1C D2 6E BC B0 8E EA B1 B9 C8 EC D1 8A A3 00 00 00 11 22 33 44 00 00 03 00 91 8C 01 

   ===== Step 2: Set Gateway Key =====
   Send: E9 FF 09 AE 24 1C D2 6E BC B0 8E EA B1 B9 C8 EC D1 8A A3 00 00 00 11 22 33 44 01 00 
   Recv: 06 00 91 9A 11 22 33 44 

   ===== Step 3: Set Gateway Params =====
   Send: E9 FF 0D 01 00 02 19 B1 24 E7 99 B7 9B D3 10 82 B6 C8 A9 A9 56 

   ===== Step 4: Scan Nodes =====
   Send: E9 FF 00 

   ===== Step 5: Set Broadcast Filter =====
   Send: E9 FF 08 4E AC 57 38 C1 A4 

   ===== Step 6: Config Node Params =====
   Send: E9 FF 0A AE 24 1C D2 6E BC B0 8E EA B1 B9 C8 EC D1 8A A3 00 00 00 11 22 33 44 02 00 

   ===== Step 7: Bind Operation =====
   Send: E9 FF 0B 00 00 00 60 96 47 71 73 4F BD 76 E3 B4 05 19 D1 D9 4A 48 
   Recv: 09 00 91 B5 01 00 02 00 80 08 FF 
   Recv: 09 00 91 B5 01 00 02 00 80 08 FF 
   Recv: 03 00 91 8A 02 
   Recv: 03 00 91 82 01 

   ===== All Config Steps Completed. Serial Port Closed =====

3. Enter the following command on the node terminal to make the node enter the receiving state:

.. code-block:: shell

   ./serial_test.out /dev/ttyS1 1

4. Enter the following command on the gateway terminal to send **12345** to the node:

.. code-block:: shell

   ./n0x002

|  At this time, the node terminal can receive 12345, the information is as follows:

.. code-block:: shell

   root@myzr:/customer/app# ./serial_test.out /dev/ttyS3 1
   Starting send data...finish
   Starting receive data:
   ASCII: 0x7          Character:  
   ASCII: 0x0          Character:  
   ASCII: 0x93          Character:  
   ASCII: 0x0          Character:  
   ASCII: 0x31          Character: 1 
   ASCII: 0x32          Character: 2 
   ASCII: 0x33          Character: 3 
   ASCII: 0x34          Character: 4 
   ASCII: 0x35          Character: 5 

5. Enter the following command on the gateway terminal to make the gateway enter the receiving state:

.. code-block:: shell

   ./serial_test.out /dev/ttyS1 1

6. Enter the following command on the node terminal to send **12345** to the gateway:

.. code-block:: shell

   ./a

|  At this time, the gateway terminal can receive 12345, the information is as follows:

.. code-block:: shell

   root@myzr:/customer/app# ./serial_test.out /dev/ttyS3 1
   Starting send data...finish
   Starting receive data:
   ASCII: 0xc          Character: 

   ASCII: 0x0          Character:  
   ASCII: 0x91          Character:  
   ASCII: 0x81          Character:  
   ASCII: 0x3          Character:  
   ASCII: 0x0          Character:  
   ASCII: 0x1          Character:  
   ASCII: 0x0          Character:  
   ASCII: 0x52          Character: R 
   ASCII: 0x31          Character: 1 
   ASCII: 0x32          Character: 2 
   ASCII: 0x33          Character: 3 
   ASCII: 0x34          Character: 4 
   ASCII: 0x35          Character: 5 

7. If a module is used for the node, use a serial port software with the following configuration:

.. figure:: /image/MYZR-其他/网关/GW510/测试手册6.png
   :alt: 测试手册6.png
   :width: 90%

|  When the gateway runs **./n0x002**, this page will receive **07 00 93 00 31 32 33 34 35**
|  When sending information from the node to the gateway, configure the page as above and click to send **00 ff 00 01 31 32 33 34 35 36**. Before sending, run **./serial_test.out /dev/ttyS1 1** on the gateway terminal to make the gateway enter the receiving state for receiving **123456** sent by the node.

LoRa Test
------------

|  **Test Description**: Start two development terminals for transmission and reception to verify the normal connection
|  **Interface Identifier**: U51
|  **System Device**: /dev/ttyS3
|  **Test Operations**:

1. Connect the antenna to the **U51** interface
2. Enter the test directory, enter the following command:

.. code-block:: shell

   cd /customer/app/

3. Configure the working mode (M0=1,M1=0), enter the following commands (required for both terminals):

.. code-block:: shell

   echo 96 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio96/direction
   echo 1 > /sys/class/gpio/gpio96/value
   echo 97 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio97/direction
   echo 0 > /sys/class/gpio/gpio97/value

4. On Terminal 2, enter the following command:

.. code-block:: shell

   ./lora /dev/ttyS1 12345

5. Output information:

.. code-block:: shell

   Sent: 12345
   Entering receive mode...

6. On Terminal 1, enter the following command:

.. code-block:: shell

   ./lora /dev/ttyS1 12345

7. Observe Terminal 2 at this time, the received output information is as follows:

.. code-block:: shell

   Sent: 12345
   Entering receive mode...
   Received: 123456

8. Stop the reception on Terminal 2 at this time and send information to Terminal 1, enter the following commands:

.. code-block:: shell

   ^C（CTRL C Stop receiving）
   ./lora /dev/ttyS3 12345

9. Observe Terminal 1 at this time, the received output information is as follows:

.. code-block:: shell

   Sent: 123456
   Entering receive mode...
   Received: 12345

DO Test
----------

|  **Test Description**: Verify the input and output functions
|  **Interface Identifier**: OUT0+,OUT0-
|  **System Device**:
|  **Test Operations**:

1. DO Test Wiring Diagram

.. figure:: /image/MYZR-其他/网关/GW510/测试手册7.png
   :alt: 测试手册7.png
   :width: 90%

|  **Note**: Set the voltage to 3.3V, the current to 0.1A, and the overcurrent protection to 0.12A.

2. Connect the OUT+ pin to a 3.3V power supply, and measure the OUT- pin with an oscilloscope or multimeter. The OUT- pin is at low level by default, and will be at 3V-3.3V after the OUT+ pin is connected to a 3.3V power supply. You can also view the pin status with the following commands.
3. Enter the following commands to perform the pull-up test:

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   echo 1 > /sys/class/gpio/gpio126/value

|  At this time, measure the OUT- pin with an oscilloscope or multimeter, and the voltage of OUT- will be 3V-3.3V.
|  You can also view the pin status with the following commands:

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   cat /sys/class/gpio/gpio126/value

|  The output information is **1**.

4. Enter the following commands to perform the pull-down test:

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   echo 0 > /sys/class/gpio/gpio126/value

|  At this time, measure the OUT- pin with an oscilloscope or multimeter, and the voltage of OUT- will be 0V.
|  You can also view the pin status with the following commands:

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   cat /sys/class/gpio/gpio126/value

|  The output information is **0**.

DI Test
----------

|  **Test Description**: Verify the input and output functions
|  **Interface Identifier**: IN0+,IN0-
|  **System Device**:
|  **Test Operations**:

1. DI Test Wiring Diagram

.. figure:: /image/MYZR-其他/网关/GW510/测试手册8.png
   :alt: 测试手册8.png
   :width: 90%

2. Connect the IN0+ pin to a 3.3V power supply and the IN0- pin to GND.

|  **Note**: Set the voltage to 3.3V, the current to 0.1A, and the overcurrent protection to 0.12A.

3. When the 3.3V power supply for the IN0+ pin is not turned on, the read level is **1**:

.. code-block:: shell

   echo 125 > /sys/class/gpio/export
   echo in > /sys/class/gpio/gpio125/direction
   cat /sys/class/gpio/gpio125/value

|  **Test Result**: Success if **1** is displayed.

.. code-block:: shell

   root@myzr:~# cat /sys/class/gpio/gpio125/value
   1

|  When the 3.3V power supply for the IN0+ pin is turned on and the IN0- pin is connected to GND, the read level is **0**:

.. code-block:: shell

   echo 125 > /sys/class/gpio/export
   echo in > /sys/class/gpio/gpio125/direction
   cat /sys/class/gpio/gpio125/value

|  **Test Result**: Failure if **0** is displayed.

.. code-block:: shell

   root@myzr:~# cat /sys/class/gpio/gpio125/value
   0
