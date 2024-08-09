
MYZR-STM32测试手册
====================

测试环境
~~~~~~~~~

- 开发板型号：MYZR-STM32-EK152
- 内核版本：Linux-5.4.31
- 文件系统：

 |  st-image-bootfs-openstlinux-weston-stm32mp1.ext4;
 |  st-image-vendorfs-openstlinux-weston-stm32mp1.ext4;
 |  st-image-weston-openstlinux-weston-stm32mp1.ext4;
 |  st-image-userfs-openstlinux-weston-stm32mp1.ext4;

接口标识图
~~~~~~~~~~~

.. image:: /image/MYZR-ST系列/MYZR-STM32-EK152/Stm32mp1-Front-view.png
   :alt: Stm32mp1-Front-view.png

.. image:: /image/MYZR-ST系列/MYZR-STM32-EK152/Stm32mp1-Back-view.png
   :alt: Stm32mp1-Back-view.png

网口测试
~~~~~~~~~

|  【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|  【接口标识】：ETH10/100/1000M
|  【接口丝印】：U4
|  【系统接口】：eth0

**测试操作**

|  1.配置电脑有线网卡ip为 192.168.137.99
|  2.网线连接板子网口和电脑网口
|  3.输入如下指令与电脑通讯：

.. code:: shell
   
   =====> Input:
   # ping 192.168.137.99

   =====> Output:
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=0.758 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.306 ms
   64 bytes from 192.168.137.99: icmp_seq=3 ttl=128 time=0.467 ms
   ^C
   --- 192.168.137.99 ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 0.306/0.510/0.758/0.187 ms

|  “0% packet loss”表示测试通过。

USB测试
~~~~~~~~

|  【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|  【接口标识】：USB2.0
|  【接口丝印】：P5

**测试操作**

1.将USB设备插入底板USB接口，系统会输出类似如下信息:

.. code:: shell

   root@stm32mp1:~# [ 3288.330096] usb 2-1.4: new high-speed USB device number 3 using ehci-platform
   [ 3288.396730] usb-storage 2-1.4:1.0: USB Mass Storage device detected
   [ 3288.413395] scsi host0: usb-storage 2-1.4:1.0
   [ 3288.595095] usbcore: registered new interface driver uas
   [ 3289.452460] scsi 0:0:0:0: Direct-Access     Generic- SD/MMC           1.00 PQ: 0 ANSI: 4
   [ 3289.468478] sd 0:0:0:0: Attached scsi generic sg0 type 0
   [ 3290.224654] sd 0:0:0:0: [sda] 60932096 512-byte logical blocks: (31.2 GB/29.1 GiB)
   [ 3290.232024] sd 0:0:0:0: [sda] Write Protect is off
   [ 3290.236486] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, does\'t support DPO or FUA
   [ 3290.307279] sda: sda1
   [ 3290.314548] sd 0:0:0:0: [sda] Attached SCSI removable disk

2.将USB设备从底板拔出，系统会输出类似如下信息：

.. code:: shell

   root@stm32mp1:~# [ 3343.077203] usb 2-1.4: USB disconnect, device number 3

SD接口测试
~~~~~~~~~~~

|  【测试说明】：采用插入并识别TF卡的方式进行测试
|  【接口标识】：TF
|  【接口丝印】：P3

**测试操作**

1.将TF卡安装到SD接口，开发会输出如下信息：

.. code:: shell
   
   root@stm32mp1:~# [ 3697.015101] mmc1: new high speed SDHC card at address 1234
   [ 3697.035081] mmcblk1: mmc1:1234 SA32G 29.1 GiB 
   [ 3697.042740]  mmcblk1: p1

2.可以查看到对应的sd接口设备：

.. code:: shell
   
   # ls /dev/mmcblk1*
   /dev/mmcblk1  /dev/mmcblk1p1

3.将TF卡拔出，输出如下信息：

.. code:: shell
   
   root@stm32mp1:~# [ 3985.400589] mmc1: card 1234 removed

GPIO测试
~~~~~~~~~

