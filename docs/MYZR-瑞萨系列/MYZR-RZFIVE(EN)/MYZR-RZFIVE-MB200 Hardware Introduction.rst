MYZR-RZFIVE-MB200 Hardware Introduction
=========================================

Interface Overview
--------------------

Front View
~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzfive_zheng.jpg
   :alt: 963px-Myzr_rzfive_zheng.jpg

Rear View
~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzg2ul-eth_bei.jpg
   :alt: 963px-Myzr_rzg2ul-eth_bei.jpg

Dimension Drawing
~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzg2ul_chicun.png
   :alt: 963px-Myzr_rzg2ul_chicun.png

Diagram Module (ETH Version)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----+--------------+---------------------------+--------------------------------+------------+
| No. |  Interface   |         Function          |         Interface Type         | Silkscreen |
+=====+==============+===========================+================================+============+
| 1   | 5V_IN        | Power Input               | DC-005 Round Port              | J1         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 2   | PWR-ON/OFF   | Power Switch              | Rocker Switch                  | J2         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 3   | Ethernet     | 2 x 10/100/1000M Ethernet | RJ45                           | U10, U14   |
+-----+--------------+---------------------------+--------------------------------+------------+
| 4   | DEBUG UART   | Debug UART                | PH1.25 Pin Header (4-pin)      | P3         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 5   | RS232        | RS232 Interface           | Phoenix Terminal Interface     | J16        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 6   | RS485        | RS485 Interface           | Phoenix Terminal Interface     | J16        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 7   | CAN          | CAN Interface             | Phoenix Terminal Interface     | J16        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 8   | 4G Module    | 4G Module Interface       | MINI-PCIE                      | J10        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 9   | SIM          | SIM Card                  | Micro SIM Drawer Type          | COM2       |
+-----+--------------+---------------------------+--------------------------------+------------+
| 10  | TF           | TF Card                   | Standard TF Card Pop-up Socket | J7         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 11  | USB          | USB2.0                    | Double-layer USB-A             | J4         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 12  | Antenna      | WIFI & Bluetooth          | IPX Connector                  | E2         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 13  | USB          | USB OTG                   | TYPE-C                         | J5         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 14  | Audio        | Audio Output, Input       | 3.5mm Headphone Jack           | P1         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 15  | Reset Button | Reset                     | Tactile Switch                 | SW2        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 16  | CSI          | Camera                    | FPC Socket (30Pin)             | J7         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 17  | BOOT MODE    | Boot Mode Selection       | DIP Switch (4-bit)             | SW1        |
+-----+--------------+---------------------------+--------------------------------+------------+

Diagram Module (LCD Version)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----+--------------+---------------------------+--------------------------------+------------+
| No. |  Interface   |         Function          |         Interface Type         | Silkscreen |
+=====+==============+===========================+================================+============+
| 1   | 5V_IN        | Power Input               | DC-005 Round Port              | J1         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 2   | PWR-ON/OFF   | Power Switch              | Rocker Switch                  | J2         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 3   | Ethernet     | 1 x 10/100/1000M Ethernet | RJ45                           | U9         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 4   | DEBUG UART   | Debug UART                | PH1.25 Pin Header (4-pin)      | P3         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 5   | RS232        | RS232 Interface           | Phoenix Terminal Interface     | J16        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 6   | RS485        | RS485 Interface           | Phoenix Terminal Interface     | J16        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 7   | CAN          | CAN Interface             | Phoenix Terminal Interface     | J16        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 8   | 4G Module    | 4G Module Interface       | MINI-PCIE                      | J9         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 9   | SIM          | SIM Card                  | Micro SIM Drawer Type          | COM2       |
+-----+--------------+---------------------------+--------------------------------+------------+
| 10  | TF           | TF Card                   | Standard TF Card Pop-up Socket | J7         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 11  | USB          | USB2.0                    | Double-layer USB-A             | J4         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 12  | RGB          | RGB Screen Interface      | FPC Socket (40Pin)             | P1         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 13  | Antenna      | WIFI & Bluetooth          | IPX Connector                  | E2         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 14  | USB          | USB OTG                   | TYPE-C                         | J5         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 15  | Audio        | Audio Output, Input       | 3.5mm Headphone Jack           | P2         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 16  | Reset Button | Reset                     | Tactile Switch                 | SW2        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 17  | CSI          | Camera                    | FPC Socket (30Pin)             | J6         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 18  | BOOT MODE    | Boot Mode Selection       | DIP Switch (4-bit)             | SW1        |
+-----+--------------+---------------------------+--------------------------------+------------+

Schematic Design Description of the Baseboard
-----------------------------------------------

Main Power Supply Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The baseboard power is supplied by a 5V DC power source, which is introduced through the DC-005 socket (J1).

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_power1.png
   :alt: Myzr_rzg2ul_power1.png

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_power2.png
   :alt: Myzr_rzg2ul_power2.png

