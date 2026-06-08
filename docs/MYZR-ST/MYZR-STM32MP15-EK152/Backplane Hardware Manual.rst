Backplane Hardware Manual
===========================

Interface Overview
~~~~~~~~~~~~~~~~~~~~

Front View
""""""""""""

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/963px-Stm32_mp157_zheng.jpg
   :alt: 963px-Stm32_mp157_zheng.jpg

Rear View
"""""""""""

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/963px-Stm32_mp157_bei.jpg
   :alt: 963px-Stm32_mp157_bei.jpg

Dimension Drawing
"""""""""""""""""""

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/963px-Stm32_mp157_chicun.png
   :alt: 963px-Stm32_mp157_chicun.png

Diagram Modules
~~~~~~~~~~~~~~~~~

+-----+----------------+--------------------------+--------------------------------+------------+
| No. | Interface      | Function                 | Interface Type                 | Silkscreen |
+-----+----------------+--------------------------+--------------------------------+------------+
| 1   | 5V_IN          | Power Input              | DC-005 Round Connector         | P1         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 2   | Ethernet       | 1x 10/100/1000M Ethernet | RJ45                           | U4         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 3   | DEBUG UART     | Debug Serial Port        | PH1.25 Pin Header (4-pin)      | P14        |
+-----+----------------+--------------------------+--------------------------------+------------+
| 4   | RS232          | RS232 Interface          | Screw Terminal Block           | P16        |
+-----+----------------+--------------------------+--------------------------------+------------+
| 5   | RS485          | RS485 Interface          | Screw Terminal Block           | P17        |
+-----+----------------+--------------------------+--------------------------------+------------+
| 6   | CAN            | CAN Interface            | Screw Terminal Block           | P13        |
+-----+----------------+--------------------------+--------------------------------+------------+
| 7   | 4G Module      | 4G Module Interface      | MINI-PCIE                      | P7         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 8   | SIM            | SIM Card                 | Micro SIM Pop-up Type          | P6         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 9   | TF             | TF Card                  | Standard TF Card Pop-up Socket | P3         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 10  | USB            | USB2.0                   | Double-Layer USB-A             | P5         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 11  | HDMI           | Video Interface          | Standard HDMI-A Port           | P8         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 12  | RGB            | RGB Display Interface    | FPC Connector (40-Pin)         | P9         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 13  | USER LIGHT     | User LED Lights          | SMD LED Lights (3 pcs)         | D3, D4, D5 |
+-----+----------------+--------------------------+--------------------------------+------------+
| 14  | Antenna        | WIFI & Bluetooth         | IPX Connector                  | E1         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 15  | USB            | BOOT LOADER              | Micro USB                      | P4         |
+-----+----------------+--------------------------+--------------------------------+------------+
| 16  | Audio          | Audio Output/Input       | 3.5mm Headphone Jack           | P10        |
+-----+----------------+--------------------------+--------------------------------+------------+
| 17  | Reset Button   | Reset                    | Tactile Pushbutton Switch      | SW1        |
+-----+----------------+--------------------------+--------------------------------+------------+
| 18  | Wake-Up Button | Wake-Up                  | Tactile Pushbutton Switch      | SW2        |
+-----+----------------+--------------------------+--------------------------------+------------+
| 19  | BOOT MODE      | Boot Mode Selection      | DIP Switch (3-position)        | SW3        |
+-----+----------------+--------------------------+--------------------------------+------------+


Interface Functions
~~~~~~~~~~~~~~~~~~~~~

Main Power Input
"""""""""""""""""""

|  Silkscreen: P1
|  Interface Attribute: Power Supply
|  Jack Polarity: Positive Inside, Negative Outside
|  Voltage: 5V
|  Current: 2A and Above

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_power.png
   :alt: Stm32_mp157_power.png

Reset
"""""""

|  Silkscreen: SW1
|  Function: Reset

Wake-Up
"""""""""

|  Silkscreen: SW2
|  Interface Attribute: Sleep Wake-Up

TF
"""

|  Silkscreen: P3
|  Interface Attribute: Standard Spring-Type TF Card Socket

RTC
""""""

|  Silkscreen: U3
|  Interface Attribute: Real-Time Clock with I2C Communication

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_rtc.png
   :alt: Stm32_mp157_rtc.png

RTC_Battery
"""""""""""""

|  Silkscreen: BT1

LED
"""""

