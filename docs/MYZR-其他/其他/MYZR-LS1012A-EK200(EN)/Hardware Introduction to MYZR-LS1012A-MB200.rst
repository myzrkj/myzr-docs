MYZR-LS1012A-MB200 Hardware Introduction
===========================================

Interface Overview
---------------------

Front View
~~~~~~~~~~~~

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/1500px-LS1012A-interface.jpg
   :alt: 1500px-LS1012A-interface.jpg

Back View (MB200)
~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/963px-LS1012A-BackView.png
   :alt: 963px-LS1012A-BackView.png

Dimension Drawing (MB200)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-size.png
   :alt: LS1012A-size.png

Interface Functions
----------------------

2-Position DIP Switch
~~~~~~~~~~~~~~~~~~~~~~~

|  Silkscreen: SW1
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-SW1.png
   :alt: LS1012A-SW1.png

+------------------+------------+------------+
| Mode Control     | Position 1 | Position 2 |
+------------------+------------+------------+
| Programming Mode | x          | 0          |
+------------------+------------+------------+
| Boot Mode        | x          | 1          |
+------------------+------------+------------+

Reset Switch
~~~~~~~~~~~~~~

|  Silkscreen: SW2
|  Function: Press to reset

Debug Serial Port
~~~~~~~~~~~~~~~~~~~

|  Silkscreen: P1
|  Interface Attribute: UART0, RS-232 Level
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-P1.png
   :alt: LS1012A-P1.png

RS-232 Serial Port & RS-485 Serial Port
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Silkscreen: J1

+--------+----------+---------------------------------------------------+
| Name   | Quantity | Interface Attribute                               |
+--------+----------+---------------------------------------------------+
| RS-232 | 3        | USB Expanded Serial Port, Data Rate up to 235Kbps |
+--------+----------+---------------------------------------------------+
| RS-485 | 3        | USB Expanded Serial Port, Data Rate up to 12Mbps  |
+--------+----------+---------------------------------------------------+

|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-J1.png
   :alt: LS1012A-J1.png

DI Expansion
~~~~~~~~~~~~~~

|  Silkscreen: J2
|  Interface Attribute: Expanded DI, Optocoupler Isolation
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-J2.png
   :alt: LS1012A-J2.png

DO Expansion
~~~~~~~~~~~~~~

|  Silkscreen: J3
|  Interface Attribute: Expanded DO, Optocoupler Isolation
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/963px-LS1012A-J3.png
   :alt: 963px-LS1012A-J3.png

GPIO & PMU Control
~~~~~~~~~~~~~~~~~~~~

|  Silkscreen: J4
|  Interface Attribute: Spare Pins, Some Can Be Used as GPIO
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-J4.png
   :alt: LS1012A-J4.png

+-------+------------+--------------------------------------------------+-------+------------------+----------------------------------------------+
| Pin   | Signal     | Description                                      | Pin   | Signal           | Description                                  |
+-------+------------+--------------------------------------------------+-------+------------------+----------------------------------------------+
| J4-1  | INT_PMU    | Core Board PMU Interrupt Request Output          | J4-2  | DUT_SAI2_RX_SYNC | Led out from Core Board, Can Be Used as GPIO |
+-------+------------+--------------------------------------------------+-------+------------------+----------------------------------------------+
| J4-3  | HRESET_PMU | Led out from Core Board PMU, Can Be Used as GPIO | J4-4  | DUT_SAI2_RX_BCLK | Led out from Core Board, Can Be Used as GPIO |
+-------+------------+--------------------------------------------------+-------+------------------+----------------------------------------------+
| J4-5  | PMU_GPIO1  | Led out from Core Board PMU, Can Be Used as GPIO | J4-6  | GND              | Digital Ground                               |
+-------+------------+--------------------------------------------------+-------+------------------+----------------------------------------------+
| J4-7  | PMU_GPIO0  | Led out from Core Board PMU, Can Be Used as GPIO | J4-8  | GND              | Digital Ground                               |
+-------+------------+--------------------------------------------------+-------+------------------+----------------------------------------------+
| J4-9  | PMU_GPIO2  | Led out from Core Board PMU, Can Be Used as GPIO | J4-10 | GND              | Digital Ground                               |
+-------+------------+--------------------------------------------------+-------+------------------+----------------------------------------------+
| J4-11 | PMU_SLEEP  | Core Board PMU Standby Mode Control Signal Input | J4-12 | GND              | Digital Ground                               |
+-------+------------+--------------------------------------------------+-------+------------------+----------------------------------------------+

