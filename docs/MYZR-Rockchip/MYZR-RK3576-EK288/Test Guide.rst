Test Guide
============

|   Qt Version: Qt 5.15.14

Ethernet Port Test
--------------------

Ethernet Port 1
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: J11
|   System Interface: eth0
|   Test Description: The test is performed by having the development board send ICMP packets to the PC.
|   Test Operations

1. Configure the computer's wired network card IP to 192.168.137.99
2. Use a network cable to connect the development board's Ethernet port to the computer's Ethernet port. The serial port displays the following information:

.. code:: shell

    [ 1069.788888] rk_gmac-dwmac 2a220000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx

3. By default, the IP is obtained automatically, but for the test, a static IP is configured. The specific configuration commands are as follows:

.. code:: shell

    ifconfig eth1 down
    ifconfig eth0 up
    ifconfig eth0 192.168.137.81

4. Enter the following command to verify Ethernet Port 1:

.. code:: shell

    ping -I eth0 192.168.137.99 -c 2 -w 4

.. code:: shell

    PING 192.168.137.99 (192.168.137.99) from 192.168.137.17 eth0: 56(84) bytes of data.
    64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=1.28 ms
    64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.378 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1002ms
    rtt min/avg/max/mdev = 0.378/0.829/1.280/0.451 ms

|   "0% packet loss" indicates the test is passed.
|   If "100% packet loss" appears, first confirm whether all the computer's firewalls are turned off.

Ethernet Port 2
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: J12
|   System Interface: eth1
|   Test Description: The test is performed by having the development board send ICMP packets to the PC.
|   Test Operations

1. Configure the computer's wired network card IP to 192.168.137.99
2. Use a network cable to connect the development board's Ethernet port to the computer's Ethernet port. The serial port displays the following information:

.. code:: shell

    [ 1030.430019] rk_gmac-dwmac 2a230000.ethernet eth1: Link is Up - 100Mbps/Full - flow control rx/tx

3. By default, the IP is obtained automatically, but for the test, a static IP is configured. The specific configuration commands are as follows:

.. code:: shell

    ifconfig eth0 down
    ifconfig eth1 up
    ifconfig eth1 192.168.137.81

4. Enter the following command to verify Ethernet Port 2:

.. code:: shell

    ping -I eth1 192.168.137.99 -c 2 -w 4

.. code:: shell

    PING 192.168.137.99 (192.168.137.99) from 192.168.137.185 eth1: 56(84) bytes of data.
    64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=1.42 ms
    64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.489 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1002ms
    rtt min/avg/max/mdev = 0.489/0.955/1.421/0.466 ms

|   "0% packet loss" indicates the test is passed.
|   If "100% packet loss" appears, first confirm whether all the computer's firewalls are turned off.

USB Test
----------

|   Interface Silkscreen:
|   1) USB 2.0: J4
|   2) USB 3.0: J3
|   3) Type-C: J2
|   Test Description: The test is performed by plugging and unplugging a USB storage device (USB flash drive).
|   Test Operations

1. Insert the USB device into the baseboard's USB interface. The system will output information similar to the following:

.. code:: shell

    [  869.018173] usb 1-1.4: new high-speed USB device number 5 using xhci-hcd
    [  869.220229] usb 1-1.4: New USB device found, idVendor=14cd, idProduct=1212, bcdDevice= 1.00
    [  869.220328] usb 1-1.4: New USB device strings: Mfr=1, Product=3, SerialNumber=2
    [  869.220365] usb 1-1.4: Product: Mass Storage Device
    [  869.220396] usb 1-1.4: Manufacturer: Generic
    [  869.220425] usb 1-1.4: SerialNumber: 121220160204
    [  869.222657] usb-storage 1-1.4:1.0: USB Mass Storage device detected
    [  869.223896] scsi host0: usb-storage 1-1.4:1.0
    [  870.239586] scsi 0:0:0:0: Direct-Access     Mass     Storage Device   1.00 PQ: 0 ANSI: 0 CCS
    [  870.399295] sd 0:0:0:0: [sda] 7725056 512-byte logical blocks: (3.96 GB/3.68 GiB)
    [  870.399787] sd 0:0:0:0: [sda] Write Protect is off
    [  870.400240] sd 0:0:0:0: [sda] No Caching mode page found
    [  870.400248] sd 0:0:0:0: [sda] Assuming drive cache: write through
    [  870.404106]  sda: sda1
    [  870.404624] sd 0:0:0:0: [sda] Attached SCSI removable disk
    [  869.018173] usb 1-1.4: new high-speed USB device number 5 using xhci-hcd
    [  869.220229] usb 1-1.4: New USB device found, idVendor=14cd, idProduct=1212, bcdDevice= 1.00
    [  869.220328] usb 1-1.4: New USB device strings: Mfr=1, Product=3, SerialNumber=2
    [  869.220365] usb 1-1.4: Product: Mass Storage Device
    [  869.220396] usb 1-1.4: Manufacturer: Generic
    [  869.220425] usb 1-1.4: SerialNumber: 121220160204
    [  869.222657] usb-storage 1-1.4:1.0: USB Mass Storage device detected
    [  869.223896] scsi host0: usb-storage 1-1.4:1.0
    [  870.239586] scsi 0:0:0:0: Direct-Access     Mass     Storage Device   1.00 PQ: 0 ANSI: 0 CCS
    [  870.399295] sd 0:0:0:0: [sda] 7725056 512-byte logical blocks: (3.96 GB/3.68 GiB)
    [  870.399787] sd 0:0:0:0: [sda] Write Protect is off
    [  870.400240] sd 0:0:0:0: [sda] No Caching mode page found
    [  870.400248] sd 0:0:0:0: [sda] Assuming drive cache: write through
    [  870.404106]  sda: sda1
    [  870.404624] sd 0:0:0:0: [sda] Attached SCSI removable disk

