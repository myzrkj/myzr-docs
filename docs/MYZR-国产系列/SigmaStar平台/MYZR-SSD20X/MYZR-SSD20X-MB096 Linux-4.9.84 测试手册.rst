MYZR-SSD20X-MB096 Linux-4.9.84 测试手册
=========================================

SPI测试
--------

|  【测试说明】：通过spidev_test程序进行自收发
|  【系统设备】：/dev/spidev0.0
|  【接口标识】：SPI_MOSI ,SPI_CLK

**测试操作**

|  1. 杜邦线短接P8-3,P8-4管脚
|  2. 使用spi测试程序进行数据收发：

.. code:: shell

   /opt/spidev_test.out -D /dev/spidev0.0

|  输出

.. code:: shell

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

I2C测试
---------

|  【测试说明】：RTC挂接在I2c1中，触摸挂接在I2C0中

.. code:: shell

   i2cdetect -y 1

|  输出以下：（UU表示芯片的驱动已经注册到内核里面）

.. code:: shell

   60: 60 61 62 63 64 65 66 67 68 69 6a 6b 6c 6d 6e UU

GPIO测试
----------

|  【测试说明】：通过控制gpio口输出高低电平来查看电压大小
|  【接口标识】：PAD_GPIO86--gpio86，PAD_GPIO12--gpio12，PAD_GPIO13--gpio13，PAD_GPIO14--gpio14，PAD_GPIO90--gpio90，PAD_GPIO47--gpio47，PAD_GPIO48--gpio48

**测试操作**

.. code:: shell

   echo 86 > /sys/class/gpio/export //导出gpio86
   echo out > /sys/class/gpio/gpio86/direction //将管脚配置为输出
   echo 1 > /sys/class/gpio/gpio86/value //输出高电平
   echo 0 > /sys/class/gpio/gpio86/value //输出低电平

ADC测试
--------

|  【测试说明】：通过调节adc引脚电压来读取adc对应值
|  【接口标识】：PAD_SAR_GPIO0 =0，PAD_SAR_GPIO2 = 2
|  【系统设备】：/dev/sar

**测试操作**

|  运行sar0_test.out或sar2_test.out测试程序

.. code:: shell

   /opt/sar0_test.out

|  输出

.. code:: shell

   SAR: get value 952SAR: get value 953SAR: get value 952SAR: get value 953SAR: get value 954SAR: get value 953SAR: get value 953SAR: get value 953SAR: get value 953SAR: get value 953

wifi—client测试
-----------------

|  【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：WIFI&BT，WIFI_ANT
|  【接口丝印】：U15，E1
|  【系统设备】：wlan0

**测试操作**

1. 把wifi天线连接到“E1”接口上
2. 生成 SSID 的 WPA PSK 文件

|  命令格式 : wpa_passphrase [passphrase]

.. code:: shell

   wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf

3. 连接

.. code:: shell

   /config/wifi/wpa_supplicant -Dnl80211 -i wlan0 -B -c /etc/wpa_supplicant.conf

4. 获取IP

.. code:: shell

   udhcpc -i wlan0

5. 测试连接

.. code:: shell

   ping -I wlan0 www.baidu.com -c 2 -w 4

**测试结果**

|  “0% packet loss”表示WIFI连接正常

蓝牙测试
---------

|  【测试说明】：扫描到蓝牙设备。
|  【接口标识】：WIFI&BT，WIFI_ANT
|  【接口丝印】：U15，E1
|  【系统设备】：hci0

**测试操作**

1. 把蓝牙天线连接到“E1”接口上

.. code:: shell

   # 输入以下命令：
   # hciconfig hci0 up
   # hciconfig
   # 输出以下信息：
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

2. 扫描蓝牙设备

.. code:: shell

   # 输入以下信息：
   # hcitool scan
   # 输出以下信息：
   root@myzr:/opt3 hcitool scan
   Scanning ...rtk_btcoex: hci (periodic)inq, notify wifi inquiry start
   rtk_btcoex: inq complete, notify wifi inquiry end
   1C:D1:07:D7:65:EC 真我GT Neo 闪速版

**测试结果**

|  能扫描到其他设备，代表蓝牙正常。

4G测试
--------

|  【测试说明】：4G连接成功后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：4G(移远EC20)
|  【接口丝印】：P10
|  【系统设备】：usb0

**测试操作**

1. 开发板断电，接上4G模块，接上天线并插入SIM卡后启动评估板。
2. 使用指令进行网络连接：

.. code:: shell

   udhcpc -i usb0

3. 测试连接

