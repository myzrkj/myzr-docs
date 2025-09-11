MYZR-SSD2351-EK112 Hardware Manual
====================================

Precautions and Maintenance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Precautions
----------------

- Do not hot-swap peripheral modules!
- Please follow all warning and guidance information marked on the product.
- Keep this product dry. If it is accidentally splashed or soaked by any liquid, please power off immediately and dry it thoroughly.
- Pay attention to the ventilation and heat dissipation of the product during use to avoid damage to components due to excessive temperature.
- Do not use or store this product in a dusty or dirty environment.
- Do not use or store this product in an environment with alternating hot and cold temperatures to avoid condensation damage to components.
- Do not rough handle this product; dropping, hitting, or剧烈 shaking may damage circuits and components.
- Do not clean this product with organic solvents or corrosive liquids.
- Do not repair or disassemble the company's products by yourself. If the product malfunctions, please contact the company for repair in a timely manner.
- Unauthorized modification or use of unauthorized accessories may damage this product, and the resulting damage will not be covered by the warranty.

2. After-sales Repair
-----------------------

| If hardware failures occur during the use of the product, repair can be carried out in accordance with the after-sales service policy;
| Service policy: Refer to the after-sales service instructions on the official website http://wiki.myzr.com.cn/;
| Address: 4th Floor, Overseas Sea Science and Technology Park, No. 20, Keji 1st Road, Science and Technology Innovation Coast, Tangjiawan Town, Gaoxin District, Zhuhai City, Guangdong Province
| Contact person: After-sales Repair Department
| Phone: 0756-3628023 Zip code: 519020
| Mailing instructions: It is recommended to use SF Express, Yuantong, or Yunda, and no cash on delivery is accepted.

Technical Support and Customization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Scope of Technical Support
--------------------------------

| Consultation on the provision of software and hardware resources of the company's products;
| Problems encountered during the use of the software and hardware manuals of the company's products;
| After-sales technical support for OEM and ODM provided by the company;
| Fault judgment and after-sales repair services for the company's products;

2. Scope of Technical Discussion
----------------------------------

| Modification and understanding of source code;
| How to port the operating system;
| Software and hardware problems encountered by users during self-modification and development;

| Note: Although the above three points are not within the scope of technical support, our company will try its best to provide help to users. If your problem still cannot be solved, please understand;

3. Technical Support Methods
-------------------------------

| Phone: 0756-3628023/3628021
| Forum: `http://bbs.myzr.com.cn/forum.php <http://bbs.myzr.com.cn/forum.php>`_
| Email: service@myzr.com.cn

4. Technical Support Time
---------------------------

| Monday to Friday: 8:30—11:30 am, 13:30—18:00 pm;
| The company rests in accordance with national statutory holidays. During this period, technical support cannot be provided. Please send an email or go to the technical support area of the forum during this period,
| We will reply to you as soon as possible on working days.

Data Update and Acquisition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Data Update
----------------

| Product-related data will be continuously improved and updated, including the content of this manual; when you use this content, please ensure that it is up-to-date;

2. How to Be Notified After Update
------------------------------------

| Mingyuan Zhirui embedded product data update notifications are pushed through the WeChat official account, please follow it!

3. How to Obtain Data
-----------------------

| Network download:
| Please register and log in to `http://wiki.myzr.com.cn <http://wiki.myzr.com.cn>`_, find "Development Board Data Download", and select the corresponding platform to download.

Copyright Notice
~~~~~~~~~~~~~~~~~~

| The copyright of this manual belongs to Zhuhai Mingyuan Zhirui Technology Co., Ltd. Without the written permission of the company, no unit or individual has the right to copy, disseminate, or reprint any part of this manual in any form, and violators will be held legally responsible.

Chapter 1 Introduction to MYZR-SSD2351-CB112 Core Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.1 Core Board Introduction
------------------------------

CPU Performance
^^^^^^^^^^^^^^^^^

1. Processor Core
""""""""""""""""""""

