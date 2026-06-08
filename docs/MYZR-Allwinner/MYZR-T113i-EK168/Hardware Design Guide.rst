Hardware Design Guide
=======================

Schematic Diagram
--------------------

BOOT
~~~~~~

|  The T113-i core board supports booting from Micro SD, NAND FLASH, and eMMC respectively. The boot mode can be changed through a DIP switch (SW3).

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导1.png
   :alt: 硬件设计指导1.png
   :width: 90%

**Design Points**:

1. ESD protection components must be added at the DIP switch.
2. The BOOT signal of the T113-i is at a high level by default. As shown in the figure below, the high/low level of the BOOT signal is controlled through the DIP switch to select the BOOT mode.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导2.png
   :alt: 硬件设计指导2.png
   :width: 90%

UART
~~~~~~

Debug
^^^^^^^

|  The CH340T chip is used to convert UART0 to a Type-C interface, which serves as the system debugging serial port.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导3.png
   :alt: 硬件设计指导3.png
   :width: 90%

**Design Points**:

1. To prevent the RX terminal from being charged before the baseboard is powered on and injecting current into the CPU (which may affect the normal startup of the CPU), a level conversion chip must be added for isolation during the baseboard design.
2. The CH340T uses an external 5V power supply, and pin 5 (V3) of the CH340T chip must be connected to a capacitor to GND.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导4.png
   :alt: 硬件设计指导4.png
   :width: 90%

3. The CH340T requires a 12MHz crystal oscillator, and two matching capacitors must be added to both ends of the crystal oscillator respectively. The capacitance value should be selected according to the CH340T chip datasheet.
4. ESD protection components must be added at the Type-C connector.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导5.png
   :alt: 硬件设计指导5.png
   :width: 90%

TTL
^^^^^

|  UART4 and UART5 are used as TTL serial ports, with a 4-pin white terminal interface and a pin pitch of 2.54mm.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导6.png
   :alt: 硬件设计指导6.png
   :width: 90%

**Design Points**:

1. Check if the UART signal is at a high level by default; if not, a pull-up resistor must be added.
2. ESD protection components must be added at the TTL terminal.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导7.png
   :alt: 硬件设计指导7.png
   :width: 90%

RS232
^^^^^^^

|  A RS232 transceiver is used to convert UART2 to a RS232 serial port, which uses a 9-pin DB9 interface.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导8.png
   :alt: 硬件设计指导8.png
   :width: 90%

1. UART2 is converted to a RS232 serial port using a 9-pin DB9 interface.
2. ESD protection components must be added at the RS232 terminal.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导9.png
   :alt: 硬件设计指导9.png
   :width: 90%

RS485
^^^^^^^

|  Two isolated transceivers (CA-IS3082WX) are used to convert UART1 and UART3 to RS485 serial ports respectively. These ports share a 12-pin green Phoenix terminal (J3) with a pitch of 3.81mm together with CAN0 and CAN1.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导10.png
   :alt: 硬件设计指导10.png
   :width: 90%

**Design Points**:

1. This circuit diagram adopts self-transceiving mode. Note that the RS1G14XC5 (inverter) has a certain delay time, which may affect high-speed communication and is not suitable for communication scenarios with high baud rates.
2. A 120Ω terminal matching resistor must be added for RS485.
3. ESD protection components must be added at the RS485 terminal.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导11.png
   :alt: 硬件设计指导11.png
   :width: 90%

4. RS485 and CAN use an isolated power supply, and the maximum current of this isolated power supply is 200mA.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导12.png
   :alt: 硬件设计指导12.png
   :width: 90%

CAN
~~~~~~

|  Two isolated transceivers (NSI1050-DDBR) are used to lead out the CAN0 and CAN1 interfaces. These interfaces share a 12-pin green Phoenix terminal (J3) with a pitch of 3.81mm together with RS485 UART1 and RS485 UART3.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导10.png
   :alt: 硬件设计指导10.png
   :width: 90%

