.. raw:: html

   <style>
   h1 {
       color: green;
   }
   </style>

Hardware Development Guide
==========================

Development Board Schematic Design Description
------------------------------------------------------

Divided into sections by module, including module introduction, performance, specifications, parameters, and principles.

Schematic design considerations, CheckList.

PCB design considerations, CheckList.

ESD, EMC, EMI design considerations.

Power supply design: current loops, current levels.

Debug Circuit
-------------------

RV1126B UART Debug is defaulted to UART0_RX_M2/UART0_TX_M2 in the PMUIO0 domain, with a default baud rate of 1500000 bps.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/Debug电路.png
   :alt: Debug Circuit
   :width: 100%

UART Interface Usage Notes:

* The UART interface at the SoC end must match the IO level of the conversion chip or peripheral chip;

* For external USB-to-UART conversion chips, it is recommended to supply VCCIO from the PMUIO0_VCC3V3 power domain of the main board to avoid voltage backflow when the SOC is powered off;

* If UART Debug is required, it is recommended to reserve 2.54 pin headers or test points. The UART circuit is shown below. The series 510 ohm resistor must not be omitted, and a TVS tube should be added to enhance anti-static surge capability and prevent damage to chip pins during development.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/Debug电路_02.png
   :alt: Debug Circuit
   :width: 100%

* Alternatively, the CH340T chip can be used to convert to USB signal.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/Debug电路_03.png
   :alt: Debug Circuit
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/Debug电路_04.png
   :alt: Debug Circuit
   :width: 100%

Power Supply System
-------------------

The power supply design of MYZR-RV1126B-EK221 evaluation board is divided into the following parts:

1. Main power input: 12V input

2. PMIC power supply: AXP15060 PMIC is used to supply power to the core, DDR, and internal peripherals of the RV1126B chip

3. External power supply: Power supply for external peripherals such as Ethernet PHY, USB HUB, WiFi/BT module, etc.

4. IO power domain: Power supply for GPIO, UART, I2C, SPI and other interfaces

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/电源系统.png
   :alt: Power Supply System
   :width: 100%

Power Supply Design Considerations:

* The power supply sequence must comply with the requirements of the RV1126B chip datasheet;

* The input voltage of each power domain must be within the specified range;

* Appropriate decoupling capacitors should be placed near the power pins of the chip;

* The power supply path should be as short as possible to reduce noise interference;

* The power plane should be properly partitioned to avoid mutual interference between different power domains.

Reset Circuit
-------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/复位电路.png
   :alt: Reset Circuit
   :width: 100%

The reset circuit uses a dedicated reset chip to ensure reliable reset of the system. The reset signal is connected to the RESET_N pin of the RV1126B chip.

Reset Circuit Design Considerations:

* The reset signal must be kept low for at least 10ms to ensure proper reset of the chip;

* The reset circuit should have a pull-up resistor to ensure a stable high level during normal operation;

* A capacitor should be added to the reset pin to filter out noise interference.

Clock Circuit
-------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/时钟电路.png
   :alt: Clock Circuit
   :width: 100%

The clock circuit uses a 24MHz crystal oscillator as the main clock source. The RV1126B chip has an internal PLL that can generate various clock frequencies required by the system.

Clock Circuit Design Considerations:

* The crystal oscillator should be placed as close as possible to the clock pin of the chip;

* The ground plane under the crystal oscillator should be kept intact to reduce noise;

* Appropriate load capacitors should be used for the crystal oscillator;

* The clock trace should be properly shielded to avoid EMI interference.

DDR Memory
----------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/DDR内存.png
   :alt: DDR Memory
   :width: 100%

The MYZR-RV1126B-EK221 evaluation board uses DDR4 memory with a capacity of 2GB. The DDR4 chip is connected to the RV1126B chip through a 64-bit data bus.

DDR Memory Design Considerations:

* The DDR signal traces should be matched in length to ensure signal integrity;

* The DDR power supply should be properly decoupled to reduce noise;

* The DDR address and control signals should be placed close to the chip;

* The DDR data signals should be routed with proper impedance matching.

eMMC Storage
------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/eMMC存储.png
   :alt: eMMC Storage
   :width: 100%

The MYZR-RV1126B-EK221 evaluation board uses an eMMC chip with a capacity of 16GB as the main storage device. The eMMC chip is connected to the RV1126B chip through an 8-bit data bus.

eMMC Storage Design Considerations:

* The eMMC power supply should be properly filtered to reduce noise;

* The eMMC clock signal should be properly terminated;

* The eMMC data signals should be routed with proper impedance matching;

* The eMMC reset signal should be properly handled to ensure reliable operation.

