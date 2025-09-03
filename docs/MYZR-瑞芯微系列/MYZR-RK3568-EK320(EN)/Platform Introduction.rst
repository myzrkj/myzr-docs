Platform Introduction
=======================

Product Overview
------------------

- Quad-core Cortex-A55 up to 2.0GHz 
- Mali-G52 GPU
- 1TOPS NPU
- LPDDR4/LPDDR4X/DDR4/DDR3/DDR3L/LPDDR3, ECC
- 4KP60 H.265/H.264/VP9 video decoder
- 1080P60 H.264/H.265 video encoder
- 8M ISP with HDR
- Dual display, LVDS/MIPI-DSI/RGB/eDp/RGB/HDMI2.0/EBC
- 1x8ch I2S/TDM, 1x8ch PDM, 2x2ch I2S
- USB3.0 x2/SATA3.0 x3/PCIE2.1/QSGMII, PCIE3.0 1x2Lanes/2x1Lane

Target Applications
~~~~~~~~~~~~~~~~~~~~~

- Industrial Control

  - Industrial Automation: It can be used in controllers, Human-Machine Interfaces (HMI), and other devices in industrial automation production lines. It realizes precise control and monitoring of the production process, can quickly process various sensor data and control commands, and ensures the efficient and stable operation of the production line.
  - Smart Factory: In the construction of smart factories, RK3568 can serve as an edge computing node to conduct real-time analysis and processing of various data in the factory. It realizes functions such as intelligent operation and maintenance of equipment, optimization of production processes, and quality inspection, thereby improving the production efficiency and management level of the factory.


- Smart Home

  - Smart Speakers: With its powerful audio processing capability, RK3568 can provide smart speakers with a clear and smooth voice interaction experience. It supports functions such as voice wake-up, voice recognition, and music playback, and can also联动控制 with other smart home devices.
  - Smart Home Appliances: It can be applied to home appliances such as smart TVs, air conditioners, and refrigerators to realize intelligent operation and management. For example, it enables smart TVs to have smoother video playback effects, more intelligent voice control functions, and the ability to interconnect with other smart home devices.


- IoT Devices

  - Smart Gateways: As the core hub of IoT devices, RK3568 can connect various types of sensors and devices, realize functions such as protocol conversion, data aggregation, and transmission, and provide stable and efficient connection services for IoT systems.
  - Smart Monitoring: In the field of smart monitoring, it can be used in network cameras, video monitoring terminals and other devices. It supports high-definition video encoding and decoding, and realizes functions such as real-time monitoring and intelligent analysis (such as face recognition, behavior analysis, etc.), ensuring the efficiency and accuracy of security monitoring.


- Consumer Electronics

  - Tablets: It provides strong performance support for tablets, meeting users' needs in daily office work, entertainment, learning, etc., such as smoothly running office software, watching high-definition videos, and playing light games.
  - E-book Readers: RK3568 can provide e-book readers with good display effects and smooth page-turning experience, while supporting the decoding and reading functions of various e-book formats to meet users' reading needs.


Main Features
~~~~~~~~~~~~~~~

- High-performance Processor

  - Adopts a quad-core Cortex-A55 architecture with a maximum main frequency of 2.0GHz, which can provide smooth multi-task processing capabilities to meet the needs of various complex application scenarios.
  - Equipped with a Neon coprocessor, it can accelerate multimedia and digital signal processing tasks, improving the overall performance of the chip.

- Rich Display Interfaces

  - Supports a variety of display interfaces, including HDMI, MIPI-DSI, LVDS, etc., which can meet the connection needs of different display devices.
  - Supports 4K resolution video decoding and output, providing clear and delicate image display effects, suitable for application scenarios such as high-definition video playback and intelligent display terminals.

- Powerful Multimedia Processing Capability

  - Integrates a dedicated video decoding and encoding engine, supporting multiple video formats such as H.265, H.264, VP9, etc., and can realize efficient video encoding and decoding functions.
  - Has the function of dual-screen different display, which can drive two different display devices at the same time to display different contents, providing convenience for some special application scenarios.

- Rich Peripheral Interfaces

  - Has multiple USB interfaces, SDIO interfaces, SPI interfaces, I2C interfaces, UART interfaces, etc., facilitating connection and communication with various external devices, such as storage devices, sensors, wireless modules, etc.
  - Supports Gigabit Ethernet interface, providing stable and high-speed network connection, meeting the device's demand for network bandwidth, and suitable for intelligent devices that need to be connected to the network.

- Low Power Consumption Design

  - Adopts advanced process technology and low-power design technology, effectively reducing the power consumption of the chip while ensuring performance.
  - Supports multiple power management modes, such as sleep and standby, which can automatically adjust power consumption according to the operating status of the device, extending the battery life of the device, and is suitable for portable devices with high power consumption requirements.

- Security Features

  - Integrates a Hardware Security Module (HSM), supporting multiple encryption algorithms such as AES, RSA, ECC, etc., providing hardware-level security protection for the device.
  - Supports functions such as secure boot and digital signature, preventing the device from being illegally tampered with and attacked, and protecting the user's data security and the stability of the device.

Processor Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/处理器框图.png
   :alt: 处理器框图.png


Processor Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Detailed Parameters**

+------------+-------------------------------------------------------------+
| CPU        | Quad-core 64-bit Cortex-A55, maximum frequency up to 2.0GHz |
+------------+-------------------------------------------------------------+
| GPU        | ARM G52 2EE                                                 |
+            +-------------------------------------------------------------+
|            | Supports OpenGL ES 1.1/2.0/3.2, OpenCL 2.0, Vulkan 1.1      |
+            +-------------------------------------------------------------+
|            | Embedded high-performance 2D acceleration hardware          |
+------------+-------------------------------------------------------------+
| NPU        | Supports 1T computing power                                 |
+------------+-------------------------------------------------------------+
| Multimedia | Supports 4K 60fps H.265/H.264/VP9 video decoding            |
+            +-------------------------------------------------------------+
|            | Supports 1080P 60fps H.265/H.264 video encoding             |
+            +-------------------------------------------------------------+
|            | Supports 8M ISP and HDR                                     |
+------------+-------------------------------------------------------------+
| Display    | Supports multi-screen different display                     |
+            +-------------------------------------------------------------+
|            | Supports eDp/HDMI2.0/MIPI/LVDS/24bit RGB/EBC                |
+------------+-------------------------------------------------------------+
| Interface  | Supports USB2.0/USB3.0/PCIE3.0/PCIE2.1/SATA3.0/QSGMII       |
+------------+-------------------------------------------------------------+