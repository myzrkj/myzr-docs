MYZR-SSD2351-EK112 Hardware Manual
======================================

Precautions and Maintenance 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1、Precautions
----------------

- Do not plug or unplug peripheral modules while the power is on! 
- Please follow all warnings and instructions marked on the product.
- Please keep this product dry. If it is accidentally splashed or soaked by any liquid, immediately cut off the power and let it dry thoroughly.
- During use, pay attention to the ventilation and heat dissipation of this product to avoid damage to components caused by excessive temperature. 
- Do not use or store this product in a dusty or dirty environment. 
- Do not apply this product in environments with alternating hot and cold conditions to avoid condensation that may damage components. 
- Please do not treat this product roughly. Dropping, hitting, or shaking it violently may damage the circuits and components.
- Do not use organic solvents or corrosive liquids to clean this product. 
- Do not repair or disassemble our company's products by yourself. If the product malfunctions, please contact our company promptly for repair. 
- Unauthorized modification or use of unauthorized accessories may damage this product, and damage caused thereby will not be covered by the warranty.

2、After-sales repair
------------------------

|  If hardware malfunctions occur during the use of the product, repairs can be carried out in accordance with the after-sales services policy; 
|  Service Policy: Refer to the official website http://wiki.myzr.com.cn/ for after-sales services instructions;
|  Address: 4th Floor, Overseas Science and Technology Park, No. 20, Science and Technology 1st Road, Science and Technology Innovation Coast, Tangjiawan Town, High-tech Zone, Zhuhai City, Guangdong Province
|  Contact: After-sales Maintenance Department
|  Phone: 0756-3628023 Zip Code: 519020
|  Shipping Instructions: It is recommended to use SF Express, YTO Express, or Yunda Express, and no cash on delivery is accepted. 

Technical Support and Customization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1、Technical Support Scope
-----------------------------

|  Consultation on the provision of software and hardware resources of the company's products;
|  Problems encountered during the use of the software and hardware manuals for the company's products;
|  OEM and ODM after-sales technical support provided by our company;
|  Fault diagnosis and after-sales repair services for the company's products; 

2、Scope of technical discussion
-----------------------------------

|  Modification and understanding of source code;
|  How to port an operating system; 
|  Hardware and software issues encountered by users during self-modification and development;
|  Note: Although the above three points are not within the scope of technical support, our company will do its best to assist users. If your issue still cannot be resolved, we sincerely ask for your understanding;

3、Technical Support Methods
-------------------------------

|  Telephone: 0756-3628023/3628021
|  Forum: http://bbs.myzr.com.cn/forum.php
|  Email: service@myzr.com.cn

4、Technical Support Hours
-----------------------------

|  Monday to Friday: 8:30 AM - 11:30 AM, 1:30 PM - 6:00 PM;
|  The company will take a break according to the national legal holidays, during which technical support cannot be provided. During this period, please send emails or post in the technical support section of the forum. 
|  We will reply to you as soon as possible on working days.

Data Update and Acquisition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1、Update of materials
-------------------------

|  Product-related materials will be continuously improved and updated, including the content of this manual; when you use these materials, please ensure they are in the latest state;

2、How to be notified after the update
-----------------------------------------

|  The notice on the update of Mingyuan Zhirui embedded product information will be pushed via the WeChat official account. Please follow it! 

3、How to obtain the materials
---------------------------------

|  Network Download:
|  Please register and log in `http://wiki.myzr.com.cn <http://wiki.myzr.com.cn>`_ , find "Development Board Data Download", select the corresponding platform, and download.



Copyright Notice
~~~~~~~~~~~~~~~~~~~

|  The copyright of this manual belongs to Zhuhai Mingyuan Zhirui Technology Co., Ltd. Without the written permission of the company, no unit or individual has the right to reproduce, disseminate, or reprint any part of this manual in any form, and violators will be held legally liable. 


Chapter 1 Introduction to MYZR-SSD2351-CB112 Core Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.1 Introduction to the Core Board
-------------------------------------

