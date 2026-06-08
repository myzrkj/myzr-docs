Test Manual
=============

Test Overview
---------------

+---------------+-------------+--+---------------+-------------+--+---------------+-------------+
|   Test Item   | Test Result |  |   Test Item   | Test Result |  |   Test Item   | Test Result |
+===============+=============+==+===============+=============+==+===============+=============+
| Indicator     | Pass        |  | Reset Key     | Pass        |  | Function Key  | Pass        |
+---------------+-------------+  +---------------+-------------+  +---------------+-------------+
| Ethernet Port | Pass        |  | I2C           | Pass        |  | UART          | Pass        |
+---------------+-------------+  +---------------+-------------+  +---------------+-------------+
| GPIO          | Pass        |  | SPI           | Pass        |  | Audio         | Pass        |
+---------------+-------------+  +---------------+-------------+  +---------------+-------------+
| TF Card       | Pass        |  | USB           | Pass        |  | HDMI          | Pass        |
+---------------+-------------+--+---------------+-------------+--+---------------+-------------+


Device Information
---------------------

**Hardware Version**

+ **Core Board**: MYZR_IMX8MQ_CB300_RevD
+ **Main Board**: MYZR_IMX8MQ_MB300_RevE


**Software Version**

+ **image**: Image-4.14.98-g8390a69729ee
+ **fdt_file**: myimx8mek300-8mq-tm-4.14.98-g8390a69729ee.dtb
+ **kernel-modules**: kernel-modules-4.14.98-g8390a69729ee.tar.bz2


Indicator
-----------

+ Silkscreen Label: D7

**Function Test**

  1) Description: D7 is used to indicate the power status of the main board.

  2) Operation: Power on the device, D7 lights up. Power off the device, D7 turns off.

  3) Result: The indicator status corresponds correctly with operation, function is normal.


Reset Key
-----------

+ Silkscreen Label: SW2

**Function Test**

  1) Description: Short pressing the reset key can perform device power reset.

  2) Operation: With main board power on, short press the reset key to trigger device power reset.
  
  3) Result: Pressing and releasing the reset key triggers main board reboot, function is normal.


CPU Temperature
-----------------

+ System Interface: /sys/class/thermal/thermal_zone0/temp

**Function Test**

  1) Description: The system supports reading CPU temperature sensor data.

  2) Operation
  
    + Input command:
  
    .. code-block:: shell

       cat /sys/class/thermal/thermal_zone0/temp
  
    + Output information:
  
    .. code-block:: text

       58000

    .. note:: The output value divided by 1000 equals the Celsius temperature
  
  3) Result: Normal output after executing the command, function is normal.


Function Key
---------------

+ Silkscreen Label: SW6, SW8, SW9, SW10
+ System Interface: /dev/input/event2

**Function Test**

  1) Description: Test with evtest tool.

  2) Operation
    a) Run the test tool with command:

    + Input command:
  
    .. code-block:: shell

      evtest /dev/input/event2
  
    + Output information (key values registered by 4 keys can be seen):
  
    .. code-block:: text

       Input driver version is 1.0.1
       Input device ID: bus 0x19 vendor 0x1 product 0x1 version 0x100
       Input device name: "gpio-keys"
       Supported events:
         Event type 0 (EV_SYN)
         Event type 1 (EV_KEY)
           Event code 106 (KEY_RIGHT)
           Event code 108 (KEY_DOWN)
           Event code 109 (KEY_PAGEDOWN)
           Event code 110 (KEY_INSERT)
       Properties:
       Testing ... (interrupt to exit)  

    b) Press SW6, SW8, SW9, SW10 respectively.

    + The following information can be observed:

    .. code-block:: text

       Event: time 1550694816.550833, type 1 (EV_KEY), code 106 (KEY_RIGHT), value 1
       Event: time 1550694816.550833, -------------- SYN_REPORT ------------
       Event: time 1550694816.746817, type 1 (EV_KEY), code 106 (KEY_RIGHT), value 0
       Event: time 1550694816.746817, -------------- SYN_REPORT ------------
       Event: time 1550694820.171340, type 1 (EV_KEY), code 108 (KEY_DOWN), value 1
       Event: time 1550694820.171340, -------------- SYN_REPORT ------------
       Event: time 1550694820.442814, type 1 (EV_KEY), code 108 (KEY_DOWN), value 0
       Event: time 1550694820.442814, -------------- SYN_REPORT ------------
       Event: time 1550694822.090817, type 1 (EV_KEY), code 109 (KEY_PAGEDOWN), value 1
       Event: time 1550694822.090817, -------------- SYN_REPORT ------------
       Event: time 1550694822.326761, type 1 (EV_KEY), code 109 (KEY_PAGEDOWN), value 0
       Event: time 1550694822.326761, -------------- SYN_REPORT ------------
       Event: time 1550694823.898812, type 1 (EV_KEY), code 110 (KEY_INSERT), value 1
       Event: time 1550694823.898812, -------------- SYN_REPORT ------------
       Event: time 1550694824.146815, type 1 (EV_KEY), code 110 (KEY_INSERT), value 0
       Event: time 1550694824.146815, -------------- SYN_REPORT ------------

  .. note:: Press Ctrl + C to exit the test.

  3) Result: The output matches expected result during operation, function is normal.