|  【测试说明】：控制GPIO的输出/输入电平
|  【接口标识】：GPIO/SPI/UART
|  【接口丝印】：P21
|  【系统接口】：/dev/gpiochipx

**测试操作**

1.列出系统上所有的gpiochip：

.. code:: shell
   
   =====> Input:
   # gpiodetect 

   =====> Output:
   gpiochip0 [GPIOA] (16 lines)
   gpiochip1 [GPIOB] (16 lines)
   gpiochip2 [GPIOC] (16 lines)
   gpiochip3 [GPIOD] (16 lines)
   gpiochip4 [GPIOE] (16 lines)
   gpiochip5 [GPIOF] (16 lines)
   gpiochip6 [GPIOG] (16 lines)
   gpiochip7 [GPIOH] (16 lines)
   gpiochip8 [GPIOI] (16 lines)
   gpiochip9 [GPIOZ] (16 lines)

2.配置P21-38脚（即PF15）输出高电平：

.. code:: shell
   
   # gpioset gpiochip5 15=1

|  使用万用表测量P21-38脚，可以测出为3.3v即高电平

3.配置P21-38脚（即PF15）输出高低平：

.. code:: shell
   
   # gpioset gpiochip5 15=0

|  使用万用表测量P21-38脚，可以测出为0v即高低平

4.配置P21-38脚（即PF15）为输入，并读取其值：

.. code:: shell
   
   =====> Input:
   # gpioget  gpiochip5 15

   =====> Output:
   0

串口测试
~~~~~~~~~

**UART**

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：GPIO/SPI/UART
|  【接口位置】：P21
|  【系统设备】：/dev/ttySTM6(uart7)，/dev/ttySTM7(uart8)

**测试操作**

1.短接P21-11和P21-13脚，即uart7_rx和uart7_tx
2.输入如下命令进行uart7收发测试：

.. code:: shell
   
   =====> Input:
   # /usr/local/myzr-demo/serial_test.out /dev/ttySTM6 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x0   Character:  

|  执行测试指令后，应用输出如上类似信息即正常。

3.输入如下命令进行uart8收发测试：

.. code:: shell

   =====> Input:
   # /usr/local/myzr-demo/serial_test.out /dev/ttySTM7 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x0   Character:

|  执行测试指令后，应用输出如上类似信息即正常。

**RS232**

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：RS232
|  【接口位置】：P16
|  【系统设备】：/dev/ttySTM2（usart3）

**测试操作**

1.短接P16-1和P16-2脚，即TX和RX
2.输入如下命令进行RS232收发测试：

.. code:: shell
   
   =====> Input:
   # /usr/local/myzr-demo/serial_test.out /dev/ttySTM2 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x0   Character:  

|  执行测试指令后，应用输出如上类似信息即正常。

**RS485**

|  【测试说明】：RS485是差分信号，不能采用自发自收的方式进行测试。
|  【接口标识】：RS485
|  【接口位置】：P17
|  【系统设备】：/dev/ttySTM4（uart5）

**测试操作**

1.使用485-232转换头连接P17-A/B脚和电脑usb转串口线
2.打开串口调试助手，设置波特率为9600，无校验位，8位数据位，1位停止位。
3.开发板使用ssh登录，向电脑端发送数据：

.. code:: shell
   
   # echo 123 > /dev/ttySTM4

|  可以看到串口助手接收到字符串123

4.开发板接收数据，电脑端发送数据：

.. code:: shell
   
   # cat /dev/ttySTM4

|  当串口助手发送字符串时，开发板会接收到数据：

.. code:: shell
   
   # cat /dev/ttySTM4 
   myzr

CAN测试
~~~~~~~~

|  注：只有stm32mp157/stm32mp153的核心板才具备can功能，且需要两个板子相连来进行测试

|  【测试说明】：can口之间互相发送数据
|  【接口标识】：CAN
|  【接口位置】：P13
|  【系统设备】：can0

**测试操作**

1.准备两个开发板，将CAN口进行连接，CAN_L与CAN_L相连；CAN_H和CAN_H相连。
2.对两个板子的can0进行配置：

.. code:: shell
   
   # ip link set can0 up type can bitrate 125000

