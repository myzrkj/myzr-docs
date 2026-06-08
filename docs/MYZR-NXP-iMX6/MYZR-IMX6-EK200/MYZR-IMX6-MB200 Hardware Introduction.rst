
MYZR-IMX6-MB200 Hardware Introduction
========================================

overview of interfaces
-------------------------

Front view
~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6ek200_front_.jpg
   :alt: Myimx6ek200_front_.jpg

Rear view
~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/963px-Myimx6ek200_rear_view.jpg
   :alt: 963px-Myimx6ek200_rear_view.jpg

size view
~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/971px-Myimx6ek200_dimension_.jpg
   :alt: 971px-Myimx6ek200_dimension_.jpg

Interface function
---------------------

18/24bit LVDS0
~~~~~~~~~~~~~~~~

|  Silk screen：J24
|  LVDS0 crystal liquid is 24 bit mode，compatible with 18bit mode，through which LVDS resistance screen panel and LVDS capacitor screen panel in different sizes and specifications produced by MYZR can be cnnected。LVDS0 interface block is build with connector imported，abandon the cheap drawer type produced domestically，which is opposite press type to ensure easier installation,better performance and connectivity.
|  Definition of pin & signal as below

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.1.0.1.png
   :alt: Myimx6_mb200_2.1.0.1.png

+--------+-----------------------+----------------------------+
| Pin    | Singnal               | Description                |
+========+=======================+============================+
| J24-16 | SD1_DAT1/TOUCH_nEINT1 | GPIO control               |
+--------+-----------------------+----------------------------+
| J24-17 | NANDF_CS3             | GPIO control               |
+--------+-----------------------+----------------------------+
| J24-19 | DISP0_CONTRAST        | LVDS0 backlight adjustment |
+--------+-----------------------+----------------------------+
| J24-21 | TOUCH_SCL             | I2C clock                  |
+--------+-----------------------+----------------------------+
| J24-22 | TOUCH_SDA             | I2C data                   |
+--------+-----------------------+----------------------------+


18/24bit RGB
~~~~~~~~~~~~~~

|  Silkscreen:J23
|  RGB crystal liquid is 24bit mode，compatible to 18bit/16bit mode,through which RGB resistance screen panel and RGB capacitor screen panel in different sizes and specifications produced by MYZR can be cnnected，RGB interface block is build with connector imported，abandon the cheap drawer type produced domestically，which is opposite press type to ensure easier installation,better performance and connectivity。</span>
|  Definition of pin & signal：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.2.0.1.png
   :alt: Myimx6_mb200_2.2.0.1.png

+--------+-----------------------+----------------------------+
|  Pin   |        Singnal        |        Description         |
+========+=======================+============================+
| J23-31 | SD1_DAT1/TOUCH_nEINT1 | GPIO control               |
+--------+-----------------------+----------------------------+
| J23-30 | NANDF_CS3             | GPIO control               |
+--------+-----------------------+----------------------------+
| J23-19 | DISP0_CONTRAST        | LVDS0 backlight adjustment |
+--------+-----------------------+----------------------------+
| J23-32 | TOUCH_SCL             | I2C clock                  |
+--------+-----------------------+----------------------------+
| J23-33 | TOUCH_SDA             | I2C data                   |
+--------+-----------------------+----------------------------+


18/24bit LVDS1
~~~~~~~~~~~~~~~~

|  Silk screen：J22
|  LVDS1 crystal liquid interface is the same as LVDS0 in terms of definition and connector model，users can connect crytal liquid in LVDS0 directly to LVDS1.
|  Definition of pin & signal：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.3.0.1.png
   :alt: Myimx6_mb200_2.3.0.1.png

+--------+-----------------------+----------------------------+
| Pin    | Singnal               | Description                |
+========+=======================+============================+
| J22-16 | SD1_DAT1/TOUCH_nEINT1 | GPIO control               |
+--------+-----------------------+----------------------------+
| J22-17 | NANDF_CS3             | GPIO control               |
+--------+-----------------------+----------------------------+
| J22-19 | DISP0_CONTRAST        | LVDS0 backlight adjustment |
+--------+-----------------------+----------------------------+
| J22-21 | TOUCH_SCL             | I2C clock                  |
+--------+-----------------------+----------------------------+
| J22-22 | TOUCH_SDA             | I2C data                   |
+--------+-----------------------+----------------------------+

10M/100M Ethernet-1
~~~~~~~~~~~~~~~~~~~~~

|  Silk screen：P4
|  Interface property：100 - Mbps Ethernet standard interface

Earphone output
~~~~~~~~~~~~~~~~~

|  Silk screen：J20
|  Interface property：audio signal output，3.5mm interface

Microphone input
~~~~~~~~~~~~~~~~~~~

|  Silk screen：J18
|  Interface propoerty：audio signal input，3.5mm interface

HDMI
~~~~~~

|  Silk screen：J5
|  Interface property：HDMI-1.4 standard interface

SATA power supply
~~~~~~~~~~~~~~~~~~~

|  silk screen：J12
|  Definition of pin & signal：

