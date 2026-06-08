MYZR-RZFIVE-EK200测试手册
============================

以太网测试
------------

网口一测试
~~~~~~~~~~~~

|   【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|   【接口标识】：10M/100M/1000M Ethernet-1
|   【系统接口】：eth0

**测试操作**

|   配置电脑有线网卡IP为 192.168.137.99。
|   把开发板的这个网口用网线跟电脑网口连接起来。
|   配置开发板网口：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# ifconfig eth1 down
    root@myzr-rzfive:~# ifconfig eth0 192.168.137.81

|   测试网口：

.. code-block:: shell

    =====> 输入指令:
    ping 192.168.137.99 -c 2 -w 4 

    =====> 输出信息：
    PING 192.168.137.99 (192.168.137.99): 56 data bytes
    64 bytes from 192.168.137.99: seq=0 ttl=128 time=0.927 ms
    64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.765 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.765/0.846/0.927 ms

**测试结果**

|   “0% packet loss”表示测试通过。

网口二测试
------------

|   【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|   【接口标识】：10M/100M/1000M Ethernet-2
|   【系统接口】：eth1

**测试操作**

|   配置电脑有线网卡IP为 192.168.137.99。
|   把开发板的这个网口用网线跟电脑网口连接起来。
|   配置开发板网口：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# ifconfig eth0 down
    root@myzr-rzfive:~# ifconfig eth1 192.168.137.82

    =====> 输出信息：
    [  394.660011] RTL8211F Gigabit Ethernet 11c30000.ethernet-ffffffff:01: attached PHY driver [RTL8211F Gigabit Ethernet] (mii_bus:phy_addr=11c30000.ethernet-ffffffff:01, irq=178)
    root@myzr-rzfive:~# [  399.044603] ravb 11c30000.ethernet eth1: Link is Up - 1Gbps/Full - flow control off

|   测试网口：

.. code-block:: shell

    =====> 输入指令:
    ping 192.168.137.99 -c 2 -w 4 

    =====> 输出信息：
    PING 192.168.137.99 (192.168.137.99): 56 data bytes
    64 bytes from 192.168.137.99: seq=0 ttl=128 time=1.831 ms
    64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.610 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.610/1.220/1.831 ms

**测试结果**

|   “0% packet loss”表示测试通过。

USB接口测试
------------

|   【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|   【接口标识】：USB HOST
|   【系统接口】：/dev/sd*

**测试方法**

|   将USB设备插入底板USB接口，系统会输出类似如下信息:

.. code-block:: shell

    [  548.085779] usb 1-1.1: new high-speed USB device number 4 using ehci-platform
    [  548.762436] usb-storage 1-1.1:1.0: USB Mass Storage device detected
    [  548.781918] scsi host0: usb-storage 1-1.1:1.0
    [  551.099373] scsi 0:0:0:0: Direct-Access              aigo U330        PMAP PQ: 0 ANSI: 6
    [  551.115142] sd 0:0:0:0: [sda] 30924800 512-byte logical blocks: (15.8 GB/14.7 GiB)
    [  551.130652] sd 0:0:0:0: [sda] Write Protect is off
    [  551.143403] sd 0:0:0:0: [sda] No Caching mode page found
    [  551.157939] sd 0:0:0:0: [sda] Assuming drive cache: write through
    [  551.214240]  sda: sda1
    [  551.229828] sd 0:0:0:0: [sda] Attached SCSI removable disk

|   将USB设备从底板拔出，系统会输出类似如下信息：

.. code-block:: shell

    [  582.421825] usb 1-1.1: USB disconnect, device number 4

**测试结果**

|   USB存储设备插拔时系统输出如上类似信息即表示正常。

SD卡接口测试
--------------

|   【测试说明】：采用插入并识别TF卡的方式进行测试
|   【接口标识】：SD3
|   【系统接口】：/dev/mmcblk1

**测试方法**

|   把SD卡插入到这个接口：

.. code-block:: shell

    =====> 输出信息：
    [   28.038307] mmc1: new high speed SDHC card at address 0001
    [   28.050565] mmcblk1: mmc1:0001 TF 4G 3.68 GiB 
    [   28.061692]  mmcblk1: p1 p2