4G mini-PCIE & SIM Card Slot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------+------------+------------------------------------------------+
| Name          | Silkscreen | Interface Attribute                            |
+---------------+------------+------------------------------------------------+
| 4G mini-PCIE  | J5         | miniPCIE Standard Interface, PCIe 2.0 Standard |
+---------------+------------+------------------------------------------------+
| SIM Card Slot | P2         | Connect to 4G SIM Card                         |
+---------------+------------+------------------------------------------------+

|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-J5.png
   :alt: LS1012A-J5.png

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-P2.png
   :alt: LS1012A-P2.png

K20-JTAG
~~~~~~~~~~

|  Silkscreen: J8
|  Interface Attribute: K20-JTAG Programming Module Interface
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/963px-LS1012A-J8.png
   :alt: 963px-LS1012A-J8.png

+-------+---------------+--------------------------+-------+----------------+-------------------+
| Pin   | Signal        | Description              | Pin   | Signal         | Description       |
+-------+---------------+--------------------------+-------+----------------+-------------------+
| J8-1  | DUT_UART_SOUT | Debug Serial Port Output | J8-2  | PROC_TMS       | Test Mode Select  |
+-------+---------------+--------------------------+-------+----------------+-------------------+
| J8-3  | DUT_UART_SIN  | Debug Serial Port Input  | J8-4  | PROC_TCK       | Test Clock Output |
+-------+---------------+--------------------------+-------+----------------+-------------------+
| J8-5  | LSJTAG_TRST_B | LS1012A Reset Signal     | J8-6  | PROC_TDO       | Test Data Output  |
+-------+---------------+--------------------------+-------+----------------+-------------------+
| J8-7  | VCC_1V8       | 1.8V Output              | J8-8  | PROC_TDI       | Test Data Input   |
+-------+---------------+--------------------------+-------+----------------+-------------------+
| J8-9  | GND           | Digital Ground           | J8-10 | SDA_RST_TGTMCU | K20 Reset Signal  |
+-------+---------------+--------------------------+-------+----------------+-------------------+
| J8-11 | GND           | Digital Ground           | J8-12 | GND_DETECT     | Ground Detection  |
+-------+---------------+--------------------------+-------+----------------+-------------------+

SD Card Slot
~~~~~~~~~~~~~~

|  Silkscreen: J9
|  Interface Attribute: Standard SD Card Slot, Supports SD3.01, Speed Complies with UHS-1 Standard
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-J9.png
   :alt: LS1012A-J9.png

USB Expansion
~~~~~~~~~~~~~~~~

|  Silkscreen: J10
|  Interface Attribute: USB1 Expands to USB3.0 + USB2.0, USB TYPE-A Interface
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/963px-LS1012A-J10.png
   :alt: 963px-LS1012A-J10.png

Main Power Input & Switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------+------------+------------------------------------------------------------+
| Name              | Silkscreen | Interface Attribute                                        |
+-------------------+------------+------------------------------------------------------------+
| Main Power Input  | J11        | Jack with Positive Inside and Negative Outside, 5V Voltage |
+-------------------+------------+------------------------------------------------------------+
| Main Power Switch | J12        | Power Switch                                               |
+-------------------+------------+------------------------------------------------------------+

|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/963px-LS1012A-J11&J12.png
   :alt: 963px-LS1012A-J11&J12.png

Ethernet Port
~~~~~~~~~~~~~~~

+-----------------+------------+------------------------------------+
| Name            | Silkscreen | Interface Attribute                |
+-----------------+------------+------------------------------------+
| Ethernet Port 1 | U1         | ETH1, SGMII, Supports 10/100/1000M |
+-----------------+------------+------------------------------------+
| Ethernet Port 0 | U2         | ETH0, SGMII, Supports 10/100/1000M |
+-----------------+------------+------------------------------------+

