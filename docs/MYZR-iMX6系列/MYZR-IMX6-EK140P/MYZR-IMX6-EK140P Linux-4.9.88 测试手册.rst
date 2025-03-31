
MYZR-IMX6-EK140P Linux-4.9.88 测试手册
=========================================

测试环境
---------

|   【开发板型号】：MYZR-IMX6-EK140P Linux-4.1.15 测试手册-IMX6-EK140P-6Y-512M-4G
|   【内核版本】：Linux-4.1.15
|   【文件系统】：L4115-fsl-image-qt5-myimx6a7.tar.bz2
|   【工具版本】：MfgTool-MYIMX6A7-L4.1.15-Patch.svn268.rar
|   **说明**：为保证测试无误，需要使用的烧录工具版本应不低于svn268


接口标识图
------------

.. figure:: /image/MYZR-iMX6系列/MYZR-IMX6-EK140P/1425px-MYIMX6A7-MB140P-Port-F.png
   :alt: 1425px-MYIMX6A7-MB140P-Port-F.png

网口测试（ETH1）
-----------------

|   【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|   【接口标识】：ETH1
|   【接口丝印】：P10
|   【系统接口】：eth0

**测试操作**

|   配置电脑有线网卡IP为 192.168.137.99。
|   用网线连接开发板的ETH1和电脑。
|   配置开发板网口：

.. code-block:: shell

   =====> 输入指令:
   ifconfig eth1 down 
   ifconfig eth0 192.168.137.81

|   测试ETH1（eth0）：

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

|   “0% packet loss”表示测试通过。


网口测试（ETH2）
----------------

|   【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|   【接口标识】：ETH2
|   【接口丝印】：P8
|   【系统接口】：eth1

**测试操作**

|   注意：检查"丝印P5"上的跳线帽，保证是接上状态。
|   配置电脑有线网卡IP为 192.168.137.99。
|   用网线连接开发板的ETH2和电脑。
|   配置开发板网口：

.. code-block:: shell

   =====> 输入指令:
   ifconfig eth0 down
   ifconfig eth1 192.168.137.82 

|   测试ETH2（eth1）：

.. code-block:: shell

   =====> 输入指令:
   ping 192.168.137.99 -c 2 -w 4 

   =====> 输出信息：
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.705 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.386 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.386/0.545/0.705/0.161 ms

**测试结果**

|   “0% packet loss”表示测试通过。


USB 测试
----------

|   【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|   【接口标识】：USB HOST
|   【接口丝印】：P20

**测试方法**

|   将USB设备插入底板USB接口，系统会输出类似如下信息:

.. code-block:: shell

   usb 1-1.3: new high-speed USB device number 4 using ci_hdrc
   usb-storage 1-1.3:1.0: USB Mass Storage device detected
   scsi host0: usb-storage 1-1.3:1.0
   scsi 0:0:0:0: Direct-Access     Mass     Storage Device   1.00 PQ: 0 ANSI: 0 CCS
   sd 0:0:0:0: Attached scsi generic sg0 type 0
   sd 0:0:0:0: [sda] 7716864 512-byte logical blocks: (3.95 GB/3.68 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] No Caching mode page found
   sd 0:0:0:0: [sda] Assuming drive cache: write through
   sda: sda1 sda2
   sd 0:0:0:0: [sda] Attached SCSI removable disk

|   将USB设备从底板拔出，系统会输出类似如下信息：

.. code-block:: shell

   usb 1-1.3: USB disconnect, device number 4

**测试结果**

|   USB存储设备插拔时系统输出如上类似信息即表示正常。


SD接口测试
------------

|   【测试说明】：采用插入并识别TF卡的方式进行测试
|   【接口标识】：SD
|   【接口丝印】：P13

**测试方法**

|   为开发板断电，把TF卡安装到SD接口。
|   查看内核中驱动输出信息

