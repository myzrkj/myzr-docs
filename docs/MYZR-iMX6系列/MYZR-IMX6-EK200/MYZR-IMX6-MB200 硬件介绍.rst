
MYZR-IMX6-MB200 硬件介绍
===========================

接口概览
---------

正面图
~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6ek200_front_.jpg
   :alt: Myimx6ek200_front_.jpg

背面图
~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/963px-Myimx6ek200_rear_view.jpg
   :alt: 963px-Myimx6ek200_rear_view.jpg

尺寸图
~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/971px-Myimx6ek200_dimension_.jpg
   :alt: 971px-Myimx6ek200_dimension_.jpg

接口功能
---------

18/24bit LVDS0
~~~~~~~~~~~~~~~~

|  丝印：J24
|  LVDS0液晶是24bit模式，兼容18bit模式，通过此接口可连接明远智睿公司生产的不同尺寸规格的电阻LVDS液晶屏和电容LVDS液晶屏。LVDS0接口座采用了进口连接器，抛弃了国内便宜的抽屉式，采用的是对面按压式，保证安装更容易，性能，连接性更好。
|  引脚及信号定义如下：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.1.0.1.png
   :alt: Myimx6_mb200_2.1.0.1.png

======  =====================  ==============
 引脚           信号                描述
======  =====================  ==============
J24-16  SD1_DAT1/TOUCH_nEINT1  GPIO控制(复位)
J24-17  NANDF_CS3              GPIO控制(中断)
J24-19  DISP0_CONTRAST         LVDS0背光调节
J24-21  TOUCH_SCL              I2C时钟
J24-22  TOUCH_SDA              I2C数据
======  =====================  ==============

18/24bit RGB
~~~~~~~~~~~~~~

|  丝印:J23
|  RGB液晶是24bit模式，兼容18bit/16bit模式，通过此接口可连接明远智睿公司生产的不同尺寸规格的电阻RGB液晶屏和电容RGB液晶屏。RGB液晶接口座采用了进口连接器，抛弃了国内便宜的抽屉式，采用的是对面按压式，保证安装更容易，性能，连接性更好。
|  引脚及信号定义：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.2.0.1.png
   :alt: Myimx6_mb200_2.2.0.1.png

======  =====================  ==============
 引脚           信号                描述
======  =====================  ==============
J23-31  SD1_DAT1/TOUCH_nEINT1  GPIO控制(复位)
J23-30  NANDF_CS3              GPIO控制(中断)
J23-19  DISP0_CONTRAST         LVDS0背光调节
J23-32  TOUCH_SCL              I2C时钟
J23-33  TOUCH_SDA              I2C数据
======  =====================  ==============

18/24bit LVDS1
~~~~~~~~~~~~~~~~

|  丝印：J22
|  LVDS1液晶接口跟LVDS0液晶接口定义，接插件型号完全一样，用户可以直接把LVDS0处的液晶直接接到LVDS1处。
|  引脚及信号定义：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.3.0.1.png
   :alt: Myimx6_mb200_2.3.0.1.png

======  =====================  ==============
 引脚           信号                描述
======  =====================  ==============
J22-16  SD1_DAT1/TOUCH_nEINT1  GPIO控制(复位)
J22-17  NANDF_CS3              GPIO控制(中断)
J22-19  DISP0_CONTRAST         LVDS0背光调节
J22-21  TOUCH_SCL              I2C时钟
J22-22  TOUCH_SDA              I2C数据
======  =====================  ==============

10M/100M Ethernet-1
~~~~~~~~~~~~~~~~~~~~~

|  丝印：P4
|  接口属性：百兆网标准接口

耳机输出
~~~~~~~~~

|  丝印：J20
|  接口属性：音频信号输出，3.5mm接口

麦克风输入
~~~~~~~~~~~

|  丝印：J18
|  接口属性：音频信号输入，3.5mm接口

HDMI
~~~~~~

|  丝印：J5
|  接口属性：HDMI-1.4标准接口

SATA电源
~~~~~~~~~

|  丝印：J12
|  引脚及信号定义：

=====  ====  ==========
引脚   信号     描述
=====  ====  ==========
J12-1  5VIN  5V电源输入
J12-2  GND   数字地
J12-3  GND   数字地
J12-4  NC    未连接
=====  ====  ==========

OTG
~~~~~

|  丝印：J5
|  接口属性：USB ON-The-GO，用于烧写

