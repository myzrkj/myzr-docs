Platform Introduction
=======================

Product Overview
------------------

- Quad-core Cortex-A53 up to 2.0GHz
- Mali-G52 GPU
- 1TOPS NPU
- LPDDR4/LPDDR4X/DDR4/DDR3/DDR3L/LPDDR3
- 4KP30 H.265/VP9, 1080P60 H.264 video decoder
- 1080P60 H.264 video encoder
- 13M ISP
- LVDS/MIPI-DSI/RGB
- 3x SAI with I2S/PCM/TDM, 1x8ch PDM
- USB3.0 OTG, USB2.0 HOST, PCIE2.1, RGMII + RMII


Target Applications
---------------------

- Consumer Electronics:
  - Tablets: Equipped with a quad-core Cortex-A53 architecture running at a maximum frequency of 2.0GHz, paired with an ARM G52 GPU, it can smoothly run office software, play high-definition videos, and support light gaming, meeting the needs of various daily scenarios.
  - Smart Speakers: Built-in NPU with 1TOPS computing power, enabling interactions such as voice wake-up and keyword detection. Combined with software, it provides services like music playback and information query.
  - Smart Dictionary Pens: For example, NetEase Youdao Dictionary Pen X6 Pro leverages the high-performance NPU and GPU of RK3562 to realize large-model AI interactions, including functions such as answering all questions and in-depth grammar explanations, ensuring fast word lookup and high accuracy.

- Smart Home:
  - Smart Home Appliances: Serving as the control core for smart air conditioners, refrigerators, and other home appliances, it enables remote control and device linkage via the network.
  - Smart Gateways: Supporting multiple protocols such as Wi-Fi and Bluetooth, it acts as the hub of the smart home, connecting and managing various devices.
  - Smart Cameras: Utilizing the computing power of NPU for face recognition and behavior detection to ensure home security.

- Industrial Applications:
  - Industrial Automation Control: With 4 high-performance ARM Cortex-A53 cores, it handles tasks such as logic control and data processing, connecting sensors and actuators to achieve precise production control.
  - Industrial Displays: Used in industrial display screens through interfaces like LVDS and MIPI DSI, providing clear display and smooth touch experience.
  - Industrial Internet of Things (IIoT): Dual Ethernet, CAN, and other interfaces ensure efficient and stable data transmission, enabling device networking and remote monitoring.

- Smart Security:
  - Video Surveillance: Supporting video decoding such as 4K 30fps H.265 and video encoding of 1080p 60fps H.264, combined with NPU for real-time video analysis, it realizes functions like face recognition to enhance the intelligence of security systems.
  - Access Control Systems: Implementing face recognition and fingerprint recognition access control through AI, which can be linked with other security devices.

- Smart Education:
  - Smart Education Tablets: In addition to regular functions, they use AI to provide personalized learning services such as intelligent tutoring and homework correction.
  - Electronic Dictionary Pens: For instance, Youdao Dictionary Pen X6 Pro relies on RK3562 to achieve powerful AI interactions and support learning.

- Smart Retail:
  - AI Electronic Scales: Built-in high-precision ADC module, with low error rate when connected to weighing sensors, supporting the deployment of AI pricing, payment, and other functions on the Android system.
  - Smart Advertising Players: Playing high-definition advertisements, using NPU to realize face recognition and passenger flow statistics for targeted advertising.


Key Features
--------------

1. High-performance CPU: Adopts a quad-core ARM Cortex-A53 architecture with a maximum frequency of up to 2.0GHz. It includes 32KB instruction cache, 32KB data cache, and 512KB L2 cache, providing strong general computing capabilities to meet the needs of multi-tasking and complex applications.
2. Powerful GPU: Integrates Mali-G52 GPU, supporting OpenGL ES 1.1/2.0/3.2, OpenCL 2.0, and Vulkan 1.1. It delivers smooth graphics rendering capabilities, suitable for graphics-intensive tasks such as high-definition video playback and image processing.
3. AI Acceleration Capability: Built-in NPU with 1TOPS computing power, supporting mixed operations of data types including INT4/INT8/INT16/FP16. It is compatible with deep learning frameworks such as TensorFlow, PyTorch, Caffe, and MXNet, providing strong support for AI applications like face recognition and speech recognition.
4. Multimedia Processing Capability: Supports video decoding of 4K 30fps H.265/VP9 and 1080P 60fps H.264, as well as video encoding of 1080P 60fps H.264. It also has high-quality JPEG encoding and decoding capabilities. In addition, it integrates a 13M ISP, supporting HDR (High Dynamic Range), 3DNR (3D Digital Noise Reduction), etc., to meet the needs of applications such as high-definition video surveillance and image processing 1.
5. Rich Interfaces: Supports interfaces such as USB3.0 OTG, USB2.0 HOST, PCIE2.1, RGMII + RMII, as well as dual Ethernet, CAN, UART, SPI, I2C, PWM, etc. It can be easily connected to various external devices to achieve function expansion.
6. Wide Memory Support: Equipped with a 32-bit wide DDR controller, supporting multiple memory types such as DDR3, DDR4, LPDDR3, and LPDDR4. The maximum memory capacity can reach 8GB, meeting the memory requirements of different applications.
7. Low-Power Design: Adopting a 22nm process, it achieves an excellent balance between performance and power consumption. It consumes less than 300mW when running on a static desktop and has a standby current of 3.3mA, making it suitable for devices with high power consumption requirements, such as smart speakers and smart cameras 4.
8. Small Package Size: Adopting an FCCSP478L package with a size of 13.9mm*13.9mm, it helps reduce the volume of products and is suitable for devices with limited space 4.


Processor Block Diagram
--------------------------

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/处理器框图.png
   :alt: 处理器框图.png


Processor Characteristics
---------------------------

**Detailed Parameters**

+------------+---------------------------------------------------------------------+
| Component  | Specifications                                                      |
+------------+---------------------------------------------------------------------+
| CPU        | Quad-core 64-bit Cortex-A53, maximum frequency up to 2.0GHz         |
+            +---------------------------------------------------------------------+
|            | ARM G52 2EE                                                         |
+------------+---------------------------------------------------------------------+
| GPU        | Supports OpenGL ES 1.1/2.0/3.2, OpenCL 2.0, Vulkan 1.1              |
+            +---------------------------------------------------------------------+
|            | Embedded high-performance 2D acceleration hardware                  |
+------------+---------------------------------------------------------------------+
| NPU        | Supports 1TOPS computing power                                      |
+------------+---------------------------------------------------------------------+
| Multimedia | Supports video decoding of 4K 30fps H.265/VP9 and 1080P 60fps H.264 |
+            +---------------------------------------------------------------------+
|            | Supports video encoding of 1080P 60fps H.264                        |
+            +---------------------------------------------------------------------+
|            | Supports 13M ISP                                                    |
+------------+---------------------------------------------------------------------+
| Display    | Single-screen display, supporting LVDS/MIPI-DSI/RGB                 |
+------------+---------------------------------------------------------------------+
| Interface  | Supports USB3.0 OTG, USB2.0 HOST, PCIE2.1, RGMII + RMII             |
+------------+---------------------------------------------------------------------+