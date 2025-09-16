Platform Introduction
=======================

Product Overview
------------------

- iFPD, industrial control and gateways, cloud terminals, face recognition devices, in-vehicle central controls, commercial displays
- ARM 64-bit high-performance octa-core general-purpose processor, equipped with a wealth of high-speed interfaces such as PCIE/USB3.0/SATA/GMAC, as well as low-speed expansion interfaces including CAN FD/DSMC/UART/SPI/I2C/I3C. It features strong computing and expansion capabilities, allowing a single platform to quickly deploy multiple products.
- Built-in 6TOPS* self-developed high-efficiency AI processor unit, meeting various artificial intelligence application needs.
- Rich display interfaces and a high-efficiency GPU processor, supporting 3 displays with different content (each screen shows different content).
- Powerful image perception, video encoding/decoding, and audio processing capabilities, integrating visual and voice recognition interactions.
- Support for standard Android and Linux SDKs, compatible with various domestic operating systems.


Target Applications
---------------------

1. Industrial Field: Can be used in high-end industrial PLCs, motion controllers, industrial vision inspection equipment, etc. It meets the requirements for stability and high performance in industrial environments and can easily handle complex tasks in industrial scenarios, such as real-time control, image recognition and analysis.
2. Edge Computing: With its high-performance CPU, 6TOPS NPU, and rich interfaces, it can perform data processing and analysis on edge devices, reducing the need for data transmission to the cloud and improving response speed. It is suitable for edge servers, industrial gateways, and other devices.
3. Smart Commercial Displays: Supports 8K decoding, 4K encoding, and three-screen different display functions, along with rich display interfaces and a powerful GPU. It can drive high-resolution displays to realize functions such as advertising playback, information display, and interactive query. It can be applied to smart advertising machines, digital signs, self-service terminals, etc.
4. Cloud Terminal Products: As a terminal device for cloud desktops, RK3576 can connect to cloud servers via the network, receive and process images, videos, and data sent from the cloud, providing users with a smooth cloud desktop experience.
5. Automotive Electronics: Suitable for the smart cockpit field, it can support different display outputs of multiple screens, providing the vehicle with infotainment systems, instrument panel displays, head-up displays, etc. It also has strong computing power to process data from in-vehicle cameras, sensors, and other devices.
6. Artificial Intelligence Devices: Built-in 6TOPS NPU, supporting mainstream deep learning frameworks. It can be used in face recognition devices, face payment devices, smart robots, etc., and can quickly and accurately perform artificial intelligence tasks such as image recognition, voice recognition, and natural language processing.
7. Medical Devices: Can be applied to medical endoscopes, medical imaging equipment, etc. Its powerful video image processing capabilities and computing performance help in high-definition display and analysis of medical images, improving the accuracy and efficiency of diagnosis.
8. Education Field: Can be used in smart education equipment, such as interactive large screens, educational tablets, etc. It supports high-definition video playback, operation of interactive teaching software, and other functions, providing rich multimedia resources and interactive experiences for teaching.
9. Smart Retail: In smart retail equipment, such as smart cash registers, self-service shopping terminals, etc., RK3576 can realize functions such as commodity recognition, price calculation, and payment processing, improving retail efficiency and user experience.


Main Features
---------------

