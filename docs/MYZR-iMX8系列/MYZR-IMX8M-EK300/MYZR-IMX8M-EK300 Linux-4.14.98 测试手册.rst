
MYZR-IMX8M-EK300 Linux-4.14.98 测试手册
=========================================

测试环境
---------

|  【开发板型号】：MYZR-IMX8M-EK300
|  【内核版本】：Linux-4.14.98
|  【文件系统】：fsl-image-validation-myimx8m.tar.bz2
|  【工具版本】：UUU-MYIMX8M-L4.14.98
|  **说明：** 为保证测试无误，需要使用的烧录工具版本应不低于20190903


接口标识图
-----------

.. image:: /image/MYZR-iMX8系列/MYZR-IMX8M-EK300/1800px-IMX8MEK300-interface.jpg
   :alt: 1800px-IMX8MEK300-interface.jpg

网口测试（ETH1）
-----------------

|  【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|  【接口标识】：Ethernet
|  【接口丝印】：J16
|  【系统接口】：eth0

**测试操作**

|  配置电脑有线网卡IP为 192.168.137.99。
|  用网线连接开发板的ETH1和电脑。
|  配置开发板网口：

.. code-block:: shell
   
   =====> 输入指令:
   ifconfig eth0 192.168.137.81
  
|  测试ETH1（eth0）：

.. code-block:: shell

   =====> 输入指令:
   ping 192.168.137.99 -c 2 -w 4 

   =====> 输出信息：
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.685 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.374 ms 
   
   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.374/0.529/0.685/0.157 ms    

**测试结果**

|  “0% packet loss”表示测试通过。


USB测试
---------

|  【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|  【接口标识】：USB3.0/USB2.0
|  【接口丝印】：J18

**测试方法**

|  将USB设备插入底板USB接口,系统输出类似如下信息。