.. code-block:: shell

   =====> 输入指令:
   dmesg | grep mmc0  

   =====> 输出信息：
   mmc0: SDHCI controller on 2190000.usdhc [2190000.usdhc] using ADMA  
   mmc0: host does not support reading read-only switch, assuming write-enable  
   mmc0: new high speed SDHC card at address 1234  
   mmcblk0: mmc0:1234 SA32G 29.0 GiB

|   查看系统的SD接口设备

.. code-block:: shell

   =====> 输入指令:
   ls /dev/mmcblk0*   

   =====> 输出信息：
   /dev/mmcblk0    ...

**测试结果**

|   SD存储设备插拔时系统输出如上类似信息即表示正常。


标准 GPIO 测试
----------------

|   【测试说明】：控制GPIO的输出电平
|   【接口标识】：SPI/I2C/GPIO
|   【接口丝印】：P21
|   【系统接口】：/sys/class/gpio/

**GPIO输出低电平测试**

|   配置 P21:35 为输出低电平的操作方法：

.. code-block:: shell

   =====> 输入指令:
   OUT_IO_OUT_NUM=4 
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|   用万用表测试管脚P21:35，电压为0V，则表示OK

**GPIO输出高电平测试**

|   配置 P21:36 为输出高电平的操作方法：

.. code-block:: shell

   =====> 输入指令:
   OUT_IO_OUT_NUM=3  
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|   用万用表测试管脚P21:36，电压为3.3V，则表示OK

**其它**

|   控制 GPIO 输出低电平的指令：

.. code-block:: shell

   =====> 输入指令:
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value   

|   控制 GPIO 输出高电平的指令：

.. code-block:: shell

   =====> 输入指令:
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|   其它可用GPIO：P21:33,34,23；对应的 IO序号Number 为：2,1,110

GPIO-LED 测试（led-heartbeat）
-------------------------------

|   【测试说明】：观察实现为led-heartbeat的LED
|   【接口标识】：LED
|   【接口丝印】：D12
|   【系统接口】：/sys/class/leds/Heartbeat/

**测试操作**

|   无需任何操作

**测试结果**

|   系统启动后可以看到 D12 在有规律的闪烁，即表示应该功能正常。

GPIO-LED 测试（leds-gpio）
----------------------------

|  【测试说明】：控制实现为leds-gpio（LED）的亮灭时间
|  【接口标识】：LED
|  【接口丝印】：D8
|  【系统接口】：/sys/class/leds/leds-gpio/

**测试操作**

|   使 D8 灭：

.. code-block:: shell

   =====> 输入指令:
   echo 1 > /sys/class/leds/leds-gpio/brightness

|   使 D8 亮：

.. code-block:: shell

   =====> 输入指令:
   echo 0 > /sys/class/leds/leds-gpio/brightness  

**测试结果**

|   执行指令后，发现对应LED的状态随指令的功能进行改变。


GPIO-LED 测试（led-default）
-----------------------------

|   【测试说明】：控制实现为led-default（LED）的亮灭状态
|   【接口标识】：LED
|   【接口丝印】：D11
|   【系统接口】：/sys/class/leds/led-timer/

**测试操作**

|   说明：系统启动后默认状态为常亮。
|   使 D11 灭：

.. code-block:: shell

   =====> 输入指令:
   echo 0 > /sys/class/leds/default/brightness

|   使 D11 亮：

.. code-block:: shell

   =====> 输入指令:
   echo 1 > /sys/class/leds/default/brightness  

**测试结果**

|   执行指令后，发现对应LED的状态随指令的功能进行改变。


PWM 测试（PWM-LED）
--------------------

|   【测试说明】：控制连接到PWM5的LED其亮灭时间
|   【接口标识】：无
|   【接口丝印】：D7（在“USB HOST”标识附近）
|   【系统接口】：/sys/class/pwm/pwmchip4/

**测试操作**

|   控制 PWM5 的占空时间：

