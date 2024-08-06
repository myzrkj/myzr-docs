
MYZR-RK3288-EK314 Android-5.1 测试手册
========================================

测试前的准备
-------------

|   1）准备MYZR-RK3288-EK314开发板一套，5V直流稳压电源，USB转串口线。
|   2）接上串口线，给开发板供电，启动板子。


测试项目
---------

网口测试
~~~~~~~~~~

|   MYZR-RK3288-EK314 评估板支持双网口，一个百兆，另一个千兆。

**接口属性**

+-------------------+----------+-----------------+----------+
|    评估板型号     | 接口位置 |  接口速率标准   | 系统接口 |
+===================+==========+=================+==========+
| MYZR-RK3288-EK314 | U13      | 10/100/1000Mbps | eth0     |
+                   +----------+-----------------+----------+
|                   | P1       | 10/100Mbps      | eth1     |
+-------------------+----------+-----------------+----------+

**测试方法**

|   1） 测试说明

- 需要使用路由器，默认网关为192.168.137.1

|   2） Eth0连接测试

- 连接网线：将评估板“eth0”对应的接口与网络路由器用网线相连接
- 附图

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.1.2.png
   :alt: My-rk32-ek314_android_test_2.1.2.png

|   3） Eth1连接测试

- 连接网线：将网线插入“eth1”对应的评估板接口，网线另一端保持与网络路由器的接口连接
- 设置第2个网口IP：

.. code:: shell

    ＃ ifconfig eth1 192.168.137.100 　　　　　＃ configure the eth1
    ＃ ping -I eth1 192.168.137.1 　　　　　＃ send ICMP to HOST

- 附图

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.1.3.png
   :alt: My-rk32-ek314_android_test_2.1.3.png


USB测试
~~~~~~~~~~

**接口属性**

+-------------------+----------+--------------+
|    评估板型号     | 接口位置 | 接口速率标准 |
+===================+==========+==============+
| MYZR-RK3288-EK314 | J10      | 480 Mbits/s  |
+-------------------+----------+--------------+

**测试方法**

|   1） 开始测试
|   将USB设备插入底板USB接口，点击“ApkInstaller“->”Install“->”USB Memory“
|   2） 测试结束
|   将USB设备从底板拔出

**附图**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.2.1.png
   :alt: My-rk32-ek314_android_test_2.2.1.png

SD卡测试
~~~~~~~~~~

**接口属性**

+-------------------+----------+----------+
|    评估板型号     | 接口位置 | 接口类型 |
+===================+==========+==========+
| MYZR-RK3288-EK314 | U22      | SD       |
+-------------------+----------+----------+

**开始测试**

|   1） 往SD卡槽插入设备
|   插入SD卡到底板SD卡接口，点击”ApkInstaller”->“Install”->“TF Card”
|   2） 结束测试
|   SD卡弹出后拨出SD卡即结束测试。

**附图**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.3.1.png
   :alt: My-rk32-ek314_android_test_2.3.1.png

背光测试
~~~~~~~~~~

|   点击“Setting”->“Display”->“Brightness level”

**附图**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.4.1.png
   :alt: My-rk32-ek314_android_test_2.4.1.png

音频测试
~~~~~~~~~~

**测试说明**

|   这项测试是通过播放音频文件验证评估板的音频功能。

**测试方法**

|   1）准备测试
|   连接音频输出设备到底板正面的音频座子，音频座子在底板正面“P15”。
|   2）执行测试
|   用U盘准备mp3音频文件，插上U盘，直接打开mp3文件

**附图**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.5.1.png
   :alt: My-rk32-ek314_android_test_2.5.1.png


标准GPIO测试
~~~~~~~~~~~~~

**接口属性**

