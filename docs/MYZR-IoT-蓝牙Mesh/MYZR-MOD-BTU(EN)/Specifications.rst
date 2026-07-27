
Specifications
==========

MYZR-BTU is a low-power embedded Bluetooth module. It mainly consists of a highly integrated Bluetooth chip TLSR8258 and a small amount of peripheral circuits, with built-in Bluetooth network communication protocol stack and rich library functions.

Product Overview
--------

BTU also includes a low-power 32-bit MCU, Bluetooth LE5.0/2.4G Radio, 4Mbits flash and 48Kbyte SRAM.

Features

• Built-in low-power 32-bit MCU, can also serve as application processor.

• Main frequency supports 48 MHz

• Operating voltage: 3.0V-3.6V

• Peripherals: 15×GPIOs, 1×UART, 2×ADC

• Bluetooth LE RF characteristics

• Compatible with Bluetooth LE 4.2/5.0

• TX transmit power: +10dBm

• RX receive sensitivity: -94.5dBm@Bluetooth LE 1Mbps

• Built-in hardware AES encryption

• Equipped with onboard PCB antenna, antenna gain 1.1dB

• Operating temperature: -40℃ to +85℃

Applications

• Smart buildings

• Smart home/appliances

• Smart sockets, smart lights

• Industrial wireless control

• Baby monitors

• Smart buses

Module Interface
--------

Dimensions
~~~~~~~~

BTU has 3 rows of pins, with pin pitch of 1.4±0.1mm.

BTU dimensions: 20.6±0.35mm (L) × 15.8±0.35mm (W) × 3.0±0.15mm (H).

Pin Definition
~~~~~~~~

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+1.png
   :alt: 规格书+1.png
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

+------------+--------+----------+------------------------------------------------------+
| Pin Number | Symbol | I/O Type |                 Function Description                 |
+============+========+==========+======================================================+
| 1          | D3     | I/O      | General IO pin, corresponds to IC's D3(Pin32)        |
+------------+--------+----------+------------------------------------------------------+
| 2          | D7     | I/O      | General IO pin, corresponds to IC's D7(Pin2)         |
+------------+--------+----------+------------------------------------------------------+
| 3          | C0     | I/O      | General IO pin, corresponds to IC's C0(Pin20)        |
+------------+--------+----------+------------------------------------------------------+
| 4          | SWS    | I/O      | Programming pin, corresponds to IC's SWS (Pin5)      |
+------------+--------+----------+------------------------------------------------------+
| 5          | B6     | I        | ADC pin, corresponds to IC's B6 (Pin16)              |
+------------+--------+----------+------------------------------------------------------+
| 6          | A0     | I/O      | General IO pin, corresponds to IC's A0 (Pin3)        |
+------------+--------+----------+------------------------------------------------------+
| 7          | A1     | I/O      | General IO pin, corresponds to IC's A1 (Pin4)        |
+------------+--------+----------+------------------------------------------------------+
| 8          | C2     | I/O      | Hardware PWM support, corresponds to IC's C2 (Pin22) |
+------------+--------+----------+------------------------------------------------------+
| 9          | C3     | I/O      | Hardware PWM support, corresponds to IC's C3 (Pin23) |
+------------+--------+----------+------------------------------------------------------+
| 10         | D2     | I/O      | Hardware PWM support, corresponds to IC's D2 (Pin31) |
+------------+--------+----------+------------------------------------------------------+
| 11         | B4     | I/O      | Hardware PWM support, corresponds to IC's B4 (Pin14) |
+------------+--------+----------+------------------------------------------------------+
| 12         | B5     | I/O      | Hardware PWM support, corresponds to IC's B5 (Pin15) |
+------------+--------+----------+------------------------------------------------------+
| 13         | GND    | P        | Power ground pin                                     |
+------------+--------+----------+------------------------------------------------------+
| 14         | VCC    | P        | Power pin (3.3V)                                     |
+------------+--------+----------+------------------------------------------------------+
| 15         | B1     | I/O      | UART\_TXD, corresponds to IC's B1 (Pin6)             |
+------------+--------+----------+------------------------------------------------------+
| 16         | B7     | I/O      | UART\_RXD, corresponds to IC's B7 (Pin17)            |
+------------+--------+----------+------------------------------------------------------+
| 17         | C4     | I/O      | ADC pin, corresponds to IC's C4 (Pin24)              |
+------------+--------+----------+------------------------------------------------------+
| 18         | RST    | I/O      | Reset pin, active low                                |
+------------+--------+----------+------------------------------------------------------+
| 19         | C1     | I/O      | General IO pin, corresponds to IC's C1 (Pin21)       |
+------------+--------+----------+------------------------------------------------------+
| 20         | D4     | I/O      | General IO pin, corresponds to IC's D4 (Pin1)        |
+------------+--------+----------+------------------------------------------------------+
| 21         | NC     | I/O      | Not connected                                        |
+------------+--------+----------+------------------------------------------------------+

Note: P indicates power pin,

Electrical Parameters
--------

Absolute Electrical Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

