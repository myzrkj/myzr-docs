Hardware Design Guide
=======================

Core Board Pin Schematic
--------------------------

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导1.png
   :alt: 硬件设计指导1.png

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导2.png
   :alt: 硬件设计指导2.png

Base Board Schematic
----------------------

Power Management
~~~~~~~~~~~~~~~~~~~

|  The evaluation base board has one power input interface, where J15 is a 12V DC power supply interface using a DC-005 power connector.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导3.png
   :alt: 硬件设计指导3.png

|  VDD_12V_MAIN is converted into power for the core board and evaluation base board peripherals through multiple power chips. To meet the power-on sequence requirement that the CPU's GPIO power supply is activated before the peripheral power supply, the recommended power-on sequence for the evaluation board is as follows: 12V DC power supply (VDD_12V_MAIN) -> Core board power supply (VDD_3V3_SOM) -> Core board-configured base board auxiliary power supply (VDD_3V3_SOM_OUT) -> Base board peripheral power supply (VDD_1V8_MAIN) -> Base board peripheral power supply (VDD_5V_MAIN) -> System reset (1P12/RESETn/PU/3V3) -> Core board audio power supply (VDD_3V3_ACODEC) -> Base board peripheral power supply (VDD_3V3_MAIN). The recommended power-on sequence design is shown in the figure below.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导4.png
   :alt: 硬件设计指导4.png

|  VDD_12V_MAIN generates a 3.3V power supply through the EC2232E DCDC power chip from Ecranic, which is used to power the core board. The network name is VDD_3V3_SOM, with a maximum current supply capacity of 3A.
|  The power enable is provided by the input voltage divider to achieve power-on immediate enable timing control. To protect the core board and facilitate voltage and current measurement, a fuse F2 is connected in series in the power path.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导5.png
   :alt: 硬件设计指导5.png

|  The core board provides VDD_3V3_SOM_OUT and VDD_3V3_ACODEC power outputs, with a power supply capacity ≤ 200mA. VDD_3V3_SOM_OUT is mainly used to control the power-on of some power supplies on the evaluation base board and to power core board configuration-related circuits (such as BOOT SET, DEBUG UART, Micro SD, etc.). VDD_3V3_ACODEC is mainly used to control the power-on of other parts of the evaluation base board. These two power supplies output by the core board shall not be used for powering other peripherals except for the aforementioned functions.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导6.png
   :alt: 硬件设计指导6.png

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导7.png
   :alt: 硬件设计指导7.png

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导8.png
   :alt: 硬件设计指导8.png

|  VDD_12V_MAIN generates three peripheral power supplies for the evaluation base board through three EC2232E DCDC power chips from Ecranic. The network names are: VDD_5V_MAIN, VDD_3V3_MAIN, and VDD_1V8_MAIN. Each peripheral power supply has a maximum current supply capacity of 3A.
|  The power enable of VDD_5V_MAIN and VDD_1V8_MAIN is provided by the VDD_3V3_SOM_OUT signal of the core board, and the power enable of VDD_3V3_MAIN is provided by the VDD_3V3_ACODEC signal of the core board. This realizes the timing control that the core board power supply is activated before the peripheral power supplies.
|  Design Notes:
|  (1) During the base board design, if some or all functions of the input-stage protection circuit are not required, appropriate simplification can be made.
|  (2) The base board power supply design can be increased or decreased according to the actual circuit design. It is recommended to refer to our company's power-on sequence for the enable control of the base board power supply.
|  (4) To ensure that VDD_5V_MAIN, VDD_3V3_MAIN, and VDD_1V8_MAIN meet the system power-on and power-off sequence requirements, the VDD_3V3_SOM_OUT signal output by the core board must be used to control the power enable of VDD_5V_MAIN and VDD_1V8_MAIN, and the VDD_3V3_ACODEC signal output by the core board must be used to control the power enable of VDD_3V3_MAIN (see the recommended power-on sequence of the evaluation base board for details).

LED Circuit
~~~~~~~~~~~~~

|  The evaluation base board is equipped with power indicator LEDs and user-programmable indicator LEDs, namely LED1~LED6. All use 0603 package SMD LEDs.
|  LED6 is the base board power indicator, and LED3 is the core board power indicator. Both are red and light up by default when powered on. LED1, LED2, LED4, and LED5 are user-programmable indicator LEDs, which are green and correspond to the four pins of GPIO4_B1_d, GPIO4_B7_d, GPIO0_A5_d, and GPIO0_A6_d respectively. They light up at high level.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导9.png
   :alt: 硬件设计指导9.png

KEY Circuit
~~~~~~~~~~~~~

