MYZR-RZG2L Hardware Introduction
===================================

Interface Overview
---------------------

Front View
~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/963px-Myzr_rzg2l_zheng.jpg
   :alt: 963px-Myzr_rzg2l_zheng.jpg

Back View
~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/963px-Myzr_rzg2l_bei.jpg
   :alt: 963px-Myzr_rzg2l_bei.jpg

Dimension Drawing
~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/963px-Myzr_rzg2l_chicun.png
   :alt: 963px-Myzr_rzg2l_chicun.png

Diagram Modules
~~~~~~~~~~~~~~~~~

+-----+--------------+---------------------------+--------------------------------+------------+
| No. |  Interface   |         Function          |         Interface Type         | Silkscreen |
+=====+==============+===========================+================================+============+
| 1   | 5V_IN        | Power Input               | DC-005 Round Port              | J1         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 2   | PWR-ON/OFF   | Power Switch              | Rocker Switch                  | J2         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 3   | Ethernet     | 2 x 10/100/1000M Ethernet | RJ45                           | U10, U13   |
+-----+--------------+---------------------------+--------------------------------+------------+
| 4   | DEBUG UART   | Debug Serial Port         | PH1.25 Pin Header (4-Pin)      | P4         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 5   | RS232        | RS232 Interface           | Phoenix Terminal Interface     | J10        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 6   | RS485        | RS485 Interface           | Phoenix Terminal Interface     | J10        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 7   | CAN          | CAN Interface             | Phoenix Terminal Interface     | J10        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 8   | 4G Module    | 4G Module Interface       | MINI-PCIE                      | J9         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 9   | SIM          | SIM Card                  | MICRO SIM Drawer Type          | COM3       |
+-----+--------------+---------------------------+--------------------------------+------------+
| 10  | TF           | TF Card                   | Standard TF Card Pop-Up Socket | J8         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 11  | USB          | USB2.0                    | Double-Layer USB-A             | J4         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 12  | RGB          | RGB Display Interface     | FPC Socket (40Pin)             | P1         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 13  | DSI          | MIPI Display Interface    | FPC Socket (30Pin)             | J6         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 14  | Antenna      | WIFI & Bluetooth          | IPX Connector                  | E2         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 15  | USB          | USB OTG                   | TYPE-C                         | J5         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 16  | Audio        | Audio Output, Input       | 3.5mm Headphone Jack           | P2         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 17  | Reset Button | Reset                     | Tactile Button Switch          | SW2        |
+-----+--------------+---------------------------+--------------------------------+------------+
| 18  | CSI          | Camera                    | FPC Socket (30Pin)             | J7         |
+-----+--------------+---------------------------+--------------------------------+------------+
| 19  | BOOT MODE    | Boot Mode Selection       | DIP Switch (4-Position)        | SW1        |
+-----+--------------+---------------------------+--------------------------------+------------+

Backplane Schematic Design Description
----------------------------------------

Main Power Supply Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The backplane power is supplied by a 5V DC power source, which is introduced through the DC-005 socket (J1).

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_power1.png
   :alt: Myzr_rzg2l_power1.png

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_power2.png
   :alt: Myzr_rzg2l_power2.png

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_power3.png
   :alt: Myzr_rzg2l_power3.png

| After the 5V power passes through the self-recovering fuse and the 5.6V overvoltage protection circuit, it steps down to 3.6V via DCDC to supply power to the core board. After the core board starts up, it controls the 5V-to-3.3V conversion on the backplane through the MainPWR_EN signal. This ensures that the core board starts first before powering other components on the backplane, preventing the occurrence of latch-up effect. The power consumption of the RZG2L_MB200 development board varies under different states. In actual tests, after installing the EC20-4G module and the company's RGB display touch screen, the maximum current during startup exceeds 1.2A. In practical use, it is recommended to select a 5V switching power adapter with an output current of not less than 3A.

BOOT Circuit
~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_boot.png
   :alt: Myzr_rzg2l_boot.png

| SW1 is the BOOT DIP switch on the backplane. When the core board starts, it needs to read the BOOT mode first (refer to the schematic for specific BOOT startup modes).

