Platform Introduction
=======================

Product Overview
------------------

- 8nm advanced manufacturing process, 8-core 64-bit architecture, high performance, low power consumption
- ARM Mali-G610 MC4 GPU with dedicated 2D graphics acceleration module
- 6TOPs NPU, enabling various AI scenarios
- 8K video encoding and decoding, 8K display output
- Built-in multiple display interfaces, supporting multi-screen different display
- Superb image processing capability, 48MP ISP, supporting multi-camera input
- Rich high-speed interfaces (PCIe, TYPE-C, SATA, Gigabit Ethernet) for easy expansion
- Compatible with Android and Linux OS

Target Applications
---------------------

1. **Industrial Control**: Can be used in industrial automation equipment, robot control, smart factories and other fields to achieve high-precision control and data processing. For example, in the controller of an automated production line, RK3588 can quickly process data from various sensors, accurately control the movement of robotic arms, and improve production efficiency and product quality.
2. **Intelligent Transportation**: Suitable for traffic monitoring, smart street lights, in-vehicle navigation and other devices in intelligent transportation systems. Taking traffic monitoring as an example, RK3588 can perform real-time analysis on video data collected by cameras, realizing functions such as vehicle identification, traffic flow statistics, and violation detection, providing strong support for traffic management.
3. **Smart Home**: Applicable to smart home central control systems, smart speakers, smart cameras and other products. For instance, in a smart home central control system, RK3588 can connect a variety of smart devices to achieve interconnection and intelligent control between devices. Users can control home devices such as lights, curtains, and air conditioners through mobile phones or voice commands.
4. **Medical Equipment**: Used in medical imaging equipment, medical monitoring equipment, intelligent medical robots and other aspects. Taking medical imaging equipment as an example, RK3588 can quickly process image data such as X-rays and CT scans, assisting doctors in disease diagnosis and improving the accuracy and efficiency of diagnosis.
5. **Education Field**: Applicable to smart education tablets, electronic whiteboards, educational robots and other products. For example, in a smart education tablet, RK3588 can support rich educational applications and interactive functions, providing students with personalized learning experiences and helping teachers carry out teaching activities more effectively.
6. **Security Monitoring**: Serves as the core chip in security monitoring systems, and can be used in network cameras, video encoders, video analysis servers and other devices. It can perform real-time encoding, storage and analysis of monitoring videos, realizing functions such as face recognition, behavior analysis and event early warning, and ensuring the safety of public places and homes.
7. **Edge Computing**: In edge computing scenarios, RK3588 can be used as an edge computing node to process and analyze collected data locally, reducing data transmission volume and improving response speed. For example, in industrial Internet of Things scenarios, it can process sensor data in real time on the device side, detect equipment faults in a timely manner and issue early warnings, reducing reliance on cloud computing resources.
8. **Consumer Electronics**: Commonly used in high-end tablets, smart TV boxes, game consoles and other consumer electronic products. Taking high-end tablets as an example, RK3588 can provide strong graphics processing capabilities and a smooth system operation experience, supporting functions such as high-definition video playback and large-scale game running, to meet users' needs for entertainment and office work.

Main Features
---------------

