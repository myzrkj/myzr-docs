MYZR-IMX6-MB314 Hardware Introduction
========================================

Overview of interfaces
-------------------------

Front view(MB314+CB314)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/1275px-My-imx6ek314_front.jpg
   :alt: 1275px-My-imx6ek314_front.jpg

Front view(MB314 + CB336)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/1275px-MY-IMX6-EK336-front.jpg
   :alt: 1275px-MY-IMX6-EK336-front.jpg

Rear view(MB314)
~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6ek314_back.jpg
   :alt: 963px-My-imx6ek314_back.jpg

Size（MB314）
~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6ek314_dimension.jpg
   :alt: 963px-My-imx6ek314_dimension.jpg

Interface function
--------------------

2 bit dial switch
~~~~~~~~~~~~~~~~~~~

|   Silk screen：SW1
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.1.0.1.png
   :alt: 963px-My-imx6-mb314-2.1.0.1.png

+--------------+-------+-------+
| Mode control | 1 bit | 2 bit |
+--------------+-------+-------+
| Burning mode | 1     | 0     |
+--------------+-------+-------+
| Booting mode | 0     | 1     |
+--------------+-------+-------+

Volume down
~~~~~~~~~~~~~~

|   Silk screen：SW2
|   Interface property: volume control(volume down)
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.2.0.1.png
   :alt: 963px-My-imx6-mb314-2.2.0.1.png

Volume up
~~~~~~~~~~~~

|  Silk screen：SW3
|  Interface property: volume control(volume up)
|  Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.3.0.1.png
   :alt: 963px-My-imx6-mb314-2.3.0.1.png

Wake up
~~~~~~~~~

|  Silk screen：SW4
|  Interface property:sleeping wake up
|  Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.4.0.1.png
   :alt: 963px-My-imx6-mb314-2.4.0.1.png

Reset
~~~~~~~

|  Silk screen：SW5
|  Interface property: system reset
|  Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.5.0.1.png
   :alt: 963px-My-imx6-mb314-2.5.0.1.png

18/24bit RGB
~~~~~~~~~~~~~~

|   Silk screen：J21
|   RGB crystal liquid is 24bit mode，compatible to 18bit/16bit mode,through which RGB resistance screen panel and RGB capacitor screen panel in different sizes and specifications produced by MYZR can be connected，RGB interface block is build with connector imported，abandon the cheap drawer type produced domestically，which is opposite press type to ensure easier installation,better performance and connectivity.
|   Sefinition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.6.0.1.png
   :alt: My-imx6-mb314-2.6.0.1.png

+--------+----------------+--------------------------+--------+-------------------------+------------------+
| Pin    | Signal         | Description              | Pin    | Signal                  | Description      |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-1  | DISP0_DAT4     | LCD data4                | J21-21 | DISP0_DRDY              | LCD_DataEn       |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-2  | DISP0_DAT10    | LCD data10               | J21-22 | DISP0_DAT1              | LCD data1        |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-3  | DISP0_DAT2     | LCD data2                | J21-23 | DISP0_DAT3              | LCD data3        |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-4  | DISP0_DAT21    | LCD data21               | J21-24 | DISP0_DAT8              | LCD data8        |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-5  | DISP0_DAT6     | LCD data6                | J21-25 | DISP0_DAT13             | LCD data13       |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-6  | DISP0_DAT20    | LCD data20               | J21-26 | DISP0_DAT15             | LCD data15       |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-7  | DISP0_DAT19    | LCD data19               | J21-27 | DISP0_DAT11             | LCD data11       |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-8  | DISP0_HSYNCH   | LCD row clock            | J21-28 | DISP0_DAT23             | LCD data23       |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-9  | DISP0_DAT0     | LCD data0                | J21-29 | DISP0_DAT16             | LCD data16       |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-10 | DISP0_DAT7     | LCD data7                | J21-30 | NANDF_CS3               | GPIO control     |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-11 | DISP0_DAT5     | LCD data5                | J21-31 | SD1_DAT1/TOUCH_nEINT1   | GPIO control     |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-12 | DISP0_DAT12    | LCD data12               | J21-32 | TOUCH_SCL               | I2C clock        |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-13 | DISP0_DAT9     | LCD data9                | J21-33 | TOUCH_SDA               | I2C data         |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-14 | DISP0_DAT17    | LCD data17               | J21-34 | 5VIN                    | 5V input         |
+--------+----------------+--------------------------+--------+                         +                  +
| J21-15 | DISP0_DAT14    | LCD data14               | J21-35 |                         |                  |
+--------+----------------+--------------------------+--------+                         +                  +
| J21-16 | DISP0_DAT22    | LCD data22               | J21-36 |                         |                  |
+--------+----------------+--------------------------+--------+-------------------------+------------------+
| J21-17 | DISP0_DAT18    | LCD data18               | J21-37 | GND                     | digital ground   |
+--------+----------------+--------------------------+--------+                         +                  +
| J21-18 | DISP0_CLK      | LCD dot clock            | J21-38 |                         |                  |
+--------+----------------+--------------------------+--------+                         +                  +
| J21-19 | DISP0_CONTRAST | LCD backlight adjustment | J21-39 |                         |                  |
+--------+----------------+--------------------------+--------+                         +                  +
| J21-20 | DISP0_VSYNCH   | LCD frame clock          | J21-40 |                         |                  |
+--------+----------------+--------------------------+--------+-------------------------+------------------+

