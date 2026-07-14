Test Guide
==========

Product Test Guide
-------------

Ethernet Port 0 Test
~~~~~~~~~~~

1. Use an Ethernet cable to connect the host computer to Ethernet Port 1 of the development board, and set the host IP address to the same subnet as the gateway, e.g., 192.168.131.99

.. figure:: ../../../../image/MYZR-其他/网关/GW510/测试手册1.png
   :alt: Test Manual 1
   :width: 100%

2. Open a serial terminal such as Xshell, enter the gateway's default IP address 192.168.131.81, select SSH protocol, and click connect

.. figure:: ../../../../image/MYZR-其他/网关/GW510/测试手册2.png
   :alt: Test Manual 2
   :width: 100%

3. After successful connection, the following message will pop up to receive the host key, click to accept and save

.. figure:: ../../../../image/MYZR-其他/网关/GW510/测试手册3.png
   :alt: Test Manual 3
   :width: 100%

4. After saving, the following will pop up, enter the username root and click OK

.. figure:: ../../../../image/MYZR-其他/网关/GW510/测试手册4.png
   :alt: Test Manual 4
   :width: 100%

5. Being able to enter the system indicates successful SSH login via Ethernet

.. figure:: ../../../../image/MYZR-其他/网关/GW510/测试手册5.png
   :alt: Test Manual 5
   :width: 100%

Ethernet Port 1 Test
~~~~~~~~~~~

|  【Test Description】: Test by having the development board send ICMP packets to the PC
|  【Interface Identifier】: J2
|  【System Device】: /dev/eth1
|  【Test Operation】:

1. Connect the development board Ethernet port to the computer's Ethernet port using an Ethernet cable. Serial port displays:

.. code-block:: shell

   [emac_phy_link_adjust] EMAC Link Up

2. Get Ethernet Port 1 IP address, enter the command:

.. code-block:: shell

   udhcpc -i eth1

3. Output as follows:

.. code-block:: shell

   udhcpc: started, v1.37.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.128.194, server 192.168.128.1
   udhcpc: lease of 192.168.128.194 obtained from 192.168.128.1, lease time 300
   deleting routers
   adding dns 192.168.128.1

4. Verify Ethernet Port 1 network, enter the command:

.. code-block:: shell

   ping -I eth1 www.baidu.com -c 3

5. Output as follows: "0% packet loss" indicates test passed

.. code-block:: shell

   PING www.baidu.com (183.2.172.177): 56 data bytes
   64 bytes from 183.2.172.177: seq=0 ttl=54 time=6.859 ms
   64 bytes from 183.2.172.177: seq=1 ttl=54 time=6.508 ms
   64 bytes from 183.2.172.177: seq=2 ttl=54 time=6.886 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 packets received, 0% packet loss
   round-trip min/avg/max = 6.508/6.751/6.886 ms

SD Interface Test
~~~~~~~~~~~~~~

|  【Test Description】: Insert TF card.
|  【Interface Identifier】: U19
|  【System Device】: /dev/mmcblk0 mmcblk0p1
|  【Test Operation】:

1. Insert the TF card into the SD interface, the development board will output:

.. code-block:: shell

   >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] HS mode. <<

2. Enter the following command to view SD card information:

.. code-block:: shell

   fdisk -l

|  Output:

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

3. Remove the TF card, output:

.. code-block:: shell

   SDMMC0 >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] DEFS mode. <<

|  Result: The observed behavior matches expected behavior, indicating TF hot swap is working correctly.

RTC Test
~~~~~~~~~~~~~~~~

|  【Test Description】: Read and set time, check if time is correct after power cycle
|  【Interface Identifier】: CON1
|  【System Device】: /dev/rtc0
|  【Test Operation】:

1. Power on the device, check current system time, enter command:

.. code-block:: shell

   date

|  Output:

.. code-block:: shell

   Sat Jan  1 00:26:33 UTC 2000

2. Check RTC time, enter command:

.. code-block:: shell

   hwclock

|  Output:

.. code-block:: shell

   Sat Jan  1 00:26:54 2000  0.000000 seconds

3. Set system time, enter command:

.. code-block:: shell

   date -s "2026-1-29 9:30:00"

4. Write system time to RTC and check, enter command:

.. code-block:: shell

   hwclock -w
   hwclock

5. Power off, check if successfully written, enter command:

.. code-block:: shell

   hwclock

|  Output:

.. code-block:: shell

   Thu Jan 29 09:32:10 2026  0.000000 seconds

|  Result: Time matches system time and continues running, indicating successful RTC write.

RS232 Test
~~~~~~~~~~~~~~~

|  【Test Description】: Short-circuit 232_TX1,232_RX1 and 232_TX2,232_RX2 for loopback test
|  【Interface Identifier】: 232_TX1,232_RX1 232_TX2,232_RX2
|  【System Device】: /dev/ttyS4,ttyS5
|  【Test Operation】:

1. Use jumper wire to short-circuit 232_TX1 and 232_RX1
2. Enter test directory, enter command:

.. code-block:: shell

   cd /customer/app/

3. Run test program, enter command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS4 "www.myzr.com.cn"

|  Output:

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

4. Use jumper wire to short-circuit 232_TX2 and 232_RX2
5. Enter test directory, enter command:

.. code-block:: shell

   cd /customer/app/

6. Run test program, enter command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS5 "www.myzr.com.cn"

|  Output:

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
~~~~~~~~~~~~

|  【Test Description】: Use 485-USB converter to connect with computer for transmit/receive test
|  【Interface Identifier】: 485_A1,485_B1,485_A2,485_B2,485_A3,485_B3
|  【System Device】: /dev/ttyS2, /dev/ttyS6, /dev/ttyS7
|  【Test Operation】:

1. Use 485-USB converter to connect development board and computer (A to A, B to B)
2. Open corresponding serial port with Xshell, set baud rate to 115200, 8 data bits, 1 stop bit
3. Enter test directory, enter command:

.. code-block:: shell

   cd /customer/app/

4. Run test, enter command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS2 "www.myzr.com.cn"

|  Result: Output visible on 485 serial terminal

.. code-block:: shell

   www.myzr.com.cn

5. Enter 123 in 485 serial terminal (without display), can see 123 on board terminal

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

6. 485_A2,485_B2 corresponds to ttyS6, 485_A3,485_B3 corresponds to ttyS7. Test method is the same as above.

Relay Test
~~~~~~~~~~~~

|  【Test Description】: Set GPIO pins high/low to test relay activation
|  【Interface Identifier】: j8,j9
|  【System Device】:
|  【Test Operation】:

1. Enter the following command to set GPIO high/low for j8 relay activation test

.. code-block:: shell

   echo 121 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio121/direction
   echo 1 > /sys/class/gpio/gpio121/value
   echo 0 > /sys/class/gpio/gpio121/value

|  Result: Relay click sound should be heard

2. Enter the following command to set GPIO high/low for j9 relay activation test

.. code-block:: shell

   echo 122 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio122/direction
   echo 1 > /sys/class/gpio/gpio122/value
   echo 0 > /sys/class/gpio/gpio122/value

|  Result: Relay click sound should be heard

LED Test
~~~~~~~~~~~~

|  【Test Description】: Set GPIO pins high/low to test LED on/off
|  【Interface Identifier】: P3
|  【System Device】: LED
|  【Test Operation】:

1. Enter the following command to set GPIO high for middle LED on test

.. code-block:: shell

   echo 98 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio98/direction
   echo 1 > /sys/class/gpio/gpio98/value

|  Result: Middle LED on indicates normal.

2. Enter the following command to set GPIO low for middle LED off test

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio98/value

|  Result: Middle LED off indicates normal.

3. Enter the following command to set GPIO high for bottom LED on test

.. code-block:: shell

   echo 82 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio82/direction
   echo 1 > /sys/class/gpio/gpio82/value

|  Result: Bottom LED on indicates normal.

4. Enter the following command to set GPIO low for bottom LED off test

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio82/value

|  Result: Bottom LED off indicates normal.

4G Test
~~~~~~~~~~

|  【Test Description】: After 4G connection successful, development board sends ICMP packets to external network to verify connection
|  【Interface Identifier】: U38
|  【System Device】: /dev/ttyUSB1, usb0
|  【Test Operation】:

1. Connect 4G antenna to "U3" interface, insert SIM card into "J3" slot
2. Set 4G_PWRKEY1 pin high to power on 4G, enter commands:

.. code-block:: shell

   echo 98 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio98/direction
   echo 1 > /sys/class/gpio/gpio98/value
   echo 64 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio64/direction
   echo 1 > /sys/class/gpio/gpio64/value

3. Enter the following command to start 4G

.. code-block:: shell

   echo -e "AT+QNETDEVCTL=3,1,1\r\n" > /dev/ttyUSB1

4. Enter the following command to check if 4G started successfully

.. code-block:: shell

   lsusb

|  Output as follows. "Quectel EC801E-CN" indicates success. Wait 1 minute if not present:

.. code-block:: shell

   Bus 001 Device 001: ID 1d6b:0002 Linux 6.1.111-rt42 ehci_hcd EHCI Host Controller
   Bus 001 Device 003: ID 0bda:d723 Realtek 802.11n WLAN Adapter
   Bus 001 Device 002: ID 1a40:0101 USB 2.0 Hub
   Bus 001 Device 005: ID 2c7c:0903 Quectel EC801E-CN

5. Enter the following command to get IP

.. code-block:: shell

   udhcpc -i usb0

|  Output as follows:

.. code-block:: shell

   udhcpc: started, v1.37.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.43.100, server 192.168.43.1
   udhcpc: lease of 192.168.43.100 obtained from 192.168.43.1, lease time 86400
   deleting routers
   adding dns 192.168.43.2
   adding dns 192.168.43.3

6. Enter the following command to verify 4G:

.. code-block:: shell

   ping -I usb0 www.baidu.com -c 3

|  Output as follows: "0% packet loss" indicates test passed

.. code-block:: shell

   PING www.baidu.com (183.240.99.224): 56 data bytes
   64 bytes from 183.240.99.224: seq=0 ttl=51 time=56.363 ms
   64 bytes from 183.240.99.224: seq=1 ttl=51 time=56.105 ms
   64 bytes from 183.240.99.224: seq=2 ttl=51 time=55.599 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 packets received, 0% packet loss
   round-trip min/avg/max = 55.599/56.022/56.363 ms

WiFi STA Test
~~~~~~~~~~~~~~

|  【Test Description】: After WiFi connection successful, development board sends ICMP packets to external network to verify connection
|  【Interface Identifier】: U41
|  【System Device】: wlan0
|  【Test Operation】:

1. Connect WiFi antenna to "U40" interface
2. Generate WPA PSK file for SSID. MY-WIFI My202412 are WiFi name and password, enter commands:

.. code-block:: shell

   wpa_passphrase MY-WIFI My202412 > /etc/wpa_supplicant.conf
   wpa_passphrase MYZR-WiFi-5G Myzr2012 > /etc/wpa_supplicant.conf

4. Connect, enter command:

.. code-block:: shell

   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

5. Output:

.. code-block:: shell

   Successfully initialized wpa_supplicant
   nl80211: kernel reports: Authentication algorithm number required
   [  266.744713] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready

6. Get IP, enter command:

.. code-block:: shell

   udhcpc -i wlan0

|  Output:

.. code-block:: shell

   udhcpc: started, v1.36.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.43.35, server 192.
   udhcpc: lease of 192.168.43.35 obtained from 192.168.43.1, lease time 3600
   deleting routers
   adding dns 192.168.43.1

7. Test connection, enter command:

.. code-block:: shell

   ping -I wlan0 www.baidu.com -c 3

|  Output: Result: "0% packet loss" indicates WiFi connection normal

.. code-block:: shell

   PING www.baidu.com (183.2.172.177) from 192.168.61.73 wlan0: 56(84) bytes of data.
   64 bytes from 183.2.172.177: icmp_seq=1 ttl=54 time=10.0 ms
   64 bytes from 183.2.172.177: icmp_seq=2 ttl=54 time=13.2 ms
   64 bytes from 183.2.172.177: icmp_seq=3 ttl=54 time=14.5 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 10.031/12.576/14.482/1.872 ms

Bluetooth
~~~~~~~

|  【Test Description】: After gateway connection successful, gateway and node transmit/receive to verify connection
|  【Interface Identifier】: U53
|  【System Device】: /dev/ttyS3
|  【Test Operation】:

**Connect two development boards. One Bluetooth module as G(mesh) gateway, one as N(mesh) node**

1. Both terminals enter test application directory, enter command:

.. code-block:: shell

   cd /customer/app

2. Enter the following command on gateway terminal

.. code-block:: shell

   ./wg

|  Output as follows indicates gateway connected to node

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

3. Enter the following command on node terminal to put node in receive mode

.. code-block:: shell

   ./serial_test.out /dev/ttyS1 1

4. Enter the following command on gateway terminal to send 12345 to node

.. code-block:: shell

   ./n0x002

|  Node terminal can receive 12345 as follows

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

5. Enter the following command on gateway terminal to put gateway in receive mode

.. code-block:: shell

   ./serial_test.out /dev/ttyS1 1

6. Enter the following command on node terminal to send 12345 to gateway

.. code-block:: shell

   ./a

|  Gateway terminal can receive 12345 as follows

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

7. If using module for node, use serial port software with following configuration

.. figure:: ../../../../image/MYZR-其他/网关/GW510/测试手册6.png
   :alt: Test Manual 6
   :width: 100%

|  When gateway runs ./n0x002, this page receives 07 00 93 00 31 32 33 34 35
|  When sending from node to gateway, configure this page and click send 00 ff 00 01 31 32 33 34 35 36. Before sending, run ./serial_test.out /dev/ttyS1 1 on gateway terminal to put gateway in receive mode to receive 12345 from node

LoRa Test
~~~~~~~~~~~~~~~

|  【Test Description】: Open two development terminals for transmit/receive verification
|  【Interface Identifier】: U51
|  【System Device】: /dev/ttyS3
|  【Test Operation】:

1. Connect antenna to "U51" interface
2. Enter test directory, enter command:

.. code-block:: shell

   cd /customer/app/

3. Configure working mode (M0=1, M1=0), enter commands (both terminals):

.. code-block:: shell

   echo 96 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio96/direction
   echo 1 > /sys/class/gpio/gpio96/value
   echo 97 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio97/direction
   echo 0 > /sys/class/gpio/gpio97/value

4. On terminal 2, enter command:

.. code-block:: shell

   ./lora /dev/ttyS1 12345

5. Output:

.. code-block:: shell

   Sent: 12345
   Entering receive mode...

6. On terminal 1, enter command:

.. code-block:: shell

   ./lora /dev/ttyS1 12345

7. Observe terminal 2, receive output:

.. code-block:: shell

   Sent: 12345
   Entering receive mode...
   Received: 123456

8. Stop receive on terminal 2, send to terminal 1, enter command:

.. code-block:: shell

   ^C（CTRL C to stop receive）
   ./lora /dev/ttyS3 12345

9. Observe terminal 1, receive output:

.. code-block:: shell

   Sent: 123456
   Entering receive mode...
   Received: 12345

DO Test
~~~~~~~~~~~~~~

|  【Test Description】: Verify output function
|  【Interface Identifier】: OUT0+,OUT0-
|  【System Device】:
|  【Test Operation】:

1. DO test wiring diagram

.. figure:: ../../../../image/MYZR-其他/网关/GW510/测试手册7.png
   :alt: Test Manual 7
   :width: 100%

|  Note: Set voltage to 3.3V, current to 0.1A, overcurrent protection to 0.12A.

2. Connect OUT+ pin to 3.3V power, measure OUT- pin with oscilloscope or multimeter. OUT- defaults to low level. After OUT+ connected to 3.3V, OUT- is 3V-3.3V. Can also check pin status with following command.
3. Enter the following command for high level test

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   echo 1 > /sys/class/gpio/gpio126/value

|  At this point, measure OUT- pin with oscilloscope or multimeter, OUT- should be 3V-3.3V
|  Can also check pin status with following command.

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   cat /sys/class/gpio/gpio126/value

|  Output is 1

4. Enter the following command for low level test

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   echo 0 > /sys/class/gpio/gpio126/value

|  At this point, measure OUT- pin with oscilloscope or multimeter, OUT- should be 0V
|  Can also check pin status with following command.

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   cat /sys/class/gpio/gpio126/value

|  Output is 0

DI Test
~~~~~~~~~~~~~~~

|  【Test Description】: Verify input function
|  【Interface Identifier】: IN0+,IN0-
|  【System Device】:
|  【Test Operation】:

1. DI test wiring diagram

.. figure:: ../../../../image/MYZR-其他/网关/GW510/测试手册8.png
   :alt: Test Manual 8
   :width: 100%

2. Connect IN0+ pin to 3.3V power, IN0- pin to ground.

|  Note: Set voltage to 3.3V, current to 0.1A, overcurrent protection to 0.12A.

