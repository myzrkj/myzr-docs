Hardware Design Guide
=======================

Core Board Pin Schematic
--------------------------

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/核心板引脚原理图-1.png
   :alt: Core Board Pin Schematic-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/核心板引脚原理图-2.png
   :alt: Core Board Pin Schematic-2.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/核心板引脚原理图-3.png
   :alt: Core Board Pin Schematic-3.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/核心板引脚原理图-4.png
   :alt: Core Board Pin Schematic-4.png
   :width: 80%

Baseboard Schematic
---------------------

Power Management
~~~~~~~~~~~~~~~~~~~

|  The baseboard power supply is a DC 12V input, connected via a DC-005 socket. J1 is the power socket. After passing through SW1 (power switch), the 12V is converted to 5V, 4V, and 3.3V by the MP8759 and RT8070-ZQW. The 3.3V is then further converted to 1.8V by the SY8089AAC.

|  The power supply section schematic for the 3588 development board is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/电源管理-1.png
   :alt: Power Management-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/电源管理-2.png
   :alt: Power Management-2.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/电源管理-3.png
   :alt: Power Management-3.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/电源管理-4.png
   :alt: Power Management-4.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/电源管理-5.png
   :alt: Power Management-5.png
   :width: 80%

Button Battery Circuit
~~~~~~~~~~~~~~~~~~~~~~~~

|  The button battery on the 3588 development board is used to power the RTC module, ensuring continuous power supply to the RTC module when the system power is off. The HYM8563TS is the real-time clock chip, which communicates with the core board via I2C.

|  The schematic is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/纽扣电池电路.png
   :alt: Button Battery Circuit.png
   :width: 80%

Fan Circuit
~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/风扇电路.png
   :alt: Fan Circuit.png
   :width: 80%

SATA Power Circuit
~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/SATA电源电路.png
   :alt: SATA Power Circuit.png
   :width: 80%

USB2.0 HOST Circuit
~~~~~~~~~~~~~~~~~~~~~

|  The development board provides one USB2.0 port. The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/USB2.0HOST_电路.png
   :alt: USB2.0HOST_Circuit.png
   :width: 80%

USB3.0HOST Circuit
~~~~~~~~~~~~~~~~~~~~

|  The development board provides one USB3.0 port. The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/USB3.0HOST电路.png
   :alt: USB3.0HOST Circuit.png
   :width: 80%

Type-C Circuit
~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/Type-C电路.png
   :alt: Type-C Circuit.png
   :width: 80%

USB2.0 HUB Circuit
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/USB2.0HUB电路.png
   :alt: USB2.0HUB Circuit.png
   :width: 80%

TF Card Circuit
~~~~~~~~~~~~~~~~~

|  The development board provides a push-push TF card socket. The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/TF卡电路.png
   :alt: TF Card Circuit.png
   :width: 80%

Camera_MIPI Circuit
~~~~~~~~~~~~~~~~~~~~~~

|  The camera interface circuit is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/Camera_MIPI电路-1.png
   :alt: Camera_MIPI Circuit-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/Camera_MIPI电路-2.png
   :alt: Camera_MIPI Circuit-2.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/Camera_MIPI电路-3.png
   :alt: Camera_MIPI Circuit-3.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/Camera_MIPI电路-4.png
   :alt: Camera_MIPI Circuit-4.png
   :width: 80%

HDMI RX Circuit
~~~~~~~~~~~~~~~~~

|  The development board's HDMI interface supports HDMI2.0 protocol. The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI_RX电路.png
   :alt: HDMI_RX Circuit.png
   :width: 80%

HDMI TX Circuit
~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI_TX_电路-1.png
   :alt: HDMI_TX_Circuit-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI_TX_电路-2.png
   :alt: HDMI_TX_Circuit-2.png
   :width: 80%

MIPI Display Interface Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The MIPI_DSI of the RK3588 processor supports a maximum resolution of 4K@60Hz and up to 4 data lanes. It is routed out from the development board via a 30-pin FPC with a pitch of 0.5mm.

|  The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/MIPI显示屏接口电路.png
   :alt: MIPI Display Interface Circuit.png
   :width: 80%

LCD-eDP Circuit
~~~~~~~~~~~~~~~~~

|  The EDP interface of the RK3588 processor development board supports a maximum resolution of 4K@60Hz. It is routed out from the development board via a 30-pin FPC with a pitch of 0.5mm (J12).

|  The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/LCD-eDP电路.png
   :alt: LCD-eDP Circuit.png
   :width: 80%

WiFi Bluetooth Circuit
~~~~~~~~~~~~~~~~~~~~~~~~

|  The development board features an onboard Wifi & Bluetooth combo module, model RTL8723.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/WiFi蓝牙电路.png
   :alt: WiFi Bluetooth Circuit.png
   :width: 80%

Audio Circuit
~~~~~~~~~~~~~~~

|  In the audio circuit, L/ROUT1 are the left and right channel interfaces for the headphone jack, HP_DET_L is the headphone detection interface, MIC2P/N are the mic input interfaces, and SPK_P and SPK_N are the speaker interfaces.
|  The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/音频电路.png
   :alt: Audio Circuit.png
   :width: 80%

Gigabit Ethernet Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The baseboard provides two Gigabit Ethernet interfaces, using the RGMII interface to connect to the PHY chip RTL8211F. They are routed out via RJ45 sockets, model HR911130C, which have built-in isolation transformers.

|  The schematic for Ethernet 0 is as follows:

|  PHY Chip

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/千兆网电路-1.png
   :alt: Gigabit Ethernet Circuit-1.png
   :width: 80%

|  Ethernet Port

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/千兆网电路-2.png
   :alt: Gigabit Ethernet Circuit-2.png
   :width: 80%

|  The schematic for Ethernet 1 is as follows:
|  PHY Chip

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/千兆网电路-3.png
   :alt: Gigabit Ethernet Circuit-3.png
   :width: 80%

|  Ethernet Port

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/千兆网电路-4.png
   :alt: Gigabit Ethernet Circuit-4.png
   :width: 80%

SATA3.0 Circuit
~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/SATA3.0电路.png
   :alt: SATA3.0 Circuit.png
   :width: 80%

5G Circuit
~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/5G电路.png
   :alt: 5G Circuit.png
   :width: 80%

PCIE 3.0 Circuit
~~~~~~~~~~~~~~~~~~

|  The development board features an onboard M.2 interface on the backside for connecting SSDs. The schematic is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/PCIE3.0电路-1.png
   :alt: PCIE3.0 Circuit-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/PCIE3.0电路-2.png
   :alt: PCIE3.0 Circuit-2.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/PCIE3.0电路-3.png
   :alt: PCIE3.0 Circuit-3.png
   :width: 80%

Sensor Circuit
~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/Sensor电路.png
   :alt: Sensor Circuit.png
   :width: 80%

Button Circuit
~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/按键电路-1.png
   :alt: Button Circuit-1.png
   :width: 80%

|  The button PCB is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/按键电路-2.png
   :alt: Button Circuit-2.png
   :width: 80%

Debug UART Circuit
~~~~~~~~~~~~~~~~~~~~

|  The development board reserves a TTL-level debug UART (J22) for connecting a serial console, as shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/调试串口电路.png
   :alt: Debug UART Circuit.png
   :width: 80%

485 Circuit
~~~~~~~~~~~~~

|  The 3588 development board features an onboard RS485 interface. The schematic is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/485电路.png
   :alt: 485 Circuit.png
   :width: 80%

Schematic Design Recommendations
-----------------------------------

Power Design
~~~~~~~~~~~~~~~

|  The baseboard power supply is a DC 12V input, which needs to generate 5V, 4V, 3.3V, and 1.8V power supplies for the core board and baseboard using DC-DC BUCK converters.
|  The 5V power on the development board is generated by the MP8759 chip. If another model needs to be used, choose a BUCK with a supply capability of at least 3A, output voltage accuracy within ±1.5%, and output ripple voltage within 30mV.
|  The 4V power is generated by the MP8759 chip. If another model needs to be used, choose a BUCK with a supply capability of at least 8A, output voltage accuracy within ±1.5%, and output ripple voltage within 30mV.
|  The 3.3V power is generated by the RT8070-ZQW chip. If another model needs to be used, choose a BUCK with a supply capability of at least 8A, output voltage accuracy within ±1.5%, and output ripple voltage within 30mV.
|  The 1.8V power is generated by the SY8089AAC chip. If another model needs to be used, choose a BUCK with a supply capability of at least 1.8A, output voltage accuracy within ±1.5%, and output ripple voltage within 30mV.

|  The power supply section schematic for the development board is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/电源设计-1.png
   :alt: Power Design-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/电源设计-2.png
   :alt: Power Design-2.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/电源设计-3.png
   :alt: Power Design-3.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/电源设计-4.png
   :alt: Power Design-4.png
   :width: 80%

Functional Interface Circuit Design Guide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RTC Circuit
^^^^^^^^^^^^^

|  The button battery on the development board is used to power the RTC module, ensuring a continuous power supply to the RTC module when the system power is off. The HYM8563 is the real-time clock chip, which communicates with the core board via I2C. The schematic is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计指南_RTC电路.png
   :alt: Design Guide_RTC Circuit.png
   :width: 80%

