MYZR-LS1012A-EK200 Linux-4.4.98 测试手册
===========================================

测试环境
----------

|   【开发板型号】：MYZR-LS1012A-EK200
|   【内核版本】：Linux-4.4.98
|   【文件系统】：rootfs.tar.gz
|   【工具版本】：CW_ARMv8_v2019.01_b190130_Win_Offline
|   说明：为保证测试无误，需要使用的烧录工具版本应不低于2019.01


接口标识图
----------

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/1275px-LS1012A-interface.jpg
   :alt: 1275px-LS1012A-interface.jpg

网口测试（ETH1）
----------------

|   【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|   【接口标识】：ETH1
|   【接口丝印】：U2
|   【系统接口】：eth0

**测试操作**

|   配置电脑有线网卡IP为 192.168.137.99。
|   用网线连接开发板的ETH1和电脑。
|   配置开发板网口：

.. code:: shell

    =====> 输入指令:
    ifconfig eth1 down 
    ifconfig eth0 192.168.137.81

|   测试ETH1（eth0）：

.. code:: shell

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
-----------------

|   【测试说明】：采用开发板向PC发送ICMP报文的方式进行测试
|   【接口标识】：ETH2
|   【接口丝印】：U1
|   【系统接口】：eth1

**测试操作**

|   配置电脑有线网卡IP为 192.168.137.99。
|   用网线连接开发板的ETH2和电脑。
|   配置开发板网口

.. code:: shell

    =====> 输入指令:
    ifconfig eth0 down
    ifconfig eth1 192.168.137.82 

|   测试ETH2（eth1）：

.. code:: shell

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


vsftpd测试
------------

|   【测试说明】：开发板与电脑之间文件的传输
|   【接口标识】：无
|   【接口丝印】：无
|   【系统接口】：无

**测试操作**

|   网线连接电脑与开发板网口1
|   配置电脑有线网卡IP为 192.168.137.99
|   打开我的电脑输入：ftp://192.168.137.81

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/Ls1012a-vsftpd.png
   :alt: Ls1012a-vsftpd.png

|   弹出登录界面，用户名输入root，密码无

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/Ls1012a-vsftpd2.png
   :alt: Ls1012a-vsftpd2.png

|   登录后，会进入到开发板的/home/root/目录，即可进行文件传输操作。

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/Ls1012a-vsftpd3.png
   :alt: Ls1012a-vsftpd3.png

USB测试
---------

|   【测试说明】：采用插拔USB存储设备（U盘）的方式进行测试
|   【接口标识】：USB3.0/USB2.0
|   【接口丝印】：J10

**测试方法**

|   将USB设备插入底板USB接口。

.. code:: shell

    =====> 输入指令:
    df  

    =====> 输出信息： 
    Filesystem     1K-blocks    Used Available Use% Mounted on  
    /dev/root        3691872  119072   3381928   4% /  
    devtmpfs          197896       4    197892   1% /dev  
    tmpfs             206364     216    206148   1% /run  
    tmpfs             206364     136    206228   1% /var/volatile  
    /dev/sda1       30450128 5837584  24612544  20% /run/media/sda1  

|   将USB设备从底板拔出。

.. code:: shell

    =====> 输入指令:
    df  

    =====> 输出信息： 
    Filesystem     1K-blocks    Used Available Use% Mounted on  
    /dev/root        3691872  119072   3381928   4% /  
    devtmpfs          197896       4    197892   1% /dev  
    tmpfs             206364     216    206148   1% /run  
    tmpfs             206364     136    206228   1% /var/volatile  

**测试结果**

|   USB存储设备插入时可查看到sda1设备。


SD接口测试
------------

|   【测试说明】：采用插拔SD卡的方式进行测试
|   【接口标识】：SD_CARD
|   【接口丝印】：J9

**测试方法**

|   将SD卡插入SD接口。

.. code:: shell

    =====> 输入指令:
    df  

    =====> 输出信息： 
    Filesystem     1K-blocks   Used Available Use% Mounted on
    /dev/root        3691872 119320   3381680   4% /
    devtmpfs          197896      4    197892   1% /dev
    tmpfs             206364    216    206148   1% /run
    tmpfs             206364    128    206236   1% /var/volatile
    /dev/mmcblk1p1    511384 258580    252804  51% /run/media/mmcblk1p1

|   将SD卡从底板拔出。

.. code:: shell

    =====> 输入指令:
    df  

    =====> 输出信息： 
    Filesystem     1K-blocks    Used Available Use% Mounted on  
    /dev/root        3691872  119072   3381928   4% /  
    devtmpfs          197896       4    197892   1% /dev  
    tmpfs             206364     216    206148   1% /run  
    tmpfs             206364     136    206228   1% /var/volatile  

