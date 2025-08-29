Test Guide
============

LED Test
-----------

|  Interface Silkscreen: LED2, LED3
|  System Interface: /sys/class/leds/user-led0 and /sys/class/leds/user-led1
|  Test Description:
|  Test Operation

1. Enter the command to turn on LED2:

.. code-block:: shell

   echo 1 > /sys/class/leds/user-led0/brightness

2. Enter the command to turn on LED3:

.. code-block:: shell

   echo 1 > /sys/class/leds/user-led1/brightness

Ethernet Port Test
--------------------

Ethernet Port 1
~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON16
|  System Interface: eth0
|  Test Description: Test by sending ICMP packets from the development board to the PC
|  Test Operation

1. Configure the PC's wired network card IP to 192.168.137.99

.. code-block:: shell

   ifconfig eth1 down
   ifconfig eth0 up
   ifconfig eth0 192.168.137.81

4. Enter the following command to verify Ethernet Port 1:

.. code-block:: shell

   ping -I eth0 192.168.137.99 -c 2 -w 4
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=128 time=0.444 ms
   64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.419 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.419/0.431/0.444 ms

|  "0% packet loss" indicates the test is passed
|  If "100% packet loss" occurs, first confirm whether all firewalls on the PC are turned off

Ethernet Port 2
~~~~~~~~~~~~~~~~~~

**Gigabit Ethernet Port:**

|  Interface Silkscreen: CON15
|  System Interface: eth1
|  Test Description: Test by sending ICMP packets from the development board to the PC
|  Test Operation

1. Configure the PC's wired network card IP to 192.168.137.99

.. code-block:: shell

   ifconfig eth0 down
   ifconfig eth1 up
   ifconfig eth1 192.168.137.81

4. Enter the following command to verify Ethernet Port 2:

.. code-block:: shell

   ping -I eth1 192.168.137.99 -c 2 -w 4
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=128 time=0.683 ms
   64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.390 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.390/0.536/0.683 ms
   # [  239.952473] random: crng init done

|  "0% packet loss" indicates the test is passed
|  If "100% packet loss" occurs, first confirm whether all firewalls on the PC are turned off

Ethernet Port 3
~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON14
|  System Interface: eth2
|  Test Description: Test by sending ICMP packets from the development board to the PC
|  Test Operation

1. Configure the PC's wired network card IP to 192.168.137.99

.. code-block:: shell

   echo 342 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio342/direction
   ifconfig eth0 down
   ifconfig eth1 down
   ifconfig eth2 up
   ifconfig eth3 down
   ifconfig eth2 192.168.137.81

4. Enter the following command to verify Ethernet Port 2:

.. code-block:: shell

   ping -I eth2 192.168.137.99 -c 2 -w 4
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=128 time=0.683 ms
   64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.390 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.390/0.536/0.683 ms
   # [  239.952473] random: crng init done

|  "0% packet loss" indicates the test is passed
|  If "100% packet loss" occurs, first confirm whether all firewalls on the PC are turned off

Ethernet Port 4
~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON13
|  System Interface: eth2
|  Test Description: Test by sending ICMP packets from the development board to the PC
|  Test Operation

1. Configure the PC's wired network card IP to 192.168.137.99

.. code-block:: shell

   echo 342 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio342/direction
   ifconfig eth0 down
   ifconfig eth1 down
   ifconfig eth2 down
   ifconfig eth3 up
   ifconfig eth3 192.168.137.81

4. Enter the following command to verify Ethernet Port 2:

.. code-block:: shell

   ping -I eth3 192.168.137.99 -c 2 -w 4
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=128 time=0.515 ms
   64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.481 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.481/0.498/0.515 ms

|  "0% packet loss" indicates the test is passed
|  If "100% packet loss" occurs, first confirm whether all firewalls on the PC are turned off

USB Test
----------

|  Interface Silkscreen:
|  1) USB 2.0 : CON11
|  2) Type-C : CON12
|  Test Description: Test by plugging and unplugging a USB storage device (USB flash drive)
|  Test Operation

1. Insert the USB device into the USB interface of the base board, and the system will output information similar to the following:

