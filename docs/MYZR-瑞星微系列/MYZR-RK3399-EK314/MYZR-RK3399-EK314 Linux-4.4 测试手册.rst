
MYZR-RK3399-EK314 Linux-4.4 测试手册
=====================================

第一部分 测试说明
-----------------

|   开发板的用户名为：myzr
|   密码：myzr
|   root用户密码：root

第二部分 接口测试
-----------------

以太网测试
~~~~~~~~~~

|   MYZR-RK3399评估板有一个千兆的网口

+-------------------+----------+-----------------+----------+
|    评估版型号     | 接口位置 |  接口速率标准   | 系统接口 |
+===================+==========+=================+==========+
| MYZR-RK3399-EK314 | P19      | 10/100/1000Mbps | eth0     |
+-------------------+----------+-----------------+----------+

**测试操作**

|   配置电脑有线网卡IP为 192.168.18.18。
|   把开发板的这个网口用网线跟电脑网口连接起来。
|   配置开发板网口：

.. code:: shell

    =====> 输入指令:
    ifconfig eth0 192.168.18.36

**测试网口**

.. code:: shell

    =====> 输入指令:
    ping 192.168.18.18 -c 2 -w 4
    =====> 输出信息：
    --- 192.168.18.18 ping statistics --- 
    2packets transmitted, 2 packets received, 0% packet loss

**测试结果**

|   “0% packet loss”表示测试通过。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.1.png
   :alt: My-rk3399-ek314_test2.1.1.png

USB接口测试
~~~~~~~~~~~~

+-------------------+----------+----------+
|    评估版型号     | 接口位置 | 接口类型 |
+===================+==========+==========+
| MYZR-RK3399-EK314 | P8       | USB3.0   |
+-------------------+----------+----------+

**测试方法**
|   将USB设备插入底板USB接口，输入以下命令:

.. code:: shell
    
    ＃ df -h

|   将USB设备从底板拔出，输入以下命令：

.. code:: shell
    
    ＃ df -h

**测试结果**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.2.png
   :alt: My-rk3399-ek314_test2.1.2.png

SD接口测试
~~~~~~~~~~~

+-------------------+----------+----------+
|    评估版型号     | 接口位置 | 接口类型 |
+===================+==========+==========+
| MYZR-RK3399-EK314 | P15      | SD       |
+-------------------+----------+----------+

**测试方法**

|   往SD卡槽插入设备，插入SD卡到底板SD卡接口，输入以下命令：

.. code:: shell
    
    ＃ df -h

|   SD卡弹出后拨出SD卡即结束测试。

**测试结果**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.3.png
   :alt: My-rk3399-ek314_test2.1.3.png

标准GPIO测试
~~~~~~~~~~~~~

+-------------------+----------+----------+--------+
|    评估版型号     | GPIO标号 | GPIO属性 | IO序号 |
+===================+==========+==========+========+
| MYZR-RK3399-EK314 | P21-3    | GPIO1_B0 | 40     |
+                   +----------+----------+--------+
|                   | P21-5    | GPIO1_A7 | 39     |
+                   +----------+----------+--------+
|                   | P21-7    | GPIO1_B2 | 42     |
+                   +----------+----------+--------+
|                   | P21-9    | GPIO1_B1 | 41     |
+                   +----------+----------+--------+
|                   | P5-3     | GPIO1_A7 | 92     |
+                   +----------+----------+--------+
|                   | P5-4     | GPIO1_C6 | 54     |
+                   +----------+----------+--------+
|                   | P5-5     | GPIO1_C7 | 55     |
+                   +----------+----------+--------+
|                   | P5-6     | GPIO2_D3 | 91     |
+                   +----------+----------+--------+
|                   | P5-7     | GPIO4_D0 | 152    |
+                   +----------+----------+--------+
|                   | P5-8     | GPIO4_C6 | 150    |
+-------------------+----------+----------+--------+

**GPIO输出测试**

|   配置P8-3为输出高、低电平的操作方法：

.. code:: shell
    
    =====> 输入指令:
    ＃ OUT_IO_NUMBER=92
    导出GPIO
    ＃ echo ${OUT_IO_NUMBER} > /sys/class/gpio/export
    设置GPIO方向
    ＃ echo out > /sys/class/gpio/gpio${OUT_IO_NUMBER}/direction
    控制输出电平
    ＃ echo 0 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value
    ＃ echo 1 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.4.png
   :alt: My-rk3399-ek314_test2.1.4.png

|   用万用表测试管脚P8-3

**GPIO输入测试**

|   配置P8-3输入的操作方法：

.. code:: shell
    
    设置需要测试的GPIO的IO序号
    ＃ IN_IO_NUMBER=91
    导出GPIO
    ＃ echo ${IN_IO_NUMBER} > /sys/class/gpio/export
    设置GPIO方向
    ＃ echo in > /sys/class/gpio/gpio${IN_IO_NUMBER}/direction
    查看输入电平
    cat /sys/class/gpio/gpio${IN_IO_NUMBER}/value

