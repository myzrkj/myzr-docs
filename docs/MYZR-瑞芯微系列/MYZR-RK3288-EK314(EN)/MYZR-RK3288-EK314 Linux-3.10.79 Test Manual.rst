MYZR-RK3288-EK314 Linux-3.10.79 Test Manual
============================================


Preparation before test
------------------------

|   1）Prepare a set of MYZR-RK3288-EK314 development board, 5V DC power supply, USB to serial cable.
|   2）Connect the serial cable to the development board and power .


Test item
----------

Network inferface test
~~~~~~~~~~~~~~~~~~~~~~~~

|   MYZR-RK3288-EK314 support two ethernet interfaces, one is 100 Mbps ethernet, the other is 1 Gbps ethernet.

**Interface property**

+---------------------------+--------------------+-------------------------+------------------+
| Evaluation board model no | Interface position | Interface rate standard | System interface |
+===========================+====================+=========================+==================+
| MYZR-RK3288-EK314         | U13                | 10/100/1000Mbps         | eth0             |
+                           +--------------------+-------------------------+------------------+
|                           | P1                 | 10/100Mbps              | eth1             |
+---------------------------+--------------------+-------------------------+------------------+


**Test method**

|   1） Test instruction
|   Set wired network card IP of computer as 192.168.18.18

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.1.1.png
   :alt: My-rk32-ek314test_2.1.1.png


|   2） Eth0 connect test
|   Connect lan line: connect “eth0”on evaluation board with corresponding wired network card interface on computer with lan line.
|   Set evaluation board IP：

.. code-block:: shell

    ＃ ifconfig eth0 192.168.18.36 　　　　　＃ configure the eth0

|   Execute test command：

.. code-block:: shell

    ＃ ifconfig eth1 down 　　　　　＃ eth1 to be shut down
    ＃ ping 192.168.18.18 -c 2 -w 4 　　　　　＃ send ICMP to HOST


|   Observe test result：system will output message like following:

.. code-block:: shell

    --- 192.168.18.18 ping statistics ---
    2packets transmitted, 2 packets received, 0% packet loss

|   Test result：“0% packet loss”represent test passing.
|   Figure

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.1.2.png
   :alt: My-rk32-ek314test_2.1.2.png

|   3） Eth1 connect test
|   Connect lan line：insert one end of lan line into “eth1”on evaluation board and another end into wired network card interface on computer.
|   Set the second network inter face IP：

.. code-block:: shell

    ＃ ifconfig eth1 192.168.18.27 　　　　　＃ configure the eth1

|   After setting the system will output message on working condition of second network interface，like following：

.. code-block:: shell

    smsc95xx 1-1.1:1.0 eth1: link up, 100Mbps, full-duplex, lpa 0x4DE1

|   Execute test command：

.. code-block:: shell

    ＃ ifconfig eth0 down ＃ eth0 to be shut down
    ＃ ping 192.168.18.18 -c 2 -w 4 　　　　　＃ send ICMP to HOST

|   Observe test result：system will output message like following：

.. code-block:: shell

    --- 192.168.18.18 ping statistics ---
    2packets transmitted, 2 packets received, 0% packet loss

|   Test result：“0% packet loss”represent test passing
|   Figures

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.1.3.png
   :alt: My-rk32-ek314test_2.1.3.png


USB test
~~~~~~~~~

**Interface property**

+----------------------------+--------------------+-------------------------+
| Evaluation board model no. | Interface position | Interface rate standard |
+============================+====================+=========================+
| MYZR-RK3288-EK314          | J10                | 480 Mbits/s             |
+----------------------------+--------------------+-------------------------+

**Test method**

|   1） Start test
|   Insert USB device into USB port on base board，enter the following command：

.. code-block:: shell

    ＃ df

|   2） Test over
|   Instruction：when plug in & out U disk from USB interface，enter the following command：


.. code-block:: shell

    ＃ df

**Figure**

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.2.1.png
   :alt: My-rk32-ek314test_2.2.1.png


SD card test
~~~~~~~~~~~~~~

**Interface property**

