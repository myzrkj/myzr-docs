**Product Introduction:**

    - **MYZR i.MX 8M Plus Development Board** (MYZR-IMX8MP-EK314) allows customers to easily evaluate the MYZR-IMX8MP-CB314 Core Board, providing a foundation and reference for customers to design their own hardware.
    - **MYZR i.MX 8M Plus Core Board** (MYZR-IMX8MP-CB314) is built for edge intelligence, machine learning/vision. It is committed to advancing machine learning (ML), machine vision, multimedia, and industrial IoT applications, providing a strong foundation for fields such as smart homes, smart cities, and Industry 4.0.

**Target Applications:**

    - **Smart Home:** AI local servers, alarm and security systems, smart robots, network nodes, controls, home medical monitoring, speakers, AV receivers, and other home automation applications.
    - **Smart City:** Security and safety, monitoring systems, crowd and traffic management, fleet management.
    - **Smart Scenarios:** Smart retail, POS terminals, targeted advertising, building controls, web conferencing systems, medical diagnostics.
    - **Industrial IoT:** Machine learning, robot control, industrial gateways, HMI and computers, commercial printing and scanners, industrial tablets, smart industrial cameras, and various other industrial automation applications.

**Key Features:**

    - **Neural Processing Unit (NPU):** Based on a quad-core Arm® Cortex®-A53 with a maximum frequency of 1.8GHz, it also integrates a neural network acceleration unit (NPU) that provides up to 2.3 TOPS of computing power.
    - **Image Signal Processor (ISP):** Equipped with an Image Signal Processor (ISP) and camera interface, the smart vision system can reach a resolution of 12MP with an input bit rate of up to 375MP/s.
    - **Video Processing and H.265 Encoding:** Features powerful video processing and H.265 encoding capabilities, enabling efficient compression of real-time video for easy upload to the cloud or local storage.
    - **Video Processing Unit (VPU):** Enables efficient encoding and decoding of high-resolution videos. The 2D/3D image processing unit delivers strong graphics capabilities and supports a range of the latest interfaces, such as OpenGL® ES 3.1, Vulkan®, OpenCL™ 1.2, and OpenVG™ 1.1.
    - **Voice Solution:** The low-power voice coprocessor is based on the Cadence® Tensilica® HiFi 4 DSP, with a maximum frequency of 800MHz, helping to achieve low-power performance and high energy efficiency.
    - **Smart Industrial IoT:** Industrial IoT requires machine learning and machine vision systems to work with smart sensors, enabling machines in manufacturing environments to perform inspection, measurement, accurate identification, and decision-making.
    - **Industry 4.0:** Integrates multiple high-speed buses to empower Industry 4.0 applications. The Gigabit Ethernet MAC supports Time-Sensitive Networking (TSN), providing real-time and synchronous control based on Ethernet connections.

| **Hardware Interfaces:**

+-----------------------------+-------------------------+---------------+----------------------------------------------------------------------------------+
|       Interface Type        | Interface Specification |  Max Cfg Cnt  |                                   Description                                    |
+=============================+=========================+===============+==================================================================================+
| Communication Interfaces    | Ethernet                | 2             | 1 channel supports EEE, Ethernet AVB, and IEEE1588                               |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | USB3.0                  | 2             | 2 channels of USB3.0 PHY interfaces                                              |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | UART                    | 4             | 4 channels of UART, up to 4.0Mbps per channel                                    |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | I2C                     | 6             | 4 channels of I2C, supporting up to 400 kbps                                     |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | SPI                     | 3             | 3 channels of eCSPI (Enhanced CSPI), up to 52Mbps each                           |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | PCIe                    | 1             | Single-lane supports PCIe Gen 3, dual-mode operation, usable as root complex     |
+                             +                         +               +                                                                                  +
|                             |                         |               | or endpoint                                                                      |
+-----------------------------+-------------------------+---------------+----------------------------------------------------------------------------------+
| External Storage Interfaces | eMMC                    | 2             | 5.1 FLASH                                                                        |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | NAND                    | 1             | 8-bit NAND flash, supporting ECC and BCH for error detection                     |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | DRAM                    | 1             | 82-bit DRAM, supporting raw MLC/SLC devices, BCH                                 |
+                             +                         +               +                                                                                  +
|                             |                         |               | ECC up to compliance with 62-bit and ONFi3.2 standards                           |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | QSPI                    | 4             | 1 quad-channel external serial flash device interface, supporting XIP mode       |
+-----------------------------+-------------------------+---------------+----------------------------------------------------------------------------------+
| Multimedia                  | HDMI                    | 1             | 1 channel of HDMI 2.0a, supporting 4096x2160@60Hz, and                           |
+                             +                         +               +----------------------------------------------------------------------------------+
|                             |                         |               | supporting HDCP 2.2 and HDCP 1.4, 20+ audio channels with 32-bit                 |
+                             +                         +               +----------------------------------------------------------------------------------+
|                             |                         |               | @384kHz fs, supporting S/PDIF input and output                                   |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | DSI (MIPI Interface)    | 1             | 1 channel of 4-lane MIPI display interface, supporting high-speed mode (per lane |
+                             +                         +               +----------------------------------------------------------------------------------+
|                             |                         |               | 1.5Gbps), supporting 1920x1080@60Hz, 4K@30Hz,                                    |
+                             +                         +               +----------------------------------------------------------------------------------+
|                             |                         |               | and supporting LCDIF displays                                                    |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | CSI (MIPI Interface)    | 2             | 2 channels of 4-lane MIPI camera interface, supporting high-speed mode (per lane |
+                             +                         +               +                                                                                  +
|                             |                         |               | 1.5Gbps), supporting 4K@30fps                                                    |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | ISI                     | 2             | ISI is a simple camera interface that supports image processing and transmission |
+                             +-------------------------+---------------+----------------------------------------------------------------------------------+
|                             | ISP                     | 2             | 1 channel for 12MP@30fps or 4kp45, 2 channels both for 1080p80                   |
+-----------------------------+-------------------------+---------------+----------------------------------------------------------------------------------+