|   弹出SD卡：

.. code-block:: shell

    =====> 输出信息：
    [  164.986044] mmc1: card 0001 removed

**测试结果**

|   SD存储设备插拔时系统输出如上类似信息即表示正常。

标准GPIO测试
--------------

|   【测试说明】：控制GPIO的输出电平
|   【接口标识】：GPIO/SD2
|   【系统接口】：/sys/class/gpio/

**MYZR-RZFIVE-MB200可用的IO**

.. code-block:: shell

    GPIO6_0(408),  GPIO11_0(448),  GPIO11_1(449), GPIO11_3(451),   GPIO13_0(464),   GPIO13_2(466)， GPIO13_4(468), GPIO0_3(363), GPIO10_1(441)

|   管脚计算公式： **GPIO_ID = GPIO_port * 8 + GPIO_pin + 360.**

**GPIO输出低电平测试**

|   配置GPIO11_0为输出低电平的操作方法：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# OUT_IO_OUT_NUM=448
    root@myzr-rzfive:~# echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
    root@myzr-rzfive:~# echo "out" > /sys/class/gpio/P11_0/direction  
    root@myzr-rzfive:~# echo 0 > /sys/class/gpio/P11_0/value 

|   用万用表测试管脚GPIO11_0，电压为0V，则表示OK

**GPIO输出高电平测试**

|   配置GPIO11_0为输出高电平的操作方法：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# OUT_IO_OUT_NUM=448
    root@myzr-rzfive:~# echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
    root@myzr-rzfive:~# echo "out" > /sys/class/gpio/P11_0/direction  
    root@myzr-rzfive:~# echo 1 > /sys/class/gpio/P11_0/value 

|   用万用表测试管脚GPIO11_0，电压为3.3V，则表示OK

**GPIO输入测试**

|   控制 GPIO 输入测试：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# OUT_IO_OUT_NUM=448
    root@myzr-rzfive:~# echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
    root@myzr-rzfive:~# echo "in" > /sys/class/gpio/P11_0/direction  
    root@myzr-rzfive:~# cat /sys/class/gpio/P11_0/value   

UART串口测试
-------------

|   【测试说明】：采用串口自发自收的方式进行测试
|   【接口标识】：TX0/1/3/4，RX0/1/3/4
|   【系统设备】：/dev/ttySC0/1/3/4

**测试操作**

|   以串口3为例，短接串口3的发送发接收管脚（P2的8和10号管脚）
|    执行测试指令：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:/# /my-demo/serial_test.out /dev/ttySC3 "www.myzr.com.cn" 

    =====> 输出信息：
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
    ASCII: 0x0   Character:  

**测试结果**

|   执行测试指令后，应用输出如上类似信息即正常。

SPI测试
---------

|   【测试说明】：采用自发自收的方式测试。
|   【接口标识】：SPI1
|   【系统设备】：/dev/spidev1.0

**测试操作**

|   短接U18的2和5管脚。 执行测试指令：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# /my-demo/spidev_test.out -D /dev/spidev1.0  

    =====> 输出信息：
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

**测试结果**

|   执行测试指令后，应用输出如上类似信息即正常。

Watchdog 超时复位测试
-----------------------

|   【测试说明】：开启看门狗，并等待看门狗超时，产生复位。
|   【接口标识】：无
|   【系统设备】：/dev/watchdog0

**测试操作**

|   运行看门狗程序：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# /my-demo/wdt_driver_test.out 10 15 1 
    
    =====> 输出信息：
    Starting wdt_driver (timeout: 10, sleep: 15, test: write)
    Trying to set timeout value=10 seconds
    The actual timeout was set to 10 seconds
    Now reading back -- The timeout is 10 seconds

**测试结果**

|   运行测试命令10秒后，WatchDog超时，系统被复位。会在终端看到系统重新启动输出的信息类似如下：

