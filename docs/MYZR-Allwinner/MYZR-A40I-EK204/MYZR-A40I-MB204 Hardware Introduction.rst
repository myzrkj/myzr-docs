MYZR-A40I-MB204 Hardware Introduction
========================================

Interface Overview
---------------------

Front View
~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/963px-MY-A40I-MB204_Front.png
   :alt: 963px-MY-A40I-MB204_Front.png

Back View
~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/963px-MY-A40I-MB204_Back.png
   :alt: 963px-MY-A40I-MB204_Back.png


MYZR_A40I_MB204 Base Board Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----+-----------------+----------------------------+--------------------------------+-------------+
| No. |    Interface    |          Function          |         Interface Type         | Silkscreen  |
+=====+=================+============================+================================+=============+
| 1   | 5V_IN           | Power Input                | DC-005 Round Port              | P26         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 2   | Ethernet        | 1 x 10/100M Ethernet       | RJ45                           | P12         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 3   | DEBUG UART      | Debug Serial Port          | PH1.25 Pin Header (4-pin)      | P14         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 4   | RS232           | RS232 Interface            | Screw Terminal Block           | P15         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 5   | RS485           | RS485 Interface            | Screw Terminal Block           | P16 and P18 |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 6   | CAN             | CAN Interface              | Screw Terminal Block           | P21         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 7   | 4G Module       | 4G Module Interface        | MINI-PCIE                      | P19         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 8   | SIM             | SIM Card                   | MICRO SIM Pop-up Type          | P27         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 9   | TF              | TF Card                    | Standard TF Card Pop-up Socket | P13         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 10  | USB             | USB2.0                     | Dual-layer USB_A               | P9          |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 11  | HDMI            | Video Interface            | Standard HDMI-A Port           | P7          |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 12  | MIPI-DSI        | MIPI DSI Display Interface | FPC Socket (40Pin)             | P23         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 13  | LVDS            | LVDS Display Interface     | FPC Socket (40Pin)             | P24         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 14  | RGB             | RGB Display Interface      | FPC Socket (40Pin)             | P25         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 15  | USER LIGHT      | User LED Lights            | SMD LED Lights (3 pcs)         | D3, D5, D6  |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 16  | Antenna         | WIFI & Bluetooth           | IPX Connector                  | E1          |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 17  | USB             | BOOT                       | LOADER Micro_USB               | P8          |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 18  | Audio           | Audio Output, Input        | 3.5mm Headphone Jack           | P4          |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 19  | Reset Button    | Reset                      | Tactile Switch                 | SW6         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 20  | Download Button | Download                   | Tactile Switch                 | SW8         |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 21  | Custom Button   | KEYADC Button              | Tactile Switch                 | SW1~SW5     |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 22  | SATA            | SATA Interface             | SATA 7P Interface              | P6          |
+-----+-----------------+----------------------------+--------------------------------+-------------+
| 23  | MIPI-CSI        | Parallel Camera Interface  | Dual-row PH2.54 20-pin Header  | P2          |
+-----+-----------------+----------------------------+--------------------------------+-------------+

A40I Base Board Description
-----------------------------

Base Board Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~

| The base board is powered by a 5V power supply through a DC 5.5 plug (P22) socket. After passing through the (P26) mechanical power switch, self-recovering fuse (F1), (D8) 5.6V Zener diode, and Q7 transistor, the power input feedback detection controls the high-low level input of the EN pin (pin4) of the 5VDC-DC (Q6) to turn the power on or off, thereby preventing overvoltage protection for the power input. The subsequent 5VIN output voltage is filtered by capacitors and beads, then stepped down to 3.3V and 1.8V in sequence to supply power to part of the control circuit on the base board.

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_5V.png
   :alt: MY-A40I-MB204_5V.png

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_3.3V.png
   :alt: MY-A40I-MB204_3.3V.png

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_1.8V.png
   :alt: MY-A40I-MB204_1.8V.png

| Notes: When designing the power supply part, the 5V/3.3V copper cladding and power traces must be designed for a minimum current of 3A. If traces need to be routed on both the top and bottom layers, multiple vias should be drilled to prevent PCB burnout due to instantaneous overload when the power is turned on, ensuring normal power supply.