3.将其中一个配置为接收：

.. code:: shell
   
   # candump can0

4.另一个发送数据：

.. code:: shell
   
   # cansend can0 1F334455#1122334455667788

5.在接收端可以接收到如下数据：

.. code:: shell
   
   can0  1F334455   [8]  11 22 33 44 55 66 77 88

SPI测试
~~~~~~~~

|  【测试说明】：采用自发自收的方式测试。
|  【接口标识】：GPIO/SPI/UART
|  【接口位置】：P21
|  【系统设备】：/dev/spidev0.0（SPI1），/dev/spidev1.0（SPI5）

**测试操作**

1.短接P21-2和P21-4脚，即SPI1_MOSI和SPI1_MISO，输入命令：

.. code:: shell
   
   =====> Input:
   # /usr/local/myzr-demo/spidev_test.out -D /dev/spidev0.0

   =====> Output:
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

2.短接P21-1和P21-3脚，即SPI5_MOSI和SPI5_MISO，输入命令：

.. code:: shell

   =====> Input:
   # /usr/local/myzr-demo/spidev_test.out -D /dev/spidev1.0

   =====> Output:
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

RTC测试
~~~~~~~~

|  【测试说明】：读取并设置时间，断电重启后检查时间是否正确
|  【接口标识】：RTC_Battery
|  【接口位置】：BT1
|  【系统设备】：/dev/rtc0

**测试操作**

1.断电重启设备，查看当前系统时间和硬件时间：

.. code:: shell

   =====> Input:
   # date

   =====> Output:
   Fri Feb  7 15:51:25 UTC 2020

2.查看当前RTC芯片时钟：

.. code:: shell

   =====> Input:
   # hwclock

   =====> Output:
   hwclock: ioctl(RTC_RD_TIME) to /dev/rtc0 to read the time failed: Invalid argument

3.设置系统时钟：

.. code:: shell

   =====> Input:
   # date -s "2021-04-08 15:00:00"

   =====> Output:
   Thu Apr  8 15:00:00 UTC 2021

4.将系统时钟写入硬件时钟：

.. code:: shell
   
   # hwclock -w

5.断电重启开发板，查看当前系统时钟和硬件时钟：

.. code:: shell

   =====> Input:
   # date

   =====> Output:
   Thu Apr  8 15:04:49 UTC 2021
   =====> Input:
   # hwclock

   =====> Output:
   2021-04-08 15:05:09.146857+00:00

音频播放测试
~~~~~~~~~~~~

|  【测试说明】：通过播放音频文件验证评估板的音频播放功能。
|  【接口标识】：AUDIO
|  【接口位置】：P10
|  【系统设备】：wm8960-audio

**测试操作**

1.把耳机插入开发板的“AUDIO”口。执行如下命令播放音频：

.. code:: shell
   
   =====> Input:
   # aplay /usr/share/sounds/alsa/Front_Center.wav

   =====> Output:
   Playing WAVE '/usr/share/sounds/alsa/Front_Center.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Mono

2.可以使用如下命令进行音量调节：

.. code:: shell
   
   # alsamixer

录音测试
~~~~~~~~

|  【测试说明】：通过录音并播放录音文件验证评估板的音频录音功能。
|  【接口标识】：AUDIO
|  【接口位置】：P10，P11
|  【系统设备】：wm8960-audio

**测试操作**

1.把带MIC的耳机插入开发板耳机接口，或直接使用开发板上的MIC（P11）

2.输入如下命令进行8秒的录音：

.. code:: shell
   
   =====> Input:
   # arecord -D hw:0,1 -f cd -d 8  record.wav

   =====> Output:
   Recording WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

2.播放录制的音频：

.. code:: shell
   
   =====> Input:
   # aplay record.wav

   =====> Output:
   Playing WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

WIFI测试
~~~~~~~~~

|  【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：WIFI&BT
|  【接口丝印】：U12，E1
|  【系统设备】：wlan0

**测试操作**

1.把WIFI天线连接到“E1”接口上

2.生成 SSID 的 WPA PSK 文件 　　命令格式: wpa_passphrase [passphrase]

