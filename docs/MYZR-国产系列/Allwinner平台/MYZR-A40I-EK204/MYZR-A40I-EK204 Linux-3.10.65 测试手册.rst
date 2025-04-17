MYZR-A40I-EK204 Linux-3.10.65 测试手册
=======================================

网口测试
----------

|  【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|  【接口标识】：10M/100M Ethernet-1
|  【系统接口】：eth0

**测试操作**

|  配置电脑有线网卡IP为 192.168.137.99。
|  把开发板的这个网口用网线跟电脑网口连接起来。
|  配置开发板网口：

.. code-block:: shell

   =====> 输入指令:
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


USB接口测试
-------------

|  【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|  【接口标识】：USB HOST
|  【系统接口】：/sys/bus/usb/

**测试方法**

|  将USB设备插入底板USB接口，系统会输出类似如下信息:

.. code-block:: 

   root@TinaLinux:/# [  795.551264] ehci_irq: highspeed device connect
   [  795.910089] usb 1-1: new high-speed USB device number 4 using sunxi-ehci
   [  796.081676] usb-storage 1-1:1.0: USB Mass Storage device detected
   [  796.110678] scsi1 : usb-storage 1-1:1.0
   [  797.111474] scsi 1:0:0:0: Direct-Access     Kingston DataTraveler 3.0 PMAP PQ: 0 ANSI: 6
   [  797.140157] sd 1:0:0:0: [sda] 60604416 512-byte logical blocks: (31.0 GB/28.8 GiB)
   [  797.156371] sd 1:0:0:0: [sda] Write Protect is off
   [  797.161892] sd 1:0:0:0: [sda] Mode Sense: 45 00 00 00
   [  797.169966] sd 1:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
   [  797.251578]  sda: sda1
   [  797.260467] CPU1: Booted secondary processor
   [  797.271003] sd 1:0:0:0: [sda] Attached SCSI removable disk
   [  797.489583]  sda: sda1
   [  797.622161] FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
   [  797.860430] CPU2: Booted secondary processor
   [  797.974464] FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|  将USB设备从底板拔出，系统会输出类似如下信息：

.. code-block:: shell

   [  810.557018] ehci_irq: highspeed device disconnect
   [  810.562361] usb 1-1: USB disconnect, device number 4
   [  810.670680] udevd[2861]: inotify_add_watch(6, /dev/sda, 10) failed: No such file or directory

**测试结果**

|  USB存储设备插拔时系统输出如上类似信息即表示正常。


TF接口测试
-----------

|  【测试说明】：采用插入并识别TF卡的方式进行测试
|  【接口标识】：SD3
|  【系统接口】：/sys/bus/mmc/

**测试方法**

|  把TF卡插入到这个接口：

