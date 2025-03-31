
MYZR-IMX6-EK200 Linux-4.1.15 测试手册 v2.0
============================================

第一部分 测试说明
------------------

测试环境
~~~~~~~~~

|  【开发板型号】：MYZR-IMX6-EK200-6Q-1G
|  【内核版本】：Linux-4.1.15
|  【文件系统】：L4115-fsl-image-qt5-myimx6a9.tar.bz2
|  【工具版本】：MfgTool-MYIMX6A9-L4.1.15-Patch.svn297.rar
|  **说明** ：为保证测试无误，建议使用的烧录工具版本应不低于svn297

接口标识图
~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/1275px-Myimx6ek200_front.jpg
   :alt: 1275px-Myimx6ek200_front.jpg

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/963px-Myimx6ek200_rear_view.jpg
   :alt: 963px-Myimx6ek200_rear_view.jpg

第二部分 接口测试
-----------------

网口一测试
~~~~~~~~~~~

|  【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|  【接口标识】：10M/100M Ethernet-1
|  【系统接口】：eth0

**测试操作**

|  配置电脑有线网卡IP为 192.168.137.99。
|  把开发板的这个网口用网线跟电脑网口连接起来。
|  配置开发板网口：

.. code-block:: shell

   =====> 输入指令:
   ifconfig eth1 down
   ifconfig eth0 192.168.137.81

|  测试网口：

.. code-block:: shell

   =====> 输入指令:
   ping 192.168.137.99 -c 2 -w 4 

   =====> 输出信息：
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=0.570 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.365 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.365/0.467/0.570/0.104 ms


**测试结果**

|  “0% packet loss”表示测试通过。

网口二测试
~~~~~~~~~~~

|  【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|  【接口标识】：10M/100M Ethernet-2
|  【系统接口】：eth1

**测试操作**

|  配置电脑有线网卡IP为 192.168.137.99。
|  把开发板的这个网口用网线跟电脑网口连接起来。
|  配置开发板网口：

.. code-block:: shell

   =====> 输入指令:
   ifconfig eth0 down
   ifconfig eth1 192.168.137.82 

|  测试网口：

.. code-block:: shell

   =====> 输入指令:
   ping 192.168.137.99 -c 2 -w 4 

   =====> 输出信息：
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=1.38 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.627 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1001ms
   rtt min/avg/max/mdev = 0.627/1.003/1.380/0.377 ms

**测试结果**

|  “0% packet loss”表示测试通过。

USB接口测试
~~~~~~~~~~~~

|  【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|  【接口标识】：USB HOST
|  【系统接口】：/sys/bus/usb/

**测试方法**

|  将USB设备插入底板USB接口，系统会输出类似如下信息:

.. code-block:: shell

   usb 1-1.2: new high-speed USB device number 5 using ci_hdrc
   usb-storage 1-1.2:1.0: USB Mass Storage device detected
   scsi host1: usb-storage 1-1.2:1.0
   scsi 1:0:0:0: Direct-Access     Mass     Storage Device   1.00 PQ: 0 ANSI: 0 CCS
   sd 1:0:0:0: Attached scsi generic sg0 type 0
   sd 1:0:0:0: [sda] 60776448 512-byte logical blocks: (31.1 GB/28.9 GiB)
   sd 1:0:0:0: [sda] Write Protect is off
   sd 1:0:0:0: [sda] No Caching mode page found
   sd 1:0:0:0: [sda] Assuming drive cache: write through
    sda: sda1
   sd 1:0:0:0: [sda] Attached SCSI removable disk

|  将USB设备从底板拔出，系统会输出类似如下信息：

.. code-block:: shell

   usb 1-1.2: USB disconnect, device number 5

**测试结果**

|  USB存储设备插拔时系统输出如上类似信息即表示正常。

SD接口测试
~~~~~~~~~~~

|  【测试说明】：采用插入并识别TF卡的方式进行测试
|  【接口标识】：SD3
|  【系统接口】：/sys/bus/mmc/

**测试方法**

|  把SD卡插入到这个接口：

.. code-block:: shell

   =====> 输出信息：
   mmc2: new high speed SDHC card at address 1234
   mmcblk2: mmc2:1234 SA32G 28.9 GiB 
    mmcblk2: p1

|  弹出SD卡：

.. code-block:: shell

   =====> 输出信息：
   mmc2: card 1234 removed

**测试结果**

|  SD存储设备插拔时系统输出如上类似信息即表示正常。

标准GPIO测试
~~~~~~~~~~~~~

|  【测试说明】：控制GPIO的输出电平
|  【接口标识】：GPIO/SD2
|  【系统接口】：/sys/class/gpio/

**MYZR-IMX6-EK200可用的IO**

.. code-block:: shell

   J4:3(15),  J4:5(14),  J4:7(10), J4:9(13),   J4:11(12),  J4:13(11)  
   J4:4(LED), J4:6(LED), J4:8(20), J4:10(LED), J4:12(LED), J4:14(NC)  

**GPIO输出低电平测试**