Reset Circuit
~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_RESET.png
   :alt: MY-A40I-MB204_RESET.png

| Note: This development board only uses the SW6 reset switch shown in the figure. The watchdog chip has not been verified, so its use is not recommended.


Button Circuit
~~~~~~~~~~~~~~~~

| The VOL+, VOL-, MENU, ENTER, and HOME buttons are connected to KEYADC0 with pull-up resistors of different values to ground for level identification to distinguish functional buttons; DOWNLOAD and PWRON are independent buttons, which are activated when pressed to connect to ground.

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_DOWNLOAD.png
   :alt: MY-A40I-MB204_DOWNLOAD.png


LED Display
~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_LED5V.png
   :alt: MY-A40I-MB204_LED5V.png

| Note: This system is equipped with 3 channels of LED output display. It is recommended that the pull-up input power supply be changed from 3.3V to 5V and the driving method be modified to the circuit shown in the following figure in later stages to prevent insufficient brightness of LEDs with higher driving voltages.


RTC (Real-Time Clock) Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The RTC chip used in this circuit has built-in crystal matching capacitors. If you need to replace the solution, attention must be paid to the crystal accuracy. Matching capacitors can be connected in parallel between the two crystal networks and ground to adjust the accuracy. When the base board is powered on, the 3.3V power supply of the base board supplies power to the RTC chip and charges the battery BT1; when the base board is powered off, the battery BT1 discharges to serve as the power supply for the RTC chip.

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_RTC.png
   :alt: MY-A40I-MB204_RTC.png


External TF Card Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_TF2.png
   :alt: MY-A40I-MB204_TF2.png

| Note: For the SDIO interface network with pull-up resistors on the right side of the figure, equal-length processing must be done during PCB design, and a 3W spacing requirement must be met with overall ground shielding. In subsequent design and development, pull-up resistors should be connected to all 7 signal lines of SDCO.


Ethernet Circuit Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_ETH.png
   :alt: MY-A40I-MB204_ETH.png

| Note: For the ETH TX/RX signal lines, equal-length processing must be done during PCB design, and a 3W spacing requirement must be met with overall ground shielding. The distance between differential pairs and other networks must be at least 3 times the line width; the equal-length error within a differential pair must be within 5mil, and the equal-length error between differential pairs must be within 25mil. For the power supply part, the filter capacitors must be thickened and placed as close to the terminal as possible.


USB Circuit
~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_USB1.png
   :alt: MY-A40I-MB204_USB1.png

| Note: The 5VIN power supply must be strictly designed with a reserved minimum current capacity of 1.5A, and the traces must be thickened. The DP/DM signal lines must be routed as differential signal lines. BR2/3 are protection components for anti-static, and L5/6/8 are common-mode filters, which must be placed close to the USB interface during PCB design. P9 is a USB2.0 socket that can be connected to external devices such as U disks or mice.


DownLoad Programming System USB Port Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_Download-USB.png
   :alt: MY-A40I-MB204_Download-USB.png

| This interface is a Micro USB interface, which is used to connect to a host PC for programming the system of this development board. The ID pin of the USB interface in the figure must be pulled up and must not be connected to low level; BR1 is a protection component for anti-static, and L4 is a common-mode filter, which must be placed close to the Micro USB interface during PCB design; the USB cable requires differential equal-length routing.


4G Module Circuit
~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_4G.png
   :alt: MY-A40I-MB204_4G.png

| Note: The instantaneous operating current of the 4G module can reach approximately 3A. During circuit design, the 3.3V power line must be strictly designed according to the current requirement, and the filter capacitor must be placed as close as possible; D4 is the working status indicator light of the module, P27S is the SIM card socket which must be placed close to the 4G module. The network from the module to the SIM card must be routed in groups to avoid excessive length errors caused by too long traces, and must be kept away from strong signal interference sources with traces arranged nearby. L12 is a common-mode filter, and the USB cable requires differential routing.


HDMI Display Circuit
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_HDMI.png
   :alt: MY-A40I-MB204_HDMI.png