Ethernet Interface
------------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/以太网接口.png
   :alt: Ethernet Interface
   :width: 100%

The MYZR-RV1126B-EK221 evaluation board has two Ethernet interfaces: one 100Mbps interface and one 1000Mbps interface. The Ethernet PHY chip is connected to the RV1126B chip through the RGMII interface.

Ethernet Interface Design Considerations:

* The Ethernet transformer should be placed close to the RJ45 connector;

* The Ethernet signal traces should be routed with proper impedance matching;

* The Ethernet power supply should be properly filtered;

* The Ethernet interface should be protected with TVS devices to enhance ESD protection.

USB Interface
-------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/USB接口.png
   :alt: USB Interface
   :width: 100%

The MYZR-RV1126B-EK221 evaluation board has two USB interfaces: one USB 2.0 interface and one USB 3.0 interface. The USB 3.0 interface is connected to the RV1126B chip through a USB 3.0 PHY chip.

USB Interface Design Considerations:

* The USB signal traces should be routed with proper impedance matching;

* The USB power supply should be properly filtered;

* The USB interface should be protected with TVS devices to enhance ESD protection;

* The USB 3.0 signal pairs should be routed as differential pairs with proper length matching.

SD Card Interface
-----------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/SD卡接口.png
   :alt: SD Card Interface
   :width: 100%

The MYZR-RV1126B-EK221 evaluation board has an SD card interface that supports SDHC cards. The SD card interface is connected to the RV1126B chip through the MMC interface.

SD Card Interface Design Considerations:

* The SD card signal traces should be routed with proper impedance matching;

* The SD card power supply should be properly filtered;

* The SD card interface should be protected with TVS devices to enhance ESD protection;

* The SD card clock signal should be properly terminated.

Audio Interface
---------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/音频接口.png
   :alt: Audio Interface
   :width: 100%

The MYZR-RV1126B-EK221 evaluation board has an audio interface that supports both input and output. The audio codec chip is connected to the RV1126B chip through the I2S interface.

Audio Interface Design Considerations:

* The audio signal traces should be kept away from high-speed signals to avoid interference;

* The audio power supply should be properly filtered to reduce noise;

* The audio ground should be properly separated from the digital ground;

* The audio interface should be protected with TVS devices to enhance ESD protection.

MIPI DSI Interface
------------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/MIPI_DSI接口.png
   :alt: MIPI DSI Interface
   :width: 100%

The MYZR-RV1126B-EK221 evaluation board has a MIPI DSI interface that supports high-resolution displays. The MIPI DSI interface is connected to the RV1126B chip through 4 data lanes.

MIPI DSI Interface Design Considerations:

* The MIPI DSI signal traces should be routed as differential pairs with proper length matching;

* The MIPI DSI power supply should be properly filtered;

* The MIPI DSI interface should be protected with TVS devices to enhance ESD protection;

* The MIPI DSI signal traces should be properly shielded to avoid EMI interference.

MIPI CSI Interface
------------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/MIPI_CSI接口.png
   :alt: MIPI CSI Interface
   :width: 100%

The MYZR-RV1126B-EK221 evaluation board has two MIPI CSI interfaces that support high-resolution cameras. Each MIPI CSI interface is connected to the RV1126B chip through 4 data lanes.

MIPI CSI Interface Design Considerations:

* The MIPI CSI signal traces should be routed as differential pairs with proper length matching;

* The MIPI CSI power supply should be properly filtered;

* The MIPI CSI interface should be protected with TVS devices to enhance ESD protection;

* The MIPI CSI signal traces should be properly shielded to avoid EMI interference.

UART Interface
--------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/UART接口.png
   :alt: UART Interface
   :width: 100%

The MYZR-RV1126B-EK221 evaluation board has multiple UART interfaces for debugging and communication. The UART interfaces are connected to the RV1126B chip through GPIO pins.

UART Interface Design Considerations:

* The UART signal traces should be routed with proper impedance matching;

* The UART power supply should be properly filtered;

* The UART interface should be protected with TVS devices to enhance ESD protection;

* The UART signal traces should be kept away from high-speed signals to avoid interference.

I2C Interface
-------------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/I2C接口.png
   :alt: I2C Interface
   :width: 100%

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Signal
     - Connection Type
     - Description (Chip Side)
   * - I2Cx_SCL
     - Direct Connection
     - I2C Clock
   * - I2Cx_SDA
     - Direct Connection
     - I2C Data Output/Input

I2C Interface Design Considerations:

* Adjust the corresponding power domain supply according to the IO level of the I2C peripheral. The levels must match;

