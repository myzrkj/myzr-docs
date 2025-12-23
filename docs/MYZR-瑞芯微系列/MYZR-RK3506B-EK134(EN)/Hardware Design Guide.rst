Hardware Design Guide
=======================

BOOT
------

|  The boot sequence of RK3506 can be set via the SARADC_IN0 pin to boot from peripherals corresponding to different interfaces. As shown in the figure below, the hardware configures ten modes of peripheral boot sequences (LEVEL1-LEVEL10) by setting different pull-up and pull-down resistor values, which can be configured according to actual application requirements.    
|  Key Design Points:
|  (1) The pull-up level is determined based on the IO level of the SARADC_IN0 signal.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导1.png
   :alt: 硬件指导1.png
   :width: 90%

KEY
------

RECOVER
~~~~~~~~~

|  If the Recovery mode button is pressed when the system starts (i.e., keeping SARADC_IN1 at low level (0V)), RK3506 will enter the Loader flashing mode. When the PC detects the USB device, release the button to restore SARADC_IN1 to high level (1.8V), and then firmware flashing can be performed. If the product has no button, SARADC_IN1 will be in an indeterminate state when left floating, which may affect startup. Therefore, the 10Kohm pull-up resistor for SARADC_IN1 must be retained (not removed) to ensure the default normal startup judgment; for convenience of development, it is recommended to reserve a button or test point for SARADC_IN1.    

RESET
~~~~~~~

|  The NPOR pin serves as an external reset signal, which is input through the NPOR pin to realize hardware reset of RK3506, and it is active at low level.  

Key Points for Circuit Design
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  (1) Check whether the SARADC_IN1 signal and NPOR signal are connected with pull-up resistors.
|  (2) ESD protection devices must be added at the button.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导2.png
   :alt: 硬件指导2.png
   :width: 90%

USB
------

|  The RK3506B chip has 2 built-in USB2.0 OTG controllers. USB20_OTG0_DM/USB20_OTG0_DP is the system firmware flashing port. If this port is not used in the product, it must be reserved during debugging and production; otherwise, debugging and production firmware flashing will not be possible.
|  OTG Mode: Automatically switch between DEVICE mode and HOST mode according to the state of the ID pin. High ID level indicates device mode, and pulled-down ID level indicates HOST mode.

DEVICE
~~~~~~~~

|  Key Points for Circuit Design:
|  (1) When the device works as a slave, two 5.1K pull-down resistors must be connected to the CC pins of the Type-C interface.
|  (2) The USB20_OTG0_ID signal only needs to be left floating.
|  (3) VBUS is connected to the USB20_OTG0_VBUSDET signal through a resistor divider.
|  (4) A 2.2R matching resistor must be connected in series with the USB20_OTG0_DM/USB20_OTG0_DP signals.
|  (5) ESD protection devices must be added to the Type-C connector.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导3.png
   :alt: 硬件指导3.png
   :width: 90%

USB_HUB
~~~~~~~~~

|  The USB20_OTG1 signal is expanded into four groups of USB signals through a HUB chip.
|  Key Points for Circuit Design:
|  (1) A 2.2R matching resistor must be connected in series with the USB20_OTG1_DM/USB20_OTG1_DP signals.
|  (2) A 680R resistor must be connected from the RREF pin of the GL850G chip to GND.
|  (3) Check whether the reset pin and OVCUR pin are connected with pull-up resistors.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导4.png
   :alt: 硬件指导4.png
   :width: 90%

HOST
^^^^^^

|  Key Points for Circuit Design:
|  (1) Pay attention to overcurrent protection. The output of USB2.0 is generally 500mA, and the OCB pin of the ETA6027 DCDC chip can be used to control the output current. The specific value of the pull-down resistor (R46) should refer to the ETA6027 chip manual.
|  (2) ESD protection devices must be added to the Type-A connector.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导5.png
   :alt: 硬件指导5.png
   :width: 90%

4G
----

