.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Test Guide
==========

MicroSD 3.0 Interface
~~~~~~~~~~~~~~~~~~~~~

Verification method: Insert the TF into the SD card interface of the Development Board, and then enter the "df -h" command at the Development Board terminal to see if the storage device is added.

Test Procedure ：

.. code-block:: text

   Before inserting the TF card, enter the print information of the "df -h" command as follows:
   
   Filesystem      Size  Used Avail Use% Mounted on
   /dev/root       6.3G  3.6G  2.4G  61% /
   devtmpfs        810M  4.0K  810M   1% /dev
   tmpfs           940M     0  940M   0% /dev/shm
   tmpfs           376M  8.8M  367M   3% /run
   tmpfs           940M  8.0K  940M   1% /tmp
   tmpfs           940M  168K  939M   1% /var/volatile
   tmpfs           188M  8.0K  188M   1% /run/user/0
   /dev/mmcblk0p1  333M   39M  294M  12% /run/media/boot-mmcblk0p1

USB Test
~~~~~~~~

Verification method: 1. Insert the USB flash drive into the USB interface of Development Board, enter the "df -h" command in the Development Board terminal, and check whether the storage device is added.

2. Insert the USB flash drive into the Development Board USB interface, enter the "lsusb" command in the Development Board terminal, and check whether the USB device is added.

Test Procedure ：

.. code-block:: text

   1、
   Before inserting the USB flash drive, enter the print information of the "df -h" command as follows:
   
   Filesystem      Size  Used Avail Use% Mounted on
   /dev/root       6.3G  3.6G  2.4G  61% /
   devtmpfs        810M  4.0K  810M   1% /dev
   tmpfs           940M     0  940M   0% /dev/shm
   tmpfs           376M  8.8M  367M   3% /run
   tmpfs           940M  8.0K  940M   1% /tmp
   tmpfs           940M  168K  939M   1% /var/volatile
   tmpfs           188M  8.0K  188M   1% /run/user/0
   /dev/mmcblk0p1  333M   39M  294M  12% /run/media/boot-mmcblk0p1
   
   2、
   Before inserting the USB flash drive, enter the print information of the "lsusb" command as follows:
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
   Bus 001 Device 002: ID 1a40:0101 Terminus Technology Inc. Hub
   Bus 001 Device 003: ID 0bda:d723 Realtek Semiconductor Corp. 802.11n WLAN Adapter

Network Port Test
~~~~~~~~~~~~~~~~~

ETH0
^^^^

Verification method: Use a network cable to connect the Development Board network port to the computer's network port, and use Development Board to send a ICMP message to the PC for testing:

Test Procedure ：

.. code-block:: text

   # By default, the IP address is automatically obtained, but the test is to configure the static IP to test, the specific configuration instructions are as follows:
   
   ifconfig eth0 192.168.128.228
   
   # Enter the following command to verify the ETH0 network port:
   ping -I eth0 -c 4 8.8.8.8
   ping -I eth0 -c 4 www.baidu.com

The expected output information is as follows:

.. code-block:: text

   root@imx93evk:~# ping -I eth0 -c 4 8.8.8.8
   PING 8.8.8.8 (8.8.8.8) from 192.168.128.228 eth0: 56(84) bytes of data.
   64 bytes from 8.8.8.8: icmp_seq=1 ttl=108 time=176 ms
   64 bytes from 8.8.8.8: icmp_seq=2 ttl=108 time=176 ms
   64 bytes from 8.8.8.8: icmp_seq=3 ttl=108 time=176 ms
   64 bytes from 8.8.8.8: icmp_seq=4 ttl=108 time=176 ms
   
   --- 8.8.8.8 ping statistics ---
   4 packets transmitted, 4 received, 0% packet loss, time 3005ms
   rtt min/avg/max/mdev = 175.807/175.935/176.235/0.174 ms
   
   
   
   root@imx93evk:~# ping -I eth0 -c 4 www.baidu.com
   PING www.baidu.com (183.2.172.177) from 192.168.128.228 eth0: 56(84) bytes of data.
   64 bytes from 183.2.172.177: icmp_seq=1 ttl=54 time=8.80 ms
   64 bytes from 183.2.172.177: icmp_seq=2 ttl=54 time=8.44 ms
   64 bytes from 183.2.172.177: icmp_seq=3 ttl=54 time=8.42 ms
   64 bytes from 183.2.172.177: icmp_seq=4 ttl=54 time=8.52 ms
   
   --- www.baidu.com ping statistics ---
   4 packets transmitted, 4 received, 0% packet loss, time 3003ms
   rtt min/avg/max/mdev = 8.424/8.546/8.799/0.150 ms
   root@imx93evk:~#

