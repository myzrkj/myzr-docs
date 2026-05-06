Hardware Design Guidelines
============================

1. Boot/Download Selection Circuit
------------------------------------

| K1 supports booting from TF Card, EMMC, SPI NOR, SPI NAND and other storage media respectively, and supports USB or Uart download modes. The development board configures the QSPI_DATA[3:0] signals via the SW2 DIP switch.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册1.jpg
   :alt: 硬件手册1.jpg
   :width: 90%

**Design Key Points:**

1. ESD protection devices shall be added at the DIP switch.
2. QSPI_DATA[3:0] defaults to low level; ensure the pull-up level matches the IO voltage level. As shown in the figure below, the high and low levels of BOOT signals are controlled by the DIP switch to select the Boot/Download mode.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册2.png
   :alt: 硬件手册2.png
   :width: 90%

2. Reset Circuit
------------------

| The hardware reset of K1 is externally controlled with active-low level. SW3 is the power reset button, and SW4 is the system reset button.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册3.jpg
   :alt: 硬件手册3.jpg
   :width: 90%

**Design Key Points:**

1. A 10nF capacitor shall be added to the pin to eliminate jitter on the reset signal, enhance anti-interference capability and prevent abnormal system reset caused by false triggering.
2. The pull-up power supply of the RESET_IN_N network must be consistent with the IO power domain (pull-up to VCC18_GPIO).
3. The PGOOD signal of P1 is directly connected to the RESET_IN_N signal of K1, enabling key reset for K1 and PMIC chip.
4. If multiplexed with other reset sources, NAND gates or diodes shall be added for isolation.
5. ESD protection devices shall be installed at the reset buttons.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册4.png
   :alt: 硬件手册4.png
   :width: 90%

3. TF Card Circuit
--------------------

| K1 is equipped with 2 MMC interfaces. MMC1 supports 3.3V/1.8V voltage levels, while MMC2 only supports 1.8V. MMC1/2 can be connected to SDIO WIFI modules and SD Cards. U5 is the Micro SD card interface led out through the MMC1 bus, adopting 4-bit data line mode.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册5.jpg
   :alt: 硬件手册5.jpg
   :width: 90%

**Design Key Points:**

1. Confirm whether a 22Ω resistor is connected in series with the MMC_CLK signal (pre-installed on the core board).
2. If pull-up resistors are required for signals, verify that the pull-up level matches the IO voltage level.
3. ESD protection devices shall be added at the TF card connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册6.png
   :alt: 硬件手册6.png
   :width: 90%

4. PCIE Interface
-------------------

| K1 provides 3 PCIE interfaces: PCIE PortA Gen2x1, PCIE PortB Gen2x2, and PCIE PortC Gen2x2. J2 is an M.2 Key M connector for external SSD connection, and J3 is an M.2 Key E connector for external WIFI module connection.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册7.jpg
   :alt: 硬件手册7.jpg
   :width: 90%

**Design Key Points:**

1. PCIE_RXP/N

| If the connected device is an IC, a 220nF capacitor must be connected in series with the RX differential signal at the device end.
| If the connected device is a PCIE slot, the RX differential signal shall be directly connected to the slot pin without series capacitors.

2. PCIE_TXP/N

| A 220nF capacitor must be connected in series with the differential signal at the K1 end for AC coupling (pre-connected on the core board).

3. PCIE_REFCLKP/N supports two clock schemes:

| K1 provides clock signals for external devices with direct connection of PCIE differential clock signals.
| External devices provide clock signals for K1; a 49.9Ω pull-down resistor must be added at the source end of external devices. The clock deviation tolerance is ±300ppm, complying with PCIE protocol specifications.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册8.png
   :alt: 硬件手册8.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册9.png
   :alt: 硬件手册9.png
   :width: 90%

5. Audio Circuit
------------------

| K1 supports 2 channels of full-duplex I2S interfaces. On the development board, audio functions including HP, MIC and SPK are led out via the ES8326B audio codec chip. J14 is a 4-section 3.5mm headphone jack, and the SPK interface adopts 2.5mm pitch wire-to-board pin headers (P1, P2).

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册10.jpg
   :alt: 硬件手册10.jpg
   :width: 90%

**Design Key Points:**