Ethernet Port
---------------

  + Silkscreen Label: J16
  + System Interface: eth0

**Function Test**
  
  1) Description: Test by sending ICMP packets from the device to PC.

  2) Operation

    a) Set PC wired network adapter IP to 192.168.137.99.

    b) Connect the Ethernet port of the development board to PC network port with network cable.

    c) Configure development board Ethernet port IP with the following commands:

    .. code-block:: shell

      ifconfig eth0 up
      ifconfig eth0 192.168.137.81

    d) Execute Ethernet port test command

    + Input command:

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4 

    + Output information:

    .. code-block:: text

      PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
      64 bytes from 192.168.137.99: icmp_seq-1 ttl-64 time-1.43 ms
      64 bytes from 192.168.137.99: icmp_seq-2 ttl-64 time-1.53 ms

      --- 192.168.137.99 ping statistics ---
      2 packets transmitted, 2 received, 0% packet loss, time 1002ms
      rtt min/avg/max/mdev - 1.437/1.487/1.538/0.063 ms

  3) Result: "0% packet loss" indicates test passed.


I2C
-----

**Function Test**

  1) Description: Execute I2C detection command and observe result.

  2) Operation
  
    a) Detect system I2C bus

    + Input command:

    .. code-block:: shell

        i2cdetect -l

    + Similar output as below indicates I2C 0, 1, 2 and HDMI adapter are detected.

    .. code-block:: text

       i2c-1	i2c       	30a30000.i2c                    	I2C adapter
       i2c-2	i2c       	30a40000.i2c                    	I2C adapter
       i2c-0	i2c       	30a20000.i2c                    	I2C adapter
      
    b) Detect I2C devices on the bus

    + Input command:
    
    .. code-block:: shell

      i2cdetect -y 2

    .. note:: The parameter 2 in i2cdetect can be the bus number obtained in previous step, such as 0, 1.

    + Similar output as below; non "--" means device detected at corresponding I2C bus address.

    .. code-block:: text

           0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
      00:                         -- -- -- -- -- -- -- -- 
      10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
      20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
      30: -- -- -- -- -- -- -- -- UU -- -- -- -- -- -- -- 
      40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
      50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
      60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 6f 
      70: -- -- -- -- -- -- -- --                         

  3) Result: The output is basically consistent with expectation, function is normal.


UART
------

+--------------------+--------------+-------------------+------------------+--------------------+
| Interface Location | Pin Location | Pin Configuration | System Interface | Interface Function |
+--------------------+--------------+-------------------+------------------+--------------------+
| J21                | P3:3         | UART1_TXD         | /dev/ttymxc0     | Debug UART         |
+                    +--------------+-------------------+                  +                    +
|                    | P3:2         | UART1_RXD         |                  |                    |
+--------------------+--------------+-------------------+------------------+--------------------+
| J20                | P4:3         | UART2_TXD         |                  | MCU UART           |
+                    +--------------+-------------------+                  +                    +
|                    | P4:2         | UART2_RXD         |                  |                    |
+--------------------+--------------+-------------------+------------------+--------------------+

