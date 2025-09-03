Hardware Design Guide
=======================

Core Board Pin Schematic
--------------------------

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导1.png
   :alt: 硬件设计指导1.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导2.png
   :alt: 硬件设计指导2.png
   :width: 90%


Development Board 40Pin Pin Definition
----------------------------------------

40Pin Pin Schematic
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导3.png
   :alt: 硬件设计指导3.png
   :width: 90%

Base Board Schematic
----------------------

Power Management
~~~~~~~~~~~~~~~~~~

|  The base board power supply is a 5V DC power supply, inserted through the DC-005 socket, and J15 is the power socket. Then it is converted to the 5V input required by the core board through the bead CBW322513U121T. VCC_5V will be converted by SY8113B to 3.3V required by the base board and 3.3V required by the core board.
|  The schematic diagram of the power input is as follows. Among them, the 5V_DC signal is the power input of the DC interface, and the subsequent model is a self-recovery fuse 1812L300MR, which is used for overload protection with a trip current of 5A. The power supply system of the development board adopts the Rockchip RK809-5 chip, combined with peripheral BUCK and LDO circuits, to provide stable power for the RK3568 main control, DDR, eMMC and related functional peripheral devices.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导4.png
   :alt: 硬件设计指导4.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导5.png
   :alt: 硬件设计指导5.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导6.png
   :alt: 硬件设计指导6.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导7.png
   :alt: 硬件设计指导7.png
   :width: 90%

Button Circuit
~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导8.png
   :alt: 硬件设计指导8.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导9.png
   :alt: 硬件设计指导9.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导10.png
   :alt: 硬件设计指导10.png
   :width: 90%

|  The button PCB is as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导11.png
   :alt: 硬件设计指导11.png
   :width: 90%

TF Card Circuit
~~~~~~~~~~~~~~~~~

|  The TF card slot is located on the front of the main board, which is a self-ejecting TF card holder, supporting a maximum of 512G MicroSD card (TF card), and supporting system startup and storage. When the TF card is used as the system startup card, do not insert or remove the TF card at will during system operation.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导12.png
   :alt: 硬件设计指导12.png
   :width: 90%

SIM Circuit
~~~~~~~~~~~~~

|  The SIM card slot is located on the front of the main board, supporting a NanoSIM card. Its signal lines are directly connected to the MINI PCI-E interface. The SIM card supports China Mobile, China Unicom, and China Telecom, and needs to be matched with a 4G/5G module with a MINIPCI-E interface to realize 4G/5G communication functions.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导13.png
   :alt: 硬件设计指导13.png
   :width: 90%

Ethernet Circuit
~~~~~~~~~~~~~~~~~~

|  The development board has two RJ45 interfaces, each controlled by an independent PHY chip RTL8211F-CG, supporting 10/100/1000Mbps data transmission rate. The onboard RJ45 interface has two LED indicators, controlled by the PHY chip.
|  The schematic diagram of the ETH0 part is as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导14.png
   :alt: 硬件设计指导14.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导15.png
   :alt: 硬件设计指导15.png
   :width: 90%

|  The schematic diagram of the ETH1 part is as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导16.png
   :alt: 硬件设计指导16.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导17.png
   :alt: 硬件设计指导17.png
   :width: 90%

USB3.0/2.0 Circuit
~~~~~~~~~~~~~~~~~~~~

|  The RK3568 chip has a built-in USB3.0 OTG controller, two USB2.0 HOST controllers, and one USB3.0 HOST controller. USB3_OTG0_DP and USB3_OTG0_DM in one USB3.0 OTG are connected to the onboard Type-C OTG interface, with a rate of USB2.0, which can be used as a firmware download port for Emmc burning.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导18.png
   :alt: 硬件设计指导18.png
   :width: 90%

|  One USB3.0 HOST1 signal is connected to the onboard USB3.0 interface (with a blue inner core); the onboard USB3.0 interface is USB3.2 Gen1, equivalent to USB3.1 Gen1 and USB3.0, with a maximum data rate of 5Gbps, and backward compatible with USB2.0.
|  One USB2.0 HOST controller USB2_HOST2 signal is connected to the USB2.0 interface in the same group as the USB3.0 interface. The remaining USB2.0 HOST3 is connected to the onboard MINIPCI-E interface. The onboard USB2.0 interface supports three modes: high-speed (480Mbps), full-speed (12Mbps), and low-speed (1.5Mbps). The system will automatically select the appropriate mode according to the inserted device.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导19.png
   :alt: 硬件设计指导19.png
   :width: 90%

MIPI DSI Circuit
~~~~~~~~~~~~~~~~~~

|  The development board has two MIPI DSI interfaces, both located on the front of the main board, J5 and J6 respectively. The interface uses a 30Pin FPC socket, supporting video output and touch, and supporting dual MIPI screens to work simultaneously. The maximum resolution in single MIPI mode is 1920x1080@60fps.
|  The schematic diagram of the MIPI DSI interface is as shown:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导20.png
   :alt: 硬件设计指导20.png
   :width: 90%

HDMI TX Circuit
~~~~~~~~~~~~~~~~~

|  The RK3568 chip supports HDMI2.0 and is backward compatible with HDMI1.4, supporting a maximum of 4K@60Hz, and supporting video output and audio output. The development board is equipped with a vertical standard HDMI interface, which can be directly connected to a display with a standard HDMI interface through a dual-head HDMI cable.
|  The schematic diagram of the HDMI TX interface is as shown:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导21.png
   :alt: 硬件设计指导21.png
   :width: 90%