1. Pull-up resistors shall be added for insertion detection pins.
2. An external LDO is required for the CPVDD power supply of the ES8326B chip, which supplies power to the headphone amplifier. Keep the current clean as much as possible. Due to the large operating current of the headphone amplifier, RC filters are not recommended for power noise reduction.
3. Isolate digital ground and analog ground with 0Ω resistors.
4. ESD protection devices shall be installed at audio connectors.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册11.png
   :alt: 硬件手册11.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册12.png
   :alt: 硬件手册12.png
   :width: 90%

6. CSI Interface
------------------

| The differential video input interface of K1 supports 4lane+4lane or 4lane+2lane+2lane input, with a maximum single-channel rate of 1.5Gbps. In 4lane+2lane+2lane mode, three cameras can output images simultaneously. However, the ISP can only process two channels; the remaining camera data (YUV or RAW format) cannot be processed by the ISP and can only be dumped to DDR through the CCIC DMA module.

- MIPI CSI1

| Four pairs of differential data are sampled based on the MIPI_CSI0_CK1XP/N differential clock.

- MIPI_CSI2

| [2 Lane Mode]: Two pairs of differential data (MIPI_CSI3_D2P/N, MIPI_CSI3_D3P/N) are sampled based on the MIPI_CSI2_CKP/N differential clock.

- MIPI_CSI3

| [2 Lane Mode]: MIPI_CSI3_D0P/N and MIPI_CSI3_D1P/N are sampled based on the MIPI_CSI3_CKP/N clock.
| [4 Lane Mode]: MIPI_CSI3_D0P/N, MIPI_CSI3_D1P/N, MIPI_CSI3_D2P/N and MIPI_CSI3_D3P/N are sampled based on the MIPI_CSI3_CKP/N differential clock.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册13.png
   :alt: 硬件手册13.png
   :width: 90%

| U12 and U13 are CSI interfaces adopting 2mm pitch pin headers.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册14.jpg
   :alt: 硬件手册14.jpg
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册15.png
   :alt: 硬件手册15.png
   :width: 90%

7. DSI Interface
------------------

| K1 integrates a 4-lane MIPI TX PHY for connecting MIPI LCD screens, with a maximum single-channel rate of 1200Mbps. CON2 is the MIPI_DSI interface using a 30-pin 0.5mm pitch FPC connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册16.jpg
   :alt: 硬件手册16.jpg
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册17.png
   :alt: 硬件手册17.png
   :width: 90%

8. HDMI Interface
-------------------

| K1 is built-in with an HDMI PHY, supporting a maximum resolution of 1920x1440@60Hz. J5 is the HDMI OUT interface with a standard female HDMI connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册18.jpg
   :alt: 硬件手册18.jpg
   :width: 90%

**Design Key Points:**

1. ESD protection shall be configured for HDMI signals, with ESD devices placed close to the HDMI connector. The parasitic capacitance of ESD devices shall be less than 0.3pF.
2. Peripheral circuits are required for HDMI_SCL, HDMI_SDA, HDMI_CEC and HDMI_HPD signals, using dedicated HDMI chips or discrete level conversion circuits. Level conversion requirements: HDMI_SCL and HDMI_SDA converted to 5V, HDMI_CEC converted to 3.3V, and external HDMI_HPD converted to 1.8V before input to the chip.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册19.png
   :alt: 硬件手册19.png
   :width: 90%

9. USB 2.0
------------

| K1 provides 3 USB 2.0 interfaces, supporting High-Speed (480Mbps), Full-Speed (12Mbps) and Low-Speed (1.5Mbps) modes. USB0 and USB2 support OTG function.

Download
~~~~~~~~~~

| U18 is the download interface adopting a Type-C connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册20.jpg
   :alt: 硬件手册20.jpg
   :width: 90%

**Design Key Points:**

1. The VBUS detection signal is 1.8V, implemented via resistor voltage division.
2. USB0 defaults to Device mode with floating ID pin; a 5.1kΩ pull-down resistor shall be connected from CC pin to GND.
3. ESD protection shall be added for USB 2.0 signals. The parasitic capacitance of ESD devices shall be less than 1pF, and ESD devices shall be placed close to the USB connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册21.png
   :alt: 硬件手册21.png
   :width: 90%

USB2.0+USB3.0
~~~~~~~~~~~~~~~

| K1 supports 1 USB 3.0 interface multiplexed with the PCIEA interface. J6 is the combined USB2.0+USB3.0 interface.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册22.jpg
   :alt: 硬件手册22.jpg
   :width: 90%

