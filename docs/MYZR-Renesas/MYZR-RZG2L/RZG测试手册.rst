RZG测试手册
=============

测试环境
----------

|  rzg2l和rzg2ul使用同一套内核和uboot源码，rzg2l使用core-image-qt-myzr-rzg2l-Release.xxx.tar.bz2系统，rzg2ul使用core-image-bsp-myzr-rzg2ul-Release.xxx.tar.bz2系统。

**拿到开发板后直接使用出厂默认镜像系统进行如下功能性测试来验证，开发板正常使用后再进行后续开发**

rzg2l测试环境
~~~~~~~~~~~~~~

|  【开发板型号】：MYZR-RZG2L-MB200 + MYZR-G2L-CB200
|  【内核版本】：Linux-5.10.131-Release.xxx.tar.bz2
|  【uboot版本】：u-boot-Release.xxx.tar.bz2
|  【文件系统】：core-image-qt-myzr-rzg2l-Release.xxx.tar.bz2

rzg2ul测试环境
~~~~~~~~~~~~~~~

|  【开发板型号】：

- MYZR-RZG2UL-MB200-ETH + MYZR-G2UL-CB200
- MYZR-RZG2UL-MB200-LCD + MYZR-G2UL-CB200

|  【内核版本】：Linux-5.10.131-Release.xxx.tar.bz2
|  【uboot版本】：u-boot-Release.xxx.tar.bz2
|  【文件系统】：core-image-bsp-myzr-rzg2ul-Release.xxx.tar.bz2

接口标识图
-----------

**rzg2l**

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2l_zheng.jpg
   :alt: 1200px-Myzr_rzg2l_zheng.jpg

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2l_bei.jpg
   :alt: 1200px-Myzr_rzg2l_bei.jpg

**rzg2ul-eth**

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2ul-eth_zheng.jpg
   :alt: 1200px-Myzr_rzg2ul-eth_zheng.jpg

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2ul-eth_bei.jpg
   :alt: 1200px-Myzr_rzg2ul-eth_bei.jpg

**rzg2ul-lcd**

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2ul-lcd_zheng.jpg
   :alt: 1200px-Myzr_rzg2ul-lcd_zheng.jpg

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2ul-lcd_bei.jpg
   :alt: 1200px-Myzr_rzg2ul-lcd_bei.jpg

网口0测试
-----------

**说明**

|  【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|  【接口标识】：ETH10/100/1000M
|  【系统接口】：eth0
|  【接口丝印】：

- MYZR-RZG2L-MB200：U10
- MYZR-RZG2UL-MB200-ETH：U10
- MYZR-RZG2UL-MB200-LCD：U9

|  注：eth0设置了静态ip地址192.168.137.81

**测试操作**

1. 配置电脑有线网卡ip为 192.168.137.99
2. 网线连接板子网口和电脑网口
3. 输入如下指令与电脑通讯：

.. code-block:: shell

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

网口1测试
-----------

**说明**

|  【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|  【接口标识】：ETH10/100/1000M
|  【系统接口】：eth1
|  【接口丝印】：

- MYZR-RZG2L-MB200：U13
- MYZR-RZG2UL-MB200-ETH：U14

**测试操作**

1. 配置电脑有线网卡ip为 192.168.137.99
2. 网线连接板子网口和电脑网口
3. 输入如下指令与电脑通讯：

.. code-block:: shell

   =====> Input:
   # ifconfig eth1 192.168.137.81
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
---------

**说明**

|  【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|  【接口标识】：USB2.0
|  【接口丝印】：

- MYZR-RZG2L-MB200：J4
- MYZR-RZG2UL-MB200-ETH：J4
- MYZR-RZG2UL-MB200-LCD：J4

**测试操作**

1. 将USB设备插入底板USB接口，系统会输出类似如下信息:

.. code-block:: shell

   root@myzr-rzg2l:~# [   41.664942] usb 1-1.1: new high-speed USB device number 4 using ehci-platform
   [   41.796776] usb-storage 1-1.1:1.0: USB Mass Storage device detected
   [   41.803713] scsi host0: usb-storage 1-1.1:1.0
   [   42.819899] scsi 0:0:0:0: Direct-Access     Generic- SD/MMC           1.00 PQ: 0 ANSI: 4
   [   43.591013] sd 0:0:0:0: [sda] 60932096 512-byte logical blocks: (31.2 GB/29.1 GiB)
   [   43.599368] sd 0:0:0:0: [sda] Write Protect is off
   [   43.605215] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn\'t support DPO or FUA
   [   43.642283]  sda: sda1
   [   43.653982] sd 0:0:0:0: [sda] Attached SCSI removable disk

