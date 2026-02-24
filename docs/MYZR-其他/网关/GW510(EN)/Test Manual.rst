Test Manual
=============

Ethernet Port 0 Test
----------------------

1. Connect the host PC to Ethernet port 1 of the development board using an Ethernet cable, and set the host IP address to the same subnet as the gateway, e.g., 192.168.131.99

.. figure:: /image/MYZR-其他/网关/GW510/测试手册1.png
   :alt: 测试手册1.png
   :width: 60%

2. Open a serial terminal such as Xshell, enter the default gateway IP address 192.168.131.81, select SSH protocol, and click Connect.

.. figure:: /image/MYZR-其他/网关/GW510/测试手册2.png
   :alt: 测试手册2.png
   :width: 60%

3. After a successful connection, the following message will pop up to receive the host key; click **Receive & Save**.

.. figure:: /image/MYZR-其他/网关/GW510/测试手册3.png
   :alt: 测试手册3.png
   :width: 60%

4. After saving, the following dialog will appear; enter username `root` and click OK.

.. figure:: /image/MYZR-其他/网关/GW510/测试手册4.png
   :alt: 测试手册4.png
   :width: 60%

5. Being able to log into the system indicates successful SSH login via Ethernet.

.. figure:: /image/MYZR-其他/网关/GW510/测试手册5.png
   :alt: 测试手册5.png
   :width: 60%

Ethernet Port 1 Test
----------------------

|  **Test Description**: Test by sending ICMP packets from the development board to the PC
|  **Interface Label**: J2
|  **System Device**: /dev/eth1
|  **Test Procedure**:

1. Connect the Ethernet port of the development board to the PC using an Ethernet cable. Serial output:

.. code-block:: shell

   [emac_phy_link_adjust] EMAC Link Up

2. Obtain the IP address for Ethernet port 1 using the following command:

.. code-block:: shell

   udhcpc -i eth1

3. Example output:

.. code-block:: shell

   udhcpc: started, v1.37.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.128.194, server 192.168.128.1
   udhcpc: lease of 192.168.128.194 obtained from 192.168.128.1, lease time 300
   deleting routers
   adding dns 192.168.128.1

4. Verify Ethernet port 1 network connectivity using the following command:

.. code-block:: shell

   ping -I eth1 www.baidu.com -c 3

5. Example output: `0% packet loss` means the test passed.

.. code-block:: shell

   PING www.baidu.com (183.2.172.177): 56 data bytes
   64 bytes from 183.2.172.177: seq=0 ttl=54 time=6.859 ms
   64 bytes from 183.2.172.177: seq=1 ttl=54 time=6.508 ms
   64 bytes from 183.2.172.177: seq=2 ttl=54 time=6.886 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 packets received, 0% packet loss
   round-trip min/avg/max = 6.508/6.751/6.886 ms

SD Interface Test
-------------------

|  **Test Description**: Insert a TF card.
|  **Interface Label**: U19
|  **System Device**: /dev/mmcblk0 mmcblk0p1
|  **Test Procedure**:

1. Insert the TF card into the SD interface. The development board will output:

.. code-block:: shell

   >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] HS mode. <<

2. Enter the following command to view SD card information:

.. code-block:: shell

   fdisk -l

|  Output as follows:

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

3. Remove the TF card; output as follows:

.. code-block:: shell

   SDMMC0 >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] DEFS mode. <<

|  **Result**: The operation behavior matches expectations, indicating normal TF card hot-plug.

RTC Test
----------

|  **Test Description**: Read and set time; check time correctness after power-off and reboot.
|  **Interface Label**: CON1
|  **System Device**: /dev/rtc0
|  **Test Procedure**:

1. Power on the device, check current system time:

.. code-block:: shell

   date

|  Output example:

.. code-block:: shell

   Sat Jan  1 00:26:33 UTC 2000

2. Check RTC clock:

.. code-block:: shell

   hwclock

|  Output example:

.. code-block:: shell

   Sat Jan  1 00:26:54 2000  0.000000 seconds

3. Set system time:

.. code-block:: shell

   date -s "2026-1-29 9:30:00"

4. Write system time to RTC and verify:

.. code-block:: shell

   hwclock -w
   hwclock

5. Power off, then check if time was saved correctly:

.. code-block:: shell

   hwclock

|  Output example:

.. code-block:: shell

   Thu Jan 29 09:32:10 2026  0.000000 seconds