.. code-block:: shell

   =====> 输入指令:
   PWM_DEV=pwmchip4
   echo 0 > /sys/class/pwm/$PWM_DEV/export 
   echo 1000000000 > /sys/class/pwm/$PWM_DEV/pwm0/period
   echo 100000000 > /sys/class/pwm/$PWM_DEV/pwm0/duty_cycle
   echo 1 > /sys/class/pwm/$PWM_DEV/pwm0/enable

**测试结果**

|   可以看到对应的 LED 在 1 秒(1000000000 纳秒)内闪烁一次(高电平持续时间为 100000000 纳秒 = 0.1 秒)。


PWM 测试（PWM-Buzzer）
-----------------------

|   【测试说明】：控制连接到PWM2的蜂鸣器
|   【接口标识】：BUZZER
|   【接口丝印】：P17
|   【系统接口】：/sys/class/pwm/pwmchip1/

**测试操作**

|   控制 PWM2 的占空时间：

.. code-block:: shell

   =====> 输入指令:
   PWM_DEV=pwmchip1
   echo 0 > /sys/class/pwm/$PWM_DEV/export 
   echo 1000000000 > /sys/class/pwm/$PWM_DEV/pwm0/period
   echo 100000000 > /sys/class/pwm/$PWM_DEV/pwm0/duty_cycle
   echo 1 > /sys/class/pwm/$PWM_DEV/pwm0/enable

**测试结果**

|   可以听到蜂鸣器在 1 秒(1000000000 纳秒)内响一次(高电平持续时间为 100000000 纳秒 = 0.1 秒)。


串口测试（UART2）
------------------

|   【测试说明】：采用串口自发自收的方式进行测试
|   【接口标识】：SPI/I2C/GPIO
|   【接口位置】：P21:27,28
|   【系统设备】：/dev/ttymxc1

**测试操作**

|   短接串口2的发送发接收管脚（P21的27和28号管脚）
|   执行测试指令：

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

|   执行测试指令后，应用输出如上类似信息即正常。


串口测试（UART3）
-------------------

|   【测试说明】：采用串口自发自收的方式进行测试
|   【接口标识】：SPI/I2C/GPIO
|   【接口位置】：P21:25,26
|   【系统设备】：/dev/ttymxc2

**测试命令**

|   短接串口2的发送发接收管脚（P21的25和26号管脚）
|   执行测试指令：

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

|   执行测试指令后，应用输出如上类似信息即正常。


RS485 测试
------------

|   【测试说明】：RS485是差分信号，不能采用自发自收的方式进行测试。如果采用两个开发板进行测试，连接好 RS485 后，参照串口的测试方法即可。


CAN 测试
----------

|   【测试说明】：采用CAN1发送，CAN0接收的方式。
|   【接口标识】：CAN1（对应系统里的can0）；CAN2（对应系统里的can1）
|   【接口丝印】：CAN1 P7:1,2；CAN2 P9:1,2


**测试准备**

|   将CAN1的CAN_L（P7:1）与CAN2的CAN_L（P9:1）连接。
|   将CAN1的CAN_H（P7:2）与CAN2的CAN_H（P9:2）连接。

**测试命令**

|   配置 CAN1（can0）：

.. code-block:: shell

   =====> 输入指令:
   ip link set can0 up type can bitrate 125000  

   =====> 输出信息：
   flexcan 2090000.can can0: writing ctrl=0x0e312005
   IPv6: ADDRCONF(NETDEV_CHANGE): can0: link becomes ready

|   配置 CAN2（can1）：

.. code-block:: shell

   =====> 输入指令:
   ip link set can1 up type can bitrate 125000  

   =====> 输出信息：
   flexcan 2094000.can can1: writing ctrl=0x0e312005
   IPv6: ADDRCONF(NETDEV_CHANGE): can1: link becomes ready

|   CAN1 (can0) 后台接收：

.. code-block:: shell

   =====> 输入指令:
   candump can0 &  

   =====> 输出信息：
   [1] 589

|   CAN2（can1）发送数据：

