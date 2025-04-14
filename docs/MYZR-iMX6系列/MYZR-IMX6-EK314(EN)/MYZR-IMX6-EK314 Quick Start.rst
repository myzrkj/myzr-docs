MYZR-IMX6-EK314 Quick Start
==============================

Prepare development board kits
---------------------------------

|   Development board kits consist of development board and its accessories.

Development board
~~~~~~~~~~~~~~~~~~~

|   Development board consist of following components:

- Core board: MYZR-IMX6-CB314 one unit
- Base board: MYZR-IMX6-MB314 one unit
- Circuit board of screen panel,one unit
- Crystal liquid screen,one piece
- Touch screen,one unit

Development board accessory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Development board accessories include:

- Adaptor,one unit
- USB download cable,one piece
- Internet cable,one piece
- Serial line,one piece

Overview of development board interface
------------------------------------------

|   We need to know about some interfaces before boot development board,and correctly connects with computers through these interfaces,here let's start with MYZR-IMX6-MB314 interfaces.

MYZR-IMX6-MB314 front view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/1275px-My-imx6ek314_front.jpg
   :alt: 1275px-My-imx6ek314_front.jpg

MYZR-IMX6-MB314 rear view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/963px-My-imx6ek314_back.jpg
   :alt: 963px-My-imx6ek314_back.jpg

Fast boot development board
------------------------------

|  1）Skip to segment “power supply switch off”，“power supply connection cable”in chapter of "connection between development and computer" for operation.
|  2）Skip to segment "power up for development board" in chapter "development board boot",continue the operations with this step.
|  Note：in mode of fast boot，there is not connection between development board and computer, but system booting status can be viewed on the screen.

Connection between development board and computer
----------------------------------------------------

|   Since we need to connect development board with computer in many cases, please refer the instructions about the job as below.

Power supply switch off
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1）We need to check switching status of development board power supply before the connection between development board and computer, to ensure power supply switch in off status.
|  2）Ways to make power supply switch in off status：press development board power supply switch J3（icon 28 on front view of development board） to be "off" status（—：closed，O：off）

Connection of serial line
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Cable connection**

|  1）Connect one end of serial line to development board P3（icon 12 on front view of development board），another connect to computer.
|  2）If there is no serial port in the computer, you need to prepare USB by yourself to serial line and connect.
|  3）If there is no connection of serial line with computer, interaction can't be done with development board via serial port, but no affection on development board booting and burning system.

**Serial port terminal tool configuration**

|  1）Use Windows's device manager to find the port number we use on the computer.
|  2）Parameter of configure for serial port terminal tool.
|  SecureCRT & USB serial port3 configuration example as below:

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/Securecrt_quick_connect_com3.jpg
   :alt: Securecrt_quick_connect_com3.jpg

Connection of network cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect one end of network cable with development board U12（icon 18 on front view），another end inserted into lan port of computer.

Connection of USB download line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect one end of USB line with development board J5（icon 22 on front view），another end inserted into USB port of computer.

Connection of power supply cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect one end of power supply cable with development J4（icon 29 on front view），another end connected with power supply socket.

Booting of development board
-------------------------------

- After all the operations in "connection between development board and computer"were completed in order，the connection of development board with computer is ready. To boot the board, we need to power on the development board.

Power on development board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Press development board power supply switch J3（icon 28 on front view）to closed status（—：closed，O：off）

Observe booting condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**U-boot dynamics**

- You will see the LCD screen lit up and display Freescale and MYZR’s LOGO.

**Serial port terminal dynamics**

- You can see the information about booting process outputed during the course of development board booting through serial port terminal.

**Kernel booting dynamics**

- After the kernel boots at a certain stage, you can see the penguins on the LCD screen.

**System dynamics**

|   1）Linux system
|   After the system booting is completed, the little penguin will be still displayed on the LCD screen.
|   The serial port output message prompts the user to press " Enter " , and then press " Enter " on the computer to enter the system .
|   For example:

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/Securecrt_quick_connect_com4.jpg
   :alt: Securecrt_quick_connect_com4.jpg

|   Linux QT system
|   After the system booting is completed, the development board will run a QT sample program, and you can see the QT sample program running on the LCD screen. 
|   3）Ubuntu system
|   After the system booting is completed, you can see the interface on the LCD screen.