.. code:: shell
   
   =====> Input:
   # wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf 
   # pkill wpa_supplicant

3.连接：

.. code:: shell

   =====> Input:
   # wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf 

   =====> Output:
   Successfully initialized wpa_supplicant
   [  487.018569] [dhd] dhd_open: Enter wlan0
   [  487.021051] [dhd] dhd_open : no mutex held. set lock
   [  487.026667] [dhd] 
   [  487.026667] Dongle Host Driver, version 100.10.545.18 (r826445-20210204-2)
   [  487.034982] [dhd-wlan0] wl_android_wifi_on : in g_wifi_on=0
   [  487.040477] [dhd] wifi_platform_set_power = 1, delay: 200 msec
   [  487.046317] [dhd] ======== PULL WL_REG_ON(62) HIGH! ========
   [  487.369854] sdio_reset_comm():
   [  487.450144] mmc0: queuing unknown CIS tuple 0x80 (2 bytes)
   [  487.465654] mmc0: queuing unknown CIS tuple 0x80 (3 bytes)
   ......

4.获取IP：

.. code:: shell

   =====> Input:
   # udhcpc -i wlan0

   =====> Output:
   udhcpc: started, v1.31.1
   udhcpc: sending discover
   udhcpc: sending select for 192.168.9.169
   udhcpc: lease of 192.168.9.169 obtained, lease time 86400
   /etc/udhcpc.d/50default: Adding DNS 192.168.9.1

5.测试连接：

.. code:: shell

   =====> Input:
   # ifconfig eth0 down
   # ping  www.baidu.com

   =====> Output:
   PING www.a.shifen.com (163.177.151.110) 56(84) bytes of data.
   64 bytes from 163.177.151.110 (163.177.151.110): icmp_seq=1 ttl=56 time=10.7 ms
   64 bytes from 163.177.151.110 (163.177.151.110): icmp_seq=2 ttl=56 time=9.29 ms
   64 bytes from 163.177.151.110 (163.177.151.110): icmp_seq=3 ttl=56 time=30.1 ms
   64 bytes from 163.177.151.110 (163.177.151.110): icmp_seq=4 ttl=56 time=9.74 ms

   --- www.a.shifen.com ping statistics ---
   4 packets transmitted, 4 received, 0% packet loss, time 3005ms
   rtt min/avg/max/mdev = 9.288/14.962/30.092/8.750 ms

蓝牙测试
~~~~~~~~~

|  【测试说明】：扫描到蓝牙设备后，发送L2CAP回应请求并接收回答
|  【接口标识】：WIFI&BT
|  【接口丝印】：U12，E1
|  【系统设备】：hci0

**测试操作**

1.把天线连接到“E1”接口上

2.初始化蓝牙设备：

.. code:: shell

   =====> Input:
   # gpioset gpiochip9 6=1
   #brcm_patchram_plus  --enable_hci -no2bytes --tosleep 200000 --baudrate 115200 --patchram /etc/firmware/bcm43438a1.hcd /dev/ttySTM1 &

3.启动蓝牙：

.. code:: shell

   =====> Input:
   # hciconfig hci0 up
   # hciconfig 

   =====> Output:
   hci0:   Type: Primary  Bus: UART
       BD Address: B0:F1:EC:A7:E8:03  ACL MTU: 1021:8  SCO MTU: 64:1
       UP RUNNING 
       RX bytes:1266 acl:0 sco:0 events:66 errors:0
       TX bytes:1138 acl:0 sco:0 commands:66 errors:0

4.扫描外部蓝牙设备：

.. code:: shell

   =====> Input:
   # hcitool scan

   =====> Output:
   Scanning ...
       88:46:04:4C:11:A7   Redmi K40

5.发送发送L2CAP包测试：

