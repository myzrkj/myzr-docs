Platform Introduction
=======================

Product Overview
------------------

- **CPU**: Equipped with a quad-core ARM Cortex-A53, with a main frequency of up to 1.5GHz, and its performance is more than twice that of chips in the same class. In addition, it also integrates a 300MHz RISC-V MCU, which is used for tasks requiring low power consumption and high real-time performance.
- **NPU**: Built-in self-developed NPU with a computing power of up to 3Tops, supporting data types such as INT8/INT16/FP16, as well as weight sparsification, W4A16/W8A16 mixed-precision quantization and Transformer optimization technology. It can smoothly run large language models and multimodal models with a parameter scale of less than 2B.
- **Memory**: Supports 32-bit DDR3/DDR3L/LPDDR3/DDR4/LPDDR4 memory, as well as storage devices such as eMMC 4.51, SPI Flash, and Nand Flash, and also supports fast startup.
- **Display**: Equipped with MIPI-DSI/RGB interface, it can support display output up to 1080P60fps. At the same time, it integrates a 2D graphics engine, supporting image rotation, mirroring, scaling and other operations.
- **Multimedia Interface**: Supports 4*MIPI CSI/sub LVDS and DVP interfaces (BT.656/BT.1120), which can connect multiple cameras. In terms of video encoding and decoding, it supports 4K H.264/H.265 30fps video encoding and decoding, and can also realize encoding of 3840 x 2160\@30 fps + 720p\@30 fps and decoding of 3840 x 2160\@30 encoding + 3840 x 2160\@30 fps.
- **Other Interfaces**: Added USB 3.0 interface to provide higher data transmission rate; built-in 100M Ethernet PHY to simplify network interface design; integrated audio codec (Audio Codec) to support high-quality audio processing.


Target Applications
----------------------

- **Intelligent Security**: Supports target detection functions such as face recognition and license plate recognition, and can be applied to access control systems, behavior analysis devices, etc. Its integrated AI-ISP engine combined with AI Remosaic technology can realize day-night dual-mode adaptive image quality optimization. At the same time, AOV 3.0 technology supports low-power audio event wake-up function, which can detect abnormal audio in real time. The standby power consumption is as low as about 1mW, enabling 7×24-hour audio and video joint monitoring, which is suitable for the deployment of smart city-level security equipment.
- **Industrial Vision**: Can be used in scenarios such as precision part quality inspection and production line defect detection. Combined with AI algorithms, it can achieve micron-level accuracy. In addition, RV1126B supports binocular/quadocular panoramic dynamic stitching technology and 6-DOF hardware-level digital anti-shake, which can eliminate image tearing, achieve ultra-wide-angle field of view, and maintain clear imaging in low-illumination environments. It is suitable for industrial scenarios such as robot navigation and PLC control auxiliary systems.
- **Intelligent Vehicle Mount**: Can be used in multi-channel video recording equipment such as driving recorders and vehicle-mounted DVRs, supporting H.264/H.265 encoding and 4K video decoding, and can adapt to the wide-temperature operation requirements of the vehicle-mounted environment (-40℃~+85℃). At the same time, it also supports 8-channel 1080P video synchronous processing, which can be applied to ADAS and DMS systems to improve driving safety.
- **Service Robots**: Relying on its powerful CPU and NPU performance, as well as multimodal processing capabilities, RV1126B can be used for multimodal environment perception and path planning of service robots. It is suitable for scenarios such as warehouse logistics and medical collaboration, and can accurately identify target objects in complex scenarios, realize cross-modal information integration, and provide support for the intelligent decision-making of robots.
- **Edge Computing**: Suitable for edge computing scenarios such as smart retail (e.g., passenger flow statistics) and smart agriculture (e.g., pest and disease identification), providing hardware-level security and low-power support. Its 3Tops computing power and efficient encoding and decoding capabilities can quickly process data at the edge and realize 7×24-hour all-weather monitoring.


Main Features
---------------

- **Powerful Computing Engine**: Equipped with a quad-core Cortex-A53 CPU architecture, with a main frequency of up to 1.5GHz, and its performance is more than twice that of chips in the same class. Built-in self-developed NPU with a computing power of up to 3Tops, supporting data types such as INT8/INT16/FP16, as well as weight sparsification, W4A16/W8A16 mixed-precision quantization and Transformer optimization technology. It can smoothly run large language models and multimodal models with a parameter scale of less than 2B.
- **Excellent Image Processing Capability**: Integrates dedicated AI-ISP hardware, which does not occupy NPU resources during operation. Combined with AI Remosaic technology, it can realize "day-night dual-mode adaptation"—presenting ultra-high-definition image quality during the day and maintaining clear imaging in ultra-low illumination at night. Supports 8-megapixel 45FPS ultra-high-definition encoding, and through dynamic bit rate optimization technology, it saves 50% of the code stream compared with the traditional CBR mode. In addition, it is equipped with hardware-level 6-DOF digital anti-shake, which accurately identifies and eliminates high-frequency jitter to make moving images smoother. At the same time, it supports binocular/quadocular panoramic dynamic stitching technology to provide an ultra-wide-angle field of view.
- **Low Power Consumption and Audio Monitoring**: The newly added AOV3.0 technology incorporates a low-power audio event wake-up function, which can detect abnormal sound sources such as dog barking, glass breaking, and gunshots in real time. The device's standby power consumption is as low as about 1mW, supporting 7×24-hour all-weather audio and video monitoring.
- **Hardware-Level Security Assurance**: Built-in national secret-level security scheme, supporting SM2/SM3/SM4 encryption algorithms, integrating TrustZone security isolation technology and keyladder key management system. From data collection to storage, as well as the protection of AI algorithm models, it further meets application scenarios with extremely high security requirements.
- **Rich Interfaces and Functions**: The DDR bandwidth has jumped from 2166MT/S to 3200MT/S, and the data transmission rate has been significantly accelerated. Added USB 3.0 interface to provide higher data transmission rate; built-in 100M Ethernet PHY to simplify network interface design; integrated audio codec (Audio Codec) to support high-quality audio processing. In addition, the number of Sensor accesses has increased to 4, supporting multi-camera synchronous processing, and the stitching performance and distortion correction performance have also been significantly improved.


Processor Block Diagram
--------------------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B/处理器框图.jpg
   :alt: 处理器框图.jpg


Processor Characteristics
---------------------------

|  Detailed Parameters

+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| CPU                      | 4-core ARM Cortex-A53                                                                                                         |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| NPU                      | Self-developed NPU with 3 TOPS computing power                                                                                |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Memory                   | Supports 32-bit DDR3/DDR3L/LPDDR3/DDR4/LPDDR4 memory, as well as storage devices such as eMMC 4.51, SPI Flash, and Nand Flash |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Supported Models         | Can smoothly run large language models and multimodal models with less than 2 billion (2B) parameters                         |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ISP                      | Dedicated AI-ISP hardware                                                                                                     |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Audio Processing         | AOV3.0 technology                                                                                                             |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Video Encoding           | Up to 8-megapixel @ 45FPS                                                                                                     |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Anti-shake and Stitching | Hardware-level 6-DOF digital anti-shake                                                                                       |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Security Encryption      | Supports SM2/SM3/SM4 encryption algorithms and integrates TrustZone security isolation technology                             |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Peripheral Interfaces    | USB3.0, Audio Codec, Ethernet PHY, etc.                                                                                       |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------+