18/24bit LVDS0
~~~~~~~~~~~~~~~~

|   Silk screen：J20
|   LVDS0 crystal liquid is 24bit mode，compatible to 18bit mode,through which LVDS resistance screen panel and LVDS capacitor screen panel in different sizes and specifications produced by MYZR can be connected, LVDS0 interface block is build with connector imported，abandon the cheap drawer type produced domestically，which is opposite press type to ensure easier installation, better performance and connectivity.
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.7.0.1.png
   :alt: My-imx6-mb314-2.7.0.1.png

+--------+-----------------------+----------------------------+--------+-------------+----------------+
| Pin    | Signal                | Description                | Pin    | Signal      | Description    |
+--------+-----------------------+----------------------------+--------+-------------+----------------+
| J20-1  | LVDS0_TX1_N           | LVDS0 differential data 1  | J20-21 | TOUCH_SCL   | I2C clock      |
+--------+-----------------------+                            +--------+-------------+----------------+
| J20-2  | LVDS0_TX1_P           |                            | J20-22 | TOUCH_SDA   | I2C data       |
+--------+-----------------------+----------------------------+--------+-------------+----------------+
| J20-3  | GND                   | digital ground             | J20-23 | GND         | digital ground |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-4  | LVDS0_TX0_P           | LVDS0 differential data 0  | J20-24 |             |                |
+--------+-----------------------+                            +--------+             +                +
| J20-5  | LVDS0_TX0_N           |                            | J20-25 |             |                |
+--------+-----------------------+----------------------------+--------+-------------+----------------+
| J20-6  | GND                   | digital ground             | J20-26 | 5VIN        | 5V input       |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-7  | LVDS0_TX3_N           | LVDS0 differential data 3  | J20-27 |             |                |
+--------+-----------------------+                            +--------+             +                +
| J20-8  | LVDS0_TX3_P           |                            | J20-28 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-9  | GND                   | digital ground             | J20-29 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-10 | LVDS0_TX2_P           | LVDS0 differential data 2  | J20-30 |             |                |
+--------+-----------------------+                            +--------+-------------+----------------+
| J20-11 | LVDS0_TX2_N           |                            | J20-31 | NC          | dangling       |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-12 | GND                   | digital ground             | J20-32 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-13 | LVDS0_CLK_N           | LVDS0 differential clock   | J20-33 |             |                |
+--------+-----------------------+                            +--------+             +                +
| J20-14 | LVDS0_CLK_P           |                            | J20-34 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-15 | GND                   | digital ground             | J20-35 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-16 | SD1_DAT1/TOUCH_nEINT1 | GPIO control               | J20-36 |             |                |
+--------+-----------------------+                            +--------+             +                +
| J20-17 | NANDF_CS3             |                            | J20-37 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-18 | GND                   | digital ground             | J20-38 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-19 | DISP0_CONTRAST        | LVDS0 backlight adjustment | J20-39 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J20-20 | GND                   | digital ground             | J20-40 |             |                |
+--------+-----------------------+----------------------------+--------+-------------+----------------+

18/24bit LVDS1
~~~~~~~~~~~~~~~

|   Silk screen：J22
|   LVDS1 crystal liquid interface is the same as LVDS0 in terms of definition and connector model，users can connect crytal liquid in LVDS0 directly to LVDS1.
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.8.0.1.png
   :alt: My-imx6-mb314-2.8.0.1.png

