Hardware Design Guide
=========================

Hardware Circuit Description
-------------------------------

Power Input / Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Power Input**:
   
   | The power supply is 5V/3A input, powered through the Type-C port with part number J1. When the development board is powered on, the power indicator stays on to indicate normal power input; the power indicator turns off to indicate reverse power connection or no power connection.

* **Programming**:

   | Programming is performed via the Type-C port of J1. To program, connect J1 to a computer. Then, you **must set the DIP switch to Device mode**; note that a **data transmission-capable USB cable** is required.
   | For programming: **Before plugging in the power supply, press and hold the programming button (part number: SW2), select the target file, then connect the power supply. Release the programming button only after the device is detected; programming will start automatically**.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件1.png
   :alt: 硬件1.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. Ensure ESD protection components are added.
   | 2. Add decoupling capacitors between power supply and ground.
   | 3. Parallel 0.1μF + 10μF ceramic capacitors at the output to cover a wide frequency range.
   | 4. Ground the metal case through a 220Ω/100MHz ferrite bead.

* **PCB Design Considerations**:

   | 1. Widen power and ground traces as much as possible. Ideally, ground traces should be wider than power traces, and power traces wider than signal traces.
   | 2. Ensure the power supply is connected to the chip pins **only after passing through decoupling capacitors**. (Decoupling capacitors typically serve two purposes: providing instantaneous current for the chip and filtering power supply noise.)
   | 3. Use a large-area copper layer as the ground plane. On the PCB, connect all unused areas to ground for use as the ground plane. Alternatively, use a multi-layer board with separate layers for power supply and ground.
  
Headphone
~~~~~~~~~~~~

   | A 3.5mm headphone jack (J9) is provided. Audio input/output functions are implemented by the main control chip H618. **Audio output is supported, while audio input is not supported**.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件2.png
   :alt: 硬件2.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. Ensure ESD protection components are added.
   | 2. Add a 0.1μF capacitor to the power supply.
   | 3. Among the signals: HP_PLUG_IN_DET is the headphone insertion detection signal, LINEOUTL is the headphone left-channel audio output signal, and LINEOUTR is the right-channel audio output signal. 

* **PCB Design Considerations**

   | 1. Ensure impedance matching for the audio signal transmission path to reduce signal distortion.
   | 2. Isolate high-frequency signals (e.g., Bluetooth modules) from audio lines to avoid crosstalk.
   | 3. Use shielding layers or ground traces to enclose sensitive signal lines.

SD Card
~~~~~~~~~~

   * The TF card slot is located on the back of the baseboard. It is a push-push TF card socket, supporting a maximum of 512GB MicroSD card (TF card) for system booting and storage. When the TF card is used as the system boot card, **do not insert or remove it arbitrarily during system operation**.
   * Testing shows that some SanDisk TF cards may get stuck on the boot screen and fail to enter the system when used as Android system boot cards. If you need to run the Android system from a TF card, it is recommended to choose TF cards from other brands such as Samsung, Kioxia, or Kingston.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件3.png
   :alt: 硬件3.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. Add ESD protection components.
   | 2. Add 10μF and 0.1μF capacitors to the power supply.
   | 3. Add a 3.3V pull-up resistor to the CD (Card Detect) pin.

* **PCB Design Considerations**:

   | 1. Shorten trace lengths: Keep high-speed signal traces (e.g., in SDIO mode) as short as possible to reduce parasitic inductance and capacitance.
   | 2. Avoid cross-interference: Keep signal traces away from high-frequency or high-current lines (e.g., power supplies, motor drivers).
   | 3. Add TVS diodes (e.g., USBLC6-4SC6) to data and power lines to prevent electrostatic damage.
   | 4. Trace impedance: Control the impedance of data lines (e.g., DAT0-DAT3, CMD, CLK) to typically 50Ω single-ended, and maintain equal lengths (especially in high-speed mode).
 
GPIO Pin Header
~~~~~~~~~~~~~~~~~

   | GPIOs are led out through a 26-pin header with a 2.54mm pitch. Among the 26 pins: 2 pins for 5V power supply, 2 pins for 3.3V power supply, 3 pins for GND, and the remaining pins are GPIO pins.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件4.png
   :alt: 硬件4.png
   :width: 90%

IR (Infrared)
~~~~~~~~~~~~~~~

   | The IR receiver (J8) is located next to the pin header. It uses the HS0038B infrared remote control receiver, and the IR reception signal is received by the PH10 pin. The schematic diagram is shown below.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件5.png
   :alt: 硬件5.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. Connect a 100Ω resistor in series with the power supply to suppress power supply noise.
   | 2. Add 0.1μF and 10μF capacitors to the power supply to stabilize signals.
   | 3. Reserve a 3.3V pull-up resistor for the reception signal line (OUT).

