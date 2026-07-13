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

Rockchip RK3568 is a mid-to-high-end general-purpose embedded SoC chip officially launched by Rockchip in 2021. Designed specifically for IoT, edge computing, industrial control, and multimedia processing applications, it is the successor to the previous generation classic product RK3399.

Target Applications
-------------------

Industrial Control
~~~~~~~~~~~~~~~~~~

1. Industrial Automation: Can be used in controllers, human-machine interfaces (HMI), and other devices in industrial automation production lines. It enables precise control and monitoring of production processes, rapidly processing various sensor data and control commands to ensure efficient and stable operation of production lines.

2. Smart Factory: In smart factory construction, RK3568 can serve as an edge computing node, performing real-time analysis and processing of various factory data. It enables intelligent equipment operation and maintenance, production process optimization, and quality inspection functions, improving factory production efficiency and management level.

Smart Home
~~~~~~~~~~

1. Smart Speakers: With its powerful audio processing capabilities, RK3568 provides clear and smooth voice interaction experiences for smart speakers. It supports voice wake-up, voice recognition, music playback, and can integrate with other smart home devices for coordinated control.

2. Smart Appliances: Can be applied in smart TVs, air conditioners, refrigerators, and other home appliances for intelligent operation and management. For example, enabling smart TVs with smoother video playback, smarter voice control, and interoperability with other smart home devices.

IoT Devices
~~~~~~~~~~~

1. Smart Gateway: As the core hub of IoT devices, RK3568 can connect multiple types of sensors and devices, providing protocol conversion, data aggregation, and transmission functions to deliver stable and efficient connectivity services for IoT systems.

2. Smart Surveillance: In smart surveillance applications, it can be used in IP cameras, video monitoring terminals, and other devices. It supports HD video encoding and decoding, enabling real-time monitoring and intelligent analysis (such as face recognition, behavior analysis), ensuring efficient and accurate security monitoring.

Consumer Electronics
~~~~~~~~~~~~~~~~~~~~

1. Tablets: Provides powerful performance support for tablets, meeting user needs in daily office work, entertainment, and learning. It can smoothly run office software, play HD videos, and handle light gaming.

2. E-book Readers: RK3568 delivers excellent display quality and smooth page-turning experiences for e-book readers. It supports decoding and reading of multiple e-book formats to meet user reading needs.

Key Features
------------

* High-performance processor: Quad-core Cortex-A55, up to 2.0GHz frequency, integrated NEON coprocessor  
* Powerful graphics processing: Mali-G52 GPU, OpenGL ES 3.2, OpenCL 2.0, Vulkan 1.0   

* AI computing capability: Integrated 1TOPS NPU, supports TensorFlow, Caffe, MXNet, PyTorch, ONNX and other AI frameworks

* Rich display interfaces: HDMI2.0, eDP, MIPI-DSI, LVDS, RGB, supports dual-screen display and 4K video output

* Rich peripheral interfaces: USB2.0, USB3.0, SATA3.0, PCIe, UART, SPI, I2C, CAN (if hardware supported)

* Low-power design: Supports dynamic voltage and frequency scaling (DVFS) and multiple sleep modes

* Security features: Supports Secure Boot, AES, RSA, ECC encryption algorithms

Processor Block Diagram
-----------------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/处理器.png
   :alt: 处理器框图
   :width: 100%

Processor Specificationskua
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
   }
   table td:nth-child(1) { width: 10%; }   /* Column 1 width */
   table td:nth-child(2) { width: 20%; }   /* Column 2 width */
   table td:nth-child(3) { width: 70%; }   /* Column 3 width */
   </style>


+----+------------+--------------------------------------------------------+
|     .. centered:: Detailed Specifications                                |
+====+============+========================================================+
| 1  | CPU        | Quad-core 64-bit Cortex-A55, up to 2.0GHz              |
+----+------------+--------------------------------------------------------+
| 2  | GPU        | ARM G52 2EE                                            |
+    +            +--------------------------------------------------------+
|    |            | Supports OpenGL ES 1.1/2.0/3.2, OpenCL 2.0, Vulkan 1.1 |
+    +            +--------------------------------------------------------+
|    |            | Integrated high-performance 2D acceleration            |
+----+------------+--------------------------------------------------------+
| 3  | NPU        | 1TOPS computing power                                  |
+----+------------+--------------------------------------------------------+
| 4  | Multimedia | Supports 4K 60fps H.265/H.264/VP9 video decoding       |
+    +            +--------------------------------------------------------+
|    |            | Supports 1080P 60fps H.265/H.264 video encoding        |
+    +            +--------------------------------------------------------+
|    |            | 8M ISP support, HDR support                            |
+----+------------+--------------------------------------------------------+
| 5  | Display    | Multi-screen display support                           |
+    +            +--------------------------------------------------------+
|    |            | Supports eDP/HDMI2.0/MIPI/LVDS/24bit RGB/EBC           |
+----+------------+--------------------------------------------------------+
| 6  | Interfaces | Supports USB2.0/USB3.0/PCIE3.0/PCIE2.1/SATA3.0/QSGMII  |
+----+------------+--------------------------------------------------------+