- ARM Cortex-A35 quad-core
- Each core: 32KB L1 instruction cache + 32KB L1 data cache
- 256KB L2 cache
- Supports Neon and FPU (Floating Point Unit)
- Independent power domain for each core
- 0.5 TOPS computing power
- Maximum frequency up to 1.4GHz

2. Intelligent Video Engine (IVE)
"""""""""""""""""""""""""""""""""""

- Pure hardware accelerator
- Supports image processing operations: Filter2D, Box filter, Gaussian filter, Bernsen, Dilate, Erode, etc.
- Supports matrix multiplication

3. Intelligent Processing Unit (IPU)
""""""""""""""""""""""""""""""""""""""

- Pure hardware accelerator
- Programmable 4/8/16-bit processing
- Supports R/W DMA for RGB/YUV data formats
- Supports multiple video analysis functions: face detection/recognition (FD/FR), human detection, motion detection/object detection (MD/OD), object tracking, etc.
- Supports Transformer network

4. Audio Processor
"""""""""""""""""""

- Supports 3-channel ADC (single-ended or differential mode)
- Supports 2-channel DAC (single-ended mode)
- The signal-to-noise ratio (SNR) of ADC and DAC exceeds 95.2dB
- Supports digital and analog gain adjustment
- Supports 8-channel DMIC (1 clock + 4 data)
- Supports TDM mode (1250/1/2), maximum 8 input channels, 2 output channels
- Supports SPDIF input

5. Video Output Interface
"""""""""""""""""""""""""""

- Image quality enhancement (gamma, sharpness, brightness, 3x3 matrix, color dithering, OSD, RGB swapping)
- Display channel supports MIPI/digital port output, digital ports include TTL/18080
- Supports MIPI DSI TX, 2.5Gbps per channel, RGB 16/18/24 bits, resolution 2560x1600@60fps
- TTL/parallel RGB interface, 16/18/24 bits, resolution 1280x800@60fps
- Supports 8/16-bit 18080 interface
- Supports MIPI CSI

6. Advanced Color Engine
""""""""""""""""""""""""""

- Brightness gain/offset adjustment
- Black and white level expansion (BLE/WLE)
- Peak/low-pass filtering/chromaticity correction/denoising

7. SPI NOR/NAND Flash Interface
"""""""""""""""""""""""""""""""""

- Compatible with standard, dual-channel, and quad-channel SPI flash components
- Maximum clock frequency 108MHz
- Supports power-off protection

8. SD/eMMC Interface
""""""""""""""""""""""

- Compatible with SD 2.0 specification, supports 1/4-bit data bus mode
- Compatible with SDIO 2.0 specification, supports 1/4-bit data bus mode
- Supports eMMC 5.0, 4/8-bit data bus, maximum clock frequency 200MHz, HS400 DDR mode

9. USB Interface
""""""""""""""""""

- USB2.0 port 0 can be configured as host or device
- USB2.0 port 1 can be configured as host or device (host mode supports EHC1 specification)

10. DRAM Memory
"""""""""""""""""

- Built-in 16-bit x1 DDR3/L, 128MB capacity
- Data rate up to 2133Mbps (DDR3/L)

11. Network Connection
""""""""""""""""""""""""

- Built-in two 10/100M Ethernet MACs, supporting RMII interface
- 256-entry hash table
- Supports broadcast/multicast storm prevention
- Supports full-duplex and half-duplex operations
- Supports IEEE 802.1Q VLAN tag detection
- Supports IPv4 header checksum and TCP, UDP, or ICMP checksum checking

12. Security Engine
"""""""""""""""""""""

- Supports AES128/AES192/AES256/DES/3DES/RSA4096/SHA-1/SHA-256/SM2/SM3/SM4 encryption algorithms
- Supports secure boot
- Random number generator compliant with FIPS 140-1 standard
- Built-in OTP (One-Time Programmable) memory for storing security data and calibration data

13. Boot Options
""""""""""""""""""