* **PCB Design Considerations**:

   | 1. Keep away from high-frequency signal lines, power supplies, motors, or other noise sources.
   | 2. Keep the reception signal line (OUT) as short as possible to reduce coupled noise.
   | 3. The PWM carrier frequency of the transmitter (typically 38kHz) must match the center frequency of the receiver; excessive deviation will reduce sensitivity.
   | 4. Physically isolate the transmitter and receiver circuits to prevent direct LED light from hitting the receiver (triggering should be via reflected or diffused light).

Buttons
~~~~~~~~~~

   * There are two buttons on the baseboard: a Reset button and a FEL (Programming) button, with silkscreen labels "Reset" and "Burn" respectively on the board. 
     * The Reset button is used to reset the system and restart it. The schematic diagram of the Reset button is shown in the above figure, where AP_RESET is the reset signal input of the core board, connected to button SW3 for easy debugging.
     * The Burn (Programming) button is used for burning Android images. Its main function is to facilitate burning/downloading Android images to the eMMC. Usage method: Open the Allwinner development tool, press and hold the KEY button while the board is powered off, then connect a USB cable via the Type-C OTG port. Release the button when the Allwinner development tool on the computer indicates that the device is successfully connected, then proceed to burn the Android image. The schematic diagram of the Programming button is shown below:

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件6.png
   :alt: 硬件6.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. Add ESD protection components.
   | 2. Add a 3.3V pull-up resistor to the Reset button, and reserve a 3.3V pull-up resistor for the Programming button.
   | 3. Add a 0.1μF capacitor for filtering.
   | 4. Connect a 22Ω resistor in series.

* **PCB Design Considerations**：

   | 1. Clearly mark the silkscreen during design.

WiFi & Bluetooth
~~~~~~~~~~~~~~~~~~~

   | The on-board WiFi module is located on the back of the baseboard, behind the TF card slot. It uses the AW869A chip, supporting 2.4GHz and 5.8GHz frequency bands, 802.11 b/g/n/ac/ax wireless standards, and Bluetooth BT5.0.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件7.png
   :alt: 硬件7.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. Ensure pull-up resistors are added.
   | 2. Reserve two capacitors for the antenna signal.

* **PCB Design Considerations**:

   | 1. RF traces (e.g., antenna feed lines): Keep them as short and straight as possible. Avoid 90° corners (use 45° or curved traces instead).
   | Avoid layer changes; if layer changes are unavoidable, add via compensation (stub effects affect impedance).

HDMI
~~~~~~

   | The only video output interface of MYZR-H618-MB120-REVA is the HDMI interface, which is a standard HDMI port for connecting external displays. The H618 chip supports HDMI 2.0 and is backward compatible with HDMI 1.4, supporting a maximum resolution of 4K@60Hz for both video and audio output. The standard HDMI interface on the baseboard can be directly connected to a display with a standard HDMI interface using a dual-head HDMI cable.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件8.png
   :alt: 硬件8.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. Add decoupling capacitors to the power supply.
   | 2. Add a diode to the 5V power supply.
   | 3. Ensure ESD protection components are added.

* **PCB Design Considerations**:

   | 1. Route HDMI signals strictly as differential pairs with a complete reference plane. Avoid crossing splits as much as possible, route on the top layer, and control the differential impedance to 100Ω ±10%.
   | Avoid 90° corners; use 45° or curved traces to reduce impedance discontinuities.
   | 2. Avoid layer changes if possible. If layer changes are necessary, add return ground vias near the vias (to reduce reference plane discontinuities).
   | 3. Control the differential pair impedance to 100Ω, and strictly maintain equal lengths and optimize trace routing.
   | 4. Ensure a clean power supply, with decoupling capacitors placed close to the chip.

USB
~~~~~

   * The H618 chip has four built-in USB 2.0 HOST controllers. To use the following Type-C or Type-A interface functions, you need to manually switch via the toggle switch:
     * Toggle the switch toward the Type-A interface to enable the Type-A Host function.
     * Toggle the switch toward the Type-C interface to enable the Type-C Device function.
   * The USB0_DP and USB0_DM signals of one USB 2.0 channel are connected to the on-board Type-C OTG interface (USB 2.0 speed). This interface can be used as a firmware download port and OTG debugging port for burning Android images or OTG debugging.
   * The on-board USB 2.0 interface supports three modes: High-Speed (480Mbps), Full-Speed (12Mbps), and Low-Speed (1.5Mbps). The system automatically selects the appropriate mode based on the connected device.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件9.png
   :alt: 硬件9.png
   :width: 90%

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件10.png
   :alt: 硬件10.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. Add ESD protection components.
   | 2. Ground the metal case through a 200Ω/100MHz ferrite bead.
   | 3. Pay attention to the corresponding package of the USB connector.