**Design Key Points:**

1. ESD protection shall be configured for USB3.0 signals. The parasitic capacitance of ESD devices shall be less than 0.5pF, and ESD devices shall be placed close to the USB connector.
2. USB3_RXP/N
- If the connected device is an IC or module, a 100nF capacitor shall be connected in series with RX differential signals at the device end.
- If the connected device is a socket, RX differential signals shall be directly connected without series capacitors.

3. USB3_TXP/N
- If the connected device is an IC or module, a 100nF capacitor shall be connected in series with TX differential signals at the K1 end.
- If the connected device is a socket, a 100nF capacitor shall be connected in series with TX differential signals near the socket.

4. Over-current protection shall be configured.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册23.png
   :alt: 硬件手册23.png
   :width: 90%

USB HUB
~~~~~~~~~

| The USB1 bus is expanded into 4-channel USB HOST buses via a USB HUB chip.

**Design Key Points:**

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册24.png
   :alt: 硬件手册24.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册25.png
   :alt: 硬件手册25.png
   :width: 90%

4G Module
~~~~~~~~~~~

| 4G function is implemented via the U20 (EC801ECNCG-N01-SNNSA) module. J7 is a pop-up SIM card connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册26.jpg
   :alt: 硬件手册26.jpg
   :width: 90%

**Design Key Points:**

1. The 4G module requires high current and stable voltage; an independent DCDC power supply is recommended.
2. ESD protection devices shall be added at the SIM card connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册27.png
   :alt: 硬件手册27.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册28.png
   :alt: 硬件手册28.png
   :width: 90%

WIFI+BT
~~~~~~~~~

| U22 is the BL-8723DU module, supporting 2.4G WIFI and Bluetooth 5.0.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册29.jpg
   :alt: 硬件手册29.jpg
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册30.png
   :alt: 硬件手册30.png
   :width: 90%

10. UART Interface
--------------------

| K1 integrates 10 groups of UART interfaces, among which UART0 serves as the debug port.

Debug
~~~~~~~

| UART0 is converted to a Type-C interface via the CH340T chip for system debugging serial communication.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册31.jpg
   :alt: 硬件手册31.jpg
   :width: 90%

**Design Key Points:**

1. To prevent current backflow to the CPU through the RX pin before baseboard power-on and avoid abnormal startup, level conversion chips shall be added for isolation in baseboard design.
2. The CH340T chip adopts external 5V power supply; a capacitor shall be connected from pin 5 (V3) of CH340T to GND.
3. ESD protection devices shall be installed at the Type-C connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册32.png
   :alt: 硬件手册32.png
   :width: 90%

RS232 & RS485
~~~~~~~~~~~~~~~

| Both RS232 and RS485 adopt green Phoenix terminals (J8, J9) as input and output ports.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册33.jpg
   :alt: 硬件手册33.jpg
   :width: 90%

**Design Key Points:**

1. The RS485 circuit adopts automatic transceiving mode. Note that the RS1G14XC5 inverter has inherent delay, which may affect high-speed communication and is not suitable for high baud rate applications.
2. A 120Ω terminal matching resistor shall be added for RS485 circuits.
3. ESD protection devices shall be installed at RS232 and RS485 connectors.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册34.png
   :alt: 硬件手册34.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册35.png
   :alt: 硬件手册35.png
   :width: 90%

11. RGMII Interface
---------------------

| K1 supports 2 channels of 10/100/1000 Mbps RGMII. U26 and U28 are Ethernet interfaces adopting Hanren RJ45 connectors.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册36.jpg
   :alt: 硬件手册36.jpg
   :width: 90%

**Design Key Points:**

1. Verify pull-up resistors for reset, interrupt and MDIO signals. Refer to the PHY chip datasheet for the resistance value of MDIO pull-up resistors. Comply with the power-on timing of the PHY chip reset pin; maintain the reset signal for at least 10ms after PHY power stabilization (refer to the chip datasheet for details). A 2.49kΩ (±1%) resistor must be connected from the RBIAS pin to GND.
2. Ensure the IO level of core board RGMII signals matches the PHY chip IO level. The RGMII IO level of K1 is 1.8V, so the PHY chip IO level shall be configured to 1.8V.
3. The indicator lights of Ethernet connectors are controlled by CFG_LDO[1:0] signals; configure light signals according to the PHY chip IO level.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册37.png
   :alt: 硬件手册37.png
   :width: 90%

