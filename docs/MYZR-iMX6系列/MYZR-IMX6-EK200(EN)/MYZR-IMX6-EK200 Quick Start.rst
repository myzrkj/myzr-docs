
MYZR-IMX6-EK200 Quick Start
==============================

Prepare development board kits
--------------------------------

|  Development board kits consist of development board and its accessories.

Development board accessory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Development board consist of following components:

- MYZR-IMX6-CB200（core board）one unit
- MYZR-IMX6-MB200（base board）one unit
- circuit board of screen panel one unit
- crystal liquid screen,one piece
- touch screen,one unit

Development board accessory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Development board accessories include：

- Power Adapter ,one piece
- USB download line ,one bar
- Network cable ,one bar
- Serial cable ,one bar

Development Board Interface Overview
---------------------------------------

|  Before we start the development board we need to know some interfaces and connect these interfaces correctly to the computer. Here I first understand the MYZR-IMX6-MB314 interface.

MYZR-IMX6-MB200 front view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/1275px-Myimx6ek200_front.jpg
   :alt: 1275px-Myimx6ek200_front.jpg

MYZR-IMX6-MB200 rear view
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/963px-Myimx6ek200_rear_view.jpg
   :alt: 963px-Myimx6ek200_rear_view.jpg

Icon Module
~~~~~~~~~~~~

+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| Graphic | Interface description | Silk screen |     | Graphic图示 | Interface description | Silk screen |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 1       | 18/24bit LVDS0        | J24         |     | 19          | RTC_Batter            | BT1         |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 2       | 18/24bit RGB          | J23         |     | 20          | UART5/TTL             | J1          |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 3       | 18/24bit LVDS1        | J22         |     | 21          | UART4/TTL             | J1          |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 4       | 10M/100M Ethernet-1   | P4          |     | 22          | GPIO                  | J4          |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 5       | Audio                 | J20         |     | 23          | UART3/TTL             | J1          |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 6       | HDMI                  | J5          |     | 24          | UART2/TTL             | J1          |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 7       | USBOTG                | J5          |     | 25          | SPI                   | J7          |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 8       | PWR_SATA              | J12         |     | 26          | SPI1                  | J7          |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 9       | SATA                  | J11         |     | 27          | MIPI_CSI              | J9          |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 10      | USBHOST               | J8          |     | 28          | CMOS_CSI              | J14         |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 11      | UART1/RS232           | P2          |     | 29          | CAN2                  | J16         |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 12      | PWR_Switch            | J3          |     | 30          | CAN1                  | J19         |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 13      | DC_5V_IN              | J4          |     | 31          | I2C3                  | J21         |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 14      | nRESET                | SW2         |     | 32          | I2C2                  | J21         |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 15      | KEY1                  | SW3         |     | 33          | I2C1                  | J21         |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 16      | KEY2                  | SW4         |     | 34          | SD3                   | J18         |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 17      | KEY3                  | SW5         |     | 35          | WIFI                  | U16         |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+
| 18      | SD2                   | J4          |     | 36          | MINI_PCIE             | J6          |
+---------+-----------------------+-------------+-----+-------------+-----------------------+-------------+

Fast boot development board
-----------------------------

|  1）Skip to segment “switch off power supply”，“power supply connection cable”in chapter of "connection between development and computer" for operation.
|  2）Skip to segment "power up for devleopment board" in chapter "development board boot",continue the operations with this step.
|  Instruction：In mode of fast boot，there is not connection between development board and computer,but system booting status can be viewed on the screen.

Connection between development board and computer
-----------------------------------------------------

|  Since we need to connect development board with computer in many cases,below is the instructions about the job.

Close Power Supply switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  We need to check switching status of development board power supply before the connection between development board and computer,to ensure power supply switch in off status.
|  Ways to make power supply switch in off status：press development board power supply switch（icon 12 on front view of development board) to be "off" status（—：closed，O：off）.

Connection of serial lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Cable connection**

|  Connect one end of serial line to development board J2（icon 11 on front view of development board），another end to computer.
|  If there is not serial pots in the computer,need to prepare by yourself USB to serial line and connect.
|  If there is not connection of serial line with computer,ineraction can't be done with development board via serial port,but no affection on development board booting and burning system.

**Serial port terminal tool configuration**

|  To find terminal number we are using through Windows device manager in computer.
|  Configure every parameter for serial port terminal tool.
|  SecureCRT & USB serial port3 configuration example as below：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK200/Securecrt_quick_connect_com3.jpg
   :alt: Securecrt_quick_connect_com3.jpg

Connection of internet line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of internet line with development board P4（icon 4 on front view），another end inserted into lan port of computer.

Connection of USB download line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of USB line with development board J8（icon 7 on front view），another end inserted into USB port of computer.

Connection of power supply cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Connect one end of power supply cable with development J3（icon 13 on front view），anotehr end connected with power supply socket.

Booting of development board
------------------------------

|  After all the operations in "connection between development board and computer"were completed in order，the connection of devlopment board with computer is ready。to boot the board, we need to power on the development board.

Power on development board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Press development board power supply switch J3（icon 28 on front view）to closed status（—：closed，O：off）.

Observe booting condition
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Serial port terminal dynamics**

|  You can see the information about booting process outputed during the course of development board booting through serial port terminal.

**Development board dynamics**

|  In a certain phase of booting，led light on development board will flash.

**Screen panel status**
|  If screen panel is correctly connected, there will be image shown on screen in the course of development board booting.