.. code:: shell

   ping -I usb0 www.baidu.com

RS232测试
-----------

|  【测试说明】：采用串口自发自收的方式进行测试。
|  【接口标识】：RS232
|  【接口丝印】：P6
|  【系统设备】：ttyS1

**测试操作**

1. 杜邦线短接P6 rx和tx
2. 输入指令

.. code:: shell

   chmod +x /usr/bin/serial_test
   serial_test /dev/ttyS1 "myzr"

3. 输出信息

.. code:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d Character: m
   ASCII: 0x79 Character: y
   ASCII: 0x7a Character: z
   ASCII: 0x72 Character: r
   ASCII: 0x0 Character:

**测试结果**

|  执行测试指令后，应用输出如上类似信息即正常。（按 ctrl+c 退出程序）

RS485测试
----------

|  【测试说明】：RS485与电脑串口助手进行通信
|  【接口标识】：RS485
|  【接口丝印】：P7
|  【系统设备】：ttyS3

**测试操作**

1. 使用RS232转RS485转换模块连接电脑和板子的P7 A2 B2管脚
2. 输入指令向电脑串口助手发送信息

.. code:: shell

   stty -F /dev/ttyS2 speed 115200
   echo myzr > /dev/ttyS2

3. 输出信息

.. code:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d Character: m
   ASCII: 0x79 Character: y
   ASCII: 0x7a Character: z
   ASCII: 0x72 Character: r
   ASCII: 0x0 Character:

**测试结果**

|  执行测试指令后，应用输出如上类似信息即正常。（按 ctrl+c 退出程序）

SD测试
--------

|  【测试说明】：采用插入并识别TF卡的方式进行测试。
|  【接口标识】：SD
|  【接口丝印】：P3
|  【系统设备】：mmcblk0

**测试操作**

1. 开发板供电，把TF卡安装到SD接口
2. 查看内核中驱动输出信息
3. 挂载SD卡

.. code:: shell

   mount /dev/mmcblk0p1 /mnt/df

4. 输出信息

.. code:: shell

   #插上SD卡，出现以下信息
   mmc0: new high speed SDHC card at address 5048
   mmcblk0: mmc0:5048 SD16G 14.4 GiB
   mmcblk0: p1
   #输入命令，出现以下信息
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

**测试结果**

|  SD存储设备插拔时系统输出如上类似信息即表示正常。

RTC测试
---------

|  【测试说明】：RS485与电脑串口助手进行通信。
|  【接口标识】：RTC_Battery
|  【接口丝印】：BT1
|  【系统设备】：/dev/rtc0

**测试操作**

1. 断电重启设备，查看当前系统时间和硬件时间：

.. code:: shell

   =====> Input:
   # date
   =====> Output:
   Fri Feb 7 15:51:25 UTC 2020

2. 查看当前RTC芯片时钟：

.. code:: shell

   =====> Input:
   # hwclock
   =====> Output:
   hwclock: ioctl(RTC_RD_TIME) to /dev/rtc0 to read the time failed: Invalid argument

3. 设置系统时钟：

.. code:: shell

   =====> Input:
   # date -s "2021-04-08 15:00:00"
   =====> Output:
   Thu Apr 8 15:00:00 UTC 2021

4. 将系统时钟写入硬件时钟：

.. code:: shell

   # hwclock -w

5. 断电重启开发板，查看当前系统时钟和硬件时钟：

.. code:: shell

   =====> Input:
   # date
   =====> Output:
   Thu Apr 8 15:04:49 UTC 2021
   =====> Input:
   # hwclock
   =====> Output:
   2021-04-08 15:05:09.146857+00:00

**网口测试**

|  【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|  【接口标识】：ETH10/100/1000M
|  【接口丝印】：P2,P11
|  【系统接口】：eth0,eth1

**测试操作**

1. 配置电脑有线网卡ip为 192.168.137.99
2. 网线连接板子网口eth0和电脑网口
3. 输入如下指令与电脑通讯：

.. code:: shell

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

|  “0% packet loss”表示测试通过。

4. 网线连接板子网口eth1和电脑网口
5. 输入如下指令与电脑通讯：

.. code:: shell

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

|  “0% packet loss”表示测试通过。

USB测试
---------

|  【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|  【接口标识】：USB2.0
|  【接口丝印】：P12

**测试操作**

1. 将USB设备插入底板USB接口，系统会输出类似如下信息:

.. code:: shell

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

2. 将USB设备从底板拔出，系统会输出类似如下信息：

.. code:: shell

   root@myzr:/opt12 usb 1-1.4: USB disconnect, device number 4