|  配置J4:8为输出低电平的操作方法：

.. code-block:: shell

   =====> 输入指令:
   OUT_IO_OUT_NUM=20
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 

|  用万用表测试管脚J4:8，电压为0V，则表示OK

**GPIO输出高电平测试**

|  配置J4:7为输出高电平的操作方法：

.. code-block:: shell

   =====> 输入指令:
   OUT_IO_OUT_NUM=10 
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  用万用表测试管脚J4:7，电压为3.3V，则表示OK

**其它**

|  控制 GPIO 输出低电平的指令：

.. code-block:: shell

   =====> 输入指令:
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value   

|  控制 GPIO 输出高电平的指令：

.. code-block:: shell

   =====> 输入指令:
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 

GPIO-LED测试（leds-heartbeat）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【测试说明】：观察 leds-heartbeat 的 LED
|  【接口标识】：GPIO-LED
|  【系统接口】：/sys/class/leds/leds-heartbeat/

**测试操作**

|  无需任何操作

**测试结果**

|  系统启动后可以看到 D7 在有规律的闪烁，即表示应该功能正常。

GPIO-LED测试（leds-mmc3）
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【测试说明】：往 eMMC 写数据，同时观察 leds-mmc3 的 LED
|  【接口标识】：GPIO-LED
|  【系统接口】：/sys/class/leds/leds-mmc3/

**测试操作**

.. code-block:: shell

   =====> 输入指令:
   dd if=/dev/zero of=/home/root/test bs=1024k count=128

**测试结果**

|  可以看到往eMMC写数据时，D8亮了。

GPIO-LED测试（leds-timer）
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【测试说明】：观察 leds-timer 的 LED
|  【测试说明】：控制 leds-timer（LED）的亮灭时间
|  【接口标识】：GPIO-LED
|  【系统接口】：/sys/class/leds/leds-timer/

**测试操作**

|  更改 led-timer (D9) 灭的时间

.. code-block:: shell

   =====> 输入指令:
   echo 1000 > /sys/class/leds/leds-timer/delay_off  

|  更改 led-timer (D9) 亮的时间

.. code-block:: shell

   =====> 输入指令:
   echo 2000 > /sys/class/leds/leds-timer/delay_on

**测试结果**

|  执行指令后，观察发现对应LED的亮灭的时间比例基本是2:1。

GPIO-LED测试（leds-gpio）
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【测试说明】：控制 ledss-gpio（LED）的亮灭时间
|  【接口标识】：LED
|  【系统接口】：/sys/class/leds/leds-gpio/

**测试操作**

|  使 D10 灭：

.. code-block:: shell

   =====> 输入指令:
   echo 0 > /sys/class/leds/leds-gpio/brightness

|  使 D10 亮：

.. code-block:: shell

   =====> 输入指令:
   echo 1 > /sys/class/leds/leds-gpio/brightness

**测试结果**

|  执行指令后，发现对应LED的状态随指令的功能进行改变。

GPIO-KEY测试
~~~~~~~~~~~~~~

|  【测试说明】：使用 evtest 进行测试
|  【接口标识】：KEY3, KEY2, KEY1
|  【系统接口】：/dev/input/eventX

**测试操作**

|  运行 evtest 准备测试

.. code-block:: shell

   =====> 输入指令:
   evtest 

   =====> 输出信息：
   No device specified, trying to scan all of /dev/input/event*
   Available devices:
   /dev/input/event0:  WM8962 Beep Generator
   /dev/input/event1:  gpio-keys
   Select the device event number [0-1]: 

|  选择 gpio-keys 所对应的序号

.. code-block:: shell

   =====> 输入指令:
   1

   =====> 输出信息：
   Input driver version is 1.0.1
   Input device ID: bus 0x19 vendor 0x1 product 0x1 version 0x100
   Input device name: "gpio-keys"
   Supported events:
     Event type 0 (EV_SYN)
     Event type 1 (EV_KEY)
       Event code 114 (KEY_VOLUMEDOWN)
       Event code 115 (KEY_VOLUMEUP)
       Event code 116 (KEY_POWER)
   Properties:
   Testing ... (interrupt to exit)

|  按动开发板上的按键

.. code-block:: shell

   Event: time 1537921332.815219, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 1
   Event: time 1537921332.815219, -------------- SYN_REPORT ------------
   Event: time 1537921332.985211, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 0
   Event: time 1537921332.985211, -------------- SYN_REPORT ------------
   Event: time 1537921335.355204, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 1
   Event: time 1537921335.355204, -------------- SYN_REPORT ------------
   Event: time 1537921335.535203, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 0
   Event: time 1537921335.535203, -------------- SYN_REPORT ------------
   Event: time 1537921337.375207, type 1 (EV_KEY), code 116 (KEY_POWER), value 1
   Event: time 1537921337.375207, -------------- SYN_REPORT ------------
   Event: time 1537921337.535204, type 1 (EV_KEY), code 116 (KEY_POWER), value 0
   Event: time 1537921337.535204, -------------- SYN_REPORT ------------