3. When IN0+ connected to 3.3V but not enabled, read level is 1.

.. code-block:: shell

   echo 125 > /sys/class/gpio/export
   echo in > /sys/class/gpio/gpio125/direction
   cat /sys/class/gpio/gpio125/value

|  Test Result: Display 1 indicates success

.. code-block:: shell

   root@myzr:~# cat /sys/class/gpio/gpio125/value
   1

|  When IN0+ connected to 3.3V and IN0- grounded and enabled, read level is 0.

.. code-block:: shell

   echo 125 > /sys/class/gpio/export
   echo in > /sys/class/gpio/gpio125/direction
   cat /sys/class/gpio/gpio125/value

|  Test Result: Display 0 indicates failure

.. code-block:: shell

   root@myzr:~# cat /sys/class/gpio/gpio125/value
   0

RS485 to MQTT Transparent Transmission Example
~~~~~~~~~~~~~~~~~~~~~

1. Objective
***********

|  Convert RS485 electricity meter (dds1079) data to MQTT messages through gateway and report to MQTT server. Users can view meter data on MQTT client on computer.
|  Involved devices:

  - Gateway development board (built-in RS485 and Ethernet interfaces, running gateway program)
  - RS485 electricity meter dds1079 (or equivalent device)
  - Client computer (for web configuration + MQTT client)
  - MQTT server (can be public broker.emqx.io or customer-built)


2. Device Connection
*****************

|  RS485 Connection

1. Prepare an RS485 communication cable (A/B two cores or differential cable).
2. Connect RS485 terminal blocks to gateway RS485 interface:

  - Meter A ↔ Gateway A2
  - Meter B ↔ Gateway B2
  - Meter GND ↔ Gateway GND

3. Confirm meter and gateway are powered on:

  - Meter display/indicator normal;
  - Gateway power indicator, RUN indicator normal.

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例1.png
   :alt: RS485 MQTT Example 1


3. Ethernet Connection
*******************

|  ETH1 -- WAN: DHCP
|  BR0 -- LAN: 192.168.9.1
|  BR0 (ETH2, WLAN0, WLAN1)

1. Connect host and development board via Ethernet cable, use static IP 192.168.137.81 to access homepage and find MAC address.

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例2.png
   :alt: RS485 MQTT Example 2


|  MAC address here is C6:72:27:3C:73:E1

2. Enter host cmd terminal, run arp -a | find /i "c6-72-27-3c-73-e1"

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例3.png
   :alt: RS485 MQTT Example 3


3. Enter web page via command terminal

4. Web Configuration
********************

|  Enter left-side configuration editor. Current interface can modify configuration files. Device is the device, UART is serial port, MQTT is server. They are connected via object/interface.

Device List Configuration
+++++++++++++

Parameter Description
##########

- **interface (Interface Name)**

  - Meaning: Unique identifier for this collection task.
  - Description: Suggest setting to device model or installation location (e.g., dds1079) for easy differentiation in logs and data platforms.

- **status (Enabled Status)**

  - Meaning: Switch for this task.
  - Description: Set to enabled to start collection immediately; set to disabled to temporarily stop.

- **command (Collection Command)**

  - Meaning: Raw command message sent to physical device.
  - Description: Usually in hexadecimal format (Hex). For example, a Modbus or DL/T 645 protocol command to read meter data.

- **period (Collection Period)**

  - Meaning: Time interval between collections.
  - Description: Unit is milliseconds. For example, 1000 means send command to device every 1 second.

- **action (Processing Action)**

  - Meaning: Processing method after receiving device response data.
  - Description: Commonly forward (forward), meaning forward collected raw data directly to server or cloud platform.

- **object (Physical Port)**

  - Meaning: Which hardware interface to send command through.
  - Description: For example, uart2 represents the 2nd serial port on development board (usually corresponds to RS485 interface on board).

- **format (Data Format)**

  - Meaning: Data encoding format used in communication.
  - Description: hex represents hexadecimal (most common for industrial devices); can also be configured as string or json as needed.

**Example:**

|  This example follows the configuration in the figure

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例4.png
   :alt: RS485 MQTT Example 4


Serial Port List Configuration
+++++++++++++++++

Parameter Description
##########

- **interface (Interface Name)**

  - Meaning: Internal identifier for this serial port configuration.
  - Description: Usually named uart1, uart2, etc., used to reference this serial port in other configurations.

- **status (Enabled Status)**

  - Meaning: Whether to activate this serial port.
  - Description: enabled to enable, disabled to disable. Suggest disabling unused serial ports to save resources.

- **device (Device Path)**

  - Meaning: Physical address of hardware serial port in Linux system.
  - Description: For example /dev/ttyS1. This directly corresponds to a physical terminal on development board, usually no modification needed.

- **baud_rate (Baud Rate)**

  - Meaning: Serial communication transmission rate.
  - Description: Must match connected external device. Common values: 9600, 115200, etc.

- **data_bits / stop_bits / parity (Data Bits/Stop Bits/Parity)**

  - Meaning: Basic low-level protocol parameters for serial communication.
  - Description: Industrial standard is usually 8 data bits, 1 stop bit, none parity. Must match external device manual.

- **flow_control (Flow Control)**

  - Meaning: Data transmission flow control method.
  - Description: Usually set to none. Not recommended unless device explicitly requires hardware or software flow control.

- **udelay (Microsecond Delay)**

  - Meaning: Forced wait time after serial read/write operations.
  - Description: Unit is microseconds. Used for older industrial devices with slow response, usually set to 0.

- **action / object (Processing Action/Forward Object)**

  - Meaning: Where data goes after serial port receives it.
  - Description: For example, action is forward, object is server1, meaning all raw data received by serial port will be immediately forwarded to configured server.