CPU Performance
^^^^^^^^^^^^^^^^^

1. Processor Core
""""""""""""""""""""

- ARM Cortex-A35 Quad-Core
- Each core: 32KB L1 instruction cache + 32KB L1 data cache
- 256KB L2 cache
- Supports Neon and FPU (Floating Point Unit)
- Independent power domain for each core
- 0.5 TOPS computing power
- Main frequency up to 1.4GHz

2. Intelligent Video Engine (IVE)
""""""""""""""""""""""""""""""""""""

- pure hardware accelerator
- Supports image processing operations: Filter2D, Box filter, Gaussian filter, Bernsen, Dilate, Erode, etc.
- Supports matrix multiplication

3. Intelligent Processing Unit (IPU)
"""""""""""""""""""""""""""""""""""""""

- pure hardware accelerator
- Programmable 4/8/16-bit processing 
- R/W DMA supporting RGB/YUV data formats 
- Supports multiple video analysis functions: face detection/recognition (FD/FR), human body detection, motion detection/object detection (MD/OD), object tracking, etc.
- Supports Transformer network

4. Audio Processor
"""""""""""""""""""""

- Supports 3-channel ADC (single-ended or differential mode) 
- Supports 2-channel DAC (single-ended mode) 
- The signal to noise ratio (SNR) of ADC and DAC exceeds 95.2dB 
- Supports digital and analog gain adjustment
- Supports 8-channel DMIC (1 clock + 4 data)
- Supports TDM mode (1250/1/2), with a maximum of 8 input channels and 2 output channels 
- Supports SPDIF input

5. Video output interface
""""""""""""""""""""""""""""

- Image Quality Enhancement (gamma, sharpness, brightness, 3x3 matrix, color dithering, OSD, RGB swap) 
- The display channel supports MIPI/digital port output, and the digital ports include TTL/18080 
- Supports MIPI DSI TX, 2.5Gbps per channel, RGB 16/18/24 bits, resolution 2560x1600@60fps
- TTL/Parallel RGB interface, 16/18/24-bit, resolution 1280x800@60fps
- Supports 8/16-bit 18080 interface
- Supports MIPI CSI

6. Advanced Color Engine
"""""""""""""""""""""""""""

- Brightness Gain/Offset Adjustment 
- Black/White Level Expansion (BLE/WLE)
- Peak/Low-pass Filtering/Chromaticity Correction/Denoising

7. SPI NOR/NAND Flash Interface 
"""""""""""""""""""""""""""""""""""

- Compatible with standard, dual-channel, and quad-channel SPI flash components 
- Maximum clock frequency 108MHz
- Supports power-off protection

8. SD/eMMC Interface
"""""""""""""""""""""""

- Compliant with SD 2.0 specification, supports 1/4-bit data bus mode
- Compatible with SDIO 2.0 specification, supports 1/4-bit data bus mode 
- Supports eMMC 5.0, 4/8-bit data bus, maximum clock frequency 200MHz, HS400 DDR mode 

9. USB Interface
"""""""""""""""""""

- USB 2.0 Port 0 can be configured as a host or a device
- USB 2.0 Port 1 can be configured as a host or a device (host mode supports the EHC1 specification)

10. DRAM Memory
"""""""""""""""""""

- Built-in 16-bit x1 DDR3/L, 128MB capacity
- Data rate up to 2133Mbps (DDR3/L) 

11. Network Connection
"""""""""""""""""""""""""

- Built-in two 10/100M Ethernet MACs, supporting RMII interface 
- 256-entry hash table
- Supports broadcast/multicast storm prevention 
- Supports full-duplex and half-duplex operation 
- Supports IEEE 802.1Q VLAN tag detection 
- Supports IPv4 header checksum and TCP, UDP, or ICMP checksum verification

