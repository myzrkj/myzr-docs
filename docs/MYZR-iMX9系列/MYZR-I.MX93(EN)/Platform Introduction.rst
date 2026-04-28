Platform Introduction
=======================

Product Overview
------------------

- The NXP i.MX9 series application processors are built on the market-proven i.MX6 and i.MX8 product families. They integrate higher-performance application cores, independent MCU-like real-time domains, Energy Flex architecture, advanced cybersecurity empowered by EdgeLock(®) secure enclave, and dedicated multi-sensor data processing engines for graphics, image, display, audio and voice. The i.MX9 series is part of the EdgeVerse(™) edge computing platform. Many products in this series integrate a hardware neural processing unit to accelerate edge machine learning applications.

Target Applications
---------------------

1. Smart City

   - The i.MX9 processors can predict, automate, secure and optimize building, energy, transportation, manufacturing and public safety systems, helping build greener, safer and more livable cities.

2. Smart Home
  
   - Smart residences achieve safety, comfort and energy efficiency through design. Scalable i.MX 9 processor solutions enable connected, entertaining and convenient smart homes.
   - Voice assistants, smart gateways, security cameras.

3. Smart Building

   - Taking innovation a step further, i.MX9 application processors deliver more edge-aware, energy-efficient and secure systems through extensive integrated processing and acceleration capabilities.

4. Smart Factory

   - Integrated with multiple processing engines and industrial communication protocols, i.MX 9 processors are suitable for factory automation, machine vision and system management, enabling seamless edge-to-cloud migration.

5. Consumer Electronics

   - E-book readers, portable medical devices.

Key Features
--------------

1. High-performance Heterogeneous Computing

   - Dual-core Arm Cortex-A55 (up to 1.7GHz): Supports complex operating systems such as Linux.
   - Single-core Arm Cortex-M33 (real-time co-processor): Designed for low-power real-time tasks including sensor data processing.
   - NPU (Neural Processing Unit): 2.5 TOPS computing power, optimized for machine learning (ML) and AI inference, compatible with frameworks such as TensorFlow Lite and PyTorch.

2. High-efficiency Design

   - i.MX9 series application processors are equipped with high-precision power control modules to optimize energy efficiency, helping customers reduce carbon footprint or extend battery life.
   - Adopts advanced process technology such as 16nm FinFET, reducing power consumption by 50% compared with the previous generation i.MX 8M Nano.
   - Supports Dynamic Voltage and Frequency Scaling (DVFS) and multi-level power management modes.

3. Edge Intelligence

   - Delivers efficient machine learning acceleration to empower next-generation embedded use cases, improving privacy protection, latency control and bandwidth utilization.

4. Cybersecurity

   - The i.MX9 series enhances cybersecurity via EdgeLock secure enclave, integrating advanced architecture to provide superior threat protection and support the latest encryption protocols.
   - Hardware encryption engine (AES, SHA, RSA, ECC).
   - Secure Boot, Root of Trust and anti-tampering protection.
   - Compliant with industrial security standards such as ISO 21434.

5. Rich Peripheral Interfaces

   - Display: Supports MIPI DSI and LVDS, up to 1080p@60fps.
   - Camera: Dual MIPI CSI interfaces with integrated Image Signal Processor (ISP).
   - Communication:

      - Gigabit Ethernet (supports TSN Time-Sensitive Networking).
      - Wi-Fi 6 / Bluetooth 5.2 (external module required).
      - Industrial interfaces including CAN-FD, USB 2.0/3.0, UART, SPI and I2C.

Processor Block Diagram
-------------------------

.. figure:: /image/MYZR-iMX9系列/MYZR-I.MX93/处理器框图.png
   :alt: 处理器框图.png

Processor Specifications
--------------------------

| Specifications

+-------------------+-------------------------------------------------------------------------------------------------------+
| Multi-core        | 1-2 x Arm® Cortex®-A55, up to 1.7GHz                                                                  |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | Arm Cortex-M33 @ 250Mhz                                                                               |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | Arm® Ethos™ U-65 microNPU                                                                             |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | EdgeLock® Secure Enclave                                                                              |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Connectivity      | 2 x USB 2.0 Type-C with integrated PHY                                                                |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 2 x Gigabit Ethernet: AVB & IEEE 1588 for synchronization, EEE for low power; 1 port with TSN support |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 2 x CAN FD                                                                                            |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 8 x UART, 8 x I2C, 8 x SPI, 2 x I3C                                                                   |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 1 x 4-channel 12-bit ADC                                                                              |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 2 x 32-pin FlexIO (for camera, bus or serial I/O)                                                     |
+-------------------+-------------------------------------------------------------------------------------------------------+
| External Memory   | Up to 3.7GT/s x16 LPDDR4/LPDDR4X (with inline ECC)                                                    |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 3 x SD 3.0/SDIO3.0/eMMC5.1                                                                            |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 1 x 8-lane SPI, supports SPI NOR and SPI NAND flash                                                   |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Graphics          | Hardware compositor for blending, scaling and color space conversion                                  |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Display Interface | 1 x 1080p60 MIPI-DSI (4-lane, 1.5Gbps per lane) with PHY                                              |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 1 x 720p60 LVDS (4-lane)                                                                              |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 24-bit parallel RGB                                                                                   |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Camera Interface  | 1 x 1080p60 MIPI-CSI (2-lane, 1.5Gbps per lane) with PHY                                              |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 8-bit parallel YUV/RGB                                                                                |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Audio             | 7 x I2S TDM (32-bit@768KHz), SPDIF Tx/Rx                                                              |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 8-channel PDM microphone input                                                                        |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | MQS: Medium Quality Sound output (Σ-Δ modulator)                                                      |
+-------------------+-------------------------------------------------------------------------------------------------------+
| OS Support        | Linux®                                                                                                |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | FreeRTOS                                                                                              |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | Greenhills                                                                                            |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | QNX                                                                                                   |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | Vxworks                                                                                               |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Packaging         | 11mm×11mm, 0.5mm pitch FCCSP                                                                          |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 9mm×9mm, 0.5mm pitch FCCSP                                                                            |
+                   +-------------------------------------------------------------------------------------------------------+
|                   | 14mm×14mm, 0.65mm pitch FCCSP                                                                         |
+-------------------+-------------------------------------------------------------------------------------------------------+
| Temperature Range | -40°C ~ 125°C                                                                                         |
+-------------------+-------------------------------------------------------------------------------------------------------+