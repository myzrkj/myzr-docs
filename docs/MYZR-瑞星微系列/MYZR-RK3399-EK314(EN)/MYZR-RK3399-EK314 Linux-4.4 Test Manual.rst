
MYZR-RK3399-EK314 Linux-4.4 Test Manual
========================================

Part 1 Test Instructions
--------------------------

|   Development board user name: myzr Password: myzr root User password: root

Part 2 Interface Test
----------------------

Ethernet test
~~~~~~~~~~~~~~

|   The MYZR-RK3399 evaluation board has a Gigabit Ethernet port.

+-------------------+--------------------+-------------------------+------------------+
| Evaluation model  | Interface Location | Interface Rate Standard | System Interface |
+===================+====================+=========================+==================+
| MYZR-RK3399-EK314 | P19                | 10/100/1000Mbps         | eth0             |
+-------------------+--------------------+-------------------------+------------------+

**Test operation**

|   Configure the computer's wired network card IP to 192.168.18.18
|   Connect this network port of the development board to the computer network port with a network cable. 
|   Configure the development board network port:

.. code-block:: shell

    =====> Input:
    ifconfig eth0 192.168.18.36

**Test network port**

.. code-block:: shell

    =====> Input:
    ping 192.168.18.18 -c 2 -w 4
    =====> Output:
    --- 192.168.18.18 ping statistics --- 
    2packets transmitted, 2 packets received, 0% packet loss

**Test Results**

|   “0% packet loss” Indicates that the test has passed。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.1.png
   :alt: My-rk3399-ek314_test2.1.1.png

USB interface test
~~~~~~~~~~~~~~~~~~~

+-------------------+--------------------+----------------+
| Evaluation model  | Interface Location | Interface Type |
+===================+====================+================+
| MYZR-RK3399-EK314 | P8                 | USB3.0         |
+-------------------+--------------------+----------------+

**Test Methods**
|   Plug the USB device into the USB interface of the backplane and enter the following command:

.. code-block:: shell
    
    ＃ df -h

|   Unplug the USB device from the backplane and enter the following command:

.. code-block:: shell
    
    ＃ df -h

**Test Results**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.2.png
   :alt: My-rk3399-ek314_test2.1.2.png

SD interface test
~~~~~~~~~~~~~~~~~~~

+-------------------+--------------------+----------------+
| Evaluation model  | Interface Location | Interface Type |
+===================+====================+================+
| MYZR-RK3399-EK314 | P15                | SD             |
+-------------------+--------------------+----------------+

**Test Methods**

|   Insert the device into the SD card slot, insert the SD card into the SD card interface on the backplane, and enter the following command:

.. code-block:: shell
    
    ＃ df -h

|   After the SD card pops out, dial out the SD card to end the test.

**Test Results**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.3.png
   :alt: My-rk3399-ek314_test2.1.3.png

Standard GPIO test
~~~~~~~~~~~~~~~~~~~

+---------------------+------------+-----------------+------------------+
|  Evaluation model   | GPIO label | GPIO attributes | IO serial number |
+=====================+============+=================+==================+
| MYZR-RK3399-EK314   | P21-3      | GPIO1_B0        | 40               |
+                     +------------+-----------------+------------------+
|                     | P21-5      | GPIO1_A7        | 39               |
+                     +------------+-----------------+------------------+
|                     | P21-7      | GPIO1_B2        | 42               |
+                     +------------+-----------------+------------------+
|                     | P21-9      | GPIO1_B1        | 41               |
+                     +------------+-----------------+------------------+
|                     | P5-3       | GPIO1_A7        | 92               |
+                     +------------+-----------------+------------------+
|                     | P5-4       | GPIO1_C6        | 54               |
+                     +------------+-----------------+------------------+
|                     | P5-5       | GPIO1_C7        | 55               |
+                     +------------+-----------------+------------------+
|                     | P5-6       | GPIO2_D3        | 91               |
+                     +------------+-----------------+------------------+
|                     | P5-7       | GPIO4_D0        | 152              |
+                     +------------+-----------------+------------------+
|                     | P5-8       | GPIO4_C6        | 150              |
+---------------------+------------+-----------------+------------------+

**GPIO output test**

|   Configure P8-3 to output high and low level operation methods:

.. code-block:: shell
    
    =====> Input:
    ＃ OUT_IO_NUMBER=92
    Export GPIO
    ＃ echo ${OUT_IO_NUMBER} > /sys/class/gpio/export
    Set GPIO direction
    ＃ echo out > /sys/class/gpio/gpio${OUT_IO_NUMBER}/direction
    Controlling the output level
    ＃ echo 0 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value
    ＃ echo 1 > /sys/class/gpio/gpio${OUT_IO_NUMBER}/value

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.4.png
   :alt: My-rk3399-ek314_test2.1.4.png

|   Test pin P8-3 with a multimeter

**GPIO input test**

|   configure P8-3 input:

