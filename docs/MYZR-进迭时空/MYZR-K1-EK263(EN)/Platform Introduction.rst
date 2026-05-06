Platform Introduction
=======================

Product Overview
------------------

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/产品简介1.png
  :alt: 产品简介 1.png
  :width: 60%

1. Overview
-------------

|  SpacemiT Key Stone® K1 is a high-performance, ultra-low-power SoC integrated with 8 RISC-V CPU cores and SpacemiT® Daoyi™ AI computing capability. It features the following core advantages:

- Integrated with self-developed SpacemiT® X60™ RISC-V core processor, compliant with RISC-V 64GCVB architecture and RVA22 specification
- Delivers 2.0 TOPS AI computing power via customized RISC-V instructions, enabling CPU-AI hybrid computing
- Compatible with mainstream AI inference frameworks, including TensorFlow Lite, TensorFlow and ONNX Runtime
- Achieves ultra-low power consumption through granular power islands and dynamic power state adjustment, leading to outstanding energy efficiency
- Equipped with full-featured interfaces for innovative applications and product development
- Compatible with mainstream operating systems to meet diverse application requirements
- Compliant with industrial-grade reliability standards

2. Features
-------------

Application Processor (AP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


- SpacemiT® X60™ RISC-V Dual-Cluster 8-Core Processor
- Compliant with RISC-V 64GCVB architecture and RVA22 specification
- Cluster 0
  - Quad-core design with 2.0 TOPS AI computing power
  - 32KB L1 cache per core
  - 512KB L2 cache
  - 512KB TCM
  - 256-bit vector unit

- Cluster 1
  - Quad-core design
  - 32KB L1 cache per core
  - 512KB L2 cache
  - 256-bit vector unit

- Adaptive DVFS, operating voltage range: 0.6V ~ 1.05V

DDR Memory
~~~~~~~~~~~~

- Dual-chip optional: 32-bit LPDDR4/LPDDR4x SDRAM, up to 2666 Mbps, maximum 16GB RAM
- Dual-chip optional: 32-bit LPDDR3 SDRAM, up to 1866 Mbps, maximum 4GB RAM

RCPU (Real-Time CPU)
~~~~~~~~~~~~~~~~~~~~~~

- 256KB SRAM ×1
- R_CAN-FD ×1
- R_I2C ×1
- R_SPI ×2
- HDMI Audio
- R_Debug
- R_UART ×2
- R_PWM ×10
- DMA ×1
- R_IR_RX ×1

Peripheral Controller
~~~~~~~~~~~~~~~~~~~~~~~

- GPIO (×128)
  - 128 configurable pins
  - Programmable pull-up / pull-down
  - 104 × 1.8V IO
  - 24 × 1.8V / 3.3V multi-level IO

- UART (×10)
  - For AP, Bluetooth and printing debugging

- I2C (×10)
  - Applicable to camera, G-sensor, electronic compass, proximity sensor, ambient light sensor, gyroscope, fingerprint module, NFC, PMIC, touch panel and other peripherals
  - 8 × AP_I2C (AP I2C0/1/7 dedicated for cameras) + 1 × HDMI I2C + 1 × Power I2C

- SPI (×4)
  - Support master and slave modes
  - For IMU, audio codec and other devices
  - Onboard 4 SPI interfaces (1 × QSPI, 1 × SPI LCD, 2 × general SPI)

- USB (×3)
  - USB 2.0 OTG
  - USB 2.0 Host
  - USB 3.0 (multiplexed with PCIE PortA)

- PCIE (×3)
  - PCIE PortA Gen2×1
  - PCIE PortB Gen2×2
  - PCIE PortC Gen2×2

- GMAC (×2)
  - 10/100/1000 Mbps adaptive
  - RGMII interface

- SDIO (×1 for Wi-Fi)
  - Compliant with 4-bit SDIO 3.0 UHS-I, up to SDR104 (208MHz)

- SD (×1 for TF Card)
  - Compliant with 4-bit SD 3.0 UHS-I, up to SDR104 (208MHz)

- eMMC (×1)
  - Compliant with 8-bit eMMC 5.1, up to HS400 (200MHz)

- MIPI CSI (CSI-2 v1.1) 4-Lane (×2)
  - 4-Lane + 4-Lane mode
  - 4-Lane + 2-Lane mode
  - 4-Lane + 2-Lane + 2-Lane triple-camera mode

- MIPI DSI (DSI v1.1) (×1)
  - 4-Lane DSI

- PWM ×20
- CAN-FD ×1
- IR Receiver ×1

- Security System
  - RISC-V PMP memory protection
  - Secure Boot
  - 4K-bit secure eFuse
  - Hardware crypto engine (TRNG, AES, RSA, ECC, SHA2, HMAC)

- Debug System
  - Dual JTAG for CPU and MCU subsystems
  - Multi-channel UART debug
  - CPU/IO register snapshot after watchdog reset

- Boot System
  - Primary AP boot support: SPI-NAND / SPI-NOR Flash / eMMC / SD card
  - 128KB built-in Boot ROM

- Auxiliary System
  - Independent watchdog for each CPU/MCU subsystem

- Operating Temperature
  - -40°C ~ +85°C (Industrial grade)

3. Multimedia Features
------------------------

GPU
~~~~~

- IMG BXE-2-32 @ 819MHz, 32KB SLC
- Support OpenCL 3.0 / OpenGL ES 3.2 / Vulkan 1.3

VPU (Video Processing Unit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Decoder: H.265/H.264/VP8/VP9/MPEG4/MPEG2, 4K@60fps
Encoder: H.265/H.264/VP8/VP9, 4K@30fps
Simultaneous 1080P@60fps encoding & decoding
Concurrent tasks: 1080P@30fps H.264/H.265 encoding + 4K@30fps H.264/H.265 decoding

Display
~~~~~~~~~

- 1 MIPI DSI-4 lane or SPI interface
- Support for up to Full HD (1920x1080@60fps)
- Support for up to 4-full-size-layer composer and maximum 8-layer composer by up-down layer reuse in RDMA channel
- Support for cmdlist mechanism which can configure register parameters by hardware
- Support for concurrent write-back with both raw and AFBC format
- Support for dither/crop/rotation in write-back path
- Support for an advanced MMU (virtual address) mechanism with nearly no page missing in 90/270 degree rotation
- Support for color key and solid color
- Support for both advanced error diffusion and pattern based dither for panel
- Support for both raw and AFBC format image source
- Support for color saturation/contrast enhancement
- Support for both video mode and cmd mode for panel
- Support for DDR frequency dynamic changing with embedded DFC buffer
- HDMI 1.4

Camera
~~~~~~~~

- Dual-ISP
  - 16M (max) 30fps Dual ISP
  - One 4-Lane CSI + one 4-Lane CSI, or 4-Lane + 2-Lane + 2-Lane
  - RAW sensor, output YUV data to DRAM
  - Hardware JPEG encoder, supporting up to 23M
  - Support for YUV/EXIF/JFIF format
  - AF/AE/AWB
  - Face detection
  - Digital zoom, panorama view
  - PDAF
  - PiP (Picture-in-Picture)
  - Continuous video AF
  - HW 3D denoise

Audio
~~~~~~~

- 2 × Full-duplex I2S
- 1 × HDMI Audio interface

4. Application Scenarios
--------------------------

- Widely applied in industrial gateways, robots, Hongmeng OS tablets and other products; capable of complex tasks such as 3D spatial computing and voice recognition

5. Block Diagram
------------------

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/产品简介2.png
   :alt: 产品简介2.png
   :width: 60%
