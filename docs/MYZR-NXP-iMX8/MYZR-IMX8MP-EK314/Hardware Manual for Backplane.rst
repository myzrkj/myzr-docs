Hardware Manual for Backplane
===============================

Overview of Interfaces
------------------------

Front View
~~~~~~~~~~~~

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-EK314.png
   :alt: image-MYZR-IMX8MP-EK314

Front Label Diagram
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-EK314.正面标识.png
   :alt: image-MYZR-IMX8MP-EK314正面标识

Dimensions
~~~~~~~~~~~~

|  187.43mm*110

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP_MB314-size.png
   :alt: image-RK3588-MB314-size

Interface Functions
---------------------

RTC
~~~~~

|  Silk Screen: U25  
|  Interface Attribute: Real-Time Clock with I2C Communication

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-RTC.png
   :alt: image-MYZR-IMX8MP-MB314-RTC

WIFI
~~~~~~

|  Silk Screen: U21  
|  Module Model: UM12BS

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-WIFI.png
   :alt: image-MYZR-IMX8MP-MB314-WIFI

SD
~~~~

|  Silk Screen: J10  
|  Interface Attribute: Standard SD Card Slot

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-SD.png
   :alt: image-MYZR-IMX8MP-MB314-SD

USB
~~~~~

|  Silk Screen: J3

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-USB.png
   :alt: image-MYZR-IMX8MP-MB314-USB

HDMI
~~~~~~

|  Silk Screen: J4

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-HDML.png
   :alt: image-MYZR-IMX8MP-MB314-HDML

DSI
~~~~~

|  Silk Screen: J5
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-DSI.png
   :alt: image-MYZR-IMX8MP-MB314-DSI

CSI
~~~~~

|  Silk Screen: J6 and J7
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-CSI1.png
   :alt: image-MYZR-IMX8MP-MB314-CSI1

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-CSI2.png
   :alt: image-MYZR-IMX8MP-MB314-CSI2

LVDS
~~~~~~

|  Silk Screen: J8 and J9
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-LVDS1.png
   :alt: image-MYZR-IMX8MP-MB314-LVDS1

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-LVDS2.png
   :alt: image-MYZR-IMX8MP-MB314-LVDS2

Debug Serial Port
~~~~~~~~~~~~~~~~~~~

|  Silk Screen: P2

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-DEBUG.png
   :alt: image-MYZR-IMX8MP-MB314-DEBUG

Main Power Switch
~~~~~~~~~~~~~~~~~~~

|  Silk Screen: J1

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-SWITCH.png
   :alt: image-MYZR-IMX8MP-MB314-SWITCH

UART - RS232 and UART - RS485
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Silk Screen: J14

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-UART.png
   :alt: image-MYZR-IMX8MP-MB314-UART

JTAG
~~~~~~

|  Silk Screen: J15

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-JTAG.png
   :alt: image-MYZR-IMX8MP-MB314-JTAG

RESET
~~~~~~~

|  Silk Screen: SW1 and SW2

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-RESET1.png
   :alt: image-MYZR-IMX8MP-MB314-RESET1

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-RESET2.png
   :alt: image-MYZR-IMX8MP-MB314-RESET2

Expansion IO Interface
~~~~~~~~~~~~~~~~~~~~~~~~

|  Silk Screen: J13

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-MB314-IO.png
   :alt: image-MYZR-IMX8MP-MB314-IO

======  ==========  ======  ===========
 Pin      Signal     Pin      Signal
======  ==========  ======  ===========
J13:1   VDD_5V      J13:2   VDD_5V
J13:3   VDD_3V3     J13:4   VDD_3V3
J13:5   VDD_1V8     J13:6   VDD_1V8
J13:7   GND         J13:8   GND
J13:9   I2C1_SCL    J13:10  SD1_CLK
J13:11  I2C1_SDA    J13:12  SD1_CMD
J13:13  TCPC_nINT   J13:14  SD1_DATA0
J13:15  TCPC_nINT1  J13:16  SD1_DATA1
J13:17  NAND_DQS    J13:18  SD1_DATA2
J13:19  CSI2_SYNC   J13:20  SD1_DATA3
J13:21  UART3_RTS   J13:22  SD1_RESET_B
J13:23  UART3_CTS   J13:24  SAI2_TXFS
J13:25  GPIO1_IO00  J13:26  SAI2_TXC
J13:27  GPIO1_IO01  J13:28  SAI2_TXD
J13:29  GPIO1_IO05  J13:30  SAI2_RXD
J13:31  GPIO1_IO12  J13:32  GND
J13:33  PWM4        J13:34  PDM_CLK
======  ==========  ======  ===========