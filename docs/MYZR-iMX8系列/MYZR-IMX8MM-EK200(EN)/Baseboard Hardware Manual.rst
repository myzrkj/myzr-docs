Baseboard Hardware Manual
===========================

Interface Overview
---------------------

Front View
~~~~~~~~~~~~

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-EK200.png
   :alt: image-MYZR-IMX8MM-EK200

Front Label
~~~~~~~~~~~~~

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-EK200.正面标识.png
   :alt: image-MYZR-IMX8MM-EK200.正面标识

Interface Functions
----------------------

RTC
~~~~~

|  Silk Screen: U21  
|  Interface Attribute: Real-time clock with I2C communication

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-RTC.png
   :alt: image-MYZR-IMX8MM-MB200-RTC

WIFI
~~~~

|  Silk Screen: U17  
|  Module Model: UM12BS 

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-WIFI.png
   :alt: image-MYZR-IMX8MM-MB200-WIFI

SD
~~~~

|  Silk Screen: J8  
|  Interface Attribute: Standard SD card socket

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-SD.png
   :alt: image-MYZR-IMX8MM-MB200-SD

USB
~~~~~

Silk Screen: J4

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-USB.png
   :alt: image-MYZR-IMX8MM-MB200-USB

DSI
~~~~~~

|  Silk Screen: J6

|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-DSI.png
   :alt: image-MYZR-IMX8MM-MB200-DSI

CSI
~~~~~

|  Silk Screen: J7

|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-CSI.png
   :alt: image-MYZR-IMX8MM-MB200-CSI


Bootloader Interface
~~~~~~~~~~~~~~~~~~~~~~~

|  Silk Screen: J14

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-Download.png
   :alt: image-MYZR-IMX8MM-MB200-Download

+-------------+-------------------+
| Pins Used   | Function          |
+-------------+-------------------+
| USB1_DN USB | Differential Data |
+-------------+-------------------+
| USB1_DP USB | Differential Data |
+-------------+-------------------+

Debug Serial Port
~~~~~~~~~~~~~~~~~~~

|  Silk Screen: P2

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-DEBUG.png
   :alt: image-MYZR-IMX8MM-MB200-DEBUG

Main Power Switch
~~~~~~~~~~~~~~~~~~~

|  Silk Screen: J1

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-SWITCH.png
   :alt: image-MYZR-IMX8MM-MB200-SWITCH

UART - RS232 and UART - RS485
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Silk Screen: J12

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-UART.png
   :alt: image-MYZR-IMX8MM-MB200-UART

JTAG
~~~~~~

|  Silk Screen: J13

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-JTAG.png
   :alt: image-MYZR-IMX8MM-MB200-JTAG

RESET
~~~~~~~

|  Silk Screen: SW2

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-RESET.png
   :alt: image-MYZR-IMX8MM-MB200-RESET

Extended IO Interface
~~~~~~~~~~~~~~~~~~~~~~~

|  Silk Screen: J10

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MM-EK200/MYZR-IMX8MM-MB200-IO.png
   :alt: image-MYZR-IMX8MM-MB200-IO.png