+-------------------+---------+----------+--------+
|    评估板型号     | LED标号 | GPIO属性 | IO序号 |
+===================+=========+==========+========+
| MYZR-RK3288-EK314 | D1      | GPIO0_B1 | 9      |
+                   +---------+----------+--------+
|                   | D2      | GPIO0_C2 | 18     |
+                   +---------+----------+--------+
|                   | D3      | GPIO0_B0 | 8      |
+                   +---------+----------+--------+
|                   | D4      | GPIO0_A7 | 7      |
+-------------------+---------+----------+--------+

**测试方法**

|   1）GPIO输出测试
|   设置需要测试的GPIO的IO序号

.. code:: shell

    ＃ OUT_IO_NUMBER=9

|  导出GPIO

.. code:: shell

    ＃ echo ${OUT_IO_NUMBER} > /sys/class/gpio/export

|  设置GPIO方向

.. code:: shell

    ＃ echo out > /sys/class/gpio/gpio${OUT_IO_NUMBER}/direction

|  控制输出电平

.. code:: shell

    ＃ echo 0 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value
    ＃ echo 1 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.6.1.png
   :alt: My-rk32-ek314_android_test_2.6.1.png

|   2）GPIO输入测试
|   设置需要测试的GPIO的IO序号

.. code:: shell

    ＃ IN_IO_NUMBER=18

|  导出GPIO

.. code:: shell

    ＃ echo ${IN_IO_NUMBER} > /sys/class/gpio/export

|  设置GPIO方向

.. code:: shell

    ＃ echo in > /sys/class/gpio/gpio${IN_IO_NUMBER}/direction

|  查看输入电平

.. code:: shell

    cat /sys/class/gpio/gpio${IN_IO_NUMBER}/value

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.5.2.png
   :alt: My-rk32-ek314test_2.5.2.png


GPIO-KEY测试
~~~~~~~~~~~~~

**接口属性**

+-------------------+-----------+-------------+
| MYZR-RK3288-EK314                           |
+===================+===========+=============+
| 接口位置          | GPIO属性  | KEY属性     |
+-------------------+-----------+-------------+
| SW1               | gpio-keys | Volume Down |
+-------------------+-----------+-------------+
| SW2               | gpio-keys | Volume Up   |
+-------------------+-----------+-------------+
| SW3               | gpio-keys | Power       |
+-------------------+-----------+-------------+
| SW4               | gpio-keys | Reset       |
+-------------------+-----------+-------------+
| SW5               | gpio-keys | Recovery    |
+-------------------+-----------+-------------+

**测试方法**

|   直接按SW1和SW2

**附图**


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.7.1.png
   :alt: My-rk32-ek314_android_test_2.7.1.png


串口测试
~~~~~~~~~~

|   MYZR-RK3288-EK314共3个串口，其中1个调试串口，2个用户串口。

**用户串口属性**

+-------------------+-------+----------------+----------+
|    评估板型号     | UARTx |    硬件接口    | 系统接口 |
+===================+=======+================+==========+
| MYZR-RK3288-EK314 | UART0 | BT (Bluetooth) | ttyS0    |
+                   +-------+----------------+----------+
|                   | UART1 | P3             | ttyS1    |
+                   +-------+----------------+----------+
|                   | UART2 | P4 (DEBUG)     | ttyS2    |
+-------------------+-------+----------------+----------+

|   提示：这里列出串口的收发管脚，串口其它管脚的定义请看原理图。

**串口测试**

- 安装串口软件APK
- 附图

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.8.1.png
   :alt: My-rk32-ek314_android_test_2.8.1.png


RTC测试
~~~~~~~~

**测试说明**

|   受快递运输影响，MYZR-RK3288-EK314 系列评估板发货时不带电池。测试RTC前请自备纽扣电池并安装到评估板上。
|   MYZR-RK3288-EK314的电池座在底板正面的“BT1”位置。

**测试方法**

|   1）开机后查看"clock"

- 附图

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.9.1.png
   :alt: My-rk32-ek314_android_test_2.9.1.png

|   2）关机后，等一会儿再开机：

- 附图

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.9.2.png
   :alt: My-rk32-ek314_android_test_2.9.2.png

SPI测试
---------