+--------+-----------------------+----------------------------+--------+-------------+----------------+
| Pin    | Signal                | Description                | Pin    | Signal      | Description    |
+--------+-----------------------+----------------------------+--------+-------------+----------------+
| J22-1  | LVDS1_TX1_N           | LVDS1 differential data 1  | J22-21 | TOUCH_SCL   | I2C clock      |
+--------+-----------------------+                            +--------+-------------+----------------+
| J22-2  | LVDS1_TX1_P           |                            | J22-22 | TOUCH_SDA   | I2C data       |
+--------+-----------------------+----------------------------+--------+-------------+----------------+
| J22-3  | GND                   | digital ground             | J22-23 | GND         | digital ground |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-4  | LVDS1_TX1_P           | LVDS1 differential data 1  | J22-24 |             |                |
+--------+-----------------------+                            +--------+             +                +
| J22-5  | LVDS1_TX1_N           |                            | J22-25 |             |                |
+--------+-----------------------+----------------------------+--------+-------------+----------------+
| J22-6  | GND                   | digital ground             | J22-26 | 5VIN        | 5V input       |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-7  | LVDS1_TX3_N           | LVDS1 differential data 3  | J22-27 |             |                |
+--------+-----------------------+                            +--------+             +                +
| J22-8  | LVDS1_TX3_P           |                            | J22-28 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-9  | GND                   | digital ground             | J22-29 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-10 | LVDS1_TX2_P           | LVDS1 differential data 2  | J22-30 |             |                |
+--------+-----------------------+                            +--------+-------------+----------------+
| J22-11 | LVDS1_TX2_N           |                            | J22-31 | NC          | dangling       |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-12 | GND                   | digital ground             | J22-32 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-13 | LVDS1_CLK_N           | LVDS1 difference clock     | J22-33 |             |                |
+--------+-----------------------+                            +--------+             +                +
| J22-14 | LVDS1_CLK_P           |                            | J22-34 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-15 | GND                   | digital ground             | J22-35 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-16 | SD1_DAT1/TOUCH_nEINT1 | GPIO control               | J22-36 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-17 | NANDF_CS3             | GPIO control               | J22-37 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-18 | GND                   | digital ground             | J22-38 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-19 | DISP1_CONTRAST        | LVDS1 backlight adjustment | J22-39 |             |                |
+--------+-----------------------+----------------------------+--------+             +                +
| J22-20 | GND                   | digital ground             | J22-40 |             |                |
+--------+-----------------------+----------------------------+--------+-------------+----------------+

18/24bit LVDS1 expansion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   slik screen ：J24
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.9.0.1.png
   :alt: 963px-My-imx6-mb314-2.9.0.1.png

+--------+-------------+---------------------------+--------+--------------+---------------------------+
| Pin    | Signal      | Description               | Pin    | Signal       | Description               |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-1  | 5VIN        | 5V input                  | J24-2  | 5VIN         | 5V input                  |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-3  | GND         | digital ground            | J24-4  | TOUCH_SDA    | I2C3 data                 |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-5  | TOUCH_SCL   | I2C3 clock                | J24-6  | DISP0_CNTRST | backlight enabling        |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-7  | GPIO6_7     | GPIO                      | J24-8  | GPIO2_1      | GPIO                      |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-9  | LVDS1_TX1_N | LVDS1 differential data1  | J24-10 | LVDS1_TX1_P  | LVDS1 differential data1  |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-11 | LVDS1_TX0_P | LVDS1 differential data 0 | J24-12 | LVDS1_TX0_N  | LVDS1 differential data 0 |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-13 | LVDS1_TX3_N | LVDS1 differential data 3 | J24-14 | LVDS1_TX3_P  | LVDS1 differential data 3 |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-15 | LVDS1_TX2_P | LVDS1 differential data 2 | J24-16 | LVDS1_TX2_N  | LVDS1 differential data 2 |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-17 | LVDS1_CLK_N | LVDS1 differential clock  | J24-18 | LVDS1_CLK_P  | LVDS1 differential clock  |
+--------+-------------+---------------------------+--------+--------------+---------------------------+
| J24-19 | GND         | digital ground            | J24-20 | GND          | digital ground            |
+--------+-------------+---------------------------+--------+--------------+---------------------------+


I2C expansion
~~~~~~~~~~~~~~~

|   Silk screen：J23
|   Definition of pin & signal as below：


.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.10.0.1.png
   :alt: 963px-My-imx6-mb314-2.10.0.1.png