2. Unplug the USB device from the baseboard. The system will output information similar to the following:

.. code:: shell

    [  891.990845] usb 1-1.4: USB disconnect, device number 4

SD Interface Test
-------------------

|   Interface Silkscreen: J5
|   Test Description: The test is performed by plugging and unplugging a TF card.
|   Test Operations

1. Install the TF card into the SD interface. The development board will output the following information:

.. code:: shell

    [ 1774.070509] mmc_host mmc1: Bus speed (slot 0) = 50000000Hz (slot req 50000000Hz, actual 50000000HZ div = 0)
    [ 1774.070687] mmc1: new high speed SDHC card at address 0001
    [ 1774.071990] mmcblk1: mmc1:0001 TF 4G 3.68 GiB 
    [ 1774.074051]  mmcblk1: p1

|   Result: The output information after the operation meets the correct expectations, indicating that the TF card is correctly recognized.

2. Remove the TF card. The output information is as follows:

.. code:: shell

    [ 1826.912490] mmc1: card 0001 removed

|   Result: The phenomenon during the operation meets the correct expectations, indicating that the TF hot-swap function is normal.

Audio Playback Test
---------------------

|   Interface Silkscreen: P1
|   Test Description: Play an audio file to verify the audio playback function of the evaluation board.
|   Test Operations

1. Connect headphones to the interface corresponding to the silkscreen.
2. Enter the following command for testing:

|   Check the rockchipes8388 sound card and its number

.. code:: shell

    aplay -l

|   Specify the playback device, hw:card number, device number

.. code:: shell

    aplay -D hw:0,0 test_app/music_test.wav

|   The following information will be output:

.. code:: shell

    Playing WAVE 'test_app/music_test.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

|   Audio output from the headphones indicates that the audio playback test is passed.

Recording Test
----------------

|   Interface Silkscreen: JP1
|   Test Description: Record and play back the recorded file for testing.
|   Test Operations

1. Insert a headphone with a MIC into the interface corresponding to the silkscreen.
2. Enter the following command to record for 10 seconds:

.. code:: shell

    arecord -d 10 -f cd -r 44100 -c 2 -t wav record.wav

3. Connect headphones or speakers to the interface corresponding to silkscreen J16 to play the recorded audio file, and enter the following command:

.. code:: shell

    aplay -D hw:0,0 record.wav

|   The recorded sound output from the headphones or speakers indicates that the recording test is passed.

Wifi Test
-----------

|   Interface Silkscreen: U13
|   Test Description: After the WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal.
|   Test Operations

1. Connect the WIFI antenna to the "U12" interface.
2. Generate the WPA PSK file for the SSID.

.. code:: shell

    wpa_passphrase command format: wpa_passphrase + wifi name + wifi password > /etc/wpa_supplicant.conf

|   Enter the following command:

.. code:: shell

    wpa_passphrase MY-WIFI My202412 > /etc/wpa_supplicant.conf

3. Connect, enter the following command:

.. code:: shell

    wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

|   Output information:

.. code:: shell

    Successfully initialized wpa_supplicant
    nl80211: kernel reports: Authentication algorithm number required
    [  266.744713] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready

4. Obtain an IP, enter the following command:

.. code:: shell

    udhcpc -i wlan0

|   Output information:

.. code:: shell

    udhcpc: started, v1.36.0
    udhcpc: broadcasting discover
    udhcpc: broadcasting select for 192.168.61.187, server 192.168.60.1
    udhcpc: lease of 192.168.61.187 obtained from 192.168.60.1, lease time 86400
    deleting routers
    adding dns 192.168.60.1

5. Test the connection, enter the following command:

.. code:: shell

    ping -I wlan0 www.baidu.com -c 3

|   Output information:

.. code:: shell

    PING www.baidu.com (183.2.172.177) from 192.168.61.73 wlan0: 56(84) bytes of data.
    64 bytes from 183.2.172.177: icmp_seq=1 ttl=54 time=10.0 ms
    64 bytes from 183.2.172.177: icmp_seq=2 ttl=54 time=13.2 ms
    64 bytes from 183.2.172.177: icmp_seq=3 ttl=54 time=14.5 ms

    --- www.baidu.com ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2003ms
    rtt min/avg/max/mdev = 10.031/12.576/14.482/1.872 ms

|   Result: "0% packet loss" indicates that the wifi connection is normal.

Bluetooth Test
----------------

|   Interface Silkscreen: U13
|   Test Description: After scanning for Bluetooth devices, send an L2CAP echo request and receive a response.
|   Test Operations

1. Connect the antenna to the "U12" interface.
2. Start Bluetooth, enter the following command:

.. code:: shell

    hciconfig hci0 up

3. Scan for external Bluetooth devices, enter the following command:

.. code:: shell

    hcitool scan

|   Output:

.. code:: shell

    Scanning ...
            40:45:A0:49:3