.. code-block:: shell

   ...
   [  988.019550] sd 0:0:0:0: [sda] 1966080 512-byte logical blocks: (1.01 GB/960 MiB)
   [  988.028539] sd 0:0:0:0: [sda] Write Protect is off
   [  988.033907] sd 0:0:0:0: [sda] Mode Sense: 0b 00 00 08
   [  988.040290] sd 0:0:0:0: [sda] No Caching mode page found
   [  988.046236] sd 0:0:0:0: [sda] Assuming drive cache: write through
   [  988.076798]  sda:
   [  988.081909] sd 0:0:0:0: [sda] Attached SCSI removable disk

2. Unplug the USB device from the base board, and the system will output information similar to the following:

.. code-block:: shell

   [ 1046.519402] usb 1-1.1.4: USB disconnect, device number 6

SD Interface Test
--------------------

|  Interface Silkscreen: CON7
|  Test Description: Test by plugging and unplugging a TF card
|  Test Operation

1. Install the TF card into the SD interface, and the development board will output the following information:

.. code-block:: shell

   ...
   [ 1181.653628] mmc1: new high speed SDHC card at address 0001
   [ 1181.660659] mmcblk1: mmc1:0001 TF 4G 3.68 GiB 
   [ 1181.669095]  mmcblk1: p1
   ...

|  Result: If the output information after the operation meets the correct expectation, it indicates that the TF card is correctly recognized.

2. Unplug the TF card, and the output information is as follows:

.. code-block:: shell

   ...
   [ 1235.622463] mmc1: card 0001 removed
   ...

|  Result: If the phenomenon during the operation meets the correct expectation, it indicates that the TF hot-swapping function is normal.

Audio Playback Test
----------------------

|  Interface Silkscreen: CON18
|  Test Description: Verify the audio playback function of the evaluation board by playing audio files
|  Test Operation

1. Connect the earphone to the interface corresponding to the silkscreen
2. Enter the following command for testing:

|  Check the audiocodec sound card and its number

.. code-block:: shell

   aplay -l

|  Configure LINEOUT 

.. code-block:: shell

   LINEOUT

|  Specify the playback device, hw:card number,device number

.. code-block:: shell

   aplay -Dhw:0 music_test.wav

|  Audio output from the earphone indicates that the audio playback test is passed

Recording Test (Temporary)
-----------------------------

|  Interface Silkscreen: JP1
|  Test Description: Test by recording and playing back the recorded file
|  Test Operation

1. Insert the earphone with MIC into the interface corresponding to the silkscreen
2. Enter the following command to record for 10 seconds:

.. code-block:: shell

   arecord -d 10 -f cd -r 44100 -c 2 -t wav record.wav

3. Insert the earphone or speaker into the interface corresponding to the silkscreen J16 to play the recorded audio file, and enter the following command:

.. code-block:: shell

   aplay -D hw:0,0 record.wav

|  The recorded sound output from the earphone or speaker indicates that the recording test is passed

Wifi Test
-----------

|  Interface Silkscreen: U13
|  Test Description: After the WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal
|  Test Operation

1. Connect the WIFI antenna to the "U12" interface
2. Generate the WPA PSK file for the SSID

.. code-block:: shell

   wpa_passphrase command format: wpa_passphrase + wifi name + wifi password > /etc/wpa_supplicant.conf

|  Enter the following commands (the first command masks redundant information):

.. code-block:: shell

   dmesg -n 1
   wpa_passphrase MY-WIFI My202412 > /etc/wpa_supplicant.conf

3. Connect, enter the following command:

.. code-block:: shell

   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

|  Output information:

.. code-block:: shell

   Successfully initialized wpa_supplicant
   nl80211: kernel reports: Authentication algorithm number required
   [  266.744713] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready

4. Obtain an IP address, enter the following command:

.. code-block:: shell

   udhcpc -i wlan0

|  Output information:

.. code-block:: shell

   udhcpc: started, v1.36.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.61.187, server 192.168.60.1
   udhcpc: lease of 192.168.61.187 obtained from 192.168.60.1, lease time 86400
   deleting routers
   adding dns 192.168.60.1