|  One group of expanded USB signals is used for the 4G module.
|  Key Points for Circuit Design:
|  (1) The 4G module requires large current and stable voltage, so a separate DCDC can be used to supply power to it.
|  (2) ESD protection devices must be added to the SIM card connector.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导6.png
   :alt: 硬件指导6.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导7.png
   :alt: 硬件指导7.png
   :width: 90%

MIPI_DSI
----------

|  The MIPI_DPHY_DSI_TX of RK3506B supports MIPI V1.2 version, with a total of 2 Lanes and a speed of 1.5Gbps per Lane.  
|  Key Points for Circuit Design:
|  (1) Check whether the I2C signal is connected with a pull-up resistor.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导8.png
   :alt: 硬件指导8.png
   :width: 90%


RGB
-----

|  RK3506 supports one LCDC interface output, which is compatible with parallel 24bit RGB mode, 16bit BT1120 mode, 8bit BT656 mode, and MCU mode. In actual product design, the power domain of the LCDC interface should select the corresponding voltage supply according to the actual IO power supply requirements (1.8V or 3.3V) of the peripheral, and the levels must be consistent.
|  Key Points for Circuit Design:
|  (1) A 22R matching resistor must be connected in series with the LCD signal.
|  (2) Check whether the I2C signal is connected with a pull-up resistor.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导9.png
   :alt: 硬件指导9.png
   :width: 90%


Audio
-------

|  RK3506 provides rich audio interface capabilities and resources, including 5 groups of SAI interfaces, 1 group of PDM interfaces, 1 SPDIF TX, 1 SPDIF RX interface, and 2 groups of ASRC processing units. Among them, SAI can be used for communication with peripherals such as audio ADC, audio DAC, audio Codec, and DSP, and can also provide integrated audio input and output support for video input/output interfaces. Through SAI1 combined with ES8388 and VA2213 chips, functions such as HP (Headphone) and SPK (Speaker) are derived. In addition, the differential ADC of the built-in ACODEC is used to realize analog signal input (MIC).    
|  Key Points for Circuit Design:
|  (1) Headphone insertion detection setting: High level when inserted, low level when pulled out (can be set according to specific requirements).
|  (2) The microphone requires a bias voltage.
|  (3) Check whether the I2C signal is connected with a pull-up resistor.
|  (4) When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain value (between 22ohm-100ohm, specific value subject to meeting SI test requirements) in series with the clock/control/signal lines.
|  (5) ESD protection devices must be added to the audio connector.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导10.png
   :alt: 硬件指导10.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导11.png
   :alt: 硬件指导11.png
   :width: 90%

WIFI
------

|  RK3506 integrates 1 SDMMC controller, which supports SDIO3.0 protocol and MMC V4.51 protocol. The SDMMC data supports up to 4 bits and a maximum frequency of 150MHz. It supports System Boot, and peripherals can be connected to eMMC, SD card, and SDIO WIFI. The BL-M8189FS6 module is connected through SDMMC signals to derive the WIFI function.
|  Key Points for Circuit Design:
|  (1) A 22R resistor must be connected in series with SDMMC0_CLK.
|  (2) A π-type circuit must be reserved for the antenna to adjust antenna matching.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导12.png
   :alt: 硬件指导12.png
   :width: 90%

Ethernet
----------

|  The RK3506 chip integrates 2 EMAC controllers, supporting RMII interface with 10/100 Mbps data transmission rate, and full-duplex and half-duplex working modes.  
|  Key Points for Circuit Design:
|  (1) A 2.49K resistor must be connected from the RBIAS pin of the YT8522C chip to GND (specific details refer to the chip manual).
|  (2) A 1.5~1.8K pull-up resistor must be connected to the MDIO pin.
|  (3) RMII0/1 supports 1.8V or 3.3V level, and the IO level of the YT8522C chip must match it.
|  (4) Configure the PYH address and signal lamp as multiplexed pins, and pay attention to keeping their initial states consistent when configuring.
|  (5) The CT (Center Tap) signal of the RJ connector is determined by the driving mode of PYH. If the PYH chip is voltage-driven, it is directly connected to GND through a capacitor; if the PYH chip is current-driven, it is connected to the power supply.
|  (6) ESD protection devices must be added to the RJ connector.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导13.png
   :alt: 硬件指导13.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导14.png
   :alt: 硬件指导14.png
   :width: 90%