.. code-block:: shell
    
    Set the IO number of the GPIO to be tested
    ＃ IN_IO_NUMBER=91
    Export GPIO
    ＃ echo ${IN_IO_NUMBER} > /sys/class/gpio/export
    Set GPIO direction
    ＃ echo in > /sys/class/gpio/gpio${IN_IO_NUMBER}/direction
    View input level
    cat /sys/class/gpio/gpio${IN_IO_NUMBER}/value

ADC-KEY test
~~~~~~~~~~~~~~

+---------------------+--------------------+-----------+---------------+
|  Evaluation model   | Interface Location | Attribute | KEY attribute |
+=====================+====================+===========+===============+
| MYZR-RK3399-EK314   | SW5                | adc-keys  | Volume UP     |
+                     +--------------------+-----------+---------------+
|                     | SW4                | adc-keys  | Volume Down   |
+                     +--------------------+-----------+---------------+
|                     | SW3                | adc-keys  | Home          |
+                     +--------------------+-----------+---------------+
|                     | SW2                | adc-keys  | Esc           |
+                     +--------------------+-----------+---------------+
|                     | SW1                | adc-keys  | Menu          |
+---------------------+--------------------+-----------+---------------+

**Test operation**

|   Install evtest

.. code-block:: shell
    
    =====> Input:
    $ sudo apt-get install evtest

|   Run evtest to prepare the test

.. code-block:: shell
    
    =====> Input:
    evtest 
    　　Select test equipment
    Select the device event number [0-2]: 1
    Enter the serial number corresponding to "adc-keys", here is 1

    　　Press the button on the development board

**Test Results**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.5.png
   :alt: My-rk3399-ek314_test2.1.5.png

**End Test**

|   Press "Ctrl" + "C" on the computer to end the key test program.

RTC Test
~~~~~~~~~

**test introduction**

.. code-block:: shell
    
    Affected by express shipping, the MYZR-RK3399-EK314 series evaluation board is shipped without batteries. Please prepare your own coin-cell battery and install it on the evaluation board before testing the RTC. The battery holder of MYZR-RK3399-EK314 is in the "BT1" position on the back of the bottom plate.

**Test operation**

1. Power off and restart the device to view the current system time and hardware time:

.. code-block:: shell
    
    =====> Input: 
    date

    =====> Output：
    Thu Aug 6 05:35:17 UTC 2012

2. View the current RTC chip clock:

.. code-block:: shell
    
    =====> Input: 
    hwclock 

    =====> Output： 
    Thu Aug 6 05:35:59 2012 0.000000 seconds

3. Set the system clock and synchronize to the RTC chip

.. code-block:: shell
    
    =====> 输入指令: 
    date -s "2019-07-04 12:30:30"

4. Write system clock to hardware clock

.. code-block:: shell
    
    =====> Input:
    hwclock -w  

**Test Results**

|   The clock you see after step 3 is the newly set clock.

Audio playback test
~~~~~~~~~~~~~~~~~~~~

**test introduction**

|   This test verifies the audio capabilities of the evaluation board by playing audio files.

**Test operation**

|   Connect the audio output device to the audio socket on the front of the baseboard. The audio socket is on the front of the baseboard. "P6".
|   Execute the test command:

.. code-block:: shell
    
    =====> Input:
    ＃aplay /usr/share/sounds/alsa/Rear_Left.wav 

**Test Results**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.6.png
   :alt: My-rk3399-ek314_test2.1.6.png

Part III Display Function Test
--------------------------------

**test introduction**

|   Connect the EDP display.

**Test Methods**

|   Flash boot_edp.img
|   Flash with AndroidTool_Release_v2.58.

**Test Results**

|   Power on, EDP display image


Part IV Demonstration of Expansion Module Functions
-----------------------------------------------------

WIFI module test
~~~~~~~~~~~~~~~~~~

|   The model of WIFI chip used by MYZR-RK3399-EK314 evaluation board is AP6354

**Test operation**

1. Click on the network settings icon in the upper right corner of the screen and a list of networks will pop up
2. Select the wifi you want to connect and click
3. Enter the wifi password in the pop-up window and click Connect

Bluetooth module test
~~~~~~~~~~~~~~~~~~~~~~

|   The model of Bluetooth chip used by MYZR-RK3399-EK314 evaluation board is AP6354

**Test operation**

1. Click the Bluetooth icon in the upper right corner of the screen, and then click the Devices option in the pop-up list.   
2. Click “Search” in the pop-up window to start searching for Bluetooth.

4G Module Test
~~~~~~~~~~~~~~~

|   Test the internet 4G module, such as L506.

**Test operation**

.. code-block:: shell
    
    Install wvdial
    =====> Input:
    sudo apt-get install wvdial

    Modify the configuration file /etc/wvdial.conf
    =====> Input:
    ＃ vim /etc/wvdial.conf  

        Add the following:  
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

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.7.png
   :alt: My-rk3399-ek314_test2.1.7.png

|   dial

.. code-block:: shell
    
    =====> Input:
    #wvdial & 

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3399-EK314/My-rk3399-ek314_test2.1.8.png
   :alt: My-rk3399-ek314_test2.1.8.png