|  The I2C signals SCL and SDA require external pull-up resistors. Choose resistors with different values based on the bus load; 2.2Kohm pull-up resistors are recommended. The device addresses on the I2C bus must not conflict. The pull-up power supply must be consistent with the power supply.

USB2.0/3.0 Circuit
^^^^^^^^^^^^^^^^^^^^

|  The development board provides 1 Type-C port, 1 USB3.0 HOST port, and 3 USB2.0 HOST ports.
|  Only TYPEC0_USB2.0_OTG0_DP/TYPEC0_USB2.0_OTG_DM supports Download Firmware. If this interface is not used in the product, it must be reserved during debugging and production; otherwise, debugging and firmware burning will be impossible. Note: TYPEC0_USB20_VBUSDET must also be connected!
|  TYPEC0_USB20_OTG_ID has an internal pull-up resistor of approximately 200Kohm to 1.8V inside the chip.
|  TYPEC0_USB20_VBUSDET is the OTG and Device mode detection pin, active high, 2.7-3.3V, typical 3.0V.
|  OTG mode can be set to the following three modes:
|  OTG Mode: Automatically switches between Device mode or HOST mode based on the ID pin status. ID high is Device mode, ID pulled low is HOST mode. In Device mode, it also checks if the VBUSDET pin is high; if high, it pulls DP high and starts enumeration.
|  Device Mode: When set to this mode, the ID pin is not needed. It only checks if the VBUSDET pin is high; if high, it pulls DP high and starts enumeration.
|  HOST Mode: When set to this mode, the status of ID and VBUSDET does not need to be concerned. (If the product only needs HOST mode, but since only TYPEC0_USB20_OTG_DP/TYPEC0_USB20_OTG_DM is the system firmware burning port and is needed during debugging and production for burning and adb debugging, it needs to be set to Device mode. Therefore, the TYPEC0_USB20_VBUSDET signal must also be connected.)
|  The default mode before uboot starts is Device mode. After entering uboot, it can be configured to these three modes according to actual needs.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计指南_USB2.0_3.0电路-1.png
   :alt: Design Guide_USB2.0_3.0 Circuit-1.png
   :width: 80%

|  To enhance ESD and surge immunity, ESD devices must be reserved on the signals. The parasitic capacitance of the ESD for USB2.0 signals must not exceed 3pF. Additionally, series 2.2ohm resistors on the USB2.0 DP/DM signals enhance ESD and surge immunity and must not be removed. To suppress electromagnetic radiation, common mode chokes can be considered on the signal lines. Choose between resistors or common mode chokes during debugging based on the actual situation. See the figure below, using USB20_HOST0_DP/DM as an example. Other USB2.0 interfaces require the same treatment.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计指南_USB2.0_3.0电路-2.png
   :alt: Design Guide_USB2.0_3.0 Circuit-2.png
   :width: 80%

|  When using HOST functionality, it is recommended to add a current limiting switch to the 5V power supply. The current limit can be adjusted according to application needs. The current limiting switch is controlled by GPIO. It is recommended to add capacitors above 100uF and 100nF to the 5V power supply.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计指南_USB2.0_3.0电路-3.png
   :alt: Design Guide_USB2.0_3.0 Circuit-3.png
   :width: 80%

|  The Type-C protocol requires adding 100nF AC coupling capacitors on the SSTXP/N lines. AC coupling capacitors are recommended to use 0201 packages for lower ESR and ESL, which also reduces impedance changes on the line. All signals of the Type-C connector must have ESD devices, placed close to the USB connector during layout. For SSTXP/N and SSRXP/N signals, the ESD parasitic capacitance must not exceed 0.3pF.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计指南_USB2.0_3.0电路-4.png
   :alt: Design Guide_USB2.0_3.0 Circuit-4.png
   :width: 80%

|  The recommended matching design for USB2.0/USB3.0 interfaces is shown in the table below.

+------------------------+------------------+-----------------------------------------------------------------------+
| Signal                 | Connection       | Description                                                           |
+------------------------+------------------+-----------------------------------------------------------------------+
| TYPEC0_USB20_OTG_DP/DM | Series 2.2ohm R  | USB HS/FS/LS mode data input/output                                   |
+------------------------+------------------+-----------------------------------------------------------------------+
| TYPEC_SSTXP/SSTXN      | Series 100nF C   | USB SS mode data output                                               |
+------------------------+------------------+-----------------------------------------------------------------------+
| TYPEC_SSRXP/SSRXN      | Series 0ohm R    | USB SS mode data input                                                |
+------------------------+------------------+-----------------------------------------------------------------------+
| TYPEC_USB20_OTG_ID     | Series 100ohm R  | USB OTG ID recognition, required for Micro-USB interface              |
+                        +                  +-----------------------------------------------------------------------+
|                        |                  | External strong pull-up required, power must be connected to the same |
|                        |                  | power as USB20_AVDD_1V8                                               |
+------------------------+------------------+-----------------------------------------------------------------------+
| TYPEC_USB20_VBUSDET    | Resistive divider| USB OTG insertion detection                                           |
+------------------------+------------------+-----------------------------------------------------------------------+
| USB30_2_SSTXP/SSTXN    | Series 100nF C   | USB SS mode data output                                               |
+------------------------+------------------+-----------------------------------------------------------------------+
| USB30_2_SSRXP/SSRXN    | Series 0ohm R    | USB SS mode data input                                                |
+------------------------+------------------+-----------------------------------------------------------------------+
| HOST0_DP/DM            | Series 2.2ohm R  | USB HS/FS/LS mode data input/output                                   |
+------------------------+------------------+-----------------------------------------------------------------------+
| HOST1_DP/DM            | Series 2.2ohm R  | USB HS/FS/LS mode data input/output                                   |
+------------------------+------------------+-----------------------------------------------------------------------+

5G Circuit
^^^^^^^^^^^^

|  The development board features an onboard M.2 B-Key interface 5G module. The HOST_D3P/M signals are for the 4G module, and the USB30_2_SSRX/SSTX signals are for the 5G module.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计指南_5G电路-1.png
   :alt: Design Guide_5G Circuit-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计指南_5G电路-2.png
   :alt: Design Guide_5G Circuit-2.png
   :width: 80%

MIPI_D/CPHY_RX Circuit
^^^^^^^^^^^^^^^^^^^^^^^^

|  RK3588 has two MIPI D-PHY/C-PHY CSI RX Combo PHYs. The D-PHY supports MIPI V2.0, with 0/1/2/3 Lanes in D-PHY mode and a maximum data rate of 4.5Gbps. The C-PHY supports V1.1, with 0/1/2 Trios in C-PHY mode (each Trio has A/B/C 3 wires) and a maximum data rate of 5.7Gbps/Trio (2.5Gsps).

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/CPHY_RX电路-1.png
   :alt: CPHY_RX Circuit-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/CPHY_RX电路-2.png
   :alt: CPHY_RX Circuit-2.png
   :width: 80%

|  MIPI D/C-PHY0 operating in D-PHY mode support:

 | Supports x4Lane mode, MIPI_DPHY0_RX_D[3:0] data references MIPI_DPHY0_RX_CLK;
 | Does not support splitting into x2Lane+x2Lane mode.

|  MIPI D/C-PHY1 operating in D-PHY mode support:

 | Supports x4Lane mode, MIPI_DPHY1_RX_D[3:0] data references MIPI_DPHY1_RX_CLK;
 | Does not support splitting into x2Lane+x2Lane mode.

|  The Camera's DVDD power supply can be 1.2V/1.5V/1.8V, etc. Please provide the accurate power supply according to the Camera's specification. Some Cameras have high DVDD current; if it exceeds 100mA, it is recommended to use a DCDC power supply. If the Camera has AF function, VCC2V8_AF needs a separate power supply. The development board generates it from 3.3V via an LDO power chip.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/CPHY_RX电路-3.png
   :alt: CPHY_RX Circuit-3.png
   :width: 80%

|  The Camera's PWDN signal must be controlled by GPIO, and the GPIO level must match the Camera IO level. The Camera's Reset signal is recommended to be controlled by GPIO, and the GPIO level must match the Camera IO level.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/CPHY_RX电路-4.png
   :alt: CPHY_RX Circuit-4.png
   :width: 80%

|  The recommended matching design for MIPI D-PHY/C-PHY Combo PHY0/1 RX is shown in the table below:

+---------------------------+------------+--------------------------------+
| Signal                    | Connection | Description                    |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY0_RX_D0P/D0N     | Direct     | MIPI_DPHY0_RX Data Lane0 Input |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY0_RX_D1P/D1N     | Direct     | MIPI_DPHY0_RX Data Lane1 Input |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY0_RX_D2P/D2N     | Direct     | MIPI_DPHY0_RX Data Lane2 Input |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY0_RX_D3P/D3N     | Direct     | MIPI_DPHY0_RX Data Lane3 Input |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY0_RX_CLKP/CLKN   | Direct     | MIPI_DPHY0_RX Clock Input      |
+---------------------------+------------+--------------------------------+
| MIPI_CPHY0_RX_TRIO0_A/B/C | Direct     | MIPI_CPHY0_RX_TRIO0 Input      |
+---------------------------+------------+--------------------------------+
| MIPI_CPHY0_RX_TRIO1_A/B/C | Direct     | MIPI_CPHY0_RX_TRIO1 Input      |
+---------------------------+------------+--------------------------------+
| MIPI_CPHY0_RX_TRIO2_A/B/C | Direct     | MIPI_CPHY0_RX_TRIO2 Input      |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY1_RX_D0P/D0N     | Direct     | MIPI_DPHY1_RX Data Lane0 Input |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY1_RX_D1P/D1N     | Direct     | MIPI_DPHY1_RX Data Lane1 Input |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY1_RX_D2P/D2N     | Direct     | MIPI_DPHY1_RX Data Lane2 Input |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY1_RX_D3P/D3N     | Direct     | MIPI_DPHY1_RX Data Lane3 Input |
+---------------------------+------------+--------------------------------+
| MIPI_DPHY1_RX_CLKP/CLKN   | Direct     | MIPI_DPHY1_RX Clock Input      |
+---------------------------+------------+--------------------------------+
| MIPI_CPHY1_RX_TRIO0_A/B/C | Direct     | MIPI_CPHY1_RX_TRIO0 Input      |
+---------------------------+------------+--------------------------------+
| MIPI_CPHY1_RX_TRIO1_A/B/C | Direct     | MIPI_CPHY1_RX_TRIO1 Input      |
+---------------------------+------------+--------------------------------+
| MIPI_CPHY1_RX_TRIO2_A/B/C | Direct     | MIPI_CPHY1_RX_TRIO2 Input      |
+---------------------------+------------+--------------------------------+

MIPI DPHY CSI RX Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^

|  RK3588 has two MIPI DPHY CSI RXs, both supporting MIPI V1.2, with a maximum data rate of 2.5Gbps per channel.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/MIPI-DPHY-CSI-RX电路-1.png
   :alt: MIPI-DPHY-CSI-RX Circuit-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/MIPI-DPHY-CSI-RX电路-2.png
   :alt: MIPI-DPHY-CSI-RX Circuit-2.png
   :width: 80%

|  MIPI DPHY CSI0 RX interface mode support:

 | Supports x4Lane mode, MIPI_CSI0_D[3:0] data references MIPI_CSI0_CLK0;
 | Supports x2Lane+x2Lane mode: MIPI0_CSI_D[1:0] data references MIPI_CSI0_CLK0; MIPI_CSI0_D[3:2] data references MIPI_CSI1_CLK1.

|  MIPI CSI1 RX interface mode support:

 | Supports x4Lane mode, MIPI_CSI1_D[3:0] data references MIPI_CSI1_CLK0;
 | Supports x2Lane+x2Lane mode: MIPI1_CSI_D[1:0] data references MIPI_CSI1_CLK0; MIPI_CSI1_D[3:2] data references MIPI_CSI1_CLK1.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/MIPI-DPHY-CSI-RX电路-3.png
   :alt: MIPI-DPHY-CSI-RX Circuit-3.png
   :width: 80%

|  The Camera's DVDD power supply can be 1.2V/1.5V/1.8V, etc. Please provide the accurate power supply according to the Camera's specification. Some Cameras have high DVDD current; if it exceeds 100mA, it is recommended to use a DCDC power supply. If the Camera has AF function, VCC2V8_AF needs a separate power supply. The development board generates it from 3.3V via an LDO power chip.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/MIPI-DPHY-CSI-RX电路-4.png
   :alt: MIPI-DPHY-CSI-RX Circuit-4.png
   :width: 80%

|  The Camera's PWDN signal must be controlled by GPIO, and the GPIO level must match the Camera IO level. The Camera's Reset signal is recommended to be controlled by GPIO, and the GPIO level must match the Camera IO level.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/MIPI-DPHY-CSI-RX电路-5.png
   :alt: MIPI-DPHY-CSI-RX Circuit-5.png
   :width: 80%

|  The recommended matching design for MIPI DPHY CSI0/1 RX interfaces is shown in the table below:

+-----------------------+------------+----------------------------+
| Signal                | Connection | Description                |
+-----------------------+------------+----------------------------+
| MIPI_CSI0_D0P/D0N     | Direct     | MIPI CSI0 Data Lane0 Input |
+-----------------------+------------+----------------------------+
| MIPI_CSI0_D1P/D1N     | Direct     | MIPI CSI0 Data Lane1 Input |
+-----------------------+------------+----------------------------+
| MIPI_CSI0_D2P/D2N     | Direct     | MIPI CSI0 Data Lane2 Input |
+-----------------------+------------+----------------------------+
| MIPI_CSI0_D3P/D3N     | Direct     | MIPI CSI0 Data Lane3 Input |
+-----------------------+------------+----------------------------+
| MIPI_CSI0_CLK0P/CLK0N | Direct     | MIPI CSI0 Clock 0 Input    |
+-----------------------+------------+----------------------------+
| MIPI_CSI0_CLK1P/CLK1N | Direct     | MIPI CSI0 Clock 1 Input    |
+-----------------------+------------+----------------------------+
| MIPI_CSI1_D0P/D0N     | Direct     | MIPI CSI1 Data Lane0 Input |
+-----------------------+------------+----------------------------+
| MIPI_CSI1_D1P/D1N     | Direct     | MIPI CSI1 Data Lane1 Input |
+-----------------------+------------+----------------------------+
| MIPI_CSI1_D2P/D2N     | Direct     | MIPI CSI1 Data Lane2 Input |
+-----------------------+------------+----------------------------+
| MIPI_CSI1_D3P/D3N     | Direct     | MIPI CSI1 Data Lane3 Input |
+-----------------------+------------+----------------------------+
| MIPI_CSI1_CLK0P/CLK0N | Direct     | MIPI CSI1 Clock 0 Input    |
+-----------------------+------------+----------------------------+
| MIPI_CSI1_CLK1P/CLK1N | Direct     | MIPI CSI1 Clock 1 Input    |
+-----------------------+------------+----------------------------+

HDMI 2.0 RX Circuit
^^^^^^^^^^^^^^^^^^^^^

|  The RK3588 chip supports HDMI2.0 RX, backward compatible with HDMI1.4b; supports RGB/YUV444/YUV422/YUV420 formats; supports up to 4K@60Hz input.
|  The HDMI RX TMDS signals are shown below. 2.2ohm resistors must be reserved near the HDMI RX connector and must not be deleted to enhance ESD and surge immunity.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-RX电路-1.png
   :alt: HDMI-2.0-RX Circuit-1.png
   :width: 80%

|  HDMI_RX_CEC is the HDMI controller CEC function multiplexed onto a normal GPIO. The level follows the voltage of its power domain. If the power domain supply voltage changes, the power for the pull-up resistor in the peripheral circuit must also be adjusted accordingly.
|  HDMI_RX_CEC is multiplexed at three locations: one on an IO in the VCCIO6 power domain, one on an IO in the VCCIO5 power domain, and one on an IO in the VCCIO4 power domain. The development board uses GPIO3_D1_d in the VCCIO5 power domain.
|  The CEC protocol specifies a 3.3V level. If the selected IO belongs to a 3.3V IO, then according to the protocol requirements, a 3.3V voltage must be applied to the CEC pin through a 56K resistor, with leakage current not exceeding 1.8uA. The MOS transistor cannot be omitted.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-RX电路-2.png
   :alt: HDMI-2.0-RX Circuit-2.png
   :width: 80%

|  When the RK3588 IO Domain is not powered, if there is voltage on the IO, leakage will occur. For example, if the RK3588 is powered off but the HDMI cable is still connected to the Sink end (TV or monitor), the CEC at the Sink end is powered and will leak through the HDMI cable to the RK3588 IO, causing CEC leakage to exceed 1.8uA. Therefore, an external isolation circuit is needed. The value of R102 must not be changed arbitrarily; 56Kohm must be used. Q9 is selected as 2SK3018 by default. If another model is to be used, the junction capacitance must be comparable. If the junction capacitance is too large, it will not only affect operation but also fail certification.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-RX电路-3.png
   :alt: HDMI-2.0-RX Circuit-3.png
   :width: 80%

|  HDMI_RX DDC_SCL/DDC_SDA are the I2C/DDC bus of the HDMI RX controller, multiplexed onto IOs in the PMUIO2, VCCIO5, and VCCIO4 power domains. The level follows the voltage of its power domain. If the power domain supply voltage changes, the power for the pull-up resistor in the peripheral circuit must also be adjusted accordingly.
|  The DDC_SCL/DDC_SDA protocol specifies a 5V level. RK3588 IO does not support 5V levels, so a level conversion circuit must be added and must not be omitted. MOS transistor level conversion is used by default, with the MOS model defaulting to 2SK3018. If another model is to be used, the junction capacitance must be comparable. If the junction capacitance is too large, it will not only affect operation but also fail certification.
|  The pull-up resistor values are recommended to follow the default values and should not be changed arbitrarily.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-RX电路-4.png
   :alt: HDMI-2.0-RX Circuit-4.png
   :width: 80%

|  A 0.1uF decoupling capacitor is recommended for pin 18 of the HDMI connector, placed close to the HDMI connector pin during layout. To enhance ESD immunity, ESD devices must be reserved on the signals. The parasitic capacitance of the ESD for HDMI2.0 signals must not exceed 0.4pF. For other signals, the ESD parasitic capacitance is recommended to be no more than 1pF.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-RX电路-5.png
   :alt: HDMI-2.0-RX Circuit-5.png
   :width: 80%