- SPI NOR
- SPI NAND (with ECC)
- SD card
- eMMC
- USB
- UART

14. Peripheral Interfaces
"""""""""""""""""""""""""""

- Dedicated GPIO for system control
- Supports 8-channel PWM input and 13-channel PWM output (shared with GPIO)
- Supports QSPI interface
- Up to 6 general-purpose UARTs and 4 fast UARTs with flow control
- Up to 12 general-purpose timers and 1 watchdog timer
- Two SPI interfaces, configurable as master or slave mode
- Two SPI interfaces in master-only mode
- Up to 6 I2C master controllers
- Built-in 10-bit SAR ADC, 1 channel
- Supports 7x7 keyboard
- Supports IrDA
- Supports POR (Power-On Reset)
- Supports internal temperature sensor

**Core Board Front**

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/核心板正面.png
   :alt: 核心板正面.png
   :width: 50%

**Core Board Back**

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/核心板背面.png
   :alt: 核心板背面.png
   :width: 50%

1.2 Core Board Structural Parameters
--------------------------------------

**Core Board Structural Parameters**

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/核心板结构参数.png
   :alt: 核心板结构参数.png
   :width: 50%


| Structural size: 26mm×26mm square stamp hole PCB, total 112 pins, pitch 0.98mm.
| Manufacturing process: 4-layer through-hole process
| Surface process: Immersion gold process


1.3 Core Board Configuration Resources
----------------------------------------

Model Interpretation
^^^^^^^^^^^^^^^^^^^^^^

| For example: MYZR-SSD2351-CB112-256-256
| MYZR-SSD2351: Core board model
| CB: Core board; MB: Base board; EK: Development board (including core board and base board)
| 112: Number of core board pins
| 256 (256M, 128M): Core board memory
| 256: Core board storage, 256M

Ordering Information
^^^^^^^^^^^^^^^^^^^^^^^

| This table is an example of core board specifications and models, but does not include all possible specifications. The latest specifications and models can be found in the latest product hardware manual. If the specification you need is not in the table, or if you have questions about the specifications, please refer to http://wiki.myzr.com.cn or contact your Mingyuan Zhirui sales representative.

Power Supply Mode
^^^^^^^^^^^^^^^^^^^

+--------------+-----------+---------------+-----+------+------+-----------------------+
| Function     | Pin Label | Specification                     | Description           |
+              +           +---------------+-----+------+------+                       +
|              |           | Min           | Typ | Max  | Unit |                       |
+--------------+-----------+---------------+-----+------+------+-----------------------+
| Power Supply | 5V_core   | 3.14          | 3.3 | 3.46 | V    | Powered by base board |
+--------------+-----------+---------------+-----+------+------+-----------------------+

Working Environment
^^^^^^^^^^^^^^^^^^^^^

+-----------------------+---------------+-----+-----+------+----------------------------------------+
| Parameter             | Specification                    | Description                            |
+                       +---------------+-----+-----+------+                                        +
|                       | Min           | Typ | Max | Unit |                                        |
+-----------------------+---------------+-----+-----+------+----------------------------------------+
| Operating Temperature | -20           | 25  | 70  | ℃    | Tested to run normally from -20 to 70℃ |
+-----------------------+---------------+-----+-----+------+----------------------------------------+

Core Board Interface Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------+----------+-----------+----------------------------------------------------------------------------------------------------------------------+
| Function                    | Quantity | Parameter |                                                                                                                      |
+-----------------------------+----------+-----------+----------------------------------------------------------------------------------------------------------------------+
| Communication Interfaces    | Ethernet | 2         | 2 channels of 10/100Mbps Ethernet, built-in 10/100M Ethernet physical layer, supports 1 RMII to connect external PHY |
+                             +----------+-----------+----------------------------------------------------------------------------------------------------------------------+
|                             | USB      | 2         | 2 channels of USB2.0 HOST                                                                                            |
+                             +----------+-----------+----------------------------------------------------------------------------------------------------------------------+
|                             | UART     | 6         | Up to 6 general-purpose UARTs and 4 fast UARTs with flow control                                                     |
+                             +----------+-----------+----------------------------------------------------------------------------------------------------------------------+
|                             | I2C      | 6         | Supports 6 I2C interfaces                                                                                            |
+                             +----------+-----------+----------------------------------------------------------------------------------------------------------------------+
|                             | SPI      | 6         | 5 SPI controllers                                                                                                    |
+                             +----------+-----------+----------------------------------------------------------------------------------------------------------------------+
|                             | ADC      | 1         | Supports 1 ADC interface                                                                                             |
+                             +----------+-----------+----------------------------------------------------------------------------------------------------------------------+
|                             | PWM      | 13        | Supports 8 PWM inputs and 13 PWM outputs (shared with GPIO)                                                          |
+                             +----------+-----------+----------------------------------------------------------------------------------------------------------------------+
|                             | I2S      | 3         | Supports 3 I2S interfaces                                                                                            |
+-----------------------------+----------+-----------+----------------------------------------------------------------------------------------------------------------------+
| External Storage Interfaces | SDIO     | 1         | 1 SDIO                                                                                                               |
+-----------------------------+----------+-----------+----------------------------------------------------------------------------------------------------------------------+
| Multimedia                  | MIPI_DSI | 1         | Supports 1 DSI_MIPI interface                                                                                        |
+                             +----------+-----------+----------------------------------------------------------------------------------------------------------------------+
|                             | MIPI_CSI | 1         | Supports 1 CSI_MIPI interface                                                                                        |
+                             +----------+-----------+----------------------------------------------------------------------------------------------------------------------+
|                             | RGB      | 1         | Supports 1 RGB interface                                                                                             |
+-----------------------------+----------+-----------+----------------------------------------------------------------------------------------------------------------------+

| Note: The parameters in the table are hardware design or CPU theoretical values;

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/主板背面.png
   :alt: 主板背面.png
   :width: 50%


Chapter 2 Introduction to MYZR-SSD2351-MB112 Embedded Development Platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.1 Introduction to Development Platform Hardware
---------------------------------------------------

2.1.1 Introduction to Base Board Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Mingyuan Zhirui MYZR-SSD2351-MB112 development platform adopts a stamp hole core board + base board structure. The 112 in the name refers to the number of core board pins, not the CPU suffix. The main interfaces of the development board are as shown in the following figure:

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/主板正面A.png
   :alt: 主板正面A.png
   :width: 50%

2.1.2 Base Board Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/底板尺寸.png
   :alt: 底板尺寸.png
   :width: 50%

| Structural size: 94mm×51mm rectangular PCB.
| Manufacturing process: thickness 1.6mm, 4-layer PCB, black.

2.1.3 Base Board Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+------------+--------------------------------+--------------------------------+------------+
| Interface  |            Function            |         Interface Form         | Silkscreen |
+============+================================+================================+============+
| Type-C     | Power input/System upgrade OTG | Type-C                         | U24        |
+------------+--------------------------------+--------------------------------+------------+
| Ethernet   | Ethernet 10/100Mbps            | RJ45                           | CONR1      |
+------------+--------------------------------+--------------------------------+------------+
| DEBUG UART | Debug serial port              | PH1.25 pin header (3 pins)     | J3         |
+------------+--------------------------------+--------------------------------+------------+
| 40pin      | Multifunctional pins           | 2.54 pin header                | J4         |
+------------+--------------------------------+--------------------------------+------------+
| 18pin      | Multifunctional pins           | 2.54 pin header                | J19        |
+------------+--------------------------------+--------------------------------+------------+
| TF         | TF card                        | Standard TF card pop-up socket | J12        |
+------------+--------------------------------+--------------------------------+------------+
| USB        | USB2.0 HOST                    | USB_A                          | J16        |
+------------+--------------------------------+--------------------------------+------------+