2. 将USB设备从底板拔出，系统会输出类似如下信息：

.. code-block:: shell

   root@myzr-rzg2l:~# [   55.524114] usb 1-1.1: USB disconnect, device number 4

SD接口测试
-----------

**说明**

|  【测试说明】：采用插入并识别TF卡的方式进行测试
|  【接口标识】：TF
|  【接口丝印】：

- MYZR-RZG2L-MB200：J8
- MYZR-RZG2UL-MB200-ETH：J7
- MYZR-RZG2UL-MB200-LCD：J7

**测试操作**

1. 将TF卡安装到SD接口，开发会输出如下信息：

.. code-block:: shell

   root@myzr-rzg2l:~# [  178.279039] mmc1: new high speed SDHC card at address 1234
   [  178.290822] mmcblk1: mmc1:1234 SA32G 29.1 GiB 
   [  178.298039]  mmcblk1: p1

2. 可以查看到对应的sd接口设备：

.. code-block:: shell

   # ls /dev/mmcblk1*
   /dev/mmcblk1  /dev/mmcblk1p1

3. 将TF卡拔出，输出如下信息：

.. code-block:: shell
   
   root@myzr-rzg2l:~# [  195.429099] mmc1: card 1234 removed

GPIO测试
----------

**说明**

|  【测试说明】：控制GPIO的输出/输入电平
|  【接口标识】：GPIO/SPI/UART
|  【系统接口】：/sys/class/gpio/
|  【接口丝印】：

- MYZR-RZG2L-MB200：P3（GPIOx_x）
- MYZR-RZG2UL-MB200-ETH：P2（GPIOx_x）
- MYZR-RZG2UL-MB200-LCD：J12（GPIOx_x）

|  注：rzg2l和rzg2ul的gpio 编号计算方式不同。

**测试操作**

**RZG2L**

1. 导出需要测试的gpio接口，以P3中的GPIO47_2为例。GPIO47_2对应核心板管脚为P47_2，对应gpio编号 = （47*8+2）+120 = 498，输入如下命令导出节点：

.. code-block:: shell

   # echo 498 > /sys/class/gpio/export 
   # ls /sys/class/gpio/
   P47_2  export  gpiochip120  unexport

2. 配置GPIO47_2脚作为输出引脚：

.. code-block:: shell

   # echo out > /sys/class/gpio/P47_2/direction

3. 配置GPIO47_2脚输出高电平：

.. code-block:: shell

   # echo 1 > /sys/class/gpio/P47_2/value

|  使用万用表测量GPIO47_2脚，可以测出大约为3.3v即高电平

4. 配置GPIO47_2脚输出低电平：

.. code-block:: shell

   # echo 0 > /sys/class/gpio/P47_2/value

|  使用万用表测量GPIO47_2脚，可以测出大约为0v即低电平

5. 配置GPIO47_2脚为输入，将管脚接地，并读取其值：

.. code-block:: shell

   # echo in > /sys/class/gpio/P47_2/direction
   # cat /sys/class/gpio/P47_2/value 
   0

**RZG2UL**

1. 导出需要测试的gpio接口，以LCD板J12中的GPIO7_3为例。GPIO7_3对应核心板管脚为P7_3，对应gpio编号 = （7*8+3）+360 = 419，输入如下命令导出节点：

.. code-block:: shell

   # echo 419 > /sys/class/gpio/export 
   # ls /sys/class/gpio/
   P7_3  export  gpiochip360  unexport

2. 配置GPIO7_3脚作为输出引脚：

.. code-block:: shell

   # echo out > /sys/class/gpio/P7_3/direction

3. 配置GPIO7_3脚输出高电平：

.. code-block:: shell

   # echo 1 > /sys/class/gpio/P7_3/value

|  使用万用表测量GPIO7_3脚，可以测出大约为3.3v即高电平

4. 配置GPIO7_3脚输出低电平：

.. code-block:: shell

   # echo 0 > /sys/class/gpio/P7_3/value

|  使用万用表测量GPIO7_3脚，可以测出大约为0v即低电平

5. 配置GPIO7_3脚为输入，将管脚接地，并读取其值：

.. code-block:: shell

   # echo in > /sys/class/gpio/P7_3/direction
   # cat /sys/class/gpio/P7_3/value 
   0