|  The recommended matching design for the HDMI RX interface is shown in the table below:

+-----------------+--------------------------+----------------------------+
| Signal          | Connection               | Description                |
+-----------------+--------------------------+----------------------------+
| HDMI_RX_D0P/D0N | Series 2.2ohm R          | TMDS Data Lane0 Input      |
+-----------------+--------------------------+----------------------------+
| HDMI_RX_D1P/D1N | Series 2.2ohm R          | TMDS Data Lane1 Input      |
+-----------------+--------------------------+----------------------------+
| HDMI_RX_D2P/D2N | Series 2.2ohm R          | TMDS Data Lane2 Input      |
+-----------------+--------------------------+----------------------------+
| HDMI_RX_D3P/D3N | Series 2.2ohm R          | TMDS Clock Input           |
+-----------------+--------------------------+----------------------------+
| HDMI_RX_REXT    | 200 ohm 1% R to GND      | HDMI_RX PHY external ref R |
+-----------------+--------------------------+----------------------------+
| HDMI_RX_HPD     | MOS control circuit      | HDMI HPD Output            |
+-----------------+--------------------------+----------------------------+
| HDMI_RX_CEC     | MOS isolation conversion | HDMI CEC Signal            |
+-----------------+--------------------------+----------------------------+
| HDMI_RX_SCL     | MOS level conversion     | HDMI DDC Clock             |
+-----------------+--------------------------+----------------------------+
| HDMI_RX_SDA     | MOS level conversion     | HDMI DDC Data I/O          |
+-----------------+--------------------------+----------------------------+

HDMI 2.0 TX Circuit
^^^^^^^^^^^^^^^^^^^^^

|  RK3588 has two built-in HDMI TX Combo PHYs, supporting a maximum resolution of 8K@60Hz, and RGB/YUV444/YUV420 (Up to 10bit) formats.
|  HDMI2.1 TX Mode:
|  RK3588 supports HDMI2.1 and is backward compatible with HDMI2.0 and HDMI1.4. Since HDMI2.1 operates in FRL mode, when switching to HDMI2.0 and below modes, it operates in TMDS mode, thus an AC coupled voltage mode driver is used.
|  As shown below, the AC coupling capacitor value is 220nF and must not be changed arbitrarily. AC coupling capacitors are recommended to use 0201 packages for lower ESR and ESL, which also reduces impedance changes on the line.
|  Using HDMI TX0 as an example, HDMI TX1 is the same as HDMI TX0.
|  When operating in HDMI2.1 mode, HDMI0_TX_ON_H is configured low, Q16, Q17, Q18, Q19 are not conducting.
|  When operating in HDMI2.0 and below modes, HDMI0_TX_ON_H is configured high, Q16, Q17, Q18, Q19 conduct. The 499ohm resistor to ground and the Sink's 50ohm pull-up resistor form a DC bias of about 3V.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-TX电路-1.png
   :alt: HDMI-2.0-TX Circuit-1.png
   :width: 80%

|  Note: 1: If only HDMI2.0 and below modes are supported, Q16, Q17, Q18, Q19 cannot be omitted. It is necessary to ensure that the transistors do not conduct when the machine is not powered on, because the HDMI CTS Test ID 7-3 TMDS Voff test requires that when the DUT is not powered, the Voff voltage must be within AVcc+-10mV, otherwise this test item cannot be passed.
|  2: The Coss of the control MOS transistor must not be too large, otherwise it will affect signal quality. It is recommended to use the reference model or a model with a comparable Coss value.
|  Supports ARC/eARC through HDMI0_TX_SBDP/HDMI0_TX_SBDN signals parsed by the RK3588 internally to extract audio data.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-TX电路-2.png
   :alt: HDMI-2.0-TX Circuit-2.png
   :width: 80%

|  HDMI_TX0_HPD is the HDMI TX controller function multiplexed onto a normal GPIO. The level follows the voltage of its power domain. If the power domain supply voltage changes, the power for the pull-up resistor in the peripheral circuit must also be adjusted accordingly.
|  HDMI_TX0/1_HPD are multiplexed in two different power domains: one on an IO in the VCCIO4 power domain and one on an IO in the VCCIO5 power domain. The development board uses GPIO1_A5/6_d in the VCCIO4 power domain.
|  HDMI_TX0_CEC is the HDMI controller CEC function multiplexed onto a normal GPIO. The level follows the voltage of its power domain. If the power domain supply voltage changes, the power for the pull-up resistor in the peripheral circuit must also be adjusted accordingly.
|  HDMI_TX0_CEC is multiplexed at two locations: one on an IO in the VCCIO6 power domain and one on an IO in the PMUIO2 power domain. The development board uses GPIO4_C1_d in the VCCIO6 power domain.
|  HDMI_TX1_CEC is multiplexed at three locations: one on an IO in the VCCIO3 power domain, one on an IO in the PMUIO2 power domain, and one on an IO in the VCCIO5 power domain. The development board uses GPIO3_C4_u in the VCCIO5 power domain.
|  The CEC protocol specifies a 3.3V level, but the protocol requires applying 3.3V to the CEC pin through a 27K resistor, with leakage current not exceeding 1.8uA.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-TX电路-3.png
   :alt: HDMI-2.0-TX Circuit-3.png
   :width: 80%

|  When the RK3588 IO Domain is not powered, if there is voltage on the IO, leakage will occur. For example, if the RK3588 is powered off but the HDMI cable is still connected to the Sink end (TV or monitor), the CEC at the Sink end is powered and will leak through the HDMI cable to the RK3588 IO, causing CEC leakage to exceed 1.8uA. Therefore, an external isolation circuit is needed. The value of R124 must not be changed arbitrarily; 27Kohm must be used. Q15 is selected as 2SK3018 by default. If another model is to be used, the junction capacitance must be comparable. If the junction capacitance is too large, it will not only affect operation but also fail certification.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-TX电路-4.png
   :alt: HDMI-2.0-TX Circuit-4.png
   :width: 80%

|  HDMI_TX DDC_SCL/DDC_SDA are the I2C/DDC bus of the HDMI TX0/1 controller, multiplexed onto IOs in the VCCIO3, VCCIO5, and VCCIO4 power domains. The level follows the voltage of its power domain. If the power domain supply voltage changes, the power for the pull-up resistor in the peripheral circuit must also be adjusted accordingly.
|  The DDC_SCL/DDC_SDA protocol specifies a 5V level. RK3588 IO does not support 5V levels, so a level conversion circuit must be added and must not be omitted. MOS transistor level conversion is used by default, with the MOS model defaulting to 2SK3018. If another model is to be used, the junction capacitance must be comparable. If the junction capacitance is too large, it will not only affect operation but also fail certification.
|  The pull-up resistor values are recommended to follow the default values and should not be changed arbitrarily.
|  The diode D15 must not be omitted; it is used to prevent leakage from the Sink end to VCC_5V0.
|  A 1K resistor is connected in series between the MOS gate for SDA signal level conversion and the power supply, and a 100pF capacitor is connected between the MOS gate and source to improve timing. These must not be deleted.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-TX电路-5.png
   :alt: HDMI-2.0-TX Circuit-5.png
   :width: 80%

|  The voltage on pin 18 of the HDMI connector must be guaranteed to be between 4.8-5.3V. A 1uF decoupling capacitor must be placed on this pin and must not be omitted. Place it close to the HDMI connector pin during layout.
|  To enhance ESD immunity, ESD devices must be reserved on the signals. The parasitic capacitance of the ESD for HDMI2.1 signals must not exceed 0.2pF. For other signals, the ESD parasitic capacitance is recommended to be no more than 1pF.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/HDMI-2.0-TX电路-6.png
   :alt: HDMI-2.0-TX Circuit-6.png
   :width: 80%

|  The recommended matching design for the HDMI TX interface is shown in the table below:

+--------------------+----------------------------------------+------------------------------------+
| Signal             | Connection                             | Description                        |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX0_D0P/D0N   | Series 220nF C (0201), 499ohm R to GND | RFL Mode Lane0/TMDS Data Lane0 Out |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX0_D1P/D1N   | Series 220nF C (0201), 499ohm R to GND | RFL Mode Lane1/TMDS Data Lane1 Out |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX0_D2P/D2N   | Series 220nF C (0201), 499ohm R to GND | RFL Mode Lane2/TMDS Data Lane2 Out |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX0_D3P/D3N   | Series 220nF C (0201), 499ohm R to GND | RFL Mode Lane3/TMDS Clock Out      |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX0_SBDP/SBDN | Series 1uF C (0201)                    | ARC/eARC Channel                   |
+--------------------+----------------------------------------+------------------------------------+
| HDMI/EDP_TX0_REXT  | 8200 ohm 1% R to GND                   | HDMI/EDP_TX0 PHY external ref R    |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX0_HPD       | Transistor conversion                  | HDMI Insertion Detection           |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX0_CEC       | MOS isolation conversion               | HDMI CEC Signal                    |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX0_SCL       | MOS level conversion                   | HDMI DDC Clock                     |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX0_SDA       | MOS level conversion                   | HDMI DDC Data I/O                  |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX1_D0P/D0N   | Series 220nF C (0201), 499ohm R to GND | RFL Mode Lane0/TMDS Data Lane0 Out |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX1_D1P/D1N   | Series 220nF C (0201), 499ohm R to GND | RFL Mode Lane1/TMDS Data Lane1 Out |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX1_D2P/D2N   | Series 220nF C (0201), 499ohm R to GND | RFL Mode Lane2/TMDS Data Lane2 Out |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX1_D3P/D3N   | Series 220nF C (0201), 499ohm R to GND | RFL Mode Lane3/TMDS Clock Out      |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX1_SBDP/SBDN | Series 1uF C (0201)                    | ARC/eARC Channel                   |
+--------------------+----------------------------------------+------------------------------------+
| HDMI/EDP_TX1_REXT  | 8200 ohm 1% R to GND                   | HDMI/EDP_TX0 PHY external ref R    |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX1_HPD       | Transistor conversion                  | HDMI Insertion Detection           |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX1_CEC       | MOS isolation conversion               | HDMI CEC Signal                    |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX1_SCL       | MOS level conversion                   | HDMI DDC Clock                     |
+--------------------+----------------------------------------+------------------------------------+
| HDMI_TX1_SDA       | MOS level conversion                   | HDMI DDC Data I/O                  |
+--------------------+----------------------------------------+------------------------------------+

MIPI Display Interface Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  The MIPI_DSI of the RK3588 processor supports a maximum resolution of 4K@60fps and up to 4 data lanes. It is routed out from the development board via 30-pin FPCs with a pitch of 0.5mm (J10, J11). The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-MIPI显示屏接口电路.png
   :alt: Design Recommendation-MIPI Display Interface Circuit.png
   :width: 80%

|  The voltage on pins 28-30 of the MIPI connector must be guaranteed to be between 4.8-5.3V. 1uF and 0.1uF decoupling capacitors must be placed on these pins and must not be omitted. Place them close to the MIPI connector pins during layout. To suppress electromagnetic radiation, common mode chokes can be reserved for the MIPI data and clock signals.

LCM-eDP Circuit
^^^^^^^^^^^^^^^^^

|  The EDP interface of the RK3588 processor development board supports a maximum resolution of 4K@60Hz and RGB/YUV422 (Up to 10bit) formats. It is routed out from the development board via a 30-pin FPC with a pitch of 0.5mm (J12). The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-LCM-eDP电路-1.png
   :alt: Design Recommendation-LCM-eDP Circuit-1.png
   :width: 80%

eDP_TX_AUXP/AUXN require 100nF AC coupling capacitors placed near the interface end. AUXP requires a 100K resistor to ground reserved, and AUXN requires a 100K pull-up resistor to 3.3V reserved.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-LCM-eDP电路-2.png
   :alt: Design Recommendation-LCM-eDP Circuit-2.png
   :width: 80%

WiFi Bluetooth Circuit
^^^^^^^^^^^^^^^^^^^^^^^^

|  The development board features an onboard Wifi & Bluetooth combo module, model RTL8723. WIFI and Bluetooth share a set of USB2.0 signals. Common mode chokes are connected in series on the USB2.0 DP/DM signals to suppress electromagnetic radiation.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-WiFi蓝牙电路.png
   :alt: Design Recommendation-WiFi Bluetooth Circuit.png
   :width: 80%

SD Card Circuit
^^^^^^^^^^^^^^^^^

|  The development board provides a push-push TF card socket, using the RK3588 SDMMC0 interface and supporting System Boot. The circuit diagram is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-SD卡电路.png
   :alt: Design Recommendation-SD Card Circuit.png
   :width: 80%

|  When using an SD card, note the following:

1. The VDD pin of the SD card is powered at 3.3V. The decoupling capacitor must not be omitted and should be placed close to the card socket during layout.
2. ESD devices can be placed at the SD card location for SDMMC0_D[3:0], SDMMC0_CMD, SDMMC0_CLK, and SDMMC0_DET signals. If SD3.0 mode support is needed, the ESD device's junction capacitance must be less than 1pF. If only SD2.0 mode support is needed, the ESD device's junction capacitance can be relaxed to 9pF.

Gigabit Ethernet Circuit
^^^^^^^^^^^^^^^^^^^^^^^^^^

|  The baseboard provides two Gigabit Ethernet interfaces, using the RGMII interface to connect to the PHY chip RTL8211F. The IO power supply is 1.8V. They are routed out via RJ45 sockets, model HR911130C, which have built-in isolation transformers. The RTL8211F chip supports 10/100/1000Mbps auto-negotiation and automatic MDI/MDIX crossover during auto-negotiation.
|  Ethernet schematic design needs attention:

1. The Reset signal of the Ethernet PHY must be controlled by GPIO. The GPIO level must match the PHY IO level. A 100nF capacitor must be added near the PHY pin to enhance ESD immunity. Note that the reset pin of RTL8211F/FI only supports 3.3V level.
2. The INTB/PMEB of RTL8211F/FI is open-drain output and must have an external pull-up resistor.
3. When the PHY uses an external crystal, the crystal capacitor should be selected according to the load capacitance value of the actual crystal used, controlling the frequency deviation within +/-20ppm.
4. The external resistor on the RSET pin of RTL8211F/FI is 2.49Kohm, 1% accuracy, and must not be changed arbitrarily.
5. MDIO must have external pull-up resistors, recommended 1.5-1.8Kohm. The pull-up power must be consistent with the power supply.
6. Must confirm whether the RJ45 package and schematic are consistent. RJ45 has Tab down and Tab up types, and the signal order is opposite. If using RTL8211F/FI, it is recommended to use Tab down, as the MDI order is sequential.
7. The hardware configuration for PHY initialization must match the actual requirements.

|  See the figure below, using the GMAC0 schematic as an example. The GMAC1 schematic requires the same treatment.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-千兆网电路-1.png
   :alt: Design Recommendation-Gigabit Ethernet Circuit-1.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-千兆网电路-2.png
   :alt: Design Recommendation-Gigabit Ethernet Circuit-2.png
   :width: 80%

Audio Circuit
^^^^^^^^^^^^^^^

|  The audio circuit uses ES8388 to achieve headphone output, dual-channel speaker output, and one differential audio input function. ES8388 is a high-performance, low-power, low-cost audio codec. It has two ADCs, 2-channel DACs, microphone amplifier, headphone amplifier, digital effects, analog mixing, and gain functions.
|  L/ROUT1 are the left and right channel interfaces for the headphone jack. HP_DET_L is the headphone detection interface.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-音频电路-1.png
   :alt: Design Recommendation-Audio Circuit-1.png
   :width: 80%

|  Additionally, ESD devices can be added to ROUT1 and LOUT1 to enhance ESD immunity.
|  MIC2P/N are the mic input interfaces. The 0.1uF DC blocking capacitor for the MIC must not be omitted.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-音频电路-2.png
   :alt: Design Recommendation-Audio Circuit-2.png
   :width: 80%

|  ROUT2 and LOUT2 are the speaker interfaces. If higher power or better output sound quality is needed, it is recommended to add an external analog amplifier or digital amplifier.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-音频电路-3.png
   :alt: Design Recommendation-Audio Circuit-3.png
   :width: 80%

SATA3.0 Circuit
^^^^^^^^^^^^^^^^^

|  The 10nF AC coupling capacitors are connected in series on the TXP/N and RXP/N differential signals of the SATA interface. AC coupling capacitors are recommended to use 0201 packages for lower ESR and ESL, which also reduces impedance changes on the line.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/SATA3.0电路-1.png
   :alt: SATA3.0 Circuit-1.png
   :width: 80%

|  The development board has an onboard SATA power connector. The current design needs to be estimated based on the actual number of SATA devices. For high power, it is recommended to use more than 2 power supplies.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/SATA3.0电路-2.png
   :alt: SATA3.0 Circuit-2.png
   :width: 80%

PCIE3.0 Circuit
^^^^^^^^^^^^^^^^^

|  The development board features an onboard M.2 M-Key interface on the backside for connecting SSDs. The required power is supplied separately using SY8113B/SM8103ADC chips.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-PCIE3.0电路-1.png
   :alt: Design Recommendation-PCIE3.0 Circuit-1.png
   :width: 80%

|  The 220nF AC coupling capacitors are connected in series on the TX0P/N and TX1P/N differential signals of the PCIe3.0 interface. AC coupling capacitors are recommended to use 0201 packages for lower ESR and ESL, which also reduces impedance changes on the line.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-PCIE3.0电路-2.png
   :alt: Design Recommendation-PCIE3.0 Circuit-2.png
   :width: 80%

|  PCIE30_CLKREQn and PCIE30_WAKEn must use functional pins and cannot be replaced by GPIO. Specifically: when selecting, both must be selected from the same group _M0 or _M1 or _M2; cannot mix _M0 and _M1.
|  PCIE30_PERSTn can be a functional pin or replaced by GPIO. If using a functional pin, it must be in the same _Mx group as PCIE30_CLKREQn and PCIE30_WAKEn.
|  PCIE30_REFCLKP/N only supports input and requires a clock input that meets PCIe3.0 requirements with HCSL level. The development board design uses the PI6C557-03BLE chip, which outputs two clocks: one to the RK3588 chip and one to the M.2 connector.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-PCIE3.0电路-3.png
   :alt: Design Recommendation-PCIE3.0 Circuit-3.png
   :width: 80%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-PCIE3.0电路-4.png
   :alt: Design Recommendation-PCIE3.0 Circuit-4.png
   :width: 80%