| Note: U4/5/6 are TVS electrostatic protection tubes, which must be placed as close to the HDMI socket as possible during PCB design. Except for the power lines, all other signal lines must be routed in accordance with differential rules with equal lengths within the differential pairs. The distance between differential pairs and other networks must be at least 3 times the line width; the equal-length error within a differential pair must be within 5mil, and the equal-length error between differential pairs must be within 15mil. HDMI_CEC / HDMI_SDA/ HDMI_SCL must be effectively pulled up in strict accordance with the circuit diagram.


RGB/LVDS/DSI Circuit
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_RGB-LVDS.png
   :alt: MY-A40I-MB204_RGB-LVDS.png

| Note: The 5V/3.3V power supply must be designed for a current of more than 1A. Except for the power lines, all other signal lines must be strictly routed as equidistant differential signal lines, and the signal lines must be routed in parallel in groups with traces as short as possible.


WIFI & Bluetooth Module Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_WIFI.png
   :alt: MY-A40I-MB204_WIFI.png

| Note: The 3.3V power supply must be designed for a current of more than 1.5A. The signal line circuit must be strictly pulled up in accordance with the schematic diagram, and the SDIO network group must be routed with equal lengths. The output line of the WL_BT_ANY output signal terminal (pin1 of the chip) must be as wide as possible. The network where E1 is located requires trace design to meet 50Ω impedance, with traces as short as possible and no right-angle bends. Components such as C93/R73/C92 must be placed as close as possible with π-type output, and both ends of the antenna output must be covered with copper GND.


MIC/HP/TVIN/TVOUT Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_MIC-HP.png
   :alt: MY-A40I-MB204_MIC-HP.png

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_TVIN-TVOUT.png
   :alt: MY-A40I-MB204_TVIN-TVOUT.png

| Note: The area under the MIC and HP traces must be hollowed out without copper cladding. Two groups of AAGND and TVGND must be connected in series with resistors to be isolated from GND. The traces for analog signals such as microphones and headphones must be thickened to more than 10mil, with smooth traces. It is best to use ground shielding and keep away from interference such as signal lines.


RS232/485/CAN Circuits
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_RS232.png
   :alt: MY-A40I-MB204_RS232.png

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_RS485.png
   :alt: MY-A40I-MB204_RS485.png

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_CAN.png
   :alt: MY-A40I-MB204_CAN.png

|  Note: The 3.3V power supply must be designed for a current of 1A or more, and the TX/RX signal line circuit must strictly adopt equidistant differential signal line routing. P14 is an internal debugging port; to facilitate later debugging, users should lead out this debugging serial port when designing the baseboard by themselves. For the 485 signal terminal matching resistors R47/R52, a 120-ohm resistor should be added depending on the number of loads and transmission length. When arranging components, place the two chips U16 and U17 close to the P21 interface.


SATA Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_SATA.png
   :alt: MY-A40I-MB204_SATA.png

|  Note: When designing the PCB, the two signal lines of each I2C channel should be routed in groups. This avoids excessive length deviation between the two network lines in the group when the routing distance is too long.


CSI (DVP) Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Port P2 is a reserved I/O led out from the core board. The output signal lines should be routed in groups, with the shortest possible length and equal differential length. The 3.3V/1.8V circuit must be designed for a current of 500mA or more.

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_CSI.png
   :alt: MY-A40I-MB204_CSI.png


I2C Parallel Connection and Core Board Connection Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  One I2C bus can be connected to multiple devices, and 0-ohm resistors are reserved for debugging purposes. Each I2C bus should be connected to pull-up resistors to the logic level, so as to prevent the signal lines from being floating and enhance the driving capability. When designing the PCB, the two signal lines of each I2C channel should be routed in groups to avoid excessive length deviation between the two network lines in the group when the routing distance is too long.
|  For the 5V power supply part of the core board, copper cladding and power traces for a 3A current must be reserved. If traces need to be routed on both the top and bottom layers, multiple vias should be drilled to prevent PCB burnout due to instantaneous overload when the power is turned on, thus ensuring normal power supply. Filter capacitors should be placed nearby, and output signal lines should be routed in groups with the shortest possible length and equal differential length.

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/MY-A40I-MB204_IIC.png
   :alt: MY-A40I-MB204_IIC.png