**测试结果**

|  当发生按键时，evtest 会输出相应的信息。

串口测试（UART2）
~~~~~~~~~~~~~~~~~~

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：UART2/3/4/5_TTL
|  【系统设备】：/dev/ttymxc1

**测试操作**

|  短接串口2的发送发接收管脚（J1的7和9号管脚）
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
~~~~~~~~~~~~~~~~~~

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：UART2/3/4/5_TTL
|  【系统设备】：/dev/ttymxc2

**测试操作**

|  短接串口3的发送发接收管脚（J1的11和13号管脚）
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

串口测试（UART4）
~~~~~~~~~~~~~~~~~

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：UART2/3/4/5_TTL
|  【系统设备】：/dev/ttymxc3

**测试操作**

|  短接串口4的发送发接收管脚（J1的15和17号管脚）
|  执行测试指令：

.. code-block:: shell

   =====> 输入指令:
   /my-demo/gcc-linaro-5.3-arm/serial_test.out /dev/ttymxc3 "www.myzr.com.cn"  

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

串口测试（UART5）
~~~~~~~~~~~~~~~~~~

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：UART2/3/4/5_TTL
|  【系统设备】：/dev/ttymxc4

**测试操作**

|  短接串口5的发送发接收管脚（J1的16和18号管脚）
|  执行测试指令：

.. code-block:: shell

   =====> 输入指令:
   /my-demo/gcc-linaro-5.3-arm/serial_test.out /dev/ttymxc4 "www.myzr.com.cn"  

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

CAN 测试
~~~~~~~~~

|  【测试说明】：采用CAN1发送，CAN0接收的方式。
|  【接口标识】：CAN1，CAN2
|  【系统接口】：can0，can1

**测试准备**

|  将CAN1的CAN_L与CAN2的CAN_L连接。
|  将CAN1的CAN_H与CAN2的CAN_H连接。

**测试命令**

|  配置 CAN1（can0）：

.. code-block:: shell

   =====> 输入指令:
   ip link set can0 up type can bitrate 125000

|  配置 CAN2（can1）：

.. code-block:: shell

   =====> 输入指令:
   ip link set can1 up type can bitrate 125000

|  CAN1 (can0) 后台接收：

.. code-block:: shell

   =====> 输入指令:
   candump can0 &  

|  CAN2（can1）发送数据：

.. code-block:: shell

   =====> 输入指令:
   cansend can1 1F334455#1122334455667788 

   =====> 输出信息：
   can0  1F334455   [8]  11 22 33 44 55 66 77 88

**测试结果**

|  CAN2(can1)发送数据后，CAN1(can0)会把接收到的数据输出，如：11 22 33 44 55 66 77 88

SPI测试（ECSPI1）
~~~~~~~~~~~~~~~~~~

|  【测试说明】：采用自发自收的方式测试。
|  【接口标识】：SPI1/2
|  【系统设备】：/dev/spidev0.1

**测试操作**

|  短接J7的7和9管脚。
|  执行测试指令

.. code-block:: shell

   =====> 输入指令:
   /my-demo/gcc-linaro-5.3-arm/spidev_test.out -D /dev/spidev0.1   

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
~~~~~~~~~~~~~~~~~~

|  【测试说明】：采用自发自收的方式测试。
|  【接口标识】：SPI1/2
|  【系统设备】：/dev/spidev1.0

**测试操作**

|  短接J7的8和10管脚。
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

Watchdog 超时复位测试
~~~~~~~~~~~~~~~~~~~~~~

|  【测试说明】：开启看门狗，并等待看门狗超时，产生复位。
|  【接口标识】：无
|  【系统设备】：/dev/watchdog

**测试操作**

|  运行看门狗程序：

.. code-block:: shell

   =====> 输入指令:
   /unit_tests/wdt_driver_test.out 10 15 1  
   
   =====> 输出信息：
   Starting wdt_driver (timeout: 10, sleep: 15, test: write)
   Trying to set timeout value=10 seconds
   The actual timeout was set to 10 seconds
   Now reading back -- The timeout is 10 seconds

**测试结果**

|  运行测试命令10秒后，WatchDog超时，系统被复位。会在终端看到系统重新启动输出的信息类似如下：

.. code-block:: shell

   U-Boot 2016.03-svn351 (Jan 25 2019 - 10:13:51 +0800)

   CPU:   Freescale i.MX6Q rev1.5 996 MHz (running at 792 MHz)
   CPU:   Extended Commercial temperature grade (-20C to 105C) at 48C
   Reset cause: WDOG
   Board: MYZR i.MX6 Evaluation Kit
   Model: MY-IMX6-EK200-6Q-1G

Watchdog 喂狗测试
~~~~~~~~~~~~~~~~~~

|  【测试说明】：开启看门狗，并使应用程序喂狗。
|  【接口标识】：无
|  【系统设备】：/dev/watchdog

**测试操作**

|  运行看门狗程序，并设置超时时间为4秒，喂狗间隔时间为2秒：

