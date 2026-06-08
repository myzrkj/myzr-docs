MYZR-SSD20X-MB096 Linux-4.9.84 Test Manual
=============================================

SPI Testing
--------------

|  【Test Instruction】：Self-transceiver through spidev_test program
|  【System device】：/dev/spidev0.0
|  【Interface ID】：SPI_MOSI ,SPI_CLK

**Test operation**

1. DuPont line shorts P8-3, P8-4 pins
2. Use the spi test program to send and receive data：

.. code-block:: shell

   /opt/spidev_test.out -D /dev/spidev0.0

|  输出

.. code-block:: shell

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

IC2 Testing
-------------

|  【Test Instruction】：RTC is hooked up in I2C1, and touch is hooked up in I2C0

.. code-block:: shell

   i2cdetect -y 1

|  The output is as follows: (UU indicates that the driver of the chip has been registered in the kernel)

.. code-block:: shell

   60: 60 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e UU

GPIO Testing
--------------

|  【Test Instruction】：Check the voltage by controlling the output high and low levels of the gpio port
|  【Interface ID】：PAD_GPIO86--gpio86，PAD_GPIO12--gpio12，PAD_GPIO13--gpio13，PAD_GPIO14--gpio14，PAD_GPIO90--gpio90，PAD_GPIO47--gpio47，PAD_GPIO48--gpio48

**Test operation**

.. code-block:: shell

   echo 86 > /sys/class/gpio/export //导出gpio86
   echo out > /sys/class/gpio/gpio86/direction //将管脚配置为输出
   echo 1 > /sys/class/gpio/gpio86/value //输出高电平
   echo 0 > /sys/class/gpio/gpio86/value //输出低电平

ADC Testing
-------------

|  【Test Instruction】：Read the corresponding value of adc by adjusting the voltage of the adc pin
|  【Interface ID】：PAD_SAR_GPIO0 =0，PAD_SAR_GPIO2 = 2
|  【System device】：/dev/sar

**Test operation**

|  Run the sar0_test.out or sar2_test.out test program

.. code-block:: shell

   /opt/sar0_test.out

|  Output

.. code-block:: shell

   SAR: get value 952SAR: get value 953SAR: get value 952SAR: get value 953SAR: get value 954SAR: get value 953SAR: get value 953SAR: get value 953SAR: get value 953SAR: get value 953

wifi—client Testing
----------------------

|  【Test Instruction】：After the WIFI is connected to the AP, the development board sends an ICMP message to the external network to verify that the connection is normal.
|  【Interface ID】：WIFI&BT，WIFI_ANT
|  【Interface silkscreen】：U15，E1
|  【System device】：wlan0

**Test operation**

1. Connect the wifi antenna to the "E1" port
2. Generate WPA PSK file for SSID

|  Command format : wpa_passphrase [passphrase]

.. code-block:: shell

   wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf

3. Connection

.. code-block:: shell

   /config/wifi/wpa_supplicant -Dnl80211 -i wlan0 -B -c /etc/wpa_supplicant.conf

4. Get IP

.. code-block:: shell

   udhcpc -i wlan0

5. Test connection

.. code-block:: shell

   ping -I wlan0 www.baidu.com -c 2 -w 4

**Test Result**

|  "0% packet loss" means the WIFI connection is normal

Bluetooth Testing
-------------------

|  【Test Instruction】：Scan to bluetooth device.
|  【Interface ID】：WIFI&BT，WIFI_ANT
|  【Interface silkscreen】：U15，E1
|  【System device】：hci0

**Test operation**

1. Connect the bluetooth antenna to the "E1" interface

.. code-block:: shell

   # Input the following command：
   # hciconfig hci0 up
   # hciconfig
   # Output the following information：
   root@myzr:/opt1 hciconfig hci0 up
   rtk_btusb: btusb_open start pm_usage_cnt(0x0)
   rtk_btusb: btusb_open hdev->promisc ==0
   rtk_btusb: download_patch start
   rtk_btusb: chip type value: 0x71
   rtk_btusb: HCI reset.
   rtk_btusb: read_ver_rsp->lmp_subver = 0x7e1b
   rtk_btusb: read_ver_rsp->hci_rev = 0x8289
   rtk_btusb: patch_entry->lmp_sub = 0x8723
   rtk_btusb: Firmware already exists
   rtk_btusb: Rtk patch end 1
   rtk_btusb: btusb_open set HCI_RUNNING
   rtk_btcoex: Open BTCOEX
   rtk_btcoex: create_udpsocket: connect_port: 30001
   rtk_btcoex: send msg INVITE_REQ with len:11
   rtk_btusb: btusb_open end pm_usage_cnt(0x0)
   rtk_btcoex: BTCOEX hci_rev 0x8289
   rtk_btcoex: BTCOEX lmp_subver 0x7e1b
   root@myzr:/opt2 hciconfig
   hci0: Type: Primary Bus: USB
   BD Address: 0C:CF:89:72:4E:1F ACL MTU: 1021:8 SCO MTU: 255:12
   UP RUNNING
   RX bytes:1168 acl:0 sco:0 events:60 errors:0
   TX bytes:738 acl:0 sco:0 commands:60 errors:0

