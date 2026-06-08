MYZR-IMX8MM-EK240-8MM Linux-4.14.98 测试手册
==============================================

网口测试（ETH1）
-----------------

|  【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|  【接口标识】：Ethernet
|  【接口丝印】：J9
|  【系统接口】：eth0

**测试操作**

|  配置电脑有线网卡IP为 192.168.137.99。 用网线连接开发板的ETH1和电脑。 配置开发板网口：
|  =====> 输入指令:

.. code-block:: shell

      ifconfig eth0 192.168.137.81

|  测试ETH1（eth0）
|  =====> 输入指令:

.. code-block:: shell

   ping 192.168.137.99 -c 2 -w 4

|  =====> 输出信息：

.. code-block:: shell

   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.685 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.374 ms 
   192.168.137.99 ping statistics 
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.374/0.529/0.685/0.157 ms

**测试结果**

|  “0% packet loss”表示测试通过。

USB测试
---------

|  【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|  【接口标识】：USB3.0/USB2.0
|  【接口丝印】：J5

**测试方法**

|  将USB设备插入底板USB接口,系统输出类似如下信息。
|  =====> 输出信息:

.. code-block:: shell

   usb 1-1.3: new high-speed USB device number 4 using ci_hdrc
   usb-storage 1-1.3:1.0: USB Mass Storage device detected
   scsi host0: usb-storage 1-1.3:1.0
   scsi 0:0:0:0: Direct-Access   Generic  STORAGE DEVICE  1532 PQ: 0 ANSI: 6
   sd 0:0:0:0: [sda] 60776448 512-byte logical blocks: (31.1 GB/29.0 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn\'t support DPO or FUA
   sda: sda1
   sd 0:0:0:0: [sda] Attached SCSI removable disk
   FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|  将USB设备从底板拔出。
|  =====> 输出信息：

.. code-block:: shell

   usb 1-1.3: USB disconnect, device number 4

**测试结果**

|  USB存储设备插入时可查看到sda1设备。

SD接口测试
-----------

|  【测试说明】：采用插入并识别TF卡的方式进行测试
|  【接口标识】：MicroSD
|  【接口丝印】：J10

**测试方法**

|  为开发板断电，把TF卡安装到SD接口。
|  =====> 输入指令:

.. code-block:: shell

   df

|  =====> 输出信息：

.. code-block:: shell

   /dev/mmcblk1p1   30379712  665216  29714496  3% /run/media/mmcblk1p1

**测试结果**

|  输入指令后系统输出如上类似信息即表示正常。

标准 GPIO 测试
----------------

|  【测试说明】：控制GPIO的输出电平
|  【接口标识】：
|  【接口丝印】：J7
|  【系统接口】：/sys/class/gpio/

**GPIO输出低电平测试**

|  配置 J7:15 为输出低电平的操作方法：

.. code-block:: shell

   =====> 输入指令:

      OUT_IO_OUT_NUM=8 
      echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export

      echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction

      echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 

|  用万用表测试管脚J7:15，电压为0V，则表示OK

**GPIO输出高电平测试**

|  配置 J7:15 为输出高电平的操作方法：
|  =====> 输入指令:

.. code-block:: shell
   
   <echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  用万用表测试管脚J5:5，电压为3.3V，则表示OK GPIO输入测试
|  控制 GPIO 为输入低电平方法：杜邦线连接J5:5和地脚
|  =====> 输入指令:

.. code-block:: shell

   echo "in" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction

   cat /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  控制 GPIO 为输入高电平方法：杜邦线连接J5:5和J5:1脚：
|  =====> 输入指令:

.. code-block:: shell

   cat /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  可看到对应的电平分别为0和1

CPU温度测试
------------

|  【测试说明】：查看CPU温度
|  【接口标识】：无
|  【系统设备】：/sys/class/thermal/thermal_zone0/temp

**测试操作**

|  =====> 输入指令:

.. code-block:: shell

   echo $[$(cat /sys/class/thermal/thermal_zone0/temp)/1000]

|  =====> 输出信息：

.. code-block:: shell
   
   47

**测试结果**

|  47表示CPU的温度为47°

音频播放测试
-------------

|  【测试说明】：通过播放音频文件验证评估板的音频播放功能。
|  【接口位置】：P4
|  【系统设备】：wm8524-audio

**测试操作**

|  把耳机插入开发板的P5口。
|  执行测试指令：
|  =====> 输入指令:

.. code-block:: shell

   aplay /unit_tests/ASRC/audio8k16S.wav

|  =====> 输出信息：

.. code-block:: shell

   Playing WAVE '/unit_tests/ASRC/audio8k16S.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Stereo

**测试结果**

|  执行上面的测试命令后会听到音频设备输出的声音。

Mipi-DSI显示测试
------------------

|  【测试说明】：通过连接Mipi显示屏观察开发板显示功能。
|  【接口位置】：J2
|  【系统设备】：/dev/fb0

**测试操作**

|  为开发板断电，用fpc排线连接mipi显示屏和开发板。

**测试结果**

|  U-Boot启动阶段可以看到U-Boot Logo；
|  内核启动阶段可以看到内核Logo；
|  文件系统启动阶段可以看到OpenEmbedded Logo；
|  系统启动完成后可以看到一个简单的GUI。

Mipi-CSI显示测试
------------------

|  【测试说明】：通过连接Mipi摄像头检查开发板Mipi-CSI接口。
|  【接口位置】：J1
|  【系统设备】：/dev/video0

**测试操作**

|  为开发板断电，用fpc排线连接mipi摄像头和开发板。

.. code-block:: shell

   gst-launch-1.0 v4l2src ! video/x-raw,format=YUY2,width=640,height=480 ! queue max-size-time=0 ! waylandsink enable-tile=true sync=false

**测试结果**

|  可以在显示屏看到摄像头所拍摄的内容

WIFI模块（RTL8723DU）测试
---------------------------

|  【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口丝印】：E1、U6
|  【系统设备】：wlan0

**测试操作**

1. 确定“U6”丝印处有贴上模块，否则无需进行测试。
2. 把天线连接到“E1”丝印的接口上。
3. 生成 SSID 的 WPA PSK 文件

|  命令格式: wpa_passphrase  [passphrase]
|  =====> 输入指令:

.. code-block:: shell

   wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf
   pkill wpa_supplicant

4. 连接

|  =====> 输入指令:

.. code-block:: shell

   wpa_supplicant -B -i wlan0 -D wext -c /etc/wpa_supplicant.conf

|  =====> 输出信息：

.. code-block:: shell

   Successfully initialized wpa_supplicant
   rfkill: Cannot open RFKILL control device
   ioctl[SIOCSIWAP]: Operation not permitted

5. 获取 IP

|  =====> 输入指令:

.. code-block:: shell

   udhcpc -i wlan0

|  =====> 输出信息：

.. code-block:: shell

   udhcpc (v1.23.2) started
   Sending discover...
   Sending select for 192.168.43.99...
   Lease of 192.168.43.99 obtained, lease time 3600
   /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

6. 测试连接

|  =====> 输入指令:

.. code-block:: shell

   ping -I wlan0 www.baidu.com -c 2 -w 4

|  =====> 输出信息：

.. code-block:: shell

   PING www.baidu.com (14.215.177.38): 56 data bytes
   64 bytes from 14.215.177.38: seq=0 ttl=49 time=15.753 ms
   64 bytes from 14.215.177.38: seq=1 ttl=49 time=11.835 ms
   --- www.baidu.com ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 11.835/13.794/15.753 ms

**测试结果**

|  “0% packet loss”表示WIFI连接正常。

蓝牙测试(RTL8723DU)
--------------------

|  【测试说明】：扫描到蓝牙设备后，发送L2CAP回应请求并接收回答。
|  【接口丝印】：E1、U6
|  【系统设备】：hci0

**测试操作**

1. 确定“U6”丝印处有贴上模块，否则无需进行测试。
2. 把天线连接到“E1”丝印的接口上。
3. 配置蓝牙系统接口

|  =====> 输入指令:

.. code-block:: shell

   hciconfig hci0 up
   hciconfig hci0 piscan
   hciconfig -a

|  =====> 输出信息：

.. code-block:: shell

   hci0:   Type: Primary  Bus: UART
   BD Address: 76:5E:F9:C6:B5:86  ACL MTU: 1021:8  SCO MTU: 64:1
   UP RUNNING PSCAN ISCAN 
   RX bytes:1381 acl:0 sco:0 events:75 errors:0
   TX bytes:1210 acl:0 sco:0 commands:75 errors:0
   Features: 0xbf 0xfe 0xcf 0xfe 0xdb 0xff 0x7b 0x87
   Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3 
   Link policy: RSWITCH SNIFF 
   Link mode: SLAVE ACCEPT 
   Name: 'imx8mqevk'
   Class: 0x200000
   Service Classes: Audio
   Device Class: Miscellaneous, 
   HCI Version: 4.0 (0x6)  Revision: 0x1000
   LMP Version: 4.0 (0x6)  Subversion: 0x610c
   Manufacturer: Broadcom Corporation (15)

4. 查看板子蓝牙设备信息

|  =====> 输入指令:

.. code-block:: shell

   hcitool dev

|  =====> 输出信息：

.. code-block:: shell

   Devices:
   hci0    76:5E:F9:C6:B5:86

5. 扫描外部蓝牙设备

|  =====> 输入指令:

.. code-block:: shell

   hcitool scan

|  =====> 输出信息：

.. code-block:: shell

   Scanning ...
   ......
   E4:B2:FB:DA:39:1D   iPhone

6. 发送发送L2CAP包测试

|  =====> 输入指令:

.. code-block:: shell

   l2ping E4:B2:FB:DA:39:1D -c 2

|  =====> 输出信息：

.. code-block:: shell

   Ping: E4:B2:FB:DA:39:1D from 76:5E:F9:C6:B5:86 (data size 44) ...
   0 bytes from E4:B2:FB:DA:39:1D id 0 time 7.10ms
   0 bytes from E4:B2:FB:DA:39:1D id 1 time 103.84ms
   2 sent, 2 received, 0% loss

**测试结果**

|  “0% packet loss”表示蓝牙连接正常

CAN 测试
----------

|  测试说明：
|  测试需要用到两个CAN接口

|  测试命令：
|  配置 CAN：
|  =====> 输入指令:

.. code-block:: shell

   ip link set can0 up type can bitrate 125000

|  设置CAN后台接收：
|  =====> 输入指令:

.. code-block:: shell

   candump can0 &

|  设置CAN发送数据：
|  =====> 输入指令:

.. code-block:: shell

   cansend can0 1F334455#1122334455667788

232串口测试
------------

- 测试方法说明：

|  串口线直接将TX1和RX1短接，执行以下命令：

.. code-block:: shell

   /unit_tests/UART/serial_test.out /dev/ttyXRUSB1 "www.myzr.com.cn"

|  串口线直接将TX2和RX2短接，执行以下命令：

.. code-block:: shell

   /unit_tests/UART/serial_test.out /dev/ttyXRUSB2 "www.myzr.com.cn"

485串口测试1
------------

|  测试说明

- 测试方法说明：

|  使用串口线通过RS485转232模块连接开发板测试串口A1、B1和电脑,用ssh客户端登陆。

|  UART测试

- 在SSH端执行发送命令，可以在电脑接受到串口发送过来的信息：

.. code-block:: shell

   echo “myzr” > /dev/ttyXRUSB3

- 测试结果说明： 通过ssh客户端向串口发送字符串，串口可以收到字符串。
- 在SSH端执行接收命令：

.. code-block:: shell

   cat /dev/ttyXRUSB3

- 测试结果说明：

|  通过串口向ssh客户端发送字符串，ssh客户端可以收到字符串。

485串口2测试2
--------------

|  测试说明

- 测试方法说明：

|  使用串口线通过RS485转232模块连接开发板测试串口A2、B2和电脑,用ssh客户端登陆。

|  UART测试

- 在SSH端执行发送命令，可以在电脑接受到串口发送过来的信息：

.. code-block:: shell

   echo “myzr” > /dev/ttyXRUSB0

- 测试结果说明： 通过ssh客户端向串口发送字符串，串口可以收到字符串。
- 在SSH端执行接收命令：

.. code-block:: shell

   cat /dev/ttyXRUSB0

- 测试结果说明：

|  通过串口向ssh客户端发送字符串，ssh客户端可以收到字符串。

EC20 模块测试
----------------

|  【测试说明】：4G连接成功后，开发板向外网发送ICMP报文来验证连接正常。
|  【系统设备】：usb0

**测试操作**

1. 开发板断电，接上4G模块，接上天线并插入SIM卡后启动评估板。
2. 使用指令进行网络连接：

|  =====> 输入指令:

.. code-block:: shell

   udhcpc -i usb0

|  =====> 输出信息：

.. code-block:: shell

   udhcpc: started, v1.27.2
   cdc_ether 1-1.1:1.4 usb0: kevent 12 may have been dropped
   udhcpc: sending discover
   udhcpc: sending select for 192.168.225.52
   udhcpc: lease of 192.168.225.52 obtained, lease time 43200
   /etc/udhcpc.d/50default: Adding DNS 192.168.225.1

|  测试连接：
|  =====> 输入指令:

.. code-block:: shell

   ping -I usb0 www.baidu.com -c 2 -w 4

|  =====> 输出信息：

.. code-block:: shell

   PING www.a.shifen.com (163.177.151.109) from 192.168.225.52 usb0: 56(84) bytes of data.
   64 bytes from 163.177.151.109: icmp_seq=1 ttl=55 time=158 ms
   --- www.a.shifen.com ping statistics ---
   1 packets transmitted, 1 received, 0% packet loss, time 0ms
   rtt min/avg/max/mdev = 158.529/158.529/158.529/0.000 ms

**测试结果**

|  “0% packet loss”表示WIFI连接正常。

tftp更新镜像
-------------

|  【测试说明】：可更新dtb、zImage

**测试操作**

|  电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。
|  把开发板的这个网口用网线跟电脑网口连接起来。
|  进入u-boot命令行。

1. 设置IP

|  =====> 输入指令:

.. code-block:: shell

   设置开发板IP：setenv ipaddr 192.168.137.9
   设置电脑IP：setenv serverip 192.168.137.99
   设置MAC地址：setenv ethaddr 00:00:00:00:00:03
   测试网络： ping 192.168.137.99

|  =====> 输出信息：

.. code-block:: shell

   ethernet@30be0000 Waiting for PHY auto negotiation to complete.... done
   Using ethernet@30be0000 device
   host 192.168.137.99 is alive

2. 设置环境变量

|  =====> 输入指令:

.. code-block:: shell

   setenv update_dtb   'if tftpboot ${loadaddr} ${fdt_file}; then '\
   'fatwrite mmc ${mmcdev}:${mmcpart} ${loadaddr} ${fdt_file} ${filesize}; fi;'

   setenv update_kern  'if tftpboot ${loadaddr} ${image}; then '\
   'fatwrite mmc ${mmcdev}:${mmcpart} ${loadaddr} ${image} ${filesize}; fi;'

   saveenv

3. 烧写dtb

|  =====> 输入指令:

.. code-block:: shell

   run update_dtb

|  =====> 输出信息：

.. code-block:: shell

   Using ethernet@30be0000 device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'myimx8mmek240-8mm.dtb'.
   Load address: 0x40480000
   Loading: ###
    610.4 KiB/s
   done
   Bytes transferred = 41910 (a3b6 hex)
   writing myimx8mmek240-8mm.dtb
   41910 bytes written

4. 烧写zImage

|  =====> 输入指令:

.. code-block:: shell

   run update_kern

|  =====> 输出信息：

.. code-block:: shell

   Using ethernet@30be0000 device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'Image'.
   Load address: 0x40480000
   Loading: #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    #################################################################
    ##########################################
    1.2 MiB/s
   done
   Bytes transferred = 23509504 (166ba00 hex)
   writing Image
   23509504 bytes written

复制更新镜像
-------------

|  【测试说明】：可更新dtb、zImage、kernel-modules

**测试操作**

1. 复制相应文件到开发板当前目录，以tftp为例，电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。把开发板的这个网口用网线跟电脑网口连接起来。
2. 测试连接

|  =====> 输入指令:

.. code-block:: shell

   ping 192.168.137.99 -c 2 -w 4 

|  =====> 输出信息：

.. code-block:: shell

   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.522 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.415 ms
   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.415/0.468/0.522/0.057 ms

|  “0% packet loss”表示连接正常。

3. 传输文件

|  =====> 输入指令:

.. code-block:: shell

   tftp -g 192.168.137.99 -r Image

   tftp -g 192.168.137.99 -r myimx8mmek240-8mm.dtb
   tftp -g 192.168.137.99 -r kernel-modules.tar.bz2

4. 复制相应的文件到/run/media/mmcblk1p1/目录，将原文件替换。

|  =====> 输入指令:

.. code-block:: shell

   cp Image /run/media/mmcblk1p1/
   cp myimx8mmek240-8mm.dtb /run/media/mmcblk1p1/

5. 解压更新内核模块

|  =====> 输入指令:

.. code-block:: shell

   tar xjvf kernel-modules.tar.bz2 -C /

6. 保存并重启

|  =====> 输入指令:

.. code-block:: shell

   reboot