.. code-block:: shell

   =====> 输入指令:
   cansend can1 1F334455#1122334455667788 

   =====> 输出信息：
   can0  1F334455   [8]  11 22 33 44 55 66 77 88

SPI测试（ECSPI1）
-------------------

|   【测试说明】：采用自发自收的方式测试。
|   【接口标识】：SPI/I2C/GPIO
|   【接口丝印】：P21: 3,4
|   【系统设备】：/dev/spidev0.0

**测试操作**

|   短接P21的3和4管脚。
|   执行测试指令

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

|   执行测试指令后，应用输出如上类似信息即正常。


SPI测试（ECSPI2）
------------------

|   【测试说明】：采用自发自收的方式测试。
|   【接口标识】：SPI/I2C/GPIO
|   【接口丝印】：P21: 9,10
|   【系统设备】：/dev/spidev1.0

**测试操作**

|   短接P21的9和10管脚。
|   执行测试指令

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

|   执行测试指令后，应用输出如上类似信息即正常。


Watchdog 超时复位测试
----------------------

|   【测试说明】：开启看门狗，并等待看门狗超时，产生复位。
|   【接口标识】：无
|   【接口丝印】：无
|   【系统设备】：/dev/watchdog

**测试操作**

|   运行看门狗程序：

.. code-block:: shell

   =====> 输入指令:
   /unit_tests/Watchdog/wdt_driver_test.out 10 15 1

   =====> 输出信息：
   Starting wdt_driver (timeout: 10, sleep: 15, test: write)
   Trying to set timeout value=10 seconds
   The actual timeout was set to 10 seconds
   Now reading back -- The timeout is 10 seconds

**测试结果**

|   运行测试命令10秒后，WatchDog超时，系统被复位。会在终端看到系统重新启动输出的信息类似如下：

.. code-block:: shell

   U-Boot 2016.03-svn270 (Oct 08 2018 - 16:52:53 +0800)

   CPU:   Freescale i.MX6ULL rev1.0 528 MHz (running at 396 MHz)
   CPU:   Industrial temperature grade (-40C to 105C) at 51C
   Reset cause: WDOG
   Board: MYIMX6EK140P-6Y

Watchdog 喂狗测试
-------------------

|   【测试说明】：开启看门狗，并使应用程序喂狗。
|   【接口标识】：无
|   【接口丝印】：无
|   【系统设备】：/dev/watchdog

**测试操作**

|   运行看门狗程序，并设置超时时间为4秒，喂狗间隔时间为2秒：

.. code-block:: shell

   =====> 输入指令:
   /unit_tests/Watchdog/wdt_driver_test.out 4 2 1 &  

   =====> 输出信息：
   [1] 831
   Starting wdt_driver (timeout: 4, sleep: 2, test: write)
   Trying to set timeout value=4 seconds
   The actual timeout was set to 4 seconds
   Now reading back -- The timeout is 4 seconds

**测试结果**

|   系统正常工作，表示喂狗功能正常。


RTC 测试
----------

|   【测试说明】：读取并设置时间，断电重启后检查时间是否正确
|   【接口标识】：无
|   【接口丝印】：无
|   【系统设备】：/sys/class/rtc/rtc0/

**测试操作**

1. 断电重启设备，查看当前系统时间和硬件时间：

.. code-block:: shell

   =====> 输入指令:
   date  

   =====> 输出信息：
   Wed Sep 19 17:39:19 UTC 2018

2. 查看当前RTC芯片时钟：

.. code-block:: shell

   =====> 输入指令:
   hwclock 

   =====> 输出信息：
   Wed Sep 19 17:40:05 2018  0.000000 seconds

3. 设置系统时钟，并同步到RTC芯片

.. code-block:: shell

   =====> 输入指令:
   date -s "2018-09-21 12:34:56"  

   =====> 输出信息：
   Fri Sep 21 12:34:56 UTC 2018

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
   Fri Sep 21 12:36:02 UTC 2018

