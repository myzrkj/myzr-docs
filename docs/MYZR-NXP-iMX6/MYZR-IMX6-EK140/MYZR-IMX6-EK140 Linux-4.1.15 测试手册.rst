
MYZR-IMX6-EK140 Linux-4.1.15 测试手册
=======================================

测试环境
---------

- 开发板型号：MYZR-IMX6-EK140-6Y
- 内核版本：Linux-4.1.15
- 文件系统：L4115-core-image-base-myimx6a7.tar.bz2

测试前的准备
-------------

|  1）请按照 :doc:`《Linux快速启动手册》<MYZR-IMX6-EK140 启动手册>` 中的“Linux快速启动” -> “连接设备”进行连接。
|  2）请按照 :doc:`《Linux快速启动手册》<MYZR-IMX6-EK140 启动手册>` 中的“Linux快速启动” -> “启动设备”进行启动。

网口测试
---------

|  MYZR-IMX6-EK140 支持1个百兆网口。

**接口属性**

|  ENET 接口位置：P2

**测试方法**

|  1）配置计算机IP
|  设置计算机有线网卡IP为: 192.168.18.18
|  2）ENET 连接测试
|  连接网线：将评估板“ENET”对应的接口与计算机有线网卡的接口用网线相连接。

- 设置评估板IP:

.. code-block:: shell

   # ifconfig eth0 192.168.18.100

|  执行测试命令:

.. code-block:: shell

   # ping 192.168.18.18 -c 4

- 观察测试结果，系统会输出类似如下信息:

.. code-block:: shell

   PING 192.168.18.18 (192.168.18.18): 56 data bytes
   64 bytes from 192.168.18.18: seq=0 ttl=64 time=2.848 ms
   64 bytes from 192.168.18.18: seq=1 ttl=64 time=0.496 ms
   64 bytes from 192.168.18.18: seq=2 ttl=64 time=0.478 ms
   64 bytes from 192.168.18.18: seq=3 ttl=64 time=0.518 ms

   --- 192.168.18.18 ping statistics ---
   4 packets transmitted, 4 packets received, 0% packet loss
   round-trip min/avg/max = 0.478/1.085/2.848 ms

- 测试结果：“0% packet loss”表示测试通过。

USB 测试
---------

**接口属性**

|  接口位置：P3

**测试方法**