- **format (Data Format)**

  - Meaning: Data representation format.
  - Description: string represents text string format, hex represents hexadecimal raw bytes.

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例5.png
   :alt: RS485 MQTT Example 5


**Example**

|  This example uses uart2 interface with device path ttyS6 as shown

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例6.png
   :alt: RS485 MQTT Example 6


MQTT List Configuration
++++++++++++++++

Parameter Description
###############

- **interface (Interface Name)**

  - Meaning: Unique identifier for this MQTT connection.
  - Description: Used to differentiate different cloud platform connections (e.g., mqtt1, mqtt2).

- **status (Enabled Status)**

  - Meaning: Whether to enable this MQTT connection.
  - Description: Set to enabled, development board will try to connect to cloud server.

- **serverURL (Server Address)**

  - Meaning: Domain name or IP address of MQTT server (Broker).
  - Description: For example broker.emqx.io. This is the destination for data reporting.

- **clientId (Client ID)**

  - Meaning: Development board's "ID card" in the cloud.
  - Description: Must be unique on the same server, usually used by cloud platform to identify specific gateway device.

- **username / password (Username / Password)**

  - Meaning: Authentication credentials for connecting to cloud platform.
  - Description: If server has security authentication enabled, fill in correct username and password.

- **topic_sub (Subscribe Topic)**

  - Meaning: Which channel the development board "listens" to.
  - Description: Development board will monitor this topic to receive remote control commands from cloud.

- **topic_pub (Publish Topic)**

  - Meaning: Which channel the development board "speaks" on.
  - Description: All data collected by development board will be published to cloud through this topic.

- **payload (Test Payload)**

  - Meaning: Default send content.
  - Description: Usually used for heartbeat packets or testing connection.

- **qos (Quality of Service)**

  - Meaning: Message transmission reliability level.
  - Description: Options: 0 (at most once), 1 (at least once), 2 (exactly once). Industrial scenarios recommend 1.

- **timeout (Timeout)**

  - Meaning: Network response waiting time.
  - Description: Unit is milliseconds. Can increase in poor network conditions.

- **action / object / format (Processing Action / Forward Object / Data Format)**

  - Meaning: Where cloud commands go after being sent down.
  - Description: For example, action is forward, object is uart2, format is hex. This means: MQTT messages sent from cloud will be automatically converted to hexadecimal and sent from RS485 serial port to field devices.

**Example**

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例7.png
   :alt: RS485 MQTT Example 7


**After modifying these three lists, web configuration for this example is complete. Next, configure serial port debugging tool**

5. Computer
**************

|  Enter serial port debugging tool

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例8.png
   :alt: RS485 MQTT Example 8


|  Default interface as shown:

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例9.png
   :alt: RS485 MQTT Example 9


|  Click top-left icon -> Tools -> Auto Response Control, open right toolbar and click Auto Response

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例10.png
   :alt: RS485 MQTT Example 10


|  Right-click on right blank area -> Import
|  Import meter configuration.cfg into Auto Response

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例11.png
   :alt: RS485 MQTT Example 11


|  After import as shown:

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例12.png
   :alt: RS485 MQTT Example 12


|  Then start Auto Response

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例13.png
   :alt: RS485 MQTT Example 13


|  Serial Port Settings
   This example uses serial port settings as shown on left:

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例14.png
   :alt: RS485 MQTT Example 14


.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例15.png
   :alt: RS485 MQTT Example 15


|  After setting, click Start and set both receive and send to hex

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例16.png
   :alt: RS485 MQTT Example 16


|  Complete configuration and open serial port
|  Then data log will have output indicating successful startup:

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例17.png
   :alt: RS485 MQTT Example 17


|  Serial port debugging assistant configuration complete

**MQTT Client Configuration**

|  Install MQTT client tool on computer (recommend MQTTX or mosquitto_sub).
|  Click top-left to add connection

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例18.png
   :alt: RS485 MQTT Example 18


|  Use MQTT server info consistent with serverURL in gateway to establish connection:

  - Server Address: e.g., broker.emqx.io or customer-built IP
  - Port: 1883 (unless specified otherwise)
  - username/password: default can be admin and public
  - Client ID: must not match clientid in configuration file, otherwise development board clientid will be kicked off

|  Click connect at top-right
|  Can refer to mqtt list in configuration editor for configuration.

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例19.png
   :alt: RS485 MQTT Example 19


.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例20.png
   :alt: RS485 MQTT Example 20


|  After connection, click Add Subscription, can refer to topic in configuration file.
|  This example:

|  If you want to see gateway uploaded data (meter readings)
|  Fill in MQTTX Topic field: emqx/my_gw/shsadl_645_ack

|  If you want to see commands received by gateway
|  Fill in MQTTX Topic field: emqx/my_gw/shsadl_645_req

|  Fill according to previously completed mqtt list configuration

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例21.png
   :alt: RS485 MQTT Example 21


|  Recommended method (full wildcard)
|  If you want to see both types of data, fill: emqx/my_gw/#

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例22.png
   :alt: RS485 MQTT Example 22


.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例23.png
   :alt: RS485 MQTT Example 23


|  After subscription, MQTT subscription configuration complete, meter data will pop up as shown.

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例24.png
   :alt: RS485 MQTT Example 24


|  Note: Development board will automatically run miot program after startup.

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例25.png
   :alt: RS485 MQTT Example 25


|  If you want to stop
|  Enter root to login, then enter /etc/init.d/S99miot stop

.. figure:: ../../../../image/MYZR-其他/网关/GW510/RS485与MQTT透传示例26.png
   :alt: RS485 MQTT Example 26

Development Board Test Guide
------------------

Note: The following is for ubifs version system

UART Test
~~~~~~~~~~~~