2. Scan for bluetooth devices

.. code-block:: shell

   # 输入以下信息：
   # hcitool scan
   # 输出以下信息：
   root@myzr:/opt3 hcitool scan
   Scanning ...rtk_btcoex: hci (periodic)inq, notify wifi inquiry start
   rtk_btcoex: inq complete, notify wifi inquiry end
   1C:D1:07:D7:65:EC 真我GT Neo 闪速版

**Test Result**

|  If other devices can be scanned, it means that the Bluetooth is normal.

4G Testing
------------

|  【Test Instruction】：After the 4G connection is successful, the development board sends an ICMP message to the external network to verify that the connection is normal.
|  【Interface ID】：4G (Quectel EC20)
|  【Interface silkscreen】：P10
|  【System device】：usb0

**Test operation**

1. Power off the development board, connect the 4G module, connect the antenna and insert the SIM card to start the evaluation board.
2. Network connection using commands：

.. code-block:: shell

   udhcpc -i usb0

3. Test connection

.. code-block:: shell

   ping -I usb0 www.baidu.com

RS232 Testing
---------------

|  【Test Instruction】：The serial port is used for testing in the way of self-transmitting and self-receiving.
|  【Interface ID】：RS232
|  【Interface silkscreen】：P6
|  【System device】：ttyS1

**Test operation**

1. Dupont wire shorted to P6 rx and tx
2. Input command

.. code-block:: shell

   chmod +x /usr/bin/serial_test
   serial_test /dev/ttyS1 "myzr"

3. Output information

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d Character: m
   ASCII: 0x79 Character: y
   ASCII: 0x7a Character: z
   ASCII: 0x72 Character: r
   ASCII: 0x0 Character:

**Test Result**

|  After executing the test command, the application output similar information as above is normal. (press ctrl+c to exit the program)

RS485 Testing
---------------

|  【Test Instruction】：RS485 communicates with computer serial assistant
|  【Interface ID】：RS485
|  【Interface silkscreen】：P7
|  【System device】：ttyS3

**Test operation**

1. Use the RS232 to RS485 conversion module to connect the P7 A2 B2 pins of the computer and the board
2. Enter the command to send information to the computer serial assistant

.. code-block:: shell

   stty -F /dev/ttyS2 speed 115200
   echo myzr > /dev/ttyS2

3. Output information

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d Character: m
   ASCII: 0x79 Character: y
   ASCII: 0x7a Character: z
   ASCII: 0x72 Character: r
   ASCII: 0x0 Character:

**Test Result**

|  After executing the test command, the application output similar information as above is normal. (press ctrl+c to exit the program)

SD Testing
------------

|  【Test Instruction】：Test by inserting and identifying the TF card.
|  【Interface ID】：SD
|  【Interface silkscreen】：P3
|  【System device】：mmcblk0

**Test operation**

|  1.Power on the development board, install the TF card to the SD interface
|  2.View driver output information in the kernel
|  3.Mount SD card

.. code-block:: shell

   mount /dev/mmcblk0p1 /mnt/df

4. Output information

.. code-block:: shell

   #Insert the SD card, the following message appears:
   mmc0: new high speed SDHC card at address 5048
   mmcblk0: mmc0:5048 SD16G 14.4 GiB
   mmcblk0: p1
   #Input the command and the following message appears:
   root@myzr:/opt52 mount /dev/mmcblk0p1 /mnt/
   FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt.
   Please run fsck.
   root@myzr:/opt53 ls /mnt/
   system~1
   root@myzr:/opt54 df
   Filesystem 1K-blocks Used Available Use% Mounted on
   ubi:rootfs 76724 12856 63868 17% /
   devtmpfs 47564 0 47564 0% /dev
   tmpfs 48588 0 48588 0% /dev/shm
   tmpfs 48588 4 48584 0% /tmp
   tmpfs 48588 28 48560 0% /run
   vendor 48588 0 48588 0% /vendor
   ubi0:miservice 7680 5672 2008 74% /config
   ubi0:customer 2980 160 2820 5% /customer
   ubi0:appconfigs 2980 24 2956 1% /appconfigs
   /dev/mmcblk0p1 15118336 128 15118208 0% /mnt
   root@myzr:/opt55 umount /mnt/
   root@myzr:/opt56 mmc0: card 5048 removed