.. code-block:: shell

    U-Boot SPL 2020.10 (Jan 11 2023 - 03:22:42 +0000)
    Trying to boot from MMC1
    board_mmc_init
    þ
    
    U-Boot 2020.10 (Jan 11 2023 - 03:22:42 +0000)
    
    CPU:   rv64imafdc
    Model: myzr-rzfive
    DRAM:  dram_init

Watchdog 喂狗测试
-------------------

|   【测试说明】：开启看门狗，并使应用程序喂狗。
|   【接口标识】：无
|   【系统设备】：/dev/watchdog0

**测试操作**

|   运行看门狗程序，并设置超时时间为4秒，喂狗间隔时间为2秒：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# /my-demo/wdt_driver_test.out 4 2 1 &  
    
    =====> 输出信息：
    [1] 206
    Starting wdt_driver (timeout: 4, sleep: 2, test: write)
    Trying to set timeout value=4 seconds
    The actual timeout was set to 4 seconds
    Now reading back -- The timeout is 4 seconds

RTC测试
---------

|   【测试说明】：读取并设置时间，断电重启后检查时间是否正确
|   【接口标识】：无
|   【系统设备】：/dev/rtc0

**测试操作**

1. 断电重启设备，查看当前系统时间和硬件时间：

.. code-block:: shell

    =====> 输入指令: 
    root@myzr-rzfive:~# date

    =====> 输出信息：
    Fri Dec 16 05:41:21 UTC 2022

2. 查看当前RTC芯片时钟：

.. code-block:: shell

    =====> 输入指令: 
    root@myzr-rzfive:~# date -s "2023-01-14 12:34:56"

    =====> 输出信息：
    hwclock: ioctl(RTC_RD_TIME) to /dev/rtc0 to read the time failed: Invalid argument

3. 设置系统时钟，并同步到RTC芯片

.. code-block:: shell

    =====> 输入指令: 
    date -s "2023-01-14 12:34:56"  

    =====> 输出信息：
    Sat Jan 14 12:34:56 UTC 2023

4. 将系统时钟写入硬件时钟

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# hwclock -w

**测试结果**

1. 断电重启评估板，查看当前系统时钟和硬件时钟

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# date

    =====> 输出信息：
    Sat Jan 14 12:36:34 UTC 2023

2. 查看当前RTC芯片时钟

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# hwclock

    =====> 输出信息：
    2023-01-14 12:37:06.057566+00:00

|   可以看到我们得到的时间与设置的时间基本相同。

音频播放测试
--------------

|   【测试说明】：通过播放音频文件验证评估板的音频播放功能。
|   【接口标识】：P1
|   【系统设备】：wm8960-audio

**测试操作**

|   把耳机插入开发板的“EAR”口。
|   执行测试命令：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# aplay /my-demo/Rear_Center.wav   

    =====> 输出信息：
    Playing WAVE '/my-demo/Rear_Center.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

**测试结果**

|   执行上面的测试命令后会听到音频设备输出的声音。

音频录音测试
-------------

|   【测试说明】：通过录音并播放录音文件验证评估板的音频录音功能。
|   【接口标识】：P1
|   【系统设备】：wm8960-audio

**测试操作**

1. 把带MIC的耳机插入开发板的“MIC”口。
2. 执行录音命令：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# arecord -d 5 -c 2 -r 48000 -f S16_LE record.wav

    =====> 输出信息：
    Recording WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

3. 播放录音

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# aplay record.wav

    =====> 输出信息：
    Playing WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Stereo

**测试结果**

|   执行上面的测试命令后会听到播放的录音。

usb识别为网口测试
------------------

|   【测试说明】：通过mini usb线将usb识别为网口
|   【接口标识】：J5
|   【系统设备】：usb0

**测试操作**

1. 载入模块

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# modprobe g_ether

    =====> 输出信息：
    [ 1142.930290] using random self ethernet address
    [ 1142.934837] using random host ethernet address
    [ 1142.963949] usb0: HOST MAC 02:07:67:c9:1c:71
    [ 1142.981727] usb0: MAC 4e:76:dc:e4:13:cf
    [ 1142.998101] using random self ethernet address
    [ 1143.018416] using random host ethernet address
    [ 1143.030241] g_ether gadget: Ethernet Gadget, version: Memorial Day 2008
    [ 1143.046032] g_ether gadget: g_ether ready