ADC-KEY测试
~~~~~~~~~~~~

+-------------------+----------+----------+-------------+
|    评估版型号     | 接口位置 |   属性   |   KEY属性   |
+===================+==========+==========+=============+
| MYZR-RK3399-EK314 | SW5      | adc-keys | Volume UP   |
+                   +----------+----------+-------------+
|                   | SW4      | adc-keys | Volume Down |
+                   +----------+----------+-------------+
|                   | SW3      | adc-keys | Home        |
+                   +----------+----------+-------------+
|                   | SW2      | adc-keys | Esc         |
+                   +----------+----------+-------------+
|                   | SW1      | adc-keys | Menu        |
+-------------------+----------+----------+-------------+

**测试操作**

|   安装evtest

.. code:: shell
    
    =====> 输入指令:
    $ sudo apt-get install evtest

|   运行 evtest 准备测试

.. code:: shell
    
    =====> 输入指令:
    evtest 
        选择测试设备
    Select the device event number [0-2]: 1
    输入“adc-keys”对应的序号，这里是1

        按动开发板上的按键

**测试结果**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.5.png
   :alt: My-rk3399-ek314_test2.1.5.png

**结束测试**

|   按计算机上的“Ctrl”+“C”可结束按键测试程序。

RTC测试
~~~~~~~~~

**测试说明**

.. code:: shell
    
    受快递运输影响，MYZR-RK3399-EK314 系列评估板发货时不带电池。测试RTC前请自备纽扣电池并安装到评估板上。MYZR-RK3399-EK314的电池座在底板背面的“BT1”位置。

**测试操作**

1. 断电重启设备，查看当前系统时间和硬件时间：

.. code:: shell
    
    =====> 输入指令: 
    date

    =====> 输出信息：
    Thu Aug 6 05:35:17 UTC 2012

2. 查看当前RTC芯片时钟：

.. code:: shell
    
    =====> 输入指令: 
    hwclock 

    =====> 输出信息：
    Thu Aug 6 05:35:59 2012 0.000000 seconds

3. 设置系统时钟，并同步到RTC芯片

.. code:: shell
    
    =====> 输入指令: 
    date -s "2019-07-04 12:30:30"

4. 将系统时钟写入硬件时钟

.. code:: shell
    
    =====> 输入指令:
    hwclock -w  

**测试结果**

|   执行第3步以后看到的时钟为新设定的时钟。

音频播放测试
~~~~~~~~~~~~

**测试说明**

|   这项测试是通过播放音频文件验证评估板的音频功能。

**测试操作**

|   连接音频输出设备到底板正面的音频座子，音频座子在底板正面“P6”。
|   执行测试命令：

.. code:: shell
    
    =====> 输入指令:
    ＃aplay /usr/share/sounds/alsa/Rear_Left.wav

**测试结果**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.6.png
   :alt: My-rk3399-ek314_test2.1.6.png

第三部分 显示功能测试
---------------------

**测试说明**

|   接上EDP显示屏。

**测试方法**

|   烧写boot_edp.img
|   用AndroidTool_Release_v2.58烧写。

**测试结果**

|   开机，EDP有显示图像 


第四部分 扩展模块功能演示
-------------------------

WIFI模块测试
~~~~~~~~~~~~~

|   MYZR-RK3399-EK314 评估板使用的WIFI芯片型号为AP6354

**测试操作**

1. 点击屏幕右上角网络设置的图标会弹出网络列表
2. 选择要连接的wifi,单击
3. 在弹出的窗口中输入wifi密码，点击连接

蓝牙模块测试
~~~~~~~~~~~~

|   MYZR-RK3399-EK314 评估板使用的WIFI芯片型号为AP6354

**测试操作**

1. 点击屏幕右上角蓝牙图标，在弹出的列表中点击Devices选项。  
2. 在弹出的窗口中点击“Search”开始搜索蓝牙。  

4G模块测试
~~~~~~~~~~~

|   测试上网4G模块，如L506。

**测试操作**

.. code:: shell
    
    安装wvdial
    =====> 输入指令:
    sudo apt-get install wvdial

    修改配置文件/etc/wvdial.conf
    =====> 输入指令:
    ＃ vim /etc/wvdial.conf

    增加以下内容：
    [Dialer Defaults] 
    Modem = /dev/ttyUSB2 
    Baud = 115200 
    Init1 = ATZ 
    Init2 = AT+CGDCONT=1,"IP","CMNET" 
    Init3 = AT+CGEQREQ=1,2,128,384,,,0,,,,,, 
    Phone = *99*1# 
    Username = cmnet 
    Password = cmnet 
    New PPPD = yes

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.7.png
   :alt: My-rk3399-ek314_test2.1.7.png

|   拨号

.. code:: shell
    
    =====> 输入指令:
    #wvdial &

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.8.png
   :alt: My-rk3399-ek314_test2.1.8.png