UART测试
----------

**说明**

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：GPIO/SPI/UART
|  【系统设备】：

- MYZR-RZG2L-MB200：/dev/ttySC2
- MYZR-RZG2UL-MB200-ETH：/dev/ttySC3
- MYZR-RZG2UL-MB200-LCD：NULL

|  【接口丝印】：

- MYZR-RZG2L-MB200：P3（UART2）
- MYZR-RZG2UL-MB200-ETH：P2（UART3）
- MYZR-RZG2UL-MB200-LCD：NULL

**测试操作**

|  以MYZR-RZG2L-MB200底板为例：

1. 短接P3-7和P3-9脚，即UART2_RXD 和UART2_TXD。
2. 输入如下命令进行UART2收发测试：

.. code-block:: shell

   =====> Input:
   # /my-demo/serial_test.out /dev/ttySC2 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x0   Character:  

|  执行测试指令后，应用输出如上类似信息即正常。测试完按Ctrl+c退出。

RS232测试
-----------

**说明**

|  【测试说明】：采用串口自发自收的方式进行测试
|  【接口标识】：RS232
|  【系统设备】：

- MYZR-RZG2L-MB200：/dev/ttySC0（debug串口）、/dev/ttySC1、/dev/ttySC3
- MYZR-RZG2UL-MB200-ETH：/dev/ttySC0（debug串口）、/dev/ttySC1、/dev/ttySC4
- MYZR-RZG2UL-MB200-LCD：/dev/ttySC0（debug串口）、/dev/ttySC1、/dev/ttySC4

|  【接口丝印】：

- MYZR-RZG2L-MB200：J10-11（debug串口/RS232_RX0）、J10-12（debug串口/RS232_TX0）、J10-14（RS232_RX3）、J10-15（RS232_TX3）、J10-19（RS232_RX1）、J10-20（RS232_TX1）
- MYZR-RZG2UL-MB200-ETH：J16（RS232_0(debug串口)，RS232_1，RS232_4）
- MYZR-RZG2UL-MB200-LCD：J16（RS232_0(debug串口)，RS232_1，RS232_4）

|  注：debug串口无需进行测试。

**测试操作**

|  以MYZR-RZG2L-MB200底板为例：

1. 短接J10的TX3和RX3
2. 输入如下命令进行RS232收发测试：

.. code-block:: shell

   =====> Input:
   # /my-demo/serial_test.out /dev/ttySC3 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m
   ASCII: 0x79      Character: y
   ASCII: 0x7a      Character: z
   ASCII: 0x72      Character: r
   ASCII: 0x0   Character:

|  执行测试指令后，应用输出如上类似信息即正常。测试完按Ctrl+c退出。

RS485测试
-----------

**说明**

|  【测试说明】：RS485是差分信号，不能采用自发自收的方式进行测试。
|  【接口标识】：RS485
|  【系统设备】：

- MYZR-RZG2L-MB200：/dev/ttySC4
- MYZR-RZG2UL-MB200-ETH：/dev/ttySC2
- MYZR-RZG2UL-MB200-LCD：/dev/ttySC2

|  【接口丝印】：

- MYZR-RZG2L-MB200：J10-8（B）、J10-9（A）
- MYZR-RZG2UL-MB200-ETH：J16（A、B）
- MYZR-RZG2UL-MB200-LCD：J16（A、B）

**测试操作**

|  以MYZR-RZG2UL-MB200-ETH底板为例：

1. 使用485-232转换头连接J16（A、B）脚和电脑usb转串口线
2. 打开串口调试助手，设置波特率为9600，无校验位，8位数据位，1位停止位。
3. 开发板使用ssh登录，向电脑端发送数据：

.. code-block:: shell

   # echo 123 > /dev/ttySC2

|  可以看到串口助手接收到字符串123

4. 开发板接收数据，电脑端发送数据：

.. code-block:: shell

   # cat /dev/ttySTM2

|  当串口助手发送字符串时，开发板会接收到数据：

.. code-block:: shell

   # cat /dev/ttySTM2
   myzr

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/MYZR-RZG_rs485.png
   :alt: MYZR-RZG_rs485.png

CAN测试
--------

**说明**

|  【测试说明】：can口之间互相发送数据
|  【接口标识】：CAN
|  【系统设备】：can0、can1
|  【接口丝印】：