2. 设置IP

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# ifconfig usb0 192.168.7.2
    将PC识别的rndis的本地连接IP设置为192.168.7.8

3. 测试网口

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# ping 192.168.7.7 -c 2 -w 4
    =====> 输出信息：
    PING 192.168.7.7 (192.168.7.7): 56 data bytes
    64 bytes from 192.168.7.7: seq=0 ttl=128 time=0.555 ms
    64 bytes from 192.168.7.7: seq=1 ttl=128 time=0.521 ms

    --- 192.168.7.7 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.521/0.538/0.555 ms

**测试结果**

|   “0% packet loss”表示测试通过。
|   注：若WIN10识别rndis为COM口，则需要下载驱动kindle_rndis.inf_amd64-v1.0.0.1.zip 解压后，以管理员权限执行5-runasadmin_register-CA-cer.cmd，然后在COM口处双击，在计算机中查找解压的驱动程序，这样就会有rndis网络了。

usb识别为U盘测试
-----------------

|   【测试说明】：通过mini usb线在PC识别开发板为U盘
|   【接口标识】：J5
|   【系统设备】：devtmpfs

**测试操作**

1. 创建一个10M大小的文件

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# dd if=/dev/zero of=/dev/shm/disk bs=1024 count=10240

    =====> 输出信息：
    10240+0 records in
    10240+0 records out
    10485760 bytes (10 MB, 10 MiB) copied, 0.0959887 s, 109 MB/s

2. 载入模块

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# modprobe g_mass_storage stall=0 file=/dev/shm/disk removable=1

    =====> 输出信息：
    [  113.101409] Mass Storage Function, version: 2009/09/11
    [  113.106701] LUN: removable file: (no medium)
    [  113.114166] LUN: removable file: /dev/shm/disk
    [  113.118655] Number of LUNs=1
    [  113.121708] g_mass_storage gadget: Mass Storage Gadget, version: 2009/09/11
    [  113.130701] g_mass_storage gadget: userspace failed to provide iSerialNumber
    [  113.138667] g_mass_storage gadget: g_mass_storage ready

3. 识别U盘

|   此时PC“我的电脑”会出现U盘的驱动器，将其格式化后，便可对其读写

4. 挂载

.. code-block:: shell

    root@myzr-rzfive:~# mount /dev/shm/disk /mnt

**测试结果**

|   在/mnt/下看到在电脑写入的文件，在开发板写入文件，重新插拔MINI USB可在PC看到在开发板写入的新文件。

CPU温度测试
-------------

|   【测试说明】：查看CPU温度
|   【接口标识】：无
|   【系统设备】：/sys/class/thermal/thermal_zone0/temp

**测试操作**

​|  输入命令

.. code-block:: shell

    =====> 输入指令:
    echo $[$(cat /sys/class/thermal/thermal_zone0/temp)/1000]
    =====> 输出信息：
    36

**测试结果**

|   36表示CPU的温度为36°

WIFI模块测试
-------------

|   【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|   【接口标识】：WIFI&BT
|   【接口丝印】：E2
|   【系统设备】：wlan0

**测试操作**

1. 把WIFI天线连接到“E1”接口上
2. 生成 SSID 的 WPA PSK 文件 |   

|   命令格式: `wpa_passphrase [passphrase]`

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf 

3. 连接：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf 

    =====> 输出信息：
    Successfully initialized wpa_supplicant
    nl80211: kernel reports: Authentication algorithm number required
    rfkill: Cannot open RFKILL control device
    。。。。。。

4. 获取IP：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# udhcpc -i wlan0

    =====> 输出信息：
    udhcpc: started, v1.31.1
    udhcpc: sending discover
    udhcpc: sending discover
    udhcpc: sending select for 192.168.43.204
    udhcpc: lease of 192.168.43.204 obtained, lease time 3600
    /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