|  Silkscreen: D3, D4, D5
|  Interface Attribute: IO Port

BOOT_MODE
"""""""""""

|  Silkscreen: SW3
|  Definition:

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_boot.png
   :alt: Stm32_mp157_boot.png

10M/100M/1000M Ethernet
"""""""""""""""""""""""""

|  Silkscreen: U4
|  Interface Attribute: Gigabit Ethernet Standard Interface

OTG
"""""

|  Silkscreen: P4
|  Interface Attribute: Standard Micro-USB Interface, USB On-The-Go (for Flashing)

USB
"""""

|  Silkscreen: P5
|  Interface Attribute: Standard USB Female Connector

MINI-PCIE
"""""""""""

|  Silkscreen: P7
|  Interface Attribute: Expanded MINI-PCIE Interface (for 4G Module)

SIM Card Socket
"""""""""""""""""

|  Silkscreen: P6
|  Interface Attribute: Standard Spring-Type SIM Card Socket

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_sim.png
   :alt: Stm32_mp157_sim.png

HDMI
""""""

|  Silkscreen: P8
|  Interface Attribute: HDMI-A Standard Interface

18/24bit RGB
""""""""""""""

|  Silkscreen: P9
|  The RGB display operates in 24-bit mode. This interface can be connected to the 7-inch RGB LCD display produced by Mingyuan Zhirui Company. The RGB LCD interface connector adopts an imported connector, replacing the low-cost domestic drawer-type connector with an opposite-press type, ensuring easier installation, better performance, and more reliable connectivity.
|  Pin and Signal Definition:

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_rgb.png
   :alt: Stm32_mp157_rgb.png

+---------------+----------------------+--------------------------+
| Interface Pin | Function Signal Name | Description              |
+---------------+----------------------+--------------------------+
| P9-10         | LTDC_TP_RST          | Touch Screen (Reset)     |
+---------------+----------------------+--------------------------+
| P9-11         | LTDC_TP_INT          | Touch Screen (Interrupt) |
+---------------+----------------------+--------------------------+
| P9-22         | LTDC_PWM             | Backlight Adjustment     |
+---------------+----------------------+--------------------------+
| P9-9          | LTDC_SCL             | Touch Screen I2C Clock   |
+---------------+----------------------+--------------------------+
| P9-8          | LTDC_SDA             | Touch Screen I2C Data    |
+---------------+----------------------+--------------------------+


WIFI & Bluetooth Antenna Socket
"""""""""""""""""""""""""""""""""

|  Silkscreen: E1
|  Interface Attribute: IPX Antenna Socket

WIFI & Bluetooth Module
"""""""""""""""""""""""""

|  Silkscreen: U12
|  Module Model: AP6214A

Headphone
"""""""""""

|  Silkscreen: P10
|  Interface Attribute: Audio Signal Output, Microphone Input, 3.5mm Jack

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_yin.png
   :alt: Stm32_mp157_yin.png

External Microphone
"""""""""""""""""""""

|  Silkscreen: P11
|  Interface Attribute: Audio Signal Input

External SPK (Speaker)
""""""""""""""""""""""""

|  Silkscreen: P12
|  Interface Attribute: Audio Signal Output

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_spk.png
   :alt: Stm32_mp157_spk.png

CAN
""""""

|  Silkscreen: P13
|  Interface Attribute: CAN

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_can.png
   :alt: Stm32_mp157_can.png

RS-485 Serial Port
""""""""""""""""""""

|  Silkscreen: P17
|  Interface Attribute: UART-based RS-485 Serial Port

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_485.png
   :alt: Stm32_mp157_485.png

RS-232 Serial Port
""""""""""""""""""""

|  Silkscreen: P14, P16
|  Interface Attribute: UART-based Standard RS232 Interface, where P14 is the Debug Serial Port.

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_232.png
   :alt: Stm32_mp157_232.png

GPIO, SPI, UART, ADC Expanded Pin Header
""""""""""""""""""""""""""""""""""""""""""

|  Silkscreen: P21

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32_mp157_kuo.png
   :alt: Stm32_mp157_kuo.png