.. code:: shell

   =====> Input:
   # l2ping 88:46:04:4C:11:A7

   =====> Output:
   Ping: 88:46:04:4C:11:A7 from B0:F1:EC:A7:E8:03 (data size 44) ...
   44 bytes from 88:46:04:4C:11:A7 id 0 time 44.84ms
   44 bytes from 88:46:04:4C:11:A7 id 1 time 28.58ms
   44 bytes from 88:46:04:4C:11:A7 id 2 time 46.05ms
   44 bytes from 88:46:04:4C:11:A7 id 3 time 44.86ms
   44 bytes from 88:46:04:4C:11:A7 id 4 time 44.67ms
   44 bytes from 88:46:04:4C:11:A7 id 5 time 52.32ms
   44 bytes from 88:46:04:4C:11:A7 id 6 time 24.86ms
   44 bytes from 88:46:04:4C:11:A7 id 7 time 59.71ms
   8 sent, 8 received, 0% loss

|  “0% packet loss”表示蓝牙连接正常。

4G模块(EC20)测试
~~~~~~~~~~~~~~~~~

|  【测试说明】：4G连接成功后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：4G
|  【接口丝印】：P7
|  【系统设备】：usb0

**测试操作**

1.开发板断电，接上4G模块，接上天线并插入SIM卡后启动评估板。

2.使用指令进行网络连接：

.. code:: shell
   
   =====> Input:
   # /usr/local/myzr-demo/quectel-CM &

   =====> Output:
   [04-08_17:05:13:944] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
   [04-08_17:05:13:945] /usr/local/myzr-demo/quectel-CM profile[1] = (null)/(null)/(null)/0, pincode = (null)
   [04-08_17:05:13:948] Find /sys/bus/usb/devices/2-1.1 idVendor=2c7c idProduct=0125
   [04-08_17:05:13:948] Find /sys/bus/usb/devices/2-1.1:1.4/net/usb0
   [04-08_17:05:13:948] Find usbnet_adapter = usb0
   [04-08_17:05:13:949] Find /sys/bus/usb/devices/2-1.1:1.4/GobiQMI/qcqmi0
   [04-08_17:05:13:949] Find qmichannel = /dev/qcqmi0
   [04-08_17:05:14:014] Get clientWDS = 7
   [04-08_17:05:14:048] Get clientDMS = 8
   [04-08_17:05:14:079] Get clientNAS = 9
   [04-08_17:05:14:111] Get clientUIM = 10
   [04-08_17:05:14:143] Get clientWDA = 11
   [04-08_17:05:14:174] requestBaseBandVersion EC20CEFAR02A10M4G
   [04-08_17:05:14:271] requestGetSIMStatus SIMStatus: SIM_READY
   [04-08_17:05:14:302] requestGetProfile[1] cmnet///0
   [04-08_17:05:14:334] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [04-08_17:05:14:366] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
   [04-08_17:05:14:431] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [04-08_17:05:14:974] requestSetupDataCall WdsConnectionIPv4Handle: 0x87206180
   [04-08_17:05:15:071] requestQueryDataCall IPv4ConnectionStatus: CONNECTED
   [04-08_17:05:15:103] ifconfig usb0 up
   [04-08_17:05:15:114] busybox udhcpc -f -n -q -t 5 -i usb0
   udhcpc: started, v1.31.1
   udhcpc: sending discover
   udhcpc: sending select for 10.145.82.192
   udhcpc: lease of 10.145.82.192 obtained, lease time 7200
   [04-08_17:05:15:502] /etc/udhcpc.d/50default: Adding DNS 221.179.38.7
   [04-08_17:05:15:502] /etc/udhcpc.d/50default: Adding DNS 120.196.165.7

3.连接测试：

.. code:: shell

   =====> Input:
   # ifconfig eth0 down
   # ping www.baidu.com

   =====> Output:
   PING www.wshifen.com (104.193.88.77) 56(84) bytes of data.
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=1 ttl=42 time=263 ms
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=2 ttl=42 time=233 ms
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=3 ttl=42 time=232 ms

   --- www.wshifen.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2000ms
   rtt min/avg/max/mdev = 232.138/242.649/262.712/14.191 ms

|  “0% packet loss”表示WIFI连接正常。

休眠唤醒测试
~~~~~~~~~~~~~

|  【测试说明】：系统进入休眠状态，使用唤醒按键使系统唤醒
|  【接口标识】：无
|  【接口丝印】：无