.. code-block:: shell

   =====> 输入指令:
   /unit_tests/wdt_driver_test.out 4 2 1 &  
   
   =====> 输出信息：
   [1] 1026
   Starting wdt_driver (timeout: 4, sleep: 2, test: write)
   Trying to set timeout value=4 seconds
   The actual timeout was set to 4 seconds
   Now reading back -- The timeout is 4 seconds

RTC 测试
~~~~~~~~~~

|  【测试说明】：读取并设置时间，断电重启后检查时间是否正确
|  【接口标识】：无
|  【系统设备】：/sys/class/rtc/rtc0/

**测试操作**

1. 断电重启设备，查看当前系统时间和硬件时间：

.. code-block:: shell

   =====> 输入指令: 
   date

   =====> 输出信息：
   Tue Sep 25 22:47:03 UTC 2018

2. 查看当前RTC芯片时钟：

.. code-block:: shell

   =====> 输入指令: 
   hwclock 

   =====> 输出信息：
   Tue Sep 25 22:47:18 2018  0.000000 seconds

3. 设置系统时钟，并同步到RTC芯片

.. code-block:: shell

   =====> 输入指令: 
   date -s "2019-01-14 12:34:56"  

   =====> 输出信息：
   Mon Jan 14 12:34:56 UTC 2019

4. 将系统时钟写入硬件时钟

.. code-block:: shell

   =====> 输入指令:
   hwclock -w  

**测试结果**

1. 断电重启评估板，查看当前系统时钟和硬件时钟

.. code-block:: shell

   =====> 输入指令:
   date

   =====> 输出信息：
   Mon Jan 14 12:36:22 UTC 2019

2. 查看当前RTC芯片时钟

.. code-block:: shell

   =====> 输入指令:
   hwclock  

   =====> 输出信息：
   Mon Jan 14 12:36:40 2019  0.000000 seconds

|  可以看到我们得到的时间与设置的时间基本相同。

WakeAlarm 唤醒测试
~~~~~~~~~~~~~~~~~~~

|  【测试说明】：设定 wakealarm 事件，之后使系统进入睡眠，等待 wakealarm 事件唤醒。
|  【接口标识】：无
|  【系统设备】：如 /sys/class/rtc/rtc1/wakealarm

**测试操作**

1. 设定 rtc1，使 10 秒后产生 wakealarm 事件

.. code-block:: shell

   =====> 输入指令:
   echo +10 > /sys/class/rtc/rtc1/wakealarm 

2. 使设备进入睡眠

.. code-block:: shell

   =====> 输入指令:
   echo mem > /sys/power/state

   =====> 输出信息：
   PM: Syncing filesystems ... done.
   Freezing user space processes ... (elapsed 0.001 seconds) done.
   Freezing remaining freezable tasks ... (elapsed 0.001 seconds) done.
   Suspending console(s) (use no_console_suspend to debug)

**测试结果**

1. 可以看到开发板的除电源指示灯以外的 LED 都灭了。
2. 10秒内 LED 的状态又恢复了，并且系统输出类似如下信息：

.. code-block:: shell

   PM: suspend of devices complete after 90.667 msecs
   PM: suspend devices took 0.090 seconds
   PM: late suspend of devices complete after 1.286 msecs
   PM: noirq suspend of devices complete after 1.272 msecs
   Disabling non-boot CPUs ...
   CPU1: shutdown
   CPU2: shutdown
   CPU3: shutdown
   Enabling non-boot CPUs ...
   CPU1 is up
   CPU2 is up
   CPU3 is up
   PM: noirq resume of devices complete after 1.140 msecs
   PM: early resume of devices complete after 1.114 msecs
   PM: resume of devices complete after 760.379 msecs
   PM: resume devices took 0.760 seconds
   Restarting tasks ... done.

音频播放测试
~~~~~~~~~~~~~

|  【测试说明】：通过播放音频文件验证评估板的音频播放功能。
|  【接口标识】：EAR
|  【系统设备】：wm8960-audio

**测试操作**

|  把耳机插入开发板的“EAR”口。
|  执行测试命令：

.. code-block:: shell

   =====> 输入指令:
   aplay /unit_tests/audio8k16S.wav   

   =====> 输出信息：
   Playing WAVE '/unit_tests/audio8k16S.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Stereo

**测试结果**

|  执行上面的测试命令后会听到音频设备输出的声音。

音频录音测试
~~~~~~~~~~~~~

|  【测试说明】：通过录音并播放录音文件验证评估板的音频录音功能。
|  【接口标识】：MIC
|  【系统设备】：wm8960-audio

**测试操作**

1. 把带MIC的耳机插入开发板的“MIC”口。
2. 将J4:8与J4:16短接
3. 执行录音命令：

.. code-block:: shell

   =====> 输入指令:
   arecord -d 5 -f S16_LE -t wav foobar.wav

   =====> 输出信息：
   Recording WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

4. 播放录音

.. code-block:: shell

   =====> 输入指令:
   aplay foobar.wav

   =====> 输出信息：
   Playing WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

**测试结果**