4. Confirm the driving mode (voltage or current) of the PHY chip. For current driving, connect the center tap of the RJ45 connector to power; for voltage driving, connect a capacitor to GND.
5. Configure independent PHY addresses when multiple PHY chips share one MAC controller.
6. ESD protection devices shall be added at Ethernet connectors.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册38.png
   :alt: 硬件手册38.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册39.png
   :alt: 硬件手册39.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册40.png
   :alt: 硬件手册40.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册41.png
   :alt: 硬件手册41.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册42.png
   :alt: 硬件手册42.png
   :width: 90%

12. CAN Interface
-------------------

| K1 supports 1 channel of CAN-FD. The CAN interface adopts a green Phoenix terminal (J13) for signal input and output.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册43.jpg
   :alt: 硬件手册43.jpg
   :width: 90%

**Design Key Points:**

1. A 120Ω terminal matching resistor shall be configured for CAN circuits.
2. ESD protection devices shall be installed at the CAN connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册44.png
   :alt: 硬件手册44.png
   :width: 90%

13. RTC Circuit
-----------------

| RTC function is realized via the U35 (HYM8563S) chip. U36 is the button battery holder.

**Design Key Points:**

1. Pull-up resistors shall be added for I2C signals.
2. Add D26 Schottky diode to prevent reverse current from the button battery.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册45.png
   :alt: 硬件手册45.png
   :width: 90%

14. ADC Interface
-------------------

| The ADC interface adopts 2.54mm pitch pin headers.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册46.jpg
   :alt: 硬件手册46.jpg
   :width: 90%

**Design Key Points:**

| ESD protection devices shall be added at the connector.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册47.png
   :alt: 硬件手册47.png
   :width: 90%

15. Power Circuit
-------------------

| The system adopts 12V DC input. DCDC chips convert the input voltage to 5V, 4V, 3.3V and other voltage rails for board power supply. The power circuit integrates reverse connection protection, over-current & over-voltage protection and fast discharge functions. The baseboard uses the SY8386J DCDC chip with a maximum output current of 6A. CON1 is a DC-005 12V power jack compatible with 5.5mm outer diameter and 2.1mm inner diameter power plugs. J1 is a 3-pin 3.5mm pitch green Phoenix terminal for 12V DC input. SW1 is the power slide switch.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册48.jpg
   :alt: 硬件手册48.jpg
   :width: 90%

**Design Key Points:**

1. The baseboard power supply shall be powered on later than the core board; the enable signal of baseboard DCDC is controlled by the PMIC chip on the core board.
2. Limit the current of the fast discharge circuit and select appropriate components (Q3, R8).
3. Select MOSFETs with qualified drain-source voltage and continuous drain current for reverse connection protection and switch control circuits.
4. TVS protection devices shall be installed at the power input port.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册49.png
   :alt: 硬件手册49.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册50.png
   :alt: 硬件手册50.png
   :width: 90%

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册51.png
   :alt: 硬件手册51.png
   :width: 90%

PCB Layout Guidelines
-----------------------

| Key PCB layout requirements:
| (1) Ensure sufficient trace width for power and ground lines in the entire loop to optimize power return performance.
| (2) Maximize the integrity and continuity of the ground plane.
| (3) Place capacitors as close to chip pins as possible for faster current return; arrange small-value capacitors first and large-value capacitors afterwards.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册52.png
   :alt: 硬件手册52.png
   :width: 90%

| (4) Separate digital ground and analog ground.
| (5) Place ESD protection devices as close to external interfaces as possible.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册53.png
   :alt: 硬件手册53.png
   :width: 90%

| (6) Copper cutout shall be implemented for non-shielded inductors connected to the ground plane, with no wiring beneath.
| (7) Complete ground pouring is allowed under integrated inductors.
| (8) Clock and high-speed signal traces shall be at least 250mil away from the board edge and 500mil away from switching power inductors and MOSFETs.
| (9) Arrange clock traces adjacent to complete ground planes and apply ground shielding when necessary.
| (10) Avoid signal routing near or under crystal oscillators and implement ground shielding for crystal oscillators.
| (11) Route reset signals away from clock lines and switching power circuits.
| (12) Impedance Specifications

