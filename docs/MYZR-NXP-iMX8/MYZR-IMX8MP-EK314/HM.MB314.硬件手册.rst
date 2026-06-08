
底板硬件手册
============

接口概览
--------

正面图
~~~~~~

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-EK314.png
   :alt: image-MYZR-IMX8MP-EK314

正面标识图
~~~~~~~~~~~~

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-EK314.正面标识.png
   :alt: image-MYZR-IMX8MP-EK314正面标识

尺寸
~~~~~~~

|  187.43mm*110

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP_MB314-size.png
   :alt: image-RK3588-MB314-size

接口功能
--------

RTC
~~~

丝印:U25 接口属性：I2C通信的实时时钟

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-RTC.png
   :alt: image-MYZR-IMX8MP-MB314-RTC

WIFI
~~~~

丝印:U21 模块型号：UM12BS

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-WIFI.png
   :alt: image-MYZR-IMX8MP-MB314-WIFI

SD
~~

丝印:J10 接口属性：标准SD卡座

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-SD.png
   :alt: image-MYZR-IMX8MP-MB314-SD

USB
~~~

丝印:J3

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-USB.png
   :alt: image-MYZR-IMX8MP-MB314-USB

HDML
~~~~

丝印：J4

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-HDML.png
   :alt: image-MYZR-IMX8MP-MB314-HDML

DSI
~~~

丝印：J5

引脚及信号定义如下:

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-DSI.png
   :alt: image-MYZR-IMX8MP-MB314-DSI

CSI
~~~

丝印：J6和J7

引脚及信号定义如下:

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-CSI1.png
   :alt: image-MYZR-IMX8MP-MB314-CSI1

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-CSI2.png
   :alt: image-MYZR-IMX8MP-MB314-CSI2

LVDS
~~~~

丝印：J8和J9

引脚及信号定义如下:

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-LVDS1.png
   :alt: image-MYZR-IMX8MP-MB314-LVDS1

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-LVDS2.png
   :alt: image-MYZR-IMX8MP-MB314-LVDS2

调试串口
~~~~~~~~

丝印：P2

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-DEBUG.png
   :alt: image-MYZR-IMX8MP-MB314-DEBUG

主电源开关
~~~~~~~~~~

丝印：J1

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-SWITCH.png
   :alt: image-MYZR-IMX8MP-MB314-SWITCH

UART - RS232和UART - RS485
~~~~~~~~~~~~~~~~~~~~~~~~~~

丝印：J14

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-UART.png
   :alt: image-MYZR-IMX8MP-MB314-UART

JTAG
~~~~

丝印：J15

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-JTAG.png
   :alt: image-MYZR-IMX8MP-MB314-JTAG

RESET
~~~~~

丝印：SW1和SW2

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-RESET1.png
   :alt: image-MYZR-IMX8MP-MB314-RESET1

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-RESET2.png
   :alt: image-MYZR-IMX8MP-MB314-RESET2

扩展IO接口
~~~~~~~~~~

丝印：J13

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-IO.png
   :alt: image-MYZR-IMX8MP-MB314-IO

====== ========== ====== ===========
引脚   信号       引脚   信号
====== ========== ====== ===========
J13:1  VDD_5V     J13:2  VDD_5V
J13:3  VDD_3V3    J13:4  VDD_3V3
J13:5  VDD_1V8    J13:6  VDD_1V8
J13:7  GND        J13:8  GND
J13:9  I2C1_SCL   J13:10 SD1_CLK
J13:11 I2C1_SDA   J13:12 SD1_CMD
J13:13 TCPC_nINT  J13:14 SD1_DATA0
J13:15 TCPC_nINT1 J13:16 SD1_DATA1
J13:17 NAND_DQS   J13:18 SD1_DATA2
J13:19 CSI2_SYNC  J13:20 SD1_DATA3
J13:21 UART3_RTS  J13:22 SD1_RESET_B
J13:23 UART3_CTS  J13:24 SAI2_TXFS
J13:25 GPIO1_IO00 J13:26 SAI2_TXC
J13:27 GPIO1_IO01 J13:28 SAI2_TXD
J13:29 GPIO1_IO05 J13:30 SAI2_RXD
J13:31 GPIO1_IO12 J13:32 GND
J13:33 PWM4       J13:34 PDM_CLK
====== ========== ====== ===========

--------------------------------------------------------------------------------

::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2023/4/26  
   * Supporter: Zhong JiaYi
   --------------------------------------------------------------------------------