+----------------------+--------------------+----------------+
| Evaluation model no. | Interface position | Interface type |
+======================+====================+================+
| MYZR-RK3288-EK314    | U22                | SD             |
+----------------------+--------------------+----------------+

**Start test**

|   1） Insert device into SD card slot
|   Insert SD card into SD card port on base board，enter the following command：

.. code-block:: shell

    ＃ df

|   2） Test over
|   Take out SD card after SD card pop-pup,then test is over.

**Figures**

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.3.1.png
   :alt: My-rk32-ek314test_2.3.1.png


Audio test
~~~~~~~~~~~

**Test instruction**

|   The test is to verify audio function of evaluation board by playing audio file.

**Test method**

|   1）Prepare test
|   Connect audio output device to audio element in front view of base board,audio element is “J20”in front view of base board.

|   2）Execute test
|   Play a video with gplay，commanded as below：

.. code-block:: shell

    ＃ aplay /usr/share/sounds/alsa/Rear_Left.wav

|   The above command will play a file designated by command with gplay.

|   3）Test result
|   You can see the vedeo played on display screen of evaluation board and hear the voices outputed by audio device.


**Figures**

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.4.1.png
   :alt: My-rk32-ek314test_2.4.1.png


Standard GPIO test
~~~~~~~~~~~~~~~~~~~

**Interface roperty**

+----------------------+-----------+---------------+-----------------+
| Evaluation model no. | LED label | GPIO property | IO order number |
+======================+===========+===============+=================+
| MY-RK3288-EK314      | D1        | GPIO0_B1      | 9               |
+                      +-----------+---------------+-----------------+
|                      | D2        | GPIO0_C2      | 18              |
+                      +-----------+---------------+-----------------+
|                      | D3        | GPIO0_B0      | 8               |
+                      +-----------+---------------+-----------------+
|                      | D4        | GPIO0_A7      | 7               |
+----------------------+-----------+---------------+-----------------+

**Test method**

|   1）GPIO output test
|   Set IO order number for GPIO of which need to be tested.

.. code-block:: shell

    ＃ OUT_IO_NUMBER=9

|   Lead out GPIO

.. code-block:: shell

    ＃ echo ${OUT_IO_NUMBER} > /sys/class/gpio/export

|   Set GPIO direction

.. code-block:: shell

    ＃ echo out > /sys/class/gpio/gpio${OUT_IO_NUMBER}/direction

|   Control outputed electrical level

.. code-block:: shell

    ＃ echo 0 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value
    ＃ echo 1 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value


.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.5.1.png
   :alt: My-rk32-ek314test_2.5.1.png


|   2）GPIO input test
|   Set IO order number for GPIO of which need to be tested

.. code-block:: shell

    ＃ IN_IO_NUMBER=18

|   Lead out GPIO

.. code-block:: shell

    ＃ echo ${IN_IO_NUMBER} > /sys/class/gpio/export

|   Set GPIO方向

.. code-block:: shell

    ＃ echo in > /sys/class/gpio/gpio${IN_IO_NUMBER}/direction

|   Check inputed electrical level

.. code-block:: shell

    cat /sys/class/gpio/gpio${IN_IO_NUMBER}/value


GPIO-KEY test
~~~~~~~~~~~~~~

**Interface property**

+--------------------+---------------+--------------+
|  MY-RK3288-EK314                                  |
+====================+===============+==============+
| Interface position | GPIO property | KEY property |
+--------------------+---------------+--------------+
| SW1                | gpio-keys     | Volume Down  |
+--------------------+---------------+--------------+
| SW2                | gpio-keys     | Volume Up    |
+--------------------+---------------+--------------+
| SW3                | gpio-keys     | Power        |
+--------------------+---------------+--------------+
| SW4                | gpio-keys     | Reset        |
+--------------------+---------------+--------------+
| SW5                | gpio-keys     | Recovery     |
+--------------------+---------------+--------------+

**Test method**

|   1）Execute test program
|   Enter command to execute on terminal,example as below：

.. code-block:: shell

    ＃ evtest

