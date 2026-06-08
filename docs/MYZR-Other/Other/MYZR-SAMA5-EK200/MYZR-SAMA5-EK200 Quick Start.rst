MYZR-SAMA5-EK200 Quick Start
==============================

Prepare development board kits
--------------------------------

|  Development board kits consist of development board and its accessories.

Composition of development board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Development board consist of following components

- MYZR-SAMA5-CB200（core board）one unit
- MYZR-SAMA5-MB200（base board）one unit
- Crystal liquid screen,one piece
- Touch screen,one unit

Development board accessory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Development board accessories include:

- Power supply
- USB line
- Serial port line
- Standard internet cable

Overview of development board interface
-----------------------------------------

|  We need to know about some inferfaces before boot development board,and correcty connects with computers through these interfaces,here let's start with MYZR-SAMA5-MB200 inferfaces.

MYZR-SAMA5-MB200 Front view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5-EK200_front_2.1.0.1.jpg
   :alt: MY-SAMA5-EK200_front_2.1.0.1.jpg

MYZR-SAMA5-MB200 Rear view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5-MB200_back_2.2.0.1.jpg
   :alt: MY-SAMA5-MB200_back_2.2.0.1.jpg

Fast boot development board
------------------------------

1. Skip to segment “switch off power supply”，“power supply connection cable”in chapter of "connection between development and computer" for operation.
2. Skip to segment "power up for devleopment board" in chapter "development board boot",continue the operations with this step.

|  Instruction：in mode of fast boot，there is not connection between development board and computer,but system booting status can be viewed on the screen.

Development board and computer connection
--------------------------------------------

|  Since we need to connect development board with computer in many cases,below is the description about the job.

Close power supply switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. We need to check switching status of development board power supply before the connection between development board and computer,to ensure power supply switch in off statu
2. Ways to make power supply switch in off status：press development board power supply switch（icon 11 on top view of development board) to be "off" status（—：closed，O：off）.)

Connection of serial line
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Connection of cable**

1. Connect one end of serial line to icon 13 of development board ，another end to computer.
2. If there is not serial ports in the computer,need to prepare by yourself USB to serial line and connect.
3. If there is not connection of serial line with computer,ineraction can't be done with development board via serial port,but no affection on development board booting and burning system.

**Serial port terminal tool configuration**

1. To find terminal number we are using through Windows device manager in computer.
2. Configure every parameter for serial port terminal tool.
3. SecureCRT & USB serial port3 configuration example as below：

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/Securecrt_quick_connect_com3.jpg
   :alt: Securecrt_quick_connect_com3.jpg

Network cable connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of internet line with icon9 of development board ，another end inserted into lan port of computer.

Connection of USB download line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of USB line with icon22 of development board ，another end inserted into USB port of computer.

Connect the power cord
~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of power supply cable with icon12 of development，anotehr end connected with power supply socket.

Development board startup
---------------------------

|  After all the operations in "connection between development board and computer"were completed in order，the connection of devlopment board with computer is completed。to boot the board, we need to power on the development board.

Power on development board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Press development board power supply switch（icon 11 on top view of development board）to closed status（—：closed，O：off）

Observe booting condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Serial port terminal dynamics**

|  You can see the information about booting process outputed during the course of development board booting through serial port terminal.

**Development board dynamics**

|  After starting to a certain stage, the led light on the development board will always blink.

**Screen panel status**

|  If screen panel is correctly connected, there will be image shown on screen in the course of development board booting.
