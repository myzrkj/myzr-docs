Hardware Design Guide
========================

Preface
---------

| This document mainly introduces the backplane hardware interface resources and design considerations of the MYZR_T536-MB.
| The IO voltage level standards for the T536MX-CXX/T536MX-CEN2 processor are generally 1.8V and 3.3V. The pull-up power supply should generally not exceed 3.3V or 1.8V. When the external signal voltage level does not match the IO voltage level, a level conversion chip or signal isolation chip must be added in between. For buttons or interfaces, ESD design should be considered. When selecting ESD devices, attention must be paid to whether the junction capacitance is too large, as this may affect signal communication.  

1 Power Supply
----------------

| The backplane is powered by a 12V DC power supply. CON2 and CON3 are power input connectors. CON2 is a 3-pin green connector with a pitch of 3.81mm. CON3 is a DC-005 power interface, which can be connected to a power plug with an outer diameter of 5.5mm and an inner diameter of 2.1mm. SW1 is a power toggle switch; when in use, select according to the nearby "ON/OFF" silk screen.  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件1.jpg
   :alt: 硬件1.jpg

| The power input end provides circuit protection functions such as overcurrent protection, overvoltage protection, reverse insertion prevention, and rapid power-down protection.

**(1) Input Stage Power Supply Protection Circuit Design, as shown in the figure below.**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件2.png
   :alt: 硬件2.png

| VDD_12V_MAIN is converted into power supplies for the core board and backplane peripherals through different power chips. The core board provides the backplane auxiliary power signal VDD_3V3_SOM_OUT, which is used to control the power-on sequence of each power supply on the evaluation backplane.
| Recommended power-on sequence for the evaluation board: 12V DC power supply (VDD_12V_MAIN) -> Core board power supply (VDD_5V_SOM) -> Core board configures backplane auxiliary power (VDD_3V3_SOM_OUT) -> Backplane peripheral power supply -> System reset (AF27/RESETn/PU/1V8), as shown in the figure below.  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件3.png
   :alt: 硬件3.png

1.1 Core Board Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| VDD_12V_MAIN generates a 5V power supply through the SY8113BADC DCDC power chip from `silergy <https://list.szlcsc.com/brand/897.html?spm=sc.gb.xh1.zy.p___sc.gb.hd.ss&lcsc_vid=RlReVAJXE1JcBlNeQ1IKXwdWTgBcA1VSQAcLAQVQQwAxVlNSQFdfUFZQRlBWVDtW>`_, which is used to power the SOM-TLT536 core board. The power network is named VDD_5V_SOM, with a maximum current supply capacity of 3A. The enablement of this power supply is provided by the voltage division of the input VDD_12V_MAIN, realizing the sequence control of enabling immediately upon power-on. To protect the core board and facilitate voltage and current measurement, a fuse F2 has been connected in series in the power path.  

**(1) VDD_5V_SOM Power Supply Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件4.png
   :alt: 硬件4.png

| **Note:** To ensure the long-term stable and reliable operation of the core board, supply power to the core board in accordance with the typical operating voltage (5.0V) provided by our company.  


1.2 Backplane Peripheral Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| VDD_12V_MAIN generates 4 channels of evaluation backplane peripheral power supplies through 4 SY8113BADC DCDC power chips from `silergy <https://list.szlcsc.com/brand/897.html?spm=sc.gb.xh1.zy.p___sc.gb.hd.ss&lcsc_vid=RlReVAJXE1JcBlNeQ1IKXwdWTgBcA1VSQAcLAQVQQwAxVlNSQFdfUFZQRlBWVDtW>`_. The network names are: VDD_5V_MAIN, VDD_3V3_MAIN, VDD_3V3_PCIE, and VDD_1V8_MAIN, each with a maximum current supply capacity of 3A. The enablement of the 4 power channels is uniformly provided by the core board's VDD_3V3_SOM_OUT signal, realizing the sequence control where the core board power supply is powered on earlier than the peripheral power supplies.  

**(1) VDD_5V_MAIN Power Supply Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件5.png
   :alt: 硬件5.png

**(2) VDD_3V3_MAIN Power Supply Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件6.png
   :alt: 硬件6.png

**(3) VDD_3V3_PCIE Power Supply Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件7.png
   :alt: 硬件7.png

**(4) VDD_1V8_MAIN Power Supply Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件8.png
   :alt: 硬件8.png