Reset Circuit
~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_reset.png
   :alt: Myzr_rzg2l_reset.png

| The reset circuit is active low. The core board has an internal pull-up resistor, so no external pull-up resistor is required on the backplane during design.

External TF Card Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/963px-Myzr_rzg2l_tfcard.png
   :alt: 963px-Myzr_rzg2l_tfcard.png

| The TF card circuit uses the SDIO bus interface. It must be designed strictly in accordance with this schematic, and pull-up resistors are indispensable. Note: For the SDIO interface network with pull-up resistors on the right side of the diagram, equal-length routing must be implemented during PCB design, and a 3W spacing requirement must be met with overall ground shielding.

RTC Real-Time Clock Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_rtc.png
   :alt: Myzr_rzg2l_rtc.png

| The RTC chip used in this circuit has a built-in crystal matching capacitor. If you need to replace the solution, pay attention to the crystal accuracy. Matching capacitors can be connected in parallel between the two crystal networks and ground to adjust the accuracy if necessary. When the backplane is powered on, the 3.3V power on the backplane supplies power to the RTC chip and charges the battery BT1; when the backplane is powered off, the battery BT1 discharges to serve as the power source for the RTC chip.

Ethernet Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_ethernet1.png
   :alt: Myzr_rzg2l_ethernet1.png

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_ethernet2.png
   :alt: Myzr_rzg2l_ethernet2.png

| To support Ethernet, an Ethernet port chip must be added to the backplane and connected through the RJ45 interface. It should be noted that the two indicator lights of the RJ45 interface must be designed in accordance with this schematic. Note: During PCB design, the 4 groups of Ethernet signal lines must be routed in accordance with differential rules and with equal length within each differential pair. The spacing between differential pairs and other networks must be at least 3 times the line width; the equal-length error within a differential pair must be within 5mil, and the equal-length error between differential pairs must be within 25mil.

USB HUB Expansion (USB HOST Circuit)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_usbhost1.png
   :alt: Myzr_rzg2l_usbhost1.png

| This circuit expands one USB interface of the core board into 4 USB interfaces. During PCB design, the 90Ohm/DLM11SN900HY2L common-mode filter should be placed close to the chip. Each group of USB signal lines must be routed in accordance with differential rules and with equal length within each differential pair. The spacing between differential pairs and other networks should be at least 3 times the line width as much as possible, and the equal-length error within a differential pair must be within 5mil. The USB HOST chip has two USB outputs connected to USB-A female sockets, which can be used to connect external devices such as U disks or mice. The circuit is shown in the following figure:

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_usbhost2.png
   :alt: Myzr_rzg2l_usbhost2.png

| E1 in the figure is the control & protection chip for the 5V output power of the USB interface. U6 controls two power channels in total, and the control signal for each channel comes from the PRTPWR and OCS networks of the corresponding channel of the USB HOST chip. As shown in the following figure, the remaining peripheral circuits of the USB HOST chip must be designed completely with reference to the schematic of this development board. During PCB design, the traces of the chip's power network should be widened, and the power decoupling capacitors should be placed close to the chip pins; the crystal oscillator should be placed close to the chip, and the crystal oscillator network should be kept away from other signal lines as much as possible with ground shielding. Ground shielding is also required around the crystal oscillator itself.

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_usbhost3.png
   :alt: Myzr_rzg2l_usbhost3.png

MINI_PCIE - 4G Module Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/963px-Myzr_rzg2l_4g.png
   :alt: 963px-Myzr_rzg2l_4g.png

| This circuit is designed based on the EC20-4G module and adopts the PCI Express Mini Card 1.2 standard interface. In practice, it communicates with the CPU through the USB network. The theoretical maximum current required by the module can reach more than 2A. Therefore, during PCB design, the power traces must be widened, and the power decoupling capacitors should be placed close to the interface pins. The total capacitance of the capacitors is recommended to be greater than 470uF. The USB signal lines must be routed in accordance with differential rules and with equal length within each differential pair. The spacing between differential pairs and other networks should be at least 3 times the line width as much as possible, and the equal-length error within a differential pair must be within 5mil. D6 is the working status indicator light of the module; CON3 is the SIM card socket, which should be placed close to the 4G module. The network between the module and the SIM card must be routed in groups to avoid excessive length and length error, and kept away from strong signal interference sources and traces.