|  The evaluation base board includes 1 system reset button RESETn (KEY1), 1 Maskrom button Maskrom (KEY2), and 1 user input button USER1 (KEY3).

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导10.png
   :alt: 硬件设计指导10.png

|  KEY1 is the RESET button of the evaluation board, which controls the reset pins of the CPU and PMIC.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导11.png
   :alt: 硬件设计指导11.png

|  Design Notes:
|  (1) 1P12/RESETn/PU/3V3 is the reset input pin of the core board. A 10K pull-up resistor is built into the core board. Under normal circumstances, it should be left floating to avoid affecting the power-on sequence.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导12.png
   :alt: 硬件设计指导12.png

|  KEY2 is the Maskrom button, and the button status is input to the CPU through the SARADC0_BOOT pin.
|  Design Notes:
|  (1) If the system image is not solidified in the eMMC when powering on and starting up, the CPU will boot into Maskrom mode. The first solidification of the system image can be performed through USB3.0 OTG. If the Loader fails to start normally during development and debugging, the system can also be solidified by entering Maskrom mode.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导13.png
   :alt: 硬件设计指导13.png

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导14.png
   :alt: 硬件设计指导14.png

|  KEY3 (USER1) is a user input button, and the status of KEY3 is input to the CPU through the SARADC0_IN1 pin. Note: The KEY3 (USER1) button also serves as the Recovery button of the system.

Debug UART Circuit
~~~~~~~~~~~~~~~~~~~~

|  The evaluation base board has an on-board UART. CON4 is a USB TO UART0 debug UART.
|  The evaluation base board converts UART0 into a Type-C connector (CON4) through the CH340T chip from WCH (Nanjing Qinheng Microelectronics Co., Ltd.) for use as a system debug UART. The CH340T uses 5V (network name: VDD_5V_VBUS) external power supply from the Type-C data cable, and VDD_5V_VBUS can also be used as the base board power supply.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导15.png
   :alt: 硬件设计指导15.png

|  Design Notes:
|  (1) During the base board design, it is recommended to adopt the RS0102YVS8 (U9) level conversion isolation scheme to prevent the RX terminal of the debug UART from being charged in advance before the base board is powered on and injecting current into the core board pins, which may cause the system to fail to start.
|  (2) The levels of the CPU pins UART0_TX_M0 and UART0_RX_M0 are both 3.3V. Do not directly connect to a debug tool with a 5V level interface, otherwise the CPU will be damaged.
|  (3) Note that the USB signal needs to be matched with 90ohm differential impedance.
|  (4) ESD devices should be placed close to the Type-C connector of the connector. The wiring is connected to the CH340T after passing through the ESD.

Micro SD Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The evaluation base board provides 1 Micro SD interface (CON5), which uses an externally soldered Micro SD connector with a pressure plate on the shell and is located on the front of the evaluation base board.
|  The Micro SD is led out through the SDMMC0 bus of the CPU and adopts a 4-bit data line mode.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导16.png
   :alt: 硬件设计指导16.png

|  Design Notes:
|  (1) During the base board design, the SHIELD[1:4] pins of the Micro SD socket shell should be connected to the digital ground.
|  (2) It is recommended to use the output power VDD_3V3_SOM_OUT of the core board to power the Micro SD (CON5). It is not recommended to use VDD_3V3_MAIN for power supply, otherwise the system may fail to start due to the power supply delay of this power supply, which may cause the system to fail to read the Micro SD card device correctly.
|  (3) The maximum frequency of the SDMMC0 bus clock is 100MHz. It is recommended that the equal-length control of D0~D3 relative to CLK be <50mil, with a single-ended 50ohm. For the wiring length of the core board signal, please refer to our core board hardware manual.

Ethernet Interface
~~~~~~~~~~~~~~~~~~~~

|  The base board of the evaluation board has 2 network ports led out in total, including 1 ETH RGMII Gigabit Ethernet port and 1 ETH RMII Fast Ethernet port.
|  The CPU has a built-in GMAC and a MAC controller, supporting 1 native RGMII Gigabit Ethernet port and 1 native RMII Fast Ethernet port.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导17.png
   :alt: 硬件设计指导17.png