5. Test the connection, enter the following command:

.. code-block:: shell

   ping -I wlan0 www.baidu.com -c 3

|  Output information:

.. code-block:: shell

   PING www.baidu.com (183.2.172.177) from 192.168.61.73 wlan0: 56(84) bytes of data.
   64 bytes from 183.2.172.177: icmp_seq=1 ttl=54 time=10.0 ms
   64 bytes from 183.2.172.177: icmp_seq=2 ttl=54 time=13.2 ms
   64 bytes from 183.2.172.177: icmp_seq=3 ttl=54 time=14.5 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 10.031/12.576/14.482/1.872 ms

|  Result: "0% packet loss" indicates that the wifi connection is normal

Bluetooth Test (No Driver)
-----------------------------

|  Interface Silkscreen: U13
|  Test Description: After scanning for Bluetooth devices, send an L2CAP response request and receive the reply
|  Test Operation

1. Connect the antenna to the "U12" interface
2. Start Bluetooth, enter the following command:

.. code-block:: shell

   hciconfig hci0 up

3. Scan for external Bluetooth devices, enter the following command:

.. code-block:: shell

   hcitool scan

|  Output:

.. code-block:: shell

   Scanning ...
           40:45:A0:49:3B:1A        chensz

|  Obtain the output information; the required information is similar to the following: "        74:B5:87:DB:09:7A        chensz"

5. Send an L2CAP packet for testing, enter the following command:

.. code-block:: shell

   l2ping 40:45:A0:49:3B:1A

|  Output information:

.. code-block:: shell

   Ping: 40:45:A0:49:3B:1A from E8:5C:5F:B5:7A:11 (data size 44) ...
   44 bytes from 40:45:A0:49:3B:1A id 0 time 32.41ms
   44 bytes from 40:45:A0:49:3B:1A id 1 time 77.03ms
   44 bytes from 40:45:A0:49:3B:1A id 2 time 90.89ms
   44 bytes from 40:45:A0:49:3B:1A id 3 time 59.38ms
   44 bytes from 40:45:A0:49:3B:1A id 4 time 93.44ms
   ^C5 sent, 5 received, 0% loss

|  Result: "0% packet loss" indicates that the Bluetooth connection is normal

CAN Test
-----------

|  Interface Silkscreen: J14
|  Test Description:
|  Test Operation

1. Use a Dupont wire to connect H2 of J14 to H4, and L2 to L4
2. Configure CAN, enter the following commands:

|  can1

.. code-block:: shell

   ip link set can1 up type can bitrate 1000000 dbitrate 5000000 fd on

|  can3

.. code-block:: shell

   ip link set can3 up type can3 bitrate 1000000 dbitrate 5000000 fd on
   candump can3 &

3. CAN1 sends data, enter the following command:

.. code-block:: shell

   cansend can1 1F334455#1122334455667788

|  Receive "can3  1F334455   [8]  11 22 33 44 55 66 77 88"

4. Modify the CAN configuration, CAN3 sends data, enter the following command:

.. code-block:: shell

   candump can1 &

.. code-block:: shell

   cansend can3 1F334455#1122334455667788

|  You can receive "can1  1F334455   [8]  11 22 33 44 55 66 77 88"
|  If the output during the operation meets the expectation, the function is normal.

UART Test
-----------

TTL
~~~~~

|  Interface Silkscreen: CON28~CON31 (where uart0 corresponds to the software ttyAS15)
|  Test Description: Conduct send and receive tests by interconnecting with the PC via a TTL-USB converter
|  Test Operation

1. Use a TTL-USB converter to connect the development board and the PC
2. Use Xshell to open the corresponding serial port, set the baud rate to 115200, data bits to 8, and stop bit to 1
3. Send test, enter the following command

.. code-block:: shell

   num=7
   stty -F /dev/ttyAS$num 115200
   echo MYZR > /dev/ttyAS$num

|  You can see MYZR output on the 485 serial port terminal

4. Receive test: On the 485 serial port terminal, directly enter 123 and press the Enter key to send, then you can see the information

