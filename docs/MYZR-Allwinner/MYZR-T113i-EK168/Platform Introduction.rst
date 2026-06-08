Platform Introduction
=======================

Product Overview
------------------

| Allwinner T113 chip is a processor integrating a dual-core Cortex-A7 CPU, a 64-bit Xuantie C906 RISC-V CPU, and a DSP, with a main frequency of 1.2GHz. It supports full-format decoding and multi-format encoding, featuring rich multimedia functions and a wide range of connection interfaces such as USB, SDIO, UART, SPI, CAN, and Ethernet. This chip is suitable for key fields including industry, electric power, and transportation.

Target Applications
---------------------

- Industrial HMI: Small touchscreen control panels (e.g., PLC interaction interfaces), HMI human-machine interfaces.
- Smart Home Central Control: Voice recognition gateways, low-power display terminals, smart central control screens, voice assistants (requiring an external DSP/AI module).
- IoT Edge Devices: Data acquisition gateways (CAN/UART to Wi-Fi/Ethernet), low-power sensor gateways.
- Consumer Electronics: Educational tablets, portable medical devices.
- In-Vehicle Devices: In-Vehicle Infotainment (IVI) systems, reverse parking cameras.

Key Features
---------------

- High Cost-Effectiveness: Compared with similar products, it has a lower price and is suitable for cost-sensitive applications.
- Hybrid Architecture: Cortex-A7 + RISC-V balances general computing and real-time performance requirements.
- Industrial-Grade Reliability: Supports wide-temperature operation from -40°C to +85°C.
- Wide-Temperature Industrial-Grade Support.
- Extremely Low Standby Power Consumption.

Processor Block Diagram
--------------------------

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/处理器框图.png
   :alt: 处理器框图.png


Processor Characteristics
----------------------------

|  Detailed Specifications

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Category                | Description                                                                                                                 |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Application Processor   | Dual-core Arm Cortex-A7 (up to 1.2GHz), running Linux/RTOS systems.                                                         |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Real-Time Coprocessor   | Xuantie C906 RISC-V (up to 600MHz), used for real-time tasks (e.g., sensor data collection, communication protocol stacks). |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| GPU                     | Mali-400 MP2, supporting OpenGL ES 2.0 and OpenVG 1.1, suitable for 2D/lightweight 3D interfaces.                           |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Display Interface       | RGB/LVDS/MIPI-DSI, supporting up to 1080p@60fps output.                                                                     |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Video Codec             | H.264 decoding (1080p@60fps), encoding (1080p@30fps).                                                                       |
+                         +-----------------------------------------------------------------------------------------------------------------------------+
|                         | JPEG encoding/decoding (supporting 16MP resolution).                                                                        |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Audio Interface         | I2S/PCM, digital microphone input, supporting multi-channel audio output.                                                   |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Memory                  | DDR3/DDR3L/LPDDR3, up to 2GB.                                                                                               |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Storage Interface       | eMMC 5.0, SD 3.0, SPI NAND/NOR Flash.                                                                                       |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Communication Interface | 10/100M Ethernet (with built-in PHY), USB 2.0 OTG/Host, Wi-Fi/Bluetooth (requiring external modules).                       |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Industrial Control      | CAN 2.0B, SPI, I2C, UART, PWM, ADC.                                                                                         |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Camera Input            | 8-bit parallel interface or MIPI CSI, supporting 5-megapixel cameras.                                                       |
+-------------------------+-----------------------------------------------------------------------------------------------------------------------------+