|  执行上面的测试命令后会听到播放的录音。

背光测试
~~~~~~~~~

|  【测试说明】：通过设置背光亮度值验证评估板的背光功能。
|  【接口标识】：显示屏
|  【系统设备】：backlight

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

usb识别为U盘测试
~~~~~~~~~~~~~~~~~

|  【测试说明】：通过mini usb线在PC识别开发板为U盘
|  【接口标识】：J13
|  【系统设备】：devtmpfs

**测试操作**

1. 创建一个10M大小的文件

.. code-block:: shell

   =====> 输入指令:
   # dd if=/dev/zero of=/dev/shm/disk bs=1024 count=10240

   =====> 输出信息：
   10240+0 records in
   10240+0 records out

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
   root@myimx6ek200:~# g_mass_storage gadget: high-speed config #1: Linux File-Backed Storage

3. 识别U盘

|  此时PC“我的电脑”会出现U盘的驱动器，将其格式化后，便可对其读写

4. 挂载

.. code-block:: shell

   # mount /dev/shm/disk /mnt

**测试结果**

|  在/mnt/下看到在电脑写入的文件，在开发板写入文件，重新插拔MINI USB可在PC看到在开发板写入的新文件。


usb识别为网口测试
~~~~~~~~~~~~~~~~~~

|  【测试说明】：通过mini usb线将usb识别为网口
|  【接口标识】：J13
|  【系统设备】：usb0

**测试操作**

1. 载入模块

.. code-block:: shell

   =====> 输入指令:
   # modprobe g_ether

   =====> 输出信息：
   using random self ethernet address
   using random host ethernet address
   usb0: HOST MAC e6:4f:57:b3:0e:5e
   usb0: MAC 26:82:d6:1d:43:f2
   using random self ethernet address
   using random host ethernet address
   g_ether gadget: Ethernet Gadget, version: Memorial Day 2008
   g_ether gadget: g_ether ready
   root@myimx6ek200:~# IPv6: ADDRCONF(NETDEV_UP): usb0: link is not ready
   g_ether gadget: high-speed config #2: RNDIS
   IPv6: ADDRCONF(NETDEV_CHANGE): usb0: link becomes ready

2. 设置IP

.. code-block:: shell

   =====> 输入指令:
   # ifconfig usb0 192.168.7.2

|  将PC识别的rndis的本地连接IP设置为192.168.7.8

3. 测试网口

.. code-block:: shell

   =====> 输入指令:
   # ping 192.168.7.8 -c 2 -w 4
   =====> 输出信息：
   PING 192.168.7.8 (192.168.7.8) 56(84) bytes of data.
   64 bytes from 192.168.7.8: icmp_seq=1 ttl=64 time=0.583 ms
   64 bytes from 192.168.7.8: icmp_seq=2 ttl=64 time=0.427 ms

   --- 192.168.7.8 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.427/0.505/0.583/0.078 ms

**测试结果**

|  “0% packet loss”表示测试通过

|  注：若WIN10识别rndis为COM口，则需要下载驱动kindle_rndis.inf_amd64-v1.0.0.1.zip 解压后，以管理员权限执行5-runasadmin_register-CA-cer.cmd，然后在COM口处双击，在计算机中查找解压的驱动程序，这样就会有rndis网络了。

CPU温度测试
~~~~~~~~~~~~

|  【测试说明】：查看CPU温度
|  【接口标识】：无
|  【系统设备】：/sys/class/thermal/thermal_zone0/temp

**测试操作**

1. 输入命令

.. code-block:: shell

   =====> 输入指令:
   echo $[$(cat /sys/class/thermal/thermal_zone0/temp)/1000]
   =====> 输出信息：
   49

**测试结果**

|  49表示CPU的温度为49°

tftp更新镜像
~~~~~~~~~~~~~

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

2. 烧写dtb

.. code-block:: shell

   =====> 输入指令:
   run update_dtb
   =====> 输出信息：
   Using FEC device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'myimx6ek200-6q-1g.dtb'.
   Load address: 0x12000000
   Loading: ###
            885.7 KiB/s
   done
   Bytes transferred = 43574 (aa36 hex)
   writing myimx6ek200-6q-1g.dtb
   43574 bytes written

3. 烧写zImage

.. code-block:: shell

   =====> 输入指令:
   run update_kern 
   =====> 输出信息：
   Using FEC device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'zImage-myimx6a9'.
   Load address: 0x12000000
   Loading: #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            #################################################################
            ####
            5.2 MiB/s
   done
   Bytes transferred = 7679976 (752fe8 hex)
   writing zImage-myimx6a9
   7679976 bytes written

4. 烧写u-boot环境变量

.. code-block:: shell

   =====> 输入指令:
   run update_scr 
   =====> 输出信息：
   Using FEC device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'my_environment.scr'.
   Load address: 0x12000000
   Loading: #
            134.8 KiB/s
   done
   Bytes transferred = 2358 (936 hex)
   writing my_environment.scr
   2358 bytes written
   ## Executing script at 12000000
   Saving Environment to SPI Flash...
   SF: Detected SST25VF016B with page size 256 Bytes, erase size 64 KiB, total 2 MiB
   Erasing SPI flash...Writing to SPI flash...done

