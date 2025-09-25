Test Manual
=============

Test Overview 
---------------

+-----------------+-------------+-----+--------------+-------------+-----+-----------------+-------------+
|    Test Item    | Test Result |     |  Test Item   | Test Result |     |    Test Item    | Test Result |
+=================+=============+=====+==============+=============+=====+=================+=============+
| Indicator Light | Pass        |     | Reset Button | Pass        |     | Function Button | Pass        |
+-----------------+-------------+-----+--------------+-------------+-----+-----------------+-------------+
| Network Port    | Pass        |     | I2C          | Pass        |     | UART            | Pass        |
+-----------------+-------------+-----+--------------+-------------+-----+-----------------+-------------+
| GPIO            | Pass        |     | SPI          | Pass        |     | Audio           | Pass        |
+-----------------+-------------+-----+--------------+-------------+-----+-----------------+-------------+
| TF Card         | Pass        |     | USB          | Pass        |     | HDMI            | Pass        |
+-----------------+-------------+-----+--------------+-------------+-----+-----------------+-------------+


Device Information
--------------------

**Hardware Version**

- **Core Board**: MYZR_IMX8MM_CB200_RevA
- **Motherboard**: MYZR_IMX8MM_MB200_RevA

**Software Version**

- **image**: Image-4.14.98-g8390a69729ee
- **fdt_file**: myimx8mek300-8mq-tm-4.14.98-g8390a69729ee.dtb
- **kernel-modules**: kernel-modules-4.14.98-g8390a69729ee.tar.bz2

Indicator Light
------------------

- Interface Silkscreen: D7

**Function Test**

  1) Description: D7 is used to indicate the power status of the motherboard.

  2) Operation: Power on the device, D7 lights up. Power off the device, D7 turns off.

  3) Result: During operation, the status of the indicator light corresponds correctly, indicating normal function.


Reset Button
---------------

- Interface Silkscreen: SW2

**Function Test**

  1) Description: Short-pressing the reset button can reset the device power.

  2) Operation: When the motherboard power is on, short-press the reset button to reset the device power.
  
  3) Result: When the reset button is pressed and released, the motherboard restarts, indicating normal function.


CPU Temperature
------------------

- System Interface: /sys/class/thermal/thermal_zone0/temp

**Function Test**

  1) Description: The system supports reading data from the CPU temperature sensor.

  2) Operation
  
    - Enter the command:
  
    .. code-block:: shell

       cat /sys/class/thermal/thermal_zone0/temp
  
    - Output information:
  
    .. code-block:: text

       58000

    .. note:: Divide the output value by 1000 to get the temperature in Celsius.
  
  3) Result: After entering the command, the output information is normal, indicating normal function.


Function Button
------------------

- Interface Silkscreen: SW6, SW8, SW9, SW10
- System Interface: /dev/input/event2

**Function Test**

  1) Description: Use the evtest tool for testing.

  2) Operation

    a) Enter the command to run the test tool:

    - Enter the command:
  
    .. code-block:: shell

      evtest /dev/input/event2
  
    - Output information (the key values registered by the 4 buttons can be seen):
  
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

    - The following information can be seen:

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

  3) Result: The output information during operation meets the correct expectations, indicating normal function.


Network Port
--------------

  - Interface Silkscreen: J16
  - System Interface: eth0

**Function Test**
  
  1) Description: Test by sending ICMP packets from the device to the PC.

  2) Operation

    a) Configure the PC's wired network card IP to 192.168.137.99.

    b) Connect the network port of the development board to the PC's network port with a network cable.

    c) Configure the development board's network port IP, the specific configuration commands are as follows:

    .. code-block:: shell

      ifconfig eth0 up
      ifconfig eth0 192.168.137.81

    d) Execute the network port test command

    - Enter the command:

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4 

    - Output information:

    .. code-block:: text

      PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
      64 bytes from 192.168.137.99: icmp_seq-1 ttl-64 time-1.43 ms
      64 bytes from 192.168.137.99: icmp_seq-2 ttl-64 time-1.53 ms

      --- 192.168.137.99 ping statistics ---
      2 packets transmitted, 2 received, 0% packet loss, time 1002ms
      rtt min/avg/max/mdev - 1.437/1.487/1.538/0.063 ms

  3) Result: "0% packet loss" indicates the test is passed.


I2C
-----

**Function Test**

  1) Description: Execute the I2C detection command and observe the result.

  2) Operation
  
    a) Detect the I2C bus of the system

    - Enter the command:

    .. code-block:: shell

        i2cdetect -l

    - The output information is similar to the following, indicating that adapters for I2C 0, 1, 2 and HDMI are detected.

    .. code-block:: text

       i2c-1	i2c       	30a30000.i2c                    	I2C adapter
       i2c-2	i2c       	30a40000.i2c                    	I2C adapter
       i2c-0	i2c       	30a20000.i2c                    	I2C adapter
      
    b) Detect I2C devices on the bus

    - Enter the command:
    
    .. code-block:: shell

      i2cdetect -y 2

    .. note:: The parameter 2 in i2cdetect can be the bus number detected in the previous step, such as 0 or 1.

    - The output has information similar to the following; non "--" indicates that a device is detected at the corresponding address on the I2C bus.

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

  3) Result: The output information during the operation process is basically consistent with the expectation, indicating normal function.