+--------------------+-------------------+------------------+
| Interface Location | Pin Configuration | System Interface |
+--------------------+-------------------+------------------+
| P22:35             | UART3_RXD         | /dev/ttymxc2     |
+--------------------+-------------------+                  +
| P22:37             | UART3_TXD         |                  |
+--------------------+-------------------+------------------+
| J17:1              | RS232_RX1         | /dev/ttyXRUSB0   |
+--------------------+-------------------+                  +
| J17:3              | RS232_TX1         |                  |
+--------------------+-------------------+------------------+
| J17:2              | RS232_RX2         | /dev/ttyXRUSB1   |
+--------------------+-------------------+                  +
| J17:4              | RS232_TX2         |                  |
+--------------------+-------------------+------------------+
| P21:2              | UART4_RXD         | /dev/ttymxc3     |
+--------------------+-------------------+                  +
| P21:4              | UART4_TXD         |                  |
+--------------------+-------------------+------------------+
| J17:7              | RS485_A1          | /dev/ttyXRUSB2   |
+--------------------+-------------------+                  +
| J17:9              | RS485_B1          |                  |
+--------------------+-------------------+------------------+
| J17:8              | RS485_A2          | /dev/ttyXRUSB3   |
+--------------------+-------------------+                  +
| J17:10             | RS485_B2          |                  |
+--------------------+-------------------+------------------+


**Function Test**

  1) Description: Test by UART loopback mode.

  2) Operation

    a) Connect P22:35 and P22:37 with DuPont line.

    b) Run test program:

    + Input command:
  
    .. code-block:: shell

      /my-demo/serial_test_arm64.out /dev/ttymxc2 "www.myzr.com.cn"

    + Output information:

    .. code-block:: text

       Starting send data...finish
       Starting receive data:
       ASCII: 0x77 	 Character: w 
       ASCII: 0x77 	 Character: w 
       ASCII: 0x77 	 Character: w 
       ASCII: 0x2e 	 Character: . 
       ASCII: 0x6d 	 Character: m 
       ASCII: 0x79 	 Character: y 
       ASCII: 0x7a 	 Character: z 
       ASCII: 0x72 	 Character: r 
       ASCII: 0x2e 	 Character: . 
       ASCII: 0x63 	 Character: c 
       ASCII: 0x6f 	 Character: o 
       ASCII: 0x6d 	 Character: m 
       ASCII: 0x2e 	 Character: . 
       ASCII: 0x63 	 Character: c 
       ASCII: 0x6e 	 Character: n 
       ASCII: 0x0 	 Character:  

  3) Result: Received data matches input content after test execution, function is normal.


GPIO
------

+--------------+-------------------+-----------+
| Pin Location | Pin Configuration | IO Number |
+--------------+-------------------+-----------+
| P21:16       | GPIO4_IO22        | 118       |
+--------------+-------------------+-----------+
| P21:31       | GPIO1_IO0         | 32        |
+--------------+-------------------+-----------+
| P22:38       | GPIO5_IO1         | 129       |
+--------------+-------------------+-----------+
| P22:40       | GPIO4_IO30        | 126       |
+--------------+-------------------+-----------+

**Function Test**

+ GPIO Output Test

  1) Description: Control GPIO output level via system interface.

  2) Operation

    a) Export IO control interface and set as output:

    .. code-block:: shell

      export OUT_IO_OUT_NUM=129
      echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
      echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction

    b) Set IO output high level:

    .. code-block:: shell

       echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

    .. note:: Measure corresponding pin with multimeter, voltage shall be 3.3V.

    c) Set IO output low level:

    .. code-block:: shell

       echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

    .. note:: Measure J13:16 with multimeter, voltage shall be 0V.

  3) Result: Measured voltage matches expectation when controlling IO level, function is normal.


+ GPIO Input Test

  1) Description: Configure and read GPIO input level via system interface.

  2) Operation
  
    a) Connect pin 38 and 40 of P22 with DuPont line or jumper cap.

    b) Export IO control interface and set as input:

    .. code-block:: shell

       export OUT_IO_IN_NUM=126
       echo ${OUT_IO_IN_NUM} > /sys/class/gpio/export
       echo "in" > /sys/class/gpio/gpio${OUT_IO_IN_NUM}/direction

    c) Set P22:38 output high level and read P22:40 input level:

    .. code-block:: shell

       # Control P22:38 IO output high level
       echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
       # Read IO input level
       cat /sys/class/gpio/gpio${OUT_IO_IN_NUM}/value

    .. note:: The terminal shall output character "1" (indicates high level).

    d) Set P22:38 output low level and read P22:40 input level:

    .. code-block:: shell

       # Control P22:38 IO output low level
       echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
       # Read IO input level
       cat /sys/class/gpio/gpio${OUT_IO_IN_NUM}/value

    .. note:: The terminal shall output character "0" (indicates low level).

  3) Result: Read level matches expected value during test, function is normal.


SPI
-----