RGB Touch Display Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_rgb.png
   :alt: Myzr_rzg2l_rgb.png

| This circuit is designed based on the company's 7-inch RGB touch display interface. It is powered by a single 5V supply with a peak current of up to 1A. The display communicates via the RGB888 bus, and the touch screen communicates via the IIC bus. During PCB design, the RGB888 bus network must be routed with equal length between the core board and the interface, and the line spacing must meet the 3W rule requirement; the IIC bus must be routed in groups to avoid excessive length and length error.

MIPI_CSI/DSI Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/963px-Myzr_rzg2l_csidsi.png
   :alt: 963px-Myzr_rzg2l_csidsi.png

WIFI & Bluetooth Module Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_wifi.png
   :alt: Myzr_rzg2l_wifi.png

| This development board communicates with the WIFI & Bluetooth module via USB. During PCB design, the USB signal lines must be routed in accordance with differential rules and with equal length within each differential pair; the network where the antenna interface E1 is located in the figure must be routed to meet the 50Ω impedance design requirement. The traces should be as short as possible without right-angle bends, and ground shielding is required around them to avoid signal interference.

Audio Circuit
~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/963px-Myzr_rzg2l_audio1.png
   :alt: 963px-Myzr_rzg2l_audio1.png

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_audio2.png
   :alt: Myzr_rzg2l_audio2.png

| The backplane hardware uses the WM8960 audio chip, and the following descriptions about the audio chip are all for this WM8960 chip. The audio chip outputs stereo audio signals to headphones and speakers, and receives mono audio signals from the microphone. P12 is the built-in Class D power amplifier output terminal of the WM8960 audio chip. When an 8Ω speaker is connected, the output power is 1W; when a 4Ω speaker is connected, the output power is 2W. Note: The speaker power comes from the Class D power amplifier, not the traditional analog power amplifier. A speaker is connected to two adjacent pins of the socket. Two speakers cannot share wires, nor can the speaker be connected to the ground wire. If the user needs to connect an external power amplifier, the signal can only be obtained from the headphone socket, not from the speaker interface. The audio function requires an external clock to work. During PCB design, the I2S0 signal, Audio_SCL, and Audio_SDA network groups must be routed in groups to avoid excessive length and length error. The traces of analog signals such as the microphone and headphone must be widened to more than 10mil, with smooth traces. Ground shielding is preferably implemented, and they should be kept away from signal lines and other interference sources.

CAN Communication Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/963px-Myzr_rzg2l_can.png
   :alt: 963px-Myzr_rzg2l_can.png

| During PCB design, the CAN0_TX and CAN0_RX networks must be routed in groups to avoid excessive length and length error. In component placement, U20 should be placed close to the interface.

RS232 Communication Interface Circuit and Debug Port Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/963px-Myzr_rzg2l_rs232.png
   :alt: 963px-Myzr_rzg2l_rs232.png

| The P4 interface in the figure is the debug port and program burning port of the development board. During PCB design, both UART0 and UART4 must be routed in groups to avoid excessive length error between the two networks in the group when the traces are too long.


RS485 Communication Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_rs485.png
   :alt: Myzr_rzg2l_rs485.png

| Resistor R171 in the figure is a matching resistor. Whether to connect it or not and its resistance value depend on the signal of the external circuit during connection. When designing the PCB, UART4 should be routed as a group to avoid excessive length deviation between the two network traces in the group when the routing distance is too long; the A and B networks should be routed differentially.

OTG Circuit
~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2L/Myzr_rzg2l_otg.png
   :alt: Myzr_rzg2l_otg.png

| The OTG uses a TYPE-C interface, and the pull-up resistors for the ID pin should be greater than 30kΩ; when using this set of USB signals, a 3.3V voltage needs to be input to USB0_VBUSIN; U7 is the control & protection chip for the 5V output power supply of the OTG-USB interface. When designing the PCB, the USB network should strictly follow the differential equal-length routing principle.