+--------+---------------+----------------+--------+-----------+-------------+
| Pin    | Signal        | Description    | Pin    | Signal    | Description |
+--------+---------------+----------------+--------+-----------+-------------+
| J23-1  | GND           | digital ground | J23-2  | 5VIN      | 5V input    |
+--------+---------------+----------------+--------+-----------+-------------+
| J23-3  | GND           | digital ground | J23-4  | GEN_3V3   | 3.3V input  |
+--------+---------------+----------------+--------+-----------+-------------+
| J23-5  | I2C1_SCL      | I2C1 clock     | J23-6  | I2C1_SDA  | I2C1 data   |
+--------+---------------+----------------+--------+-----------+-------------+
| J23-7  | I2C2_SCL      | I2C2 clock     | J23-8  | I2C2_SDA  | I2C2 data   |
+--------+---------------+----------------+--------+-----------+-------------+
| J23-9  | I2C3_SCL      | I2C3 clock     | J23-10 | I2C3_SDA  | I2C3 data   |
+--------+---------------+----------------+--------+-----------+-------------+
| J23-11 | USB_H1_PWR_EN | GPIO           | J23-12 | USB_H1_OC | GPIO        |
+--------+---------------+----------------+--------+-----------+-------------+


Debug serial port
~~~~~~~~~~~~~~~~~~~

|   Silk screen：P3
|   Interface property：UART0，232电平，调试串口
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.11.0.1.png
   :alt: 963px-My-imx6-mb314-2.11.0.1.png

Headphone output
~~~~~~~~~~~~~~~~~~

|   Silk screen：J16
|   Interface property：audio signal output, 3.5mm interface
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.12.0.1.png
   :alt: 963px-My-imx6-mb314-2.12.0.1.png

MIC input
~~~~~~~~~~~

|   Silk screen：J14
|   Interface property：audio signal input, 3.5mm interface
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.13.0.1.png
   :alt: 963px-My-imx6-mb314-2.13.0.1.png

Serial port extension/TTL electrical level
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Silk screen：J12
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.14.0.1.png
   :alt: 963px-My-imx6-mb314-2.14.0.1.png

+--------+-----------+-------------------------+--------+-----------+-------------------------+
| Pin    | Signal    | Description             | Pin    | Signal    | Description             |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-1  | 5VIN      | 5V input                | J12-2  | 5VIN      | 5V input                |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-3  | GND       | digital ground          | J12-4  | GND       | digital ground          |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-5  | GEN_3V3   | 3.3v input              | J12-6  | GEN_3V3   | 3.3v input              |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-7  | UART2_CTS | serial port 2 CTS       | J12-8  | UART2_RTS | serial port 2 RTS       |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-9  | UART2_RXD | serial port 2 receiving | J12-10 | UART2_TXD | serial port 2 sending   |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-11 | UART3_RTS | serial port 3 RTS       | J12-12 | UART3_RXD | serial port 3 receiving |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-13 | UART3_TXD | serial port 3 sending   | J12-14 | UART3_CTS | serial port 3 sending   |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-15 | UART4_TXD | serial port 4 sending   | J12-16 | UART5_RXD | serial port 5 receiving |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-17 | UART4_RXD | serial port 4 receiving | J12-18 | UART5_TXD | serial port 5 sending   |
+--------+-----------+-------------------------+--------+-----------+-------------------------+
| J12-19 | GND       | digital ground          | J12-20 | GND       | digital ground          |
+--------+-----------+-------------------------+--------+-----------+-------------------------+

232 serial port
~~~~~~~~~~~~~~~~~

|   Silk screen：P2
|   Interface property：UART4, RS-232, application serial port
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.15.0.1.png
   :alt: 963px-My-imx6-mb314-2.15.0.1.png

485 serial port
~~~~~~~~~~~~~~~~~

|   Silk screen：J11
|   Interface property：UART3, RS-485, application serial port
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.16.0.1.png
   :alt: 963px-My-imx6-mb314-2.16.0.1.png

RGMII
~~~~~~~

|   Silk screen：U12
|   Interface property：GigE Vision
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.17.0.1.png
   :alt: My-imx6-mb314-2.17.0.1.png

SATA II
~~~~~~~~~

|   Silk screen：J9
|   interface property: 3Gbps SATA I interface
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.18.0.1.png
   :alt: 963px-My-imx6-mb314-2.18.0.1.png

SATA power supply
~~~~~~~~~~~~~~~~~~~

|   Silk screen：J10
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.19.0.1.png
   :alt: My-imx6-mb314-2.19.0.1.png