|  **Result**: Time is close to the set value and continues running, indicating successful write to RTC.

RS232 Test
------------

|  **Test Description**: Loopback test by shorting 232_TX1↔232_RX1 and 232_TX2↔232_RX2.
|  **Interface Label**: 232_TX1,232_RX1  232_TX2,232_RX2
|  **System Device**: /dev/ttyS4, ttyS5
|  **Test Procedure**:

1. Short 232_TX1 and 232_RX1 using a Dupont wire.
2. Enter the test directory:

.. code-block:: shell

   cd /customer/app/

3. Run the test program:

.. code-block:: shell

   ./serial_test.out /dev/ttyS4 "www.myzr.com.cn"

|  Output example:

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

4. Short 232_TX2 and 232_RX2 using a Dupont wire.
5. Enter the test directory:

.. code-block:: shell

   cd /customer/app/

6. Run the test program:

.. code-block:: shell

   ./serial_test.out /dev/ttyS5 "www.myzr.com.cn"

|  Output example:

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
------------

|  **Test Description**: Transmit/receive test via RS485‑USB adapter connected to PC.
|  **Interface Label**: 485_A1,485_B1,485_A2,485_B2,485_A3,485_B3
|  **System Device**: /dev/ttyS2，/dev/ttyS6，/dev/ttyS7
|  **Test Procedure**:

1. Connect the development board and PC using an RS485‑USB adapter (A↔A, B↔B).
2. Open the corresponding serial port in Xshell; set baud rate 115200, data bits 8, stop bit 1.
3. Enter the test directory:

.. code-block:: shell

   cd /customer/app/

4. Run the test:

.. code-block:: shell

   ./serial_test.out /dev/ttyS2 "www.myzr.com.cn"

|  The RS485 serial terminal will output:

.. code-block:: shell

   www.myzr.com.cn

5. Enter `123` in the RS485 serial terminal (no echo); it will be displayed on the board terminal.

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

6. 485_A2,485_B2 correspond to ttyS6; 485_A3,485_B3 correspond to ttyS7. Test procedure is the same as above.

Relay Test
------------

|  **Test Description**: Test pull-in by setting GPIO pins high/low.
|  **Interface Label**: J8, J9
|  **System Device**:
|  **Test Procedure**:

1. Enter the following commands to test relay J8 pull-in by toggling GPIO:

.. code-block:: shell

   echo 121 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio121/direction
   echo 1 > /sys/class/gpio/gpio121/value
   echo 0 > /sys/class/gpio/gpio121/value

|  **Result**: Relay pull-in sound can be heard.

2. Enter the following commands to test relay J9 pull-in by toggling GPIO:

.. code-block:: shell

   echo 122 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio122/direction
   echo 1 > /sys/class/gpio/gpio122/value
   echo 0 > /sys/class/gpio/gpio122/value

|  **Result**: Relay pull-in sound can be heard.

LED Test
----------

|  **Test Description**: Test LED on/off by setting GPIO pins high/low.
|  **Interface Label**: P3
|  **System Device**: LED
|  **Test Procedure**:

1. Set GPIO high to turn on the middle LED:

.. code-block:: shell

   echo 98 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio98/direction
   echo 1 > /sys/class/gpio/gpio98/value

|  **Result**: Middle LED lights up → normal.

2. Set GPIO low to turn off the middle LED:

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio98/value

|  **Result**: Middle LED turns off → normal.

3. Set GPIO high to turn on the bottom LED:

.. code-block:: shell

   echo 82 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio82/direction
   echo 1 > /sys/class/gpio/gpio82/value

|  **Result**: Bottom LED lights up → normal.

4. Set GPIO low to turn off the bottom LED:

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio82/value

|  **Result**: Bottom LED turns off → normal.

4G Test
---------

|  **Test Description**: After successful 4G connection, verify by sending ICMP packets to the external network.
|  **Interface Label**: U38
|  **System Device**: /dev/ttyUSB1，usb0
|  **Test Procedure**:

1. Connect the 4G antenna to interface “U3” and insert the SIM card into slot “J3”.
2. Set pin 4G_PWRKEY1 high to power on the 4G module:

.. code-block:: shell

   echo 98 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio98/direction
   echo 1 > /sys/class/gpio/gpio98/value
   echo 64 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio64/direction
   echo 1 > /sys/class/gpio/gpio64/value

3. Initialize and start 4G:

.. code-block:: shell

   echo -e "AT+QNETDEVCTL=3,1,1\r\n" > /dev/ttyUSB1

