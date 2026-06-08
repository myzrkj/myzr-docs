Platform Introduction
========================

Product Overview
-------------------

- The Allwinner T536 chip integrates multiple high-performance computing units, including a 4-core Arm(®) Cortex(®)-A55 CPU, NPU, and dual RISC-V MCUs. It boasts powerful hardware encoding capabilities, supports a large number of interfaces commonly used in industrial scenarios (such as 4-channel CAN-FD and LocalBus), and enables ECC full-path data verification and error correction. Meeting industrial-grade quality standards, the chip can be applied in fields like smart industry and smart power. Its main applications include smart large-screen devices, advertising players, interactive terminals, and AIoT scenarios.

Target Applications
----------------------

| 1. Smart Large-Screen Devices
| - 8K advertising players and digital signage (supporting HDR playback + AI interaction)
| - Conference tablets (4K video conferencing + whiteboard writing)

| 2. Industrial HMI & Edge Computing
| - Machine vision (NPU-accelerated defect detection)
| - Industrial control (CAN FD + real-time Linux)

| 3. Smart Home Central Control
| - Voice assistants (NPU-accelerated speech recognition)
| - Multi-screen interaction (HDMI + MIPI dual-screen different display)

| 4. In-Vehicle Infotainment (IVI)
| - Supports Android Automotive and multi-screen in-vehicle display

Key Features
--------------

- Integrates a 4-core Arm Cortex-A55 (with a maximum frequency of 1.6GHz), along with multiple computing units such as NPU and MCU.
- Supports ECC full-path data verification and error correction.
- Supports a large number of commonly used interfaces, including 4-channel CAN-FD.
- Operating temperature range: -40℃ ~ 85℃.

Processor Block Diagram
--------------------------

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/处理器框图.jpg
   :alt: 处理器框图.jpg
   :width: 90%

Processor Characteristics
---------------------------

|  Detailed Parameters

+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Category              | Specifications                                                                                                                                     |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| CPU                   | 4-core ARM Cortex-A55, with a maximum main frequency of 1.6GHz.                                                                                    |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| RISC-V MCU            | Dual 64-bit Xuantie E907 cores, with a main frequency of 600MHz.                                                                                   |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| NPU                   | Computing power up to 2TOPS                                                                                                                        |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Industrial Interfaces | 4-channel CAN-FD, 17-channel UART, 2-channel GMAC Gigabit Ethernet, LocalBus (self-developed high-speed parallel bus with a bandwidth of 300MB/s). |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| High-Speed Interfaces | USB3.1, PCIe2.1, SDIO, SPI, I2C, PWM, etc.                                                                                                         |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Multimedia Interfaces | 4-channel MIPI CSI camera input, MIPI DSI/LVDS/RGB display interfaces (supporting 1920×1200@60Hz).                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Memory                | Supports LPDDR4/LPDDR4X                                                                                                                            |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Storage               | Supports eMMC, SPI NAND, etc.                                                                                                                      |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Video Codec           | 4K@25fps H.264 encoding, 4K@15fps decoding.                                                                                                        |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ISP Technology        | Self-developed AI ISP, supporting 8M@30fps, WDR, and low-light optimization.                                                                       |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Graphics Acceleration | G2D engine, supporting display channel acceleration.                                                                                               |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Operating Systems     | Linux 5.10/5.15, Tina 5.x, Debian, etc.                                                                                                            |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Temperature Range     | -40℃ ~ 85℃, meeting harsh industrial environments.                                                                                                 |
+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
