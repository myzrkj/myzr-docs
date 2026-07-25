
Specifications
======

Product Overview
--------

TB04 Smart Lighting Module is a Bluetooth module based on TLSR8258 chip design, compliant with BLE 5.0 low-power Tmall Genie Mesh; This module has Bluetooth mesh networking capability; Devices communicate through peer-to-peer star network, using Bluetooth broadcasting for communication, which can ensure timely response in multi-device situations. It is mainly used for smart lighting control, and can meet the requirements of low power consumption, low latency, and short-range wireless data communication.

Features

*  1.1mm pitch SMD-20 package

*  6-channel PWM output

*  Brightness (duty cycle) adjustment range 5%-100%

*  Factory default cold and warm color duty cycle each 50%

*  With night light function

*  With wall switch to change color temperature function

Applications

*  Smart LED / Smart Home

*  Smart low-power sensors

*  Smart buildings

*  Smart home/appliances

*  Smart sockets, smart lights

*  Industrial wireless control

*  Baby monitors

*  Smart buses

Module Interface
--------

Dimensions
~~~~~~~~

.. raw:: html

   <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
   <div style="text-align: center; width: 45%;">

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_1.png
   :alt: 规格书_1.png
   :width: 100%

.. raw:: html

   </div>
   <div style="text-align: center; width: 45%;">

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_2.png
   :alt: 规格书_2.png
   :width: 90%



.. raw:: html

   </div>
   <div style="text-align: center; width: 45%;">

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_3.png
   :alt: 规格书_3.png
   :width: 100%

.. raw:: html

   </div>
   <div style="text-align: center; width: 45%;">

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_4.png
   :alt: 规格书_4.png
   :width: 90%

Pin Definition
~~~~~~~~

TB-04 module has 20 interfaces exposed, as shown in the pin diagram. The pin function definition table is the interface definition.

TB-04 Pin Diagram

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_5.png
   :alt: 规格书_5.png
   :width: 100%

Pin Function Definition Table

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
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
       word-wrap: break-word;
   }
   </style>

+-----+------+-------------------------------------------------------------------+
| Pin | Name |                       Function Description                        |
+=====+======+===================================================================+
| 1   | NC   | NOT CONNECTED                                                     |
+-----+------+-------------------------------------------------------------------+
| 2   | RST  | Reset pin                                                         |
+-----+------+-------------------------------------------------------------------+
| 3   | NC   | NOT CONNECTED                                                     |
+-----+------+-------------------------------------------------------------------+
| 4   | C4   | PWM2 output/UART\_CTS/PWM0 inverted output/SAR ADC input/GPIO PC4 |
+-----+------+-------------------------------------------------------------------+
| 5   | C1   | I2C serial clock/ PWM1 inverted output/ PWM0 output/GPIO PC1      |
+-----+------+-------------------------------------------------------------------+
| 6   | C0   | I2C serial data/ PWM4 inverted output/ UART\_RTS / GPIO PC0       |
+-----+------+-------------------------------------------------------------------+
| 7   | B7   | SPI data output/UART\_RX/SAR ADC input/GPIO PB7                   |
+-----+------+-------------------------------------------------------------------+
| 8   | B6   | SPI data input (I2C\_SDA) /UART\_RTS/SAR ADC input/GPIO PB6       |
+-----+------+-------------------------------------------------------------------+
| 9   | B5   | PWM5 output/SAR ADC input/GPIO PB5                                |
+-----+------+-------------------------------------------------------------------+
| 10  | B4   | PWM4 output/SAR ADC input/GPIO PB4                                |
+-----+------+-------------------------------------------------------------------+
| 11  | 3V3  | 3.3V power supply                                                 |
+-----+------+-------------------------------------------------------------------+
| 12  | GND  | Ground                                                            |
+-----+------+-------------------------------------------------------------------+
| 13  | RXD  | PWM0 inverted output/UART\_RX/GPIO PA0                            |
+-----+------+-------------------------------------------------------------------+
| 14  | TXD  | PWM4 output/UART\_TX/SAR ADC input/GPIO PB1                       |
+-----+------+-------------------------------------------------------------------+
| 15  | SWS  | Single-wire slave                                                 |
+-----+------+-------------------------------------------------------------------+
| 16  | A1   | GPIO PA1                                                          |
+-----+------+-------------------------------------------------------------------+
| 17  | D7   | GPIO PD7/SPI clock (I2C\_SCK)                                     |
+-----+------+-------------------------------------------------------------------+
| 18  | D4   | GPIO PD4/Single-wire master/PWM2 inverted output                  |
+-----+------+-------------------------------------------------------------------+
| 19  | D3   | PWM1 inverted output/GPIO PD3                                     |
+-----+------+-------------------------------------------------------------------+
| 20  | D2   | SPI chip select (active low) /PWM3 output/GPIO PD2                |
+-----+------+-------------------------------------------------------------------+