**Design Considerations:**

| The VDD_3V3_SOM_OUT power output provided by the core board has a power supply capacity of ≤500mA. It is mainly used to control the power-on sequence of each power supply on the evaluation backplane and to power circuits related to core board configuration (such as BOOT SET, Micro SD, watchdog circuits, etc.). Do not use it to power other peripherals.  

1.3 Isolated Power Supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| VDD_5V_MAIN generates a 5V DC isolated power supply through the B0505S-1WR3L isolated power module from MORNSUN (Jin Shengyang Technology), which is used to power the isolated circuits on the evaluation backplane. The network names are VDD_5V_ISO1 and VDD_5V_ISO2, with a maximum current supply capacity of 200mA and a DC isolation capability of 3000V DC.  

**(1) VDD_5V_ISO1 Power Supply Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件9.png
   :alt: 硬件9.png

**(2) VDD_5V_ISO2 Power Supply Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件10.png
   :alt: 硬件10.png

**Design Considerations:**

| (1) When designing the backplane, if some or all functions of the input stage protection circuit are not required, appropriate simplification can be made.
| (2) The backplane power supply design can be adjusted (increased or decreased) according to the actual circuit design. It is recommended to refer to the power-on sequence provided by our company for the enablement control of the backplane power supply.
| (3) For the core board power supply, refer to the power circuit design of our company's evaluation backplane. Note that the core board power supply is 5.0V.
| (4) VDD_5V_SOM does not have a reserved large energy storage capacitor for the main power input inside the core board. When designing the backplane, place an energy storage capacitor with a total capacitance of approximately 50uF near the LGA pad of the core board.
| (5) To ensure that VDD_5V_MAIN, VDD_3V3_MAIN, VDD_3V3_PCIE, and VDD_1V8_MAIN meet the system power-on and power-off sequence requirements, the VDD_3V3_SOM_OUT output from the core board must be used to control the power enablement of VDD_5V_MAIN, VDD_3V3_MAIN, VDD_3V3_PCIE, and VDD_1V8_MAIN. This ensures that the VDD_5V_MAIN, VDD_3V3_MAIN, VDD_3V3_PEIE, and VDD_1V8_MAIN power supplies on the evaluation backplane are powered on after VDD_3V3_SOM_OUT and before the AF27/RESETn/PU/1V8 reset signal (for details, see the recommended power-on sequence of the evaluation backplane).  

2 System Startup Description
-------------------------------

| After the system is powered on, the boot code in the CPU's internal BootRom sequentially detects the SPL startup program from the SD card and eMMC FLASH, and starts from the first device containing the SPL startup program. After the SPL starts, it will first boot the U-Boot image from the SD system card (not a regular SD card); otherwise, it will boot the U-Boot image from the original startup device.  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件11.png
   :alt: 硬件11.png

**Design Considerations:**

| (1) K28/BOOT-SEL/PU/1V8 is a startup configuration pin. On the core board, a 10K resistor has been connected to pull it up to the 1.8V power supply, and a 3.9K resistor has been connected to pull it down to ground. The default startup sequence is SD card first, then eMMC FLASH.
| (2) When the KEY3 button is pressed and the evaluation board is powered on again, the input of the AD21/FEL/PU/3V3 pin is at a low level, and the CPU will enter the Mandatory Update Process mode. Firmware upgrade can be performed through the USB2.0 DRD interface.  

3 LED
--------

| The backplane is equipped with a power indicator light, user-programmable indicator lights, and module status indicator lights, which are LED1~LED4 and adopt a surface-mount package.  

3.1 Power Indicator Light
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**(1) Backplane Power Indicator Light Circuit Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件12.png
   :alt: 硬件12.png

3.2 User-Programmable Indicator Lights
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The backplane is equipped with 2 user-programmable indicator lights, LED2 and LED3, which are lit at a high level and are green in color. They are controlled through the PA7 and PJ19 pins of the CPU.  

**(1) Backplane Power Indicator Light Circuit Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件13.png
   :alt: 硬件13.png

3.3 Module Status Indicator Light
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**(1) 4G/5G Module Status Indicator Light Circuit Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件14.png
   :alt: 硬件14.png

4 KEY
--------

| The backplane includes 1 system reset button RESETn (KEY1), 1 PMIC power-on/off button PWRON (KEY2), 1 FEL button FEL (KEY3), and 2 user input buttons USER1 (KEY4) and USER2 (KEY5).  