|  The evaluation base board provides 1 channel of 10/100/1000Mbps adaptive Ethernet through the integrated Ethernet transceiver solution YT8521SH-CA from Motorcomm (Suzhou Yutai Microelectronics Co., Ltd.), a domestic manufacturer. A Gigabit RJ45 socket (CON8) with a built-in isolation transformer is used, and independent RGMII bus and MDIO bus are used to realize PHY communication and configuration.
|  YT8521SH-CA complies with the 10BASE-Te, 100BASE-TX, and 1000BASE-T IEEE 802.3 standards and provides functions such as cross-detection, automatic correction, polarity correction, and adaptive equalization.
|  Design Notes:
|  (1) The PHY of ETH0 RGMII uses 3.3V IO level. The RGMII level selection is configured using CFG_LDO[1:0], and the corresponding power supply pin of the circuit is DVDD_RGMII (pin29 of the YT8521SH-CA chip).
|  (2) A 25MHz passive crystal is connected to the XTAL_I and XTAL_O pins. If a 25MHz active crystal needs to be used, it can be connected from the XTAL_I pin, and the XTAL_O pin should be left floating.
|  (3) The YT8521SH-CA solution adopted by the evaluation base board uses an internally generated 1.2V voltage (VDD_1V2_ETH0L) for core logic power supply, and no additional 1.2V voltage is required. VDD_1V2_ETH0L shall not be used for powering other loads.
|  (4) The YT8521SH-CA chip requires that the reset signal is pulled high after the power supply is stable for 100ms; it is recommended to use IO to control the reset of the PHY chip.
|  (5) The PESDALC10N5VU close to the RJ45 connector is a 10-pin packaged ESD device. Note that the two side-by-side pins (such as IN1 and NC4, IN2 and NC3) are not connected inside the ESD device. In the actual design, the corresponding pins should be directly short-circuited externally (as shown in the figure below), that is, the network names of the corresponding pins must be consistent.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导18.png
   :alt: 硬件设计指导18.png

|  (6) PCB Layout and Wiring Instructions:
|  a) The ESD device should be placed close to the RJ45. The signal line requiring ESD protection should directly pass through the ESD pin before connecting to the subsequent circuit.
|  b) Note that the MDIx_P/N signal should be routed as a 100ohm differential signal, and the clock signal provided by the crystal should be routed with ground wrapping.
|  c) The two sets of transmit and receive signals in the RGMII bus should be subjected to equal-length processing within 50mil respectively, and the two sets of transmit and receive signals should be subjected to equal-length processing within 100mil, with a single-ended impedance of 50ohm.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导19.png
   :alt: 硬件设计指导19.png

|  The evaluation base board leads out 1 channel of 10/100Mbps adaptive Ethernet through the integrated Ethernet transceiver YT8512H from Motorcomm (Suzhou Yutai Microelectronics Co., Ltd.). Independent RMII bus and MDIO bus are used to realize PHY communication and configuration, and a Fast Ethernet RJ45 socket (CON9) with a built-in isolation transformer is adopted.
|  YT8512H complies with the 10BASE-Te and 100BASE-TX EEE 802.3az and EEE standards and provides functions such as polarity detection and automatic correction, auto-negotiation, and adaptive equalization.
|  Design Notes:
|  (1) A 25MHz passive crystal is connected to the XTAL_IN and XTAL_OUT pins. If a 25MHz active crystal needs to be used, it can be connected from the XTAL_IN pin, and the XTAL_OUT pin should be left floating.
|  (2) The YT8512H chip requires that the reset signal is pulled high after the power supply is stable for 100ms. Please refer to the reset circuit scheme of the evaluation base board and use IO to control the network port reset.
|  (3) The PESDALC10N5VU close to the RJ45 connector is a 10-pin packaged ESD device. Note that the two side-by-side pins (such as IN1 and NC4, IN2 and NC3) are not connected inside the ESD device. In the actual design, the corresponding pins should be directly short-circuited externally (as shown in the figure below), that is, the network names of the corresponding pins must be consistent.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导20.png
   :alt: 硬件设计指导20.png

|  (4) PCB Layout and Wiring Instructions:
|  a) The ESD device should be placed close to the RJ45, and the signal line should directly pass through the ESD pin before connecting to the subsequent circuit.
|  b) The ETH1_xP/N signal should be routed as a 100ohm differential signal.
|  c) The clock signal provided by the crystal should be routed with ground wrapping.
|  d) The two sets of transmit and receive signals in the RMII bus should be subjected to equal-length processing of ±50mil, with a single-ended impedance of 50ohm.

MIPI LCD Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The evaluation base board leads out the MIPI LCD interface and capacitive touch interface J10 through a 30-pin FFC connector with a pitch of 0.5mm. The core board uses the I2C1 bus to connect with the capacitive touch interface for communication.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导21.png
   :alt: 硬件设计指导21.png