Uart
------

|  The RK3506B chip has 6 UART controllers, among which UART0 is the default Debug UART of RK3506B.

Debug
~~~~~~~

|  The CH340T chip is used to convert UART0 to a Type-C interface, which serves as the system debugging serial port.
|  Key Points for Circuit Design:​
|  (1) To prevent the RX terminal from being charged before the bottom board is powered on and injecting current into the CPU (which affects the normal startup of the CPU), a level conversion chip must be added for isolation during the bottom board design.
|  (2) The CH340T uses external 5V power supply, and a capacitor must be connected from pin 5 (V3) of the CH340T chip to GND.
|  (3) The CH340T requires a 12MHz crystal oscillator, and two matching capacitors must be connected to both ends of the crystal oscillator respectively. The capacitance value should refer to the CH340T chip data sheet.
|  (4) When the device works as a slave, the CC pin of the Type-C interface is pulled down to GND through a 5.1K resistor.
|  (5) ESD protection devices must be added to the Type-C connector.
|  Debug Reference Circuit:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导15.png
   :alt: 硬件指导15.png
   :width: 90%

RS232 & TTL & IO Expansion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Key Points for Circuit Design:
|  (1) Check whether the I2C signal is connected with a pull-up resistor.
|  (2) ESD protection devices must be added to the pin header.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导16.png
   :alt: 硬件指导16.png
   :width: 90%

RS485
~~~~~~~

|  Key Points for Circuit Design:
|  (1) The SIT3485 chip has no isolation function, so isolation (Q4) must be implemented.
|  (2) A 120R terminal matching resistor must be added to RS485.
|  (3) ESD protection devices must be added to the RS485 connector.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导17.png
   :alt: 硬件指导17.png
   :width: 90%

CAN
-----

|  The RK3506 chip integrates 2 CAN controllers.
|  Key Points for Circuit Design:
|  (1) A 120R terminal matching resistor must be added to CAN.
|  (2) ESD protection devices must be added to the CAN connector.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导18.png
   :alt: 硬件指导18.png
   :width: 90%

Power Supply
--------------

|  The RK3506B core board adopts a discrete power supply. The 12V DC input (DCIN_12V) of the bottom board is converted to 5V through DC/DC to supply power to the core board, and then converted to various voltages required by the system through DC/DC and LDO respectively. All power supplies of the core board are powered on by default when the system is turned on. After the core board starts, some power supplies of the bottom board are turned on through GPIO. J2 is a DC-005 power interface with 12V DC input, which can be connected to a power plug with an outer diameter of 5.5mm and an inner diameter of 2.1mm. The power input has functions such as reverse connection protection, overcurrent and overvoltage protection, and rapid discharge. SW6 is a power toggle switch.  
|  Key Points for Circuit Design:
|  (1) Pay attention to adding overcurrent protection, overvoltage protection, reverse input protection, and rapid discharge functions.
|  (2) A TVS protection device (D39) must be added at the power input.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导19.png
   :alt: 硬件指导19.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导20.png
   :alt: 硬件指导20.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导21.png
   :alt: 硬件指导21.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导22.png
   :alt: 硬件指导22.png
   :width: 90%

PCB
-----

|  Key Points for PCB Layout:
|  (1) Ensure that the power lines and ground lines have sufficient width throughout the loop to enable fast power return.
|  (2) Ensure the integrity of the ground plane and the continuity of the GND plane as much as possible.
|  (3) Capacitors should be placed as close to the chip pins as possible to enable fast return. Generally, capacitors with smaller capacitance are placed first, followed by those with larger capacitance.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导23.png
   :alt: 硬件指导23.png
   :width: 90%