|   MYZR-RK3288-EK314上有两组SPI接口。

**接口属性**

|   测试需要用到SPI接口的MISO和MOSI管脚，在下表中列出。

+-------------------+------+--------+--------+-----------+
|    评估板型号     | SPIx |  MISO  |  MOSI  | 系统接口  |
+===================+======+========+========+===========+
| MYZR-RK3288-EK314 | SPI1 | J11:33 | J11:35 | spidev0.0 |
+                   +------+--------+--------+-----------+
|                   | SPI2 | J11:38 | J13:34 | spidev2.0 |
+-------------------+------+--------+--------+-----------+

**测试说明**

|   1）采用SPI自发送（输出）自接收（输入）的方式。
|   注意：测试需要短接评估板的管脚，如果不确定自己能正确短接的请找硬件工程师支持，否则可能会损坏评估板。
|   2）与SPI测试程序匹配的SPI接口是SPI2，所以我们的SPI测试是测试SPI2。

**测试方法**

|   1）准备测试
|   短接SPI0的MISO和MOSI管脚。
|   2）执行测试

.. code:: shell

    ＃ ./spi_test -D /dev/spidev0.0

|   3）测试结果
|   如果SPI正常，在终端上会看到如下字符：

.. code:: shell

    FF FF FF FF FF FF
    40 00 00 00 00 95
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    DE AD BE EF BA AD
    F0 0D

**附图**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.10.1.png
   :alt: My-rk32-ek314_android_test_2.10.1.png

摄像头OV13850测试
~~~~~~~~~~~~~~~~~~

|   接上摄像头，启动，接着打开“Camera”，会出现如下：

- 附图


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.11.1.png
   :alt: My-rk32-ek314_android_test_2.11.1.png

WIFI测试
~~~~~~~~~~

|   MYZR-RK3288-EK314 评估板使用的WIFI芯片型号为AP6335
|   1）步骤一
|   点击“Settings”->“Wi-Fi”，打开WIFI的开关

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.12.1.png
   :alt: My-rk32-ek314_android_test_2.12.1.png

|   2）步骤二
|   输入WIFI密码,并连接成功


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.12.2.png
   :alt: My-rk32-ek314_android_test_2.12.2.png

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.12.3.png
   :alt: My-rk32-ek314_android_test_2.12.3.png


蓝牙测试
~~~~~~~~~~

|   MYZR-RK3288-EK314 评估板使用的Bluetooth芯片型号为AP6335
|   1）步骤一
|   点击“Settings”->“Bluetooth”，打开蓝牙

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.13.1.png
   :alt: My-rk32-ek314_android_test_2.13.1.png

|   2）步骤二
|   匹配

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.13.2.png
   :alt: My-rk32-ek314_android_test_2.13.2.png

|   3）步骤三
|   发送和接收文件

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.13.3.png
   :alt: My-rk32-ek314_android_test_2.13.3.png

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.13.4.png
   :alt: My-rk32-ek314_android_test_2.13.4.png


4G测试
~~~~~~~~

**测试说明**

|   测试上网4G模块，如L506。

**测试方法**

- 接上模块，开机，显示3G标志

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_test_2.14.1.png
   :alt: My-rk32-ek314_android_test_2.14.1.png


HDMI测试
~~~~~~~~~

**测试说明**

|   接上HDMI显示屏。

**测试方法**

- 烧写resource-hdmi.img

|   用AndroidTool_Release_v2.35烧写。

- 测试

|   开机，HDMI有显示图像

- 修改分辨率

|   想修改分辨率，可以修改arch/arm/boot/dts/lcd-box.dtsi。


EDP测试
~~~~~~~~~

**测试说明**

|   接上EDP显示屏。

**测试方法**

- 烧写resource-edp.img

|   用AndroidTool_Release_v2.35烧写。

- 测试

|   开机，EDP有显示图像

- 修改分辨率

|   想修改分辨率，可以修改arch/arm/boot/dts/lcd-EDP1080p.dtsi。