.. code-block:: shell

   =====> 输出信息： 
   usb 1-1.1: new high-speed USB device number 3 using xhci-hcd
   usb-storage 1-1.1:1.0: USB Mass Storage device detected
   scsi host0: usb-storage 1-1.1:1.0
   scsi 0:0:0:0: Direct-Access     Generic  STORAGE DEVICE   1402 PQ: 0 ANSI: 6
   sd 0:0:0:0: [sda] 7774208 512-byte logical blocks: (3.98 GB/3.71 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
    sda: sda1
   sd 0:0:0:0: [sda] Attached SCSI removable disk
   FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|  将USB设备从底板拔出。

.. code-block:: shell

   =====> 输出信息： 
   usb 1-1.1: USB disconnect, device number 3 

**测试结果**

|  USB存储设备插入时可查看到sda1设备。


SD接口测试
-----------

|  【测试说明】：采用插入并识别TF卡的方式进行测试
|  【接口标识】：MicroSD
|  【接口丝印】：J9

**测试方法**

|  为开发板断电，把TF卡安装到SD接口。

.. code-block:: shell

   =====> 输入指令:
   dmesg | grep -E "mmc1|mmcblk1" 

   =====> 输出信息： 
   mmc1: SDHCI controller on 30b50000.usdhc [30b50000.usdhc] using ADMA
   mmc1: host does not support reading read-only switch, assuming write-enable
   mmc1: new high speed SDHC card at address 1234
   mmcblk1: mmc1:1234 SA04G 3.71 GiB 
    mmcblk1: p1

**测试结果**

|  SD存储设备插拔时系统输出如上类似信息即表示正常。


标准 GPIO 测试
---------------

|  【测试说明】：控制GPIO的输出电平
|  【接口标识】：NAND/SAI/S/PDIF/PCIe/I2C/GPIO
|  【接口丝印】：J12
|  【系统接口】：/sys/class/gpio/

GPIO输出低电平测试
~~~~~~~~~~~~~~~~~~~

|  配置 J12:70 为输出低电平的操作方法：

.. code-block:: shell

   =====> 输入指令:
   OUT_IO_OUT_NUM=4 
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 

|  用万用表测试管脚J12:70，电压为0V，则表示OK

GPIO输出高电平测试
~~~~~~~~~~~~~~~~~~~

|  配置 J12:70 为输出高电平的操作方法：

.. code-block:: shell

   =====> 输入指令:  
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  用万用表测试管脚J12:70，电压为3.3V，则表示OK

GPIO输入测试
~~~~~~~~~~~~

|  控制 GPIO 为输入低电平方法：杜邦线连接J12:70和地脚

.. code-block:: shell

   =====> 输入指令:
   echo "in" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction   
   cat /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  控制 GPIO 为输入高电平方法：杜邦线连接J12:70和J12:49脚：

.. code-block:: shell

   =====> 输入指令:
   cat /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value   

|  可看到对应的电平分别为0和1


CPU温度测试
------------

|  【测试说明】：查看CPU温度
|  【接口标识】：无
|  【系统设备】：/sys/class/thermal/thermal_zone0/temp

**测试操作**

1. 输入命令

.. code-block:: shell

   =====> 输入指令:
   echo $[$(cat /sys/class/thermal/thermal_zone0/temp)/1000]
   =====> 输出信息：
   53

**测试结果**

|  53表示CPU的温度为53°

音频播放测试
-------------

|  【测试说明】：通过播放音频文件验证评估板的音频播放功能。
|  【接口标识】：HP
|  【接口位置】：P1
|  【系统设备】：wm8524-audio

**测试操作**

|  把耳机插入开发板的“HP”口。
|  执行测试指令：

.. code-block:: shell

   =====> 输入指令:
   aplay /unit_tests/ASRC/audio8k16S.wav    

   =====> 输出信息：
   Playing WAVE '/unit_tests/ASRC/audio8k16S.wav' : Signed 16 bit Little 
   Endian, Rate 8000 Hz, Stereo

**测试结果**

|  执行上面的测试命令后会听到音频设备输出的声音。


HDMI显示测试
-------------

|  【测试说明】：通过连接HDMI显示屏观察开发板显示功能。
|  【接口标识】：HDMI
|  【接口位置】：J12
|  【系统设备】：/dev/fb0

**测试操作**

|  为开发板断电，用HDMI线连接HDMI显示器和开发板，并为HDMI显示屏供电。
|  建议使用HDMI接口的显示屏，而不是其它接口转HDMI的。
|  建议使用1920x1080分辨率的HDMI显示屏。

**测试结果**

|  U-Boot启动阶段可以看到U-Boot Logo；
|  内核启动阶段可以看到内核Logo；
|  文件系统启动阶段可以看到OpenEmbedded Logo；
|  系统启动完成后可以看到一个简单的GUI。

mipi与HDMI的转换
-----------------

|  进入u-boot控制台

.. code-block:: shell

   输入setenv fdt_file myimx8mek300-8mq-hdmi.dtb
   saveenv保存设置，重新启动即可切换到HDMI显示。

|  进入u-boot控制台

.. code-block:: shell

   输入setenv fdt_file myimx8mek300-8mq.dtb
   saveenv保存设置，重新启动即可切换到mipi显示。

WIFI模块（AP6354）测试
-----------------------

|  【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：WIFI&BT,WIFI_ANT
|  【接口丝印】：U3，ANT1/ANT2/ANT3   【系统设备】：wlan0

**测试操作**

1. 确定“WIFI+BT”标识处有贴上模块，否则无需进行测试。
2. 把WIFI天线连接到“WIFI_ANT”标识的接口上。
3. 生成 SSID 的 WPA PSK 文件

|  命令格式: wpa_passphrase <ssid> [passphrase]

.. code-block:: shell

   =====> 输入指令:
   wpa_passphrase MY-TEST-AP myzr2012 > /etc/wpa_supplicant.conf
   pkill wpa_supplicant

4. 连接

.. code-block:: shell

   =====> 输入指令:
   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

   =====> 输出信息：
   Successfully initialized wpa_supplicant
   rfkill: Cannot open RFKILL control device
   ioctl[SIOCSIWAP]: Operation not permitted

5. 获取 IP

.. code-block:: shell

   =====> 输入指令:
   udhcpc -i wlan0

   =====> 输出信息：
   udhcpc (v1.23.2) started
   Sending discover...
   Sending select for 192.168.43.99...
   Lease of 192.168.43.99 obtained, lease time 3600
   /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

6. 测试连接

.. code-block:: shell

   =====> 输入指令:
   ping -I wlan0 www.baidu.com -c 2 -w 4

   =====> 输出信息：
   PING www.baidu.com (14.215.177.38): 56 data bytes
   64 bytes from 14.215.177.38: seq=0 ttl=49 time=15.753 ms
   64 bytes from 14.215.177.38: seq=1 ttl=49 time=11.835 ms

   --- www.baidu.com ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 11.835/13.794/15.753 ms

**测试结果**

|  “0% packet loss”表示WIFI连接正常。

蓝牙测试(AP6354)
-----------------

|  【测试说明】：扫描到蓝牙设备后，发送L2CAP回应请求并接收回答。
|  【接口标识】：WIFI+BT，BL_ANT
|  【接口丝印】：U24，E1
|  【系统设备】：hci0

**测试操作**

1. 确定“WIFI+BT”标识处有贴上模块，否则无需进行测试。
2. 把蓝牙天线连接到“BL_ANT”标识的接口上。
3. 通过UART HCI连接到BlueZ堆栈

.. code-block:: shell

   =====> 输入指令:
   hciattach /dev/ttymxc2 bcm43xx 2000000 flow

   =====> 输出信息：
   bcm43xx_init
   Patch not found, continue anyway
   Set Controller UART speed to 2000000 bit/s
   Setting TTY to N_HCI line discipline
   Device setup complete


4. 配置蓝牙系统接口

.. code-block:: shell

   =====> 输入指令:
   hciconfig hci0 up
   hciconfig hci0 piscan
   hciconfig -a


   =====> 输出信息：
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

5. 查看板子蓝牙设备信息

.. code-block:: shell

   =====> 输入指令:
   hcitool dev  

   =====> 输出信息：
   Devices:
       hci0    76:5E:F9:C6:B5:86

6. 扫描外部蓝牙设备

.. code-block:: shell

   =====> 输入指令:
   hcitool scan  

   =====> 输出信息：
   Scanning ...
       ......
       E4:B2:FB:DA:39:1D   iPhone

7. 发送发送L2CAP包测试

.. code-block:: shell

   =====> 输入指令:
   l2ping E4:B2:FB:DA:39:1D -c 2
   =====> 输出信息：
   Ping: E4:B2:FB:DA:39:1D from 76:5E:F9:C6:B5:86 (data size 44) ...
   0 bytes from E4:B2:FB:DA:39:1D id 0 time 7.10ms
   0 bytes from E4:B2:FB:DA:39:1D id 1 time 103.84ms
   2 sent, 2 received, 0% loss

**测试结果**

|  “0% packet loss”表示蓝牙连接正常。


tftp更新镜像
-------------

|  【测试说明】：可更新dtb、Image
|  【接口标识】：无
|  【系统设备】：无

**测试操作**

|  电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。
|  把开发板的这个网口用网线跟电脑网口连接起来。
|  进入u-boot命令行。

1. 设置IP

.. code-block:: shell

   =====> 输入指令:
   设置开发板IP：setenv ipaddr 192.168.137.9
   设置电脑IP：setenv serverip 192.168.137.99
   设置MAC地址：setenv ethaddr 00:00:00:00:00:03
   测试网络： ping 192.168.137.99 
   =====> 输出信息：
   Using FEC device
   host 192.168.137.99 is alive

2. 设置环境变量

.. code-block:: shell

   =====> 输入指令:
   setenv update_dtb   'if tftpboot ${loadaddr} ${fdt_file}; then '\
   'fatwrite mmc ${mmcdev}:${mmcpart} ${loadaddr} ${fdt_file} ${filesize}; fi;'  

   setenv update_kern  'if tftpboot ${loadaddr} ${image}; then '\
   'fatwrite mmc ${mmcdev}:${mmcpart} ${loadaddr} ${image} ${filesize}; fi;'  

   saveenv

3. 烧写dtb

.. code-block:: shell

   =====> 输入指令:
   run update_dtb
   =====> 输出信息：
   Using ethernet@30be0000 device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'myimx8mek300-8mq.dtb'.
   Load address: 0x40480000
   Loading: ###
        4.5 MiB/s
   done
   Bytes transferred = 42713 (a6d9 hex)
   writing myimx8mek300-8mq.dtb
   42713 bytes written

4. 烧写zImage

.. code-block:: shell

   =====> 输入指令:
   run update_kern   
   =====> 输出信息：
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
        #################################################################
        #################################################################
        5.9 MiB/s
   done
   Bytes transferred = 24805888 (17a8200 hex)
   writing Image
   24805888 bytes written

复制更新镜像
-------------

|  【测试说明】：可更新dtb、Image、kernel-modules
|  【接口标识】：无
|  【系统设备】：无

**测试操作**

1. 复制相应文件到开发板当前目录，以tftp为例

|  电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。
|  把开发板的这个网口用网线跟电脑网口连接起来。

2. 测试连接

.. code-block:: shell

   =====> 输入指令:
   ping 192.168.137.99 -c 2 -w 4 
   =====> 输出信息：
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.522 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.415 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.415/0.468/0.522/0.057 ms

|  “0% packet loss”表示连接正常。

3. 传输文件

.. code-block:: shell

   =====> 输入指令:
   tftp -g 192.168.137.99 -r Image  
   tftp -g 192.168.137.99 -r myimx8mek300-8mq.dtb  
   tftp -g 192.168.137.99 -r kernel-modules.tar.bz2

4. 复制相应的文件到/run/media/mmcblk1p1/目录，将原文件替换。

.. code-block:: shell

   =====> 输入指令:
   cp Image /run/media/mmcblk1p1/
   cp myimx8mek300-8mq.dtb /run/media/mmcblk1p1/

5. 解压更新内核模块

.. code-block:: shell

   =====> 输入指令:

 t ar xjvf kernel-modules.tar.bz2 -C /

6. 保存并重启

.. code-block:: shell

   =====> 输入指令:
   reboot

usb识别为U盘测试
-----------------

|  【测试说明】：通过 usb线在PC识别开发板为U盘
|  【接口标识】：J15
|  【系统设备】：devtmpfs

**测试操作**

1. 创建一个10M大小的文件

.. code-block:: shell

   =====> 输入指令:
   # dd if=/dev/zero of=/dev/shm/disk bs=1024 count=10240

   =====> 输出信息：
   10240+0 records in
   10240+0 records out
   10485760 bytes (10 MB, 10 MiB) copied, 0.163177 s, 64.3 MB/s

2. 载入模块

.. code-block:: shell

   =====> 输入指令:
   # modprobe g_mass_storage stall=0 file=/dev/shm/disk removable=1

   =====> 输出信息：
   Mass Storage Function, version: 2009/09/11
   LUN: removable file: (no medium)
   LUN: removable file: /dev/shm/disk
   Number of LUNs=1
   Number of LUNs=1
   g_mass_storage gadget: Mass Storage Gadget, version: 2009/09/11
   g_mass_storage gadget: userspace failed to provide iSerialNumber
   g_mass_storage gadget: g_mass_storage ready
   imx8mqevk login:~# g_mass_storage gadget: high-speed config #1: Linux File-Backed Storage

3. 识别U盘

|  此时PC“我的电脑”会出现U盘的驱动器，将其格式化后，便可对其读写

4. 挂载

.. code-block:: shell

   # mount /dev/shm/disk /mnt

**测试结果**

|  在/mnt/下看到在电脑写入的文件，在开发板写入文件，重新插拔MINI USB可在PC看到在开发板写入的新文件。


usb识别为网口测试
------------------

|  【测试说明】：通过usb线将usb识别为网口
|  【接口标识】：J15
|  【系统设备】：usb0

**测试操作**

1. 载入模块

.. code-block:: shell

   =====> 输入指令:
   # modprobe g_ether
   =====> 输出信息：
   using random self ethernet address
   using random host ethernet address
   usb0: HOST MAC 4a:d6:a1:ff:e6:53
   usb0: MAC 12:e3:37:e8:7a:ab
   using random self ethernet address
   using random host ethernet address
   g_ether gadget: Ethernet Gadget, version: Memorial Day 2008
   g_ether gadget: g_ether ready
   imx8mqevk login:/# IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
   g_ether gadget: high-speed config #2: RNDIS
   IPv6: ADDRCONF(NETDEV_CHANGE): usb0: link becomes ready

2. 设置IP

.. code-block:: shell

   =====> 输入指令:
   # ifconfig usb0 192.168.7.2
   将PC识别的rndis的本地连接IP设置为192.168.7.8

3. 测试网口

.. code-block:: shell

   =====> 输入指令:
   # ping 192.168.7.8 -c 2 -w 4
   =====> 输出信息：
   PING 192.168.7.8 (192.168.7.8) 56(84) bytes of data.
   64 bytes from 192.168.7.8: icmp_seq=1 ttl=64 time=0.609 ms
   64 bytes from 192.168.7.8: icmp_seq=2 ttl=64 time=0.630 ms

   --- 192.168.7.8 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.609/0.619/0.630/0.027 ms

**测试结果**

|  “0% packet loss”表示测试通过
|  注：若WIN10识别rndis为COM口，则需要下载驱动kindle_rndis.inf_amd64-v1.0.0.1.zip 解压后，以管理员权限执行5-runasadmin_register-CA-cer.cmd，然后在COM口处双击，在计算机中查找解压的驱动程序，这样就会有rndis网络了。

Mipi-CSI显示测试
-----------------

|  【测试说明】：通过连接Mipi摄像头检查开发板Mipi-CSI接口。
|  【接口位置】：J1
|  【系统设备】：/dev/video0 
|  【测试操作】：为开发板断电，用fpc排线连接mipi摄像头和开发板。

**测试操作**

|  gst-launch-1.0 v4l2src ! video/x-raw,format=YUY2,width=720,height=480 ! queue max-size-time=0 ! waylandsink enable-tile=true sync=false

**测试结果**

|  可以在显示屏看到摄像头所拍摄的内容