(4) Separate digital ground from analog ground.
(5) ESD protection devices should be placed as close to the interface as possible.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导24.png
   :alt: 硬件指导24.png
   :width: 90%

|  (6) For non-shielded inductors, copper cutting is required until the ground plane is exposed, and no traces are allowed under the inductor.
|  (7) The ground can be laid under the integrated inductor.
|  (8) The routing of clock and high-speed signals should be at least 250mil away from the edge of the board, and at least 500mil away from the switching power supply inductor and MOS tube.
|  (9) The clock should be adjacent to a complete ground plane, and ground shielding should be implemented if necessary.
|  (10) No other signal traces should be routed near or under the crystal oscillator, and it is best to shield the crystal oscillator with ground.
|  (11) The reset signal should be kept away from clock lines and switching power supply switching circuits.
|  (12) Impedance Recommendations

+------------------------------------------------------+-------------------+-----------+
| Signal Group                                         | Impedance         | Tolerance |
+------------------------------------------------------+-------------------+-----------+
| Single-ended signals with no special requirements    | 50Ω Single-ended  | ±10%      |
+------------------------------------------------------+-------------------+-----------+
| USB Differential Signals                             | 90Ω Differential  | ±10%      |
+------------------------------------------------------+-------------------+-----------+
| Differential Signals (including Ethernet, DSI, LVDS) | 100Ω Differential | ±10%      |
+------------------------------------------------------+-------------------+-----------+

|  (13) High-Speed Differential Signals

- Avoid discontinuous routing impedance.
- If high-speed signal lines are too close to each other, crosstalk is likely to occur, so increase the spacing between traces as much as possible.
- The DP and DM traces must have equal spacing, equal width, and equal length. High-speed differential signal pairs must ensure strict time delay; otherwise, communication failure may occur. Therefore, to meet this requirement, serpentine traces can be used to achieve equal length, thereby meeting the time delay requirement.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导25.png
   :alt: 硬件指导25.png
   :width: 90%

- When signals are used for multiple multiplexing functions and require equal length, a Pin Pair from the start end of the signal to the terminal of the module must be established, and then the Pin Pair is used to achieve equal length.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导26.png
   :alt: 硬件指导26.png
   :width: 90%

- Vias or components are not allowed to be placed within the differential pair.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导27.png
   :alt: 硬件指导27.png
   :width: 90%

- The DP and DM traces should not pass through plane splits or gaps in the reference plane.
- The DP and DM traces should not cross other signals. If crossing is unavoidable, place a digital power plane or ground plane between them.
- Minimize the number of bends of the DP and DM traces. If a 90° bend is required, replace it with two 45° bends.


.. list-table::
   :widths: 50 50
   :header-rows: 0

   * - .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导28.png
          :width: 100%
          :align: center
          :alt: 硬件指导28.png
          
     - .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导29.png
          :width: 100%
          :align: center
          :alt: 硬件指导29.png


- To prevent noise, minimize the number of bends and vias of the DP and DM traces, and these signal lines should be routed on a solid GND reference plane. The DP and DM traces should have the same number of vias. Avoid vias and layer changes as much as possible. It is recommended to route the signal lines on the top or bottom layer.
- The DP and DM should be kept away from other signals, especially paying attention to the noise from clock and data buses.
- The two sides of the DP and DM traces are preferably shielded by the GND plane.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导30.png
   :alt: 硬件指导30.png
   :width: 90%

- Place the GND loop vias adjacent to the differential pair vias.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导31.png
   :alt: 硬件指导31.png
   :width: 90%

- The return path should be continuous with the ground. That is, the return path is usually realized through the ground (GND). To ensure effective and stable return, the ground line (GND) should be kept continuous as much as possible to avoid splits or interruptions.

|  (14) USB 2.0