+-------+--------+----------------+
| pin   | signal | description    |
+-------+--------+----------------+
| J10-1 | 5VIN   | 5V power input |
+-------+--------+----------------+
| J10-2 | GND    | digital ground |
+-------+--------+----------------+
| J10-3 | GND    | digital ground |
+-------+--------+----------------+
| J10-4 | NC     | unconnected    |
+-------+--------+----------------+

MIPI-CSI
~~~~~~~~~~

|   Silk screen：J7
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.20.0.1.png
   :alt: My-imx6-mb314-2.20.0.1.png

+-------+-----------+-------------------------+-------+-----------+-------------------------+
| pin   | signal    | description             | pin   | signal    | description             |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-1  | 5VIN      | 5V input                | J7-2  | 5VIN      | 5V input                |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-3  | 5VIN      | 5V input                | J7-4  | GND       | digital ground          |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-5  | CSI_CLK0P | CSI differential clock  | J7-6  | CSI_CLK0M | CSI differential clock  |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-7  | GND       | digital ground          | J7-8  | CSI_D0P   | CSI differential data 0 |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-9  | CSI_D0M   | CSI differential data 0 | J7-10 | GND       | digital ground          |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-11 | CSI_D1P   | CSI differential data 1 | J7-12 | CSI_D1M   | CSI differential data 1 |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-13 | GND       | digital ground          | J7-14 | CSI_MCLK  | CSI master clock        |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-15 | GND       | digital ground          | J7-16 | GND       | digital ground          |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-17 | CSI2-SDA  | I2C2 data               | J7-18 | CSI2_SCL  | I2C2 clock              |
+-------+-----------+-------------------------+-------+-----------+-------------------------+
| J7-19 | GPIO7_12  | GPIO                    | J7-20 | GPIO7_13  | GPIO                    |
+-------+-----------+-------------------------+-------+-----------+-------------------------+

OTG
~~~~~

|   Silk screen：J5
|   Interface property：USB ON-The-Go, use for burning
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.21.0.1.png
   :alt: 963px-My-imx6-mb314-2.21.0.1.png

RMII
~~~~~~

|   Silk screen：P1
|   Interface property：USB1 extended gigabit Ethernet
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.22.0.1.png
   :alt: 963px-My-imx6-mb314-2.22.0.1.png

USB expansion
~~~~~~~~~~~~~~~

|   Silk screen：J2
|   Interface property：USB1 expansion, double USB
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.23.0.1.png
   :alt: 963px-My-imx6-mb314-2.23.0.1.png

RTC
~~~~~

|   Silk screen：U8
|   Interface property：I2C通信的实时时钟
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.24.0.1.png
   :alt: 963px-My-imx6-mb314-2.24.0.1.png

MIPI-DSI
~~~~~~~~~

|   Silk screen：U1
|   Preselection screen type：N070ICN-GB1
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.25.0.1.png
   :alt: My-imx6-mb314-2.25.0.1.png

+-------+-----------+-------------------------+-------+--------+---------------------------------+
| pin   | signal    | description             | pin   | signal | description                     |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-1  | GND1      | digital ground          | U1-17 | LEDPWM | unconnected                     |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-2  | GND2      | digital ground          | U1-18 | CLK_P  | DSI differential clock          |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-3  | GND3      | digital ground          | U1-19 | VLED1  | 9V backlight power supply input |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-4  | D0_N      | DSI differential data 0 | U1-20 | GND6   | digital ground                  |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-5  | RST       | reset                   | U1-21 | VLED2  | 9V backlight power supply input |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-6  | D0_P      | DSI differential data 0 | U1-22 | D2_N   | unconnected                     |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-7  | VCI1_3V3  | 3.3V input              | U1-23 | ID     | earthing                        |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-8  | GND4      | digital ground          | U1-24 | D2_P   | unconnected                     |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-9  | VCI2_3V3  | 3.3V input              | U1-25 | LED1   | earthing                        |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-10 | D1_N      | DSI differential data 1 | U1-26 | GND7   | digital ground                  |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-11 | MTP       | unconnected             | U1-27 | LED2   | unconnected                     |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-12 | D1_P      | DSI differential data 1 | U1-28 | D3_N   | unconnected                     |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-13 | VDDI2_1V8 | 1.8V input              | U1-29 | GND8   | digital ground                  |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-14 | GND5      | digital ground          | U1-30 | D3_P   | unconnected                     |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-15 | VDDI2_1V8 | 1.8V input              | U1-31 | GND9   | digital ground                  |
+-------+-----------+-------------------------+-------+--------+---------------------------------+
| U1-16 | CLK_N     | DSI differential clock  |       |        |                                 |
+-------+-----------+-------------------------+-------+--------+---------------------------------+