1. A 120Ω terminal matching resistor must be added for CAN.
2. A power isolation module must be added.
3. ESD protection components must be added at the CAN terminal.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导13.png
   :alt: 硬件设计指导13.png
   :width: 90%


RTC
~~~~~

|  An external RTC chip (U13) is used to implement the RTC function. CON6 is an RTC button battery holder, which is compatible with button batteries ML2032 (3V rechargeable) and CR2032 (3V non-rechargeable). When using a rechargeable battery, a jumper cap can be inserted into the J1 interface to enable charging. When using a non-rechargeable battery, do not insert a jumper cap into the J1 interface.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导14.png
   :alt: 硬件设计指导14.png
   :width: 90%

**Design Points**:

1. Check if pull-up resistors are added to the I2C signals; if not, pull-up resistors must be added.
2. J1 in the figure can be used to charge the button battery, but D4 (Schottky diode) must be connected to prevent current from flowing back into the button battery.
3. Positions for matching capacitors can be reserved at both ends of the crystal oscillator.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导15.png
   :alt: 硬件设计指导15.png
   :width: 90%

KEY
~~~~~

|  The system includes the following buttons: CPU RESET (KEY0) for system reset, USB0 UPGRADE (KEY1), and USER (KEY2) for user input.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导16.png
   :alt: 硬件设计指导16.png
   :width: 90%

**Design Points**:

1. Reserve positions for pull-up resistors for the RESET signal and FEL signal to facilitate later debugging.
2. Reserve positions for capacitors for the RESET signal and FEL signal to adjust the power-on time later.
3. ESD protection components must be added at the buttons.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导17.png
   :alt: 硬件设计指导17.png
   :width: 90%

WatchDog
~~~~~~~~~~

|  An external chip (U14) is used to implement the Watchdog function. A 3-pin pin header (J2) with a pitch of 2.54mm is led out as the Watchdog function configuration interface, and the Watchdog function can be enabled through jumper cap configuration. On the software side, the Watchdog timeout duration can be configured through the V1/PE0/WD_SET0/NCSI0_HSYNC/3V3 pin.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导18.png
   :alt: 硬件设计指导18.png
   :width: 90%

**Design Points**:

1. When using the MAX6369KA+T chip, the Watchdog startup delay time and monitoring time can be adjusted through the voltage levels of pins 4, 5, and 6. Customers can modify these settings according to their own needs. The table in the figure is for reference only; please refer to the chip datasheet for specific details.
2. The WatchDog function can be enabled or disabled through the J2 pin header.
3. ESD protection components must be added at the pin header.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导19.png
   :alt: 硬件设计指导19.png
   :width: 90%

SD
~~~~

|  CON7 is a Micro SD card interface, which is led out through the SDC0 bus and adopts a 4-bit data line mode.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导20.png
   :alt: 硬件设计指导20.png
   :width: 90%

**Design Points**:

1. It is recommended to use VDD_3V3_SOM output by the core board to power the Micro SD (CON7) to meet the power-on sequence requirements. This avoids failure of the CPU to correctly recognize the SD card device and subsequent startup failure due to delayed power supply to the Micro SD.
2. ESD protection components must be added at the TF card holder.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导21.png
   :alt: 硬件设计指导21.png
   :width: 90%

3. There is a pin multiplexing relationship between the ARM/RISC-V JTAG and the SDC0 bus; these two modules cannot be used simultaneously.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导22.png
   :alt: 硬件设计指导22.png
   :width: 90%

JTAG
~~~~~~

|  CON8 is the JTAG interface for the ARM and RISC-V ends, and CON12 is the JTAG interface for the HiFi4 DSP end. The interfaces use 2x7pin terminals with a pitch of 2.0mm.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导23.png
   :alt: 硬件设计指导23.png
   :width: 90%

**Design Points**:

1. ESD protection components must be added at the JTAG terminal.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导24.png
   :alt: 硬件设计指导24.png
   :width: 90%

USB
~~~~~

USB0 DRD
^^^^^^^^^^^