* I2C signals SCL and SDA require external pull-up resistors. Choose resistors with different values according to the bus load. It is recommended to use 2.2-4.7kohm pull-up resistors.

* Device addresses on the I2C bus must not conflict. The pull-up power supply must match the GPIO power domain.

* When implementing board-to-board connections through connectors, it is recommended to series a resistor (between 22ohm-100ohm, depending on SI test requirements) and reserve TVS devices.

SPI
---

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;}
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* 统一宽度 */
       border-collapse: collapse;
       table-layout: auto;  /* 列宽自动分配 */
   }
   td {
       word-wrap: break-word;  /* 内容过长自动换行 */
   }
   </style>

.. list-table::
   :widths: auto
   :header-rows: 1

   * - SPI Number
     - Multiplexing Options
     - Multiplexing Power Domain
   * - SPI0
     - M0,M1,M2
     - M0:PMUIO0 M1:VCCIO4N
   * - SPI1
     - M0,M1,M2
     - M0:VCCIO6 M1:VCCIO3N

Adjust the corresponding power domain supply according to the IO level of the SPI peripheral. The levels must match. The matching design for SPI interface is shown in the following table:

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* 统一宽度 */
       border-collapse: collapse;
       table-layout: auto;  /* 列宽自动分配 */
   }
   td {
       word-wrap: break-word;  /* 内容过长自动换行 */
   }
   </style>

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Signal
     - Connection Type
     - Description (Chip Side)
   * - SPIx_CLK
     - Direct Connection
     - SPI Clock
   * - SPIx_MOSI
     - Direct Connection
     - SPI Data Output (Master)
   * - SPIx_MISO
     - Direct Connection
     - SPI Data Input (Master)
   * - SPIx_CS0
     - Direct Connection
     - SPI Chip Select 0
   * - SPIx_CS1
     - Direct Connection
     - SPI Chip Select 1

SPI Interface Design Considerations:

When implementing board-to-board connections through connectors, it is recommended to series a resistor (between 22ohm-100ohm, depending on SI test requirements) and reserve TVS devices.

According to the interface design differences, the usage rates of different SPI interfaces are as follows:

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* 统一宽度 */
       border-collapse: collapse;
       table-layout: auto;  /* 列宽自动分配 */
   }
   td {
       word-wrap: break-word;  /* 内容过长自动换行 */
   }
   </style>

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Interface
     - Maximum CLK Rate
   * - SPI1_M1
     - 50MHz
   * - SPI0_M0
     - 24MHz
   * - SPI0_M1/SPI0_M2 SPI1_M0/SPI1_M2
     - 20MHz

PWM
---

The RV1126B chip integrates 4 independent PWM controllers, supporting up to 28 PWM channels. PWM0 controller has 8 channels: PWM0_CH0~PWM0_CH7. PWM1 controller has 4 channels: PWM1_CH0~PWM1_CH3. PWM2 controller has 8 channels: PWM2_CH0~PWM2_CH7. PWM3 controller has 8 channels: PWM3_CH0~PWM3_CH7.

All PWM controllers support the following features:

* Capture mode support;

* Continuous mode or one-shot mode support;

* Each channel has two clock input options: one is a fixed frequency from the crystal oscillator, and the other is configurable from the PLL bus divider;

Functional differences between different PWM controllers:

* Waveform generator can implement breathing light function through hardware without consuming CPU;

* IR input can implement infrared input;

* Dual-phase counter is commonly used for multi-motor control, such as sweepers;

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* 统一宽度 */
       border-collapse: collapse;
       table-layout: auto;  /* 列宽自动分配 */
   }
   td {
       word-wrap: break-word;  /* 内容过长自动换行 */
   }
   </style>

+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
|                                     Feature                                      |                                             PWM0_8CH                                              |                   PWM1_4CH                   |                                             PWM2_8CH                                              |                              PWM3_8                              |
+==================================================================================+===================================================================================================+==============================================+===================================================================================================+==================================================================+
| Waveform Generator                                                               | NO                                                                                                | NO                                           | All 8 channels supported, shared LUT (depth 768)                                                  | NO                                                               |
|                                                                                  |                                                                                                   |                                              | Example: 1 channel 768 granularity; 3 channels 256 granularity; 6 channels 128 granularity        |                                                                  |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| IR Input                                                                         | NO                                                                                                | Only 1 supported, configurable on PWM1_CH0~3 | NO                                                                                                | NO                                                               |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| IR Output                                                                        | NO                                                                                                | NO                                           | NO                                                                                                | NO                                                               |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| Dual-phase Counter                                                               | Supports 4 dual-phase counters (can also be used as frequency counter with 20M frequency support) | NO                                           | Supports 4 dual-phase counters (can also be used as frequency counter with 20M frequency support) | Supports 4 dual-phase counters, can be used as frequency counter |
|                                                                                  | CH0+CH4/CH1+CH5/CH2+CH6/CH3+CH7                                                                   |                                              | CH0+CH4/CH1+CH5/CH2+CH6/CH3+CH7                                                                   | CH0+CH4/CH1+CH5/CH2+CH6/CH3+CH7                                  |
|                                                                                  |                                                                                                   |                                              |                                                                                                   | forms four dual-phase counters                                   |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| Global Control Mode (supports synchronous update of multi-channel configuration) | YES                                                                                               | YES                                          | YES                                                                                               | YES                                                              |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| Output Offset Mode (PWM output waveform offset by specified time)                | YES                                                                                               | YES                                          | YES                                                                                               | YES                                                              |
+----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+----------------------------------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

