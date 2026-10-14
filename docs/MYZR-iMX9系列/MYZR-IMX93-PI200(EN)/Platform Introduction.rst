.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Platform Introduction
=====================

Product Overview
----------------

i.MX 93 application processors provide efficient machine learning (ML) acceleration and advanced information security through integrated EdgeLock ® security zones to support energy-efficient edge computing.

the i.MX 93 application processor is the first product in the i.MX series to integrate the scalable Arm Cortex- A55 core, helping to improve the performance and energy efficiency of Linux ® edge applications and the Arm Ethos™ - U65 microNPU, helping developers create more powerful, cost-effective, and energy-efficient ML applications.

i.MX 93 processors utilize NXP's innovative Energy Flex architecture to optimize the performance and energy efficiency of industrial, IoT and automotive devices. SoCs offer a wealth of peripherals for the automotive, industrial, and consumer electronics IoT segments.

As part of the EdgeVerse™ Smart Edge solution, the i.MX 93 series offers consumer electronics, industrial, extended industrial, and automotive-grade certified products, supported by a long-term supply plan for NXP products.

Target Applications
-------------------

1. Smart Cities
~~~~~~~~~~~~~~~

• i. The MX9 processor predicts, automates, protects, and simplifies building, energy, transportation, manufacturing, and public safety systems to help make cities greener, safer, and more livable.

2. Smart Home
~~~~~~~~~~~~~

• Smart homes are designed to be safe, comfortable and energy efficient. The scalable i.MX 9 processor solution enables the home to be connected, fun, and convenient.

• Voice assistant, smart gateway, security camera.

3. Smart Building
~~~~~~~~~~~~~~~~~

• i. MX9 application processors go one step further to create more edge-aware, energy-efficient, and secure systems through extensive integrated processing and accelerated innovation.

4. Smart Factory
~~~~~~~~~~~~~~~~

• i.MX 9 processors integrate multiple processing engines and industrial communication protocols for factory automation, machine vision, and systems management for edge-to-cloud migration.

5. Consumer Electronics
~~~~~~~~~~~~~~~~~~~~~~~

• E-book readers, portable medical devices.

Main characteristics
--------------------

1. High-performance heterogeneous calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

• Dual-core Arm Cortex- A55 (clock frequency up to 1.7GHz): Supports complex operating systems such as Linux.

• Single-core Arm Cortex- M33 (real-time coprocessor): for low-power real-time tasks such as sensor data processing.

• NPU (neural network processing unit): 2.5 TOPS computing power, optimized for machine learning (ML) and AI reasoning, supports TensorFlow Lite, PyTorch and other frameworks.

2. High-performance design
~~~~~~~~~~~~~~~~~~~~~~~~~~

• i. The MX9 series of application processors have built-in high-precision power control to optimize energy efficiency, helping customers reduce their carbon footprint or extend battery life.

• 50% lower power consumption than the previous generation (i.MX 8M Nano) with more advanced process processes such as 16nm FinFET.

• Support dynamic voltage / frequency scaling (DVFS) and multi-level power management modes.

3. Edge perception
~~~~~~~~~~~~~~~~~~

• Provides efficient machine learning acceleration to support next-generation use cases for embedded systems, improving privacy protection, latency, and bandwidth.

4. Information Security
~~~~~~~~~~~~~~~~~~~~~~~

• i. MX9 improves information security with EdgeLock security zones, integrates advanced architectures, provides superior threat protection, and supports the latest encryption protocols.

• Hardware encryption engines (AES, SHA, RSA, ECC).

• Secure Boot, Root of Trust, and Tamper Protection.

• Complies with industrial safety standards (e.g. ISO 21434).

5. Rich peripheral interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

• Display: Supports MIPI DSI and LVDS up to 1080p @ 60fps.

• Camera: Dual MIPI CSI interface with support for image signal processing (ISP).

Correspondence:

• Gigabit Ethernet (supports TSN time-sensitive networks).

•  Wi-Fi 6 / Bluetooth 5.2 (requires an external module).

•  CAN-FD、USB 2.0/3.0、ART、SPI、I2C、and other industrial interfaces.

Processor Block Diagram
-----------------------

.. image:: ../../../image/MYZR-iMX9系列/MYZR-IMX93-PI200/处理器框图.png
   :alt: 处理器框图.png
   :width: 100%

Processor Features
------------------

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;
       word-wrap: break-word;
   }
   </style>

+------+-----------+--------------------------------------------------------------------------+
|      | SPECIFICA |                                                                          |
|      | TIONS     |                                                                          |
+======+===========+==========================================================================+
| 1    | Applicati | Arm Cortex- A55: 1-2 cores, frequency up to 1.7GHz, used to run rich     |
|      | on        | operating systems such as Linux.                                         |
|      | Processin |                                                                          |
|      | g         |                                                                          |
+------+-----------+--------------------------------------------------------------------------+
| 2    | Real-time | Arm Cortex- M33: 1 core, frequency up to 250MHz, for real-time tasks,    |
|      | control   | independent operation.                                                   |
+------+-----------+--------------------------------------------------------------------------+
| 3    | AI/ML     | Arm Ethos- U65 microNPU: Dedicated neural network processor with a       |
|      | Accel     | hashrate of about 0.5 TOPS for efficient edge inference.                 |
+------+-----------+--------------------------------------------------------------------------+
| 4    | Memory    | LPDDR4 /LPDDR4X: Supports up to 3.7GT/s rate with inline ECC,            |
|      |           | capacity up to 2GB.                                                      |
+------+-----------+--------------------------------------------------------------------------+
| 5    | Save      | eMMC 5.1/SD 3.0/SPI NOR /NAND: Supports multiple flash interfaces for    |
|      |           | system boot and data storage.                                            |
+------+-----------+--------------------------------------------------------------------------+
| 6    | Display   | MIPI-DSI, LVDS, parallel RGB: Support 1080p60 MIPI-DSI, 720p60 LVDS and  |
|      |           | other display interfaces.                                                |
+------+-----------+--------------------------------------------------------------------------+
| 7    | Camera    | MIPI-CSI, Parallel YUV /RGB: Supports 1080p60 MIPI-CSI camera input,     |
|      |           | suitable for vision applications.                                        |
+------+-----------+--------------------------------------------------------------------------+
| 8    | CONNECTIO | 2x Gigabit Ethernet, 2x USB 2.0, 2x CAN FD: One of the Ethernet ports    |
|      | N         | supports TSN, which is suitable for industrial real-time communication.  |
+------+-----------+--------------------------------------------------------------------------+
| 9    | Audio     | I2S /TDM, PDM, SPDIF: Supports multi-channel audio interface and         |
|      |           | 8-channel PDM microphone input.                                          |
+------+-----------+--------------------------------------------------------------------------+
| 10   | SAFETY    | EdgeLock ® security zones: preconfigured autonomous security subsystems  |
|      |           | that provide root of trust, secure boot, and more.                       |
+------+-----------+--------------------------------------------------------------------------+
| 11   | Package   | FCCSP: 11x11mm, 9x9mm, 14x14mm and other small size packages are         |
|      |           | available.                                                               |
+------+-----------+--------------------------------------------------------------------------+
| 12   | Operating | Industrial / Automotive grade: Industrial grade up to -40°C to 125°C     |
|      | Temperatu |                                                                          |
|      | re        |                                                                          |
+------+-----------+--------------------------------------------------------------------------+