|  The USB0 DRD (CON4) interface is led out through the USB0 bus, supporting DRD mode, high-speed mode (480Mbps), full-speed mode (12Mbps), and low-speed mode (1.5Mbps).

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导25.png
   :alt: 硬件设计指导25.png
   :width: 90%

**Design Points**:

1. Check if pull-up resistors are added to the I2C and interrupt pins.
2. The Type-C CC signal can control the USB2.0 ID signal through the WUSB3801Q-12/TR (U11) chip to realize master-slave switching control. If the B5819WS-SL solution is adopted, please actually mount B5819WS-SL (D3), 0Ω resistor (R38), and 100K resistor (R40), and leave WUSB3801Q-12/TR (U11), 100K resistor (R39), 10K resistor (R41), 0Ω resistor (R274), and 100nF capacitor (C42) unmounted.
3. ESD protection components must be added at the Type-C connector.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导26.png
   :alt: 硬件设计指导26.png
   :width: 90%

USB HUB
^^^^^^^^^

|  A USB HUB chip is used to expand the USB1 bus into 4 USB HOST buses.

**Design Points**:

1. Check if a pull-up resistor is added to the RESET pin; it is not recommended to leave it completely floating.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导27.png
   :alt: 硬件设计指导27.png
   :width: 90%

USB HOST
""""""""""

|  A USB HUB chip is used to expand the USB1 bus into 4 USB HOST buses, and one of the buses is led out to the USB1 HOST interface. CON22 (USB1 HOST) is a USB2.0 HOST interface, which uses a single-layer Type-A connector.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导28.png
   :alt: 硬件设计指导28.png
   :width: 90%

**Design Points**:

1. Overcurrent protection must be added.
2. ESD protection components must be added at the Type-A connector.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导29.png
   :alt: 硬件设计指导29.png
   :width: 90%

WIFI
""""""

|  A USB HUB chip is used to expand the USB1 bus into 4 USB HOST buses, and one of the buses is led out for WIFI module expansion. The onboard WIFI module (U47) is model B-Link BL-R8723DU1, which adopts a stamp hole connection method. CON24 is an SMA interface for connecting an external 2.4G antenna of the WIFI module.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导30.png
   :alt: 硬件设计指导30.png
   :width: 90%

**Design Points**:

1. ESD protection components must be added at the antenna connector.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导31.png
   :alt: 硬件设计指导31.png
   :width: 90%

4G
""""

|  CON25 is a 4G module expansion interface, which uses a Mini PCIe slot. The evaluation baseboard uses a USB HUB chip to expand the USB1 bus into 4 USB HOST buses, and one of the buses is led out for 4G module expansion. CON23 is a Micro SIM card holder, which adopts a self-popping card insertion method and has no detection pins.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导32.png
   :alt: 硬件设计指导32.png
   :width: 90%

**Design Points**:

1. Determine the current and stable voltage required by the 4G module; an independent DCDC module must be added for power supply.
2. ESD protection components must be added at the SIM card holder.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导33.png
   :alt: 硬件设计指导33.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导34.png
   :alt: 硬件设计指导34.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导35.png
   :alt: 硬件设计指导35.png
   :width: 90%