+--------------+-------------------+------------------+
| Pin Location | Pin Configuration | System Interface |
+--------------+-------------------+------------------+
| P22:27       | SPI1_SCLK         | /dev/spidev0.0   |
+--------------+-------------------+                  +
| P22:29       | SPI1_MISO         |                  |
+--------------+-------------------+                  +
| P22:31       | SPI1_MOSI         |                  |
+--------------+-------------------+                  +
| P22:33       | SPI1_SS           |                  |
+--------------+-------------------+------------------+
| P22:19       | SPI2_SCLK         | /dev/spidev1.0   |
+--------------+-------------------+                  +
| P22:21       | SPI2_MISO         |                  |
+--------------+-------------------+                  +
| P22:23       | SPI2_MOSI         |                  |
+--------------+-------------------+                  +
| P22:25       | SPI2_SS           |                  |
+--------------+-------------------+------------------+

**Function Test**

  1) Description: Send string via SPI interface.

  .. note:: The spidev_test.c test program is located at kernel source code tools/spi/ directory and can be compiled manually.

  2) Operation

  + Connect SPI MISO and MOSI with jumper cap.

  + Run test program with command:

  .. code-block:: shell

     /my-demo/spidev_test -D /dev/spidev0.0 -v -p my_spi_test_string

  .. note:: "my_spi_test_string" is the string sent through SPI.

  + Similar output as below can be observed:

  .. code-block:: text

      spi mode: 0x0
      bits per word: 8
      max speed: 500000 Hz (500 KHz)
      TX | 6D 79 5F 73 70 69 5F 74 65 73 74 5F 73 74 72 69 6E 67 __ __ __ __ __ __ __ __ __ __ __ __ __ __  | my_spi_test_string
      RX | 6D 79 5F 73 70 69 5F 74 65 73 74 5F 73 74 72 69 6E 67 __ __ __ __ __ __ __ __ __ __ __ __ __ __  | my_spi_test_string

  3) Result: Output matches expected content, transmission successful.


Audio
-------

+ System Interface: wm8524-audio

**Function Test**

  1) Description: Test by playing audio file.

  2) Operation

    a) Insert earphone or speaker to the interface corresponding to silkscreen P1.

    b) Execute test command:

    .. code-block:: shell

      aplay /unit_tests/ASRC/audio8k16S.wav

  3) Result: Sound can be heard from earphone after executing command, function is normal.


TF Card
----------

+ Silkscreen Label: J5

**Function Test**

  .. note:: The device TF card interface supports hot plugging with pop-up TF card slot.

+ TF Card Insertion Test

  1) Description: Insert TF card and check if device can recognize it correctly.

  2) Operation
    
    a) Insert a TF card into device TF card interface.

    b) Similar output as below:

    .. code-block:: text

       ...
       mmc1: new high speed SDHC card at address 0001
       mmcblk1: mmc1:0001 TF 4G 3.68 GiB 
       ...

  3) Result: Output matches expectation, TF card recognized correctly.


+ TF Card Ejection Test

  1) Eject TF card and check device response.

  2) Operation
  
    a) Press the TF card inward in insertion direction (release after clicking sound, TF card will pop out automatically).

    b) Similar output as below:

    .. code-block:: text

      ...
      mmc1: card 0001 removed
      ...

  3) Result: Device response matches expectation, TF card hot plug function normal.


USB
------

+ Silkscreen Label: J18

**Function Test**

+ USB Device Recognition

  1) Description: Insert USB flash drive and check device response.

  2) Operation:

    a) Insert a USB flash drive into device USB interface.

    b) Similar output as below:

    .. code-block:: text

       ...
       usb 1-1.2: new high-speed USB device number 4 using xhci-hcd
       usb-storage 1-1.2:1.0: USB Mass Storage device detected
       scsi host0: usb-storage 1-1.2:1.0
       ...

  3) Result: Output matches expectation, USB flash drive recognized correctly.


+ USB Flash Drive Removal Test

  1) Remove USB flash drive and check device response.

  2) Operation: Remove USB flash drive, similar output as below can be seen:

    .. code-block:: text

      ...
      usb 1-1.2: USB disconnect, device number 4
      ...

  3) Result: Device response matches expectation, USB removal detection normal.


HDMI
------

+ Silkscreen Label: J11

**Function Test**

  1) Description: The device can detect and enable HDMI display device; adapter conversion (such as HDMI to VGA) is not supported.

  2) Operation: Connect HDMI display screen and power cycle the device.

  3) Result: HDMI display screen outputs content during device startup, function is normal.