+-----------------------------------------+---------------------+------+-----+------+
|                Parameter                |     Description     | Min  | Max | Unit |
+=========================================+=====================+======+=====+======+
| Ts                                      | Storage temperature | -65  | 150 | ℃    |
+-----------------------------------------+---------------------+------+-----+------+
| VCC                                     | Supply voltage      | -0.3 | 3.9 | V    |
+-----------------------------------------+---------------------+------+-----+------+
| ESD voltage (Human body model) TAMB-25℃ | ——                  | 2    | KV  |      |
+-----------------------------------------+---------------------+------+-----+------+
| ESD voltage (Machine model) TAMB-25℃    | ——                  | 0.5  | KV  |      |
+-----------------------------------------+---------------------+------+-----+------+

Operating Conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

+-------------+-------------------------------------------+-----------+------+
|   Symbol    |                 Condition                 | Max (Typ) | Unit |
+=============+===========================================+===========+======+
| Itx         | Continuous transmit, 11.5dBm output power | 22.6      | mA   |
+-------------+-------------------------------------------+-----------+------+
| Irx         | Continuous receive                        | 6.5       | mA   |
+-------------+-------------------------------------------+-----------+------+
| IDC         | Mesh network operating mode Average value | 6.59      | mA   |
+-------------+-------------------------------------------+-----------+------+
| IDC         | Mesh network operating mode Peak value    | 24.9      | mA   |
+-------------+-------------------------------------------+-----------+------+
| Ideepsleep1 | Deep sleep mode (16KB RAM retained)       | 1.2       | μA   |
+-------------+-------------------------------------------+-----------+------+
| Ideepsleep2 | Deep sleep mode (RAM not retained)        | 0.4       | μA   |
+-------------+-------------------------------------------+-----------+------+

RF Parameters
--------

Basic RF Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

+------------------------+----------------------+
|       Parameter        |     Description      |
+========================+======================+
| Operating frequency    | 2.4GHz ISM band      |
+------------------------+----------------------+
| Wireless standard      | Bluetooth LE 4.2/5.0 |
+------------------------+----------------------+
| Data transmission rate | 1 Mbps               |
+------------------------+----------------------+
| Antenna type           | Onboard PCB antenna  |
+------------------------+----------------------+

RF Output Power
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

+--------------------------------------+-----+-----+------+------+
|              Parameter               | Min | Typ | Max  | Unit |
+======================================+=====+=====+======+======+
| RF average output power              | -21 | 10  | 11.5 | dBm  |
+--------------------------------------+-----+-----+------+------+
| 20dB modulated signal bandwidth (1M) | ——  | ——  | 2500 | KHz  |
+--------------------------------------+-----+-----+------+------+

RF Receive Sensitivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

+-----------------------------------+------+-------+-----+------+
|             Parameter             | Min  |  Typ  | Max | Unit |
+===================================+======+=======+=====+======+
| RX sensitivity 1Mbps              | ——   | -94.5 | ——  | dBm  |
+-----------------------------------+------+-------+-----+------+
| Frequency offset error 1Mbps      | -250 | ——    |     | KHz  |
+-----------------------------------+------+-------+-----+------+
| Co-channel interference rejection | ——   | ——    | -10 | dB   |
+-----------------------------------+------+-------+-----+------+

Module Power-On Sequence Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+2.png
   :alt: 规格书+2.png
   :width: 100%

The TLSR8258 chip has requirements for the power-on sequence. During power-on, the system starts when the RST pin reaches 1.62V. At this time, VDD needs to reach 1.8V or above within 10ms. Since the RST pin has an RC circuit, when the bare module's RST reaches 1.62V, VDD has already far exceeded 1.8V. If the power driver connected to the TLSR8258 chip module has large capacitance charging/discharging, if the module voltage is not fully discharged below 0.6V, there is a risk of system crash when the module restarts. The module VDD_3.3V power pin requires a 1K dummy load to quickly release electrical energy. Please refer to the partial power driver circuit below:

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+3.png
   :alt: 规格书+3.png
   :width: 100%

Antenna Information
--------

Antenna Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BTU uses an onboard PCB antenna with antenna gain of 1.1dBi.

Reducing Antenna Interference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure optimal RF performance, it is recommended that the distance between the module antenna and other metal components be at least 15mm. If the antenna's surroundings in the usage environment are wrapped with metal materials, it will greatly attenuate the wireless signal and degrade RF performance. When designing the finished product, ensure sufficient space is reserved for the antenna area.

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+4.png
   :alt: 规格书+4.png
   :width: 100%

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+5.png
   :alt: 规格书+5.png
   :width: 100%

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+6.png
   :alt: 规格书+6.png
   :width: 100%

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+7.png
   :alt: 规格书+7.png
   :width: 100%

Package Information and Production Guide
------------------

Mechanical Dimensions
~~~~~~~~

PCB dimensions: 20.3±0.35mm (L) × 15.8±0.35mm (W) × 1.0±0.1mm (H).

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+8.png
   :alt: 规格书+8.png
   :width: 100%