|  1）开始测试 将USB设备(U盘）插入底板USB接口，系统会输出类似如下信息:

.. code-block:: shell

   usb 1-1: new high-speed USB device number 2 using ci_hdrc
   usb-storage 1-1:1.0: USB Mass Storage device detected
   scsi host0: usb-storage 1-1:1.0
   scsi 0:0:0:0: Direct-Access     SMI      USB DISK         1100 PQ: 0 ANSI: 0 CCS
   sd 0:0:0:0: Attached scsi generic sg0 type 0
   sd 0:0:0:0: [sda] 15730688 512-byte logical blocks: (8.05 GB/7.50 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] No Caching mode page found
   sd 0:0:0:0: [sda] Assuming drive cache: write through
    sda:
   sd 0:0:0:0: [sda] Attached SCSI removable disk

|  2）结束测试 将USB设备从底板拔出，系统会输出类似如下信息：

.. code-block:: shell

   usb 1-1: USB disconnect, device number 2

- 测试结果：如上“(8.05 GB/7.50 GiB)”能识别U盘的大小表示测试通过。

TF卡测试
---------

**接口属性**

|  接口位置：P5
|  接口类型：MicroSD

**测试方法**

|  1）开始测试
|  断电下，插入TF卡到底板背面的TF卡接口后再启动系统
|  输入如下命令：

.. code-block:: shell

   # dmesg | grep mmc0

|  系统输出类似以下信息，即表示 TF 接口正常：

.. code-block:: shell

   mmc0: SDHCI controller on 2190000.usdhc [2190000.usdhc] using ADMA
   mmc0: host does not support reading read-only switch, assuming write-enable
   mmc0: new high speed SDHC card at address 1234
   mmcblk0: mmc0:1234 SA32G 28.9 GiB

|  2）查看系统的TF卡设备
|  输入如下命令:

.. code-block:: shell

   # ls /dev/mmcblk0*   

|  系统会输出以下信息：

.. code-block:: shell

   /dev/mmcblk0    /dev/mmcblk0p1

RGB屏测试
-----------

|  测试说明；显示模块的连接不可接错，避免烧板；

- 具体连接参考 :doc:`《Linux快速启动手册》<MYZR-IMX6-EK140 启动手册>` 里的显示屏模块连接里的附图
- 开发板开机进入系统后，屏幕上有如下几行文字显示如下：

.. code-block:: shell

   Freescale i.MX Release Distro 4.1.15-2.1.0 myimxlek140/dev/tty1
   imx6ek140 login:

|  屏幕上出现以上显示则说明屏幕正常。


GPIO-LED 测试（led-heartbeat）
-------------------------------

|  【测试说明】：观察实现为led-heartbeat的LED
|  【接口标识】：USER LIGHT
|  【接口丝印】：D2
|  【系统接口】：/sys/class/leds/Heartbeat/

**测试操作**

|  无需任何操作

**测试结果**

|  系统启动后可以看到 D2 在有规律的闪烁，即表示应该功能正常。


GPIO-LED 测试（led-timer）
---------------------------

|  【测试说明】：控制实现为led-timer（LED）的亮灭时间
|  【接口标识】：USER LIGHT
|  【接口丝印】：D3
|  【系统接口】：/sys/class/leds/led-timer/

**测试操作**

|  更改灭的时间：

.. code-block:: shell

   =====> 输入指令:
   echo 1000 > /sys/class/leds/led-timer/delay_off  

|  更改亮的时间：

.. code-block:: shell

   =====> 输入指令:
   echo 2000 > /sys/class/leds/led-timer/delay_on  

**测试结果**

|  执行上面两条指令后，发现对应LED亮的持续时间为2秒，LED灭的持续时间为1秒。


GPIO-LED 测试（led-default）
------------------------------

|  【测试说明】：控制实现为led-default（LED）的亮灭状态
|  【接口标识】：USER LIGHT
|  【接口丝印】：D4
|  【系统接口】：/sys/class/leds/default/

**测试操作**

|  说明：系统启动后默认状态为常亮。
|  使 D4 灭：

.. code-block:: shell

   =====> 输入指令:
   echo 0 > /sys/class/leds/default/brightness  

|  使 D4 亮：

.. code-block:: shell

   =====> 输入指令:
   echo 1 > /sys/class/leds/default/brightness  

**测试结果**

|  执行指令后，发现对应LED的状态随指令的功能进行改变。


串口测试（UART2）
------------------

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：IO
|  【接口位置】：P7:11,12
|  【系统设备】：/dev/ttymxc1

**测试操作**

|  短接串口2的发送发接收管脚（P7的11和12号管脚）
|  执行测试指令：

.. code-block:: shell

   =====> 输入指令:
   /my-demo/gcc-linaro-5.3-arm/serial_test.out /dev/ttymxc1 "www.myzr.com.cn"  

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
   ASCII: 0x0       Character:

**测试结果**

|  执行测试指令后，应用输出如上类似信息即正常。


串口测试（UART3）
------------------

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：IO
|  【接口位置】：P7:13,14
|  【系统设备】：/dev/ttymxc2

**测试命令**

|  短接串口2的发送发接收管脚（P7的13和14号管脚）
|  执行测试指令：

.. code-block:: shell

   =====> 输入指令:
   /my-demo/gcc-linaro-5.3-arm/serial_test.out /dev/ttymxc2 "www.myzr.com.cn"  

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
   ASCII: 0x0       Character:   

**测试结果**

|  执行测试指令后，应用输出如上类似信息即正常。


SPI测试（ECSPI1）
------------------

|  【测试说明】：采用自发自收的方式测试。
|  【接口标识】：IO
|  【接口丝印】：P8: 24,26
|  【系统设备】：/dev/spidev0.0

**测试操作**

|  短接P8的24和26管脚。
|  执行测试指令

.. code-block:: shell

   =====> 输入指令:
   /my-demo/gcc-linaro-5.3-arm/spidev_test.out -D /dev/spidev0.0   

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

|  执行测试指令后，应用输出如上类似信息即正常。


SPI测试（ECSPI2）
-------------------

|  【测试说明】：采用自发自收的方式测试。
|  【接口标识】：IO
|  【接口丝印】：P8: 23,25
|  【系统设备】：/dev/spidev1.0

**测试操作**

|  短接P8的23和25管脚。
|  执行测试指令

.. code-block:: shell

   =====> 输入指令:
   /my-demo/gcc-linaro-5.3-arm/spidev_test.out -D /dev/spidev1.0   

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

|  执行测试指令后，应用输出如上类似信息即正常。


Watchdog 喂狗测试
------------------

|  【测试说明】：开启看门狗，并使应用程序喂狗。
|  【接口标识】：无
|  【接口丝印】：无
|  【系统设备】：/dev/watchdog

**测试操作**

|  运行看门狗程序，并设置超时时间为4秒，喂狗间隔时间为2秒：

.. code-block:: shell

   =====> 输入指令:
   /unit_tests/wdt_driver_test.out 4 2 1 &  

   =====> 输出信息：
   [1] 831
   Starting wdt_driver (timeout: 4, sleep: 2, test: write)
   Trying to set timeout value=4 seconds
   The actual timeout was set to 4 seconds
   Now reading back -- The timeout is 4 seconds

**测试结果**

|  系统正常工作，表示喂狗功能正常。


wakealarm 唤醒测试
--------------------

|  【测试说明】：设定 wakealarm 事件，之后使系统进入睡眠，等待 wakealarm 事件唤醒。
|  【接口标识】：无
|  【接口丝印】：无
|  【系统设备】：如 /sys/class/rtc/rtc0/wakealarm

**测试操作**

1. 设定 rtc0，使 10 秒后产生 wakealarm 事件

.. code-block:: shell

   =====> 输入指令:
   echo +10 > /sys/class/rtc/rtc0/wakealarm 

2. 使设备进入睡眠

.. code-block:: shell

   =====> 输入指令:
   echo mem > /sys/power/state

   =====> 输出信息：
   PM: Syncing filesystems ... done.
   Freezing user space processes ... (elapsed 0.007 seconds) done.
   Freezing remaining freezable tasks ... (elapsed 0.001 seconds) done.
   Suspending console(s) (use no_console_suspend to debug)

**测试结果**

1. 可以看到开发板的除电源指示灯以外的 LED 都灭了。
2. 10内 LED 的状态又恢复了，并且系统输出类似如下信息：

.. code-block:: shell

   PM: suspend of devices complete after 708.601 msecs
   PM: suspend devices took 0.710 seconds
   PM: late suspend of devices complete after 2.543 msecs
   PM: noirq suspend of devices complete after 2.410 msecs
   Disabling non-boot CPUs ...
   PM: noirq resume of devices complete after 1.494 msecs
   PM: early resume of devices complete after 1.571 msecs
   PM: resume of devices complete after 223.182 msecs
   PM: resume devices took 0.230 seconds
   Restarting tasks ... done.

背光测试
---------

|  【测试说明】：通过设置背光亮度值验证评估板的背光功能。
|  【接口标识】：LCD DISPLAY 　　【系统设备】：backlight

**测试操作**

1. 查看最大背光亮度值。

.. code-block:: shell

   =====> 输入指令:
   cat /sys/class/backlight/backlight/max_brightness

   =====> 输出信息：
   7

2. 设置背光亮度，直接看显示屏亮度。

.. code-block:: shell

   =====> 输入指令:
   echo 5 > /sys/class/backlight/backlight/brightness
   cat /sys/class/backlight/backlight/brightness

   =====> 输出信息：
   5

**测试结果**

|  执行上面的测试命令后会看到显示屏的亮度发生变化。

CPU温度测试
-------------

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

usb识别为网口测试
------------------

|  【测试说明】：通过mini usb线将usb识别为网口
|  【接口标识】：P4
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
   root@myimx6ek140p:/# IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
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

tftp更新镜像
--------------

|  【测试说明】：可更新dtb、zImage、u-boot、u-boot环境变量
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

2. 加载环境变量

**emmc开发板**

.. code-block:: shell

   =====> 输入指令:
   run load_scr_emmc; source ${loadaddr};

   =====> 输出信息：
   reading my_environment_emmc.scr
   1514 bytes read in 14 ms (105.5 KiB/s)
   ## Executing script at 80800000
   
**nand开发板**

.. code-block:: shell

   =====> 输入指令:
   run load_scr_nand; source ${loadaddr};

   =====> 输出信息：
   NAND read: device 0 offset 0x3c0000,size 0x20000
    131072 bytes read:OK
   ## Executing script at 80800000

3. 烧写dtb

.. code-block:: shell

   =====> 输入指令:
   run update_dtb

   =====> 输出信息：
   Using FEC device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'myimx6ek140-6g-256m-emmc.dtb'.
   Load address: 0x80800000
   Loading: ###
            282.2 KiB/s
   done
   Bytes transferred = 34705 (8791 hex)
   writing myimx6ek140-6g-256m-emmc.dtb
   34705 bytes written

4. 烧写zImage

.. code-block:: shell

   =====> 输入指令:
   run update_kern

   =====> 输出信息：
   Using FEC device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'zImage-myimx6a7'.
   Load address: 0x80800000
   Loading: #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            ##
            3.8 MiB/s
   done
   Bytes transferred = 7654360 (74cbd8 hex)
   writing zImage-myimx6a7
   7654360 bytes written

5. 烧写u-boot环境变量

.. code-block:: shell

   =====> 输入指令:
   run update_scr

   =====> 输出信息：
   Using FEC device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'my_environment_emmc.scr'.
   Load address: 0x80800000
   Loading: #
            35.2 KiB/s
   done
   Bytes transferred = 1514 (5ea hex)
   writing my_environment_emmc.scr
   1514 bytes written
   ## Executing script at 80800000
   Saving Environment to MMC...
   Writing to MMC(1)... done

6. 烧写u-boot

.. code-block:: shell

   =====> 输入指令:
   run update_ubot
   
   =====> 输出信息：
   Using FEC device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'uboot-myimx6ek140-6g-256m-emmc.imx'.
   Load address: 0x80800000
   Loading: ####################################################
            3 MiB/s
   done
   Bytes transferred = 752640 (b7c00 hex)
   switch to partitions #0, OK
   mmc1(part 0) is current device

   MMC write: dev # 1, block # 2, count 1022 ... 1022 blocks written: OK
 
复制更新镜像
--------------

|  【测试说明】：可更新dtb、zImage、u-boot环境变量、kernel-modules
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
   tftp -g 192.168.137.99 -r zImage-myimx6a7
   tftp -g 192.168.137.99 -r myimx6ek140-6g-256m-emmc.dtb
   tftp -g 192.168.137.99 -r my_environment_emmc.scr
   tftp -g 192.168.137.99 -r kernel-modules-myimx6a9.tar.bz2

4. 查看系统是否自动挂载分区

.. code-block:: shell

   =====> 输入指令:
   ls /run/media/mmcblk1p1/

   =====> 输出信息：
   my_environment_emmc.scr  myimx6ek140-6g-256m-emmc.dtb  zImage-myimx6a7

**系统自动挂载分区**

1. 复制相应的文件到/run/media/mmcblk1p1/目录，将原文件替换。

.. code-block:: shell

   =====> 输入指令:
   cp zImage-myimx6a7 /run/media/mmcblk1p1/
   cp myimx6ek140-6g-256m-emmc.dtb /run/media/mmcblk1p1/
   cp my_environment_emmc.scr /run/media/mmcblk1p1/

2. 解压更新内核模块

.. code-block:: shell

   =====> 输入指令:
   tar xjvf kernel-modules-myimx6a9.tar.bz2 -C /

3. 保存并重启

.. code-block:: shell

   =====> 输入指令:
   reboot

**若系统没有自动挂载分区**

1. 查看fat分区地址

.. code-block:: shell

   =====> 输入指令:
   fdisk -l

   =====> 输出信息：
   ......
   Device         Boot   Start     End Sectors  Size Id Type
   /dev/mmcblk1p1        20480 1044479 1024000  500M  c W95 FAT32 (LBA)
   /dev/mmcblk1p2      1228800 7733247 6504448  3.1G 83 Linux
   ......

2. 手动挂载

.. code-block:: shell

   =====> 输入指令:
   mount /dev/mmcblk1p1 /mnt

3. 复制相应的文件到/mnt目录，将原文件替换。

.. code-block:: shell

   =====> 输入指令:
   cp zImage-myimx6a7 /mnt
   cp myimx6ek140-6g-256m-emmc.dtb /mnt
   cp my_environment_emmc.scr /mnt

4. 解压更新内核模块

.. code-block:: shell

   =====> 输入指令:
   tar xjvf kernel-modules-myimx6a9.tar.bz2 -C /

5. 保存并重启

.. code-block:: shell

   =====> 输入指令:
   reboot