12. Security Engine
""""""""""""""""""""""

- Supports AES128/AES192/AES256/DES/3DES/RSA4096/SHA-1/SHA-256/SM2/SM3/SM4 encryption algorithms 
- Supports Secure Boot 
- Random number generator compliant with FIPS 140-1 standard
- Built-in OTP (One-Time Programmable) memory for storing security data and calibration data 

13. Startup Options
""""""""""""""""""""""

- SPI NOR
- SPI NAND（带ECC）
- SD card
- eMMC
- USB
- UART

14. Peripheral Interface
"""""""""""""""""""""""""""

- Dedicated GPIO is used for system control 
- Supports 8-channel PWM input and 13-channel PWM output (shared with GPIO)
- Supports QSPI Interface 
- Up to 6 general-purpose UARTs and 4 fast UARTs with flow control
- Up to 12 general-purpose timers and 1 watchdog timer
- Two SPI interfaces, configurable as master or slave mode 
- Two SPI interfaces in host-only mode 
- Up to 6 I2C master controllers
- Built-in 10-bit SAR ADC, 1 channel
- Supports 7x7 keyboard
- Supports IrDA
- Supports POR (Power-On Reset) 
- Supports internal temperature sensor

**Front of the core board**

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/核心板正面.png
   :alt: 核心板正面.png
   :width: 50%

**Back of the core board**

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/核心板背面.png
   :alt: 核心板背面.png
   :width: 50%

1.2 1.2 Core Board Structural Parameters
-------------------------------------------

**Core board structural parameters**

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/核心板结构参数.png
   :alt: 核心板结构参数.png
   :width: 50%


|  Structural Dimensions: 26mm×26mm square stamp hole PCB, with a total of 112 pins and a pitch of 0.98mm. 
|  Manufacturing Process: 4-layer full through-hole process 
|  Surface Process: Immersion Gold Process


1.3 Core Board Configuration Resources
------------------------------------------

Model Analysis
^^^^^^^^^^^^^^^^

|  Example：MYZR-SSD2351-CB112-256-256
|  MYZR-SSD2351: Core board model
|  CB: Core Board; MB: Baseplate; EK: Development Board (including Core Board and Baseplate)
|  112: Number of pins on the core board
|  256 (256M, 128M): Core board memory
|  256: Core board storage, 256M

Order Information
^^^^^^^^^^^^^^^^^^^

|  This table is an example of core board specifications and models, but does not include all possible specifications. The latest specifications and models can be found in the latest product hardware manual. If the specifications you need are not listed in the table, or if you have questions about the specifications, please refer to `http://wiki.myzr.com.cn <http://wiki.myzr.com.cn>`_ or contact your Mingyuan Zhirui sales representative. 

Power Supply Mode
^^^^^^^^^^^^^^^^^^^^

+--------------+-----------+---------------+---------+---------+------+--------------------------+
| Function     | Pin Label | specification                            | Description              |
+              +           +---------------+---------+---------+------+                          +
|              |           | Minimum       | Typical | Maximum | unit |                          |
+--------------+-----------+---------------+---------+---------+------+--------------------------+
| Power Supply | 5V_core   | 3.14          | 3.3     | 3.46    | V    | Powered by the baseplate |
+--------------+-----------+---------------+---------+---------+------+--------------------------+

Working Environment
^^^^^^^^^^^^^^^^^^^^^

+-----------------------+---------------+---------+---------+------+------------------------------------------------------------+-----+
| Parameter             | Specification                            | Description                                                |     |
+                       +---------------+---------+---------+------+                                                            +-----+
|                       | Minimum       | Typical | Maximum | Unit |                                                            |     |
+-----------------------+---------------+---------+---------+------+------------------------------------------------------------+-----+
| Operating Temperature | -20           | 25      | 70      | ℃    | Actual measurement shows normal operation from -20 to 70°C |     |
+-----------------------+---------------+---------+---------+------+------------------------------------------------------------+-----+

Core board interface resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
| Function                   |          | Quantity | Parameter                                                                                                                     |
+----------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
| Communication Interface    | Ethernet | 2        | 2-channel 10/100Mbps Ethernet, with built-in 10/100M Ethernet physical layer, supporting 1 RMII connection to an external PHY |
+                            +----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
|                            | USB      | 2        | 2-channel USB2.0 HOST                                                                                                         |
+                            +----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
|                            | UART     | 6        | Up to 6 general-purpose UARTs and 4 fast UARTs with flow control                                                              |
+                            +----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
|                            | I2C      | 6        | Supports 6-channel I2C interface                                                                                              |
+                            +----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
|                            | SPI      | 6        | 5-channel SPI controller                                                                                                      |
+                            +----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
|                            | ADC      | 1        | Supports 1-channel ADC interface                                                                                              |
+                            +----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
|                            | PWM      | 13       | Supports 8-channel PWM input and 13-channel PWM output (shared with GPIO)                                                     |
+                            +----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
|                            | I2S      | 3        | Supports 3 channels of 12S interface                                                                                          |
+----------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
| External Storage Interface | SDIO     | 1        | 1-channel SDIO                                                                                                                |
+----------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
| Multimedia                 | MIPI_DSI | 1        | Supports 1-channel DSI_MIPI interface                                                                                         |
+                            +----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
|                            | MIPI_CSI | 1        | Supports 1-channel CSI_MIPI interface                                                                                         |
+                            +----------+----------+-------------------------------------------------------------------------------------------------------------------------------+
|                            | RGB      | 1        | Supports 1-channel RGB interface                                                                                              |
+----------------------------+----------+----------+-------------------------------------------------------------------------------------------------------------------------------+

|  Chapter 2 Introduction to MYZR-SSD2351-MB112 Embedded Development Platform

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/主板背面.png
   :alt: 主板背面.png
   :width: 50%


Chapter 2 Introduction to MYZR-SSD2351-MB112 Embedded Development Platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.1 Introduction to the Development Platform Hardware
--------------------------------------------------------

2.1.1 Introduction to Baseplate Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  The Mingyuan Zhirui MYZR-SSD2351-MB112 development platform adopts a structure of a stamp-hole core board + baseplate, where the 112 in its name refers to the number of pins on the core board rather than the CPU suffix. The main interfaces of the development board are shown in the following figure: 

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/主板正面A.png
   :alt: 主板正面A.png
   :width: 50%

2.1.2 Baseplate Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/底板尺寸.png
   :alt: 底板尺寸.png
   :width: 50%

|  Structural Dimensions: 94mm×51mm rectangular PCB. 
|  Platemaking process: 1.6mm thick, 4-layer PCB, black.

2.1.3 Baseplate Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------+--------------------------------+---------------------------------------+------------+
| Interface    | Function                       | Interface form                        | Silkscreen |
+==============+================================+=======================================+============+
| Type-C       | Power Input/System Upgrade OTG | Type-C                                | U24        |
+--------------+--------------------------------+---------------------------------------+------------+
| Ethernet     | Ethernet 10/100Mbps            | RJ45                                  | CONR1      |
+--------------+--------------------------------+---------------------------------------+------------+
| DEBUG UART   | Debug Serial Port              | PH1.25 Female Header (3 Pins)         | J3         |
+--------------+--------------------------------+---------------------------------------+------------+
| 40pin        | Function Reuse Pin             | 2.54 Pin Header                       | J4         |
+--------------+--------------------------------+---------------------------------------+------------+
| 18pin        | Function Reuse Pin             | 2.54 Pin Header                       | J19        |
+--------------+--------------------------------+---------------------------------------+------------+
| TF           | TF Card                        | Standard TF Card Self-Ejecting Socket | J12        |
+--------------+--------------------------------+---------------------------------------+------------+
| USB          | USB2.0 HOST                    | USB_A                                 | J16        |
+--------------+--------------------------------+---------------------------------------+------------+
| LCD          | LCD MIPI                       |                                       | J17        |
+--------------+--------------------------------+---------------------------------------+------------+
| Antenna      | WIFI&Bluetooth                 | IPX Connector                         | U12        |
+--------------+--------------------------------+---------------------------------------+------------+
| Reset Button | Reset                          | Lightly touch the push-button switch  | RESET2     |
+--------------+--------------------------------+---------------------------------------+------------+
| BOOT MODE    | Startup Mode Selection         | DIP Switch (3-bit)                    | SW1        |
+--------------+--------------------------------+---------------------------------------+------------+


2.2 Design Description of Baseplate Schematic Diagram
-------------------------------------------------------

2.2.1 Main Power Supply Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  The baseplate power is supplied by a DC 5V power source, introduced via the Type-C socket (U24). 

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/底板电源.png
   :alt: 底板电源.png
   :width: 90%

|  The 5V power supply is split into two 3.3V outputs by the power IC to supply power to the core and other devices respectively. 

**BOOT Mode**

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/boot_mode.png
   :alt: boot_mode.png
   :width: 90%

|  When the core board starts, it needs to first read the BOOT mode (see the schematic diagram for specific BOOT startup modes). 

2.2.2 Reset Circuit
^^^^^^^^^^^^^^^^^^^^^

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/复位电路.png
   :alt: 复位电路.png
   :width: 90%

|  This development board only uses the RESET22 reset switch shown in the figure. 

2.2.3 External TF Card Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/外接TF卡电路.png
   :alt: 外接TF卡电路.png
   :width: 90%

|  The TF card circuit uses the SDIO bus interface. 
|  Note: During PCB design, equal-length processing must be performed, a 3W spacing is required, and overall ground wrapping must be done.

2.2.4 Ethernet Interface Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/以太网接口电路.png
   :alt: 以太网接口电路.png
   :width: 90%

|  There is no network port chip in the core board; the network port chip is on the baseplate. It should be noted that the two indicator lights of the RJ45 interface need to be designed according to this schematic diagram. 
|  Note: During PCB design, the 4 sets of Ethernet signal lines need to be routed according to differential rules and have equal lengths within the differential pairs, and the differential pairs should maintain a spacing of at least 3 times the line width from other networks; the equal-length error range within the differential pairs is required to be within 5 mils, and the equal-length error range between differential pairs is required to be within 25 mils.

2.2.5 DownLoad Burning System USB Port Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/USB口电路.png
   :alt: USB口电路.png
   :width: 90%

|  This interface is a Type-C interface, used to connect to the host PC for burning the system to this development board. The USB cable requires differential routing. 

2.2.6 USB HOST电路
^^^^^^^^^^^^^^^^^^^^

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/USB_HOST电路.png
   :alt: USB_HOST电路.png
   :width: 90%

|  During PCB design, each group of USB signal lines needs to be routed according to differential rules and have equal lengths within the differential pair. The differential pair should maintain a spacing of at least 3 times the line width from other networks, and the equal length error within the differential pair is required to be within 5 mils. 
|  When designing a PCB, the traces of the chip power supply network should be thickened, and the power decoupling capacitors should be placed close to the chip pins; the crystal oscillator should be placed close to the chip, the crystal oscillator network should be kept as far away from other signal lines as possible and be surrounded by ground, and the area around the crystal oscillator itself should also be surrounded by ground. 

2.2.7 WIFI
^^^^^^^^^^^^

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/wifi.png
   :alt: wifi.png
   :width: 90%

|  During PCB design, the network group is required to have equal-length traces, the trace spacing must meet the requirements of the 3W rule, and the entire group should be grounded; the network where the antenna interface U12 is located in the figure requires traces to meet the 50Ω impedance design, with traces as short as possible and no sharp corners, and the surrounding area should be grounded to avoid signal interference.

2.2.8 Debug Port
^^^^^^^^^^^^^^^^^^^

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2351/Debug调试口电路.png
   :alt: Debug调试口电路.png
   :width: 90%

|  The J3 interface is the Debug port of the development board. 
|  When designing a PCB, traces should be routed in groups to avoid excessive length errors between two nets within the group when the traces are too long. 