**UART1 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS1
   #Test description: Short J4:9(OUTP_RX0_CH0_FUART1_RX) and J4:10(OUTN_RX0_CH0_FUART1_TX) pins.
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS1 "www.myzr.com.cn"
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

**UART2 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS2
   #Test description: Short J4:7(OUTP_RX0_CH2_FUART2_RX) and J19:8(OUTN_RX0_CH2_FUART2_TX) pins.
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS2 "www.myzr.com.cn"
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

**UART3 Configuration and Test**

.. code-block:: shell

   #Configuration (disabled by default, configured as MIPI interface. To use, need to enable configuration)
   $ vim arch/arm/boot/dts/pcupid-ssm001c-s01a-voip-padmux.dtsi

   #Add (need to mask other pin configurations for PAD_OUTP_CH0 and PAD_OUTN_CH0)
   //UART3 Mode2
   <PAD_OUTP_CH0  MDRV_PUSE_UART3_TX>,
   <PAD_OUTN_CH0  MDRV_PUSE_UART3_RX>,

   #Device interface: /dev/ttyS3
   #Test description: Short J19:5(OUTP_TX0_CH0_MIPITX_D0P) and J19:6(OUTN_TX0_CH0_MIPITX_D0N) pins.
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS3 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x2e    Character: .
   ASCII: 0x6d    Character: m
   ASCII: 0x79    Character: y
   ASCII: 0x7a    Character: z
   ASCII: 0x72    Character: r
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6f    Character: o
   ASCII: 0x6d    Character: m
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6e    Character: n
   ASCII: 0x0     Character:

**UART4 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS1
   #Test description: Short J4:9(OUTP_RX0_CH0_FUART1_RX) and J4:10(OUTN_RX0_CH0_FUART1_TX) pins.
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS1 "www.myzr.com.cn"
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

**UART5 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS5
   #Test description: Short J18:1(GPIOE_07_UART5_TX) and J18:2(GPIOE_06_UART5_RX) pins.
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS5 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x2e    Character: .
   ASCII: 0x6d    Character: m
   ASCII: 0x79    Character: y
   ASCII: 0x7a    Character: z
   ASCII: 0x72    Character: r
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6f    Character: o
   ASCII: 0x6d    Character: m
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6e    Character: n
   ASCII: 0x0     Character:

**UART6 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS6
   #Test description: Short J4:35(UART0_TX) and J4:38(UART0_RX) pins.
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS6 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x2e    Character: .
   ASCII: 0x6d    Character: m
   ASCII: 0x79    Character: y
   ASCII: 0x7a    Character: z
   ASCII: 0x72    Character: r
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6f    Character: o
   ASCII: 0x6d    Character: m
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6e    Character: n
   ASCII: 0x0     Character:

**UART7 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS7
   #Test description: Short J4:37(ADC_PWM_OUT01_UART7_TX) and J4:40(ADC_PWM_OUT00_UART7_RX) pins.
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS7 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x2e    Character: .
   ASCII: 0x6d    Character: m
   ASCII: 0x79    Character: y
   ASCII: 0x7a    Character: z
   ASCII: 0x72    Character: r
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6f    Character: o
   ASCII: 0x6d    Character: m
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6e    Character: n
   ASCII: 0x0     Character:

I2C2 Configuration and Test
-----------
.. code-block:: shell

   #1.i2ctool test
   #Device interface: /dev/i2c2
   #Test description: Connect the hym8563 module to pin J19:11(GPIOE_10_I2C2_SDA) and pin J19:13(GPIOE_09_I2C2_SCL), plus power and ground. i2c2 is connected to the hym8563 RTC clock module, 0x51 is the hym8563 device address. If the module is not present, an error will be reported. Normal output is as follows:
   $ cd /customer/app/
   $ ./i2cdump -f -y 2 0x51
   
   #Output:
   No size specified (using byte-data access)
       0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
   00: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   10: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   20: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   30: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   40: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   50: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   60: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   70: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   80: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   90: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   a0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   b0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   c0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   d0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   e0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   f0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   
   #2.Test hym8563 real-time clock
   #Device interface: /dev/rtc1
   #Test description: Detect and set the clock
   $ dmesg | grep rtc
   
   #Output:
   sstar,rtcpwc 1f006800.rtcpwc: registered as rtc0
   sstar,rtcpwc 1f006800.rtcpwc: setting system clock to 1970-01-01T04:41:54 UTC
   (16914)
   input: rtcpwc as /devices/soc0/soc/1f006800.rtcpwc/input/input0
   rtc-hym8563 2-0051: registered as rtc1
   
   #Test hym8563 clock
   #a.Set system clock to 2025-03-01 12:34:19
   $ date
   Thu Jan  1 04:59:47 UTC 1970
   $ date -s "2025-03-01 12:34:19"
   Sat Mar  1 12:34:19 UTC 2025
   
   #b.Write system clock to hardware clock
   $ hwclock -w -f /dev/rtc1
   
   #c.Read hardware clock to verify correctness
   $ hwclock -r -f /dev/rtc1
   Sat Mar  1 12:35:07 2025  0.000000 seconds

SPI0 Configuration and Test
-----------
.. code-block:: shell

   #Device interface: /dev/spidev0.0
   #Test description: Short pin J18:16(GPIOA_15_MSPI0_MISO) and pin J18:17(GPIOA_14_MSPI0_MOSI).
   $ cd /customer/app/
   $ /customer/tools # ./spidev_test.out -D /dev/spidev0.0
   
   #Output
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
   
   #Note: If not shorted, the following output is shown:
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
PWM Configuration and Test
-----------
**Interface Silkscreen**: PM_PWM0_OUT, PM_PWM1_OUT, EMMC_D4, EMMC_D5, EMMC_D6

