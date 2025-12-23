Test Guide
============

Ethernet Port Test
--------------------

Ethernet Port 1
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: J14
|   System Interface: eth0
|   Test Description: Test by sending ICMP packets from the development board to the PC
|   Test Operations:

1. Configure the PC's wired network card IP to 192.168.137.99
2. Use an Ethernet cable to connect the development board's Ethernet port to the PC's Ethernet port. The serial port displays the following information:

.. code-block:: shell

    [  275.170629] rk_gmac-dwmac fe1c0000.ethernet eth0: Link is Up - 1Gbps/

3. By default, the IP is obtained automatically, but a static IP is configured for the test. The specific configuration commands are as follows:

.. code-block:: shell

    ifconfig eth1 down
    ifconfig eth0 up
    ifconfig eth0 192.168.137.81


4. Enter the following command to verify Ethernet Port 1:

.. code-block:: shell

    ping -I eth0 192.168.137.99 -c 2 -w 4
    PING 192.168.137.99 (192.168.137.99) from 192.168.137.81 eth0: 56(84) bytes of data.
    64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=0.947 ms
    64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.588 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1001ms
    rtt min/avg/max/mdev = 0.588/0.767/0.947/0.179 ms

|   "0% packet loss" indicates the test is passed
|   If "100% packet loss" occurs, first confirm whether all firewalls on the PC are turned off


Ethernet Port 2
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: U5
|   System Interface: eth1
|   Test Description: Test by sending ICMP packets from the development board to the PC
|   Test Operations:

1. Configure the PC's wired network card IP to 192.168.137.99
2. Use an Ethernet cable to connect the development board's Ethernet port to the PC's Ethernet port. The serial port displays the following information:

.. code-block:: shell

    [  528.550794] IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready

3. By default, the IP is obtained automatically, but a static IP is configured for the test. The specific configuration commands are as follows:

.. code-block:: shell

    ifconfig eth0 down
    ifconfig eth1 up
    ifconfig eth1 192.168.137.81

4. Enter the following command to verify Ethernet Port 2:

.. code-block:: shell

    ping -I eth1 192.168.137.99 -c 2 -w 4
    64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.575 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1002ms
    rtt min/avg/max/mdev = 0.575/0.812/1.049/0.237 ms


|   "0% packet loss" indicates the test is passed
|   If "100% packet loss" occurs, first confirm whether all firewalls on the PC are turned off


GPIO Test
-----------

+------------+------+------+------+------+------+------+------+
| Silkscreen | 11   | 12   | 13   | 14   | 15   | 16   | 17   |
+------------+------+------+------+------+------+------+------+
| GPIO       | IO11 | IO12 | IO13 | IO14 | IO15 | IO16 | IO17 |
+------------+------+------+------+------+------+------+------+
| High Level | 1.8V | 1.8V | 1.8V | 1.8V | 1.8V | 1.8V | 1.8V |
+------------+------+------+------+------+------+------+------+

|   Test Operations:

.. code-block:: shell

    echo out >/proc/myzr_gpio/IO11

    cat /proc/myzr_gpio/IO11

|   The output information is similar to the following:

.. code-block:: shell

    0
    echo 1 > /proc/myzr_gpio/IO11
    cat /proc/myzr_gpio/IO11

|   The output information is similar to the following:

.. code-block:: shell

    1

UART Test
------------

|   Interface Silkscreen: J17
|   Test Description: Test using UART self-transmission and self-reception
|   Test Operations

1. Short-circuit pins J17-3 (UART1_TX_M0) and J17-4 (UART1_RX_M0)
2. Enter the following command to perform the transmission and reception test:

.. code-block:: shell

    chmod 777 ./serial_test.out
    ./serial_test.out /dev/ttyS1 "myzr"
    Starting send data...finish
    Starting receive data:
    ASCII: 0x6d          Character: m 
    ASCII: 0x79          Character: y 
    ASCII: 0x7a          Character: z 
    ASCII: 0x72          Character: r 
    ASCII: 0x0            Character: 

Audio Playback Test
---------------------

|   Interface Silkscreen: J10
|   Test Description: Verify the audio playback function of the evaluation board by playing an audio file
|   Test Operations

1. Connect headphones to the interface corresponding to the silkscreen
2. Enter the following command to perform the test:

.. code-block:: shell

    aplay test.wav

3. Result: Audio output from the headphones indicates the audio playback test is passed

Recording Test
-----------------

|   Interface Silkscreen: J11
|   Test Description: Test by recording and playing back the recorded file
|   Test Operations:

1. Insert a MIC into the interface corresponding to the silkscreen
2. Enter the following command to record for 10 seconds:

.. code-block:: shell

    arecord -Dhw:1,0 -c 2 -r 44100 -f S16_LE -t wav test.wav

3. Connect headphones or a speaker to the interfaces corresponding to silkscreens J10 and J13 to play the recorded audio file, and enter the following command:

.. code-block:: shell

    aplay test.wav

|   Recorded audio output from the headphones or speaker indicates the recording test is passed


SPEAKER Test
---------------

|   Interface Silkscreen: J12
|   Test Description: The interface has 3 pins; connect a speaker to the interface corresponding to silkscreen J12
|   Test Operations

1. Enter the following command

.. code-block:: shell

    aplay /myzr_test/audio/mytest.wav

|   Sound output from the speaker indicates the test is passed


4G Test
----------