Button Circuit
^^^^^^^^^^^^^^^^

|  The development board features onboard PWRON (power on), RESET (reset), VOL+ (volume up), VOL- (volume down), BACK (back), and HOME (home) buttons. Among them, the PWRON and RESET buttons are connected to the core board power management chip RK806-1, while the others use the RK3588's SARADC_VIN1 signal.
|  The RK806-1 chip's RK809_PWRON and RESETn signals are used as input sampling ports to detect whether the PWRON button and RESET button are pressed by checking the level status on these signals.
|  For button sampling, ESD protection is needed near the button. A series 100ohm resistor on the detection signal line enhances ESD and surge immunity.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-按键电路-1.png
   :alt: Design Recommendation-Button Circuit-1.png
   :width: 80%

|  The RK3588 chip's SARADC_VIN1 is defaults to being the key value input sampling port and is multiplexed as the Recovery mode button (cannot be modified). The SARADC_VIN1 signal is already pulled up to 1.8V through a 10Kohm resistor on the core board. When there is no button action and the system has firmware burned, it directly enters the system upon power-up. If the Recovery mode button is pressed during system startup, i.e., SARADC_VIN1 is held low (0V), the RK3588 enters Loader burning mode. When the PC recognizes the USB device, release the button to restore SARADC_VIN1 to high level (1.8V), and firmware burning can proceed. Therefore, if the product has no buttons, SARADC_VIN1 is floating, which may cause an indeterminate state and affect booting. So the 10Kohm pull-up resistor for SARADC_VIN1 on the core board must be retained and not omitted to ensure default normal boot judgment. Additionally, for convenience in development, it is recommended to reserve buttons or test points.
|  On RK3588, the SARADC sampling range is 0-1.8V with 10-bit precision. The button array uses a parallel type. Multiple key inputs can be achieved by adding/removing buttons and adjusting the voltage divider resistor ratio to meet customer product needs. It is recommended in the design that the difference between any two key values must be greater than +/-35, meaning the center voltage difference must be greater than 123mV.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-按键电路-2.png
   :alt: Design Recommendation-Button Circuit-2.png
   :width: 80%

|  The button PCB is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-按键电路-3.png
   :alt: Design Recommendation-Button Circuit-3.png
   :width: 80%

Debug UART Circuit
^^^^^^^^^^^^^^^^^^^

|  The development board reserves a TTL-level debug UART (J22) for connecting a serial console, as shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-调试串口电路.png
   :alt: Design Recommendation-Debug UART Circuit.png
   :width: 80%

|  The RK3588 UART Debug defaults to UART2_RX_M0/UART2_TX_M0. To prevent damage to the chip pins during development, 2.54mm pin headers are reserved.

485 Circuit
^^^^^^^^^^^^^

|  The development board features an onboard RS485 interface. The schematic is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-485电路.png
   :alt: Design Recommendation-485 Circuit.png
   :width: 80%

|  The RS485 chip used on the development board is 3.3V, and the UART IO level is also 3.3V. If the replaced RS485 chip is 5V powered, level conversion is needed on the UART side; otherwise, leakage will occur. Do not directly replace it with a 5V powered RS485 chip.

CAN Circuit
^^^^^^^^^^^^^

|  The development board features an onboard CAN interface. When using the CAN interface,need to confirm the compatibility of external devices. The schematic is shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-CAN电路.png
   :alt: Design Recommendation-CAN Circuit.png
   :width: 80%

FAN Circuit
^^^^^^^^^^^^^

|  The development board features an onboard FAN interface with an operating voltage of DC12V. The PWM_FAN signal can be used for fan speed control. As shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-FAN电路.png
   :alt: Design Recommendation-FAN Circuit.png
   :width: 80%

PCB Design Recommendations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PCB Stackup Design
^^^^^^^^^^^^^^^^^^^^

|  To reduce reflection during high-speed signal transmission, impedance matching must be maintained at the signal source, receiver, and transmission line. The specific impedance of a single-ended signal line depends on its trace width and its relative position to the reference plane. The trace width/spacing for差分对 (differential pairs) with specific impedance requirements depends on the chosen PCB stackup structure. Since the minimum trace width and spacing are determined by the PCB type and cost requirements, the chosen PCB stackup must be able to achieve all impedance requirements on the board, including inner and outer layers, single-ended and differential lines, etc.
|  Layer definition design principles:

1. The layer adjacent to the main chip should be a ground plane, providing a reference plane for routing on the component side.
2. All signal layers should be adjacent to a ground plane as much as possible.
3. Avoid direct adjacency between two signal layers.
4. Main power supplies should be adjacent to their corresponding ground as much as possible.
5. In principle, a symmetrical structure design should be adopted. Symmetry includes: dielectric thickness and type, copper thickness, and pattern distribution type (large copper layer, routing layer).

|  Recommended PCB layer definition scheme: When setting the specific PCB layers, be flexible with the above principles. Determine the layer arrangement according to actual needs, and avoid rigid application. If there are adjacent routing layers, increase the spacing between them to reduce crosstalk. For跨分割 (cross-segmentation) situations, ensure that critical signals have a relatively complete reference ground plane or provide necessary bridging measures.

Interface PCB Design Recommendations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Power Circuit PCB Design
""""""""""""""""""""""""""

|  Place the input capacitor Cin and output capacitor Cout between the Vin pin, Vout pin, and the GND of the DC/DC converter. Minimize the loop area between Vin, Vout, and the DC/DC's GND. This can reduce power ripple amplitude and greatly improve chip reliability.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK360/设计建议-电源电路PCB设计.png
   :alt: Design Recommendation-Power Circuit PCB Design.png
   :width: 80%

|  Add multiple vias for the input capacitor Cin, output capacitor Cout, and the GND of the DC/DC converter.建议 4 个以上的 0503 过孔 (Recommend more than 4 vias of 0503 size). If the Vin and Vout power supplies change layers, it is also recommended to add more vias,建议 4 个以上的 0503 过孔 (recommend more than 4 vias of 0503 size) (related to current). The inductor should be as close as possible to the DC/DC converter, and the traces should be as thick and short as possible. The ground of the FB terminal resistor should be kept away from interference sources.
| 禁止覆铜 (Copper pour is prohibited) on the power pins of board-to-board connectors. All power pins should connect to the outside through traces. The trace width should not exceed the pin width to prevent solder bridging or虚焊 (cold solder joints) after manufacturing when the pad becomes larger.

USB2.0 Circuit PCB Design
"""""""""""""""""""""""""""

|  Table 3-1 USB2.0 Signal Impedance and Routing Requirements

+---------------------+------------------------------+
| Parameter           | Requirement                  |
+---------------------+------------------------------+
| Trace Impedance     | Differential 90ohm ±10%      |
+---------------------+------------------------------+
| Max Intra-Pair Skew | Less than 20mil              |
+---------------------+------------------------------+
| Trace Length        | Less than 6 inches           |
+---------------------+------------------------------+
| Allowed Via Count   | Recommended <=4, Must not >6 |
+---------------------+------------------------------+

|  When USB differential signals need to change layers, ensure the number of vias on the trace is less than 4, must not exceed 6. Place symmetrical ground stitching vias near the signal vias. The center distance between the ground stitching via and the signal via must not exceed 30mil. The USB differential pair should preferably have a complete ground plane as its reference layer. If crossing different planes is unavoidable, the entire route must be handled with ground pouring. The ground pour trace should have ground vias within every 300mil interval.

USB3.0 Circuit PCB Design
""""""""""""""""""""""""""""

|  USB3.0 Signal Impedance and Routing Requirements

+---------------------------------------+---------------------------------------------+
| Parameter                             | Requirement                                 |
+---------------------------------------+---------------------------------------------+
| Differential Trace Impedance          | 90Ω±10%                                     |
+---------------------------------------+---------------------------------------------+
| SSTXP/SSTXN Intra-Pair Skew           | < 12mil                                     |
+---------------------------------------+---------------------------------------------+
| SSRXP/SSRXN Intra-Pair Skew           | < 12mil                                     |
+---------------------------------------+---------------------------------------------+
| SSTXP/N and SSRXP/N Inter-Pair Skew   | < 6000mil Recommended <=4, Must not >6      |
+---------------------------------------+---------------------------------------------+
| Total PCB Trace Length                | < 6000mil                                   |
+---------------------------------------+---------------------------------------------+
| Spacing between SSTX and SSRX signals | >=4 x trace width                           |
+---------------------------------------+---------------------------------------------+
| Spacing to other signals              | >=4 x trace width                           |
+---------------------------------------+---------------------------------------------+
| Layer Change Vias                     | < 2, need symmetrical ground stitching vias |
|                                       | near signal layer change vias               |
+---------------------------------------+---------------------------------------------+