5. 测试连接：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# ping -I wlan0 www.baidu.com -c 2 -w 4

    =====> 输出信息：
    PING www.baidu.com (163.177.151.110): 56 data bytes
    64 bytes from 163.177.151.110: seq=0 ttl=55 time=34.722 ms
    64 bytes from 163.177.151.110: seq=1 ttl=55 time=31.935 ms

    --- www.baidu.com ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 31.935/33.328/34.722 ms

蓝牙测试
----------

|   【测试说明】：扫描到蓝牙设备后，发送L2CAP回应请求并接收回答
|   【接口标识】：WIFI&BT
|   【接口丝印】：E2
|   【系统设备】：hci0

**测试操作**

1. 把天线连接到“E1”接口上
2. 启动蓝牙：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# hciconfig hci0 up
    root@myzr-rzfive:~# hciconfig

    =====> 输出信息：
    hci0:   Type: Primary  Bus: USB
        BD Address: 30:7B:C9:6E:F6:43  ACL MTU: 1021:8  SCO MTU: 255:12
        UP RUNNING PSCAN 
        RX bytes:1250 acl:0 sco:0 events:72 errors:0
        TX bytes:1090 acl:0 sco:0 commands:72 errors:0

3. 扫描外部蓝牙设备：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~#  hcitool scan

    =====> 输出信息：
    Scanning ...
        A5:7C:A2:26:9F:F8   豪华智能按摩椅
        1C:D1:07:D7:65:EC   真我GT Neo 闪速版

4. 发送发送L2CAP包测试：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# l2ping 1C:D1:07:D7:65:EC

    =====> 输出信息：
    Ping: 1C:D1:07:D7:65:EC from 30:7B:C9:6E:F6:43 (data size 44) ...
    44 bytes from 1C:D1:07:D7:65:EC id 0 time 6.07ms
    44 bytes from 1C:D1:07:D7:65:EC id 1 time 24.67ms
    44 bytes from 1C:D1:07:D7:65:EC id 2 time 26.03ms
    44 bytes from 1C:D1:07:D7:65:EC id 3 time 72.35ms
    44 bytes from 1C:D1:07:D7:65:EC id 4 time 72.37ms
    44 bytes from 1C:D1:07:D7:65:EC id 5 time 62.30ms
    ^C6 sent, 6 received, 0% loss

|   “0% packet loss”表示蓝牙连接正常。

EC20 模块测试
---------------

|   【测试说明】：4G连接成功后，开发板向外网发送ICMP报文来验证连接正常。
|   【接口标识】：J9
|   【系统设备】：usb0或者usb1

**测试操作**

1. 开发板断电，接上4G模块，接上天线并插入SIM卡后启动评估板。
2. 使用指令进行网络连接：

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# /my-demo/quectel-CM &

    =====> 输出信息：
    [1] 231
    [12-16_05:31:07:561] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
    [12-16_05:31:07:561] ./quectel-CM profile[1] = (null)/(null)/(null)/0, pincode = (null)
    [12-16_05:31:07:564] Find /sys/bus/usb/devices/1-1.4 idVendor=2c7c idProduct=0125
    [12-16_05:31:07:564] Find /sys/bus/usb/devices/1-1.4:1.4/net/usb0
    [12-16_05:31:07:564] Find usbnet_adapter = usb0
    [12-16_05:31:07:564] Find /sys/bus/usb/devices/1-1.4:1.4/GobiQMI/qcqmi0
    [12-16_05:31:07:564] Find qmichannel = /dev/qcqmi0
    [12-16_05:31:07:598] Get clientWDS = 7
    root@myzr-rzfive:~# [12-16_05:31:07:631] Get clientDMS = 8
    [12-16_05:31:07:661] Get clientNAS = 9
    [12-16_05:31:07:694] Get clientUIM = 10
    [12-16_05:31:07:726] Get clientWDA = 11
    [12-16_05:31:07:759] requestBaseBandVersion EC20CEHCLGR06A04M1G
    [12-16_05:31:07:854] requestGetSIMStatus SIMStatus: SIM_READY
    [12-16_05:31:07:886] requestGetProfile[1] ctnet///0
    [12-16_05:31:07:917] requestRegistrationState2 MCC: 460, MNC: 11, PS: Attached, DataCap: LTE
    [12-16_05:31:07:951] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
    [12-16_05:31:08:015] requestRegistrationState2 MCC: 460, MNC: 11, PS: Attached, DataCap: LTE
    [12-16_05:31:08:046] requestSetupDataCall WdsConnectionIPv4Handle: 0xe174f930
    [12-16_05:31:08:143] requestQueryDataCall IPv4ConnectionStatus: CONNECTED
    [12-16_05:31:08:174] ifconfig usb0 up
    [12-16_05:31:08:208] busybox udhcpc -f -n -q -t 5 -i usb0
    udhcpc: started, v1.31.1
    udhcpc: sending discover
    udhcpc: sending select for 10.26.232.226
    udhcpc: lease of 10.26.232.226 obtained, lease time 7200
    [12-16_05:31:08:451] /etc/udhcpc.d/50default: Adding DNS 202.96.128.86
    [12-16_05:31:08:451] /etc/udhcpc.d/50default: Adding DNS 202.96.134.133