- The routing of USB high-speed signals between the chip and the connector should be as short as possible.
- The USB routing length should not be too long, and the length error of signals within the differential pair should not exceed 0.12mm.
- The spacing between high-speed clock and periodic signal traces parallel to DP and DM should be at least 50mil (1.27 mm).
- The spacing between low-speed and aperiodic signal traces should be at least 20mil (0.51 mm).
- The spacing between DP and DM traces (within the same pair) should be at least 7.5 mils (0.2 mm).
- The spacing between DP and DM traces (differential pairs) should not be less than 20mil (0.51 mm).

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导32.png
   :alt: 硬件指导32.png
   :width: 90%

|  (15) Ethernet

- When multiple PHY chips are mounted on the MDIO bus, use the series connection method instead of branched routing.
- The RGMII interface is divided into transmit signals, receive signals, and control signals, and the impedance of each group is controlled at 50Ω±10%.
- The routing length of transmit signals and receive signals should not exceed 100mm, and the length error of signals within the group should not exceed 2.54mm.
- The MDI interface adopts differential routing with an impedance of 100Ω±10%.
- The differential error within the MDI group should not exceed 0.12mm.
- The power inductor connected to the internal DCDC of the chip should be placed close to the chip to ensure the shortest loop and the integrity of the ground loop.
- The series resistors reserved on the data lines should be placed close to the source end.

|  (16) CAN

- CAN adopts differential routing, and a 120Ω terminal resistor is reserved.
- It is recommended to reserve a ground signal for the connection port.

|  (17) 485

- 485 adopts differential routing, and a 120Ω terminal resistor is reserved.
- The 485 bus adopts half-duplex mode for transmission, so transmit-receive control must be implemented.
- It is recommended to reserve a ground signal for the connection port.

|  (18) AUDIO

- Audio signals are analog signals and need to be isolated from digital signals. If necessary, ground shielding should be implemented to ensure the integrity of the reference ground.
- The trace width of analog signals should be as large as possible during routing.

|  (19) WIFI

- The WIFI antenna signal should be shielded with ground.
- The routing width should be large. 90° or 45° bends are not allowed; straight lines are preferred. If a bend is necessary, use arc routing.
- The signal lines should be kept away from the WIFI module as much as possible.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/硬件指导33.png
   :alt: 硬件指导33.png
   :width: 90%

Debugging
-----------

|  General Troubleshooting Ideas When Problems Occur During Debugging:
|  (1) Check the soldering for issues such as cold solder joints, solder bridges, missing solders, and wrong solders. Especially for polar components, check whether their placement is correct.
|  (2) Check whether the pin numbers of the physical component match those of the PCB package.
|  (3) Refer to the chip manual to check the principle, whether the signal line connections are correct, and whether the IO levels match.
|  (4) Confirm whether the component selection meets the circuit requirements.
|  (5) Measure whether the power voltage, clock, enable terminal, and the pin voltages of pins requiring pull-up or pull-down resistors are correct.
|  (6) Pay attention to chips with power-on sequence requirements. Sometimes the voltage is normal, but the sequence does not meet the requirements, which may also cause the chip to fail to work normally.
|  (7) Check whether the PCB routing and layout are reasonable. Check whether the power line and via sizes meet the current requirements, and pay attention to the strict layout requirements for important signals such as crystal oscillators and differential signals.
|  (8) Measure whether the pin signals are normal and record the signal waveforms.
|  (9) Confirm whether the pins are multiplexed.
|  (10) Check whether the components are damaged.
|  It is best to have multiple boards for comparative experiments during debugging. When a problem occurs, do not measure the circuit blindly; instead, have a basis and measure according to the circuit schematic. During detection, you can start from the input end to the output end, or from the output end to the input end, but it is best not to skip levels, as this may disrupt the thinking and lead to missed measurements, making it difficult to analyze the error finally. Record the measured waveforms and analyze the problem in combination with the chip manual.
|  Points to Note During Debugging:
|  (1) Prevent static electricity. Before touching the board, touch a metal object to discharge static electricity.
|  (2) Before power-on, perform a short-circuit test on each power supply on the board, and check whether the power voltage is correct and whether the positive and negative poles are connected correctly.
|  (3) Check whether the BOOT mode is correct.
|  Divide into sections by module, including module introduction, performance, indicators, parameters, and principles.