+-------+--------+----------------+
|  pin  | signal |  description   |
+=======+========+================+
| J12-1 | 5VIN   | 5V power input |
+-------+--------+----------------+
| J12-2 | GND    | digital        |
+-------+--------+----------------+
| J12-3 | GND    | digital        |
+-------+--------+----------------+
| J12-4 | NC     | unconnected    |
+-------+--------+----------------+

OTG
~~~~~

|  silk screen：J5
|  Interface property：USB ON-The-GO，for burn and write

SATA II
~~~~~~~~~

|  Silk screen：J11
|  Interface property：3Gbps SATA II standard interface

10M/100M Ethernet-2
~~~~~~~~~~~~~~~~~~~~~

|  Silk screen：P3
|  Interface property：100 - Mbps Ethernet standard interface

USB扩展
~~~~~~~~

|  silk screen:J8
|  Interface property：USB1 expanded to dual USB，standard USB interface

Debug uart
~~~~~~~~~~~~

|  Silk screen：P2
|  Interface property：3 thread standard RS232 port，for debug of sirial port

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.13.0.1.png
   :alt: Myimx6_mb200_2.13.0.1.png

Main power supply switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Silk screen：J3
|  Interface property：power supply switch
|  Status property：—，close；O，off

Main power input
~~~~~~~~~~~~~~~~~~

|  Silk screen：J4
|  Interface property：

 | Jack with inside positive and outside negative
 | Voltage：5V
 | Current：2.5A and above

Reset
~~~~~~~

|  Silk screen：SW1
|  Function：reset

Wake up
~~~~~~~~

|  Silk screen：SW2
|  Interface property：sleeping wake up

Volume up
~~~~~~~~~~~

|  Silk screen：SW3
|  Interface property：volume control（volume up）

Volume down
~~~~~~~~~~~~~

|  Silk screen：SW2
|  Interface property：volume control（volume down）

RS-232 serial port
~~~~~~~~~~~~~~~~~~~~

|  silk screen：P1
|  Interface property：UART4，3 thread standard RS232 port

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.20.0.1.png
   :alt: Myimx6_mb200_2.20.0.1.png

RS-485 serial port
~~~~~~~~~~~~~~~~~~~~~

|  Silk screen：J2
|  Interface property：UART3，RS-485 serial port

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.21.0.1.png
   :alt: Myimx6_mb200_2.21.0.1.png

MINI-PCIE
~~~~~~~~~~~

|  Silk screen：J6
|  Interface property：standard MINI-PCIE port

串口扩展/TTL电平
~~~~~~~~~~~~~~~~~

|  Silk screen：J1

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.23.0.1.png
   :alt: Myimx6_mb200_2.23.0.1.png

GPIO/SD2
~~~~~~~~~~

|  Silk screen：J4

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.24.0.1.png
   :alt: Myimx6_mb200_2.24.0.1.png

SPI expansion
~~~~~~~~~~~~~~~

|  Silk screen：J7

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.25.0.1.png
   :alt: Myimx6_mb200_2.25.0.1.png

SIM cassette
~~~~~~~~~~~~~~

|  Silk screen：CON1
|  Interface property：standard SIM cassette

MIPI-CSI
~~~~~~~~~

|  Silk screen:J9

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.27.0.1.png
   :alt: Myimx6_mb200_2.27.0.1.png

CMOS-CSI
~~~~~~~~~~

|  Silk screen:J14

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.28.0.1.png
   :alt: Myimx6_mb200_2.28.0.1.png

CAN2
~~~~~~

|  Silk screen:J16
|  Interface property：CAN2

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.29.0.1.png
   :alt: Myimx6_mb200_2.29.0.1.png

CAN1
~~~~~~

|  Silk screen:J19
|  Interface property：CAN1

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.30.0.1.png
   :alt: Myimx6_mb200_2.30.0.1.png

I2C expansion
~~~~~~~~~~~~~~~~

|  Silk screen:J21

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.31.0.1.png
   :alt: Myimx6_mb200_2.31.0.1.png

GPS antenna pedestal
~~~~~~~~~~~~~~~~~~~~~~~

|  Silk screen:E4
|  Interface property：antenna pedestal

GPS
~~~~~

|  Silk screen:U15
|  Module model：NEO-6M

MINI_PCIE_FPC
~~~~~~~~~~~~~~~

|  Silk screen:J26
|  Note：can't be used with MINI_PCIE simultaneously，e.g can only choose one from the two.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.34.0.1.png
   :alt: Myimx6_mb200_2.34.0.1.png

SD3
~~~~~

|  Silk screen:J25
|  Interface property：standard SD cassette

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.35.0.1.png
   :alt: Myimx6_mb200_2.35.0.1.png

WIFI
~~~~~~

|  Silk screen:U16
|  Module model：UM12BS

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Myimx6_mb200_2.36.0.1.png
   :alt: Myimx6_mb200_2.36.0.1.png

RTC
~~~~

|  Silk screen:U19
|  Interface property：real clock for I2C communication

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/963px-Myimx6_mb200_2.37.0.1.png
   :alt: 963px-Myimx6_mb200_2.37.0.1.png

RTC_Batter
~~~~~~~~~~~~

|  Silk screen:BT1