4.1 RESETn Reset Button
~~~~~~~~~~~~~~~~~~~~~~~~~~

| KEY1 is the RESETn reset button of the backplane, which controls the reset pins of the CPU and PMIC. 

**(1) RESETn Button Circuit Design**   

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件15.png
   :alt: 硬件15.png

**Design Considerations:**

| (1) AF27/RESETn/PU/1V8 is the reset input pin of the core board. A 10K pull-up resistor is built into the core board. Under normal circumstances, leave it unconnected to avoid affecting the power-on sequence.  


4.2 PWRON Button
~~~~~~~~~~~~~~~~~~~

| KEY2 is the PMIC power-on/off button, and the button status is input to the PMIC through the PWRON pin.

**(1) PWRON Button Circuit Design**    

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件16.png
   :alt: 硬件16.png

**Design Considerations:**

| (1) PWRON is the power-on/off control pin of the PMIC. A pull-up resistor is built into the PMIC. Under normal circumstances, leave it unconnected.
| PWRON Button Circuit Design  

4.3 FEL Button
~~~~~~~~~~~~~~~~~

| KEY3 is the FEL button. When the system is powered on again, if the AD21/FEL/PU/3V3 signal is detected to be at a low level, the CPU will enter the Mandatory Update Process mode, and firmware upgrade can be performed through the USB2.0 DRD interface.  

**(1) FEL Button Circuit Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件17.png
   :alt: 硬件17.png

4.4 User Input Buttons
~~~~~~~~~~~~~~~~~~~~~~~~~

| KEY4 (USER1) and KEY5 (USER2) are user input buttons. The status of KEY4 is input to the CPU through the GPADC2_0 pin, and the status of KEY5 is input to the CPU through the PA9 pin.  

**(1) User Input Button Circuit Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件18.png
   :alt: 硬件18.png

**Design Considerations:**

| (1) The voltage input range of L27/GPADC2-0/KEY1/1V8 is 0~1.8V. For the evaluation backplane, voltage dividers can be used to control the input voltage within the range of 0~1.8V. Since no pull-up resistor is reserved for the L27/GPADC2-0/KEY1/1V8 signal inside the core board, a 10K pull-up resistor to the 1.8V power supply should be provided for this signal by default.  


5 UART
---------

| The backplane is equipped with 13 on-board UART ports. CON5 is a USB TO UART0 debug UART port, CON9 is an RS232 S-UART1 port, CON10 is an RS232 UART6 port, and J20 includes RS485 UART1, RS485 UART2, RS485 UART3, RS485 UART4, RS485 UART9, and RS485 UART11 ports. CON29 is a TTL S-UART0 port that is multiplexed with the WiFi/BT module, CON28 is a TTL UART5 port, CON30 is a TTL UART12 port that is multiplexed with EXPORT1, and CON31 is a TTL UART7 port that is multiplexed with EXPORT1.    

5.1 USB TO UART0 Port
~~~~~~~~~~~~~~~~~~~~~~~~

| The backplane uses the CH340T chip from WCH (沁恒微电子) to convert UART0 into a Type-C connector (CON5) for use as a system debug UART port. The CH340T is powered by 5V (network name: UART_VBUS) from the Type-C data cable.  

**(1) USB TO UART0 Circuit Design**  

.. figure:: /image/MYZR-全志系列/MYZR-T536-EK270/硬件19.png
   :alt: 硬件19.png

**Design Considerations:**

| (1) When designing the backplane, it is recommended to adopt the RS0102YVS8 (U7) level conversion isolation solution to prevent the RX terminal of the debug UART port from being charged in advance before the backplane is powered on, which may inject current into the core board pins and cause the system to fail to start.
| (2) The voltages of the CPU pins UART0-TX and UART0-RX are both 3.3V. Do not directly connect a debug tool with a 5V level interface, otherwise the CPU may be damaged.
| (3) Note that the USB signal requires 90ohm differential impedance matching.
| (4) ESD devices should be placed close to the Type-C connector of the interface. The traces should pass through the ESD device before connecting to the CH340T.
| (5) When designing the backplane, it is recommended to add a 2.2K pull-up resistor from the AG26/UART0-RX/Debug/3V3 network to VDD_3V3_MAIN