|  Design Notes:
|  (1) The signals of the MIPI LCD interface and the LVDS LCD interface are multiplexed. At the same time, their capacitive touch screen interfaces also share signals, and the HDMI OUT signal is led out by converting the MIPI DSI signal through the LT8912B (U33) chip. Therefore, only one of the MIPI LCD, LVDS LCD, and HDMI OUT interfaces can be used at the same time.
|  (2) The voltage of pins 28-30 of the MIPI socket must be maintained between 4.8-5.3V. Decoupling capacitors of 1uF and 0.1uF must be placed on the pins and shall not be omitted. During layout, they should be placed close to the pins of the MIPI socket. To suppress electromagnetic radiation, common-mode inductors can be reserved for the data and clock signals of MIPI.
|  (3) It is recommended that the equal length within the MIPI DSI differential signal pair be <5mil, the equal length between pairs be <30mil, and the differential impedance be 100ohm.

HDMI OUT Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The evaluation base board adopts the 10-channel double-throw MIPI switch DIO1647WL36 from Dioo (Suzhou Dioo Microelectronics Co., Ltd.) and the video signal conversion chip LT8912B from Lontium (Shenzhen Lontium Semiconductor Co., Ltd.) to expand and lead out the HDMI OUT (CON14) interface through the MIPI DSI bus, using a standard 19-pin HDMI connector.
|  The LT8912B is powered by 1.8V, complies with HDMI1.4, supports 1080p HDMI output, and supports 7-bit automatic or manual output swing calibration and hot-plug detection.
|  The DIO1647WL36 is a differential MIPI double-throw switch chip with 10 channels (4 pairs of data differential pairs and 1 pair of clock differential pairs), with a speed of up to 3.5Gbps and a power supply voltage range of 1.65V~5V.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导22.png
   :alt: 硬件设计指导22.png

|  Design Notes:
|  (1) Since the HDMI OUT signal is led out by converting the MIPI DSI signal through the LT8912B (U33) chip, and the signals of the MIPI LCD interface and the LVDS LCD interface are multiplexed, and their capacitive touch screen interfaces also share signals, only one of the MIPI LCD, LVDS LCD, and HDMI OUT interfaces can be used at the same time.
|  (2) The IO levels of AF18/I2C1_SDA_M0/3V3 and AE17/I2C1_SCL_M0/3V3 are 3.3V, which need to be converted to 1.8V level before being connected to the LT8912B chip.
|  (3) The HPLG signal of the HDMI socket needs to be converted to a 1.8V signal through an NPN transistor before being connected to the LT8912B chip. When an external device is connected, this signal will be pulled high.
|  (4) To prevent power feeding through the HDMI interface when the core board is powered off, the D19 device should be added with reference to the evaluation base board circuit.
|  (5) It is recommended that the equal length within the HDMI differential pair be less than 5mil, the equal length between pairs be less than 100mil, and the differential impedance be controlled at 100ohm.

LVDS LCD Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  CON11 is a single-channel 8-bit LVDS LCD interface, using a 2x15-pin pin header with a pitch of 2.0mm, including LVDS signals and power supply. CON12 is a BACK LIGHT backlight control interface, using a 6-pin white terminal block with a pitch of 2.0mm. J3 is a RES TS resistive touch screen interface, using a 4-pin pin header with a pitch of 2.54mm. J4 is an LVDS CAPTS capacitive touch screen interface, using a 6-pin FFC connector with a pitch of 0.5mm. The core board uses the I2C1 bus to connect with it for communication.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导23.png
   :alt: 硬件设计指导23.png

|  Design Notes:
|  (1) The signals of the LVDS LCD interface and the MIPI LCD interface are multiplexed. At the same time, their capacitive touch screen interfaces also share signals, and the HDMI OUT signal is led out by converting the MIPI DSI signal through the LT8912B (U33) chip. Therefore, only one of the MIPI LCD, LVDS LCD, and HDMI OUT interfaces can be used at the same time.
|  (2) It is recommended that the equal length within the LVDS differential pair be less than 5mil, the equal length between pairs be less than 30mil, and the differential impedance be controlled at 100ohm.


USB2.0 HOST Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The evaluation base board directly leads out the USB20_HOST1 bus through a Type-A connector (CON7).

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导24.png
   :alt: 硬件设计指导24.png

USB3.0 OTG Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  CON6 is a USB3.0 OTG interface, using a 24-pin Type-C female socket, which is led out from the core board through the USB3_OTG0 bus.
|  The evaluation base board adopts the Type-C control chip WUSB3801Q-12/TR from WILLSEMI (Shanghai Will Semiconductor Co., Ltd.) to realize the communication role detection function.
|  Since the USB3.0 differential pair signal rate is as high as 5Gbps, it cannot be directly branched and connected to the front and back of the Type-C interface in the same way as USB2.0. To realize the positive and negative connection function, the USB switch chip CH482D from WCH (Nanjing Qinheng Microelectronics Co., Ltd.) is selected. This chip supports 2-to-1 switching of 2 channels of differential signals such as Super Speed+, PCIe Gen1/2/3, SATA/SAS 3Gbps/6Gbps, and Display Port.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导25.png
   :alt: 硬件设计指导25.png