| After the 5V power passes through a self-recovering fuse and a 5.6V overvoltage protection circuit, it outputs 3.6V through DCDC buck conversion to power the core board. After the core board starts up, it controls the baseboard's 5V to 3.3V conversion via the MainPWR_EN signal. This ensures that the core board starts first before powering other components on the baseboard, preventing the occurrence of latch-up effects. The power consumption of the RZFIVE_EK200 development board varies under different states. In actual tests, when the EC20-4G module and the company's RGB display touch screen are installed, the maximum current during startup exceeds 1.2A. In practical use, it is recommended to select a 5V switching power adapter with an output current of not less than 3A.

BOOT Circuit
~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_boot.png
   :alt: Myzr_rzg2ul_boot.png

| SW1 is the BOOT DIP switch on the baseboard. When the core board starts, it first needs to read the BOOT mode (refer to the schematic for specific BOOT startup modes).

Reset Circuit
~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_reset.png
   :alt: Myzr_rzg2ul_reset.png

| The reset circuit is integrated with the watchdog circuit, which is active at low level and requires a pull-up resistor.

External TF Card Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzg2ul_tfcard.png
   :alt: 963px-Myzr_rzg2ul_tfcard.png

| The TF card circuit uses an SDIO bus interface. The design must strictly follow this schematic, and pull-up resistors are indispensable. Note: For the SDIO interface network with pull-up resistors on the right side of the diagram, equal-length routing must be implemented during PCB design, with a 3W spacing requirement and overall ground shielding.

RTC Real-Time Clock Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_rtc.png
   :alt: Myzr_rzg2ul_rtc.png

| The RTC chip used in this circuit has a built-in crystal matching capacitor. If a different solution needs to be replaced, attention must be paid to the crystal accuracy. Matching capacitors can be connected in parallel between the two crystal networks and ground to adjust the accuracy if necessary. When the baseboard is powered on, the 3.3V power supply of the baseboard powers the RTC chip and charges the battery BT1; when the baseboard is powered off, the battery BT1 discharges to serve as the power source for the RTC chip.

Ethernet Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzg2ul_ethernet1.png
   :alt: 963px-Myzr_rzg2ul_ethernet1.png

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_ethernet2.png
   :alt: Myzr_rzg2ul_ethernet2.png

| To support Ethernet, an Ethernet port chip must be added to the baseboard and connected via an RJ45 interface. It should be noted that the two indicator lights of the RJ45 interface must be designed in accordance with this schematic. Note: During PCB design, the 4 groups of Ethernet signal lines must be routed in accordance with differential rules and have equal lengths within each differential pair. A spacing of more than 3 times the line width must be maintained between differential pairs and other networks; the equal-length error within a differential pair must be within 5mil, and the equal-length error between differential pairs must be within 25mil.

USB Network Expansion USB HOST Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_usbhost1.png
   :alt: Myzr_rzg2ul_usbhost1.png

| This circuit expands one USB interface of the core board into 4 USB interfaces. During PCB design, the 90Ohm/DLM11SN900HY2L common-mode filter should be placed close to the chip. Each group of USB signal lines must be routed in accordance with differential rules and have equal lengths within each differential pair. A spacing of more than 3 times the line width should be maintained between differential pairs and other networks, and the equal-length error within a differential pair must be within 5mil. The USB HOST chip has two USB outputs connected to USB-A female sockets, which can be used to connect external devices such as U disks or mice. The circuit is shown in the following figure:

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_usbhost2.png
   :alt: Myzr_rzg2ul_usbhost2.png

| E1 in the figure is the control & protection chip for the 5V output power of the USB interface. U6 controls two power channels in total, and the control signal for each channel comes from the PRTPWR and OCS networks of the corresponding channel of the USB HOST chip. As shown in the following figure, the remaining peripheral circuits of the USB HOST chip must be designed with full reference to the schematic of this development board. During PCB design, the power network traces of the chip should be thickened, and power decoupling capacitors should be placed close to the chip pins; the crystal should be placed close to the chip, and the crystal network should be kept away from other signal lines with ground shielding. Ground shielding is also required around the crystal itself.

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_usbhost3.png
   :alt: Myzr_rzg2ul_usbhost3.png

MINI_PCIE - 4G Module Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzg2ul_4g.png
   :alt: 963px-Myzr_rzg2ul_4g.png

