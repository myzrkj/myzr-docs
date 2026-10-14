.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Product Introduction
====================

PI Board Introduction
---------------------

Hardware Resources
~~~~~~~~~~~~~~~~~~

NXP i. The MX9 series of application processors are built on market-proven i. Based on the MX6 and i. MX8 series products, it brings together a higher performance application core, a separate MCU-like real-time domain, an Energy Flex architecture, advanced information security powered by EdgeLock (®) security zones, and a dedicated multi-sensor data processing engine (graphics, images, display, audio, and voice). i. The MX9 series is part of the EdgeVerse (™) edge computing platform, and many of its products integrate hardware neural processing units to accelerate machine learning applications at the edge.

Core Computing Resources
^^^^^^^^^^^^^^^^^^^^^^^^

#. Application Processor (Main CPU): 1-2x Arm Cortex- A55, clock frequency up to 1.7GHz, based on Armv8-A architecture, supports DynamIQ technology.

#. Real-time coprocessor (Low Power Domain): 1x Arm Cortex- M33, frequency 250MHz, for real-time control, no need for external MCU.

#. AI /ML Acceleration (Flex Domain): Arm Ethos- U65 microNPU, dedicated to neural network inference acceleration.

#. Cache and Memory: A55 Core: 32 kB I-cache, 32 kB D-cache, 64 kB L2 Cache, 256 kB L3 Cache with ECC. M33 Core: 16 kB +16 kB Code + Sys Cache, 256 kB TCM /OCRAM (with ECC).

Memory and storage resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. External DRAM: x16 LPDDR4 /LPDDR4X, speed up to 3.7GT /s, support Inline ECC.

#. Boot storage: Support Octal SPI (compatible with SPI NOR /NAND Flash) with Inline Crypto function.

#. Extended Storage: 3x SD 3.0/SDIO 3.0/eMMC 5.1 Interface.

#. On-chip memory (OCRAM): 640 kB OCRAM with ECC protection.

Connect with I /O resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. High-speed network: 2x Gigabit Ethernet (supports AVB, IEEE 1588, EEE), 1 of which supports TSN.

#. USB: 2x USB 2.0 Type-C, built-in PHY.

#. Industrial bus: 2x CAN FD, 8x UART /USART、8x I2C, 8x SPI, 2x I3C.

#. Analog and expansion: 1x 4-channel 12-bit ADC, 2x 32-pin FlexIO interface (configurable as camera, bus or serial I /O）

Multimedia & Display Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Display interface: 1x 1080p60 MIPI-DSI (4-lane, 1.5Gbps /lane）、1x 720p60 LVDS (4-lane), 24-bit parallel RGB.

#. Camera interface: 1x 1080p60 MIPI-CSI (2-lane, 1.5Gbps /lane）、8位并行 YUV /RGB。

#. Graphics Processing: Hardware Compositor that supports blending, composition, scaling, and color space conversion.

#. Audio interface: 7x I2S TDM (32-bit @ 768KHz), SPDIF Tx /Rx、8通道 PDM microphone input, MQS (medium quality sound output)

PI board front and back diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-iMX9系列/MYZR-IMX93-PI200/PI板正反图_01.jpeg
   :alt: PI板正反图_01.jpeg
   :width: 100%

.. image:: ../../../image/MYZR-iMX9系列/MYZR-IMX93-PI200/PI板正反图_02.jpeg
   :alt: PI板正反图_02.jpeg
   :width: 100%

PI Board Interface Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-iMX9系列/MYZR-IMX93-PI200/PI板接口图_01.jpeg
   :alt: PI板接口图_01.jpeg
   :width: 100%

.. image:: ../../../image/MYZR-iMX9系列/MYZR-IMX93-PI200/PI板接口图_02.jpeg
   :alt: PI板接口图_02.jpeg
   :width: 100%