5. 烧写u-boot

.. code-block:: shell

   =====> 输入指令:
   run update_ubot 
   =====> 输出信息：
   Using FEC device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'uboot-myimx6ek200-6q-1g.imx'.
   Load address: 0x12000000
   Loading: ###########################
            3 MiB/s
   done
   Bytes transferred = 396288 (60c00 hex)
   SF: Detected SST25VF016B with page size 256 Bytes, erase size 64 KiB, total 2 MiB
   SF: 2097152 bytes @ 0x0 Erased: OK
   device 0 offset 0x400, size 0x60c00
   SF: 396288 bytes @ 0x400 Written: OK

复制更新镜像
~~~~~~~~~~~~~

|  【测试说明】：可更新dtb、zImage、u-boot环境变量、内核模块
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
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=64 time=0.311 ms
   64 bytes from 192.168.137.99: seq=1 ttl=64 time=0.510 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.311/0.410/0.510 ms

|  “0% packet loss”表示连接正常。

3. 传输文件

.. code-block:: shell

   =====> 输入指令:
   tftp -g 192.168.137.99 -r zImage-myimx6a9 
   tftp -g 192.168.137.99 -r myimx6ek200-6q-1g.dtb
   tftp -g 192.168.137.99 -r my_environment.scr
   tftp -g 192.168.137.99 -r kernel-modules-myimx6a9.tar.bz2

4. 查看系统是否自动挂载分区

.. code-block:: shell

   =====> 输入指令:
   ls /run/media/mmcblk3p1/
   =====> 输出信息：
   my_environment.scr  myimx6ek200-6q-1g.dtb  zImage-myimx6a9

系统自动挂载分区
~~~~~~~~~~~~~~~~

1. 复制相应的文件到/run/media/mmcblk3p1/目录，将原文件替换。

.. code-block:: shell

   =====> 输入指令:
   cp zImage-myimx6a9 /run/media/mmcblk3p1/
   cp myimx6ek200-6q-1g.dtb /run/media/mmcblk3p1/
   cp my_environment.scr /run/media/mmcblk3p1/

解压更新内核模块
~~~~~~~~~~~~~~~~

.. code-block:: shell

   tar xjvf kernel-modules-myimx6a9.tar.bz2 -C /

2. 保存并重启

.. code-block:: shell

   =====> 输入指令:
   reboot

|  若系统没有自动挂载分区

1. 查看fat分区地址　

.. code-block:: shell

   =====> 输入指令:
   fdisk -l
   =====> 输出信息：
   ......
   Device         Boot   Start      End  Sectors  Size Id Type
   /dev/mmcblk3p1        20480  1044479  1024000  500M  c W95 FAT32 (LBA)
   /dev/mmcblk3p2      1228800 30777343 29548544 14.1G 83 Linux
   ......

2. 手动挂载

.. code-block:: shell

   =====> 输入指令:
   mount /dev/mmcblk3p1 /mnt

3. 复制相应的文件到/mnt目录，将原文件替换。

.. code-block:: shell

   =====> 输入指令:
   cp zImage-myimx6a9 /mnt
   cp myimx6ek200-6q-1g.dtb /mnt
   cp my_environment.scr /mnt

4. 保存并重启

.. code-block:: shell

   =====> 输入指令:
   reboot

第三部分 显示功能测试
----------------------

操作说明
~~~~~~~~~

|  每项显示功能测试都需要重启系统进入到u-boot命令行，并在u-boot命令行下执行指令。

单屏显示
~~~~~~~~~~

- LVDS1 显示

|  说明：默认为 LVDS1 显示，即上电后不干预启动的情况下，LVDS1 为显示设备。
|  显式配置 LVDS1 为显示的方法：

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds1; saveenv; boot

- LVDS0 显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds0; saveenv; boot

- HDMI 显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_hdmi; saveenv; boot

- LCD(RGB) 显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lcd; saveenv; boot

双LVDS屏显示
~~~~~~~~~~~~~~

- LVDS1 + LVDS0 双屏同步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_lvds_dul; saveenv; boot

- LVDS1 + LVDS0(fb4) 双屏异步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_lvds_sep; saveenv; boot

双屏异步显示
~~~~~~~~~~~~~

- LVDS1 + HDMI 双屏异步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds1 $disp_fb1_hdmi; saveenv; boot

- LVDS1 + LCD(RGB) 双屏异步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds1 $disp_fb1_lcd; saveenv; boot

- LVDS0 + HDMI 双屏异步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds0$disp_fb1_hdmi; saveenv; boot

- LVDS0 + LCD(RGB) 双屏异步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lvds0 $disp_fb1_lcd; saveenv; boot

- HDMI + LVDS1 双屏异步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_hdmi $disp_fb1_lvds1; saveenv; boot

- HDMI + LVDS0 双屏异步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_hdmi $disp_fb1_lvds0; saveenv; boot

