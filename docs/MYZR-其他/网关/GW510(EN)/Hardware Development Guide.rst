
.. raw:: html

   <style>
   h1 {
       color: #4CAF50;  /* Level 1 heading font color */
   }
   </style>


Hardware Development Guide
==========================

Schematic Design Description
---------------------------
**Main Power Supply Circuit**

The development board is powered by a 5V DC power supply, which is connected via the Type-C connector (U24).

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/底板电源.png
   :alt: Board Power Supply
   :width: 100%

The 5V power is converted into two 3.3V outputs by the power IC, supplying power to the core and other peripherals.

**BOOT Mode**

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/boot_mode.png
   :alt: Boot Mode
   :width: 100%   

The core board reads the BOOT mode during startup (refer to the schematic for specific BOOT modes).

**Reset Circuit**

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/复位电路.png
   :alt: Reset Circuit
   :width: 100%   
Only the RESET22 button is used on this development board.

**External TF Card Circuit**

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/外接TF卡电路.png
   :alt: External TF Card Circuit
   :width: 100%    
The TF card circuit uses the SDIO bus interface.

Note: For PCB design, length matching, 3W spacing rule, and ground shielding are required.

**Ethernet Interface Circuit**

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/以太网接口电路.png
   :alt: Ethernet Interface Circuit
   :width: 100%    

The Ethernet PHY chip is located on the development board, not on the core board. Note that the two indicator LEDs of the RJ45 connector must be designed according to this schematic.

Note: For PCB design, the 4 Ethernet differential pairs must follow differential routing rules with length matching within pairs. Maintain at least 3x line width spacing between differential pairs and other signals. Length mismatch within pairs should be within 5mil, and between pairs within 25mil.

**USB Download Port Circuit**

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/USB口电路.png
   :alt: USB Port Circuit
   :width: 100%    
This is a Type-C interface used to connect to a PC for programming the board. USB signals require differential routing.

**USB HOST Circuit**

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/USB_HOST电路.png
   :alt: USB HOST Circuit
   :width: 100%    
For PCB design, each USB signal pair must follow differential routing rules with length matching within pairs. Maintain at least 3x line width spacing between differential pairs and other signals. Length mismatch within pairs should be within 5mil.

For PCB design: power traces should be wider; decoupling capacitors should be placed close to chip pins; crystals should be placed close to the chip with ground shielding and kept away from other signals.

**WIFI**

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/WIFI.png
   :alt: WIFI Circuit
   :width: 100%    
For PCB design: maintain length matching for signal groups, follow 3W spacing rule, and use ground shielding for the entire group. The antenna interface U12 requires 50Ω impedance matching, traces should be as short as possible without sharp corners, and ground shielding is required to prevent signal interference.

**Debug Port**

.. image:: ../../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/Debug调试口电路.png
   :alt: Debug Port Circuit
   :width: 100%
J3 is the debug port for the development board.

When designing the PCB, route signals in groups to avoid excessive length mismatch within signal groups.