**测试操作**

1.系统进入休眠状态

.. code:: shell

   =====> Input:
   # echo mem > /sys/power/state

   =====> Output:
   [  100.468138] PM: suspend entry (deep)
   [  100.485714] Filesystems sync: 0.015 seconds
   [  100.492393] Freezing user space processes ... (elapsed 0.002 seconds) done.
   [  100.500456] OOM killer disabled.
   [  100.503573] Freezing remaining freezable tasks ... (elapsed 0.001 seconds) done.
   [  100.511083] printk: Suspending console(s) (use no_console_suspend to debug)

2.使用sw2按键唤醒，按下按键后，系统恢复：

.. code:: shell

   =====> Output:
   NOTICE:  CPU: STM32MP157AAC Rev.Z
   NOTICE:  Model: MYZR STM32MP15 Discovery Board
   INFO:    Reset reason (0x810):
   INFO:    System exits from STANDBY
   INFO:    PMIC version = 0x21
   INFO:    Using SDMMC
   INFO:      Instance 1
   INFO:    Boot used partition fsbl1
   NOTICE:  BL2: v2.2-r1.0(debug):
   NOTICE:  BL2: Built : 07:34:54, Apr 14 2021
   INFO:    Using crypto library 'stm32_crypto_lib'
   INFO:    BL2: Doing platform setup
   INFO:    RAM: DDR3-DDR3L 16bits 533000Khz
   INFO:    BL2 runs SP_MIN setup
   INFO:    BL2: Loading image id 4
   INFO:    Loading image id=4 at address 0x2ffed000
   INFO:    Image id=4 loaded: 0x2ffed000 - 0x2ffff000
   INFO:    BL2: Skip loading image id 5
   NOTICE:  BL2: Booting BL32
   INFO:    Entry point address = 0x2ffed000
   INFO:    SPSR = 0x1d3
   NOTICE:  SP_MIN: v2.2-r1.0(debug):
   NOTICE:  SP_MIN: Built : 07:35:03, Apr 14 2021
   INFO:    ARM GICv2 driver initialized
   INFO:    stm32mp IWDG1 (12): Secure
   INFO:    ETZPC: CRYP1 (9) could be non secure
   INFO:    SP_MIN: Initializing runtime services
   INFO:    SP_MIN: Preparing exit to normal world
   [   77.721158] dwc2 49000000.usb-otg: suspending usb gadget configfs-gadget
   [   77.764676] Disabling non-boot CPUs ...
   [   77.765689] CPU1 killed.
   [   77.775207] Enabling non-boot CPUs ...
   [   77.778224] CPU1 is up
   [   77.795959] dwmac4: Master AXI performs any burst length
   [   77.795994] stm32-dwmac 5800a000.ethernet eth0: No Safety Features support found
   [   77.796061] stm32-dwmac 5800a000.ethernet eth0: configuring for phy/rgmii-id link mode
   [   77.799109] usb usb2: root hub lost power or was reset
   [   77.802455] dwc2 49000000.usb-otg: resuming usb gadget configfs-gadget
   [   78.199987] usb 2-1: reset high-speed USB device number 2 using ehci-platform
   [   78.429336] OOM killer enabled.
   [   78.432502] Restarting tasks ... done.
   [   78.506503] PM: suspend exit

ADC测试
~~~~~~~~

|  【测试说明】：读取ADC管脚的采样输出值
|  【接口标识】：GPIO/SPI/UART
|  【接口丝印】：P21
|  【系统设备】：/sys/bus/iio/devices/iio:device*/

测试操作
~~~~~~~~

1.P21:18脚（ANA0）为adc的0通道，P21:17脚（ANA1）为adc的1通道

2.可以短接0通道和P21:40脚（即短接地），然后读取adc值

.. code:: shell
   
   =====> Input:
   # cat /sys/bus/iio/devices/iio\:device0/in_voltage0_raw

   =====> Output:
   0

3.采样的最大电压不能超过3.3V，否则可能导致核心板损坏，采样的最大输出值为 65535。