|  Design Notes:
|  (1) The maximum USB signal rate is 5Gbps, and the differential pair is recommended to have an equal length <5mil and a differential impedance of 90Ω.
|  (2) If the INT_N/OUT3 pin of U19 needs to be allocated to other GPIOs, please use the GPIO pin that supports the interrupt function of the CPU (all GPIOs support the CPU interrupt function).
|  (3) For the WUSB3801Q-12/TR chip scheme, the status of CC1 and CC2 of the Type-C connector is automatically detected by the internal state machine of the chip and updated in the register map. If the CC channel is detected as SRC or DRP, the ID pin of the chip outputs a low level. If two boards are connected, the role of one board needs to be manually configured so that the other board can automatically switch roles.

AUDIO Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~

|  The evaluation base board leads out three AUDIO interfaces: HEADPHONE OUT, SPK OUT, and MIC IN through the on-board PMIC chip of the core board. CON10 is a HEADPHONE OUT audio interface, using a 3.5mm audio socket. J1 is an SPK OUT audio interface, and J2 is a MIC IN audio interface. Both use 2-pin white terminal blocks with a pitch of 2.0mm.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导26.png
   :alt: 硬件设计指导26.png

|  Design Notes:
|  (1) For the HEADPHONE OUT design, RK809_HP_SNS should be connected to the GND of the audio socket.


MIPI CSI0/MIPI CSI1 Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The evaluation base board leads out two camera interfaces, MIPI CSI0 (J5) and MIPI CSI1 (J6), through two 30-pin FFC connectors with a pitch of 0.5mm. Both are placed on the back of the evaluation base board and support the TL13850 camera module (designed based on the OV13850 camera module). At the same time, they support the external dual-channel camera adapter board TL-MIPICSI-PinBoard-A1.0-000 matched with Tronlong Technology, which expands 1 4Lane MIPI CSI interface into 2 2Lane MIPI CSI interfaces. It can connect 2 different Raspberry Pi camera modules CAM-MIPI9281RAW-V2 (designed based on the OV9281 camera module) and Camera Module v2 module (designed based on the IMX219 camera module) at the same time.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导27.png
   :alt: 硬件设计指导27.png

|  Design Notes:
|  (1) Since the signal level of the MIPI CSI camera interface is 1.8V, when using the 3.3V signal level output by the core board, level conversion is required before connecting to the MIPI CSI interface. To ensure the quality of the interface CAM_CLK clock signal, it is recommended that the value of the voltage divider resistor used for the clock signal be consistent with the design of the evaluation base board reference circuit.
|  (2) For the MIPI CSI differential signal, it is recommended that the equal length within the pair be <5mil, the equal length between pairs be <30mil, and the differential impedance be 100Ω.

EXPORT Interface
~~~~~~~~~~~~~~~~~~

|  The evaluation base board leads out CPU resources through the EXPORT0 (J8) and EXPORT1 (J9) expansion interfaces. Both EXPORT0 and EXPORT1 use 2x10-pin pin headers with a pitch of 2.54mm.
|  The CPU resources led out by the EXPORT0 and EXPORT1 interfaces are as follows.
|  (1) Communication interfaces: 3 UART serial ports, 3 I2Cs, 2 CANs (RK3562J), 1 SPI, and 1 SDIO.
|  (2) Audio interface: 1 I2S.
|  (3) System reset: 1 PWRON, which can be used to control the power on/off of the PMIC.
|  (4) Signal detection: 14 SARADCs, with an ADC sampling rate of up to 1MSPS.
|  Note: The signal levels led out by EXPORT0 and EXPORT1 are not consistent. Before use, the level standard of the selected signal must be determined.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3562-EK200/硬件设计指导28.png
   :alt: 硬件设计指导28.png

|  Design Notes:
|  (1) The voltage range of the ADC inputs SARADC0_IN2~7 and SARADC1_IN0~7 is 0~1.8V. During the base board design, attention should be paid to the input signal, which shall not exceed the voltage requirement range, otherwise the core board may be damaged.
|  (2) When there is no voltage input to the ADC input pin, to reduce the crosstalk of the ADC channel, it is recommended to add a 1MΩ pull-down resistor with reference to our base board design.