Test Guide
============

Ethernet Port Test
---------------------

Ethernet Port 1
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: J13
|   System Interface: eth0
|   Test Description: Test by having the development board send ICMP packets to the PC
|   Test Operations:

1. Configure the computer's wired network card IP to 192.168.137.99
2. Use a network cable to connect the development board's Ethernet port to the computer's Ethernet port. The serial port displays the following information:

.. code-block:: shell

    [  275.170629] rk_gmac-dwmac fe1c0000.ethernet eth0: Link is Up - 1Gbps/


3. By default, the IP is obtained automatically, but for the test, a static IP is configured. The specific configuration commands are as follows:

.. code-block:: shell

    ifconfig eth1 down
    ifconfig eth0 up
    ifconfig eth0 192.168.137.81

4. Enter the following command to verify Ethernet Port 1:

.. code-block:: shell

    ping -I eth0 192.168.137.99 -c 2 -w 4

.. code-block:: shell

    PING 192.168.137.99 (192.168.137.99) from 192.168.137.81 eth0: 56(84) bytes of data.
    64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=0.947 ms
    64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.588 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1001ms
    rtt min/avg/max/mdev = 0.588/0.767/0.947/0.179 ms

|   "0% packet loss" indicates the test passed
|   If "100% packet loss" appears, first confirm whether all the computer's firewalls are turned off

Ethernet Port 2
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: J14
|   System Interface: eth1
|   Test Description: Test by having the development board send ICMP packets to the PC
|   Test Operations:

1. Configure the computer's wired network card IP to 192.168.137.99
2. Use a network cable to connect the development board's Ethernet port to the computer's Ethernet port. The serial port displays the following information:

.. code-block:: shell

    [  528.550794] IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready


3. By default, the IP is obtained automatically, but for the test, a static IP is configured. The specific configuration commands are as follows:

.. code-block:: shell

    ifconfig eth0 down
    ifconfig eth1 up
    ifconfig eth1 192.168.137.81

4. Enter the following command to verify Ethernet Port 2:

.. code-block:: shell

    ping -I eth1 192.168.137.99 -c 2 -w 4


.. code-block:: shell

    64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.575 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1002ms
    rtt min/avg/max/mdev = 0.575/0.812/1.049/0.237 ms

|   "0% packet loss" indicates the test passed
|   If "100% packet loss" appears, first confirm whether all the computer's firewalls are turned off

USB Test
----------

|   Interface Silkscreen:
|   1) J4
|   2) J29
|   3) P2
|   Test Description: Test by plugging and unplugging a USB storage device (USB flash drive)
|   Test Operations:

1. Insert the USB device into the baseboard's USB interface. The system will output information similar to the following:

.. code-block:: shell

    [ 1029.428426] usb 2-1.1: new high-speed USB device number 4 using ehci-platform
    [ 1029.526593] usb 2-1.1: New USB device found, idVendor=abcd, idProduct=1234, bcdDevice= 1.00
    [ 1029.526688] usb 2-1.1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    [ 1029.526712] usb 2-1.1: Product: UDisk           
    [ 1029.526733] usb 2-1.1: Manufacturer: General 
    [ 1029.526753] usb 2-1.1: SerialNumber: 2401121918117820734311
    [ 1029.528412] usb-storage 2-1.1:1.0: USB Mass Storage device detected
    [ 1029.530317] scsi host1: usb-storage 2-1.1:1.0
    [ 1030.543580] scsi 1:0:0:0: Direct-Access     General  UDisk            5.00 PQ: 0 ANSI: 2
    [ 1030.545097] sd 1:0:0:0: [sda] 15728640 512-byte logical blocks: (8.05 GB/7.50 GiB)
    [ 1030.545832] sd 1:0:0:0: [sda] Write Protect is off
    [ 1030.546583] sd 1:0:0:0: [sda] No Caching mode page found
    [ 1030.546595] sd 1:0:0:0: [sda] Assuming drive cache: write through
    [ 1030.550462]  sda: sda1
    [ 1030.553978] sd 1:0:0:0: [sda] Attached SCSI removable disk
    [ 1030.778434] FAT-fs (sda1): utf8 is not a recommended IO charset for FAT filesystems, filesystem will be case sensitive!
    [ 1030.782177] FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

2. Unplug the USB device from the baseboard. The system will output information similar to the following:

.. code-block:: shell

    [ 1066.341847] usb 2-1.1: USB disconnect, device number 4


SD Interface Test
-------------------

|   Interface Silkscreen: J6
|   Test Description: Test by plugging and unplugging a TF card
|   Test Operations:

1. Install the TF card into the SD interface. The development board will output the following information:

.. code-block:: shell

    [  380.723829] dwmmc_rockchip fe2c0000.mmc: could not set regulator OCR (-22)
    [  380.723921] dwmmc_rockchip fe2c0000.mmc: failed to enable vmmc regulator
    [  380.736730] mmc_host mmc1: Bus speed (slot 0) = 400000Hz (slot req 400000Hz, actual 400000HZ div = 0)
    [  380.892477] mmc_host mmc1: Bus speed (slot 0) = 49500000Hz (slot req 50000000Hz, actual 49500000HZ div = 0)
    [  380.892687] mmc1: new high speed SDHC card at address 0001
    [  380.894512] mmcblk1: mmc1:0001 TF 4G 3.68 GiB 
    [  380.896321]  mmcblk1: p1
    [  381.134266] FAT-fs (mmcblk1p1): utf8 is not a recommended IO charset for FAT filesystems, filesystem will be case sensitive!
    [  381.140831] FAT-fs (mmcblk1p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|   Result: The output information after the operation meets the correct expectations, indicating that the TF card is correctly recognized.

2. Pull out the TF card, and the output information is as follows:

.. code-block:: shell

    [  376.270975] mmc1: card 0001 removed


Audio Playback Test
---------------------

|   Interface Silkscreen: J16
|   Test Description: Play an audio file to verify the audio playback function of the evaluation board
|   Test Operations

1. Connect headphones to the interface corresponding to the silkscreen
2. Enter the following command for testing:

|   Check the rockchipes8388 sound card and its number

.. code-block:: shell

    aplay -l

|   Specify the playback device, hw:card number, device number

.. code-block:: shell

    aplay -D hw:2,0 test_app/music_test.wav

|   The following information will be output

.. code-block:: shell

    Playing WAVE '/test_app/music_test.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

|   Audio output from the headphones indicates that the audio playback test passed

Recording Test
----------------

|   Recording Test
|   Interface Silkscreen: J15
|   Test Description: Test by recording and playing back the recorded file
|   Test Operations

1. Insert a headphone with a MIC into the interface corresponding to the silkscreen
2. Enter the following command to record for 10 seconds:

.. code-block:: shell

    arecord -d 10 -f cd -r 44100 -c 2 -t wav record.wav

3. Connect headphones or speakers to the interface corresponding to silkscreen J16 to play the recorded audio file, and enter the following command:

.. code-block:: shell

    aplay record.wav

|   The recorded sound output from the headphones or speakers indicates that the recording test passed


Wifi Test
-----------

|   Interface Silkscreen: U19
|   Test Description: After WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal
|   Test Operations:

1. Connect the WIFI antenna to the "U19" interface
2. Generate the WPA PSK file for the SSID

.. code-block:: shell

    wpa_passphrase command format: wpa_passphrase + wifi name + wifi password > /etc/wpa_supplicant.conf

|   Enter the command as follows:

.. code-block:: shell

    wpa_passphrase MY-WIFI My202412 > /etc/wpa_supplicant.conf

3. Connect, enter the command as follows:

.. code-block:: shell

    wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

|   Output information:

.. code-block:: shell

    Successfully initialized wpa_supplicant
    nl80211: kernel reports: Authentication algorithm number required
    [  266.744713] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready

4. Obtain an IP, enter the command as follows:

.. code-block:: shell

    udhcpc -i wlan0

|   Output information:

.. code-block:: shell

    udhcpc: started, v1.36.0
    udhcpc: broadcasting discover
    udhcpc: broadcasting select for 192.168.61.187, server 192.168.60.1
    udhcpc: lease of 192.168.61.187 obtained from 192.168.60.1, lease time 86400
    deleting routers
    adding dns 192.168.60.1

5. Test the connection, enter the command as follows:

.. code-block:: shell

    ping -I wlan0 www.baidu.com -c 3

|   Output information:

.. code-block:: shell

    PING www.a.shifen.com (183.2.172.177) from 192.168.61.187 wlan0: 56(84) bytes of data.
    64 bytes from 183.2.172.177 (183.2.172.177): icmp_seq=1 ttl=54 time=11.2 ms
    64 bytes from 183.2.172.177 (183.2.172.177): icmp_seq=2 ttl=54 time=13.8 ms
    64 bytes from 183.2.172.177 (183.2.172.177): icmp_seq=3 ttl=54 time=14.1 ms

    --- www.a.shifen.com ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2003ms
    rtt min/avg/max/mdev = 11.158/13.029/14.104/1.328 ms

|   Result: "0% packet loss" indicates that the wifi connection is normal

Bluetooth Test
----------------

|   Interface Silkscreen: U19
|   Test Description: After scanning for Bluetooth devices, send an L2CAP echo request and receive a response
|   Test Operations:

1. Connect the antenna to the "U19" interface
2. Start Bluetooth, enter the command as follows:

.. code-block:: shell

    hciconfig hci0 up

3. Scan for external Bluetooth devices, enter the command as follows:

.. code-block:: shell

    hcitool scan

|   Output:

.. code-block:: shell

    [  679.593805] rtk_btcoex: inquiry complete
            D0:57:7E:BF:9B:44        SZ-L0648
            10:38:1F:5C:61:9D        n/a
            7C:21:4A:C7:A2:21        PFBYRXUIAKYSFRJ
            74:B5:87:DB:09:7A        chensz

|   Obtain the output information. The required information is similar to "        74:B5:87:DB:09:7A        chensz"

4. Send an L2CAP packet test, enter the command as follows:

.. code-block:: shell

    l2ping 74:B5:87:DB:09:7A

|   Output information:

.. code-block:: shell

    root@root:/# l2ping 74:B5:87:DB:09:7A
    Ping: 74:B5:87:DB:09:7A from C8:FE:0F:02:26:03 (data size 44) ...
    0 bytes from 74:B5:87:DB:09:7A id 0 time 7.54ms
    0 bytes from 74:B5:87:DB:09:7A id 1 time 14.19ms
    0 bytes from 74:B5:87:DB:09:7A id 2 time 142.73ms
    0 bytes from 74:B5:87