- MYZR-RZG2L-MB200：J10-1（can0_H）、J10-3（can0_L）、J10-4（can1_H）、J10-6（can0_L）、
- MYZR-RZG2UL-MB200-ETH：J16（can0，can1）
- MYZR-RZG2UL-MB200-LCD：J16（can0）

|  注：MYZR-RZG2UL-MB200-LCD底板只有一个can口，无法进行自身收发测试，可以使用两个开发板进行can口互联。

**测试操作**

|  以MYZR-RZG2L-MB200底板为例：

1. 将CAN口进行连接，CAN0_L与CAN1_L相连；CAN0_H和CAN1_H相连。
2. 对can0和can1进行配置：

.. code-block:: shell

   # ip link set can0 up type can bitrate 500000 dbitrate 1000000 fd on
   # ip link set can1 up type can bitrate 500000 dbitrate 1000000 fd on

3. 将can0配置为接收：

.. code-block:: shell

   # candump can0 &

4. can1发送数据：

.. code-block:: shell

   # cansend can1 1F334455#1122334455667788

5. 可以接收到如下数据：

.. code-block:: shell

   can0  1F334455   [8]  11 22 33 44 55 66 77 88

SPI测试
---------

**说明**

|  【测试说明】：采用自发自收的方式测试。
|  【接口标识】：GPIO/SPI/UART
|  【系统设备】：/dev/spidev1.0
|  【接口丝印】：

- MYZR-RZG2L-MB200：P3（SPI1）
- MYZR-RZG2UL-MB200-ETH：NULL
- MYZR-RZG2UL-MB200-LCD：NULL

**测试操作**

1. 短接P3的SPI1_MOSI和SPI1_MISO，输入命令：

.. code-block:: shell

   =====> Input:
   # /my-demo/spidev_test.out -D /dev/spidev1.0

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
---------

**说明**

|  【测试说明】：读取并设置时间，断电重启后检查时间是否正确
|  【接口标识】：RTC_Battery
|  【系统设备】：/dev/rtc0
|  【接口丝印】：BT1

**测试操作**

1. 断电重启设备，查看当前系统时间和硬件时间：

.. code-block:: shell

   =====> Input:
   # date

   =====> Output:
   Wed Feb  8 11:17:01 UTC 2023

2. 查看当前RTC芯片时钟：

.. code-block:: shell

   =====> Input:
   # hwclock

   =====> Output:
   2023-02-08 11:17:13.930687+00:00

3. 设置系统时钟：

.. code-block:: shell

   =====> Input:
   # date -s "2023-02-08 15:00:00""

   =====> Output:
   Wed Feb  8 15:00:00 UTC 2023

4. 将系统时钟写入硬件时钟：

.. code-block:: shell

   # hwclock -w

5. 断电重启开发板，查看当前系统时钟和硬件时钟：

.. code-block:: shell

   =====> Input:
   # date

   =====> Output:
   Wed Feb  8 15:01:00 UTC 2023
   =====> Input:
   # hwclock

   =====> Output:
   2023-02-08 15:01:11.537317+00:00

音频播放测试
-------------

**说明**

|  【测试说明】：通过播放音频文件验证评估板的音频播放功能。
|  【接口标识】：AUDIO
|  【系统设备】：wm8960-audio
|  【接口丝印】：

- MYZR-RZG2L-MB200：P2
- MYZR-RZG2UL-MB200-ETH：P1
- MYZR-RZG2UL-MB200-LCD：P2

**测试操作**

1. 把耳机插入开发板的“AUDIO”口。执行如下命令播放音频：

.. code-block:: shell

   =====> Input:
   # aplay /usr/share/sounds/alsa/Front_Center.wav

   =====> Output:
   Playing WAVE '/usr/share/sounds/alsa/Front_Center.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Mono

2. 可以使用如下命令进行音量调节：

.. code-block:: shell

   # alsamixer

录音测试
---------

**说明**

|  【测试说明】：通过录音并播放录音文件验证评估板的音频录音功能。
|  【接口标识】：AUDIO
|  【系统设备】：wm8960-audio
|  【接口丝印】：

- MYZR-RZG2L-MB200：P3
- MYZR-RZG2UL-MB200-ETH：P1
- MYZR-RZG2UL-MB200-LCD：P2

**测试操作**

1. 把带MIC的耳机插入开发板耳机接口
2. 输入如下命令进行4秒的录音：

.. code-block:: shell

   =====> Input:
   # arecord -d 4 record.wav

   =====> Output:
   Recording WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

3. 播放录制的音频：