**测试结果**

|   SD卡插入时可查看到sda1设备。


RS232测试(RS232_3)
-------------------

|   【测试说明】：采用自发自收的方式进行测试
|   【接口标识】：RS232/RS485
|   【接口位置】：J1
|   【系统设备】：/dev/TtyXRUSB2

**测试操作**

|   短接RS232_3的发送和接收管脚（J1下列从左往右第5/6接口）
|   (J1下列从左往右依次为：RS2232_TX1,RS232_RX1,RS232_TX2,RS232_RX2,RS232_TX3,RS232_RX3,空脚，空脚
|   对应的系统设备依次为：ttyXRUSB0、ttyXRUSB1、ttyXRUSB2)
|   执行测试指令：

.. code:: shell

    =====> 输入指令:
    /my-demo/uart_test.out /dev/ttyXRUSB2 "www.myzr.com.cn"  

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

RS485测试(RS485_1)
--------------------

|   【测试说明】：采用差分的方式进行测试
|   【接口标识】：RS232/RS485
|   【接口位置】：J1
|   【系统设备】：/dev/TtyXRUSB3

**测试操作**

|   使用Telnet登录开发板。
|   485-232转接头连接开发板RS485_1的收发管脚（J1上列第1/2接口），转接头+接A，—接B。
|   (J1上列从左往右依次为：RS485_A1,RS485_B1,RS485_A2,RS485_B2,RS485_A3,RS485_B3,空脚，空脚
|   对应的系统设备依次为：ttyXRUSB3、ttyXRUSB4、ttyXRUSB5)
|   转接头另一端与电脑USB转串口线相连。
|   设置串口终端波特率为9600。
|   执行测试指令：

.. code:: shell

    =====> 输入指令:
    echo "myzr" > /dev/ttyXRUSB3

    =====> 串口端输出信息：
    myzr
    =====> 输入指令:
    cat /dev/ttyXRUSB3

    =====> 串口端输入：
    myzr

    =====> 开发板输出信息：
    myzr

**测试结果**

|   执行测试指令后，应用输出如上类似信息即正常。

GPIO输入测试
--------------

|   【测试说明】：采用按键中断方式
|   【接口标识】：DI
|   【接口位置】：J2
|   【系统设备】：/sys/class/gpio/

**测试操作**

|   DI接口对应的gpio为：
|   gpio440 ---->I2C_3_GPIO1_0_IN J2下1,2
|   gpio441 ---->I2C_3_GPIO1_1_IN J2上1,2
|   gpio442 ---->I2C_3_GPIO1_2_IN J2下3,4
|   gpio443 ---->I2C_3_GPIO1_3_IN J2上3,4
|   gpio444 ---->I2C_3_GPIO1_4_IN J2下5,6
|   gpio445 ---->I2C_3_GPIO1_5_IN J2上5,6
|   gpio446 ---->I2C_3_GPIO1_6_IN J2下7,8
|   gpio447 ---->I2C_3_GPIO1_7_IN J2上7,8

|   使用GPIO测试板J2接口连接开发板DI上列或下列。
|   给测试板接上5v电源。
|   执行测试指令：

.. code:: shell

    =====> 输入指令:
    chmod +x /home/root/gpio-in.sh  
    /home/root/gpio-in.sh  

    =====> 输出信息：
    gpio440
    gpio441
    gpio442
    gpio443
    gpio444
    gpio445
    gpio446
    gpio447

|   查看gpio按键中断次数：

.. code:: shell

    =====> 输入指令:
    cat /proc/interrupts | grep gpio  

    =====> 输出信息：
     25:          0  mpc8xxx-gpio  22 Edge      0-0026
     29:          0   pca953x   8 Edge      gpiolib
     30:          0   pca953x   9 Edge      gpiolib
     31:          0   pca953x  10 Edge      gpiolib
     32:          0   pca953x  11 Edge      gpiolib
     33:          0   pca953x  12 Edge      gpiolib
     34:          0   pca953x  13 Edge      gpiolib
     35:          0   pca953x  14 Edge      gpiolib
     36:          0   pca953x  15 Edge      gpiolib

|   按下测试版相应gpio的按键若干次，重复查看中断次数：