Key Parameters
--------

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
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
       word-wrap: break-word;
   }
   </style>

+-----------------------+--------------------------------------------------+
|     Module Model      |                       TB04                       |
+=======================+==================================================+
| Dimensions            | 12.2*14.1*2.3(± 0.2)MM                           |
+-----------------------+--------------------------------------------------+
| Package               | SMD-20                                           |
+-----------------------+--------------------------------------------------+
| Wireless Standard     | Bluetooth 5.0                                    |
+-----------------------+--------------------------------------------------+
| Frequency Range       | 2400 ~ 2483.5MHz                                 |
+-----------------------+--------------------------------------------------+
| Max Transmit Power    | Max 10dBm                                        |
+-----------------------+--------------------------------------------------+
| Receive Sensitivity   | -93dBm± 2                                        |
+-----------------------+--------------------------------------------------+
| Interface             | GPIO/PWM/SPI/ADC                                 |
+-----------------------+--------------------------------------------------+
| Operating Temperature | -40℃ ~ 85 ℃                                      |
+-----------------------+--------------------------------------------------+
| Storage Environment   | -40 ℃ ~ 125 ℃ , < 90%RH                          |
+-----------------------+--------------------------------------------------+
| Power Supply Range    | Supply voltage 2.7V ~ 3.6V, Supply current ≥50mA |
+-----------------------+--------------------------------------------------+
| Power Consumption     | Deep sleep mode: 0.8uA                           |
+                       +--------------------------------------------------+
|                       | Sleep mode: 1.8uA                                |
+                       +--------------------------------------------------+
|                       | TX (10dBm): 20.69mA                              |
+-----------------------+--------------------------------------------------+

Electrical Parameters
--------

Absolute Maximum Ratings

Exceeding the following absolute maximum ratings may cause damage to the TLSR8258

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
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
       word-wrap: break-word;
   }
   </style>

+----------------------------+------+-----+------+------+
|            Name            | Min  | Typ | Max  | Unit |
+============================+======+=====+======+======+
| Supply voltage             | 2.7  | 3.3 | 3.6  | V    |
+----------------------------+------+-----+------+------+
| I/O supply voltage (VCCIO) | -0.3 | ——  | 3.6  | V    |
+----------------------------+------+-----+------+------+
| Operating temperature      | -40  | ——  | +85  | ℃    |
+----------------------------+------+-----+------+------+
| Storage temperature        | -40  | ——  | +125 | ℃    |
+----------------------------+------+-----+------+------+

Operating Conditions

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
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
       word-wrap: break-word;
   }
   </style>

+-----------+-----------------------+---------+-----+---------+------+
| Parameter |      Description      |   Min   | Typ |   Max   | Unit |
+===========+=======================+=========+=====+=========+======+
| Ta        | Operating temperature | -40     | ——  | 85      | ℃    |
+-----------+-----------------------+---------+-----+---------+------+
| VCC       | Operating voltage     | 3       | 3.3 | 3.6     | V    |
+-----------+-----------------------+---------+-----+---------+------+
| VIL       | IO low-level input    | VSS     | ——  | VCC*0.3 | V    |
+-----------+-----------------------+---------+-----+---------+------+
| VIH       | IO high-level input   | VCC*0.7 | ——  | VCC     | V    |
+-----------+-----------------------+---------+-----+---------+------+
| VOL       | IO low-level output   | VSS     | ——  | VCC*0.1 | V    |
+-----------+-----------------------+---------+-----+---------+------+
| VOH       | IO high-level output  | VCC*0.9 | ——  | VCC     | V    |
+-----------+-----------------------+---------+-----+---------+------+

Power Consumption in Operating Mode

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
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
       word-wrap: break-word;
   }
   </style>

+------------------------------+-------+------+
|        Parameter Name        |  Typ  | Unit |
+==============================+=======+======+
| TX power consumption (10dBm) | 20.69 | mA   |
+------------------------------+-------+------+
| RX power consumption         | 6.26  | mA   |
+------------------------------+-------+------+
| Standby power consumption    | 3.06  | mA   |
+------------------------------+-------+------+
| Light sleep                  | 1.8   | uA   |
+------------------------------+-------+------+
| Deep sleep                   | 0.8   | uA   |
+------------------------------+-------+------+