DSI backlight power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Silk screen：J1
|   Interface property：9V power supply input
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.26.0.1.png
   :alt: 963px-My-imx6-mb314-2.26.0.1.png

MPS main power switch
~~~~~~~~~~~~~~~~~~~~~~~~

|   Silk screen：J3
|   Interface property：power switch

main power input
~~~~~~~~~~~~~~~~~~

|   Silk screen：J4
|   Interface property：

 |  jack with inside positive and outside negative
 |  power supply：5V
 |  current：2.5A or above

|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.28.0.1.png
   :alt: 963px-My-imx6-mb314-2.28.0.1.png

HDMI
~~~~~~

|   Silk screen：J6
|   Interface property：HDMI-1.4
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.29.0.1.png
   :alt: My-imx6-mb314-2.29.0.1.png

3G mini-PCIE & SIM cassette
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+-------------+---------------------------------+
| Name         | Silk screen | Interface property              |
+--------------+-------------+---------------------------------+
| 3G mini-PCIE | J8          | miniPCIE standard interface     |
+--------------+-------------+---------------------------------+
| SIM cassette | CON1        | Interface property: 3G SIM card |
+--------------+-------------+---------------------------------+


|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.30.0.1.png
   :alt: 963px-My-imx6-mb314-2.30.0.1.png

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.30.0.2.png
   :alt: 963px-My-imx6-mb314-2.30.0.2.png

JTAG
~~~~~~

|   Silk screen：U11
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.31.0.1.png
   :alt: 963px-My-imx6-mb314-2.31.0.1.png

+-------+----------+---------------------+--------+--------+----------------+
| pin   | signal   | description         | pin    | signal | description    |
+-------+----------+---------------------+--------+--------+----------------+
| U11-1 | JTAG_TCK | TCK input           | U11-2  | GND    | digital ground |
+-------+----------+---------------------+--------+--------+----------------+
| U11-3 | JTAG_TDO | test data output    | U11-4  | VCC    | 3.3V input     |
+-------+----------+---------------------+--------+--------+----------------+
| U11-5 | JTAG_TMS | test mode selection | U11-6  | nRST   | reset          |
+-------+----------+---------------------+--------+--------+----------------+
| U11-7 | NC       | unconnected         | U11-8  | NC     | unconnected    |
+-------+----------+---------------------+--------+--------+----------------+
| U11-9 | JTAG_TDI | test mode selection | U11-10 | GND    | digital ground |
+-------+----------+---------------------+--------+--------+----------------+


GPIO expansion
~~~~~~~~~~~~~~~~~

|   Silk screen：U14
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.32.0.1.png
   :alt: 963px-My-imx6-mb314-2.32.0.1.png

+--------+------------+----------------------+--------+----------------+----------------------+
| pin    | signal     | description          | pin    | signal         | description          |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-1  | 5VIN       | 5V input             | U14-2  | GEN_3V3        | 3.3V input           |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-3  | SD3_DATA4  | configurable as GPIO | U14-4  | SD3_DATA5      | configurable as GPIO |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-5  | SD3_DATA7  | configurable as GPIO | U14-6  | SD3_DATA6      | configurable as GPIO |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-7  | GPIO6_16   | GPIO                 | U14-8  | GPIO2_7        | GPIO                 |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-9  | GPIO2_3    | GPIO                 | U14-10 | GPIO2_6        | GPIO                 |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-11 | GPIO6_9    | GPIO                 | U14-12 | GPIO6_11       | GPIO                 |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-13 | GPIO2_2    | GPIO                 | U14-14 | GPIO2_0        | GPIO                 |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-15 | GPIO2_4    | GPIO                 | U14-16 | GPIO2_5        | GPIO                 |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-17 | GPIO1_29   | GPIO                 | U14-18 | GPIO1_27       | GPIO                 |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-19 | GPIO1_30   | GPIO                 | U14-20 | GPIO1_26       | GPIO                 |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-21 | GPIO1_24   | GPIO                 | U14-22 | GND            | digital ground       |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-23 | SD2_CLK    | SD2 clock            | U14-24 | SD2_DATA0      | SD2 data wire        |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-25 | SD2_DATA3  | SD2 data wire        | U14-26 | SD2_DATA2      | SD2 data wire        |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-27 | SD2_CMD    | SD2 command pin      | U14-28 | SD2_DATA1      | SD2 data wire        |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-29 | USB_OTG_OC | configurable as GPIO | U14-30 | USB_OTG_PWR_EN | configurable as GPIO |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-31 | GND        | digital ground       | U14-32 | GND            | digital ground       |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-33 | SD1_CMD    | SD1 command pin      | U14-34 | SD1_DAT0       | SD1 data wire        |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-35 | SD1_CLK    | SD1 clock            | U14-36 | SD1_DAT1       | SD1 data wire        |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-37 | SD1_DAT3   | SD1 data wire        | U14-38 | SD1_DAT2       | SD1 data wire        |
+--------+------------+----------------------+--------+----------------+----------------------+
| U14-39 | GND        | digital ground       | U14-40 | GND            | digital ground       |
+--------+------------+----------------------+--------+----------------+----------------------+


