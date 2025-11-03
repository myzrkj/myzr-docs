GW510-4G(EN)
==============

1 Product Overview
--------------------

1.1 Product Introduction
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  GW510-4G is an industrial-grade wireless communication gateway. It provides isolated RS485, isolated RS232, 100M Ethernet, optocoupler-isolated DI, optocoupler-isolated DO, and relay switch interfaces to realize external device control, data collection, data parsing, and transparent transmission. The uplink can access servers or the cloud via 4G or Ethernet to control terminal devices and collect information. The device meets industrial-grade standards for temperature rating, static electricity, EMC, vibration, etc., and can be applied in various harsh industrial environments to achieve highly reliable data transmission.

|  Device Connections:
|  Ethernet Port: Can be used as a WAN port to connect the gateway to the target network. It can also be configured as a LAN port. RS232/RS485: Used to connect external devices, supporting data collection, transparent transmission, or parsing.

1.2 Product Features
~~~~~~~~~~~~~~~~~~~~~~

**1.2.1 High Hardware Reliability**

|  The operating temperature ranges from -20°C to 75°C, supporting 12V power input. The power supply features overvoltage protection, overcurrent protection, reverse connection protection, surge immunity, ESD protection, etc., and can withstand 4KV lightning strikes. The shell is made of 0.8mm high-quality electrolytic aluminum plate, stamped and formed with a special metal mold, boasting an exquisite appearance, good mechanical strength, and anti-electromagnetic interference performance. It meets industrial-grade standards for ESD surge, EMC, vibration, etc. Adopting a DIN rail mounting method, it is easy to install on-site. LAN, RS485, and RS232 interfaces ensure transmission reliability in industrial environments. It integrates an RTC (Real-Time Clock) with an on-board backup battery, meeting the requirements of high-performance industrial applications with large data volumes.

**1.2.2 High Performance**

|  The product is equipped with a Cortex-A35 quad-core processor with a main frequency of up to 1.4GHz.

**1.2.3 4G Network Access**

|  Supports 802.11a/b/g/n/ac 2x2 protocol. In 802.11n, it adopts dual-stream WLAN connection with a transmission speed of up to 867Mbps. Dual-band (2.4G and 5G) support, featuring seamless roaming and high security, with stronger anti-interference capability and stability.

**1.2.4 Rich Data Communication Interfaces**

|  RS485 Interfaces: 3 RS485 interfaces, supporting 4KV lightning protection
|  RS232 Interfaces: 2 RS232 interfaces, supporting 4KV lightning protection
|  Ethernet Ports: 2 100M Ethernet ports, supporting 4KV lightning protection
|  DI Interface: 1 DI interface
|  DO Interface: 1 DO interface
|  Relay Switches: 2 relay switches

1.3 Product Technical Specifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------+---------------------------------------------------------------------------------------------------+
|          Model          |                                             GW510-4G                                              |
+=========================+===================================================================================================+
| **Basic Information**                                                                                                       |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Processor               | Cortex-A35 Quad-Core, 1.4GHz Main Frequency                                                       |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Memory                  | 128MB                                                                                             |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Storage                 | 128MByte Flash                                                                                    |
+-------------------------+---------------------------------------------------------------------------------------------------+
| 4G                      | LTE TDD: B34/ 38/ 39/ 40/ 41                                                                      |
+                         +---------------------------------------------------------------------------------------------------+
|                         | LTE FDD: B1/ 3/ 5/ 8                                                                              |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Power Supply            | 12V DC Input                                                                                      |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Operating Temperature   | -20°C ~ 75°C                                                                                      |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Storage Temperature     | -40°C ~ 85°C                                                                                      |
+-------------------------+---------------------------------------------------------------------------------------------------+
| **Physical Appearance**                                                                                                     |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Dimensions              | 120.5mm (Length) x 88mm (Width) x 30mm (Height), excluding antenna connector                      |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Weight                  |                                                                                                   |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Case Craftsmanship      | Electrolytic Aluminum, Matte Black Spray Coating                                                  |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Mounting Method         | DIN Rail Mounting                                                                                 |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Antenna                 | External Rod Antenna or Suction Cup Antenna (1 piece)                                             |
+-------------------------+---------------------------------------------------------------------------------------------------+
| **Software Features**                                                                                                       |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Local Configuration     | Configurable via Local Configuration Files or Configuration Tools                                 |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Ethernet Port           | Support Configuration as LAN or WAN Port                                                          |
+-------------------------+---------------------------------------------------------------------------------------------------+
| MQTT                    | MQTT Protocol Supported                                                                           |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Modbus                  | Modbus RTU/TCP Protocols Supported                                                                |
+-------------------------+---------------------------------------------------------------------------------------------------+
| UART                    | Direct UART Data Transmit/Receive Supported                                                       |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Network Communication   | Direct Data Transmit/Receive via SDK Supported                                                    |
+-------------------------+---------------------------------------------------------------------------------------------------+
| Secondary Development   | Linux-Based, Supporting Upper-Layer Application Secondary Development as Per Project Requirements |
+-------------------------+---------------------------------------------------------------------------------------------------+

2 Product Appearance and Interfaces
--------------------------------------

2.1 Product Appearance
~~~~~~~~~~~~~~~~~~~~~~~~~

**2.1.1 Front View**

.. figure:: /image/MYZR-其他/网关/GW510/产品介绍1.png
   :alt: 产品介绍1.png

**2.1.2 Side View**

.. figure:: /image/MYZR-其他/网关/GW510/产品介绍2.png
   :alt: 产品介绍2.png

2.2 Product Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-其他/网关/GW510/产品介绍3.png
   :alt: 产品介绍3.png

2.3 Product Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~

**2.3.1 Front Interfaces**

.. figure:: /image/MYZR-其他/网关/GW510/产品介绍4.png
   :alt: 产品介绍4.png

+--------------------+-----------------------------------------------------------------+
| Hardware Interface |                      Interface Description                      |
+====================+=================================================================+
| ETH                | Ethernet Port (RJ45), 10/100M Supported                         |
+--------------------+-----------------------------------------------------------------+
| RS232              | 3.81mm Pitch Phoenix Terminal, External RS232 Device Compatible |
+--------------------+-----------------------------------------------------------------+
| RS485              | 3.81mm Pitch Phoenix Terminal, External RS485 Device Compatible |
+--------------------+-----------------------------------------------------------------+
| PWR                | Power Indicator (Red)                                           |
+--------------------+-----------------------------------------------------------------+
| SYS                | System Indicator (Green)                                        |
+--------------------+-----------------------------------------------------------------+
| 4G                 | 4G Indicator (Green)                                            |
+--------------------+-----------------------------------------------------------------+
| RST                | Button (System Reset Function)                                  |
+--------------------+-----------------------------------------------------------------+

**2.3.2 Side Interfaces**

.. figure:: /image/MYZR-其他/网关/GW510/产品介绍5.png
   :alt: 产品介绍5.png

+--------------------+--------------------------------------------------+
| Hardware Interface |              Interface Description               |
+====================+==================================================+
| Power Interface    | 3P Phoenix Terminal (5.08mm Pitch), 12V DC Input |
+--------------------+--------------------------------------------------+
| 4G_ANTx            | Standard SMA Female Antenna Interface            |
+--------------------+--------------------------------------------------+

2.4 Packing List
~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-其他/网关/GW510/产品介绍6.png
   :alt: 产品介绍6.png