|   2）Select test device
|   Select the device event number [0-2]: 2
|   Enter order number corrsponding with“gpio-keys”，here it is 2

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.6.1.png
   :alt: My-rk32-ek314test_2.6.1.png


|   3）Proceed with interactive test
|   On terminal you can“Testing ... (interrupt to exit)”，this time press or release SW1、SW2。message like below will come out：

.. code-block:: shell

    Event: time 1452590477.115958, type 1 (EV_KEY), code 114 (KEY_VOLUMEDOWN), value 0
    Event: time 1452590477.115958, -------------- SYN_REPORT ------------
    Event: time 1452590478.415953, type 1 (EV_KEY), code 115 (KEY_VOLUMEUP), value 1

|   Message of“value 1”is outputed with press of key，message of“value 0”is outputed with release of key.


.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.6.2.png
   :alt: My-rk32-ek314test_2.6.2.png

|   4）End test
|   Press “Ctrl”+“C”on computer to end the test program for keys.


Serial port test
~~~~~~~~~~~~~~~~

|   MYZR-RK3288-EK314 has total 5 serial ports，one is debug seiral port，the other 4 are user serial ports.

**User serial port property**

+----------------------------+-------+--------------------+------------------+
| Evaluation board model no. | UARTx | Hardware interface | System interface |
+============================+=======+====================+==================+
| MYZR-RK3288-EK314          | UART0 | BT (Bluetooth)     | ttyS0            |
+                            +-------+--------------------+------------------+
|                            | UART1 | P3                 | ttyS1            |
+                            +-------+--------------------+------------------+
|                            | UART2 | P4 (DEBUG)         | ttyS2            |
+----------------------------+-------+--------------------+------------------+

|   Tips：transceiver pins of serial port are listed here,but please refer to schematic for definition of all pins of serial port.

**Serial port test**

|   1）Serial port test
|   Intruction of test method：
|   Serial cable directly connected to the computer and UART1, landing and testing with ssh client.
|   Instruction of test result：
|   Send charater string to serial port through ssh client, and the serial port can receive the charater string.
|   2）Install ssh client

.. code-block:: shell

    ＃ apt-get install ssh

|   3）UART1 test
|   Execute test command

.. code-block:: shell

    ＃ echo “myzr” > /dev/ttyS1 (UART1 send charater string “myzr“)
    ＃ cat /dev/ttyS1 (UART1 receive charater string )

|   Figures for test result

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.7.1.png
   :alt: My-rk32-ek314test_2.7.1.png


RTC test
~~~~~~~~

**Test instruction**

|   Due to restrictions in transportation，MYZR-RK3288-EK314 evaluation board doesn't contatin battery in delivery。before RTC test please prepare button cell to install on evaluation board.
|   MYZR-RK3288-EK314 battery holder is located in“BT1”on front view of base board.

**Test method**

|   1）Power off then reboot device,to check the time of system and hardware.
|   Command to check clock of current system as below:

.. code-block:: shell
    
    ＃ date

|   Message outputed by system as below：

.. code-block:: shell

    Thu Aug 6 05:35:17 UTC 2012

2）Command to check clock of RTC chip as below：

.. code-block:: shell

    ＃ hwclock

|   Message outputed by system as below：

.. code-block:: shell

    Thu Aug 6 05:35:59 2012 0.000000 seconds

|   3）Set system clock and synchronously set to RTC chip.
|   Command to set system clock are with below reference：

.. code-block:: shell

    ＃ date -s "2013-03-28 12:30:30"

|   Command to write system clock into hardware as below：

.. code-block:: shell

    ＃ hwclok –w

|   4）Power off and reboot evaluation board，to check current system clock and hardware clock.
|   Please refer to step 1
|   5）Test Results
|   It will be a newly-set clock after execution until step3.

**Figures**

|   Figure 1:

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.8.1.png
   :alt: My-rk32-ek314test_2.8.1.png

|   Figure 2:

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.8.2.png
   :alt: My-rk32-ek314test_2.8.2.png


SPI test
~~~~~~~~

|   MYZR-RK3288-EK314 has two groups of SPI interfaces。

**Interface property**

|   Pins of MISO and MOSI need to be used for test,listed as below.

