Core Board Hardware Manual
=============================

Core Board View
-----------------

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-CB314.png
   :alt: image-MYZR-IMX8MP-CB314

Dimensions
------------

|  82mm*40mm

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-EK314/MYZR-IMX8MP-CB314-size.png
   :alt: image-MYZR-IMX8MP-CB314-size

Operating Temperature
-----------------------

- Commercial Grade:

   0°C ~ 70°C

- Industrial Grade:

   -40°C ~ 85°C

Power Supply
--------------

- 5V Input

Supported Operating Systems
------------------------------

- Linux
- Android

Hardware Interfaces
----------------------

+------------------------------+-------------------------+---------------+--------------------------------------------------------------------------------------+
|        Interface Type        | Interface Specification |  Max Cfg Qty  |                                     Description                                      |
+==============================+=========================+===============+======================================================================================+
| Communication Interfaces     | Ethernet                | 2             | 1 channel supports EEE, Ethernet AVB and IEEE1588                                    |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | USB3.0                  | 2             | 2 channels of USB3.0 PHY interfaces                                                  |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | UART                    | 4             | 4 channels of UART, each up to 4.0Mbps                                               |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | I2C                     | 6             | 4 channels of I2C, maximum support up to 400 kbps                                    |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | SPI                     | 3             | 3 channels of eCSPI (Enhanced CSPI), each up to 52Mbps                               |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | PCIe                    | 1             | Single-channel supports PCIe Gen 3, dual-mode operation, can be used as root complex |
+                              +                         +               +                                                                                      +
|                              |                         |               | or endpoint                                                                          |
+------------------------------+-------------------------+---------------+--------------------------------------------------------------------------------------+
| External Storage Interfaces  | eMMC                    | 2             | 5.1 FLASH                                                                            |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | NAND                    | 1             | 8-bit NAND flash, supports ECC and BCH for error detection                           |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | DRAM                    | 1             | 82-bit DRAM, supports raw MLC/SLC devices, BCH                                       |
+                              +                         +               +                                                                                      +
|                              |                         |               | ECC up to compliance with 62-bit and ONFi3.2 standards                               |
+                              +                         +---------------+--------------------------------------------------------------------------------------+
|                              |                         | 4             | 1 quad-channel external serial flash device interface, supports XIP mode             |
+------------------------------+-------------------------+---------------+--------------------------------------------------------------------------------------+
| Multimedia                   | HDMI                    | 1             | 1 channel of HDMI 2.0a, supports 4096x2160@60Hz, supports                            |
+                              +                         +               +                                                                                      +
|                              |                         |               | HDCP 2.2 and HDCP 1.4, 20+ audio interleaved 32-bit                                  |
+                              +                         +               +                                                                                      +
|                              |                         |               | @384khz fs, supports S/PDIF input and output                                         |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | DSI (MIPI Interface)    | 1             | 1 channel of 4-lane MIPI display interface, supports high-speed mode (per lane       |
+                              +                         +               +                                                                                      +
|                              |                         |               | 1.5Gbps), supports 1920x1080@60Hz, 4K@30Hz,                                          |
+                              +                         +               +                                                                                      +
|                              |                         |               | supports LCDIF display                                                               |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | CSI (MIPI Interface)    | 2             | 2 channels of 4-lane MIPI camera interface, supports high-speed mode (per lane       |
+                              +                         +               +                                                                                      +
|                              |                         |               | 1.5Gbps), supports 4K@30fps                                                          |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | ISI                     | 2             | ISI is a simple camera interface that supports image processing and transmission     |
+                              +-------------------------+---------------+--------------------------------------------------------------------------------------+
|                              | ISP                     | 2             | 1 channel of 12MP@30fps or 4kp45, both 2 channels support 1080p80                    |
+------------------------------+-------------------------+---------------+--------------------------------------------------------------------------------------+

Pin Definition
-----------------

:doc:`《PinDef》<HM.CB314-PinDef>`

Pin Definition & Detailed Function Description
------------------------------------------------

:doc:`《PinMux》<HM.CB314-PinMux>`