2. 查看当前RTC芯片时钟

.. code-block:: shell

   =====> 输入指令:
   hwclock  

   =====> 输出信息：
   Fri Sep 21 12:36:12 2018  0.000000 seconds 

|   可以看到我们得到的时间与设置的时间基本相同。

wakealarm 唤醒测试
--------------------

|   【测试说明】：设定 wakealarm 事件，之后使系统进入睡眠，等待 wakealarm 事件唤醒。
|   【接口标识】：无
|   【接口丝印】：无
|   【系统设备】：如 /sys/class/rtc/rtc1/wakealarm

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
   Freezing user space processes ... (elapsed 0.007 seconds) done.
   Freezing remaining freezable tasks ... (elapsed 0.001 seconds) done.
   Suspending console(s) (use no_console_suspend to debug)

**测试结果**

|   1. 可以看到开发板的除电源指示灯以外的 LED 都灭了。
|   2. 10内 LED 的状态又恢复了，并且系统输出类似如下信息：

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

ADC 测试
---------

|   【测试说明】：系统默认配置CPU的GPIO1_IO01和GPIO1_IO02为ADC。
|   【接口标识】：SPI/I2C/GPIO
|   【接口丝印】：P21:34，P21:33
|   【系统设备】：/sys/bus/iio/devices/iio:device0/

**测试操作**

1. 获取 ADC1_IN1 采集到的数据

.. code-block:: shell

   =====> 输入指令:
   cat /sys/bus/iio/devices/iio\:device0/in_voltage1_raw

   =====> 输出信息：
   848

2. 获取 ADC1_IN2 采集到的数据

.. code-block:: shell

   =====> 输入指令:
   cat /sys/bus/iio/devices/iio\:device0/in_voltage2_raw

   =====> 输出信息：
   1

**测试结果**

|   输出的值为 ADC 采集到的数值。 
|   `采样的最大电压不能超过3.3V，否则可能导致核心板损坏，采样的最大输出值为 4096。`


音频播放测试
-------------

|   【测试说明】：通过播放音频文件验证评估板的音频播放功能。
|   【接口标识】：HP/MIC
|   【接口丝印】：P12
|   【系统设备】：wm8960-audio

**测试操作**

|   把耳机插入开发板的“HP/MIC”口。
|   执行测试命令：

.. code-block:: shell

   =====> 输入指令:
   aplay /unit_tests/ASRC/audio8k16S.wav

   =====> 输出信息：
   Playing WAVE '/unit_tests/audio8k16S.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Stereo  

**测试结果**

|   执行上面的测试命令后会听到音频设备输出的声音。


音频录音测试
--------------

|   【测试说明】：通过录音并播放录音文件验证评估板的音频录音功能。
|   【接口标识】：HP/MIC
|   【接口丝印】：P12
|   【系统设备】：wm8960-audio

**测试操作**

1. 把带MIC的耳机插入开发板的“HP/MIC”口。
2. 执行录音命令：

.. code-block:: shell

   =====> 输入指令:
   arecord -d 5 -f S16_LE -t wav foobar.wav  

   =====> 输出信息：
   Recording WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

3. 播放录音

.. code-block:: shell

   =====> 输入指令:
   aplay foobar.wav  

   =====> 输出信息：
   Playing WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

**测试结果**

|   执行上面的测试命令后会听到播放的录音。

背光测试
---------

|   【测试说明】：通过设置背光亮度值验证评估板的背光功能。
|   【接口标识】：显示屏
|   【系统设备】：backlight

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

|   执行上面的测试命令后会看到显示屏的亮度发生变化。

usb识别为U盘测试
------------------

|   【测试说明】：通过mini usb线在PC识别开发板为U盘
|   【接口标识】：p18
|   【系统设备】：devtmpfs

**测试操作**

1. 创建一个10M大小的文件