**Test Result**

|  When the SD storage device is inserted or removed, the system outputs similar information as above, which means it is normal.

RTC Testing
-------------

|  【Test Instruction】：RS485 communicates with the computer serial assistant.
|  【Interface ID】：RTC_Battery
|  【Interface silkscreen】：BT1
|  【System device】：/dev/rtc0

**Test operation**

1. Power off and restart the device to check the current system time and hardware time:

.. code-block:: shell

   =====> Input:
   # date
   =====> Output:
   Fri Feb 7 15:51:25 UTC 2020

2. Check the current RTC chip clock:

.. code-block:: shell

   =====> Input:
   # hwclock
   =====> Output:
   hwclock: ioctl(RTC_RD_TIME) to /dev/rtc0 to read the time failed: Invalid argument

3. Set the system clock:

.. code-block:: shell

   =====> Input:
   # date -s "2021-04-08 15:00:00"
   =====> Output:
   Thu Apr 8 15:00:00 UTC 2021

4. Write the system clock to the hardware clock:

.. code-block:: shell

   # hwclock -w

5. Power off and restart the development board to view the current system clock and hardware clock:

.. code-block:: shell

   =====> Input:
   # date
   =====> Output:
   Thu Apr 8 15:04:49 UTC 2021
   =====> Input:
   # hwclock
   =====> Output:
   2021-04-08 15:05:09.146857+00:00

Network port Testing
----------------------

|  【Test Instruction】：Use the development board to send ICMP messages to the PC for testing
|  【Interface ID】：ETH10/100/1000M
|  【Interface silkscreen】：P2,P11
|  【System interface】：eth0,eth1

**Test operation**

1. Configure the computer's wired network card ip to 192.168.137.99
2. The network cable connects the board subnet port eth0 and the computer network port
3. Enter the following command to communicate with the computer:

.. code-block:: shell

   =====> Input:
   # ifconfig eth0 192.168.137.81
   # ping 192.168.137.99
   =====> Output:
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.1: seq=0 ttl=128 time=0.586 ms
   64 bytes from 192.168.137.1: seq=1 ttl=128 time=0.417 ms
   64 bytes from 192.168.137.1: seq=2 ttl=128 time=0.523 ms

   --- 192.168.137.99 ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 0.306/0.510/0.758/0.187 ms

|  “0% packet loss”indicates that the test passed。 

4. The network cable connects the board subnet port eth1 and the computer network port
5. Enter the following command to communicate with the computer：

.. code-block:: shell

   =====> Input:
   # ifconfig eth1 192.168.137.80
   # ping 192.168.137.99
   =====> Output:
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: seq=0 ttl=128 time=0.586 ms
   64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.417 ms
   64 bytes from 192.168.137.99: seq=2 ttl=128 time=0.523 ms

   --- 192.168.137.99 ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 0.306/0.510/0.758/0.187 ms

|  “0% packet loss”indicates that the test passed。

USB Testing
-------------

|  【Test Instruction】：Test by plugging and unplugging the USB storage device (U disk)
|  【Interface ID】：USB2.0
|  【Interface silkscreen】：P12

**Test operation**

1. Insert the USB device into the USB port of the backplane, and the system will output information similar to the following:

.. code-block:: shell

   root@myzr:/opt12 usb 1-1.4: new high-speed USB device number 4 using Sstar-ehci2
   usb 1-1.4: New USB device found, idVendor=13fe, idProduct=6300
   usb 1-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=3
   usb 1-1.4: Product: U330
   usb 1-1.4: Manufacturer:
   usb 1-1.4: SerialNumber: 90000C442B2E5C08
   usb-storage 1-1.4:1.0: USB Mass Storage device detected
   scsi host0: usb-storage 1-1.4:1.0
   scsi 0:0:0:0: Direct-Access aigo U330 PMAP PQ: 0 ANSI: 6
   sd 0:0:0:0: [sda] 30924800 512-byte logical blocks: (15.8 GB/14.7 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] No Caching mode page found
   sd 0:0:0:0: [sda] Assuming drive cache: write through
   sda: sda1
   sd 0:0:0:0: [sda] Attached SCSI removable disk

2. Unplug the USB device from the baseboard, the system will output information similar to the following：

.. code-block:: shell

   root@myzr:/opt12 usb 1-1.4: USB disconnect, device number 4