.. code-block:: shell

   #Device interface: # PAD_PM_PWM0_OUT: corresponds to device node /sys/class/sstar/pwm/pwm18
   # PAD_PM_PWM1_OUT: corresponds to device node /sys/class/sstar/pwm/pwm19
   # PAD_EMMC_D4: corresponds to device node /sys/class/sstar/pwm/group3/pwm14
   # PAD_EMMC_D5: corresponds to device node /sys/class/sstar/pwm/group3/pwm15
   # PAD_EMMC_D6: corresponds to device node /sys/class/sstar/pwm/group3/pwm16
   #Test description: Check with an oscilloscope. Take J18:7(EMMC_D4_PWM_OUT[14]) as an example, output 100Hz, 50% duty cycle, normal polarity waveform
   $ cd /sys/class/sstar/pwm/group3/pwm14
   $ echo 1000000  > period
   $ echo 500000   > duty
   $ echo normal   > polarity
   $ echo 1        > enable
GPIO Configuration and Test
-----------
**Interface Silkscreen**: EMMC_CMD, EMMC_D5, EMMC_D3, EMMC_D0, EMMC_D1

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;  /* Header centered */
   }
     td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;  /* First row content centered */
   }

   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Unified width */
       border-collapse: collapse;
       table-layout: auto;  /* Column width auto-distributed */
   }
   td {
       word-wrap: break-word;  /* Auto-wrap long content */
   }
   </style>


=============  ===========  =============  ===========  =============  ===========
Pad Name       GPIO Index   Pad Name       GPIO Index   Pad Name       GPIO Index
=============  ===========  =============  ===========  =============  ===========
PAD_EMMC_CMD   52           PAD_EMMC_D5    57           PAD_EMMC_D3    54
PAD_EMMC_D0    56           PAD_EMMC_D1    58
=============  ===========  =============  ===========  =============  ===========
.. code-block:: shell

   #Device interface: /sys/class/gpio
   #Test description: Take J18:10(EMMC_D1_GPIO) as an example
   #Set high and low level
   $ echo 68 > /sys/class/gpio/export
   $ echo out > /sys/class/gpio/gpio58/direction
   $ echo 1 > /sys/class/gpio/gpio58/value
   $ echo 0 > /sys/class/gpio/gpio58/value
   
   #Read pin level
   $ echo in > /sys/class/gpio/gpio58/direction
   $ cat /sys/class/gpio/gpio58/value
TF Card Test
-----------
**Interface Silkscreen**: J12

.. code-block:: shell

   #Device interface: /dev/mmcblk0
   #Test description: Insert TF card
   #Prompt message as follows:
   SDMMC0 >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] HS mode. <<
   
   #Check partitions:
   $ ls /dev/mmcblk0*
   
   #Output:
   /dev/mmcblk0   /dev/mmcblk0p1   /dev/mmcblk0p2
   
   #Mount
   $ mount  /dev/mmcblk0p1  /mnt/
   $ ls /mnt/
   imx6ul~1.dtb   imx6ul~3.dtb    imx6ul~5.dtb    imx6ul~7.dtb    zimage
   imx6ul~2.dtb   imx6ul~4.dtb    imx6ul~6.dtb    system~1
   
   #Unmount
   $ umount /mnt/
USB Flash Drive Test
-----------
**Interface Silkscreen**: J16

