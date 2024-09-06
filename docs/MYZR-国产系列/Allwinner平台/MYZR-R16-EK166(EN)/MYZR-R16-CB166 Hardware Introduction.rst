
MYZR-R16-CB166 Hardware Introduction
======================================

MYZR-R16-CB166 Introduction
-----------------------------

MYZR-R16-CB166 is an embedded core control module developed by our company based on the design of full log R16 application processor.The core plate is connected with a stamp hole.

MYZR-R16-CB166 View
~~~~~~~~~~~~~~~~~~~~~

**Front view**

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/540px-MY-R16-CB166_1.png
   :alt: 540px-MY-R16-CB166_1.png

**Rear view**

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/540px-MY-R16-CB166_2.png
   :alt: 540px-MY-R16-CB166_2.png


MYZR-R16-CB166 Size
~~~~~~~~~~~~~~~~~~~~~

|  42.4mm * 45.4mm

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/840px-MY-R16-CB166_3.png
   :alt: 840px-MY-R16-CB166_3.png


R16 processor introduction
----------------------------

Block diagram and basic specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Block diagram**

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/840px-MY-R16-CB166_4.png
   :alt: 840px-MY-R16-CB166_4.png


Introduction
~~~~~~~~~~~~~~~

|  MYZR-R16-EK166 is a low-power, high-performance and scalable application development board that we are fully committed to. It is highly competitive in terms of flexibility, system performance and energy efficiency.
|  MYZR-R16-CB166 adopted the most cost-effective quad-core processor CortexTM - A7 architecture, Mali carrying 400 MP2 graphics processing unit, a support 1080 p hd video processing and playback, the largest support 1280 x 800 resolution screen, support 5 million megapixel camera, support the USB2.0 interface.Beautiful color display system, excellent display effect.

Features
~~~~~~~~~~

- Quad-core Cortex?-A7，main frequency 1.2 GHZ
- 256KB L1 Cache,512KB L2 Cache
- 16-bit DDR3/DDR3L ,Up to 2GB
- Supports 8-bit NAND Flash controller
- LVDS，maximum resolution 1280x800
- 8/10/16/24bit parallel camera sensor interface
- one 10/100 Ethernet，Support IEEE 1588 protocol
- Support 1080p@60fps video playback
- Switchable headset mode / phone mode

MYZR-R16-CB166 introduction
-----------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~

+---------+----------------+-----------------------+
| CPU     | R16            | Commercial grade      |
+---------+----------------+-----------------------+
| Memory  | DDR3/DDR3L 1GB | Can Expandable to 2GB |
+---------+----------------+-----------------------+
| Storage | 8GB eMMC       | Compatible to 64GB    |
+---------+----------------+-----------------------+


Power supply
~~~~~~~~~~~~~~

   |  5V输入

Temperature range
~~~~~~~~~~~~~~~~~~~~

- working temperature

   |  0°C ~ 70°C

- Storage temperature

   |  -60°C ~ 125°C

Operating system support
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Linux**

   |  Linux-3.4.39

- **Android**

   |  Android 4.4（Use the Linux-3.4.39 kernel）


Hardware default interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------+-----------------+-------+-----------------------------+
| Display module | LVDS            | 2 way | 8bit mode                   |
+----------------+-----------------+-------+-----------------------------+
| Camera         | CSI             | 1 way | 8bit mode                   |
+----------------+-----------------+-------+-----------------------------+
| Ethernet       | USB to Ethernet | 1 way | 100M                        |
+----------------+-----------------+-------+-----------------------------+
| Audio          | Audio           | 1way  | ADC/DAC，HI-FI              |
+----------------+-----------------+-------+-----------------------------+
| PCI Express    | PCI Express     | 1way  | Gen 2.0                     |
+----------------+-----------------+-------+-----------------------------+
| storage        | SD/MMC Card     | 3way  | 1/4bit                      |
+----------------+-----------------+-------+-----------------------------+
| USB            | USBOTG          | 1way  | 480M high speed             |
+                +-----------------+-------+-----------------------------+
|                | USBHOST         | 2way  | 480M high speed             |
+----------------+-----------------+-------+-----------------------------+
| UART           | UART            | 6way  | up to 4.0 Mbps              |
+----------------+-----------------+-------+-----------------------------+
| PWM            | PWM             | 2way  | Optional configuration 4way |
+----------------+-----------------+-------+-----------------------------+


Pin definition
~~~~~~~~~~~~~~~

.. include:: MYZR-R16-CB166 Pin definition.rst