+----------------------------+------+--------+--------+------------------+
| Evaluation board model no. | SPIx |  MISO  |  MOSI  | System interface |
+============================+======+========+========+==================+
| MYZR-RK3288-EK314          | SPI1 | J11:33 | J11:35 | spidev0.0        |
+                            +------+--------+--------+------------------+
|                            | SPI2 | J11:38 | J13:34 | spidev2.0        |
+----------------------------+------+--------+--------+------------------+


**Test specification**

|   1）Adopt way of SPI self-sending（output）self-receiving（input).
|   ``Note：the test need a short connection of evaluation board pins,if you are not sure of how to conduct this kind of connection,please ask hardware engineer for a support,otherwise it may cause a damage of evaluation board.``
|   2）SPI port which is matched up with SPI test program is SPI2，e.g.SPI test is SPI2 test.

**Test method**

|   1）Prepare test
|   Short connect MISO pin and MOSI pin of SPI2.
|
|   Execute test

.. code-block:: shell

    ＃ ./spi_test -D /dev/spidev0.0

|   3）Test result
|   If SPI is normal,you can see following charaters on terminal：

.. code-block:: shell

    FF FF FF FF FF FF
    40 00 00 00 00 95
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    FF FF FF FF FF FF
    DE AD BE EF BA AD
    F0 0D


**Figures**

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.9.1.png
   :alt: My-rk32-ek314test_2.9.1.png

WIFI test
~~~~~~~~~

|   The model of the WIFI chip used in the MY-RK3288-EK314 evaluation board is: AP6335
|   1）Step 1
|   Select the SSID, such as: Honor V9

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.10.1.png
   :alt: My-rk32-ek314test_2.10.1.png

|   2）Step 2
|   Enter WIFI password and connect successfully

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.10.2.png
   :alt: My-rk32-ek314test_2.10.2.png


Bluetooth test
~~~~~~~~~~~~~~

|   The Bluetooth chip model used on the MY-RK3288-EK314 evaluation board is: AP6335
|   1）Step 1
|   Turn on Bluetooth, click on "Prefrences" -> "Bluetooth Manager"

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.11.1.png
   :alt: My-rk32-ek314test_2.11.1.png

|   2）Step 2
|   Search Bluetooth, click "Search"


.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.11.2.png
   :alt: My-rk32-ek314test_2.11.2.png

4G internet module test
~~~~~~~~~~~~~~~~~~~~~~~~

**Test instruction**

|   Test online 4G module, such as L506.

**Test method**

- Install wvdial

.. code-block:: shell

    ＃ sudo apt-get install wvdial

|   Modify the configuration file /etc/wvdial.conf

.. code-block:: shell

    ＃ vim /etc/wvdial.conf

|   Add the following:

.. code-block:: shell

    [Dialer Defaults]
    Modem = /dev/ttyUSB2
    Baud = 115200
    Init1 = ATZ
    Init2 = AT+CGDCONT=1,"IP","CMNET"
    Init3 = AT+CGEQREQ=1,2,128,384,,,0,,,,,,
    Phone = *99*1#
    Username = cmnet
    Password = cmnet
    New PPPD = yes

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.12.1.png
   :alt: My-rk32-ek314test_2.12.1.png

|   Dial

.. code-block:: shell
    
    ＃ wvdial &

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314test_2.12.2.png
   :alt: My-rk32-ek314test_2.12.2.png


HDMI test
~~~~~~~~~

**Test instruction**

|   Connect HDMI.

**Test method**

- Write linux-boot_hdmi.img

|   Write the image with AndroidTool_Release_v2.35.

- Test

|   Power on, HDMI has display image

- Modify the resolution

|   To modify the resolution, modify arch/arm/boot/dts/lcd-box.dtsi.


EDP test
~~~~~~~~

**Test instruction**

|   Connect EDP.

**Test method**

- Write linux-boot_edp.img

|   Write the image with AndroidTool_Release_v2.35.

- Test

|   Power on, EDP has display image

- Modify the resolution

|   To modify the resolution, modify arch/arm/boot/dts/lcd-EDP1080p.dtsi.