UART
------

+--------------------+-------------------+------------------+-----+--------------------+-------------------+------------------+
| Interface Location | Pin Configuration | System Interface |     | Interface Location | Pin Configuration | System Interface |
+--------------------+-------------------+------------------+     +--------------------+-------------------+------------------+
| J12:4              | UART1_RXD         | /dev/ttymxc0     |     | P2:4               | UART2_TXD         | /dev/ttymxc1     |
+--------------------+-------------------+                  +     +--------------------+-------------------+                  +
| J12:5              | UART1_TXD         |                  |     | P2:5               | UART2_RXD         |                  |
+--------------------+-------------------+------------------+     +--------------------+-------------------+------------------+
| J12:1              | UART3_RXD         | /dev/ttymxc2     |     | P2:1               | UART4_RXD         | /dev/ttymxc3     |
+--------------------+-------------------+                  +     +--------------------+-------------------+                  +
| J12:2              | UART3_TXD         |                  |     | P2:2               | UART4_TXD         |                  |
+--------------------+-------------------+------------------+-----+--------------------+-------------------+------------------+

**Function Test**

  1) Description: Test using the UART self-transmit and self-receive method.

  2) Operation

    a) Use a Dupont wire to connect P22:35 and P22:37.

    b) Run the test program:

    - Enter the command:
  
    .. code-block:: shell

      ./serial_test_arm64.out /dev/ttymxc2 "www.myzr.com.cn"

    - Output information:

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

  3) Result: After executing the test operation, the input information meets the correct expectations, indicating normal function.


GPIO
------

+--------------+-------------------+-----------+-----+--------------+-------------------+-----------+
| Pin Position | Pin Configuration | IO Number |     | Pin Position | Pin Configuration | IO Number |
+--------------+-------------------+-----------+     +--------------+-------------------+-----------+
| P21:16       | GPIO4_IO22        | 118       |     | P22:38       | GPIO5_IO1         | 129       |
+--------------+-------------------+-----------+     +--------------+-------------------+-----------+
| P21:31       | GPIO1_IO0         | 32        |     | P22:40       | GPIO4_IO30        | 126       |
+--------------+-------------------+-----------+-----+--------------+-------------------+-----------+

**Functional Test**

+ GPIO Output Test

  1) Description: Control the output level of GPIO through the system interface.

  2) Operations

    a) Enter commands to export the IO operation interface and configure it as output:

    .. code-block:: shell

      export OUT_IO_OUT_NUM-129
      echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
      echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction

    b) Enter commands to control the IO to output high level:

    .. code-block:: shell

       echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

    .. note:: At this time, using a multimeter to test the corresponding pin, the voltage should be 3.3V.

    c) Control the IO to output low level:

    .. code-block:: shell

       echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

    .. note:: At this time, using a multimeter to test J13:16, the voltage should be 3.3V.

  3) Result: During the test operation, when controlling the IO level, the measured voltage is consistent with the expected value, which means it is normal.

+ GPIO Input Test

  1) Description: Configure and read the input level of GPIO through the system interface.

  2) Operations
  
    a) Use a Dupont wire or jumper cap to connect pins 38 and 40 of P22.

    b) Enter commands to export the IO operation interface and configure it as input:

    .. code-block:: shell

       export OUT_IO_IN_NUM-126
       echo ${OUT_IO_IN_NUM} > /sys/class/gpio/export
       echo "in" > /sys/class/gpio/gpio${OUT_IO_IN_NUM}/direction

    c) Enter commands to control P22:38 to output high level and read the input level of P22:40:

    .. code-block:: shell

       # Note: Control P22:38 IO to output high level
       echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
       # Note: Read the input level of IO
       cat /sys/class/gpio/gpio${OUT_IO_IN_NUM}/value

    .. note:: At this time, the command line interface terminal should output the character "1" (indicating high level).

    d) Enter commands to control P22:38 to output low level and read the input level of P22:40:

    .. code-block:: shell

       # Note: Control P22:38 IO to output low level
       echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
       # Note: Read the input level of IO
       cat /sys/class/gpio/gpio${OUT_IO_IN_NUM}/value

    .. note:: At this time, the command line interface terminal should output the character "0" (indicating low level).

  3) Result: During the test operation, the read level meets the correct expectations, indicating that the function is normal.


SPI
------

