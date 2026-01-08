Platform Introduction
=======================

Product Overview
-------------------

- RZV2H is a processor specifically designed for high-performance edge AI vision. It balances general computing, real-time control, and AI inference requirements through heterogeneous multi-cores and dedicated accelerators, making it suitable for application development in harsh environments such as industrial, medical, and automotive fields. It features strong computing power and low power consumption, and is applicable to scenarios like industrial automation, robotics, and smart cameras.

Target Applications
----------------------

- Industrial machine vision: Defect detection, barcode recognition, automated sorting.
- Smart cameras: Real-time face recognition, behavior analysis, security monitoring.
- Robotics: SLAM (Simultaneous Localization and Mapping), object grasping and navigation.
- Medical equipment: Endoscopic image processing, medical image analysis.
- Automotive ADAS: Real-time image processing in assisted driving (requires combination with automotive-grade chips).

Key Features
--------------

- **High-performance Heterogeneous Multi-core Architecture**:

- Dual-core Arm Cortex-A55 (1.8 GHz): Handles general-purpose operating systems (such as Linux) and complex applications.
- Dual-core Arm Cortex-R8 (1.0 GHz): Responsible for real-time control tasks.
- Dual-core Renesas self-developed DSP (1.0 GHz): Optimized for vision processing and AI inference.
- IMR (Intelligent Reconfigurable Processor): A hardware accelerator that supports real-time image processing (e.g., ISP, noise reduction, HDR).

- **AI Acceleration Capability**:

- Integrates DRP-AI (Dynamic Reconfigurable Processor) and AI-MAC units, supporting mainstream AI frameworks (TensorFlow, PyTorch, etc.).
- Typical performance: 10 TOPS (INT8), enabling efficient operation of AI models for object detection, classification, etc.

- **Image Processing Unit**:

- Supports multi-camera input (up to 4K resolution).
- Hardware-accelerated H.264/H.265 encoding and decoding, and the ISP (Image Signal Processor) supports noise reduction, distortion correction, etc.

- **Rich Peripheral Interfaces**:

- Video input: MIPI CSI-2, parallel interface.
- Display output: HDMI, MIPI DSI.
- Network: Gigabit Ethernet, TSN (Time-Sensitive Networking).
- Others: USB 3.0, PCIe, CAN FD, SPI, I2C, etc.

- **Low Power Consumption Design**:

- Adopts 16nm FinFET process to balance performance and power consumption, suitable for edge devices.

Processor Block Diagram
--------------------------

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/处理器框图.png
   :alt: 处理器框图.png


Processor Characteristics
---------------------------

**Detailed Specifications**

+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Application Processor        | Dual-core or quad-core Arm Cortex-A55 (1.8GHz), running complex OS such as Linux.                                  |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Real-time Processor          | Dual-core Arm Cortex-R8 (800MHz), used for real-time control (e.g., motors, sensors)                               |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| AI Accelerator               | DRP-AI3 (Dynamically Configurable Processor) + CNN Accelerator, supporting INT8/FP16 with 10 TOPS computing power. |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ISP (Image Signal Processor) | Supports 4K@60fps H.264/H.265 encoding and decoding.                                                               |
+                              +--------------------------------------------------------------------------------------------------------------------+
|                              | Multi-camera input (4x MIPI CSI-2).                                                                                |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| GPU                          | PowerVR Series9XMP, supporting OpenGL ES 3.2/OpenCL 1.2/Vulkan.                                                    |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Memory                       | LPDDR4/LPDDR4X, up to 8GB.                                                                                         |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Storage Interface            | eMMC 5.1, SD card, SPI NOR/NAND Flash.                                                                             |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| High-speed Communication     | USB 3.1, PCIe Gen3, Gigabit Ethernet (supporting TSN).                                                             |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Display Output               | HDMI 2.0 (4K), MIPI DSI.                                                                                           |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Industrial Interfaces        | CAN FD, SPI, I2C, UART, GPIO.                                                                                      |
+------------------------------+--------------------------------------------------------------------------------------------------------------------+