1. **High-performance CPU**: Adopts 8nm process and an 8-core 64-bit architecture consisting of four Cortex-A76 cores and four Cortex-A55 cores. The Cortex-A76 cores have a maximum frequency of 2.4GHz, and the Cortex-A55 cores have a frequency of 1.8GHz, delivering strong performance with a significant improvement compared to the previous generation. For example, compared with RK3399, the CPU performance is increased by 3 times.
2. **Powerful GPU**: Integrates a Mali-G610 MP4 quad-core GPU, supporting graphics processing interfaces such as OpenGL ES1.1/2.0/3.2, OpenCL 2.2, and Vulkan 1.2. It can provide smooth 2D/3D graphics processing capabilities. Compared with RK3399, the GPU performance is increased by 6 times, which can meet the needs of high-end games, high-definition video playback and complex graphical interfaces.
3. **Efficient NPU**: Built-in with Rockchip's self-developed third-generation NPU processor, with a computing power of up to 6Tops, supporting INT4/INT8/INT16/FP16 mixed operations. Its strong compatibility allows for easy conversion of network models based on a series of frameworks such as TensorFlow/PyTorch/Caffe, and can provide strong computing power support for various AI application scenarios, such as artificial intelligence algorithm training, inference, as well as face recognition and behavior analysis in intelligent security.
4. **Excellent Video Encoding and Decoding Capability**: Supports 8K@60fps H.265/VP9 and 8K@30fps H.264/AV1 video decoding, as well as 8K@30fps H.265/H.264 and 1080P@60fps VP8/AVS1/AVS1+/MPEG-4 video encoding. It can realize high-quality video playback, recording and editing functions, meeting the needs of the 8K video era.
5. **Advanced Image Signal Processor**: Built-in a new generation of hardware-based image signal processor (ISP) with a maximum of 48 million pixels. It can implement algorithm accelerators such as HDR, 3A, LSC, 3DNR, 2DNR, sharpening, dehaze, fisheye correction and gamma correction, and has a wide range of applications in post-processing of graphics, which can improve image quality and provide better support for camera applications.
6. **Rich Storage and Interfaces**: In terms of storage, it supports a maximum of 32G large-capacity running memory and has a high-performance 4-channel external memory interface (LPDDR4/LPDDR4X/LPDDR5). It is equipped with rich interfaces, including multiple video output interfaces such as HDMI2.1/MIPI-DSI/DP1.4/VGA and video input interfaces such as HDMI RX2.0/MIPI-CSI, supporting multiple 8K video outputs and 4K video inputs, and can realize up to four-screen different display. It also includes 4 standard SATA3.0 interfaces, on-board high-speed M.2 SATA3.0 interface, standard PCIe3.0 (4lane) interface, as well as expansion interfaces such as RS485, RS232, I2S, I2C, UART, CAN, SPDIF, MIPI CSI, MIPI DSI, USB3.0, USB2.0, SPI and GPIO, which can meet the connection needs of various devices.
7. **Multiple Network Support**: Supports dual Gigabit Ethernet, 2.4GHz/5GHz dual-band WiFi6 (802.11ax), Bluetooth 5.0, and supports 5G/4G LTE expansion, enabling devices to have high-speed and stable network connections, suitable for various application scenarios that require network access.
8. **Low Power Consumption Design**: Combines the big.LITTLE architecture with advanced power management functions. While providing high performance, it can also maintain good energy efficiency, making it suitable for devices with power consumption requirements, such as mobile devices and portable devices.

Processor Block Diagram
--------------------------

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/处理器框图.png
   :alt: 处理器框图.png

Processor Characteristics
---------------------------

**Detailed Parameters**

+-----------------------+------------------------------------------------------------------------------------------------+
| CPU                   | 8-core 64-bit big.LITTLE architecture, 4*Cortex-A76 + 4*Cortex-A55                             |
+-----------------------+------------------------------------------------------------------------------------------------+
| GPU                   | ARM Mali-G610 MC4                                                                              |
+                       +------------------------------------------------------------------------------------------------+
|                       | OpenGL ES 1.1/2.0/3.1/3.2                                                                      |
+                       +------------------------------------------------------------------------------------------------+
|                       | Vulkan 1.1, 1.2                                                                                |
+                       +------------------------------------------------------------------------------------------------+
|                       | OpenCL 1.1, 1.2, 2.0                                                                           |
+                       +------------------------------------------------------------------------------------------------+
|                       | Built-in high-performance 2D graphics acceleration module                                      |
+-----------------------+------------------------------------------------------------------------------------------------+
| NPU                   | 6TOPS computing power, triple-core architecture, supporting int4/int8/int16/FP16/BF16/TF32     |
+-----------------------+------------------------------------------------------------------------------------------------+
| Multimedia            | Supports H.265/H.264/AV1/VP9/AVS2 video decoding, up to 8K60FPS                                |
+                       +------------------------------------------------------------------------------------------------+
|                       | Supports H.264/H.265 video encoding, up to 8K30FPS                                             |
+-----------------------+------------------------------------------------------------------------------------------------+
| Display               | Supports multiple display interfaces such as eDP/DP/HDMI2.1/MIPI                               |
+                       +------------------------------------------------------------------------------------------------+
|                       | Supports multi-screen different display, up to 8K60FPS                                         |
+-----------------------+------------------------------------------------------------------------------------------------+
| Video Input           | 32MP ISP, supporting HDR and 3DNR                                                              |
+                       +------------------------------------------------------------------------------------------------+
|                       | Supports multi-camera input (4*4lanes or 4*2lanes+2*4Lanes) with MIPI CSI-2 and DVP interfaces |
+                       +------------------------------------------------------------------------------------------------+
|                       | Supports HDMI2.0 input, up to 4K60FPS                                                          |
+-----------------------+------------------------------------------------------------------------------------------------+
| High-speed Interfaces | Supports PCle3.0/PCle2.0/SATA3.0/RGMII/TYPE-C/USB3.1/USB2.0                                    |
+-----------------------+------------------------------------------------------------------------------------------------+