Audio Circuit
~~~~~~~~~~~~~~~

|  The 3.5mm headphone interface and SPK speaker interface are located next to the USB socket on the front of the main board. The audio input/output function is realized through the power chip PMIC RK809-5 of the core board.
|  The onboard 3.5mm headphone interface supports audio input/output, which is a 2-in-1 interface for headphone output + microphone input, and can be connected to wired headphones or to an amplifier through an AUX cable. The SPK interface specification is XH2.54-2P, which can be used to connect a small 8-ohm 1W speaker with a 2.54mm interface.
|  The peripheral circuits of the headphone interface and SPK interface are as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导22.png
   :alt: 硬件设计指导22.png
   :width: 90%

|  Among them, HPL_OUT is the headphone left channel audio output signal, HPR_OUT is the right channel audio output signal, HP_SNS is the headphone reference ground, MIC1_INP is the microphone negative signal input, MIC1_INN is the microphone positive signal input, SARADC_VIN2_HP_HOOK is the headphone wire control detection signal, SPKN_OUT is the speaker audio negative output, and SPKP_OUT is the speaker audio positive output.

MINIPCI-E Circuit
~~~~~~~~~~~~~~~~~~~

|  The M2-B interface is located on the back of the development board. The PCIe type of M2-B is PCIe2.0x1, supporting a maximum data rate of 5Gbps; it can be used with full-height or half-height WIFI network cards and 4G/5G modules.
|  When the M2-B interface is connected to a network card module, it uses the PCIe protocol; when the interface is connected to a 4G/5G module, although the physical connection interface is M2-B, it actually uses the USB protocol.
|  The M2-B circuit connection is as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导23.png
   :alt: 硬件设计指导23.png
   :width: 90%

Debug Serial Port Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The development base board has one onboard serial port, and CON4 is the USB TO UART0 debug serial port.
|  The development board base board converts UART0 to a Type-C connector (CON4) through the CH340T chip of WCH (Nanjing Qinheng Microelectronics Co., Ltd.) for use as a system debug serial port. CH340T is powered by 5V (network name: VDD_5V_VBUS) from the Type-C data cable.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导24.png
   :alt: 硬件设计指导24.png
   :width: 90%

|  Design considerations:

1. When designing the base board, it is recommended to adopt the RS0102YVS8 (U9) level conversion isolation scheme to prevent the RX end of the debug serial port from being charged in advance before the base board is powered on, which may inject current into the core board pins and cause the system to fail to start.
2. The levels of CPU pins UART2_RX_M0_DEBUG and UART2_TX_M0_DEBUG are both 3.3V. Do not directly connect to debug tools with 5V level interfaces, otherwise the CPU will be damaged.
3. Note that the USB signal needs to be 90ohm differential impedance matched.
4. ESD devices should be placed close to the Type-C connector, and the wiring should be connected to CH340T after passing through ESD.

FAN Circuit
~~~~~~~~~~~~~

|  The development board has a reserved 2Pin 2.54mm 5V fan power supply interface, which can control the conduction state of the 2SK3018 MOS tube through the TSADC_SHUT_M0 (GPIO0_A1_z) signal, thereby controlling the conduction of the BSS84 MOS tube to realize the on-off control of the fan.
|  The schematic diagram of the FAN fan driver is as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导25.png
   :alt: 硬件设计指导25.png
   :width: 90%

RTC Circuit
~~~~~~~~~~~~~

|  The development board has a reserved 2Pin 2.54mm RTC battery interface, which can be used to connect an external RTC battery to achieve more accurate timing and lower power consumption.
|  The schematic diagram of the RTC interface is as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导26.png
   :alt: 硬件设计指导26.png
   :width: 90%

IR Circuit
~~~~~~~~~~~~

|  The IR infrared receiver is IR1, which uses the IRM_3638 infrared remote control receiver. The IR infrared receiving signal is received by the PWM3_IR pin.
|  As shown below:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导27.png
   :alt: 硬件设计指导27.png
   :width: 90%

MIPI CSI Circuit
~~~~~~~~~~~~~~~~~~

|  The development board has two onboard camera interfaces, with a specification of 24Pin 0.5mm pitch FPC sockets, only supporting the connection of mipi cameras.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导28.png
   :alt: 硬件设计指导28.png
   :width: 90%

M2 Circuit
~~~~~~~~~~~~

|  The development board has one onboard M2 interface, located on the back of the main board, and the connector type is M2_NGFF_M_KEY.
|  In the M2 interface circuit design, the spread spectrum clock generator chip PI6C557-03BLE is used. PI6C557-03BLE is a spread spectrum clock generator that meets the requirements of PCI Express®3.0 and Ethernet. Its connection schematic diagram is as follows. The PI6C557-03BLE chip expands two clocks, one for PCIE30_REFCLKP_IN and PCIE30_REFCLKN_IN, and the other for PCIE30_REFCLKP_CON and PCIE30_REFCLKN_CON.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导29.png
   :alt: 硬件设计指导29.png
   :width: 90%

|  The circuit schematic diagram of the M2 interface is as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/硬件设计指导30.png
   :alt: 硬件设计指导30.png
   :width: 90%

|  The M2 interface can be used to connect 2280 and 2260规格 M.Key interface NVME solid-state drives.