.. code-block:: shell

   cat /dev/ttyAS$num

|  Press "Ctrl + C" to exit. If the output during the operation meets the expectation, the function is normal.

RS232
~~~~~~~

|  Interface Silkscreen: CON10, CON9
|  Test Description: Conduct send and receive tests by interconnecting with the PC via a 485-USB converter
|  Test Operation

1. Use a 485-USB converter to connect the development board and the PC
2. Use Xshell to open the corresponding serial port, set the baud rate to 115200, data bits to 8, and stop bit to 1
3. Send test, enter the following command

.. code-block:: shell

   num=1
   stty -F /dev/ttyAS$num 115200 -crtscts
   echo 200 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio200/direction
   echo 1 > /sys/class/gpio/gpio200/value
   echo MYZR > /dev/ttyAS$num

|  You can see 123456789 output on the 485 serial port terminal

4. Receive test: On the 485 serial port terminal, directly enter 123 and press the Enter key to send, then you can see the information

.. code-block:: shell

   echo 200 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio200/direction
   echo 0 > /sys/class/gpio/gpio200/value
   cat /dev/ttyAS$num
   ...
   123

|  Press "Ctrl + C" to exit. If the output during the operation meets the expectation, the function is normal.
|  GPIOs for other serial ports: uart2 (118), uart3 (230), uart4 (271), uart9 (261), uart11 (238)

RS485
~~~~~~~~

|  Interface Silkscreen: J20
|  Test Description: Conduct send and receive tests by interconnecting with the PC via a 485-USB converter
|  Test Operation

1. Use a 485-USB converter to connect the development board and the PC
2. Use Xshell to open the corresponding serial port, set the baud rate to 115200, data bits to 8, and stop bit to 1
3. Send test, enter the following command

.. code-block:: shell

   num=1
   stty -F /dev/ttyAS$num 115200 -crtscts
   echo 200 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio200/direction
   echo 1 > /sys/class/gpio/gpio200/value
   echo MYZR > /dev/ttyAS$num

|  You can see MYZR output on the 485 serial port terminal

4. Receive test: On the 485 serial port terminal, directly enter 123 and press the Enter key to send, then you can see the information

.. code-block:: shell

   echo 200 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio200/direction
   echo 0 > /sys/class/gpio/gpio200/value
   cat /dev/ttyAS$num
   ...
   123

|  Press "Ctrl + C" to exit. If the output during the operation meets the expectation, the function is normal.
|  GPIOs for other serial ports: uart2 (118), uart3 (230), uart4 (271), uart9 (261), uart11 (238)

RTC Test
----------

|  Interface Silkscreen: BT1
|  Test Description: Read and set the time, and check if the time is correct after power-off and restart
|  Test Operation

1. Power off, check if the button battery is installed, use a multimeter to check if the RTC battery has power; a measured voltage of approximately 3.3V is normal
2. Power on the device, check the current system clock, enter the following command:

.. code-block:: shell

   date

|  Output information:

.. code-block:: shell

   Wed May 14 02:06:10 UTC 2025

3. Check the RTC clock, enter the command:

.. code-block:: shell

   hwclock

|  Output information:

.. code-block:: shell

   Wed May 14 02:06:20 2025  0.000000 seconds

4. Set the system time

.. code-block:: shell

   date -s "2025-5-14 10:30:00"

5. Write the system time to RTC, and check if the writing is successful, enter the following command:

.. code-block:: shell

   hwclock -w
   hwclock

|  Output information:

.. code-block:: shell

   Wed May 14 10:30:10 2025  0.000000 seconds

|  If it is roughly the same as the system time, it indicates that the RTC writing is successful.

5. Power off and restart the device, check the RTC clock, enter the following command:

.. code-block:: shell

   hwclock

|  Output information:

.. code-block:: shell

   Wed May 14 10:30:43 2025  0.000000 seconds

|  If the RTC time continues to advance from the original time, it indicates that the RTC test is passed.

Key Test
----------

|  Interface Silkscreen: K4, K5
|  Test Description:
|  Test Operation:

1. Enter the command and press K5:

.. code-block:: shell

   od -x /dev/input/event23

|  Output:

.. code-block:: shell

   0000000 1d3f 0000 0000 0000 14f4 000f 0000 0000
   0000020 0001 0095 0001 0000 1d3f 0000 0000 0000
   0000040 14f4 000f 0000 0000 0000 0000 0000 0000
   0000060 1d40 0000 0000 0000 78c1 0002 0000 0000
   0000100 0001 0095 0000 0000 1d40 0000 0000 0000
   0000120 78c1 0002 0000 0000 0000 0000 0000 0000

1. Enter the command and press K5:

.. code-block:: shell

   od -x /dev/input/event11

|  Output:

.. code-block:: shell

   0000000 1d46 0000 0000 0000 a050 0006 0000 0000
   0000020 0001 0094 0001 0000 1d46 0000 0000 0000
   0000040 a050 0006 0000 0000 0000 0000 0000 0000
   0000060 1d46 0000 0000 0000 afc4 000a 0000 0000
   0000100 0001 0094 0000 0000 1d46 0000 0000 0000
   0000120 afc4 000a 0000 0000 0000 0000 0000 0000

HDMI Test
-----------

|  Interface Silkscreen: CON22
|  Test Description:
|  Test Operation:

1. Connect the HDMI interface screen to the interface corresponding to the silkscreen on the development board
2. Copy the program lt8912_force_1080p to the board
3. Enter the following command

.. code-block:: shell

   echo 202 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio202/direction
   echo 0 > /sys/class/gpio/gpio202/value
   ./lt8912_force_1080p

4. After outputting this information

.. code-block:: shell

   LT8912b chip ID: 0x12, 0xb2

|  The HDMI screen will display logs.

GPIO Test
------------

+------------+----------+----------+----------+----------+-----+-----+----------+
| Silkscreen | 1        | 3        | 5        | 7        | 11  | ... | 16       |
+------------+----------+----------+----------+----------+-----+-----+----------+
| GPIO       | GPIO1_B4 | GPIO1_B5 | GPIO1_B6 | GPIO1_B7 | GND | ... | GPIO1_C7 |
+------------+----------+----------+----------+----------+-----+-----+----------+
| High Level | 1.8V     | 1.8V     | 1.8V     | 1.8V     | -   | ... | 1.8V     |
+------------+----------+----------+----------+----------+-----+-----+----------+

|  Test Operation

1. Enter the following command to set GPIO1_B4 to high level:

.. code-block:: shell

   ./test_app/gpio_test.out GPIO1_B4 1

|  Output

.. code-block:: shell

   Set GPIO44 HIGH

|  Use a multimeter to measure this pin; a reading of 3.3V indicates the test is successful.

2. Enter the following command to set GPIO1_B4 to low level:

.. code-block:: shell

   ./test_app/gpio_test.out GPIO1_B4 0

|  Output

.. code-block:: shell

   Set GPIO44 LOW

|  Use a multimeter to measure this pin; a reading of 0V indicates the test is successful.

3. Interrupt detection: The trigger mode is falling edge trigger. Connect pins J23:1 and J23:2 with a Dupont wire, and enter the following command to make the pin enter interrupt detection mode

.. code-block:: shell

   ./test_app/gpio_test.out GPIO1_B4 irq &

|  Pull up GPIO3_A6 and then pull it down to meet the falling edge trigger condition

.. code-block:: shell

   ./test_app/gpio_test.out GPIO1_B5 1
   ./test_app/gpio_test.out GPIO1_B5 0

|  Output

.. code-block:: shell

   GPIO44 interrupt detected! Value: 0

|  If the above result meets the test expectation, it indicates the test is successful.

5G
-----

|  Interface Silkscreen: U23
|  Test Description:
|  Test Operation:
|  Connect the 5G module to U23 and connect the antenna to the 5G module
|  Enter the command:

.. code-block:: shell

   ./test_app/quectel-CM &

|  Output information:

.. code-block:: shell

   [01-01_00:07:13:012] Find /sys/bus/usb/devices/1-1.3 idVendor=0x2c7c idProduct=0x800, bus=0x001, dev=0x004
   [01-01_00:07:13:012] Auto find qmichannel = /dev/qcqmi2
   [01-01_00:07:13:012] Auto find usbnet_adapter = eth2
   [01-01_00:07:13:012] netcard driver = GobiNet, driver version = 6.1.75
   [01-01_00:07:13:012] qmap_mode = 1, qmap_version = 5, qmap_size = 16384, muxid = 0x81, qmap_netcard = eth2
   [01-01_00:07:13:012] Modem works in QMI mode
   [01-01_00:07:13:024] Get clientWDS = 7
   [01-01_00:07:13:056] Get clientDMS = 8
   [01-01_00:07:13:088] Get clientNAS = 9
   [01-01_00:07:13:121] Get clientUIM = 10
   [01-01_00:07:13:152] requestBaseBandVersion RM500QGLABR11A02M4G
   [01-01_00:07:13:280] requestGetSIMStatus SIMStatus: SIM_READY
   [01-01_00:07:13:345] requestGetProfile[pdp:1 index:1] cmnet///0/IPV4
   [01-01_00:07:13:377] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: 5G_SA
   [01-01_00:07:13:409] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
   [01-01_00:07:13:409] ip addr flush dev eth2
   [01-01_00:07:13:416] ip link set dev eth2 down
   [  391.576009] GobiNet 1-1.3:1.4: Runtime PM usage count underflow!
   [01-01_00:07:14:048] requestSetupDataCall WdsConnectionIPv4Handle: 0xe5441560
   [  392.332033] net eth2: link_state 0x0 -> 0x1
   [01-01_00:07:14:177] ip link set dev eth2 up
   [01-01_00:07:14:188] busybox udhcpc -f -n -q -t 5 -i eth2
   udhcpc: started, v1.36.1
   udhcpc: broadcasting discover
   [  392.386699] GobiNet::GobiNetDriverRxQmapFixup rx_pkts=1, rx_len=312
   udhcpc: broadcasting select for 10.60.64.247, server 10.60.64.248
   udhcpc: lease of 10.60.64.247 obtained from 10.60.64.248, lease time 7200
   [01-01_00:07:14:246] deleting routers
   [01-01_00:07:14:278] adding dns 120.196.165.7
   [01-01_00:07:14:278] adding dns 221.179.38.7
   [  392.578960] IPv6: ADDRCONF(NETDEV_CHANGE): eth2: link becomes ready
   [  393.671782] GobiNet::GobiNetDriverRxQmapFixup rx_pkts=1, rx_len=328

|  Verify network connection:

.. code-block:: shell

   ping -I eth2 www.baidu.com -c 2 -w 4

|  Output information:

.. code-block:: shell

   PING www.a.shifen.com (183.240.99.169) from 10.60.64.247 eth2: 56(84) bytes of data.
   64 bytes from 183.240.99.169: icmp_seq=1 ttl=52 time=26.0 ms
   64 bytes from 183.240.99.169: icmp_seq=2 ttl=52 time=24.2 ms

   --- www.a.shifen.com ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1002ms
   rtt min/avg/max/mdev = 24.219/25.096/25.973/0.877 ms

|  If the above result meets the test expectation, it indicates the test is successful.

4G
-----

|  Interface Silkscreen: U23
|  Test Description:
|  Test Operation:
|  Connect the 4G module to U23 and connect the antenna to the 5G module
|  Enter the command:

.. code-block:: shell

   ./test_app/quectel-CM &

|  Output information:

.. code-block:: shell

   [01-01_00:07:13:012] Find /sys/bus/usb/devices/1-1.3 idVendor=0x2c7c idProduct=0x800, bus=0x001, dev=0x004
   [01-01_00:07:13:012] Auto find qmichannel = /dev/qcqmi2
   [01-01_00:07:13:012] Auto find usbnet_adapter = eth2
   [01-01_00:07:13:012] netcard driver = GobiNet, driver version = 6.1.75
   [01-01_00:07:13:012] qmap_mode = 1, qmap_version = 5, qmap_size = 16384, muxid = 0x81, qmap_netcard = eth2
   [01-01_00:07:13:012] Modem works in QMI mode
   [01-01_00:07:13:024] Get clientWDS = 7
   [01-01_00:07:13:056] Get clientDMS = 8
   [01-01_00:07:13:088] Get clientNAS = 9
   [01-01_00:07:13:121] Get clientUIM = 10
   [01-01_00:07:13:152] requestBaseBandVersion RM500QGLABR11A02M4G
   [01-01_00:07:13:280] requestGetSIMStatus SIMStatus: SIM_READY
   [01-01_00:07:13:345] requestGetProfile[pdp:1 index:1] cmnet///0/IPV4
   [01-01_00:07:13:377] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: 5G_SA
   [01-01_00:07:13:409] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
   [01-01_00:07:13:409] ip addr flush dev eth2
   [01-01_00:07:13:416] ip link set dev eth2 down
   [  391.576009] GobiNet 1-1.3:1.4: Runtime PM usage count underflow!
   [01-01_00:07:14:048] requestSetupDataCall WdsConnectionIPv4Handle: 0xe5441560
   [  392.332033] net eth2: link_state 0x0 -> 0x1
   [01-01_00:07:14:177] ip link set dev eth2 up
   [01-01_00:07:14:188] busybox udhcpc -f -n -q -t 5 -i eth2
   udhcpc: started, v1.36.1
   udhcpc: broadcasting discover
   [  392.386699] GobiNet::GobiNetDriverRxQmapFixup rx_pkts=1, rx_len=312
   udhcpc: broadcasting select for 10.60.64.247, server 10.60.64.248
   udhcpc: lease of 10.60.64.247 obtained from 10.60.64.248, lease time 7200
   [01-01_00:07:14:246] deleting routers
   [01-01_00:07:14:278] adding dns 120.196.165.7
   [01-01_00:07:14:278] adding dns 221.179.38.7
   [  392.578960] IPv6: ADDRCONF(NETDEV_CHANGE): eth2: link becomes ready
   [  393.671782] GobiNet::GobiNetDriverRxQmapFixup rx_pkts=1, rx_len=328

|  Verify network connection:

.. code-block:: shell

   ping -I eth2 www.baidu.com -c 2 -w 4

|  Output information:

.. code-block:: shell

   PING www.a.shifen.com (183.240.99.169) from 10.60.64.247 eth2: 56(84) bytes of data.
   64 bytes from 183.240.99.169: icmp_seq=1 ttl=52 time=26.0 ms
   64 bytes from 183.240.99.169: icmp_seq=2 ttl=52 time=24.2 ms

   --- www.a.shifen.com ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1002ms
   rtt min/avg/max/mdev = 24.219/25.096/25.973/0.877 ms

|  If the above result meets the test expectation, it indicates the test is successful.

External Watchdog Test
-------------------------

|  Interface Silkscreen: J1
|  Test Description:
|  Test Operation:

1. Select the ON position with the jumper cap to enable the external hardware watchdog. If no operation is performed, the system will restart within 1~3 minutes.

|  Enter the following command to feed the watchdog so that the system will not restart

.. code-block:: shell

   echo 8 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio8/direction
   while true; do echo 1 > /sys/class/gpio/gpio8/value;sleep 1;echo 0 > /sys/class/gpio/gpio8/value;sleep 1; done

ADC Test
----------

|  Interface Silkscreen: CON27
|  Test Description:
|  Test Operation:

1. Determine the pin position according to the schematic diagram
2. Use a Dupont wire to connect pin 2 and pin 1

|  Enter the following command (echo the corresponding pin number, gpadc_chip corresponds to the group):

.. code-block:: shell

   echo 1 > /sys/class/gpadc/gpadc_chip1/data
   cat /sys/class/gpadc/gpadc_chip1/data

|  Output:

.. code-block:: shell

   gpadc1-channel1 voltage data is 1797

|  Use a Dupont wire to connect pin 27 and pin 1
|  Enter the following command:

.. code-block:: shell

   cat /sys/class/gpadc/gpadc_chip1/data

|  Output:

.. code-block:: shell

   gpadc1-channel1 voltage data is 0