RF Parameters
--------

Basic RF Characteristics

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
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
       word-wrap: break-word;
   }
   </style>

+------------------------+---------------------+
|       Parameter        |     Description     |
+========================+=====================+
| Operating frequency    | 2.4GHz ISM band     |
+------------------------+---------------------+
| Wireless standard      | Bluetooth 5.0       |
+------------------------+---------------------+
| Data transmission rate | 1 Mbps              |
+------------------------+---------------------+
| Antenna type           | Onboard PCB antenna |
+------------------------+---------------------+

RF Transmit Power

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
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
       word-wrap: break-word;
   }
   </style>

+---------------+-----+-----+-----+------+
|     Name      | Min | Typ | Max | Unit |
+===============+=====+=====+=====+======+
| Average power | ——  | 8.5 | 10  | dBm  |
+---------------+-----+-----+-----+------+

RF Receive Sensitivity

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
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
       word-wrap: break-word;
   }
   </style>

+---------------------+-----+-----+-----+------+
|        Name         | Min | Typ | Max | Unit |
+=====================+=====+=====+=====+======+
| Receive sensitivity | -94 | -93 | ——  | dBm  |
+---------------------+-----+-----+-----+------+

Module Power-On Sequence Requirements

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_6.png
   :alt: 规格书_6.png
   :width: 100%

The TLSR8258 chip has requirements for the power-on sequence. During power-on, the system starts when the RST pin reaches 1.62V. At this time, VDD needs to reach 1.8V or above within 10ms. Since the RST pin has an RC circuit, when the bare module's RST reaches 1.62V, VDD has already far exceeded 1.8V. If the power driver connected to the TLSR8258 chip module has large capacitance charging/discharging, if the module voltage is not fully discharged below 0.6V, there is a risk of system crash when the module restarts. The module VDD_3.3V power pin requires a 1K dummy load to quickly release electrical energy. Please refer to the partial power driver circuit below:

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_7.png
   :alt: 规格书_7.png
   :width: 100%

Antenna Information
--------

**Antenna Type**

BTU uses an onboard PCB antenna with antenna gain of 1.1dBi.

**Reducing Antenna Interference**

To ensure optimal RF performance, it is recommended that the distance between the module antenna and other metal components be at least 15mm. If the antenna's surroundings in the usage environment are wrapped with metal materials, it will greatly attenuate the wireless signal and degrade RF performance. When designing the finished product, ensure sufficient space is reserved for the antenna area.

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_8.png
   :alt: 规格书_8.png
   :width: 100%

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_9.png
   :alt: 规格书_9.png
   :width: 100%

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_10.png
   :alt: 规格书_10.png
   :width: 100%

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_11.png
   :alt: 规格书_11.png
   :width: 100%

Package Information and Production Guide
------------------

Mechanical Dimensions
~~~~~~~~

PCB dimensions: 20.3±0.35mm (L) × 15.8±0.35mm (W) × 1.0±0.1mm (H).

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_12.png
   :alt: 规格书_12.png
   :width: 100%

Side View

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_13.png
   :alt: 规格书_13.png
   :width: 100%

PCB Package Diagram - SMT

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_14.png
   :alt: 规格书_14.png
   :width: 100%

Design Guidelines
--------

1. Application Circuit

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_15.png
   :alt: 规格书_15.png
   :width: 100%

2. Antenna Layout Requirements

Place the module at the edge of the main board. No metal components should be placed around the antenna. Keep away from high-frequency devices.

3. Power Supply

*  Recommended 3.3V voltage, peak current above 50mA

*  It is recommended to use LDO for power supply; if using DC-DC, it is recommended to control ripple within 30mV.

*  DC-DC power supply circuit is recommended to reserve a position for dynamic response capacitor, which can optimize output ripple when load changes significantly.

*  It is recommended to add ESD components to the 3.3V power interface.

4. PWM Dimming Design Description

For lamps that require dimming function, simply connect the PWM pin of the corresponding color to the control terminal of the subsequent drive circuit; PWM independently outputs a 100-level adjustable duty cycle digital signal, and the subsequent circuit can be voltage-driven or current-driven.

Connection Diagram

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_16.png
   :alt: 规格书_16.png
   :width: 100%

5. LED Driver Reference Design