|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-U1.png
   :alt: LS1012A-U1.png

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-U2.png
   :alt: LS1012A-U2.png

LORA Module
~~~~~~~~~~~~~

|  Silkscreen: U23
|  Interface Attribute: LORA Module, Serial Communication
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012A-U23.png
   :alt: LS1012A-U23.png

+------------------------------------+----------+----------------------------------+
| Pin                                | Signal   | Attribute                        |
+------------------------------------+----------+----------------------------------+
| U23-1, 2, 3, 4, 11, 13, 19, 20, 22 | GND      | Digital Ground                   |
+------------------------------------+----------+----------------------------------+
| U23-12, 14, 15, 16, 17, 18, 21     | NC       | No Connection                    |
+------------------------------------+----------+----------------------------------+
| U23-10                             | 5VIN     | Module 5V Input                  |
+------------------------------------+----------+----------------------------------+
| U23-9                              | LoRa_AUX | Module Working Status Indication |
+------------------------------------+----------+----------------------------------+
| U23-8                              | LoRa_RX  | Module TTL Serial Port Input     |
+------------------------------------+----------+----------------------------------+
| U23-7                              | LoRa_TX  | Module TTL Serial Port Output    |
+------------------------------------+----------+----------------------------------+
| U23-6                              | LoRa_M1  | Module Working Mode Control      |
+------------------------------------+----------+----------------------------------+
| U23-5                              | LoRa_M0  | Module Working Mode Control      |
+------------------------------------+----------+----------------------------------+

WIFI/BT Module
~~~~~~~~~~~~~~~~

|  Silkscreen: U24
|  Interface Attribute: WIFI/BT Module, USB Communication
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/963px-LS1012A-U24.png
   :alt: 963px-LS1012A-U24.png

+-------+------------+-------------------+
| Pin   | Signal     | Attribute         |
+-------+------------+-------------------+
| U24-1 | GND        | Digital Ground    |
+-------+------------+-------------------+
| U24-2 | ANT        | Antenna Interface |
+-------+------------+-------------------+
| U24-3 | VCC_3.3V   | Module 3.3V Input |
+-------+------------+-------------------+
| U24-4 | WIFI_USBDM | USB Data Positive |
+-------+------------+-------------------+
| U24-5 | WIFI_USBDP | USB Data Negative |
+-------+------------+-------------------+
| U24-6 | GND        | Digital Ground    |
+-------+------------+-------------------+

ZIGBEE Module
~~~~~~~~~~~~~~~

|  Silkscreen: U26
|  Interface Attribute: ZIGBEE Module, Serial Communication
|  The pin and signal definitions are as follows:

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/963px-LS1012A-U26.png
   :alt: 963px-LS1012A-U26.png

+--------+-----------------+------------------------------------------+--------+-------------+------------------------------------------+
| Pin    | Signal          | Attribute                                | Pin    | Signal      | Attribute                                |
+--------+-----------------+------------------------------------------+--------+-------------+------------------------------------------+
| U26-1  | GND             | Digital Ground                           | U26-11 | ZigBee_TX   | Module TTL Serial Port Input             |
+--------+-----------------+------------------------------------------+--------+-------------+------------------------------------------+
| U26-2  | VCC_3.3V        | Module 3.3V Input                        | U26-12 | RUN_LED     | Indicates Module Normal Operation Status |
+--------+-----------------+------------------------------------------+--------+-------------+------------------------------------------+
| U26-6  | ZigBee_Baud_RST | Restores Serial Port Baud Rate to 115200 | U26-13 | NWK_LED     | Indicates Module Network Access Status   |
+--------+-----------------+------------------------------------------+--------+-------------+------------------------------------------+
| U26-7  | ZigBee_AT_HEX   | Switches Command Mode                    | U26-24 | ZigBee_nRST | Module Reset                             |
+--------+-----------------+------------------------------------------+--------+-------------+------------------------------------------+
| U26-10 | ZigBee_RX       | Module TTL Serial Port Output            |        |             |                                          |
+--------+-----------------+------------------------------------------+--------+-------------+------------------------------------------+