|  SSTXP/N and SSRXP/N should preferably be routed on the TOP layer. If layer change is necessary, do not exceed 2 vias. Place symmetrical ground stitching vias near the signal vias, with a center distance not exceeding 30mil. Use arcs or obtuse angles for trace bends, not right angles or acute angles.
|  The reference layer for SSTXP/N and SSRXP/N signals needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path. Place AC coupling capacitors symmetrically and close to the USB connector. The area below the pads of the USB3 connector and the AC coupling capacitor pads must be voided of one layer to ensure impedance continuity. The void size should be no smaller than the package pad size.

Camera_MIPI_CSI Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  MIPI CSI RX Signal Impedance and Routing Requirements

+------------------------------+---------------------------------------------+
| Parameter                    | Requirement                                 |
+------------------------------+---------------------------------------------+
| Differential Trace Impedance | 100Ω±10%                                    |
+------------------------------+---------------------------------------------+
| Intra-Pair Skew              | < 12mil                                     |
+------------------------------+---------------------------------------------+
| Inter-Pair Skew              | < 36mil                                     |
+------------------------------+---------------------------------------------+
| Total PCB Trace Length       | < 6000mil                                   |
+------------------------------+---------------------------------------------+
| Spacing between MIPI signals | >=3 x trace width                           |
+------------------------------+---------------------------------------------+
| Spacing to other signals     | >=3 x trace width                           |
+------------------------------+---------------------------------------------+
| Layer Change Vias            | < 4, need symmetrical ground stitching vias |
|                              | near signal layer change vias               |
+------------------------------+---------------------------------------------+

|  Minimize layer change vias. If necessary, a maximum of 4 vias is allowed. Place symmetrical ground stitching vias near the signal vias, with a center distance not exceeding 30mil. The reference layer for MIPI CSI differential pairs needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path.

HDMI 2.0 Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  HDMI TX Signal Impedance and Routing Requirements

+-----------------------------------+---------------------------------------------+
| Parameter                         | Requirement                                 |
+-----------------------------------+---------------------------------------------+
| Differential Trace Impedance      | 100Ω±10%                                    |
+-----------------------------------+---------------------------------------------+
| Intra-Pair Skew                   | < 12mil                                     |
+-----------------------------------+---------------------------------------------+
| Clock-Data Skew                   | < 480mil                                    |
+-----------------------------------+---------------------------------------------+
| Total PCB Trace Length            | < 6000mil                                   |
+-----------------------------------+---------------------------------------------+
| Spacing between HDMI data signals | >=5 x trace width                           |
+-----------------------------------+---------------------------------------------+
| Spacing between data and clock    | >=5 x trace width                           |
+-----------------------------------+---------------------------------------------+
| Layer Change Vias                 | < 2, need symmetrical ground stitching vias |
|                                   | near signal layer change vias               |
+-----------------------------------+---------------------------------------------+

|  Route traces preferably on the TOP layer. If layer change is necessary, do not exceed 2 vias. Place symmetrical ground stitching vias near the signal vias, with a center distance not exceeding 30mil. Use arcs or obtuse angles for trace bends, not right angles or acute angles.
|  Route差分线整组并行走线 (the entire group of differential lines in parallel). Pour ground around the outermost periphery. The spacing between the ground pour and the signals should be no less than 4 times the trace width, and the ground pour trace should have ground vias within every 300mil interval.
|  The reference layer for all signals needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path.
|  The area below the pads of the HDMI connector and the TVS diode pads must be voided of one layer to ensure impedance continuity. The void size should be no smaller than the package pad size.
|  Place the HDMI TVS diodes as close as possible to the connector. The signal topology should be: HDMI Connector --> TVS --> CPU. During an ESD event, the ESD current must first pass through the TVS device for attenuation. There should be no stubs on the TVS device traces. The ground pin should have as many ground vias as possible, at least 2 vias of 0.4*0.2mm, to enhance ESD discharge capability.

MIPI Display Interface Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  MIPI DSI TX Signal Impedance and Routing Requirements

+------------------------------+---------------------------------------------+
| Parameter                    | Requirement                                 |
+------------------------------+---------------------------------------------+
| Differential Trace Impedance | 100Ω±10%                                    |
+------------------------------+---------------------------------------------+
| Intra-Pair Skew              | < 12mil                                     |
+------------------------------+---------------------------------------------+
| Inter-Pair Skew              | < 36mil                                     |
+------------------------------+---------------------------------------------+
| Total PCB Trace Length       | < 6000mil                                   |
+------------------------------+---------------------------------------------+
| Spacing between MIPI signals | >=3 x trace width                           |
+------------------------------+---------------------------------------------+
| Spacing to other signals     | >=3 x trace width                           |
+------------------------------+---------------------------------------------+
| Layer Change Vias            | < 4, need symmetrical ground stitching vias |
|                              | near signal layer change vias               |
+------------------------------+---------------------------------------------+

|  Minimize layer change vias for MIPI differential pairs. If necessary, do not exceed 4 vias. Place symmetrical ground stitching vias near the signal vias, with a center distance not exceeding 30mil. The reference layer for MIPI DSI differential pairs needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path.

LCM-eDP Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  eDP TX Signal Impedance and Routing Requirements

+------------------------------+---------------------------------------------+
| Parameter                    | Requirement                                 |
+------------------------------+---------------------------------------------+
| Differential Trace Impedance | 85Ω±10%                                     |
+------------------------------+---------------------------------------------+
| Intra-Pair Skew              | < 12mil                                     |
+------------------------------+---------------------------------------------+
| Total PCB Trace Length       | < 6000mil                                   |
+------------------------------+---------------------------------------------+
| Spacing between eDP signals  | >=4 x trace width                           |
+------------------------------+---------------------------------------------+
| Spacing to other signals     | >=4 x trace width                           |
+------------------------------+---------------------------------------------+
| Layer Change Vias            | < 4, need symmetrical ground stitching vias |
|                              | near signal layer change vias               |
+------------------------------+---------------------------------------------+

|  Minimize layer change vias. If necessary, a maximum of 4 vias is allowed. Place symmetrical ground stitching vias near the signal vias, with a center distance not exceeding 30mil. The reference layer for eDP_TX differential pairs needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path.

WiFi Bluetooth Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  Place the WIFI module appropriately, away from DDR, HDMI, USB, LCD circuits, speakers, and other easily interfering modules or connectors.
|  The longer the antenna routing, the greater the energy loss. Therefore, the antenna path should be as short as possible during design, with no branches, and尽量不换层 (try not to change layers). The antenna matching circuit must be close to the antenna connector. The antenna trace should be 50 ohms, ensure a complete reference ground, avoid impedance突变 (discontinuities), and no other signal lines or power supplies are allowed below it.

SD Card Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  SDMMC0 Signal Impedance and Routing Requirements

+-------------------------------------+----------------------------------------------------------+
| Parameter                           | Requirement                                              |
+-------------------------------------+----------------------------------------------------------+
| Single-Ended Impedance              | 50Ω±10%                                                  |
+-------------------------------------+----------------------------------------------------------+
| DATA/CMD and CLK Skew               | < 120mil                                                 |
+-------------------------------------+----------------------------------------------------------+
| Total PCB Trace Length              | When CLK <= 50MHz: < 6000mil                             |
+                                     +----------------------------------------------------------+
|                                     | When CLK > 50MHz: < 4000mil                              |
+-------------------------------------+----------------------------------------------------------+
| Spacing between SDMMC0 signals      | >=2 x trace width                                        |
+-------------------------------------+----------------------------------------------------------+
| Spacing to other signals            | >=3 x trace width                                        |
+-------------------------------------+----------------------------------------------------------+
| Layer Change Vias                   | < 4, need symmetrical ground stitching vias              |
|                                     | near signal layer change vias                            |
+-------------------------------------+----------------------------------------------------------+
| SDMMC0 CLK Trace Requirement        | Must have ground pour along entire route, with ground    |
|                                     | vias within every 300mil interval of the ground pour     |
+-------------------------------------+----------------------------------------------------------+

|  The reference layer for all SDMMC0 signals needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path. When this signal connects to an SD card, the power capacitor for the card socket must be placed at the card socket's power pin. During routing, the power must first pass through the capacitor and then to the card socket pin. The power trace for the card socket should be at least 40mil wide.
|  Place the TVS protection diode as close as possible to the card socket. The signal topology should be: Micro-SD Card Socket --> TVS --> CPU. During an ESD event, the ESD current must first pass through the TVS device for attenuation. There should be no stubs on the TVS device traces. The ground pin should have as many ground vias as possible, at least 2 vias of 0.4*0.2mm, to enhance ESD discharge capability.
|  Avoid routing under the Micro-SD card socket area to prevent coupling effects during ESD events.

Gigabit Ethernet Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  RGMII Signal Impedance and Routing Requirements