.. code-block:: shell

   =====> Input:
   # aplay record.wav

   =====> Output:
   Playing WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

WIFI测试
----------

**说明**

|  【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：WIFI&BT
|  【系统设备】：wlan0
|  【接口丝印】：

- MYZR-RZG2L-MB200：U22、E2（天线接口）
- MYZR-RZG2UL-MB200-ETH：U24、E2（天线接口）
- MYZR-RZG2UL-MB200-LCD：U19、E2（天线接口）

**测试操作**

1. 把WIFI天线连接到“E1/E2”接口上
2. 生成 SSID 的 WPA PSK 文件

.. code-block:: shell

   wpa_passphrase命令格式：wpa_passphrase + wifi名称 + wifi密码 > /etc/wpa_supplicant.conf

   =====> Input:
   # wpa_passphrase MYZR-WIFI-2.4G myzr2012 > /etc/wpa_supplicant.conf

3. 连接：

.. code-block:: shell

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
   。。。。。。

4. 获取IP：

.. code-block:: shell

   =====> Input:
   # udhcpc -i wlan0

   =====> Output:
   udhcpc: started, v1.31.1
   udhcpc: sending discover
   udhcpc: sending select for 192.168.9.169
   udhcpc: lease of 192.168.9.169 obtained, lease time 86400
   /etc/udhcpc.d/50default: Adding DNS 192.168.9.1

5. 测试连接：

.. code-block:: shell

   =====> Input:
   # ping -I wlan0 www.baidu.com

   =====> Output:
   [   39.924248] RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 SeqNum = 40
   PING www.baidu.com (163.177.151.109): 56 data bytes
   [   40.813870] RTW: OnAction_back
   [   40.816968] RTW: OnAction_back, action=0
   [   40.821089] RTW: Drop duplicate management frame with seq_num = 668.
   64 bytes from 163.177.151.109: seq=0 ttl=56 time=233.235 ms
   [   40.832117] RTW: issue_addba_rsp_wait_ack(wlan0) ra=40:77:a9:64:76:b2 status:=0 tid=4 size:64, acked, 1/3 in 12 ms
   64 bytes from 163.177.151.109: seq=1 ttl=56 time=22.882 ms
   64 bytes from 163.177.151.109: seq=2 ttl=56 time=8.862 ms
   64 bytes from 163.177.151.109: seq=3 ttl=56 time=9.219 ms
   64 bytes from 163.177.151.109: seq=4 ttl=56 time=7.952 ms
   64 bytes from 163.177.151.109: seq=5 ttl=56 time=400.328 ms
   64 bytes from 163.177.151.109: seq=6 ttl=56 time=11.634 ms
   ^C
   --- www.baidu.com ping statistics ---
   7 packets transmitted, 7 packets received, 0% packet loss
   round-trip min/avg/max = 7.952/99.158/400.328 ms

|  “0% packet loss”表示wifi连接正常。

蓝牙测试
----------

**说明**

|  【测试说明】：扫描到蓝牙设备后，发送L2CAP回应请求并接收回答
|  【接口标识】：WIFI&BT
|  【系统设备】：hci0
|  【接口丝印】：

- MYZR-RZG2L-MB200：U22、E2（天线接口）
- MYZR-RZG2UL-MB200-ETH：U24、E2（天线接口）
- MYZR-RZG2UL-MB200-LCD：U19、E2（天线接口）

**测试操作**

1. 把天线连接到“E2”接口上
2. 启动蓝牙：

.. code-block:: shell

   =====> Input:
   # hciconfig hci0 up
   # hciconfig 

   =====> Output:
   hci0:   Type: Primary  Bus: UART
       BD Address: B0:F1:EC:A7:E8:03  ACL MTU: 1021:8  SCO MTU: 64:1
       UP RUNNING 
       RX bytes:1266 acl:0 sco:0 events:66 errors:0
       TX bytes:1138 acl:0 sco:0 commands:66 errors:0

3. 扫描外部蓝牙设备：

.. code-block:: shell

   =====> Input:
   # hcitool scan
   
   =====> Output:
   Scanning ...
       88:46:04:4C:11:A7   Redmi K40

4. 发送发送L2CAP包测试：

.. code-block:: shell

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
   ^C8 sent, 8 received, 0% loss

|  “0% packet loss”表示蓝牙连接正常。

4G模块(EC20)测试
------------------

**说明**

|  【测试说明】：4G连接成功后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：4G
|  【系统设备】：usb0
|  【接口丝印】：