|   Interface Silkscreen: J19, ANT2
|   Test Description: Test by inserting/removing a SIM card and connecting an antenna
|   Test Operations:

1. Connect the 4G antenna and insert the SIM card
2. Start the development board
3. Obtain an IP address

.. code-block:: shell

    udhcpc -i usb0

4. Test the connection status

.. code-block:: shell

    ping -I usb0 baidu.com


USB Test
----------

|   Interface Silkscreen: J7, USB2.0
|   Test Description: Test by inserting/removing a USB storage device (USB flash drive)
|   Test Operations:

1. Insert the USB device into the USB interface of the baseboard. The system will output information similar to the following:

.. code-block:: shell

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

2. Remove the USB device from the baseboard. The system will output information similar to the following:

.. code-block:: shell

    [ 2690.764161] usb 2-1.1: USB disconnect, device number 3


Backlight Test
----------------

|   The brightness adjustment range of the backlight is (0--255), where 255 indicates the highest brightness and 0 indicates the backlight is turned off. After entering the system, enter the following commands in the terminal to perform the backlight test.
|   Enter the following command to check the current screen backlight value

.. code-block:: shell

    cat /sys/class/backlight/backlight/brightness

|   The output information is similar to the following:

.. code-block:: shell

    200

|   Enter the following command to turn off the backlight

.. code-block:: shell

    echo 0 > /sys/class/backlight/backlight/brightness

|   Enter the following command to turn on the backlight

.. code-block:: shell

    echo 200 > /sys/class/backlight/backlight/brightness


RTC Test
----------

|   Interface Silkscreen: RTC1
|   Test Description: Read and set the time, then check if the time is correct after power-off and restart
|   Test Operations:

1. Power off the device, check if the coin cell battery is installed, and use a multimeter to check if the RTC battery has power. A reading of approximately 3.3V is normal.
2. Power on the device and check the current system clock by entering the following command:

.. code-block:: shell

    date

|   Output information:

.. code-block:: shell

    Wed May 14 02:06:10 UTC 2025

3. Check the RTC clock by entering the command:

.. code-block:: shell

    hwclock

|   Output information:

.. code-block:: shell

    Wed May 14 02:06:20 2025  0.000000 seconds

4. Set the system time

.. code-block:: shell

    date -s "2025-5-14 10:30:00"

5. Write the system time to the RTC and check if the writing is successful by entering the following commands:

.. code-block:: shell

    hwclock -w
    hwclock

|   Output information:

.. code-block:: shell

    Wed May 14 10:30:10 2025  0.000000 seconds

|   A time similar to the system time indicates successful writing to the RTC.

6. Power off the device, restart it, and check the RTC clock by entering the following command:

.. code-block:: shell

    hwclock

|   Output information:

.. code-block:: shell

    Wed May 14 10:30:43 2025  0.000000 seconds

|   The RTC time continues to advance from the original time, indicating the RTC test is passed


Wifi Test
------------

|   Interface Silkscreen: ANT1
|   Test Description: After the WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify the connection is normal
|   Test Operations:

1. Connect the WIFI antenna to the "ANT1" interface
2. Generate a WPA PSK file for the SSID

.. code-block:: shell

    wpa_passphrase command format: wpa_passphrase + wifi name + wifi password > /etc/wpa_supplicant.conf

|   Enter the following command:

.. code-block:: shell

    wpa_passphrase MY-WIFI My202412 > /etc/wpa_supplicant.conf

3. Connect by entering the following command:

.. code-block:: shell

    wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

|   Output information:

.. code-block:: shell

    Successfully initialized wpa_supplicant
    nl80211: kernel reports: Match already configured

4. Obtain an IP address by entering the following command:

.. code-block:: shell

    udhcpc -i wlan0

|   Output information:

.. code-block:: shell

    udhcpc: started, v1.36.1
    udhcpc: broadcasting discover
    udhcpc: broadcasting select for 192.168.61.109, server 192.168.60.1
    udhcpc: lease of 192.168.61.109 obtained from 192.168.60.1, lease time 86400
    deleting routers
    route: SIOCADDRT: Network is unreachable
    adding dns 192.168.60.1

5. Test the connection by entering the following command:

.. code-block:: shell

    ping -I wlan0 www.baidu.com -c 3

|   Output information:

.. code-block:: shell

    PING www.baidu.com (183.2.172.17): 56 data bytes
    64 bytes from 183.2.172.17: seq=0 ttl=54 time=11.818 ms
    64 bytes from 183.2.172.17: seq=1 ttl=54 time=579.288 ms
    64 bytes from 183.2.172.17: seq=2 ttl=54 time=38.478 ms

    --- www.a.shifen.com ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss
    round-trip min/avg/max = 11.818/209.861/579.288 ms

|   Result: "0% packet loss" indicates the WIFI connection is normal


CAN Test
----------

|   The CAN interface of the RK3506 series is a CANFD interface.
|   The test can be performed using candump and cansend. Note to connect the devices in advance.

1. Configure and enable the CAN interface

.. code-block:: shell

    ip link set can0 up type can bitrate 100000  dbitrate 200000 fd on restart-ms 1000
    ip link set can1 up type can bitrate 100000  dbitrate 200000 fd on restart-ms 1000

2. Transmit and receive data

.. code-block:: shell

    candump can0 &
    candump can1 &
    
    cansend can0 123#112233eeff
    cansend can1 123#112233eeff