SPI expansion
~~~~~~~~~~~~~~

|   Silk screen：J13
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.33.0.1.png
   :alt: 963px-My-imx6-mb314-2.33.0.1.png

+--------+------------+------------------------+--------+------------+-------------------------+
| pin    | signal     | description            | pin    | signal     | description             |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-1  | 5VIN       | 5V input               | J13-2  | 5VIN       | 5V input                |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-3  | 5VIN       | 5V input               | J13-4  | GEN_3V3    | 3.3V input              |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-5  | CSPI2_RDY  | SPI2 data-ready signal | J13-6  | CSPI1_MISO | SPI1 Master data input  |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-7  | CSPI2_MISO | Reuse the EIM OE       | J13-8  | CSPI1_RDY  | SPI1 data-ready signal  |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-9  | CSPI2_CLK  | Reuse the EIM_CS0      | J13-10 | CSPI1_CLK  | SPI1 clock              |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-11 | CSPI2_MOSI | Reuse the EIM_CS1      | J13-12 | CSPI1_MOSI | SPI1 Master data output |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-13 | CSPI2_CSI  | Reuse the EIM_LBA      | J13-14 | CSPI1_CS1  | selective signal        |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-15 | CSPI2_CS0  | Reuse the EIM_RW       | J13-16 | GND        | digital ground          |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-17 | GND        | digital ground         | J13-18 | GND        | digital ground          |
+--------+------------+------------------------+--------+------------+-------------------------+
| J13-19 | GND        | digital ground         | J13-20 | GND        | digital ground          |
+--------+------------+------------------------+--------+------------+-------------------------+

CAN1
~~~~~~~

|   Silk screen：J17
|   Interface property：CAN1
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.34.0.1.png
   :alt: 963px-My-imx6-mb314-2.34.0.1.png

CAN2
~~~~~~~

|   Silk screen：J15
|   Interface property：CAN2
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.35.0.1.png
   :alt: 963px-My-imx6-mb314-2.35.0.1.png

CSI(CMOS Sensor Interface)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Silk screen：J19
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.36.0.1.png
   :alt: 963px-My-imx6-mb314-2.36.0.1.png

+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| pin    | signal      | description                     | pin    | signal       | description                    |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-1  | 5VIN        | 5V input                        | J19-2  | GND          | digital ground                 |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-3  | CSI0_SCL    | I2C1 clock                      | J19-4  | CSI0_SDA     | I2C1 data                      |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-5  | CSI0_VSYNCH | field synchronization interface | J19-6  | CSI0_HSYNCH  | Line synchronization interface |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-7  | CDI0_PIXCLK | camera output master clock      | J19-8  | CSI0_MCLK    | CSI output master clock        |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-9  | CSI0_DAT19  | CSI data bus                    | J19-10 | CSI0_DAT18   | CSI data bus                   |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-11 | CSI0_DAT17  | CSI data bus                    | J19-12 | CSI0_DAT16   | CSI data bus                   |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-13 | CSI0_DAT15  | CSI data bus                    | J19-14 | CSI0_DAT14   | CSI data bus                   |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-15 | CSI0_DAT13  | CSI data bus                    | J19-16 | CSI0_DAT12   | CSI data bus                   |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-17 | GND         | digital ground                  | J19-18 | CSI0_DATA_EN | bus enable                     |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+
| J19-19 | NC          | unconnected                     | J19-20 | NC           | unconnected                    |
+--------+-------------+---------------------------------+--------+--------------+--------------------------------+