USB ETH1
""""""""""

|  CON21 is an ETH1 (USB1) 100M Ethernet port, which uses an RJ45 connector with a built-in isolation transformer. A USB HUB chip is used to expand the USB1 bus into 4 USB HOST buses, and the SR9900AI chip is used to expand one of the buses into an ETH1 (USB1) 100M Ethernet port.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导36.png
   :alt: 硬件设计指导36.png
   :width: 90%

**Design Points**:

1. A 2.49K (±1%) resistor must be connected to the RSET pin of the SR9900AI chip.
2. The DVDD12_UPS pin of the SR9900AI chip is a backup power pin, and R241 must be left unmounted.
3. When configuring the LED signals of the Ethernet connector, pay attention to the cathode and anode of the LEDs.
4. ESD protection components must be added at the Ethernet connector.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导37.png
   :alt: 硬件设计指导37.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导38.png
   :alt: 硬件设计指导38.png
   :width: 90%

RGMII
~~~~~~~

|  CON20 is an ETH0 (RGMII) Gigabit Ethernet port, and the RJ45 connector has a built-in isolation transformer.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导39.png
   :alt: 硬件设计指导39.png
   :width: 90%
  
**Design Points**:

1. Check if the I/O level of the RGMII signal on the core board matches the I/O level of the PHY chip. The I/O level of the RGMII signal of T113I is 3V3, so the I/O level of the PHY chip must be configured to 3V3. As shown in the table below (for reference only; please refer to the chip datasheet for specific details), the CFG_LDO[1:0] signals need to be configured to low levels.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导40.png
   :alt: 硬件设计指导40.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导41.png
   :alt: 硬件设计指导41.png
   :width: 90%

2. The LEDs of the Ethernet connector are also controlled by the CFG_LDO[1:0] signals. Therefore, when configuring the LED signals, pay attention to whether the I/O level configuration of the PHY chip will be changed. The LEDs can be configured according to the table below (for reference only).

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导42.png
   :alt: 硬件设计指导42.png
   :width: 90%

3. Configure the PHY address. If multiple PHYs share one MAC, different PHY addresses need to be configured.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导43.png
   :alt: 硬件设计指导43.png
   :width: 90%

4. The PHY chip can be configured with multiple modes.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导44.png
   :alt: 硬件设计指导44.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导45.png
   :alt: 硬件设计指导45.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导46.png
   :alt: 硬件设计指导46.png
   :width: 90%

5. The signal levels of pins LED0/PHYAD0, LED1/CFG_LDO0, LED2/CFG_LDO1, and RESET_N of the YT8521SH-CA chip are all 3.3V. For pull-up configuration, use 3.3V for pull-up; for pull-up configuration of other signal pins, use the DVDD_RGMII (1.8V/2.5V/3.3V) power supply for pull-up.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导46-1.png
   :alt: 硬件设计指导46-1.png
   :width: 90%

6. Check if pull-up resistors are added to the reset, interrupt, and MDIO signals. The resistance value of the pull-up resistor for the MDIO signal should be checked in the PHY chip datasheet. At the same time, pay attention to the power-on sequence of the RESET pin of the PHY chip; after the PHY chip is powered on stably, the RESET signal must be maintained for at least 10ms (please refer to the chip datasheet for specific details). A 2.49K (±1%) resistor must be connected from the RBIAS pin to GND.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导47.png
   :alt: 硬件设计指导47.png
   :width: 90%

7. A 25MHz passive crystal oscillator is connected to the XTAL_I and XTAL_O pins. If a 25MHz active crystal oscillator needs to be used, it can be connected from the XTAL_I pin, and the XTAL_O pin should be left floating.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导48.png
   :alt: 硬件设计指导48.png
   :width: 90%

8. Determine whether the PHY chip is voltage-driven or current-driven. If it is voltage-driven, connect the center tap (pin 1) of the RJ45 connector to the power supply; if it is current-driven, directly connect a capacitor to GND.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导49.png
   :alt: 硬件设计指导49.png
   :width: 90%

9. ESD protection components must be added at the Ethernet connector.

LVDS
~~~~~~

|  CON14 is a dual-channel 8-bit LVDS LCD interface, which uses a 2x15pin double-row pin header with a pitch of 2.0mm, including LVDS signals and power supply. CON15 is a backlight control interface, which uses a 6-pin white terminal block with a pitch of 2.54mm. J4 is a resistive touch screen interface, which uses a 4-pin pin header with a pitch of 2.54mm.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导50.png
   :alt: 硬件设计指导50.png
   :width: 90%

**Design Points**:

1. 100Ω terminal resistors can be reserved for LVDS differential signals.
2. Since LVDS0 and LVDS1 are multiplexed with LCD0 (RGB) pins, and LVDS0 is multiplexed with MIPI_DSI pins, and HDMI is led out by converting MIPI_DSI through LT8912B (U27), only one of the MIPI_DSI, HDMI, LVDS, and RGB interfaces can be used at the same time.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导51.png
   :alt: 硬件设计指导51.png
   :width: 90%

3. The LVDS and RGB interfaces share the four-wire resistive touch signals C12/TP_X1, A11/TP_X2, B11/TP_Y1, and C11/TP_Y2. Do not connect two types of display devices at the same time.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导52.png
   :alt: 硬件设计指导52.png
   :width: 90%

RGB
~~~~~

|  CON13 is an RGB interface, which leads out an 18-bit RGB666 parallel bus through a 40-pin FPC connector with a pitch of 0.5mm.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导53.png
   :alt: 硬件设计指导53.png
   :width: 90%

**Design Points**:

1. Since LVDS0 and LVDS1 are multiplexed with LCD0 (RGB) pins, and LVDS0 is multiplexed with MIPI_DSI pins, and HDMI is led out by converting MIPI_DSI through LT8912B (U27), only one of the MIPI_DSI, HDMI, LVDS, and RGB interfaces can be used at the same time.
2. The LVDS and RGB interfaces share the four-wire resistive touch signals C12/TP_X1, A11/TP_X2, B11/TP_Y1, and C11/TP_Y2. Do not connect two types of display devices at the same time.
3. The P3/PE10/PWM4/BL_PWM/NCSI0_D6/3V3 pin outputs PWM to control the LCD backlight, and an external 10K pull-down resistor to GND is reserved.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导54.png
   :alt: 硬件设计指导54.png
   :width: 90%

MIPI_DSI
~~~~~~~~~~

|  CON16 is a MIPI_DSI interface, which uses a 30-pin FPC connector with a pitch of 0.5mm.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导55.png
   :alt: 硬件设计指导55.png
   :width: 90%

**Design Points**:

1. Since LVDS0 and LVDS1 are multiplexed with LCD0 (RGB) pins, and LVDS0 is multiplexed with MIPI_DSI pins, and HDMI is led out by converting MIPI_DSI through LT8912B (U27), only one of the MIPI_DSI, HDMI, LVDS, and RGB interfaces can be used at the same time.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导56.png
   :alt: 硬件设计指导56.png
   :width: 90%

HDMI
~~~~~~

|  CON17 is an HDMI OUT interface, which is led out by converting MIPI DSI through LT8912B (U27) and uses a standard HDMI female connector.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导57.png
   :alt: 硬件设计指导57.png
   :width: 90%

**Design Points**:

1. Since LVDS0 and LVDS1 are multiplexed with LCD0 (RGB) pins, and LVDS0 is multiplexed with MIPI_DSI pins, and HDMI is led out by converting MIPI_DSI through LT8912B (U27), only one of the MIPI_DSI, HDMI, LVDS, and RGB interfaces can be used at the same time.
2. The maximum input voltage of the data signal pins of the LT8912B chip is 2.2V. If the MIPI_DSI to HDMI multiplexing solution is adopted, there may be a risk of damaging the LT8912B. Please use an analog switch chip DI01647 (for reference only; the input pins can withstand a maximum voltage greater than 3.3V) for isolation.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导58.png
   :alt: 硬件设计指导58.png
   :width: 90%

3. Pay attention to whether the I2C levels match; a level conversion chip can be used for connection.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导59.png
   :alt: 硬件设计指导59.png
   :width: 90%

4. ESD protection components must be added at the HDMI connector.

CVBS
~~~~~~

|  J8 is a CVBS OUT interface, which is led out from TVOUT0. J6 and J7 are CVBS IN interfaces, which are led out from TVIN0 and TVIN1 respectively. They all use RCA lotus connectors.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导60.png
   :alt: 硬件设计指导60.png
   :width: 90%

CVBS_IN
^^^^^^^^^^

**Design Points**:

1. Pay attention to the TVIN-Vth voltage, which determines the resistance values of R1 and R2 and whether R2 is left unmounted.
2. ESD protection components must be added at the CVBS_IN connector.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导61.png
   :alt: 硬件设计指导61.png
   :width: 90%

CVBS_OUT
^^^^^^^^^^

**Design Points**:

1. ESD protection components must be added at the CVBS_OUT connector.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导62.png
   :alt: 硬件设计指导62.png
   :width: 90%

Audio
~~~~~~~

|  CON18 is a LINE_IN audio interface, and CON19 is an HP/MIC audio interface, both using 4-segment 3.5mm audio jacks.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导63.png
   :alt: 硬件设计指导63.png
   :width: 90%

HP/MIC
^^^^^^^^^

**Design Points**:

1. Check if the MIC has a bias voltage.
2. Insertion pin configuration: If R384 and R386 are actually mounted, and R385 and R169 are left unmounted, the HP_DET pin is at a high level when the headphone is unplugged and at a low level when the headphone is plugged in. If R385 and R169 are actually mounted, and R384 and R386 are left unmounted, the HP_DET pin is at a low level when the headphone is unplugged and at a high level when the headphone is plugged in. Note that the HP_DET pin should not be left floating, as this may cause unstable pin levels and susceptibility to interference, thereby affecting the normal use of audio.
3. ESD protection components must be added at the audio jack.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导64.png
   :alt: 硬件设计指导64.png
   :width: 90%

LINE IN
^^^^^^^^^^

**Design Points**:

1. ESD protection components must be added at the audio jack.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导65.png
   :alt: 硬件设计指导65.png
   :width: 90%

Power Supply
~~~~~~~~~~~~~~~

|  CON1 is a 12V DC input DC-005 power interface, which can be connected to a power plug with an outer diameter of 5.5mm and an inner diameter of 2.1mm. CON2 is a 12V DC input green Phoenix terminal, with 3 pins and a pitch of 3.81mm. The power input has reverse connection protection, overcurrent protection, and overvoltage protection functions. SW1 is a power toggle switch.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导66.png
   :alt: 硬件设计指导66.png
   :width: 90%

**Design Points**:

1. VDD_12V_MAIN outputs VDD_5V_SOM through a DC-DC chip for the core board, and outputs VDD_5V_MAIN, VDD_3V3_MAIN, and VDD_1V8_MAIN through three other DC-DC chips for the peripherals of the evaluation baseboard.
2. The VDD_5V_SOM does not have a reserved large energy storage capacitor for the main power input inside the core board. During the baseboard design, the large capacitor should be placed close to the pad of VDD_5V_SOM.
3. M2/RESETn is the reset input/output pin of the CPU, which will be pulled up to a high level 92.5ms after the VDD_5V_SOM power input. If the baseboard peripherals use M2/RESETn as the system reset signal, pay attention to the power-on sequence design.
4. To ensure that VDD_5V_MAIN, VDD_3V3_MAIN, and VDD_1V8_MAIN meet the system power-on and power-off sequence requirements, the VDD_3V3_SOM output by the core board must be used to control the power enable, so that the VDD_5V_MAIN, VDD_3V3_MAIN, and VDD_1V8_MAIN power supplies of the development board are powered on later than the core board power supply.
5. Pay attention to adding overcurrent protection, overvoltage protection, reverse input protection, and fast discharge.
6. A TVS protection component (D2) must be added at the power input.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导67.png
   :alt: 硬件设计指导67.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导68.png
   :alt: 硬件设计指导68.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导69.png
   :alt: 硬件设计指导69.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导70.png
   :alt: 硬件设计指导70.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导71.png
   :alt: 硬件设计指导71.png
   :width: 90%
  
PCB
------

**PCB Layout Key Points**:

1. Ensure that the power lines and ground lines have sufficient width throughout the loop to enable fast power return.
2. Ensure the integrity of the ground plane and the continuity of the GND plane as much as possible.
3. Capacitors should be placed as close to the chip pins as possible to enable fast return. Generally, capacitors with smaller capacitance values are placed first, followed by those with larger values.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导72.png
   :alt: 硬件设计指导72.png
   :width: 90%

4. Separate digital ground and analog ground.
5. ESD protection components should be placed as close to the interface as possible.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导73.png
   :alt: 硬件设计指导73.png
   :width: 90%

6. For unshielded inductors, copper cutting is required, and the cutting should extend to the ground plane. No routing is allowed below the inductor.
7. Ground can be laid below the integrated inductors.
8. The routing of clock and high-speed signals should be at least 250mil away from the edge of the board, and at least 500mil away from switching power supply inductors and MOS tubes.
9. The clock should be adjacent to a complete ground plane; ground shielding should be implemented if necessary.
10. No other signal lines should be routed near or below the crystal oscillator; it is best to shield the crystal oscillator with ground.
11. Reset signals should be kept away from clock lines and switching power supply switching circuits.
12. Impedance Recommendations

+------------------------------------------------------+-------------------+-----------+
| Signal Group                                         | Impedance         | Tolerance |
+------------------------------------------------------+-------------------+-----------+
| Single-ended signals with no special requirements    | 50Ω Single-ended  | ±10%      |
+------------------------------------------------------+-------------------+-----------+
| USB differential signals                             | 90Ω Differential  | ±10%      |
+------------------------------------------------------+-------------------+-----------+
| Differential signals (including Ethernet, DSI, LVDS) | 100Ω Differential | ±10%      |
+------------------------------------------------------+-------------------+-----------+

13. High-speed Differential Signals

- Avoid discontinuous routing impedance.
- If high-speed signal lines are too close to each other, crosstalk is likely to occur; increase the spacing between routing lines as much as possible.
- The DP and DM routing lines should have equal spacing, equal width, and equal length. Strict time delay must be ensured between the two signal lines of high-speed differential signal pairs; otherwise, communication failure may occur. Therefore, to meet this requirement, serpentine lines can be used to achieve equal length, thereby meeting the time delay requirement.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导74.png
   :alt: 硬件设计指导74.png
   :width: 90%

- When a signal is used for multiple multiplexing functions and requires equal length, a Pin Pair from the start end of the signal to the terminal of the module must be established, and then the Pin Pair is used to achieve equal length.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导75.png
   :alt: 硬件设计指导75.png
   :width: 90%

- Vias or components are not allowed to be placed within differential line pairs.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导76.png
   :alt: 硬件设计指导76.png
   :width: 90%

- The DP and DM routing lines should not cross plane splits or gaps in the reference plane.
- The DP and DM routing lines should not cross other signals. If they must cross, place a digital power plane or ground plane between them.
- Minimize the number of bends in the DP and DM routing lines. If a 90° bend is required, replace it with two 45° bends.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导77.png
   :alt: 硬件设计指导77.png
   :width: 90%

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导78.png
   :alt: 硬件设计指导78.png
   :width: 90%

- To prevent noise, minimize the number of bends and vias in the DP and DM routing lines, and these signal lines should be routed on a solid GND reference plane. The DP and DM routing lines should have the same number of vias. Avoid vias and layer changes as much as possible. It is recommended to use the top or bottom layer for signal line routing.
- The DP and DM should be kept away from other signals. Pay special attention to the noise from clock and data buses.
- The two sides of the DP and DM routing lines should preferably be shielded by the GND plane.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导79.png
   :alt: 硬件设计指导79.png
   :width: 90%

- Place the GND loop vias adjacent to the differential pair vias.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导80.png
   :alt: 硬件设计指导80.png
   :width: 90%

- The return path should be continuous with the ground. That is, the return path is usually realized through the ground (GND). To ensure effective and stable current return, the ground line (GND) should be kept as continuous as possible to avoid splits or interruptions.

14. USB 2.0

- The USB high-speed signal routing between the chip and the connector should be as short as possible.
- The USB routing length should not be too long, and the length error of signals within the differential pair should not exceed 0.12mm.
- The spacing between high-speed clock and periodic signal routing lines parallel to the DP and DM should be at least 50mil (1.27mm).
- The spacing between low-speed and aperiodic signal routing lines should be at least 20mil (0.51mm).
- The spacing between the DP and DM (within the same pair) routing lines should be at least 7.5 mils (0.2mm).
- The spacing between the DP and DM (differential pair) routing lines should be no less than 20mil (0.51mm).

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导81.png
   :alt: 硬件设计指导81.png
   :width: 90%

15. Ethernet

- When multiple PHY chips are mounted on the MDIO bus, use a series connection method; do not use branched routing.
- The RGMII interface is divided into transmit signals, receive signals, and control signals, and the impedance of each group is controlled within 50Ω±10%.
- The routing length of transmit signals and receive signals should not exceed 100mm, and the length error of signals within the group should not exceed 2.54mm.
- The MDI interface adopts differential routing with an impedance of 100Ω±10%.
- The differential error within the MDI group should not exceed 0.12mm.
- The power inductor connected to the internal DCDC of the chip should be placed close to the chip to ensure the shortest loop and the integrity of the ground loop.
- The series resistors reserved on the data lines should be placed close to the source end.

16. CAN

- CAN uses differential routing, and a 120Ω terminal resistor is reserved.
- It is recommended to reserve a ground signal for the connection port.

17. 485

- 485 uses differential routing, and a 120Ω terminal resistor is reserved.
- The 485 bus adopts half-duplex mode for transmission, and transceiving control is required.
- It is recommended to reserve a ground signal for the connection port.

18. AUDIO

- Audio signals are analog signals and need to be isolated from digital signals; ground shielding should be implemented if necessary to ensure the integrity of the reference ground.
- When routing analog signals, the line width should be as thick as possible.

19. WIFI

- The WIFI antenna signal should be shielded with ground.
- The routing width should be thick. There should be no 90° or 45° bends; straight lines are preferred. If bends are necessary, use arc routing.
- The signal lines should be kept as far away from the WIFI module as possible.

.. figure:: /image/MYZR-全志系列/MYZR-T113-i-EK168/硬件设计指导82.png
   :alt: 硬件设计指导82.png
   :width: 90%

Debugging
------------

**General Troubleshooting Ideas When Problems Occur During Debugging**:

1. Check the soldering for issues such as cold soldering, bridged soldering, missing soldering, and wrong soldering. Especially for polarized components, check if their orientation is correct.
2. Check if the pin numbers of the physical component match the PCB package.
3. Refer to the chip datasheet to check the schematic diagram, the correctness of signal line connections, and the matching of IO levels.
4. Confirm whether the component selection meets the circuit requirements.
5. Measure whether the power voltage, clock, enable terminal, and the voltage of pins requiring pull-up or pull-down resistors are correct.
6. Pay attention to chips that have power-on sequence requirements. Sometimes the voltage is normal, but the sequence does not meet the requirements, which may also cause the chip to fail to work normally.
7. Check whether the PCB routing and layout are reasonable. Check whether the power line and via sizes meet the current requirements, and also pay attention to the strict layout requirements for important signals such as crystal oscillators and differential signals.
8. Measure whether the pin signals are normal and record the signal waveforms.
9. Confirm whether the pins are multiplexed.
10. Check whether the components are damaged.

|  It is best to have multiple boards for comparative experiments during debugging. When a problem occurs, do not measure the circuit blindly; instead, have a basis and measure according to the circuit schematic diagram. During detection, you can start from the input end to the output end, or from the output end to the input end, but it is best not to skip levels for measurement, as this may disrupt the thinking and lead to missed measurements, making it difficult to analyze the error in the end. Record the measured waveforms and analyze the problem in combination with the chip datasheet.

**Points to Note During Debugging**:

1. Prevent static electricity. Before touching the board, touch a metal object to discharge static electricity.
2. Before powering on, perform a short-circuit test on each power supply on the board, and check whether the power voltage is correct and whether the positive and negative poles are connected correctly.
3. Check whether the BOOT mode is correct.