.. code-block:: shell

   =====> 输入指令:
   # dd if=/dev/zero of=/dev/shm/disk bs=1024 count=10240

   =====> 输出信息：
   10240+0 records in
   10240+0 records out
   10485760 bytes (10 MB, 10 MiB) copied, 0.164056 s, 63.9 MB/s

2. 载入模块

.. code-block:: shell

   =====> 输入指令:
   # modprobe g_mass_storage stall=0 file=/dev/shm/disk removable=1

   =====> 输出信息：
   Mass Storage Function, version: 2009/09/11
   LUN: removable file: (no medium)
   LUN: removable file: /dev/shm/disk
   Number of LUNs=1
   g_mass_storage gadget: Mass Storage Gadget, version: 2009/09/11
   g_mass_storage gadget: userspace failed to provide iSerialNumber
   g_mass_storage gadget: g_mass_storage ready
   root@myimx6ek140p:~# g_mass_storage gadget: high-speed config #1: Linux File-Backed Storage

3. 识别U盘

|   此时PC“我的电脑”会出现U盘的驱动器，将其格式化后，便可对其读写

4. 挂载

.. code-block:: shell
   
   # mount /dev/shm/disk /mnt

**测试结果**

|   在/mnt/下看到在电脑写入的文件，在开发板写入文件，重新插拔MINI USB可在PC看到在开发板写入的新文件。

usb识别为网口测试
-------------------

|   【测试说明】：通过mini usb线将usb识别为网口
|   【接口标识】：P18
|   【系统设备】：usb0

**测试操作**

1. 载入模块

.. code-block:: shell

   =====> 输入指令:
   # uname -r

   =====> 输出信息：
   4.9.88-myimx6

|  将/lib/modules/中的4.9.88-myimx6*文件名称 改为uname -r中的名称如：

.. code-block:: shell

   # mv /lib/modules/4.9.88-myimx6-svn441/ /lib/modules/4.9.88-myimx6
   # depmod -a
   =====> 输入指令:
   # modprobe g_ether

   =====> 输出信息：
   using random self ethernet address
   using random host ethernet address
   usb0: HOST MAC 3a:26:8c:40:8b:f6
   usb0: MAC 66:4a:a4:ee:79:1e
   using random self ethernet address
   using random host ethernet address
   g_ether gadget: Ethernet Gadget, version: Memorial Day 2008
   g_ether gadget: g_ether ready
   root@myimx6ek140p:~# g_ether gadget: high-speed config #2: RNDIS

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
   64 bytes from 192.168.7.8: icmp_seq=1 ttl=64 time=1.11 ms
   64 bytes from 192.168.7.8: icmp_seq=2 ttl=64 time=0.536 ms

   --- 192.168.7.8 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 1001ms
   rtt min/avg/max/mdev = 0.536/0.825/1.114/0.289 ms

**测试结果**

|   “0% packet loss”表示测试通过
|   `注：若WIN10识别rndis为COM口，则需要下载驱动kindle_rndis.inf_amd64-v1.0.0.1.zip 解压后，以管理员权限执行5-runasadmin_register-CA-cer.cmd，然后在COM口处双击，在计算机中查找解压的驱动程序，这样就会有rndis网络了。`

CPU温度测试
-------------

|   【测试说明】：查看CPU温度
|   【接口标识】：无
|   【系统设备】：/sys/class/thermal/thermal_zone0/temp

**测试操作**

1. 输入命令

.. code-block:: shell

   =====> 输入指令:
   echo $[$(cat /sys/class/thermal/thermal_zone0/temp)/1000]
   =====> 输出信息：
   51

**测试结果**

|   51表示CPU的温度为51°

tftp更新镜像
--------------

|   【测试说明】：可更新dtb、zImage、u-boot、u-boot环境变量
|   【接口标识】：无
|   【系统设备】：无

**测试操作**