4. Check if 4G module is detected:

.. code-block:: shell

   lsusb

|  If `Quectel EC801E-CN` appears, startup succeeded. Wait 1 minute if not found:

.. code-block:: shell

   Bus 001 Device 001: ID 1d6b:0002 Linux 6.1.111-rt42 ehci_hcd EHCI Host Controller
   Bus 001 Device 003: ID 0bda:d723 Realtek 802.11n WLAN Adapter
   Bus 001 Device 002: ID 1a40:0101 USB 2.0 Hub
   Bus 001 Device 005: ID 2c7c:0903 Quectel EC801E-CN

5. Obtain IP address:

.. code-block:: shell

   udhcpc -i usb0

|  Example output:

.. code-block:: shell

   udhcpc: started, v1.37.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.43.100, server 192.168.43.1
   udhcpc: lease of 192.168.43.100 obtained from 192.168.43.1, lease time 86400
   deleting routers
   adding dns 192.168.43.2
   adding dns 192.168.43.3

6. Verify 4G connection:

.. code-block:: shell

   ping -I usb0 www.baidu.com -c 3

|  `0% packet loss` means the test passed.

.. code-block:: shell

   PING www.baidu.com (183.240.99.224): 56 data bytes
   64 bytes from 183.240.99.224: seq=0 ttl=51 time=56.363 ms
   64 bytes from 183.240.99.224: seq=1 ttl=51 time=56.105 ms
   64 bytes from 183.240.99.224: seq=2 ttl=51 time=55.599 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 packets received, 0% packet loss
   round-trip min/avg/max = 55.599/56.022/56.363 ms

WiFi STA Test
---------------

|  **Test Description**: After successful WiFi connection, verify by sending ICMP packets to the external network.
|  **Interface Label**: U41
|  **System Device**: wlan0
|  **Test Procedure**:

1. Connect the WiFi antenna to interface “U40”.
2. Generate WPA PSK file for SSID (example: MY‑WIFI My202412):

.. code-block:: shell

   wpa_passphrase MY-WIFI My202412 > /etc/wpa_supplicant.conf
   wpa_passphrase MYZR-WiFi-5G Myzr2012 > /etc/wpa_supplicant.conf

4. Connect to WiFi:

.. code-block:: shell

   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

5. Example output:

.. code-block:: shell

   Successfully initialized wpa_supplicant
   nl80211: kernel reports: Authentication algorithm number required
   [  266.744713] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready

6. Obtain IP address:

.. code-block:: shell

   udhcpc -i wlan0

|  Example output:

.. code-block:: shell

   udhcpc: started, v1.36.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.43.35, server 192.
   udhcpc: lease of 192.168.43.35 obtained from 192.168.43.1, lease time 3600
   deleting routers
   adding dns 192.168.43.1

7. Test connection:

.. code-block:: shell

   ping -I wlan0 www.baidu.com -c 3

|  `0% packet loss` means normal WiFi connection.

.. code-block:: shell

   PING www.baidu.com (183.2.172.177) from 192.168.61.73 wlan0: 56(84) bytes of data.
   64 bytes from 183.2.172.177: icmp_seq=1 ttl=54 time=10.0 ms
   64 bytes from 183.2.172.177: icmp_seq=2 ttl=54 time=13.2 ms
   64 bytes from 183.2.172.177: icmp_seq=3 ttl=54 time=14.5 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 10.031/12.576/14.482/1.872 ms

Bluetooth
-----------

|  **Test Description**: After gateway connection is successful, verify communication by sending/receiving data between gateway and node.
|  **Interface Label**: U53
|  **System Device**: /dev/ttyS3
|  **Test Procedure**:

**Connect two development boards: one Bluetooth module as G(mesh) gateway, the other as N(mesh) node.**

1. Enter the test application directory on both terminals:

.. code-block:: shell

   cd /customer/app

2. On the gateway terminal, run:

.. code-block:: shell

   ./wg

|  Output below indicates gateway connected to node:

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

3. On the node terminal, put node into receive mode:

.. code-block:: shell

   ./serial_test.out /dev/ttyS1 1

4. On the gateway terminal, send `12345` to the node:

.. code-block:: shell

   ./n0x002

|  The node terminal will receive `12345`:

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

5. On the gateway terminal, put gateway into receive mode:

.. code-block:: shell

   ./serial_test.out /dev/ttyS1 1

6. On the node terminal, send `12345` to the gateway:

.. code-block:: shell

   ./a

|  The gateway terminal will receive `12345`:

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

7. If using a module as the node, use a serial tool with the following configuration:

.. figure:: /image/MYZR-其他/网关/GW510/测试手册6.png
   :alt: 测试手册6.png
   :width: 60%

|  When the gateway runs `./n0x002`, this tool will receive: `07 00 93 00 31 32 33 34 35`
|  To send from node to gateway: configure as shown, send `00 ff 00 01 31 32 33 34 35 36`.
|  First run `./serial_test.out /dev/ttyS1 1` on the gateway to enable reception.

LoRa Test
-----------

|  **Test Description**: Open two development terminals for transmit/receive verification.
|  **Interface Label**: U51
|  **System Device**: /dev/ttyS3
|  **Test Procedure**:

1. Connect the antenna to interface “U51”.
2. Enter the test directory:

.. code-block:: shell

   cd /customer/app/

3. Set operating mode (M0=1, M1=0) on **both terminals**:

.. code-block:: shell

   echo 96 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio96/direction
   echo 1 > /sys/class/gpio/gpio96/value
   echo 97 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio97/direction
   echo 0 > /sys/class/gpio/gpio97/value

4. On Terminal 2:

.. code-block:: shell

   ./lora /dev/ttyS1 12345

5. Output:

.. code-block:: shell

   Sent: 12345
   Entering receive mode...

6. On Terminal 1:

.. code-block:: shell

   ./lora /dev/ttyS1 123456

7. Terminal 2 will receive:

.. code-block:: shell

   Sent: 12345
   Entering receive mode...
   Received: 123456

8. Stop reception on Terminal 2 (Ctrl+C), then send to Terminal 1:

.. code-block:: shell

   ^C
   ./lora /dev/ttyS3 12345

9. Terminal 1 will receive:

.. code-block:: shell

   Sent: 123456
   Entering receive mode...
   Received: 12345

DO Test
---------

|  **Test Description**: Verify digital output function.
|  **Interface Label**: OUT0+, OUT0-
|  **System Device**:
|  **Test Procedure**:

1. DO test wiring diagram:

.. figure:: /image/MYZR-其他/网关/GW510/测试手册7.png
   :alt: 测试手册7.png
   :width: 60%

|  Note: Voltage = 3.3V, Current = 0.1A, Overcurrent protection = 0.12A.

2. Connect OUT+ to 3.3V power supply. Measure OUT− with oscilloscope or multimeter:
   OUT− is low by default; after connecting OUT+ to 3.3V, OUT− is 3V–3.3V.
   You may also check pin status via commands.

3. Set pin high test:

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   echo 1 > /sys/class/gpio/gpio126/value

|  Measure OUT−: 3V–3.3V.
|  Check status:

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   cat /sys/class/gpio/gpio126/value

|  Output = 1.

4. Set pin low test:

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   echo 0 > /sys/class/gpio/gpio126/value

|  Measure OUT−: 0V.
|  Check status:

.. code-block:: shell

   echo 126 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio126/direction
   cat /sys/class/gpio/gpio126/value

|  Output = 0.

DI Test
---------

|  **Test Description**: Verify digital input function.
|  **Interface Label**: IN0+, IN0-
|  **System Device**:
|  **Test Procedure**:

1. DI test wiring diagram:

.. figure:: /image/MYZR-其他/网关/GW510/测试手册8.png
   :alt: 测试手册8.png
   :width: 60%

2. Connect IN0+ to 3.3V power supply, IN0− to GND.

|  Note: Voltage = 3.3V, Current = 0.1A, Overcurrent protection = 0.12A.

3. When IN0+ (3.3V) is **off**, read logic level = 1.

.. code-block:: shell

   echo 125 > /sys/class/gpio/export
   echo in > /sys/class/gpio/gpio125/direction
   cat /sys/class/gpio/gpio125/value

|  Result: `1` → OK.

.. code-block:: shell

   root@myzr:~# cat /sys/class/gpio/gpio125/value
   1

|  When IN0+ (3.3V) and IN0− (GND) are **on**, read logic level = 0.

.. code-block:: shell

   echo 125 > /sys/class/gpio/export
   echo in > /sys/class/gpio/gpio125/direction
   cat /sys/class/gpio/gpio125/value

|  Result: `0` → normal response.

.. code-block:: shell

   root@myzr:~# cat /sys/class/gpio/gpio125/value
   0