1. High-performance CPU: Adopts 8nm process, based on octa-core Quad A72+A53 CPU with a maximum frequency of 2.2GHz. It has super strong general computing performance and can easily handle multi-task processing and complex computing tasks.
2. Powerful AI acceleration capability: Integrates a 6TOPS NPU, supporting INT4/INT8/INT16/FP16/TF32 hybrid operations and mainstream deep learning frameworks. It can perform efficient artificial intelligence algorithm processing, meeting the needs of various AI applications such as smart security, face recognition, and voice recognition.
3. Excellent multimedia processing capability: Supports 8K 30fps and 4K 120fps high-frame-rate video decoding, including formats such as H.265/HEVC, VP9, AVS2, AV1, etc. It also supports 4K 60fps H.265 and H.264 video encoding, as well as MJPEG 4K 60fps encoding/decoding capabilities, providing a clear and smooth video playback and processing experience.
4. Rich display interfaces: Supports various display interfaces such as HDMI2.1, EDP1.3, MIPI DSI-2, DP1.4, etc., and can realize three-screen different display function. It supports a maximum video display resolution of 4K, meeting the connection needs of different display devices and providing users with diversified display solutions.
5. Strong network communication capability: Equipped with 1 channel of 1000Mbps Ethernet, 1 channel of 100Mbps Ethernet, 2.4GHz/5GHz dual-band WiFi, Bluetooth 5.0, 4G LTE and other network interfaces, enabling more stable data transmission and faster speed, meeting the network connection needs in different application scenarios.
6. Rich expansion interfaces: Has various interfaces such as USB3.2, USB2.0, Type-C, RS232, RS485, CAN, optocoupler isolation input, relay output, etc. It also supports high-speed interfaces such as PCIE2.1 and SATA3.1, facilitating the connection of various external devices for function expansion.
7. Support for multiple operating systems: Supports Android14, Linux OS, Buildroot + QT, domestic operating systems, etc., providing a safe and stable system environment for product research and development, and meeting the software needs of different users.
8. Low-power design: Adopts advanced 8nm process technology, effectively reducing power consumption while ensuring high performance. It also supports low-power standby mode, which can reduce the power consumption of the device in standby state, extend the battery life of the device, and is suitable for devices with high power consumption requirements.


Processor Block Diagram
--------------------------

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/处理器框图.png
   :alt: 处理器框图.png

Processor Characteristics
---------------------------

**Detailed Parameters**

+-------------+-----------------------------------------------------------------------------------+
| CPU         | Quad-core Cortex-A72 + Quad-core Cortex-A53, maximum frequency 2.2GHz             |
+-------------+-----------------------------------------------------------------------------------+
| GPU         | ARM G52 MC3                                                                       |
+-------------+-----------------------------------------------------------------------------------+
| NPU         | 6TOPS*RKNN                                                                        |
+-------------+-----------------------------------------------------------------------------------+
| PQ          | Rockchip dedicated Picture Quality Engine (HDR, ACM, DCl, etc.)                   |
+-------------+-----------------------------------------------------------------------------------+
| Display     | DisplayPort/MIPI/eDP/HDMI/RGB/EBC, multi-screen different display                 |
+-------------+-----------------------------------------------------------------------------------+
| Memory      | 32bits LPDDR4/4x, LPDDR5                                                          |
+             +-----------------------------------------------------------------------------------+
|             | UFS 2.0 (2-lane), eMMC 5.1, SPI Nor/Nand                                          |
+-------------+-----------------------------------------------------------------------------------+
| Video       | 8K30 H.264/H.265/VP9/AV2/AVS2 Decoder                                             |
+             +-----------------------------------------------------------------------------------+
|             | 4K60 H.264/H.265 Encoder                                                          |
+-------------+-----------------------------------------------------------------------------------+
| Camera      | 16M ISP with HDR (up to 120dB)                                                    |
+             +-----------------------------------------------------------------------------------+
|             | MIPICSI-2(CDPHY=1*4-lane, DPHY=2*4-lane/4*2-lane), DVP                            |
+-------------+-----------------------------------------------------------------------------------+
| Interface   | 5 SAl interfaces (total 7-tx and 7-rx lanes, each lane supports 8-ch 12S/PCM/TDM) |
+             +-----------------------------------------------------------------------------------+
|             | 2 PCM (2*8-ch)                                                                    |
+             +-----------------------------------------------------------------------------------+
|             | 2 S/PDIF TX and 1 S/PDIF RX                                                       |
+             +-----------------------------------------------------------------------------------+
|             | ASRC                                                                              |
+             +-----------------------------------------------------------------------------------+
|             | USB 3.0 DRD (supports Alt mode with DP)                                           |
+             +-----------------------------------------------------------------------------------+
|             | Combo USB3.0 DRD/PCIe 2.1 RC/SATA3                                                |
+             +-----------------------------------------------------------------------------------+
|             | Combo PCle 2.1 RC/SATA3                                                           |
+             +-----------------------------------------------------------------------------------+
|             | RGMIlx2                                                                           |
+             +-----------------------------------------------------------------------------------+
|             | CAN FD, DSMC                                                                      |
+             +-----------------------------------------------------------------------------------+
|             | UART, SPI, PWM, I2C, SAR-ADC                                                      |
+-------------+-----------------------------------------------------------------------------------+