- MYZR-RZG2L-MB200：J9
- MYZR-RZG2UL-MB200-ETH：J10
- MYZR-RZG2UL-MB200-LCD：J9

**测试操作**

1. 开发板断电，接上4G模块，接上天线并插入SIM卡后启动评估板。
2. 使用指令进行网络连接：

.. code-block:: shell

   =====> Input:
   # /myzr-demo/quectel-CM &

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

3. 连接测试：

.. code-block:: shell

   =====> Input:
   # ping -I usb0 www.baidu.com

   =====> Output:
   PING www.wshifen.com (104.193.88.77) 56(84) bytes of data.
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=1 ttl=42 time=263 ms
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=2 ttl=42 time=233 ms
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=3 ttl=42 time=232 ms
   ^C
   --- www.wshifen.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2000ms
   rtt min/avg/max/mdev = 232.138/242.649/262.712/14.191 ms

|  “0% packet loss”表示4G连接正常。

DSI显示
---------

**说明**

|  【测试说明】：使用DSI显示需先进行设备树的更换。
|  【接口标识】：DSI
|  【接口丝印】：J6
|  注：DSI显示只有rzg2l才有此功能

**测试操作**

1. 启动开发板，在uboot倒数结束前按下回车键进行uboot命令行模式，输入printenv fdtfile查看当前设备树名称

.. code-block:: shell

   => printenv fdtfile 
   fdtfile=myzr-rzg2l-rgb.dtb

2. 如果当前设备树不是dsi，则进行更换：

.. code-block:: shell

   => setenv fdtfile myzr-rzg2l-dsi.dtb

3. 保存当前环境变量

.. code-block:: shell

   => saveenv 
   Saving Environment to MMC... Writing to MMC(0)... OK

4. 断电，接入DSI显示屏，启动开发板即可看到启动画面显示在显示屏上。

RGB显示
---------

**说明**

|  【测试说明】：系统默认是RGB显示，如果切换过HDMI显示需从新切换回来。
|  【接口标识】：LCD
|  【接口丝印】：

- MYZR-RZG2L-MB200：P1
- MYZR-RZG2UL-MB200-ETH：NULL
- MYZR-RZG2UL-MB200-LCD：P1

|  注：只有MYZR-RZG2L-MB200和MYZR-RZG2UL-MB200-LCD有lcd显示功能，MYZR-RZG2UL-MB200-LCD对应设备树为：myzr-rzg2ul-lcd.dtb，无需进行更换。

**测试操作**

|  更换rzg2l为rgb显示：

1. 启动开发板，在uboot倒数结束前按下回车键进行uboot命令行模式，输入printenv fdtfile查看当前设备树名称

.. code-block:: shell

   => printenv fdtfile 
   fdtfile=myzr-rzg2l-dsi.dtb

2. 如果当前设备树不是rgb，则进行更换：

.. code-block:: shell

   => setenv fdtfile myzr-rzg2l-rgb.dtb

3. 保存当前环境变量

.. code-block:: shell

   => saveenv 
   Saving Environment to MMC... Writing to MMC(0)... OK

4. 断电，接入rgb显示屏，启动开发板即可看到启动画面显示在显示屏上。

ADC测试
---------

**说明**

|  【测试说明】：读取ADC管脚的采样输出值
|  【接口标识】：GPIO/SPI/UART
|  【系统设备】：/sys/bus/iio/devices/iio:devicex
|  【接口丝印】：

- MYZR-RZG2L-MB200：J11
- MYZR-RZG2UL-MB200-ETH：P2（ADC_CH0 、ADC_CH01）
- MYZR-RZG2UL-MB200-LCD：J12（ADC_CH0 、ADC_CH01）

**测试操作**

|  以MYZR-RZG2L-MB200底板为例：

1. 查找ADC对应的外设：

.. code-block:: shell

   # grep -H "" /sys/bus/iio/devices/*/name | grep adc
   /sys/bus/iio/devices/iio:device0/name:rzg2l-adc

|  可知adc通道节点在/sys/bus/iio/devices/iio:device0目录下

2. 可以短接ADC_CH0通道和J11:1脚（即短接地），然后读取adc值

.. code-block:: shell

   =====> Input:
   # cat /sys/bus/iio/devices/iio\:device0/in_voltage0_raw

   =====> Output:
   0

3. 采样的最大电压不能超过1.8V，否则可能导致核心板损坏，采样的最大输出值为 4096。