- LCD(RGB) + LVDS1 双屏异步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lcd $disp_fb1_lvds1; saveenv; boot

- LCD(RGB) + LVDS0 双屏异步显示

.. code-block:: shell

   run load_scr; source; setenv display $disp_fb0_lcd $disp_fb1_lvds0; saveenv; boot

视频播放测试
~~~~~~~~~~~~~

- 设置Linux的环境变量

.. code-block:: shell

   # export GSTL=gst-launch-1.0
   # export PLAYBIN=playbin
   # export GPLAY=gplay-1.0
   # export GSTINSPECT=gst-inspect-1.0
   # export MP4_FILE="///unit_tests/akiyo.mp4"

- 播放视频到主显示屏

.. code-block:: shell

   # $GSTL $PLAYBIN uri=file:$MP4_FILE video-sink="imxv4l2sink device=/dev/video17"

- 播放视频到第二显示屏

.. code-block:: shell

   # $GSTL $PLAYBIN uri=file:$MP4_FILE video-sink="imxv4l2sink device=/dev/video18"

第四部分 扩展模块功能演示
--------------------------

RTL8188 模块功能演示（WIFI Client）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【测试说明】：使用RTL8188作为无线网卡连接到WIFI AP。
|  【接口标识】：WIFI、WIFI_ANT
|  【系统设备】：wlan0

**测试操作**

1. 确定“WIFI”标识处有贴上WIFI模块，否则无需进行测试。
2. 把WIFI天线连接到“WIFI_ANT”标识的接口上。
3. 生成 SSID 的 WPA PSK 文件

`命令格式: wpa_passphrase <ssid> [passphrase]`

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
   ==> rtl8188e_iol_efuse_patch
   IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
   ......

5. 获取 IP

.. code-block:: shell

   =====> 输入指令:
   udhcpc -i wlan0

   =====> 输出信息：
   udhcpc (v1.23.1) started
   Sending discover...
   Sending select for 192.168.43.121...
   Lease of 192.168.43.121 obtained, lease time 3600
   /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

6. 测试连接

.. code-block:: shell

   =====> 输入指令:
   ping -I wlan0 192.168.43.1 -c 2 -w 4

   =====> 输出信息：
   PING 192.168.43.1 (192.168.43.1) from 192.168.43.130 wlan0: 56(84) bytes of data.
   64 bytes from 192.168.43.1: icmp_seq=1 ttl=64 time=5.66 ms
   64 bytes from 192.168.43.1: icmp_seq=2 ttl=64 time=9.22 ms

   --- 192.168.43.1 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1000ms
   rtt min/avg/max/mdev = 5.663/7.444/9.226/1.783 ms

**测试结果**

|  “0% packet loss”表示WIFI连接正常。

RTL8188 模块功能演示（WIFI AP mode）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【测试说明】：使用RTL8188作为WIFI AP，并把手机连接到此AP。
|  【接口标识】：WIFI、WIFI_ANT
|  【系统设备】：wlan0

**测试操作**

1. 确定“WIFI”标识处有贴上WIFI模块，否则无需进行测试。
2. 把WIFI天线连接到“WIFI_ANT”标识的接口上。
3. 为 wlan0 配置 IP：

.. code-block:: shell

   =====> 输入指令:
   ifconfig wlan0 192.168.99.1

   =====> 输出信息：
   ==> rtl8188e_iol_efuse_patch
   IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready

4. 为 wlan0 启用 DHCP 服务：

.. code-block:: shell

   =====> 输入指令:
   touch /var/lib/misc/udhcpd.leases
   udhcpd -f /etc/my_udhcpd.conf &

   =====> 输出信息：
   [1] 469
   udhcpd (v1.23.1) started

5. 为 wlan0 启用 Host-AP 功能

.. code-block:: shell

   =====> 输入指令:
   hostapd /etc/my_hostapd.conf -B

   =====> 输出信息：
   Configuration file: /etc/my_hostapd.conf
   rfkill: Cannot open RFKILL control device
   Using interface wlan0 with hwaddr e0:b9:4d:7f:e4:40 and ssid "MY_HOSTAP_V25"
   RTL871X: set group key camid:1, addr:00:00:00:00:00:00, kid:1, type:AES
   wlan0: interface state UNINITIALIZED->ENABLED
   wlan0: AP-ENABLED

6. 客户端设备连接到 Host-AP

|  至此，开发板的 Host-AP 功能已启用，客户端设备可搜索“MY_HOSTAP_V25”，通过密码“myzr2012”连接到此AP。

**测试结果**

1. 设备连接成功时产生的信息

.. code-block:: shell

   =====> 输出信息：
   Sending OFFER of 192.168.12.20
   Sending OFFER of 192.168.12.20
   Sending ACK to 192.168.12.20

2. 设备断开连接时产生的信息

.. code-block:: shell

   =====> 输出信息：
   RTL871X: OnDeAuth(wlan0) reason=3, ta=b4:0b:44:f5:64:2f
   RTL871X: clear key for addr:b4:0b:44:f5:64:2f, camid:4