.. code-block:: shell

   =====> 输出信息：
   root@TinaLinux:/# [   80.560114] sunxi-mmc sdc0: sdc set ios: clk 0Hz bm PP pm UP vdd 22 width 1 timing LEGACY(SDR12) dt B
   [   80.590139] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 22 width 1 timing LEGACY(SDR12) dt B
   [   80.620937] sunxi-mmc sdc0: smc 1 p0 err, cmd 52, RTO !!
   [   80.627845] sunxi-mmc sdc0: smc 1 p0 err, cmd 52, RTO !!
   [   80.634740] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 22 width 1 timing LEGACY(SDR12) dt B
   [   80.653529] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 22 width 1 timing LEGACY(SDR12) dt B
   [   80.670770] sunxi-mmc sdc0: smc 1 p0 err, cmd 5, RTO !!
   [   80.677415] sunxi-mmc sdc0: smc 1 p0 err, cmd 5, RTO !!
   [   80.687485] sunxi-mmc sdc0: smc 1 p0 err, cmd 5, RTO !!
   [   80.694393] sunxi-mmc sdc0: smc 1 p0 err, cmd 5, RTO !!
   [   80.702493] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 15 width 1 timing LEGACY(SDR12) dt B
   [   80.714629] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 15 width 1 timing LEGACY(SDR12) dt B
   [   80.733353] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 15 width 1 timing LEGACY(SDR12) dt B
   [   80.750809] CPU1: Booted secondary processor
   [   80.943958] mmc1: host does not support reading read-only switch. assuming write-enable.
   [   80.958125] sunxi-mmc sdc0: sdc set ios: clk 400000Hz bm PP pm ON vdd 15 width 1 timing SD-HS(SDR25) dt B
   [   80.970520] sunxi-mmc sdc0: sdc set ios: clk 50000000Hz bm PP pm ON vdd 15 width 1 timing SD-HS(SDR25) dt B
   [   80.982111] sunxi-mmc sdc0: sdc set ios: clk 50000000Hz bm PP pm ON vdd 15 width 4 timing SD-HS(SDR25) dt B
   [   80.993313] mmc1: new high speed SDHC card at address aaaa
   [   80.999904] mmcblk1: mmc1:aaaa SC16G 14.8 GiB 
   [   81.013518]  mmcblk1:
   [   81.016702] sndhdmi sndhdmi: ASoC: CPU DAI (null) not registered
   [   81.023541] sndhdmi sndhdmi: snd_soc_register_card() failed: -517
   [   81.030614] platform sndhdmi: Driver sndhdmi requests probe deferral
   [   81.103148] FAT-fs (mmcblk1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|  弹出TF卡：

.. code-block:: shell

   =====> 输出信息：
   root@TinaLinux:/# [  147.600144] sunxi-mmc sdc0: smc 1 p0 err, cmd 13, RTO !!
   [  147.606083] sunxi-mmc sdc0: smc 1 p0 err, cmd 13, RTO !!
   [  147.612251] sunxi-mmc sdc0: smc 1 p0 err, cmd 13, RTO !!
   [  147.618180] sunxi-mmc sdc0: smc 1 p0 err, cmd 13, RTO !!
   [  147.624573] mmc1: card aaaa removed
   [  147.637669] sunxi-mmc sdc0: sdc set ios: clk 0Hz bm OD pm OFF vdd 0 width 1 timing LEGACY(SDR12) dt B

|  TF存储设备插拔时系统输出如上类似信息即表示正常。


标准GPIO测试
--------------

|  【测试说明】：控制GPIO的输出电平
|  【接口标识】：GPIO/SD2
|  【系统接口】：/sys/class/gpio/


GPIO输出低电平测试
-------------------

|  配置P26:2为输出低电平的操作方法：

.. code-block:: shell

   =====> 输入指令:
   OUT_IO_OUT_NUM=270
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export    
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 

|  用万用表测试管脚P26:2，电压为0V，则表示OK


GPIO输出高电平测试
-------------------

|  配置P26:2为输出高电平的操作方法：

.. code-block:: shell

   =====> 输入指令:
   OUT_IO_OUT_NUM=270
   echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
   echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction  
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  用万用表测试管脚P26:2，电压为3.3V，则表示OK

**其它**

|  控制 GPIO 输出低电平的指令：

.. code-block:: shell

   =====> 输入指令:
   echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value   

|  控制 GPIO 输出高电平的指令：

.. code-block:: shell

   =====> 输入指令:
   echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value 


GPIO-LED测试
--------------

|  【测试说明】：控制LED
|  【接口标识】：LED
|  【系统接口】：/sys/class/leds/led*

**测试操作**

|  控制LED关闭：

.. code-block:: shell

   echo 1 > /sys/class/leds/led1/brightness
   echo 1 > /sys/class/leds/led2/brightness
   echo 1 > /sys/class/leds/led3/brightness

|  控制LED开启：

.. code-block:: shell

   echo 0 > /sys/class/leds/led1/brightness
   echo 0 > /sys/class/leds/led2/brightness
   echo 0 > /sys/class/leds/led3/brightness


GPIO-KEY测试
--------------

|  【测试说明】：使用 evtest 进行测试
|  【接口标识】：KEY4, KEY4, KEY3, KEY2, KEY1
|  【系统接口】：/dev/input/event0

**测试操作**

|  运行 evtest 准备测试

.. code-block:: shell

   =====> 输入指令:
   evtest 

   =====> 输出信息：
   No device specified, trying to scan all of /dev/input/event*
   Available devices:
   /dev/input/event0:  sunxi-keyboard
   /dev/input/event1:  sunxi-ir
   /dev/input/event2:  axp22-powerkey
   Select the device event number [0-2]: 

|  选择 sunxi-keyboard 所对应的序号

.. code-block:: shell

   =====> 输入指令:
   0

   =====> 输出信息：
   Input driver version is 1.0.1
   Input device ID: bus 0x19 vendor 0x1 product 0x1 version 0x100
   Input device name: "sunxi-keyboard"
   Supported events:
     Event type 0 (EV_SYN)
     Event type 1 (EV_KEY)
       Event code 28 (KEY_ENTER)
       Event code 102 (KEY_HOME)
       Event code 114 (KEY_VOLUMEDOWN)
       Event code 115 (KEY_VOLUMEUP)
       Event code 139 (KEY_MENU)
   Properties:
   Testing ... (interrupt to exit)

|  按动开发板上的按键

.. code-block:: shell

   Event: time 1262304222.998060, type 1 (EV_KEY), code 102 (KEY_HOME), value 1
   Event: time 1262304222.998060, -------------- SYN_REPORT ------------
   Event: time 1262304223.162092, type 1 (EV_KEY), code 102 (KEY_HOME), value 0
   Event: time 1262304223.162092, -------------- SYN_REPORT ------------
   Event: time 1262304223.533178, type 1 (EV_KEY), code 28 (KEY_ENTER), value 1
   Event: time 1262304223.533178, -------------- SYN_REPORT ------------
   Event: time 1262304223.697226, type 1 (EV_KEY), code 28 (KEY_ENTER), value 0
   Event: time 1262304223.697226, -------------- SYN_REPORT ------------
   Event: time 1262304224.622976, type 1 (EV_KEY), code 139 (KEY_MENU), value 1
   Event: time 1262304224.622976, -------------- SYN_REPORT ------------
   Event: time 1262304224.923742, type 1 (EV_KEY), code 139 (KEY_MENU), value 0
   Event: time 1262304224.923742, -------------- SYN_REPORT ------------
   Event: time 1262304225.818243, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 1
   Event: time 1262304225.818243, -------------- SYN_REPORT ------------
   Event: time 1262304226.083851, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 0
   Event: time 1262304226.083851, -------------- SYN_REPORT ------------
   Event: time 1262304227.911909, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 1
   Event: time 1262304227.911909, -------------- SYN_REPORT ------------
   Event: time 1262304228.165801, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 0
   Event: time 1262304228.165801, -------------- SYN_REPORT ------------

**测试结果**

|  当发生按键时，evtest 会输出相应的信息。


串口测试（RS232）
------------------

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：UART
|  【系统设备】：/dev/ttyS4

**测试操作**

|  短接串口4的发送发接收管脚（RS232的TX和RX管脚）
|  执行测试指令：

.. code-block:: shell

   =====> 输入指令:
   serial_test /dev/ttyS4 "www.myzr.com.cn"

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


串口测试（RS485）
------------------

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：UART
|  【系统设备】：/dev/ttyS5/7

**测试操作**

|  短接串口5的发送管脚与串口7的接收管脚（485-1的TX和485-2的RX管脚）
|  短接串口7的发送管脚与串口5的接收管脚（485-2的TX和485-1的RX管脚）
|  执行测试指令：

.. code-block:: shell

   =====> 输入指令:
   cat /dev/ttyS5 &
   echo www.myzr.com.cn > /dev/ttyS7
   =====> 输出信息:
   www.myzr.com.cn

   =====> 输入指令:
   killall cat
   cat /dev/ttyS7 &
   echo www.myzr.com.cn > /dev/ttyS5
   =====> 输出信息:
   www.myzr.com.cn


RTC 测试
----------

|  【测试说明】：读取并设置时间，断电重启后检查时间是否正确
|  【接口标识】：无
|  【系统设备】：/sys/class/rtc/

**测试操作**

1. 断电重启设备，查看当前系统时间和硬件时间：

.. code-block:: shell

   =====> 输入指令: 
   date

   =====> 输出信息：
   Fri Jan  1 08:00:29 CST 2010

2. 查看当前RTC芯片时钟：

.. code-block:: shell

   =====> 输入指令: 
   hwclock 

   =====> 输出信息：
   Fri Jan  1 00:00:41 2010  0.000000 seconds

3. 设置系统时钟，并同步到RTC芯片

.. code-block:: shell

   =====> 输入指令: 
   date -s "2021-05-14 12:34:56" 

   =====> 输出信息：
   Fri May 14 12:34:59 CST 2021

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
   Fri May 14 12:35:34 2021  0.000000 seconds
   2. 查看当前RTC芯片时钟

   =====> 输入指令:
   hwclock  

   =====> 输出信息：
   Fri May 14 12:35:37 2021  0.000000 seconds

|  可以看到我们得到的时间与设置的时间基本相同。


音频播放测试
-------------

|  【测试说明】：通过播放音频文件验证评估板的音频播放功能。

**测试操作**

|   把耳机插入开发板的音频口。
|   执行测试命令：

.. code-block:: shell

   =====> 输入指令:
   aplay /test/test.wav 
   =====> 输出信息：
   Playing WAVE 'test.wav' : Signed 16 bit Little Endian, Rate 16000 Hz, Mono

**测试结果**

|  执行上面的测试命令后会听到音频设备输出的声音


音频录音测试
-------------

|  【测试说明】：通过录音并播放录音文件验证评估板的音频录音功能。
|  【接口标识】：MIC

**测试操作**

|  执行测试命令：

.. code-block:: shell

   =====> 输入指令:
   arecord -d 5 -f S16_LE -t wav foobar.wav
   =====> 输出信息：
   Recording WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

|  播放录音:

.. code-block:: shell

   =====> 输入指令:
   aplay foobar.wav

   =====> 输出信息：
   Playing WAVE 'foobar.wav' : Signed 16 bit Little Endian, Rate 8000 Hz, Mono

**测试结果**

|  执行上面的测试命令后会听到播放的录音。


显示测试
---------

|  【测试说明】：执行显示程序。
|  【接口标识】：lvds/lcd/dsi
|  【系统设备】：fb0

**测试操作**

1. 关机后接上显示屏
2. 执行命令

.. code-block:: shell

   df_andi

WIFI测试
----------

|  【测试说明】：使用RTL8723du作为无线网卡连接到WIFI AP。
|  【接口标识】：WIFI、WIFI_ANT
|  【系统设备】：wlan0

**测试操作**

1. 确定“WIFI”标识处有贴上WIFI模块，否则无需进行测试。
2. 把WIFI天线连接到“WIFI_ANT”标识的接口上。

.. code-block:: shell

   =====> 输入指令:
   wifi_connect_ap_test MYZR-WIFI myzr2012

|  MYZR-WIFI为WIFI名 myzr2012为密码
|  测试连接

.. code-block:: shell

   =====> 输入指令:
   ping -I wlan0 www.baidu.com -c 2 -w 4

   =====> 输出信息：
   PING www.baidu.com (163.177.151.109): 56 data bytes
   64 bytes from 163.177.151.109: seq=0 ttl=56 time=9.776 ms
   64 bytes from 163.177.151.109: seq=1 ttl=56 time=9.620 ms

   --- www.baidu.com ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 9.620/9.698/9.776 ms

**测试结果**

|  “0% packet loss”表示WIFI连接正常。


蓝牙测试
----------

|  【测试说明】：扫描到蓝牙设备后，发送L2CAP回应请求并接收回答。
|  【系统设备】：hci0

1. 确定“WIFI”标识处有贴上WIFI模块，否则无需进行测试。
2. 把WIFI天线连接到“WIFI_ANT”标识的接口上。

|  配置蓝牙系统接口

.. code-block:: shell

   =====> 输入指令:
   hciconfig hci0 up
   hciconfig hci0 piscan
   hciconfig -a
   hci0:   Type: BR/EDR  Bus: USB
       BD Address: 74:EE:2A:45:64:EC  ACL MTU: 1021:8  SCO MTU: 255:12
       UP RUNNING PSCAN ISCAN 
       RX bytes:1403 acl:0 sco:0 events:59 errors:0
       TX bytes:786 acl:0 sco:0 commands:59 errors:0
       Features: 0xff 0xff 0xff 0xfa 0xdb 0xbd 0x7b 0x87
       Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3 
       Link policy: RSWITCH HOLD SNIFF PARK 
       Link mode: SLAVE ACCEPT 
       Name: 'RTK_BT_4.1'
       Class: 0x000000
       Service Class[   54.305172] rtk_btcoex: BTCOEX hci_rev 0x82a8
   es: Unspecified
       Device Class: [   54.311358] rtk_btcoex: BTCOEX lmp_subver 0x2df4
   Miscellaneous, 
       HCI Version: 4.1 (0x7)  Revision: 0x82a8
       LMP Version: 4.1 (0x7)  Subversion: 0x2df4
       Manufacturer: Realtek Semiconductor Corporation (93)

|  查看板子蓝牙设备信息

.. code-block:: shell

   =====> 输入指令:

      hcitool dev
   =====> 输出信息：

      Devices:
      hci0    74:EE:2A:45:64:EC

2. 扫描外部蓝牙设备

.. code-block:: shell

   =====> 输入指令:

      hcitool scan
   =====> 输出信息：

      Scanning ...
      ......
      7C:2A:DB:08:EF:70    Redmi K30 Pro

3. 发送发送L2CAP包测试

.. code-block:: shell

   =====> 输入指令:

      l2ping  7C:2A:DB:08:EF:70 -c 2
   =====> 输出信息：

   Ping: 7C:2A:DB:08:EF:70 from 74:EE:2A:45:64:EC (data size 44) ...
   44 bytes from 7C:2A:DB:08:EF:70 id 0 time 7.89ms
   44 bytes from 7C:2A:DB:08:EF:70 id 1 time 24.88ms
   44 bytes from 7C:2A:DB:08:EF:70 id 2 time 9.80ms
   ^C3 sent, 3 received, 0% loss

**测试结果**

|  “0% packet loss”表示蓝牙连接正常


EC20 模块测试
---------------

|  【测试说明】：4G连接成功后，开发板向外网发送ICMP报文来验证连接正常。
|  【系统设备】：usb0

**测试操作**

1. 开发板断电，接上4G模块，接上天线并插入SIM卡后启动评估板。
2. 使用指令进行网络连接：

.. code-block:: shell

   =====> 输入指令:

      /etc/quectel-CM

|  测试连接：

.. code-block:: shell

   =====> 输入指令:

      ping www.baidu.com -c 2 -w 4
   =====> 输出信息：

   PING www.a.shifen.com (183.232.231.172) from 10.77.19.81 ppp0: 56(84) bytes of data.
   64 bytes from 183.232.231.172: icmp_seq=1 ttl=56 time=197 ms
   --- www.a.shifen.com ping statistics ---
   1 packets transmitted, 1 received, 0% packet loss, time 0ms
   rtt min/avg/max/mdev = 197.497/197.497/197.497/0.000 ms

**测试结果** 　

|  “0% packet loss”表示WIFI连接正常。