.. code-block:: shell

   #Device interface: /dev/sd*
   #Test description: Insert USB flash drive
   $ dmesg | grep sd
   
   #Prompt message as follows:
   sd 0:0:0:0: [sda] 61440000 512-byte logical blocks: (31.5 GB/29.3 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
   sd 0:0:0:0: [sda] No Caching mode page found
   sd 0:0:0:0: [sda] Assuming drive cache: write through
   sda: sda1
   sd 0:0:0:0: [sda] Attached SCSI removable disk
   
   #Check partitions:
   $ ls /dev/sd*
   
   #Output:
   /dev/sda   /dev/sda1
   
   #Mount
   $ mount /dev/sda1 /mnt/
   $ ls /mnt/
   imx6ul~1.dtb  imx6ul~3.dtb  imx6ul~5.dtb  imx6ul~7.dtb  zimage
   imx6ul~2.dtb  imx6ul~4.dtb  imx6ul~6.dtb  system~1
   
   #Unmount
   $ umount /mnt/
Ethernet Test
-----------
**Interface Silkscreen**: CONR1

.. code-block:: shell

   #Device interface: /dev/eth0
   #Test description: Set computer IP to 192.168.137.99, set board IP to 192.168.137.81, test via ping
   $ ifconfig eth0 192.168.137.81
   
   #Output:
   [emac_phy_link_adjust] EMAC Link Down
   [emac_phy_link_adjust] EMAC Link Up
   
   #Test: If no packet loss, it is normal.
   $ ping 192.168.137.99 -c 2 -w 4
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=64 time=0.537 ms
   64 bytes from 192.168.137.99: seq=1 ttl=64 time=0.276 ms
   
   --- 192.168.137.99 ping statistics --
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.276/0.406/0.537 ms
WIFI STA Test
-----------
**Interface Silkscreen**: U12

.. code-block:: shell

   [Test Description]: After WIFI connects to the AP, the development board sends ICMP packets to the external network to verify the connection is normal.
   [Interface Label]: WIFI&BT
   [System Device]: wlan0
   [Interface Silkscreen]: U12
   
   Test Operations
   Connect the antenna to the "U12" interface
   Generate WPA PSK file for SSID
   
   1.Set the WIFI SSID username and password
   wpa_passphrase command format: wpa_passphrase + wifi name + wifi password > /etc/wpa_supplicant.conf
   
   =====> Input:
   wpa_passphrase MYZR-WIFI-2.4G myzr2012 > /etc/wpa_supplicant.conf
   
   2.Connect:
   =====> Input:
   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
   
   =====> Output:
   Successfully initialized wpa_supplicant
   nl80211: kernel reports: Match already configured
   rfkill: Cannot open RFKILL control device
   ......
   
   3.Obtain IP:
   =====> Input:
   $ udhcpc -i wlan0=====> Output:
   udhcpc: started, v1.37.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.43.74, server 192.168.43.1
   udhcpc: lease of 192.168.43.74 obtained from 192.168.43.1, lease time 3600
   deleting routers
   adding dns 192.168.43.1
   
   4.Test connection
   =====> Input:
   $ ping -I wlan0 www.baidu.com
   
   =====> Output:
   [   39.924248] RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 SeqNum = 40
   PING www.baidu.com (163.177.151.109): 56 data bytes
   [   40.813870] RTW: OnAction_back
   [   40.816968] RTW: OnAction_back, action=0[   40.821089] RTW: Drop duplicate management frame with seq_num = 668.
   64 bytes from 163.177.151.109: seq=0 ttl=56 time=233.235 ms
   [   40.832117] RTW: issue_addba_rsp_wait_ack(wlan0) ra=40:77:a9:64:76:b2 status:=0 tid=4 size:64, acked, 1/3 in 12 ms
   64 bytes from 163.177.151.109: seq=1 ttl=56 time=22.882 ms
   64 bytes from 163.177.151.109: seq=2 ttl=56 time=8.862 ms
   64 bytes from 163.177.151.109: seq=3 ttl=56 time=9.219 ms
   64 bytes from 163.177.151.109: seq=4 ttl=56 time=7.952 ms
   64 bytes from 163.177.151.109: seq=5 ttl=56 time=400.328 ms
   64 bytes from 163.177.151.109: seq=6 ttl=56 time=11.634 ms
   ^C
   --- www.baidu.com ping statistics ---
   22 packets transmitted, 22 packets received, 0% packet loss
   round-trip min/avg/max = 17.336/38.637/123.220 ms
   "0% packet loss" indicates the WIFI connection is normal
WIFI AP Test
-----------
.. code-block:: shell

   [Test Description]: After WIFI connects to the AP, the development board sends ICMP packets to the external network to verify the connection is normal.
   [Interface Label]: WIFI&BT
   [System Device]: wlan0
   [Interface Silkscreen]: U12
   
   Test Operations
   Connect the antenna to the "U12" interface
   Generate WPA PSK file for SSID
   
   1.Create hotspot
   $ Change ssid in /etc/hostapd.conf to MYZR-SSD2351-EK112 and interface to wlan1
   $ ifconfig wlan1 192.168.8.1
   $ hostapd -B /etc/hostapd.conf
   $ dnsmasq --interface=wlan1 --dhcp-range=192.168.8.2,192.168.8.100,24h
   #Mobile phone can detect MYZR-SSD2351-EK112
   
   2.Enable IP forwarding and NAT
   $ echo 1 > /proc/sys/net/ipv4/ip_forward
   $ iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
Bluetooth Test
-----------
.. code-block:: shell

   [Test Description]: After scanning for Bluetooth devices, send L2CAP echo requests and receive responses
   [Interface Label]: WIFI&BT
   [System Device]: hci0
   [Interface Silkscreen]: U12
   
   Test Operations
   Connect the antenna to the "U12" interface
   
   1.Enable Bluetooth:
   =====> Input:
   $ hciconfig hci0 up
   $ hciconfig=====> Output:
   hci0:   Type: Primary  Bus: UART
       BD Address: B0:F1:EC:A7:E8:03  ACL MTU: 1021:8  SCO MTU: 64:1
       UP RUNNING
       RX bytes:1266 acl:0 sco:0 events:66 errors:0
       TX bytes:1138 acl:0 sco:0 commands:66 errors:0
       
   2.Scan for external Bluetooth devices:
   =====> Input:
   $ hcitool scan=====> Output:
   Scanning ...
       88:46:04:4C:11:A7   Redmi K40
   
   3.Send L2CAP packet test:
   =====> Input:
   $ l2ping 88:46:04:4C:11:A7
   
   =====> Output:
   Ping: 88:46:04:4C:11:A7 from B0:F1:EC:A7:E8:03 (data size 44) ...
   44 bytes from 88:46:04:4C:11:A7 id 0 time 44.84ms
   44 bytes from 88:46:04:4C:11:A7 id 1 time 28.58ms
   44 bytes from 88:46:04:4C:11:A7 id 2 time 46.05ms
   44 bytes from 88:46:04:4C:11:A7 id 3 time 44.86ms
   44 bytes from 88:46:04:4C:11:A7 id 4 time 44.67ms
   ^C8 sent, 8 received, 0% loss
   "0% packet loss" indicates the Bluetooth connection is normal.
   
   4.Bluetooth connection can use the bluetoothctl command
   #Enter terminal;
   [bluetooth]#
   [bluetooth]# show //Check if controller Power is yes. If Power is no, run power on
   [bluetooth]# power on
   [bluetooth]# agent NoInputNoOutput //Other IO caps can be set, such as KeyboardDisplay
   [bluetooth]# default-agent
   [bluetooth]# scan on //After scanning for the corresponding device, use scan off to stop scanning.
   [bluetooth]# pair 00:22:48:DC:89:0F //Pair with remote device.
   [bluetooth]# connect 00:22:48:DC:89:0F //Connect to remote device
MIC Test
-----------
.. code-block:: shell

   #prog_audio_ai_ao_demo is in the SDK
   #MIC0 recording test
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic1.wav -A 0 -D 0 -R 8000 -C 1 -T 10 -V 60
   #MIC1 recording test
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60
   #MIC2 recording test
   ./prog_audio_ai_ao_demo capture -i adc_b -F test_amic3.wav -A 0 -D 0 -R 8000 -C 1 -T 10 -V 60