|   电脑端打开软件 tftpd 地址设置为需更换的文件所在的目录。
|   把开发板的这个网口用网线跟电脑网口连接起来。
|   进入u-boot命令行。

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
   Filename 'myimx6ek140p-6g-256m-emmc.dtb'.
   Load address: 0x80800000
   Loading: ###
            282.2 KiB/s
   done
   Bytes transferred = 34705 (8791 hex)
   writing myimx6ek140p-6g-256m-emmc.dtb
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

5. 烧写u-boot环境变量(nand开发板没有uboot更新)

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

6. 烧写u-boot(nand开发板没有uboot更新)

.. code-block:: shell

   =====> 输入指令:
   run update_ubot 

   =====> 输出信息：
   Using FEC device
   TFTP from server 192.168.137.99; our IP address is 192.168.137.9
   Filename 'uboot-myimx6ek140p-6g-256m-emmc.imx'.
   Load address: 0x80800000
   Loading: ####################################################
            3 MiB/s
   done
   Bytes transferred = 752640 (b7c00 hex)
   switch to partitions #0, OK
   mmc1(part 0) is current device

   MMC write: dev # 1, block # 2, count 1022 ... 1022 blocks written: OK
 

复制更新镜像
-------------

|   【测试说明】：可更新dtb、zImage、u-boot环境变量、kernel-modules
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
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.522 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.415 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 received, 0% packet loss, time 999ms
   rtt min/avg/max/mdev = 0.415/0.468/0.522/0.057 ms

|   “0% packet loss”表示连接正常。

3. 传输文件

.. code-block:: shell

   =====> 输入指令:
   tftp -g 192.168.137.99 -r zImage-myimx6a7
   tftp -g 192.168.137.99 -r myimx6ek140p-6g-256m-emmc.dtb
   tftp -g 192.168.137.99 -r my_environment_emmc.scr
   tftp -g 192.168.137.99 -r kernel-modules-myimx6a9.tar.bz2

4. 查看系统是否自动挂载分区

.. code-block:: shell

   =====> 输入指令:
   ls /run/media/mmcblk1p1/

   =====> 输出信息：
   my_environment_emmc.scr  myimx6ek140p-6g-256m-emmc.dtb  zImage-myimx6a7

系统自动挂载分区
-----------------

1. 复制相应的文件到/run/media/mmcblk1p1/目录，将原文件替换。

.. code-block:: shell

   =====> 输入指令:
   cp zImage-myimx6a7 /run/media/mmcblk1p1/
   cp myimx6ek140p-6g-256m-emmc.dtb /run/media/mmcblk1p1/
   cp my_environment_emmc.scr /run/media/mmcblk1p1/

2. 解压更新内核模块

.. code-block:: shell

   =====> 输入指令:
   tar xjvf kernel-modules-myimx6a9.tar.bz2 -C /

3. 保存并重启

.. code-block:: shell

   =====> 输入指令:
   reboot

|   若系统没有自动挂载分区

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
   cp myimx6ek140p-6g-256m-emmc.dtb /mnt
   cp my_environment_emmc.scr /mnt

4. 解压更新内核模块

.. code-block:: shell

   =====> 输入指令:
   tar xjvf kernel-modules-myimx6a9.tar.bz2 -C /

5. 保存并重启

.. code-block:: shell

   =====> 输入指令:
   reboot

WIFI模块RTL8188EUS（选配）测试
-------------------------------

|   【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|   【接口标识】：WIFI，WIFI_ANT
|   【接口丝印】：U20，E2
|   【系统设备】：wlan0

**测试操作**

1. 确定“WIFI”标识处有贴上WIFI模块，否则无需进行测试。
2. 把WIFI天线连接到“WIFI_ANT”标识的接口上。
3. 生成 SSID 的 WPA PSK 文件

|   命令格式: wpa_passphrase <ssid> [passphrase]

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
   ==> rtl8188e_iol_efuse_patch
   IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready

5. 获取 IP

.. code-block:: shell

   =====> 输入指令:
   udhcpc -i wlan0

   =====> 输出信息：
   udhcpc (v1.24.1) started
   Sending discover...
   Sending select for 192.168.43.130...
   Lease of 192.168.43.130 obtained, lease time 3600
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