.. code:: shell

    =====> 输入指令:
    cat /proc/interrupts | grep gpio  

    =====> 输出信息：
     25:         20  mpc8xxx-gpio  22 Edge      0-0026
     29:          2   pca953x   8 Edge      gpiolib
     30:          0   pca953x   9 Edge      gpiolib
     31:          4   pca953x  10 Edge      gpiolib
     32:          0   pca953x  11 Edge      gpiolib
     33:          2   pca953x  12 Edge      gpiolib
     34:          0   pca953x  13 Edge      gpiolib
     35:          2   pca953x  14 Edge      gpiolib
     36:          0   pca953x  15 Edge      gpiolib

**测试结果**

|   执行指测操作后，应用输出如上类似信息即正常。

GPIO输出测试
--------------

|   【测试说明】：控制GPIO输出电平
|   【接口标识】：DO
|   【接口位置】：J3
|   【系统设备】：/sys/class/gpio/

**测试操作**

|   DO接口对应的gpio为：
|   gpio432 ----> I2C_3_GPIO0_0_OUT J3下1,2
|   gpio433 ----> I2C_3_GPIO0_1_OUT J3上1,2
|   gpio434 ----> I2C_3_GPIO0_2_OUT J3下3,4
|   gpio435 ----> I2C_3_GPIO0_3_OUT J3上3,4
|   gpio436 ----> I2C_3_GPIO0_4_OUT J3下5,6
|   gpio437 ----> I2C_3_GPIO0_5_OUT J3上5,6
|   gpio438 ----> I2C_3_GPIO0_6_OUT J3下7,8
|   gpio439 ----> I2C_3_GPIO0_7_OUT J3上7,8

|   使用GPIO测试板J3接口连接开发板DO上列或下列。
|   给测试板接上5v电源。
|   执行测试指令：

.. code:: shell

    =====> 输入指令:
    chmod +x /home/root/gpio-out.sh  
    /home/root/gpio-out.sh  

    =====> 输出信息：
    goio432
    goio433
    goio434
    goio435
    goio436
    goio437
    goio438
    goio439
    Please add the parameter 1 or 0

|   控制输出高电平：

.. code:: shell

    =====> 输入指令:
    /home/root/gpio-out.sh 1    

|   控制输出低电平：

.. code:: shell

    =====> 输入指令:
    /home/root/gpio-out.sh 0

**测试结果**

|   输出高电平时，相应的四个led灯点亮；
|   输出低电平时，相应的四个led灯熄灭。

WIFI模块RTL8723du测试
-----------------------

|   【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|   【接口标识】：WIFI&BT,WIFI_ANT
|   【接口丝印】：U24，E1
|   【系统设备】：wlan0

**测试操作**

1. 确定“WIFI”标识处有贴上WIFI模块，否则无需进行测试。
2. 把WIFI天线连接到“WIFI_ANT”标识的接口上。
3. 生成 SSID 的 WPA PSK 文件

|   命令格式: wpa_passphrase <ssid> [passphrase]

.. code:: shell

    =====> 输入指令:
    wpa_passphrase MY-TEST-AP myzr2012 > /etc/wpa_supplicant.conf
    pkill wpa_supplicant

4. 连接

.. code:: shell

    =====> 输入指令:
    wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

    =====> 输出信息：
    Successfully initialized wpa_supplicant
    rfkill: Cannot open RFKILL control device
    ioctl[SIOCSIWAP]: Operation not permitted

5. 获取 IP

.. code:: shell

    =====> 输入指令:
    udhcpc -i wlan0

    =====> 输出信息：
    udhcpc (v1.23.2) started
    Sending discover...
    Sending select for 192.168.43.99...
    Lease of 192.168.43.99 obtained, lease time 3600
    /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

6. 测试连接

.. code:: shell

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

|   “0% packet loss”表示WIFI连接正常。


蓝牙测试
----------

|   【测试说明】：蓝牙连接后，开发板与手机发送信息来验证连接正常。
|   【接口标识】：WIFI，WIFI_ANT
|   【接口丝印】：U24，E1
|   【系统设备】：hci0

**测试操作**

1. 确定“WIFI”标识处有贴上WIFI模块，否则无需进行测试。
2. 把WIFI天线连接到“WIFI_ANT”标识的接口上。
3. 查看hci0

.. code:: shell

    =====> 输入指令:
    hciconfig -a

    =====> 输出信息：
    hci0:   Type: BR/EDR  Bus: USB
        BD Address: 74:EE:2A:46:E8:83  ACL MTU: 1021:8  SCO MTU: 255:12
        DOWN 
        RX bytes:590 acl:0 sco:0 events:31 errors:0
        TX bytes:372 acl:0 sco:0 commands:31 errors:0
        Features: 0xff 0xff 0xff 0xfe 0xdb 0xfd 0x7b 0x87
        Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3 
        Link policy: RSWITCH HOLD SNIFF PARK 
        Link mode: SLAVE ACCEPT 