**测试连接**

.. code-block:: shell

    =====> 输入指令:
    root@myzr-rzfive:~# ping -I usb0 www.baidu.com -c 2 -w 4

    =====> 输出信息：
    PING www.baidu.com (14.215.177.39): 56 data bytes
    64 bytes from 14.215.177.39: seq=0 ttl=54 time=43.305 ms
    64 bytes from 14.215.177.39: seq=1 ttl=54 time=28.630 ms

    --- www.baidu.com ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 28.630/35.967/43.305 ms

复制更新镜像
--------------

|   【测试说明】：可更新dtb、Image、kernel-modules.tar.bz2
|   【接口标识】：无
|   【系统设备】：无

**测试操作**

1. 复制相应文件到开发板当前目录，以tftp为例

|   电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。
|   把开发板的这个网口用网线跟电脑网口连接起来。

2. 测试连接

.. code-block:: shell

    =====> 输入指令:
    ping 192.168.137.99 -c 2 -w 4 
    =====> 输出信息：
    root@myzr-rzfive:~# ping 192.168.137.99 -c 2 -w 4
    PING 192.168.137.99 (192.168.137.99): 56 data bytes
    64 bytes from 192.168.137.99: seq=0 ttl=128 time=1.061 ms
    64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.546 ms

    --- 192.168.137.1 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.546/0.803/1.061 ms

|   0% packet loss”表示连接正常。

3. 传输文件

.. code-block:: shell

    =====> 输入指令:
    tftp -gr kernel-image.tar.bz2 192.168.137.99
    tftp -gr kernel-modules.tar.bz2 192.168.137.99

4. 查看系统是否自动挂载分区

.. code-block:: shell

    =====> 输入指令:
    ls /run/media/mmcblk0p1/
    =====> 输出信息：
    Image             kernel-modules.tar.bz2  ramsys.img
    kernel-image.tar.bz2  myzr-rzfive-2g.dtb      rootfs.tar.bz2

5. 更新内核和dtb文件

.. code-block:: shell

    =====> 输入指令:
    tar jxvf kernel-image.tar.bz2 -C /run/media/mmcblk0p1/
    =====> 输出信息：
    root@myzr-rzfive:~# tar jxvf kernel-image.tar.bz2 -C /run/media/mmcblk0p1/
    Image
    myzr-rzfive-2g.dtb

6. 更新内核模块

.. code-block:: shell

    =====> 输入指令:
    tar jxvf kernel-modules.tar.bz2 -C /
    =====> 输出信息：
    root@myzr-rzfive:~# tar jxvf kernel-modules.tar.bz2 -C /
    lib/
    lib/modules/
    lib/modules/5.10.145-cip17-riscv-renesas/
    lib/modules/5.10.145-cip17-riscv-renesas/modules.softdep
    lib/modules/5.10.145-cip17-riscv-renesas/modules.order
    lib/modules/5.10.145-cip17-riscv-renesas/modules.symbols.bin
    lib/modules/5.10.145-cip17-riscv-renesas/modules.builtin
    lib/modules/5.10.145-cip17-riscv-renesas/modules.devname
    lib/modules/5.10.145-cip17-riscv-renesas/source