+--------------------------------------------+-------------------+-----------+
| Signal Group                               | Impedance         | Tolerance |
+--------------------------------------------+-------------------+-----------+
| General Single-ended Signals               | 50Ω Single-ended  | ±10%      |
+--------------------------------------------+-------------------+-----------+
| USB Differential Signals                   | 90Ω Differential  | ±10%      |
+--------------------------------------------+-------------------+-----------+
| Differential Signals (Ethernet, DSI, LVDS) | 100Ω Differential | ±10%      |
+--------------------------------------------+-------------------+-----------+

| (13) High-speed Differential Signals
- Avoid discontinuous trace impedance.
- Increase spacing between adjacent high-speed traces to reduce crosstalk.
- Maintain equal spacing, width and length for DP/DM traces. Strict time delay matching is mandatory for high-speed differential pairs to prevent communication failure; meander lines are adopted for length matching and delay control.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册54.png
   :alt: 硬件手册54.png
   :width: 90%

- Establish Pin Pairs from signal start pins to module terminal pins for length matching of multiplexed signals.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册55.png
   :alt: 硬件手册55.png
   :width: 90%

- Vias and components are prohibited inside differential pairs.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册56.png
   :alt: 硬件手册56.png
   :width: 90%

- DP/DM traces shall not cross splits or gaps in reference planes.
- Avoid cross routing between DP/DM and other signals; insert digital power or ground planes for isolation if crossing is unavoidable.
- Minimize bending of DP/DM traces; replace 90° corners with two 45° corners when turning is required.

.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - .. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册57.png
          :width: 100%
          :align: center
          :alt: 硬件手册57.png
          
     - .. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册58.png
          :width: 100%
          :align: center
          :alt: 硬件手册58.png

- Minimize bending and via counts of DP/DM traces for noise suppression, and route signals on solid GND reference planes. Keep identical via counts for DP and DM traces, minimize layer changes, and prefer top/bottom layer routing.
- Isolate DP/DM traces from other signals, especially clock and data buses with high noise.
- Apply ground shielding on both sides of DP/DM traces.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册59.png
   :alt: 硬件手册59.png
   :width: 90%

- Arrange GND return vias adjacent to differential pair vias.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册60.png
   :alt: 硬件手册60.png
   :width: 90%

- Ensure continuous ground return paths. Ground (GND) serves as the main return path and shall be kept continuous without splits or interruptions for stable signal reflux.

(14) USB 2.0 Layout
- Minimize the length of high-speed USB signal traces between chips and connectors.
- Control USB routing length with differential pair length error less than 0.12mm.
- Maintain a minimum spacing of 50mil (1.27mm) between high-speed clock/cyclic signals and parallel DP/DM traces.
- Maintain a minimum spacing of 20mil (0.51mm) for low-speed and non-cyclic signal traces.
- Keep a minimum spacing of 7.5mil (0.2mm) between internal DP and DM traces of one pair.
- The spacing of USB differential pairs shall not be less than 20mil (0.51mm).

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册61.png
   :alt: 硬件手册61.png
   :width: 90%

(15) Ethernet Layout
- Adopt daisy-chain routing for multiple PHY chips on the MDIO bus without branch routing.
- RGMII interface includes transmit, receive and control signals with 50Ω±10% impedance control.
- Limit the routing length of transmit and receive signals within 100mm with intra-group length error less than 2.54mm.
- Adopt differential routing for MDI interface with 100Ω±10% impedance.
- The length error of MDI differential pairs shall not exceed 0.12mm.
- Place power inductors of on-chip DCDC circuits close to chips for minimal loop length and complete ground return.
- Reserve series resistors on data lines and place them near the signal source.

(16) CAN Layout
- Adopt differential routing for CAN signals and reserve 120Ω terminal resistors.
- Reserve ground pins at external ports.

(17) 485 Layout
- Adopt differential routing for 485 signals and reserve 120Ω terminal resistors.
- The 485 bus works in half-duplex mode with dedicated transceiving control circuits.
- Reserve ground pins at external ports.

(18) Audio Layout
- Isolate analog audio signals from digital signals and apply ground shielding to ensure complete reference ground.
- Use wide traces for analog signal routing.

(19) WIFI Layout
- Implement ground shielding for WIFI antenna traces.
- Use wide traces and avoid 90°/45° sharp corners; adopt arc routing for turns and keep traces straight as much as possible.
- Route other signal traces away from WIFI modules.

.. figure:: /image/MYZR-进迭时空/MYZR-K1-EK263/硬件手册62.png
   :alt: 硬件手册62.png
   :width: 90%