4. 启动hci0

.. code:: shell

    =====> 输入指令:
    hciconfig hci0 up

    =====> 输出信息：
    [  283.065459] rtk_btusb: btusb_open hdev->promisc ==0

5. 扫描蓝牙

.. code:: shell

    =====> 输入指令:
    hcitool scan

    =====> 输出信息：
    Scanning ...
        A4:50:46:9E:11:86   小米手机

6. 测试连接

.. code:: shell

    =====> 输入指令:
    l2ping A4:50:46:9E:11:86

    =====> 输出信息：
    Ping: A4:50:46:9E:11:86 from 74:EE:2A:46:E8:83 (data size 44) ...
    44 bytes from A4:50:46:9E:11:86 id 0 time 5022.50ms
    44 bytes from A4:50:46:9E:11:86 id 1 time 57.15ms
    44 bytes from A4:50:46:9E:11:86 id 2 time 26.12ms

**测试结果**

|   “0% packet loss”表示蓝牙连接正常。


4G模块EC20测试
----------------

|   【测试说明】：4G连接成功后，开发板向外网发送ICMP报文来验证连接正常。
|   【接口标识】：3G/4G
|   【接口丝印】：J5
|   【系统设备】：eth2

**测试操作**

1. 开发板断电，接上4G模块，接上天线并插入SIM卡后启动评估板。
2. 使用指令进行网络连接：

.. code:: shell

    =====> 输入指令:
    /my-demo/quectel-CM &

    =====> 输出信息：
    [1] 607
    [09-21_13:36:14:352] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
    [09-21_13:36:14:353] /my-demo/gcc-linaro-5.3-arm/quectel-CM.out profile[1] = (null)/(null)/(null)/0, pincode = (null)
    [09-21_13:36:14:356] Find /sys/bus/usb/devices/1-1.2 idVendor=2c7c idProduct=0125
    [09-21_13:36:14:356] Find /sys/bus/usb/devices/1-1.2:1.4/net/eth2
    [09-21_13:36:14:356] Find usbnet_adapter = eth2
    [09-21_13:36:14:356] Find /sys/bus/usb/devices/1-1.2:1.4/GobiQMI/qcqmi2
    [09-21_13:36:14:357] Find qmichannel = /dev/qcqmi2
    [09-21_13:36:14:403] Get clientWDS = 7
    [09-21_13:36:14:435] Get clientDMS = 8
    [09-21_13:36:14:467] Get clientNAS = 9
    [09-21_13:36:14:499] Get clientUIM = 10
    [09-21_13:36:14:532] Get clientWDA = 11
    [09-21_13:36:14:563] requestBaseBandVersion EC20CEFAR02A10M4G
    [09-21_13:36:14:659] requestGetSIMStatus SIMStatus: SIM_READY
    [09-21_13:36:14:692] requestGetProfile[1] cmnet///0
    [09-21_13:36:14:724] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
    [09-21_13:36:14:755] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
    [09-21_13:36:14:819] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
    [09-21_13:36:16:036] requestSetupDataCall WdsConnectionIPv4Handle: 0x87756f40
    [09-21_13:36:16:132] requestQueryDataCall IPv4ConnectionStatus: CONNECTED
    [09-21_13:36:16:163] ifconfig eth2 up
    [09-21_13:36:16:193] busybox udhcpc -f -n -q -t 5 -i eth2
    [09-21_13:36:16:211] udhcpc (v1.24.1) started
    [09-21_13:36:16:318] Sending discover...
    [09-21_13:36:16:378] Sending select for 10.151.159.101...
    [09-21_13:36:16:438] Lease of 10.151.159.101 obtained, lease time 7200
    [09-21_13:36:16:522] /etc/udhcpc.d/50default: Adding DNS 221.179.38.7
    [09-21_13:36:16:522] /etc/udhcpc.d/50default: Adding DNS 120.196.165.7

3. 测试连接

.. code:: shell

    =====> 输入指令:
    ifconfig eth0 down
    ping -I eth2 www.baidu.com -c 2 -w 4

    =====> 输出信息：
    PING www.baidu.com (14.215.177.38): 56 data bytes
    64 bytes from 14.215.177.38: seq=0 ttl=49 time=15.753 ms
    64 bytes from 14.215.177.38: seq=1 ttl=49 time=11.835 ms

    --- www.baidu.com ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 11.835/13.794/15.753 ms

**测试结果**

|   “0% packet loss”表示连接正常。