SATA II
~~~~~~~~~

|  丝印：J11
|  接口属性：3Gbps SATA II标准接口

10M/100M Ethernet-2
~~~~~~~~~~~~~~~~~~~~~

|  丝印：P3
|  接口属性：百兆网标准接口

USB扩展
~~~~~~~~

|  丝印:J8
|  接口属性：USB1扩展双USB，标准USB接口

调试串口
~~~~~~~~~

|  丝印：P2
|  接口属性：3线标准RS232接口，用作调试串口

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.13.0.1.png
   :alt: Myimx6_mb200_2.13.0.1.png

主电源开关
~~~~~~~~~~~

|  丝印：J3
|  接口属性：电源开关
|  状态属性：—，闭合；O，断开

主电源输入
~~~~~~~~~~

|  丝印：J4
|  接口属性：内正外负插孔
|  电压：5V
|  电流：2.5A及以上

复位
~~~~~~

|  丝印：SW1
|  功能：复位

唤醒
~~~~~~

|  丝印：SW2
|  接口属性：休眠唤醒

音量加
~~~~~~~~

|  丝印：SW3
|  接口属性：音量控制（音量加）

音量减
~~~~~~~~

|  丝印：SW2
|  接口属性：音量控制（音量减）

RS-232串口
~~~~~~~~~~~~

|  丝印：P1
|  接口属性：UART4，3线标准RS232接口

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.20.0.1.png
   :alt: Myimx6_mb200_2.20.0.1.png

RS-485串口
~~~~~~~~~~~~

|  丝印：J2
|  接口属性：UART3，RS-485串口

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.21.0.1.png
   :alt: Myimx6_mb200_2.21.0.1.png

MINI-PCIE
~~~~~~~~~~~

|  丝印：J6
|  接口属性：标准MINI-PCIE接口

串口扩展/TTL电平
~~~~~~~~~~~~~~~~~

|  丝印：J1

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.23.0.1.png
   :alt: Myimx6_mb200_2.23.0.1.png

GPIO/SD2
~~~~~~~~~~

|  丝印：J4

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.24.0.1.png
   :alt: Myimx6_mb200_2.24.0.1.png

SPI扩展
~~~~~~~~

|  丝印：J7

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.25.0.1.png
   :alt: Myimx6_mb200_2.25.0.1.png

SIM卡座
~~~~~~~~

|  丝印：CON1
|  接口属性：标准的SIM卡座

MIPI-CSI
~~~~~~~~~

|  丝印:J9

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.27.0.1.png
   :alt: Myimx6_mb200_2.27.0.1.png

CMOS-CSI
~~~~~~~~~~

|  丝印:J14

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.28.0.1.png
   :alt: Myimx6_mb200_2.28.0.1.png

CAN2
~~~~~~

|  丝印:J16
|  接口属性：CAN2

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.29.0.1.png
   :alt: Myimx6_mb200_2.29.0.1.png

CAN1
~~~~~~

|  丝印:J19
|  接口属性：CAN1

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.30.0.1.png
   :alt: Myimx6_mb200_2.30.0.1.png

I2C扩展
~~~~~~~~

|  丝印:J21

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.31.0.1.png
   :alt: Myimx6_mb200_2.31.0.1.png

GPS天线座
~~~~~~~~~~~

|  丝印:E4
|  接口属性：天线座

GPS
~~~~~

|  丝印:U15
|  模块型号：NEO-6M

MINI_PCIE_FPC
~~~~~~~~~~~~~~~

|  丝印:J26
|  注意：跟标准的MINI_PCIE座子不能同时使用，即2选1。

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.34.0.1.png
   :alt: Myimx6_mb200_2.34.0.1.png

SD3
~~~~~

|  丝印:J25
|  接口属性：标准SD卡座

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.35.0.1.png
   :alt: Myimx6_mb200_2.35.0.1.png

WIFI
~~~~~~

|  丝印:U16
|  模块型号：UM12BS

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.36.0.1.png
   :alt: Myimx6_mb200_2.36.0.1.png

RTC
~~~~

|  丝印:U19
|  接口属性：I2C通信的实时时钟

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/963px-Myimx6_mb200_2.37.0.1.png
   :alt: 963px-Myimx6_mb200_2.37.0.1.png

RTC_Batter
~~~~~~~~~~~~

|  丝印:BT1