|   “0% packet loss”表示WIFI连接正常。


4G模块EC20（选配）测试

|   【测试说明】：4G连接成功后，开发板向外网发送ICMP报文来验证连接正常。
|   【接口标识】：3G/4G
|   【接口丝印】：P19
|   【系统设备】：eth2

**测试操作**

|   1. 开发板断电，接上4G模块，接上天线并插入SIM卡后启动评估板。
|   2. 使用指令进行网络连接：

.. code-block:: shell

   =====> 输入指令:
   /my-demo/gcc-linaro-5.3-arm/quectel-CM.out &  

   =====> 输出信息：
   [1] 540
   [12-18_03:17:06:719] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
   [12-18_03:17:06:720] /my-demo/gcc-linaro-5.3-arm/quectel-CM.out profile[1] = (null)/(null)/(null)/0, pincode = (null)
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
   [12-18_03:17:07:492] udhcpc (v1.24.1) started
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

|   “0% packet loss”表示WIFI连接正常。


显示屏（选配）测试
-------------------

|   【测试说明】：观察系统启动过程中显示屏的显示来确定显示功能是否正常
|   【接口标识】：RGB
|   【接口丝印】：P3
|   【系统设备】：/dev/fb0

**测试操作**

|   为开发板接上显示屏，上电，观察开发板启动过程中显示屏的显示。

**测试结果**

|   在系统启动过程中，可以看到 Linux 小企鹅和 OpenEmbedded 启动画面。


FXLS8471（选配）测试
---------------------

|   【测试说明】：通过在系统下读取传感器的数据来确认该功能正常
|   【接口标识】：Accelerometer
|   【接口丝印】：U18
|   【系统设备】：/sys/class/misc/FreescaleAccelerometer/

**测试操作**

1. 使传感器 Enable

.. code-block:: shell

   =====> 输入指令:
   echo 1 > /sys/class/misc/FreescaleAccelerometer/enable  

   =====> 输出信息：
   mma enable setting actived

2. 查看传感器数据

.. code-block:: shell

   =====> 输入指令:
   cat /sys/class/misc/FreescaleAccelerometer/data  

   =====> 输出信息：
   -384,136,16384

**测试结果**

|   执行上面指令后，系统会输出传感器数据即正常。

FXAS2100（选配）测试
---------------------

|   【测试说明】：通过在系统下读取传感器的数据来确认该功能正常
|   【接口标识】：Gyroscope
|   【接口丝印】：U19
|   【系统设备】：/dev/input/eventX

**测试操作**

1. 使传感器 Enable

.. code-block:: shell

   =====> 输入指令:
   echo 1 > /sys/class/misc/FreescaleGyroscope/enable 

   =====> 输出信息：
   misc FreescaleGyroscope: mma enable setting active

2. 运行 evtest 程序：

.. code-block:: shell

   =====> 输入指令:
   evtest 

   =====> 输出信息：
   No device specified, trying to scan all of /dev/input/event*
   Available devices:
   /dev/input/event0:  fxas2100x
   /dev/input/event1:  20cc000.snvs:snvs-powerkey
   /dev/input/event2:  FreescaleAccelerometer
   /dev/input/event3:  mag3110
   Select the device event number [0-3]:

3. 选择对应的设备，这里fxas2100对应event0，所以我们输入0：

.. code-block:: shell

   =====> 输入指令:
   0

   =====> 输出信息：
   Event: time 1538485645.829802, type 3 (EV_ABS), code 0 (ABS_X), value -3
   Event: time 1538485645.829802, type 3 (EV_ABS), code 1 (ABS_Y), value 13
   Event: time 1538485645.829802, type 3 (EV_ABS), code 2 (ABS_Z), value 4
   Event: time 1538485645.829802, -------------- SYN_REPORT ------------

**测试结果**

|   执行上面指令后，系统输出的 value 值即传感器数据。