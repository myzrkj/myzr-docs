.. raw:: html

   <style>
   h1 {
       color: green;
   }
   </style>

Hardware Development Guide
==========================

Schematic Design Description
----------------------------

Divided into sections by module, including module introduction, performance, specifications, parameters, and principles.

Schematic design considerations, CheckList.

PCB design considerations, CheckList.

ESD, EMC, EMI design considerations.

Power supply design: current loops, current magnitude.

Core Board Pin Schematic
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/核心板引脚原理图.png
   :alt: Core Board Pin Schematic
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/核心板引脚原理图_02.png
   :alt: Core Board Pin Schematic_02
   :width: 100%

40Pin Pin Definition
--------------------

40Pin Pin Schematic
~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/40Pin引脚原理图.png
   :alt: 40Pin Pin Schematic
   :width: 100%

Baseboard Schematic
-------------------

Power Management
~~~~~~~~~~~~~~~~

The baseboard power supply is a DC 5V power supply, inserted through the DC-005 socket. J15 is the power socket. Then it is converted to the 5V input required by the core board through the magnetic bead CBW322513U121T. VCC_5V will be converted by SY8113B to the 3.3V required by the baseboard and the 3.3V required by the core board.

The schematic of the power input is shown below. The 5V_DC signal is the power input from the DC interface, followed by a self-resetting fuse 1812L300MR for overload protection with a trip current of 5A. The power system of the development board uses Rockchip RK809-5 chip, combined with peripheral BUCK and LDO circuits, to provide stable power supply for the RK3568 main control, DDR, eMMC and related functional peripherals.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/电源管理.png
   :alt: Power Management
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/电源管理_02.png
   :alt: Power Management_02
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/电源管理_03.png
   :alt: Power Management_03
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/电源管理_04.png
   :alt: Power Management_04
   :width: 100%

Button Circuit
~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/按键电路.png
   :alt: Button Circuit
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/按键电路_02.png
   :alt: Button Circuit_02
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/按键电路_03.png
   :alt: Button Circuit_03
   :width: 100%

The button PCB is shown below:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/按键电路_04.png
   :alt: Button Circuit_04
   :width: 100%

TF Card Circuit
~~~~~~~~~~~~~~~

The TF card slot is located on the front side of the motherboard. It is a self-ejecting TF card socket, supporting up to 512GB MicroSD card (TF card), and supports system boot and storage. When the TF card is used as the system boot card, do not remove or insert the TF card at will during system operation.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/TFCard电路.png
   :alt: TF Card Circuit
   :width: 100%

SIM Circuit
~~~~~~~~~~~

The SIM card slot is located on the front side of the motherboard. It supports NanoSIM card size. Its signal lines are directly connected to the MINI PCI-E interface. The SIM card supports China Mobile, China Unicom, and China Telecom. It needs to be used with a 4G/5G module with MINIPCI-E interface to realize 4G/5G communication functions.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/SIM电路.png
   :alt: SIM Circuit
   :width: 100%

Ethernet Circuit
~~~~~~~~~~~~~~~~

The development board has two RJ45 interfaces, each controlled by an independent PHY chip RTL8211F-CG, supporting 10/100/1000Mbps data transmission rate. The onboard RJ45 interface has two LED indicators, controlled by the PHY chip.

The schematic of ETH0 is shown below:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/以太网电路.png
   :alt: Ethernet Circuit
   :width: 100%

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/以太网电路_02.png
   :alt: Ethernet Circuit_02
   :width: 100%

USB3.0/2.0 Circuit
~~~~~~~~~~~~~~~~~~

The RK3568 chip integrates one USB3.0 OTG controller, two USB2.0 HOST controllers and one USB3.0 HOST controller. USB3_OTG0_DP and USB3_OTG0_DM of one USB3.0 OTG channel are connected to the onboard Type-C OTG interface, with a speed of USB2.0, which can be used as a firmware download port for Emmc programming.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/USB3.0_2.0电路.png
   :alt: USB3.0/2.0 Circuit
   :width: 100%

One USB3.0 HOST1 signal is connected to the onboard USB3.0 interface (blue inner core); The onboard USB3.0 interface is USB3.2 Gen1, equivalent to USB3.1 Gen1 and USB3.0, with a maximum data rate of up to 5Gbps, and is backward compatible with USB2.0.

One USB2.0 HOST controller USB2_HOST2 signal is connected to the USB2.0 interface in the same group as the USB3.0 interface. The remaining USB2.0 HOST3 is connected to the onboard MINIPCI-E interface. The onboard USB2.0 interface supports three modes: high speed (480Mbps), full speed (12Mbps), and low speed (1.5Mbps). The system will automatically select the appropriate mode according to the inserted device.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/USB3.0_2.0电路_02.png
   :alt: USB3.0/2.0 Circuit_02
   :width: 100%

MIPI DSI Circuit
~~~~~~~~~~~~~~~~

The development board has two MIPI DSI interfaces, both located on the front side of the motherboard, namely J5 and J6. The interface uses a 30Pin FPC socket, supports video output and touch, supports dual MIPI screens working simultaneously, and the maximum resolution supported in single MIPI mode is 1920x1080@60fps.

The MIPI DSI interface schematic is shown in the figure:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/MIPIDSI电路.png
   :alt: MIPI DSI Circuit
   :width: 100%

HDMI TX Circuit
~~~~~~~~~~~~~~~