EC20 模块测试
~~~~~~~~~~~~~~

|  【测试说明】：4G连接成功后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：MINI_PCIE
|  【系统设备】：eth2

**测试操作**

1. 开发板断电，接上4G模块，接上天线并插入SIM卡后启动评估板。
2. 使用指令进行网络连接：

.. code-block:: shell

   =====> 输入指令:
   /my-demo/gcc-linaro-5.3-arm/quectel-CM &

   =====> 输出信息：
   [1] 540
   [12-18_03:17:06:719] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
   [12-18_03:17:06:720] /my-demo/gcc-linaro-5.3-arm/quectel-CM profile[1] = (null)/(null)/(null)/0, pincode = (null)
   [12-18_03:17:06:723] Find /sys/bus/usb/devices/1-1.2 idVendor=2c7c idProduct=0125
   [12-18_03:17:06:723] Find /sys/bus/usb/devices/1-1.2:1.4/net/eth2
   [12-18_03:17:06:723] Find usbnet_adapter = eth2
   [12-18_03:17:06:723] Find /sys/bus/usb/devices/1-1.2:1.4/GobiQMI/qcqmi2
   [12-18_03:17:06:724] Find qmichannel = /dev/qcqmi2
   [12-18_03:17:06:794] Get clientWDS = 7
   [12-18_03:17:06:826] Get clientDMS = 8
   [12-18_03:17:06:858] Get clientNAS = 9
   [12-18_03:17:06:890] Get clientUIM = 10
   [12-18_03:17:06:922] Get clientWDA = 11
   [12-18_03:17:06:954] requestBaseBandVersion EC20CEFAR02A10M4G
   [12-18_03:17:07:050] requestGetSIMStatus SIMStatus: SIM_READY
   [12-18_03:17:07:082] requestGetProfile[1] cmnet///0
   [12-18_03:17:07:114] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [12-18_03:17:07:146] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
   [12-18_03:17:07:223] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [12-18_03:17:07:274] requestSetupDataCall WdsConnectionIPv4Handle: 0x8777e7a0
   [12-18_03:17:07:370] requestQueryDataCall IPv4ConnectionStatus: CONNECTED
   [12-18_03:17:07:403] ifconfig eth2 up
   [12-18_03:17:07:452] busybox udhcpc -f -n -q -t 5 -i eth2
   [12-18_03:17:07:492] udhcpc (v1.23.1) started
   [12-18_03:17:07:656] Sending discover...
   [12-18_03:17:07:706] Sending select for 10.25.154.46...
   [12-18_03:17:07:766] Lease of 10.25.154.46 obtained, lease time 7200
   [12-18_03:17:07:888] /etc/udhcpc.d/50default: Adding DNS 211.136.17.107
   [12-18_03:17:07:888] /etc/udhcpc.d/50default: Adding DNS 211.136.20.203

3. 测试连接

.. code-block:: shell

   =====> 输入指令:
   ping -I eth2 www.baidu.com -c 2 -w 4

   =====> 输出信息：
   PING www.baidu.com (14.215.177.38): 56 data bytes
   64 bytes from 14.215.177.38: seq=0 ttl=49 time=15.753 ms
   64 bytes from 14.215.177.38: seq=1 ttl=49 time=11.835 ms

   --- www.baidu.com ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 11.835/13.794/15.753 ms

**测试结果**

|  “0% packet loss”表示WIFI连接正常。

OV5642摄像头 测试
~~~~~~~~~~~~~~~~~~

|  【测试说明】：屏幕显示图像。
|  【接口标识】：CAMARE
|  【系统设备】：video*

**测试操作**

1. 开发板断电，在"CAMARE"接上OV5642摄像头，接上摄像头后启动评估板。
2. 使用指令进行测试

.. code-block:: shell

   # /unit_tests/mxc_v4l2_overlay.out -iw 640 -ih 480 -it 0 -il 0 -ow 640 -oh 480 -ot 20 -ol 20 -r 0 -t 50 -do 0 -fg -fr 30

4路视频采集模块（选配）测试
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【测试说明】：屏幕显示田字格4个图像。
|  【接口标识】：MINI_PCIE
|  【系统设备】：video0-video7

**测试操作**

1. 开发板断电，接上tw6865四路摄像头模块，接上摄像头后启动评估板。
2. 使用指令进行测试

.. code-block:: shell

   # EXEC_FILE=/my-demo/linux-4.1.15/MY_TW6865_DEMO_L4115_MYIMX6A9.out
   # ${EXEC_FILE} -x 2 -ot 0 -ol 0 -ow 512 -oh 300 -m 2 &
   # ${EXEC_FILE} -x 3 -ot 0 -ol 512 -ow 512 -oh 300 -m 2 &
   # ${EXEC_FILE} -x 4 -ot 300 -ol 0 -ow 512 -oh 300 -m 2 &
   # ${EXEC_FILE} -x 5 -ot 300 -ol 512 -ow 512 -oh 300 -m 2 &
