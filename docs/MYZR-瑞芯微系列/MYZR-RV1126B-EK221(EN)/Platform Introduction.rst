.. raw:: html

   <style>
   h1 {
       color: green;
   }
   </style>

Platform Introduction
=====================

Product Overview
----------------

RV1126B-P is a high-performance vision processing system-on-chip (SoC) designed for machine vision, especially suitable for artificial intelligence applications.

Target Applications
-------------------

Smart Security
~~~~~~~~~~~~~~

1. Access Control: Face recognition access control, community gate license plate recognition devices

2. Campus Security: Factory/community video behavior analysis cameras, high-altitude parabolic monitoring cameras

3. Ultra-low Power Security: AOV low-power audio-visual alarm cameras, 7×24h audio-visual warning cameras for machine rooms and corridors

Industrial Vision
~~~~~~~~~~~~~~~~~

1. Production Line Inspection: Electronic component, hardware parts appearance defect detection equipment

2. Industrial Camera: AGV inspection robot binocular panoramic camera module, robotic arm visual positioning camera

3. Industrial Control Accessories: PLC visual auxiliary inspection complete machine, assembly line ultra-wide-angle anti-shake industrial camera

Smart Vehicle
~~~~~~~~~~~~~

1. Vehicle Recording: Multi-channel panoramic dash cam, bus/truck vehicle DVR recorder

2. Driving Assistance: ADAS forward collision warning, DMS driver fatigue monitoring vehicle camera

3. Special Vehicles: Engineering machinery, cold chain vehicle multi-channel video monitoring terminal (wide temperature -40°C~85°C)

Service Robots
~~~~~~~~~~~~~~

1. Warehouse Logistics: Warehouse handling AGV robot environmental visual perception module, shelf goods recognition robot

2. Commercial Services: Hotel welcome robot, shopping mall guide robot visual main control

3. Medical Equipment: Medical care robot, ward inspection robot multi-modal perception motherboard

Edge Computing
~~~~~~~~~~~~~~

1. Smart Retail: Store passenger flow statistics camera, shelf product recognition terminal

2. Smart Agriculture: Field pest and disease recognition camera, breeding environment all-weather monitoring equipment

3. Small Edge Terminal: Community IoT edge collection box, small station AI data processing complete machine

Key Features
------------

Computing Power Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Quad-core Cortex-A53 processor, 1.5GHz frequency, comprehensive performance is 2 times better than competitors of the same specification;

* Built-in 3TOPS self-developed NPU, compatible with multi-precision data and hybrid quantization, Transformer optimization, can deploy large models within 2B parameters and multi-modal AI models.

Image Imaging Performance
~~~~~~~~~~~~~~~~~~~~~~~~

* Equipped with independent hardware AI-ISP, does not occupy NPU computing power;

* Equipped with AIRemosaic for day-night adaptive imaging, clear low-light images;

* Supports up to 8MP@45FPS encoding, dynamic bitrate optimization can save 50% bitstream;

* Hardware 6-DOF anti-shake + binocular/quad-camera panoramic stitching, outstanding anti-shake and ultra-wide-angle imaging capabilities.

Ultra-low Power Audio Warning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Equipped with AOV3.0 technology, with built-in audio event wake-up, can recognize abnormal sound sources such as breaking and abnormal noise;

* Standby power consumption is about 1mW, achieving all-weather uninterrupted audio-visual detection.

Security Encryption Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Built-in national cryptographic security engine, supports SM2/SM3/SM4 national cryptographic algorithms;

* Equipped with TrustZone isolation and Keyladder key management to achieve end-to-end security protection for video data and AI models.

Peripheral and Storage Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* DDR speed upgraded to 3200MT/S, improved transmission efficiency;

* Equipped with USB3.0, integrated 100Mbps Ethernet PHY and onboard audio Codec;

* Can connect up to 4 external Sensors, supports multi-channel camera synchronous acquisition, improved image stitching and distortion correction capabilities.

Processor Block Diagram
-----------------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/处理器框图.jpg
   :alt: Processor Block Diagram
   :width: 100%

Processor Specifications
------------------------

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
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
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+----------------------------------------+------------------------+--------------------------------------------------------+
| .. centered :: Detailed Specifications                                                                                   |
+========================================+========================+========================================================+
| 1                                      | CPU                    | Quad-core ARM Cortex-A53                               |
+----------------------------------------+------------------------+--------------------------------------------------------+
| 2                                      | NPU                    | Self-developed NPU with 3TOPS computing power          |
+----------------------------------------+------------------------+--------------------------------------------------------+
| 3                                      | Memory                 | Supports 32-bit DDR3/DDR3L/LPDDR3/DDR4/LPDDR4 memory,  |
|                                        |                        | also supports eMMC 4.51, SPI Flash, Nand               |
+----------------------------------------+------------------------+--------------------------------------------------------+
| 4                                      | Supported Models       | Can smoothly run large language models and multi-modal |
|                                        |                        | models with up to 2 billion (2B) parameters            |
+----------------------------------------+------------------------+--------------------------------------------------------+
| 5                                      | ISP                    | Dedicated AI-ISP hardware                              |
+----------------------------------------+------------------------+--------------------------------------------------------+
| 6                                      | Audio Processing       | AOV3.0 technology                                      |
+----------------------------------------+------------------------+--------------------------------------------------------+
| 7                                      | Video Encoding         | Up to 8MP@45FPS                                        |
+----------------------------------------+------------------------+--------------------------------------------------------+
| 8                                      | Anti-shake & Stitching | Hardware-level 6-DOF digital anti-shake                |
+----------------------------------------+------------------------+--------------------------------------------------------+
| 9                                      | Security Encryption    | Supports SM2/SM3/SM4 encryption algorithms,            |
|                                        |                        | integrates TrustZone security isolation technology     |
+----------------------------------------+------------------------+--------------------------------------------------------+
| 10                                     | Peripheral Interfaces  | USB3.0, Audio Codec, Ethernet PHY, etc.                |
+----------------------------------------+------------------------+--------------------------------------------------------+