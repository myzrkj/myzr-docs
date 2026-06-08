Platform Introduction
=======================

Product Overview
------------------

- SSD2355 is a highly integrated AIoT system-on-chip (SoC).
- Specifically designed for personal mobile devices, battery-powered devices, and AIoT applications.
- Integrates a 64-bit quad-core processor, advanced ISP, and AI acceleration engine.
- Equipped with rich high-speed interfaces to support connections with various peripherals.
- Provides a complete solution with high performance, high image quality, and low cost.
- Features a programmable neural network engine to facilitate the implementation of edge-side intelligent applications.

Target Applications
---------------------

1. Smart Home: Applied to smart home central controllers, AI cameras, smart doorbells and other devices. For example, with its IVE and IPU, it can perform real-time human detection and face recognition to achieve intelligent alarm and automatic control.
2. Industrial Vision: Suitable for industrial sensors, scanners, small PLCs, etc. Its powerful ISP and IVE support operations such as image filtering and matrix operations, enabling precise object recognition and robotic arm control.
3. Battery-Powered Devices: Widely used in portable medical devices, handheld payment terminals, walkie-talkies, etc. Its advanced low-power architecture and low-leakage RTC mode ensure long battery life of the devices.
4. Consumer Electronics: Can be used in smart network cameras, educational tablets, advertising players, etc. Supports dual-camera input and multi-channel display output to meet interaction and display needs.
5. Security Surveillance: As the core of network cameras and video analysis boxes, it supports smooth video capture at 30fps and ensures video stream security through a hardware encryption engine.
6. Edge Computing: Serves as an edge computing node to complete sensor data analysis and AI inference on the edge, reducing cloud dependency and achieving fast response.

Main Features
---------------

1. High-Performance Processor Core:

  - Adopts a quad-core ARM Cortex-A35 CPU with a maximum frequency of 1.5GHz.
  - Each core is equipped with 32KB L1 I-Cache and 32KB L1 D-Cache, sharing a 256KB L2 cache.
  - Integrates Neon and FPU to support parallel computing and floating-point operations.
  - Each core has an independent power domain and voltage domain to achieve refined power consumption control.

2. Powerful AI Computing Power and Multi-Core Heterogeneity:

  - Integrates a 1TOPS NPU: The Intelligent Processing Unit (IPU) is a pure hardware accelerator that supports 4/8/16-bit programmable precision, empowering edge-side AI applications.
  - Efficient AI Ecosystem: Supports model conversion for mainstream open-source frameworks (ONNX/Caffe/TensorFlow, etc.) and efficiently supports Transformer networks.
  - Algorithm Optimization: Specifically optimized for model series such as PoolFormer, SegFormer, Swin, and TopFormer.
  - 576MHz RISC-V Coprocessor: Forms a "general-purpose processing + real-time hardware control" multi-core heterogeneous solution, responsible for real-time tasks and low-power control to improve system efficiency.

3. Excellent Image Processing Capability:

  - Security-Grade ISP: Supports 12M@30fps or 21M@30fps camera input.
  - Multi-Interface Input: Supports MIPI CSI (2 data lanes + 2 clock lanes) and parallel interface.
  - Advanced Image Enhancement: Supports 3DNR/2DNR, Wide Dynamic Range (WDR), lens shading correction, 3A (AWB/AE/AF), etc., to output high-definition image quality.

4. Advanced Video and Analysis Engine:

  - Intelligent Video Engine (IVE): A pure hardware accelerator that supports image processing operators such as Filter2D, Gaussian filtering, dilation/erosion, and matrix multiplication to achieve efficient video analysis.
  - Intelligent Processing Unit (IPU): In addition to AI inference, it also supports various video analysis functions such as FD/FR, motion detection, and object tracking.

5. Flexible Display Output:

  - Supports MIPI DSI TX 4-lane with a maximum resolution of 2560x1600@60fps.
  - Supports TTL/parallel RGB interface with a maximum resolution of 1280x800@60fps.
  - Adapts to displays of different sizes and supports multi-screen display applications.

6. Rich Peripheral Interfaces:

  - Network: Built-in dual 10/100M Ethernet MAC (EMAC x2).
  - USB: 2 USB 2.0 interfaces, each configurable as Host or Device mode.
  - Storage: Supports eMMC 5.0, SDIO 2.0, SPI NOR/NAND Flash.
  - Control and Expansion: 7 UARTs, 4 FUARTs, 6 I2C Masters, multiple SPI Masters/Slaves, 20 PWM outputs, 8 PWM inputs (supports encoder mode).
  - ADC: Built-in multiple high-precision ADCs (10-bit 5-channel, 12-bit 22-channel/2-channel) for various analog signal acquisition.

7. Highly Integrated Audio System:

  - Supports 8-channel DMIC, 3-channel AMIC (single-ended/differential), 2-channel DAC with a signal-to-noise ratio (SNR) exceeding 95.2dB.
  - Supports 3 groups of I2S (compatible with TDM mode), with a maximum of 8 inputs and 2 outputs, and a bit width of up to 32-bit.
  - Supports SPDIF input (24-bit).

8. Security and Reliability:

  - Integrates a hardware encryption engine that supports national and international algorithms such as AES/DES/3DES/SM2/SM3/SM4.
  - Supports Secure Boot and ARM TrustZone technology.
  - Built-in OTP memory to ensure the security of keys and data.

9. Low Power Consumption and Power Management:

  - Built-in Real-Time Clock (RTC) that supports a 32.768kHz crystal oscillator and features a low-leakage mode, suitable for battery-powered applications.
  - Equipped with an independent Power Management (PM) domain that supports multiple wake-up sources.

Processor Block Diagram
-------------------------

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2355-EK199/处理器框图.png
   :alt: 处理器框图.png
   :width: 80%

Processor Characteristics
----------------------------

|  Detailed Parameters

+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| CPU                   | Quad-core ARM Cortex-A35 64-bit processor                                                                                                           |
+                       +-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Maximum frequency up to 1.5GHz                                                                                                                      |
+                       +-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Integrates 576MHz RISC-V coprocessor                                                                                                                |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| NPU                   | Integrates an AI processing unit with 1TOPS computing power                                                                                         |
+                       +-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Pure hardware accelerator, supporting 4/8/16-bit programmable precision                                                                             |
+                       +-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Efficiently supports Transformer networks and mainstream AI frameworks                                                                              |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Multimedia            | Intelligent Video Engine (IVE) supports hardware-accelerated video analysis                                                                         |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Display               | Supports MIPI DSI TX 4-lane, maximum 2560x1600@60fps                                                                                                |
+                       +-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Supports TTL/parallel RGB interface, maximum 1280x800@60fps                                                                                         |
+                       +-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Supports 8/16-bit I8080 interface                                                                                                                   |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Video Input           | Built-in ISP, supporting 12M/21M@30fps cameras                                                                                                      |
+                       +-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Supports MIPI CSI (2 data lanes) and parallel interface                                                                                             |
+                       +-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                       | Supports dual-camera (1 data lane) input                                                                                                            |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| High-Speed Interfaces | Integrates dual USB 2.0, dual Ethernet, SD/eMMC, and multiple groups of SPI/I2C/UART interfaces to meet the expansion needs of various peripherals. |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+