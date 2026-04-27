Platform Introduction
=======================

Product Overview
-------------------

- The iMX8MP is a balanced processor oriented to edge AI and multimedia applications. It accelerates machine learning tasks through NPU. Adopting a heterogeneous design with Cortex-A53 and Cortex-M7, it is suitable for industrial, consumer electronics and IoT scenarios.

Target Applications
---------------------

- Industrial Automation: Machine vision quality inspection, predictive maintenance (real-time NPU analysis).
- Smart Home: Multimodal AI central control (voice + video processing), voice assistants (such as Alexa), facial recognition access control.
- Medical Devices: High-definition medical image display and processing.
- In-Vehicle Infotainment: Multi-screen interaction and navigation systems.
- Edge AI Devices: Security cameras, drone obstacle avoidance systems.
- Multimedia Terminals: 4K smart displays, digital signage.

Key Features
---------------

1. High-performance Heterogeneous Computing Architecture

- Quad-core Arm Cortex-A53: Maximum main frequency up to 1.8 GHz, supports Linux/Android systems for general computing and complex applications.
- Real-time Core Cortex-M7: Single-core 800 MHz, dedicated to low-latency real-time tasks (such as sensor control and industrial communication).
- Dedicated NPU (Neural Processing Unit):

  - 2.3 TOPS (INT8) computing power, optimized for edge AI inference, compatible with frameworks such as TensorFlow Lite and PyTorch.

2. Powerful Multimedia Processing Capabilities

- 4K Video Codec:
    
  - Supports H.265/H.264 4K@30fps encoding and decoding, as well as VP9 decoding.

- Integrated ISP (Image Signal Processor):

  - Dual camera input (MIPI CSI-2) supported, up to 12MP resolution, with HDR, noise reduction and distortion correction functions.

- GPU Graphics Rendering:

  - Vivante GC7000UL GPU, supports OpenGL ES 3.1 and Vulkan 1.1, applicable to graphical interfaces and lightweight 3D rendering.

3. Edge AI and Machine Learning Optimization

- NPU Acceleration: Efficiently runs AI models such as image classification and object detection (e.g., MobileNet, YOLOv3).
- eIQ® Toolchain:

  - Provides tools for model quantization, optimization and deployment, supporting ONNX, TensorFlow Lite and other frameworks.

- Low-power AI Inference: Ideal for battery-powered or heat-limited edge devices.
  
4. Rich Industrial-grade Interfaces

- High-speed Communication:

  - Dual Gigabit Ethernet (supports TSN Time-Sensitive Networking), 2x USB 3.0, PCIe Gen3.

- Display Output: HDMI 2.0a (4K), MIPI DSI, LVDS.
- Industrial Control Interfaces: CAN FD, SPI, I2C, UART, PWM, GPIO.
- Camera Input: Dual MIPI CSI-2 interfaces for industrial camera connection.

5. High Reliability and Security

- Hardware Security Engine:

  - AES-256/SHA-2 encryption, secure boot (HAB), anti-tamper protection.

- Industrial-grade Design:

  - Operating temperature range: -40°C to +105°C, compliant with industrial EMI/EMC standards.

6. Flexible Development Support

- Operating System Compatibility:

  - Linux (Yocto customized), Android, FreeRTOS (Cortex-M7).

- Evaluation Kit:

  - i.MX 8M Plus EVK development board, equipped with hardware resources including camera interfaces, display interfaces and expansion slots.

- Software Ecosystem:

  - NXP official BSP, MCUXpresso IDE, pre-trained AI model library.

Processor Block Diagram
--------------------------

.. figure:: /image/MYZR-iMX8系列/MYZR-IMX8MP-LB276/处理器框图.png
   :alt: 处理器框图.png

Processor Specifications
--------------------------

**Detailed Parameters**

+--------------+------------------------------+
| CPU          | 4x Cortex-A53 + 1x Cortex-M7 |
+--------------+------------------------------+
| AI Computing | 2.3 TOPS (NPU)               |
+--------------+------------------------------+
| Video Codec  | 4K H.265/H.264               |
+--------------+------------------------------+
| ISP          | Dual MIPI CSI                |
+--------------+------------------------------+
| GPU          | Vivante GC7000UL             |
+--------------+------------------------------+
| Video Decode | 4K Multi-format Decoding     |
+--------------+------------------------------+