ETH1
^^^^

Verification method: Use a network cable to connect the Development Board network port to the computer's network port, and use Development Board to send a ICMP message to the PC for testing:

Test Procedure ：

.. code-block:: text

   ## Obtain an IP address automatically by default, but the test is to configure a static IP to test, the specific configuration instructions are as follows:
   
   ifconfig eth1 192.168.128.229
   
   ## Enter the following command to verify the ETH1 network port:
   ping -I eth1 -c 4 8.8.8.8
   ping -I eth1 -c 4 www.baidu.com

The expected output information is as follows:

.. code-block:: text

   root@imx93evk:~# ping -I eth1 -c 4 8.8.8.8
   PING 8.8.8.8 (8.8.8.8) from 192.168.128.229 eth1: 56(84) bytes of data.
   64 bytes from 8.8.8.8: icmp_seq=1 ttl=108 time=176 ms
   64 bytes from 8.8.8.8: icmp_seq=2 ttl=108 time=176 ms
   64 bytes from 8.8.8.8: icmp_seq=3 ttl=108 time=176 ms
   64 bytes from 8.8.8.8: icmp_seq=4 ttl=108 time=176 ms
   
   --- 8.8.8.8 ping statistics ---
   4 packets transmitted, 4 received, 0% packet loss, time 3005ms
   rtt min/avg/max/mdev = 175.807/175.935/176.235/0.174 ms
   
   
   
   root@imx93evk:~# ping -I eth1 -c 4 www.baidu.com
   PING www.baidu.com (183.2.172.177) from 192.168.128.229 eth1: 56(84) bytes of data.
   64 bytes from 183.2.172.177: icmp_seq=1 ttl=54 time=8.80 ms
   64 bytes from 183.2.172.177: icmp_seq=2 ttl=54 time=8.44 ms
   64 bytes from 183.2.172.177: icmp_seq=3 ttl=54 time=8.42 ms
   64 bytes from 183.2.172.177: icmp_seq=4 ttl=54 time=8.52 ms
   
   --- www.baidu.com ping statistics ---
   4 packets transmitted, 4 received, 0% packet loss, time 3003ms
   rtt min/avg/max/mdev = 8.424/8.546/8.799/0.150 ms
   root@imx93evk:~#

WIFI Test
~~~~~~~~~

Verification method: After WIFI is connected to the AP, Development Board sends a ICMP message to the external network to verify that the connection is normal.

Test Procedure ：

.. code-block:: text

   ## Enter the following command to write the WiFi name and password to the /etc/wpa_supplicant.conf file
   wpa_passphrase realme fgew5678 > /etc/wpa_supplicant.conf
   ## Enter a command to connect to wifi
   ifconfig wlan0 up
   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
   #Obtain IP address automatically
   udhcpc -i wlan0
   ## Enter the following command to verify the WiFi:
   ping -I eth1 -c 4 8.8.8.8
   ping -I eth1 -c 4 www.baidu.com

The expected output information is as follows:

.. code-block:: text

   root@imx93evk:~# wpa_passphrase realme fgew5678 > /etc/wpa_supplicant.conf
   root@imx93evk:~#
   root@imx93evk:~# wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
   Successfully initialized wpa_supplicant
   rfkill: Cannot open RFKILL control device
   
   root@imx93evk:~# udhcpc -i wlan0
   udhcpc: started, v1.36.1
   Dropped protocol specifier '.udhcpc' from 'wlan0.udhcpc'. Using 'wlan0' (ifindex=4).
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 10.192.95.113, server 10.192.95.197
   udhcpc: lease of 10.192.95.113 obtained from 10.192.95.197, lease time 3599
   /etc/udhcpc.d/50default: Adding DNS 10.192.95.197
   Dropped protocol specifier '.udhcpc' from 'wlan0.udhcpc'. Using 'wlan0' (ifindex=4).
   
   root@imx93evk:~# ping -I wlan0 -c 4 8.8.8.8
   PING 8.8.8.8 (8.8.8.8) from 10.192.95.113 wlan0: 56(84) bytes of data.
   64 bytes from 8.8.8.8: icmp_seq=1 ttl=107 time=226 ms
   64 bytes from 8.8.8.8: icmp_seq=2 ttl=107 time=217 ms
   64 bytes from 8.8.8.8: icmp_seq=3 ttl=107 time=189 ms
   64 bytes from 8.8.8.8: icmp_seq=4 ttl=107 time=220 ms
   
   --- 8.8.8.8 ping statistics ---
   4 packets transmitted, 4 received, 0% packet loss, time 3005ms
   rtt min/avg/max/mdev = 189.266/212.935/225.702/14.037 ms
   
   root@imx93evk:~# ping -I wlan0 -c 4 www.baidu.com
   PING www.a.shifen.com (183.2.172.177) from 10.192.95.113 wlan0: 56(84) bytes of data.
   64 bytes from 183.2.172.177: icmp_seq=1 ttl=52 time=60.7 ms
   64 bytes from 183.2.172.177: icmp_seq=2 ttl=52 time=21.8 ms
   64 bytes from 183.2.172.177: icmp_seq=3 ttl=52 time=23.8 ms
   64 bytes from 183.2.172.177: icmp_seq=4 ttl=52 time=16.5 ms
   
   --- www.a.shifen.com ping statistics ---
   4 packets transmitted, 4 received, 0% packet loss, time 3005ms
   rtt min/avg/max/mdev = 16.492/30.700/60.653/17.500 ms
   root@imx93evk:~#

If the following information is printed when pinging the URL:

.. code-block:: text

   ping: www.baidu.com: Temporary failure in name resolution

Indicates that the DNS needs to be configured. After the Development Board terminal enters the following command, you can try again:

.. code-block:: text

   printf '%s\n' \
   'nameserver 10.192.95.197' \
   'nameserver 8.8.8.8' > /etc/resolv.conf

Bluetooth Test
~~~~~~~~~~~~~~

Authentication method: After scanning to a Bluetooth device, send a L2CAP echo request and receive an answer

Test Procedure ：

Enter the command to start Bluetooth:

.. code-block:: text

   hciconfig hci0 up

Enter the command to scan for external Bluetooth devices:

.. code-block:: text

   hcitool scan

The following types of information are expected to be printed:

.. code-block:: text

   Scanning ...
   E4:33:AE:6D:77:96        n/a
   DC:0D:30:5C:4C:93        XP-236B-L

Enter the command to send the L2CAP package test:

.. code-block:: text

   l2ping DC:0D:30:5C:4C:93

Output the following information:

.. code-block:: text

   Ping: DC:0D: 30:5C:4C: 93 from 94:BA:06: 78:1B:33 (data size 44) ...
   0 bytes from DC:0D: 30:5C:4C: 93 id 0 time 3.89ms
   0 bytes from DC:0D: 30:5C:4C: 93 id 1 time 24.91 ms
   0 bytes from DC:0D: 30:5C:4C: 93 id 2 time 48.93 ms
   0 bytes from DC:0D: 30:5C:4C: 93 id 3 time 37.43 ms
   0 bytes from DC:0D: 30:5C:4C: 93 id 4 time 27.48 ms
   5 sent, 5 received, 0% loss

MIPI_CSI Test
~~~~~~~~~~~~~

Verification method: Call the camera and show the screen

Test Procedure ：

Enter the command to call the camera:

.. code-block:: text

   XDG_RUNTIME_DIR=/run/user/0 WAYLAND_DISPLAY=wayland-1 gst-launch-1.0 -v v4l2src device=/dev/video2 io-mode=mmap ! 'video/x-raw,format=YUY2,width=1024,height=768,framerate=30/1' ! queue leaky=downstream max-size-buffers=2 ! videoconvert n-threads=2 ! 'video/x-raw,format=RGBx,width=1024,height=768' ! imxvideoconvert_g2d qos=true ! 'video/x-raw,format=RGBx,width=800,height=600' ! waylandsink sync=false