+--------+---------------+--------+-----------+
| Pin    | Signal        | Pin    | Signal    |
+--------+---------------+--------+-----------+
| J10:1  | VDD_5V        | J10:2  | VDD_5V    |
+--------+---------------+--------+-----------+
| J10:3  | VDD_3V3       | J10:4  | GND       |
+--------+---------------+--------+-----------+
| J10:5  | GND           | J10:6  | SAI1_RXFS |
+--------+---------------+--------+-----------+
| J10:7  | SAI5_RXFS     | J10:8  | SAI1_TXC  |
+--------+---------------+--------+-----------+
| J10:9  | PDM_CLK       | J10:10 | SAI2_RXD  |
+--------+---------------+--------+-----------+
| J10:11 | PDM_DATA0     | J10:12 | SAI2_TXD  |
+--------+---------------+--------+-----------+
| J10:13 | PDM_DATA1     | J10:14 | SAI2_TXFS |
+--------+---------------+--------+-----------+
| J10:15 | PDM_DATA2     | J10:16 | SAI2_TXC  |
+--------+---------------+--------+-----------+
| J10:17 | PDM_DATA3     | J10:18 | SAI2_MCLK |
+--------+---------------+--------+-----------+
| J10:19 | SAI5_MCLK     | J10:20 | SAI3_RXFS |
+--------+---------------+--------+-----------+
| J10:21 | REF_CLK_32K   | J10:22 | SAI3_RXC  |
+--------+---------------+--------+-----------+
| J10:23 | SD2_VSEL      | J10:24 | GND       |
+--------+---------------+--------+-----------+
| J10:25 | ENET_WoL      | J10:26 | PWM2      |
+--------+---------------+--------+-----------+
| J10:27 | SPDIF_TX      | J10:28 | PWM3      |
+--------+---------------+--------+-----------+
| J10:29 | SPDIF_RX      | J10:30 | PWM4      |
+--------+---------------+--------+-----------+
| J10:31 | SPDIF_EXT_CLK | J10:32 | GND       |
+--------+---------------+--------+-----------+
| J10:33 | I2C4_SDA      | J10:34 | I2C1_SCL  |
+--------+---------------+--------+-----------+
| J10:35 | GND           | J10:36 | I2C1_SDA  |
+--------+---------------+--------+-----------+
| J10:37 | PMIC_nINT     | J10:38 | GND       |
+--------+---------------+--------+-----------+

+--------+--------------+--------+-----------+
| Pin    | Signal       | Pin    | Signal    |
+--------+--------------+--------+-----------+
| J11:1  | VDD_3V3      | J11:2  | GND       |
+--------+--------------+--------+-----------+
| J11:3  | SD1_STROBE   | J11:4  | SD1_CLK   |
+--------+--------------+--------+-----------+
| J11:5  | WL_REG_ON    | J11:6  | SD1_CMD   |
+--------+--------------+--------+-----------+
| J11:7  | WL_WAKE_HOST | J11:8  | SD1_DATA0 |
+--------+--------------+--------+-----------+
| J11:9  | BT_WAKE_HOST | J11:10 | SD1_DATA1 |
+--------+--------------+--------+-----------+
| J11:11 | BT_WAKE_DEV  | J11:12 | SD1_DATA2 |
+--------+--------------+--------+-----------+
| J11:13 | BT_REG_ON    | J11:14 | SD1_DATA3 |
+--------+--------------+--------+-----------+

+-------+-------------+-------+-------------+
| Pin   | Signal      | Pin   | Signal      |
+-------+-------------+-------+-------------+
| J5:1  | VDD_1V8     | J5:2  | VDD_3V3     |
+-------+-------------+-------+-------------+
| J5:3  | QSPIA_nSS0  | J5:4  | ECSPI1_SS0  |
+-------+-------------+-------+-------------+
| J5:5  | QSPIA_DATA0 | J5:6  | ECSPI1_SCLK |
+-------+-------------+-------+-------------+
| J5:7  | QSPIA_DATA1 | J5:8  | ECSPI1_MISO |
+-------+-------------+-------+-------------+
| J5:9  | QSPIA_DATA2 | J5:10 | ECSPI1_MOSI |
+-------+-------------+-------+-------------+
| J5:11 | QSPIA_DATA3 | J5:12 | GND         |
+-------+-------------+-------+-------------+
| J5:13 | QSPIA_SCLK  | J5:14 | ECSPI2_SS0  |
+-------+-------------+-------+-------------+
| J5:15 | GND         | J5:16 | ECSPI2_SCLK |
+-------+-------------+-------+-------------+
| J5:17 | GND         | J5:18 | ECSPI2_MISO |
+-------+-------------+-------+-------------+
| J5:19 | VDD_3V3     | J5:20 | ECSPI2_MOSI |
+-------+-------------+-------+-------------+