+-----------------------------------------+-------------------------------------------------------+
| Parameter                               | Requirement                                           |
+-----------------------------------------+-------------------------------------------------------+
| Single-Ended Impedance                  | 50Ω±10%                                               |
+-----------------------------------------+-------------------------------------------------------+
| TXD0,TXD1,TXD2,TXD3,TXEN and TXCLK Skew | < 120mil                                              |
+-----------------------------------------+-------------------------------------------------------+
| RXD0,RXD1,RXD2,RXD3,RXDV and RXCLK Skew | < 120mil                                              |
+-----------------------------------------+-------------------------------------------------------+
| Total PCB Trace Length                  | < 5000mil                                             |
+-----------------------------------------+-------------------------------------------------------+
| Spacing between PRGMII signals          | >=2 x trace width                                     |
+-----------------------------------------+-------------------------------------------------------+
| Spacing to other signals                | >=3 x trace width                                     |
+-----------------------------------------+-------------------------------------------------------+
| TXCLK and RXCLK Trace Requirement       | Must have ground pour along entire route, with ground |
|                                         | vias within every 300mil interval of the ground pour  |
+-----------------------------------------+-------------------------------------------------------+

|  The 22ohm series matching resistors for RXD0-RXD3, RXCLK, RXDV should be placed close to the PHY end. The trace length between the PHY pin and the resistor must be controlled within 400mil.
|  ETH0/1_REFCLKO_25M must have ground pour along its entire route, with ground vias within every 300mil interval of the ground pour.
|  The reference layer for all RGMII signals needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path.
|  Taking RTL8211F/FI as an example, points to note on the PHY side:
|  The crystal circuit layout needs priority consideration. It should be on the same layer as the chip and placed as close as possible to avoid vias. The crystal traces should be as short as possible, away from interference sources, and try to stay away from the board edge. The crystal and clock signals must have ground pour along their entire route. The ground pour should have GND vias at least every 100mil, and the adjacent layer's ground reference plane must be complete.
|  The RSET resistor must be close to the RTL8211F/FI pin. The trace length should not exceed 800mil and should be away from other interfering signals.
|  Must confirm whether the RJ45 package and schematic are consistent. RJ45 has Tab down and Tab up types, and the signal order is opposite. If using RTL8211F/FI, it is recommended to use Tab down, as the MDI order is sequential. The development board design uses RJ45 socket model HR911130A with a built-in isolation transformer. Alternatively, a separate RJ45 socket and network transformer can be used. In this case, the network transformer should be as close as possible to the RJ45 socket. The MDI trace length should not exceed 4.5 inches.
|  The differential signal impedance from the PHY to the network transformer should be 100Ω±10%. The intra-pair length deviation for MDI0+, MDI0-, MDI1+, MDI1-, MDI2+, MDI2-, MDI3+, MDI3- should be controlled within ±5mil. MDI differential pairs must strictly follow differential routing rules. For example, they must maintain the same length, same width, same layer, fixed spacing, and be as symmetrical as possible. The inter-pair delay for MDI differential pairs should be controlled within 800mil. The spacing between differential pairs should be no less than 3 times the trace width. The spacing to other signals should be no less than 4 times the trace width.
|  Minimize layer change vias for MDI signals. If necessary, a maximum of 2 vias is allowed. Place symmetrical ground stitching vias near the signal vias. The reference layer needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path.
|  For the MDI differential pairs on the high-voltage side of the network transformer, it is recommended to use wider traces, suggested 8mil. The trace for the 75ohm resistor should be at least 25mil wide.
|  The filter capacitor for the center tap of the network transformer must be close to the corresponding pin of the network transformer.
|  The RJ45 interface and the high-voltage side of the network transformer belong to the high-voltage area. Copper pour is prohibited. It is recommended to have a间隔至少 4mm 以上 (separation of at least 4mm) from the low-voltage area.
|  The decoupling capacitors for the PHY chip power supply should be placed as close as possible to the respective pins of the PHY chip. During routing, the trace should first go to the capacitor pad and then to the chip pin. The trace length between the pin and the capacitor should not exceed 100mil.
|  For the internal DCDC of RTL8211F/FI, the inductor must be close to the chip pin. The LX trace should be as short and thick as possible, with a width of at least 60mil and a length not exceeding 200mil. The output capacitor must be close to the inductor. During routing, the trace must first go to the output capacitor and then to the subsequent stage.
|  Pin21 and Pins 3,8,38 must use star routing. The trace width should be at least 30mil.
|  If the PHY IO uses 3.3V, the VCCIO_PHY and VCC3V3_PHY power traces must use star routing. The trace width should be at least 30mil.
|  The center pad of the PHY chip must be well grounded. Place at least a 5x5 array of vias of 0.5*0.3mm.

Audio Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^

|  Route SPKP/SPKN as differential lines and pour ground around the entire group. Trace width 20mil, keep traces as short as possible.
|  L/ROUT1 left and right channels should have separate ground pours. They are not differential lines and should not be close together, as this reduces the isolation between channels. Recommended trace width greater than 10mil.
|  When MIC is single-ended connected, MIC1/MIC2 should be routed separately with individual ground pours. When MIC is differentially connected, route MICP/MICN as differential pairs and pour ground around the entire group. MIC trace width is recommended to be at least 8mil.
|  Keep all audio signals away from LCD, DRAM, and other high-speed signal lines. prohibit routing audio signals on layers adjacent to high-speed signal lines. The adjacent layers of all audio signals must not be power planes or routing layers; they must be ground planes. prohibit placing vias for layer changes near high-speed signal lines. Do not route through inductor areas. Keep away from RF signals and components.
|  Place the TVS protection diode for the headphone jack/microphone as close as possible to the connector. The signal topology should be: Headphone Jack/Microphone --> TVS --> CPU. During an ESD event, the ESD current must first pass through the TVS device for attenuation. There should be no stubs on the TVS device traces. The ground pin should have as many ground vias as possible, at least 2 vias of 0.4*0.2mm, to enhance ESD discharge capability.

SATA3.0 Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  SATA3.0 Signal Impedance and Routing Requirements

+-----------------------------------+---------------------------------------------+
| Parameter                         | Requirement                                 |
+-----------------------------------+---------------------------------------------+
| Differential Trace Impedance      | 90Ω±10%                                     |
+-----------------------------------+---------------------------------------------+
| TXP/TXN Intra-Pair Skew           | < 12mil                                     |
+-----------------------------------+---------------------------------------------+
| RXP/RXN Intra-Pair Skew           | < 12mil                                     |
+-----------------------------------+---------------------------------------------+
| Total PCB Trace Length            | < 6000mil                                   |
+-----------------------------------+---------------------------------------------+
| Spacing between TX and RX signals | >=4 x trace width                           |
+-----------------------------------+---------------------------------------------+
| Spacing to other signals          | >=4 x trace width                           |
+-----------------------------------+---------------------------------------------+
| Layer Change Vias                 | < 2, need symmetrical ground stitching vias |
|                                   | near signal layer change vias               |
+-----------------------------------+---------------------------------------------+

|  TXP/N and RXP/N should preferably be routed on the TOP layer. If layer change is necessary, do not exceed 2 vias. Place symmetrical ground stitching vias near the signal vias, with a center distance not exceeding 30mil. Use arcs or obtuse angles for trace bends, not right angles or acute angles.
|  The reference layer for TXP/N and RXP/N signals needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path.
|  Place AC coupling capacitors symmetrically and close to the SATA connector. The area below the pads of the SATA connector and the AC coupling capacitor pads must be voided of one layer to ensure impedance continuity. The void size should be no smaller than the package pad size.

PCIE3.0 Circuit PCB Design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|  PCIe3.0 Signal Impedance and Routing Requirements

+------------------------------------+-------------------------------------------------------+
| Parameter                          | Requirement                                           |
+------------------------------------+-------------------------------------------------------+
| Data Differential Trace Impedance  | 85Ω±10%                                               |
+------------------------------------+-------------------------------------------------------+
| Clock Differential Trace Impedance | 100Ω±10%                                              |
+------------------------------------+-------------------------------------------------------+
| TXP/TXN Intra-Pair Skew            | < 12mil                                               |
+------------------------------------+-------------------------------------------------------+
| RXP/RXN Intra-Pair Skew            | < 12mil                                               |
+------------------------------------+-------------------------------------------------------+
| Total PCB Trace Length             | < 6000mil                                             |
+------------------------------------+-------------------------------------------------------+
| TX and RX Trace Length Skew        | < 6000mil                                             |
+------------------------------------+-------------------------------------------------------+
| Spacing between TX and RX signals  | >=5 x trace width                                     |
+------------------------------------+-------------------------------------------------------+
| Spacing to other signals           | >=5 x trace width                                     |
+------------------------------------+-------------------------------------------------------+
| REFCLKP/N Differential Trace Req.  | Must have ground pour along entire route, with ground |
|                                    | vias within every 300mil interval of the ground pour  |
+------------------------------------+-------------------------------------------------------+
| Layer Change Vias                  | < 2, need symmetrical ground stitching vias           |
|                                    | near signal layer change vias                         |
+------------------------------------+-------------------------------------------------------+

|  TXP/N, RXP/N, REFCLKP/N should preferably be routed on the TOP layer. If layer change is necessary, do not exceed 2 vias. Place symmetrical ground stitching vias near the signal vias, with a center distance not exceeding 30mil. Use arcs or obtuse angles for trace bends, not right angles or acute angles.
|  The reference layer for the signals needs to be a complete ground plane. Avoid situations where continuous vias block the signal return path.
|  Place AC coupling capacitors symmetrically and close to the PCIe Slot. The area below the pads of the Slot and the AC coupling capacitor pads must be voided of one layer to ensure impedance continuity. The void size should be no smaller than the package pad size.