SD cassette
~~~~~~~~~~~~~

|   Silk screen：J25
|   Interface property: standard SD cassette
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.37.0.1.png
   :alt: 963px-My-imx6-mb314-2.37.0.1.png

PCIT expansion
~~~~~~~~~~~~~~~~~

|   Silk screen：J26
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.38.0.1.png
   :alt: My-imx6-mb314-2.38.0.1.png

+--------+----------+-------------------------------+--------+---------------+----------------+
| pin    | signal   | description                   | pin    | signal        | description    |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-1  | PCIE_RXP | receiving differential signal | J26-13 | GPIO6_8       | GPIO           |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-2  | PCIE_RXM | receiving differential signal | J26-14 | GPIO6_14      | GPIO           |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-3  | GND      | digital ground                | J26-15 | PCIE_SMD_CLK  | I2C3 clock     |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-4  | PCIE_TXP | sending differential signal   | J26-16 | PCIE_SMB_DATA | I2C3 data      |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-5  | PCIE_TXM | sending differential signal   | J26-17 | GPIO7_11      | GPIO           |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-6  | GND      | digital ground                | J26-18 | GND           | digital ground |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-7  | CLK1_P   | differential clock            | J26-19 | GND           | digital ground |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-8  | CLK1_N   | differential clock            | J26-20 | GND           | digital ground |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-9  | GND      | digital ground                | J26-21 | 5VIN          | 5V input       |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-10 | 3G_USBDM | USB differential signal       | J26-22 | 5VIN          | 5V input       |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-11 | 3G_USBDP | USB differential signal       | J26-23 | 5VIN          | 5V input       |
+--------+----------+-------------------------------+--------+---------------+----------------+
| J26-12 | GND      | digital ground                | J26-24 | 5VIN          | 5V input       |
+--------+----------+-------------------------------+--------+---------------+----------------+

WIFI module
~~~~~~~~~~~~~

|   Silk screen：U24
|   Module model：UM12BS
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.39.0.1.png
   :alt: 963px-My-imx6-mb314-2.39.0.1.png

GPS module
~~~~~~~~~~~~~

|   Silk screen：U27
|   Interface property: standard IPX interface
|   Module model：NEO-6M
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6-mb314-2.40.0.1.png
   :alt: 963px-My-imx6-mb314-2.40.0.1.png

EIM expansion
~~~~~~~~~~~~~~~

|   Silk screen：J27
|   Definition of pin & signal as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/My-imx6-mb314-2.41.0.1.png
   :alt: My-imx6-mb314-2.41.0.1.png

+--------+----------+----------------+--------+----------+----------------+
| pin    | signal   | description    | pin    | signal   | description    |
+--------+----------+----------------+--------+----------+----------------+
| J27-1  | GND      | digital ground | J27-17 | EIM_DA7  | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-2  | GND      | digital ground | J27-18 | EIM_DA8  | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-3  | GND      | digital ground | J27-19 | EIM_DA3  | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-4  | GND      | digital ground | J27-20 | EIM_DA6  | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-5  | EIM_DA15 | address & data | J27-21 | EIM_DA1  | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-6  | EIM_WAIT |                | J27-22 | EIM_DA11 | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-7  | EIM_RW   |                | J27-23 | EIM_OE   |                |
+--------+----------+----------------+--------+----------+----------------+
| J27-8  | EIM_DA2  | address & data | J27-24 | EIM_DA14 | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-9  | EIM_DA10 | address & data | J27-25 | EIM_DA13 | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-10 | EIM_EB0  |                | J27-26 | EIM_BCLK | output clock   |
+--------+----------+----------------+--------+----------+----------------+
| J27-11 | EIM_DA4  | address & data | J27-27 | EIM_DA5  | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-12 | EIM_EB1  |                | J27-28 | EIM_DA9  | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-13 | EIM_LBA  |                | J27-29 | EIM_DA0  | address & data |
+--------+----------+----------------+--------+----------+----------------+
| J27-14 | EIM_CS1  | chip select 1  | J27-30 | 5VIN     | 5V input       |
+--------+----------+----------------+--------+----------+----------------+
| J27-15 | EIM_CS0  | chip select 1  | J27-31 | 5VIN     | 5V input       |
+--------+----------+----------------+--------+----------+----------------+
| J27-16 | EIM_DA12 | address & data | J27-32 | 5VIN     | 5V input       |
+--------+----------+----------------+--------+----------+----------------+