+--------------+-------------------+------------------+-----+--------------+-------------------+------------------+
| Pin Position | Pin Configuration | System Interface |     | Pin Position | Pin Configuration | System Interface |
+--------------+-------------------+------------------+-----+--------------+-------------------+------------------+
| P22:27       | SPI1_SCLK         | /dev/spidev0.0   |     | P22:19       | SPI2_SCLK         | /dev/spidev1.0   |
+--------------+-------------------+                  +     +--------------+-------------------+------------------+
| P22:29       | SPI1_MISO         |                  |     | P22:21       | SPI2_MISO         | packet           |
+--------------+-------------------+                  +     +--------------+-------------------+                  +
| P22:31       | SPI1_MOSI         |                  |     | P22:23       | SPI2_MOSI         |                  |
+--------------+-------------------+                  +     +--------------+-------------------+                  +
| P22:33       | SPI1_SS           |                  |     | P22:25       | SPI2_SS           |                  |
+--------------+-------------------+------------------+-----+--------------+-------------------+------------------+

**Functional Test**

  1) Description: Send strings through the SPI interface.

  .. note:: There is a spidev_test.c test program in the tools/spi/ directory of the kernel source code, which can be compiled by yourself.

  2) Operations

  + Use jumpers to connect SPI's MISO and MOSI

  + Enter commands to run the test program:

  .. code-block:: shell

     ./spidev_test -D /dev/spidev0.0 -v -p my_spi_test_string

  .. note:: "my_spi_test_string" is the string sent through spi.

  + You can see output information similar to the following:

  .. code-block:: text

      spi mode: 0x0
      bits per word: 8
      max speed: 500000 Hz (500 KHz)
      TX | 6D 79 5F 73 70 69 5F 74 65 73 74 5F 73 74 72 69 6E 67 __ __ __ __ __ __ __ __ __ __ __ __ __ __  | my_spi_test_string
      RX | 6D 79 5F 73 70 69 5F 74 65 73 74 5F 73 74 72 69 6E 67 __ __ __ __ __ __ __ __ __ __ __ __ __ __  | my_spi_test_string

  3) Result: The output information seen meets the correct expectations, indicating that the transmission is successful.

Audio
-------

+ System Interface: wm8524-audio

**Functional Test**

  1) Description: Play audio files for testing.

  2) Operations

    a) Insert headphones or speakers into the interface corresponding to the silk screen P1.

    b) Enter commands for testing:

    .. code-block:: shell

      aplay /unit_tests/ASRC/audio8k16S.wav

  3) Result: When executing the test command, if sound can be heard from the headphones, the function is normal.

TF Card
---------

+ Interface Silk Screen: J5

**Functional Test**

  .. note:: The TF card interface of the device supports hot swapping, and the TF card slot is self-ejecting.

+ TF Card Insertion Test

  1) Description: Insert the TF card and observe whether the device can correctly recognize the card.

  2) Operations
    
    a) Take a TF card and insert it into the TF card interface of the device.

    b) The output information is similar to the following:

    .. code-block:: text

       ...
       mmc1: new high speed SDHC card at address 0001
       mmcblk1: mmc1:0001 TF 4G 3.68 GiB 
       ...

  3) Result: The output information after the operation meets the correct expectations, indicating that the TF card is correctly recognized.

+ TF Card Ejection Test

  1) Eject the TF card and observe whether the device can respond correctly.

  2) Operations
  
    a) Press the TF card in the insertion direction (release when a "click" sound is heard, and the TF card will pop out).

    b) The output information is similar to the following:

    .. code-block:: text

      ...
      mmc1: card 0001 removed
      ...

  3) Result: The phenomenon during the operation meets the correct expectations, indicating that the TF hot swapping is normal.

USB
-----

+ Interface Silk Screen: J18

**Functional Test**

+ USB Device Recognition

  1) Description: Insert a USB flash drive and observe whether the device can respond correctly.

  2) Operations:

    a) Take a USB flash drive and insert it into the USB interface of the device.

    b) The output information is similar to the following:

    .. code-block:: text

       ...
       usb 1-1.2: new high-speed USB device number 4 using xhci-hcd
       usb-storage 1-1.2:1.0: USB Mass Storage device detected
       scsi host0: usb-storage 1-1.2:1.0
       ...

  3) Result: The output information after the operation meets the correct expectations, indicating that the USB flash drive is correctly recognized.

+ USB Flash Drive Removal Test

  1) Remove the USB flash drive and observe whether the device can respond correctly.

  2) Operations: Remove the USB flash drive, and you can see output information similar to the following:

    .. code-block:: text

      ...
      usb 1-1.2: USB disconnect, device number 4
      ...

  3) Result: The phenomenon during the operation meets the correct expectations, indicating that the USB flash drive is removed normally.

HDMI
------

+ Interface Silk Screen: J11

**Functional Test**

  1) Description: The device will recognize the HDMI display device and enable it. Adapters (such as HDMI to VGA) are not supported.

  2) Operations: Connect an HDMI display and power on the device again.

  3) Result: During the device startup process, if the HDMI display shows content, it indicates that the function is normal.