* **PCB Design Considerations**:

   | 1. Route USB signals strictly as differential pairs with a complete reference plane. Avoid crossing splits as much as possible, and control the differential impedance to 90Ω ±10%.
   | 2. Widen the VBUS power traces.

FAN
~~~~~

   | The baseboard reserves a 2-pin 1.5mm fan power interface (5V). The conduction state of the SS8050 transistor is controlled via PWM1, which in turn controls the conduction time of the MOSFET to adjust the fan speed. The silk screen for the positive and negative poles of the fan interface is located on the front of the board; check carefully during connection to prevent reverse connection (which may damage the fan).

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件11.png
   :alt: 硬件11.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. PWM signal control is required.
   | 2. Add diodes to the positive and negative poles to prevent device damage from reverse connection.

* **PCB Design Considerations**:

   | 1. Widen the traces for the power supply section.

Debug Interface
~~~~~~~~~~~~~~~~~~

   | The on-board Debug UART port is led out through a 1×3 pin header with a 2.54mm pitch. The pin silkscreens are GND, RX, and TX respectively. The core board leads out UART0_TX and UART_RX, which are connected to the on-board TX and RX header pins via a 74LVC1G125GW line driver and a 22Ω resistor. When the IOFF circuit disables the output, it prevents destructive reverse current from flowing through the device when powered off. Additionally, ESD protection components (PESD3V3L1BA) are connected between the TX/RX pins of the header and ground to protect sensitive electronic devices from electrostatic discharge (ESD) without distorting data signals.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件12.png
   :alt: 硬件12.png
   :width: 90%

LED Indicators
~~~~~~~~~~~~~~~~~

   * There are two LED indicators on the baseboard: 1 power indicator and 1 user indicator. LED2 is the power indicator, and LED1 is the user indicator.
   * The power indicator stays red when the core board is working normally, and turns off when the system is shut down or powered off. DLDO1_3V3 is the power input of the core board, generated by stepping down the 5V power supply of the baseboard via the AXP313A chip.
   * The user indicator is a green LED. By default, it functions as a system status indicator (heartbeat LED) when the system starts. After the system boots up normally, the status indicator enters heartbeat mode (flashing twice per cycle). The user LED is programmable, and users can control it via commands/programs.

.. image:: /image/MYZR-全志系列/MYZR-H618-EK120/硬件13.png
   :alt: 硬件13.png
   :width: 90%

* **Schematic Design Considerations**:

   | 1. Connect a 4.7kΩ resistor in series during design to prevent excessive current from damaging the LED.
   | 2. Note that the power supply voltage is 3.3V.

* **PCB Design Considerations**:

   | 1. Clearly mark the diode direction on the silkscreen.

Ethernet
~~~~~~~~~~~

   | MYZR-H618-MB120-REVA leads out one RJ45 interface. The on-board RJ45 interface has two LED indicators controlled by the PHY chip. The Gigabit Ethernet port is controlled by the independent PHY chip RTL8211F-GG, supporting data transmission rates of 10/100/1000Mbps. The following are two working modes of the Ethernet port LEDs, which depend on the driver used by the PHY; the actual working status shall prevail. 

   * Mode 1 (Dual-LED Mode): 

     * The left green LED indicates the network connection status: stays on for successful connection, turns off for connection failure or no connection. 
     * The right yellow LED indicates the network data transmission status: stays on when there is no data transmission, flashes when data is being transmitted (the flashing frequency is related to the real-time data transmission volume). 
     * In this mode, only the network connection and data transmission status can be determined; it is impossible to distinguish between Gigabit and Fast Ethernet connections.
   
   * Mode 2 (Single-LED Mode):
    
     * The left green LED indicates the Gigabit network connection/transmission status. 
     * The right yellow LED indicates the Fast Ethernet connection/transmission status. 
     * Flashing indicates data

PCB Precautions
-----------------

   | 1. For the network port part, the TX and RX differential traces shall comply with differential requirements, with complete signal reference. They should not cross splits as much as possible, and the differential impedance shall be controlled at 100Ω ± 10%.
   | 2. For the high-voltage part of the network port, check whether it is far enough from low-voltage signal lines and components, with a minimum distance of 2mm.
   | 3. Check whether the area under the network port transformer has been hollowed out.
   | 4. The differential impedance of differential lines (TXD/RXD) shall be controlled at 100Ω (50Ω for single-ended). It is recommended to use stack-up calculation tools first to confirm the trace width and spacing.
   | 5. For high-current PHY chips, reserved thermal vias or copper foils are required.