Side View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+9.png
   :alt: 规格书+9.png
   :width: 100%

PCB Package Diagram - SMT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+10.png
   :alt: 规格书+10.png
   :width: 100%

Design Guidelines
--------

1. Application Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+11.png
   :alt: 规格书+11.png
   :width: 100%

2. Antenna Layout Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Place the module at the edge of the main board. No metal components should be placed around the antenna. Keep away from high-frequency devices.

3. Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(1) Recommended 3.3V voltage, peak current above 50mA

(2) It is recommended to use LDO for power supply; if using DC-DC, it is recommended to control ripple within 30mV.

(3) DC-DC power supply circuit is recommended to reserve a position for dynamic response capacitor, which can optimize output ripple when load changes significantly.

(4) It is recommended to add ESD components to the 3.3V power interface.

4. PWM Dimming Design Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For lamps that require dimming function, simply connect the PWM pin of the corresponding color to the control terminal of the subsequent drive circuit; PWM independently outputs a 100-level adjustable duty cycle digital signal, and the subsequent circuit can be voltage-driven or current-driven.

Connection Diagram

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+12.png
   :alt: 规格书+12.png
   :width: 100%

5. LED Driver Reference Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TB-04 module application only needs 3.3V power supply and simple drive circuit to realize smart light control. Taking MOS tube driving one channel of positive white light as an example, the design reference is shown in the figure below; CW_I is the PWM output pin for positive white light of the module, Q1 is MOS tube, WW is LED bead. The other 4 channels of LED drive circuit have the same design method as this channel.

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+13.png
   :alt: 规格书+13.png
   :width: 100%

6. Reflow Soldering Profile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+14.png
   :alt: 规格书+14.png
   :width: 100%

Production Guide
--------

1. Assembly Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The factory's surface-mount and through-hole packaged modules are selected for assembly method according to the customer's base board design. When the base board is designed for surface-mount package, SMT process is used for production. When the base board is designed for through-hole package, wave soldering process is used for production. After the module product is unpacked, it is recommended to complete welding within 24 hours. Otherwise, it must be placed in a drying cabinet with humidity not exceeding 10%RH, or re-vacuum packaged and the exposure time recorded. The total exposure time must not exceed 168 hours.

* SMT Process) Equipment required for SMT:

• Placement machine

• SPI

• Reflow soldering

• Temperature profiler

• AOI

* Wave Soldering Process) Equipment required for wave soldering:

• Wave soldering equipment

• Wave soldering fixture

• Constant temperature soldering iron

• Solder bar, solder wire, flux

• Temperature profiler

* Baking Required) Equipment required for baking:

• Cabinet baking oven

• Anti-static high-temperature tray

• Anti-static high-temperature gloves

2. Factory module storage conditions are as follows:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

• Moisture barrier bags must be stored in an environment with temperature <40℃ and humidity <90%RH.

• Products with dry packaging have a shelf life of 12 months from the date of packaging sealing.

• The sealed package contains a humidity indicator card:

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+15.png
   :alt: 规格书+15.png
   :width: 100%

3. Baking is required when the factory module may have been exposed to moisture:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

• Vacuum packaging bag is found damaged before unpacking.

• No humidity indicator card is found in the package after unpacking.

• If the humidity indicator card shows that 10% or more of the color ring turns pink after unpacking.

• Total exposure time exceeds 168 hours after unpacking.

• More than 12 months from the date of first sealed packaging.

4. Baking parameters are as follows:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

• Baking temperature: Reel packaging 40℃, less than or equal to 5%RH. Tray packaging 125℃, less than or equal to 5%RH (high-temperature resistant tray, not plastic tray).

• Baking time: Reel packaging 168 hours, tray packaging 12 hours.

• Alarm temperature setting: Reel packaging 50℃, tray packaging 135℃.

• After cooling to below 36℃ under natural conditions, production can proceed.

5. During the entire production process, please provide ESD protection for the module.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

6. To ensure product qualification rate, it is recommended to use SPI and AOI test equipment to monitor solder paste printing and mounting quality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Recommended Temperature Profile
------------------------------------

Please select the appropriate soldering method according to the process. SMT refers to the reflow soldering temperature profile recommendation, and wave soldering process refers to the wave soldering temperature profile recommendation. There is a certain difference between the set furnace temperature and the measured furnace temperature. The temperatures shown in this article are all measured temperatures.

SMT Process (SMT Reflow Soldering Recommended Temperature Profile)

Please refer to the reflow soldering temperature profile requirements for furnace temperature setting. The reflow soldering temperature curve is shown in the figure below:

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+16.png
   :alt: 规格书+16.png
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

.. image:: ../../../image/MYZR-IoT系列/MYZR-MOD-BTU/规格书+17.png
   :alt: 规格书+17.png
   :width: 100%

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

+---------------+------------------------+
|     Model     |      Description       |
+===============+========================+
| MYZR-BTU-ANT  | Onboard PCB antenna    |
+---------------+------------------------+
| MYZR-BTU-IPEX | Onboard IPEX connector |
+---------------+------------------------+