TB-04 module application only needs 3.3V power supply and simple drive circuit to realize smart light control. Taking MOS tube driving one channel of positive white light as an example, the design reference is shown in the figure below; CW_I is the PWM output pin for positive white light of the module, Q1 is MOS tube, WW is LED bead. The other 4 channels of LED drive circuit have the same design method as this channel.

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_17.png
   :alt: 规格书_17.png
   :width: 100%

6. Reflow Soldering Profile

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_18.png
   :alt: 规格书_18.png
   :width: 100%

Production Guide
--------

1. Assembly Method

The factory's surface-mount and through-hole packaged modules are selected for assembly method according to the customer's base board design. When the base board is designed for surface-mount package, SMT process is used for production. When the base board is designed for through-hole package, wave soldering process is used for production. After the module product is unpacked, it is recommended to complete welding within 24 hours. Otherwise, it must be placed in a drying cabinet with humidity not exceeding 10%RH, or re-vacuum packaged and the exposure time recorded. The total exposure time must not exceed 168 hours.

• (SMT Process) Equipment required for SMT:

• Placement machine

• SPI

• Reflow soldering

• Temperature profiler

• AOI

• (Wave Soldering Process) Equipment required for wave soldering:

• Wave soldering equipment

• Wave soldering fixture

• Constant temperature soldering iron

• Solder bar, solder wire, flux

• Temperature profiler

• Baking required equipment:

• Cabinet baking oven

• Anti-static high-temperature tray

• Anti-static high-temperature gloves

2. Factory module storage conditions are as follows:

• Moisture barrier bags must be stored in an environment with temperature <40℃ and humidity <90%RH.

• Products with dry packaging have a shelf life of 12 months from the date of packaging sealing.

• The sealed package contains a humidity indicator card:

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_19.png
   :alt: 规格书_19.png
   :width: 100%

3. Baking is required when the factory module may have been exposed to moisture:

• Vacuum packaging bag is found damaged before unpacking.

• No humidity indicator card is found in the package after unpacking.

• If the humidity indicator card shows that 10% or more of the color ring turns pink after unpacking.

• Total exposure time exceeds 168 hours after unpacking.

• More than 12 months from the date of first sealed packaging.

4. Baking parameters are as follows:

• Baking temperature: Reel packaging 40℃, less than or equal to 5%RH. Tray packaging 125℃, less than or equal to 5%RH (high-temperature resistant tray, not plastic tray).

• Baking time: Reel packaging 168 hours, tray packaging 12 hours.

• Alarm temperature setting: Reel packaging 50℃, tray packaging 135℃.

• After cooling to below 36℃ under natural conditions, production can proceed.

5. During the entire production process, please provide ESD protection for the module.

6. To ensure product qualification rate, it is recommended to use SPI and AOI test equipment to monitor solder paste printing and mounting quality

Recommended Temperature Profile

Please select the appropriate soldering method according to the process. SMT refers to the reflow soldering temperature profile recommendation, and wave soldering process refers to the wave soldering temperature profile recommendation. There is a certain difference between the set furnace temperature and the measured furnace temperature. The temperatures shown in this article are all measured temperatures.

SMT Process (SMT Reflow Soldering Recommended Temperature Profile)

Please refer to the reflow soldering temperature profile requirements for furnace temperature setting. The reflow soldering temperature curve is shown in the figure below:

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-TB04/规格书_20.png
   :alt: 规格书_20.png
   :width: 100%

• A: Temperature axis

• B: Time axis

• C: Alloy liquidus temperature range is 217-220℃

• D: Heating rate is 1-3℃/S

• E: Soak time is 60-120S, soak temperature range is 150-200℃

• F: Time above liquidus is 50-70S

• G: Peak temperature is 235-245℃

Module Storage Precautions
------------------

• If the exposure time after baking exceeds 168 hours and the modules are not fully used, please bake again.

• If the exposure time exceeds 168 hours without baking, wave soldering process is not recommended for this batch of modules. As the module is a Level 3 moisture-sensitive device, exceeding the allowed exposure time may cause moisture absorption, which may lead to device failure or poor soldering during high-temperature soldering.

• During the entire production process, please provide ESD protection for the module.

• To ensure product qualification rate, it is recommended to use SPI and AOI test equipment to monitor solder paste printing and mounting quality.

Ordering Options
--------

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
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
       word-wrap: break-word;
   }
   </style>

+----------------+------------------------+
|     Model      |      Description       |
+================+========================+
| MYZR-TB04-ANT  | Onboard PCB antenna    |
+----------------+------------------------+
| MYZR-TB04-IPEX | Onboard IPEX connector |
+----------------+------------------------+