| This circuit is designed based on the EC20-4G module and adopts the PCI Express Mini Card 1.2 standard interface. In practice, it communicates with the CPU via the USB network. The theoretical maximum current required by the module can exceed 2A. Therefore, during PCB design, the power traces must be thickened, and power decoupling capacitors should be placed close to the interface pins. The total capacitance of the capacitors is recommended to be greater than 470uF; the USB signal lines must be routed in accordance with differential rules and have equal lengths within each differential pair. A spacing of more than 3 times the line width should be maintained between differential pairs and other networks, and the equal-length error within a differential pair must be within 5mil; D6 is the working status indicator light of the module; CON3 is the SIM card socket, which should be placed close to the 4G module. The network from the module to the SIM card must be routed in groups to avoid excessive length and length errors, and kept away from strong signal interference sources and traces.

RGB Touch Display Screen Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_rgb.png
   :alt: Myzr_rzg2ul_rgb.png

| This circuit is designed based on the company's 7-inch RGB touch display screen interface. It is powered by a single 5V supply and has a peak current of up to 1A. The display screen communicates via the RGB888 bus, and the touch screen communicates via the IIC bus interface. During PCB design, the networks of the RGB888 bus must be routed with equal lengths between the core board and the interface, and the line spacing must meet the 3W rule requirement; the IIC bus must be routed in groups to avoid excessive length and length errors.

MIPI_CSI/DSI Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzg2ul_csidsi.png
   :alt: 963px-Myzr_rzg2ul_csidsi.png

| This development board's interface circuit is designed based on the MIPI screen and camera used by our company. It requires 5V, 3.3V, and 1.8V power supplies, and the MIPI screen is equipped with touch functionality. During PCB design, the networks of the MIPI bus must be routed with differential equal lengths between the core board and the interface, and the spacing must meet the 3W rule requirement; the IIC bus must be routed in groups to avoid excessive length and length errors.

WIFI & Bluetooth Module Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_wifi.png
   :alt: Myzr_rzg2ul_wifi.png

| This development board communicates with the WIFI & Bluetooth module via USB. During PCB design, the USB signal lines must be routed in accordance with differential rules and have equal lengths within each differential pair; the network where the antenna interface E1 is located in the figure must be routed to meet the 50Ω impedance design. The traces should be as short as possible without right-angle bends, and ground shielding is required around them to avoid signal interference.


Audio Circuit
~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzg2ul_audio1.png
   :alt: 963px-Myzr_rzg2ul_audio1.png

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_audio2.png
   :alt: Myzr_rzg2ul_audio2.png

| The audio chip used in the baseboard hardware is the WM8960, and the following descriptions of the audio chip all apply to this WM8960 chip. The audio chip outputs stereo audio signals to headphones and speakers, while it receives mono audio signals from the microphone. P12 is the built-in Class D power amplifier output terminal of the WM8960 audio chip. When an 8Ω speaker is connected, the output power is 1W; when a 4Ω speaker is connected, the output power is 2W. **Note**: The speaker power comes from the Class D power amplifier, not the traditional analog power amplifier. Connect one speaker to two adjacent pins of the socket—do not share wires between two speakers, and do not connect the speaker to the ground wire. If the user needs to connect an external power amplifier, the signal can only be taken from the headphone socket, not from the speaker interface. The audio function requires an external clock to operate. During PCB design, the I2S0 signal, along with the Audio_SCL and Audio_SDA network groups, must be routed in groups to avoid excessive length and large length errors. For the routing of analog signals such as those for microphones and headphones, the trace width must be increased to more than 10mil, the traces should be smooth, and ground shielding is recommended. These traces must be kept away from interference sources such as signal lines.

CAN Communication Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzg2ul_can.png
   :alt: 963px-Myzr_rzg2ul_can.png

| During PCB design, the CAN0_TX and CAN0_RX networks must be routed in groups to avoid excessive length and large length errors. In component placement, U20 should be placed close to the interface.

RS232 Communication Interface Circuit and Debug Port Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/963px-Myzr_rzg2ul_rs232.png
   :alt: 963px-Myzr_rzg2ul_rs232.png

| The P4 interface in the figure serves as the debug port and program burning port of the development board. During PCB design, both UART0 and UART4 must be routed in groups to avoid large length errors between the two networks in the group when the routing distance is too long.

RS485 Communication Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_rs485.png
   :alt: Myzr_rzg2ul_rs485.png

| Resistor R171 in the figure is a matching resistor. Whether to connect it and its resistance value depend on the signal of the external circuit. During PCB design, UART4 should be routed in groups to avoid large length errors between the two networks in the group when the routing distance is too long; the A and B networks must be routed as differential pairs.

OTG Circuit
~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZFIVE/Myzr_rzg2ul_otg.png
   :alt: Myzr_rzg2ul_otg.png

| The OTG uses a TYPE-C interface. The pull-up resistors for the ID pin and other pins must be greater than 30kΩ. When using this group of USB signals, a 3.3V voltage must be input to USB0_VBUSIN; U7 is the control & protection chip for the 5V output power of the OTG-USB interface. During PCB design, the USB network must strictly follow the differential equal-length routing rule.