Considering the flexibility of different product applications, the 28 PWM channels are multiplexed in several different power domains, distinguished by suffixes M0/M1/M2. IOMUX_M0/M1/M2 cannot be used simultaneously, and only one group can be selected during allocation. For example, if PWM_CH0_M0 is selected, PWM_CH0_M1 or other PWM_CH0_M* cannot be selected.

The PWM interface distribution of RV1126B is shown in the following table:

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* 统一宽度 */
       border-collapse: collapse;
       table-layout: auto;  /* 列宽自动分配 */
   }
   td {
       word-wrap: break-word;  /* 内容过长自动换行 */
   }
   </style>

.. list-table::
   :widths: auto
   :header-rows: 1

   * - PWM Number
     - Multiplexing Options
     - Multiplexing Power Domain
   * - PWM0_CH0~3
     - M0,M1,M2
     - M0:PMUIO1 M1:VCCIO5 M2:VCCIO6
   * - PWM0_CH4~7
     - M0,M1,M2
     - M0:PMUIO1 M1:VCCIO4 M2:VCCIO5
   * - PWM1_CH0~3
     - M0,M1,M2
     - M0:PMUIO0 M1:VCCIO5 M2:VCCIO6
   * - PWM2_CH0~3
     - M0,M1,M2
     - M0:VCCIO3 M1:VCCIO5 M2:VCCIO6
   * - PWM2_CH4~7
     - M0,M1
     - M0:VCCIO5 M1:VCCIO7
   * - PWM3_CH0~7
     - M0,M1
     - M0:VCCIO1 M1:VCCIO5

PWM Interface Design Considerations:

* Adjust the corresponding power domain supply according to the IO level of the PWM peripheral. The levels must match.

* When implementing board-to-board connections through connectors, it is recommended to series a resistor (between 22ohm-100ohm, depending on SI test requirements) and reserve TVS devices.

* When using infrared receiver signal input, note the following:

  To support infrared receiver wake-up in standby mode and consider low power consumption (i.e., LOGIC_DVDD power-off scheme), only PWM1_CH0~3 can be selected as infrared receiver input;

  The power supply for the infrared receiver should use the voltage from PMUIO1_VCC pin;

  The power supply for the infrared receiver requires RC filtering with 22-100ohm resistor and 10uF or larger capacitor;

  The infrared receiver defaults to 38KHz. If other frequencies are used, software adjustments are required;

  The output level of the infrared receiver must match the RV1126B IO level;

  It is recommended to series a 22ohm resistor and connect to a 1nF capacitor at the output pin of the infrared receiver before connecting to RV1126B to enhance anti-static surge capability.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/PWM_03.png
   :alt: PWM
   :width: 100%

When placing the infrared receiver, keep it away from wireless module antennas such as Wi-Fi antennas to avoid interference with infrared signal reception during wireless data transmission.

The infrared receiver placement should avoid direct exposure to LED light sources on the board to prevent LED flicker frequency from affecting infrared reception.

IR signals are recommended to be grounded throughout. If grounding is not possible, maintain a spacing of ≥2 times the line width from other signals.

WIFI&BT
-------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/WIFI&BT.png
   :alt: WIFI&BT
   :width: 100%

1. Uses BL-8723DU module.

2. Supports 2.4G WIFI and 5.0 Bluetooth.

Buttons
-------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/按键.png
   :alt: Buttons
   :width: 100%

The development board uses SARADC_IN0 (ESC/RECOVERY, MENU, LEFT, RIGHT) as button detection ports, supporting 13-bit resolution. The 4 ADCKEY buttons can be configured for different purposes through software.

Press and hold the button during power-on to enter RECOVERY mode.

Pin Header
----------

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/排针.png
   :alt: Pin Header
   :width: 100%

1. 40-pin header.

2. Includes GPIO, I2C, ADC.