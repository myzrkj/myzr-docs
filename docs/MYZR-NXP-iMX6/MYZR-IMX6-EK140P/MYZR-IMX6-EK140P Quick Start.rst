MYZR-IMX6-EK140P Quick Start
===============================

Development board instruction
-------------------------------

Development board consist of following components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1、Core board: MYZR-IMX6-CB140 ,one unit
|  2、Base board: MYZR-IMX6-MB140P ,one unit
|  3、Circuit board of screen panel ,one unit
|  4、Crystal liquid screen,one piece
|  5、 Touch screen,one unit

Development board accessory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1、Adaptor,one unit
|  2、 USB download cable,one piece
|  3、Internet cable,one piece
|  4、Serial line,one piece

Overview of development board interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-iMX6系列/MYZR-IMX6-EK140P/1425px-MYIMX6A7-MB140P-Port-F.png
   :alt: 1425px-MYIMX6A7-MB140P-Port-F.png

Booting development board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1、We need to check switching status of development board power supply before the connection between development board and computer, to ensure power supply switch in off status.(一：closed, 0: off).
|  2、Connection of serial line with computer. Connect one end of serial line to development board RS232，another connect to computer. If there is no connection of serial line with computer, interaction can't be done with development board via serial port, but no affection on development board booting and burning system.
|  3、Serial port terminal tool configuration. Use Windows's device manager to find the port number we use on the computer. Parameter of configure for serial port terminal tool.
|  SecureCRT & USB serial port3 configuration example as below:

.. figure:: /image/MYZR-iMX6系列/MYZR-IMX6-EK140P/Myimx6_mb140p_1.4.1.png
   :alt: Myimx6_mb140p_1.4.1.png

|  4、Connection of network cable. Connect one end of network cable with development board ETHO，another end inserted into lan port of computer.
|  5、Connection of USB download line. Connect one end of USB line with development board USB-OTG，another end inserted into USB port of computer.
|  6、Connection of power supply cable. Connect one end of power supply cable with development 5V_IN，another end connected with power supply socket.
|  7、Power on development board. Press development board power supply switch to closed status（—：closed，O：off）

Observe booting condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1、U-boot dynamics. You will see the LCD screen lit up and display Freescale and MYZR’s LOGO.
|  2、Serial port terminal dynamics. You can see the information about booting process outputed during the course of development board booting through serial port terminal.
|  3、After the kernel boots at a certain stage, you can see the penguins on the LCD screen. < br >
|  4、System dynamics：

.. figure:: /image/MYZR-iMX6系列/MYZR-IMX6-EK140P/963px-Myimx6_mb140p_1.5.1.png
   :alt: 963px-Myimx6_mb140p_1.5.1.png
   