The RK3568 chip supports HDMI2.0 and is backward compatible with HDMI1.4, supporting up to 4K@60Hz, and supports video output and audio output. The development board is equipped with a vertical standard HDMI interface, which can be directly connected to a display with a standard HDMI interface through a dual-head HDMI cable.

The HDMI TX interface schematic is shown in the figure:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/HDMITX电路.png
   :alt: HDMI TX Circuit
   :width: 100%

Audio Circuit
~~~~~~~~~~~~~

The 3.5mm headphone jack and SPK speaker interface are located next to the USB socket on the front side of the motherboard. The audio input/output function is implemented through the power management chip PMIC RK809-5 on the core board.

The onboard 3.5mm headphone jack supports audio input/output, which is a 2-in-1 interface for headphone output + microphone input. It can be connected to wired headphones or to an amplifier through an AUX cable. The SPK interface specification is XH2.54-2P, which can be used to connect an 8-ohm 1W small speaker with a 2.54mm interface.

The peripheral circuits of the headphone jack and SPK interface are shown below:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/Audio电路.png
   :alt: Audio Circuit
   :width: 100%

Among them, HPL_OUT is the headphone left channel audio output signal, HPR_OUT is the right channel audio output signal, HP_SNS is the headphone reference ground, MIC1_INP is the microphone negative signal input, MIC1_INN is the microphone positive signal input, SARADC_VIN2_HP_HOOK is the headphone wire control detection signal, SPKN_OUT is the speaker audio negative output, and SPKP_OUT is the speaker audio positive output.

MINIPCI-E Circuit
~~~~~~~~~~~~~~~~~

The M2-B interface is located on the back of the development board. The PCIe type of M2-B is PCIe2.0x1, supporting a maximum data rate of 5Gbps; It can be used with full-height or half-height WIFI network cards and 4G/5G modules.

When the M2-B interface is connected to a network card module, it uses the PCIe protocol; When this interface is connected to a 4G/5G module, although the physical connection interface is M2-B, it actually uses the USB protocol.

The M2-B circuit connection is shown below:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/MINIPCI-E电路.png
   :alt: MINIPCI-E Circuit
   :width: 100%

Debug UART Circuit
~~~~~~~~~~~~~~~~~~

The development baseboard is equipped with one UART. CON4 is the USB TO UART0 debug serial port.

The development board baseboard converts UART0 to a Type-C connector (CON4) through the CH340T chip from WCH (WCH Electronics), which is used as the system debug serial port. The CH340T is powered externally by 5V (network name: VDD_5V_VBUS) from the Type-C data cable.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/Debug调试串口电路.png
   :alt: Debug UART Circuit
   :width: 100%

Design considerations:

When designing the baseboard, it is recommended to use the RS0102YVS8 (U9) level conversion isolation scheme to prevent the RX terminal of the debug serial port from being charged in advance before the baseboard is powered on, which would inject current into the core board pins and cause the system to fail to start.

The CPU pins UART2_RX_M0_DEBUG and UART2_TX_M0_DEBUG are both 3.3V level. Do not directly connect debug tools with 5V level interfaces, otherwise the CPU will be damaged.

Note that the USB signal needs to be matched with 90ohm differential impedance.

ESD devices should be placed close to the Type-C connector, and the traces should be connected to the CH340T after passing through the ESD.

FAN Circuit
~~~~~~~~~~~

The development board reserves a 2Pin 2.54mm specification 5V fan power supply interface. The conduction state of the 2SK3018 MOS tube can be controlled through the TSADC_SHUT_M0 (GPIO0_A1_z) signal, thereby controlling the conduction of the BSS84 MOS tube to realize the fan on/off control.

The FAN driver schematic is shown below:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/FAN电路.png
   :alt: FAN Circuit
   :width: 100%

RTC Circuit
~~~~~~~~~~~

The development board reserves a 2Pin 2.54mm specification RTC battery interface, which can be used to connect an external RTC battery for more accurate timing and lower power consumption.

The RTC interface schematic is shown below:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/RTC电路.png
   :alt: RTC Circuit
   :width: 100%

IR Circuit
~~~~~~~~~~

The IR infrared receiver is IR1, which uses the IRM_3638 infrared remote control receiver. The IR infrared receiving signal is received by the PWM3_IR pin.

As shown below:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/IR电路.png
   :alt: IR Circuit
   :width: 100%

MIPI CSI Circuit
~~~~~~~~~~~~~~~~

The development board is equipped with two camera interfaces. The interface specification is a 24Pin 0.5mm pitch FPC socket, which only supports connecting MIPI cameras.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/MIPICSI电路.png
   :alt: MIPI CSI Circuit
   :width: 100%

M2 Circuit
~~~~~~~~~~

The development board is equipped with an M2 interface, located on the back of the motherboard, with the connector type being M2_NGFF_M_KEY.

In the M2 interface circuit design, a spread spectrum clock generator chip PI6C557-03BLE is used. PI6C557-03BLE is a spread spectrum clock generator that meets PCI Express®3.0 and Ethernet requirements. Its connection schematic is shown below. The PI6C557-03BLE chip expands two clock channels, one for PCIE30_REFCLKP_IN and PCIE30_REFCLKN_IN, and the other for PCIE30_REFCLKP_CON and PCIE30_REFCLKN_CON.

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/M2电路.png
   :alt: M2 Circuit
   :width: 100%

The circuit schematic of the M2 interface is shown below:

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/M2电路_02.png
   :alt: M2 Circuit_02
   :width: 100%

The M2 interface can be used to connect NVME solid-state drives with M.Key interface in 2280 and 2260 specifications.