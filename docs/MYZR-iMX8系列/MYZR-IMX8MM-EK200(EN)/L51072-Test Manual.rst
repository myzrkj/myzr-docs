Test Manual
=============

Test Overview 
---------------

+-----------------+-------------+--------------+-------------+-----------+-------------+
| Test Item       | Test Result | Test Item    | Test Result | Test Item | Test Result |
+-----------------+-------------+--------------+-------------+-----------+-------------+
| Indicator Light | Pass        | Reset Button | Pass        | USB       | Pass        |
+-----------------+-------------+--------------+-------------+-----------+-------------+
| Ethernet Port   | Pass        | I2C          | Pass        | UART      | Pass        |
+-----------------+-------------+--------------+-------------+-----------+-------------+
| GPIO            | Pass        | SPI          | Pass        | Audio     | Pass        |
+-----------------+-------------+--------------+-------------+-----------+-------------+
| TF Card         | Pass        | RTC          | Pass        | Watchdog  | Pass        |
+-----------------+-------------+--------------+-------------+-----------+-------------+


Device Information
--------------------

**Hardware Version**

- **Core Board**: MYZR_IMX8MM_CB200_RevB
- **Main Board**: MYZR_IMX8MM_MB200_RevB

**Software Version**

- **Image**: Image-5.10.72-492a823d1cf5a9f54f
- **fdt_file**: myimx8mmek200.dtb-492a823d1cf5a9f54f
- **kernel-modules**: kernel-modules.tar.bz2-492a823d1cf5a9f54f


Indicator Light
-----------------

  Interface Silkscreen: LED1, LED2, LED3

**Function Test**

  1) Description: LED1 is used to indicate the main board power status.

  2) Operation: Power on the device, LED1 turns on. Power off the device, LED1 turns off.

  3) Result: During operation, the indicator light status corresponds correctly, indicating normal function.


Reset Button
--------------

- Interface Silkscreen: SW2

**Function Test**

  1) Description: Short-pressing the reset button can reset the device power.

  2) Operation: When the main board power is on, short-press the reset button to reset the device power.
  
  3) Result: When the reset button is pressed and released, the main board restarts, indicating normal function.


CPU Temperature
-----------------

- System Interface: /sys/class/thermal/thermal_zone0/temp

**Function Test**

  1) Description: The system supports reading CPU temperature sensor data.

  2) Operation
  
    - Enter the command:
  
    .. code-block:: shell

       cat /sys/class/thermal/thermal_zone0/temp
  
    - Output information:
  
    .. code-block:: text

       58000

    .. note:: Divide the output value by 1000 to get the temperature in Celsius.
  
  3) Result: After entering the command, the output information is normal, indicating normal function.


Ethernet Port
----------------

  - Interface Silkscreen: U10
  - System Interface: eth0

**Function Test**
  
  1) Description: The test is performed by sending ICMP packets from the device to the PC.

  2) Operation

    a) Configure the PC's wired network card IP to 192.168.137.99.

    b) Connect the Ethernet port of the development board to the PC's Ethernet port using a network cable.

    c) Configure the development board's Ethernet port IP with the following specific configuration commands:

    .. code-block:: shell

      ifconfig eth0 up
      ifconfig eth0 192.168.137.81

    d) Execute the Ethernet port test command

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

  3) Result: "0% packet loss" indicates the test passed.


I2C
-----

**Function Test**

  1) Description: Execute the I2C detection command and observe the result.

  2) Operation
  
    a) Detect the I2C bus of the system

    - Enter the command:

    .. code-block:: shell

        i2cdetect -l

    - The output information is similar to the following, indicating that I2C 0, 1, 2 and HDMI adapters are detected.

    .. code-block:: text

       i2c-1	i2c       	30a30000.i2c                    	I2C adapter
       i2c-2	i2c       	30a40000.i2c                    	I2C adapter
       i2c-0	i2c       	30a20000.i2c                    	I2C adapter
      
    b) Detect I2C devices on the bus

    - Enter the command:
    
    .. code-block:: shell

      i2cdetect -y 2

    .. note:: The parameter 2 in i2cdetect can be the bus number detected in the previous step, such as 0 or 1.

    - The output is similar to the following information; non "--" indicates that a device is detected at the corresponding address on the I2C bus.

    .. code-block:: text

            0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
        00:                         -- -- -- -- -- -- -- -- 
        10: -- -- -- -- -- -- -- -- -- -- UU -- -- -- -- -- 
        20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
        60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- UU 
        70: -- -- -- -- -- -- -- --                           

  3) Result: The output information during the operation is basically consistent with the expected result, indicating normal function.


UART
------

+--------------------+--------------+-------------------+------------------+--------------------+
| Interface Location | Pin Location | Pin Configuration | System Interface | Interface Function |
+--------------------+--------------+-------------------+------------------+--------------------+
| P2                 | P2:4         | UART2_TXD         | /dev/ttymxc1     | Debug Serial Port  |
+                    +--------------+-------------------+                  +                    +
|                    | P2:5         | UART2_RXD         |                  |                    |
+--------------------+--------------+-------------------+------------------+--------------------+
| P2                 | P2:1         | UART4_TXD         | /dev/ttymxc3     | MCU Serial Port    |
+                    +--------------+-------------------+                  +                    +
|                    | P2:2         | UART4_RXD         |                  |                    |
+--------------------+--------------+-------------------+------------------+--------------------+
| J12                | J12:RX3      | UART3_RXD         | /dev/ttymxc2     | Serial Port        |
+                    +--------------+-------------------+                  +                    +
|                    | J12:TX3      | UART3_TXD         |                  |                    |
+--------------------+--------------+-------------------+------------------+--------------------+
| J12                | J12:A        | UART1_TXD         | /dev/ttymxc0     | Serial Port        |
+                    +--------------+-------------------+                  +                    +
|                    | J12:B        | UART1_RXD         |                  |                    |
+--------------------+--------------+-------------------+------------------+--------------------+

**Function Test**

  1) Description: The test is performed using the serial port's self-transmit and self-receive method.

  2) Operation

    a) Use a Dupont wire to connect J12:RX3 and J12:TX3.

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
| Pin Location | Pin Configuration | IO Number |     | Pin Location | Pin Configuration | IO Number |
+--------------+-------------------+-----------+-----+--------------+-------------------+-----------+
| J10:10       | GPIO4_IO23        | 119       |     | J10:18       | GPIO5_IO27        | 123       |
+--------------+-------------------+-----------+-----+--------------+-------------------+-----------+
| J10:12       | GPIO1_IO26        | 122       |     | J10:20       | GPIO4_IO28        | 124       |
+--------------+-------------------+-----------+-----+--------------+-------------------+-----------+
| J10:14       | GPIO1_IO24        | 120       |     | J10:22       | GPIO4_IO29        | 125       |
+--------------+-------------------+-----------+-----+--------------+-------------------+-----------+
| J10:18       | GPIO1_IO25        | 121       |     | J10:31       | GPIO5_IO5         | 133       |
+--------------+-------------------+-----------+-----+--------------+-------------------+-----------+

**Function Test**

- GPIO Output Test

  1) Description: Control the output level of GPIO through the system interface.

  2) Operation

    a) Enter the command to export the IO operation interface and configure it as output:

    .. code-block:: shell

      export OUT_IO_OUT_NUM=122
      echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
      echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction

    b) Enter the command to control the IO to output high level:

    .. code-block:: shell

       echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

    .. note:: At this time, using a multimeter to test the corresponding pin, the voltage should be 3.3V.

    c) Control the IO to output low level:

    .. code-block:: shell

       echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

    .. note:: At this time, using a multimeter to test J10:12, the voltage should be 3.3V.

  3) Result: When controlling the IO level during the test operation, the measured voltage matches the expectation, indicating normal function.

- GPIO Input Test

  1) Description: Configure and read the input level of GPIO through the system interface.

  2) Operation
  
    a) Use a Dupont wire or jumper cap to connect pins 10 and 12 of J10.

    b) Enter the command to export the IO operation interface and configure it as input:

    .. code-block:: shell

       export OUT_IO_IN_NUM=119
       echo ${OUT_IO_IN_NUM} > /sys/class/gpio/export
       echo "in" > /sys/class/gpio/gpio${OUT_IO_IN_NUM}/direction

    c) Enter the command to control J10:12 to output high level and read the input level of J10:10:

    .. code-block:: shell

       # Comment: Control J10:12 IO to output high level
       echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
       # Comment: Read the input level of IO
       cat /sys/class/gpio/gpio${OUT_IO_IN_NUM}/value

    .. note:: At this time, the command line interface terminal should output the character "1" (indicating high level).

    d) Enter the command to control J10:12 to output low level and read the input level of J10:10:

    .. code-block:: shell

       # Comment: Control J10:12 IO to output low level
       echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
       # Comment: Read the input level of IO
       cat /sys/class/gpio/gpio${OUT_IO_IN_NUM}/value

    .. note:: At this time, the command line interface terminal should output the character "0" (indicating low level).

  3) Result: During the test operation, the read level meets the correct expectations, indicating normal function.


SPI
-----

+--------------+-------------------+------------------+--+--------------+-------------------+------------------+
| Pin Location | Pin Configuration | System Interface |  | Pin Location | Pin Configuration | System Interface |
+--------------+-------------------+------------------+  +--------------+-------------------+------------------+
| J5:4         | SPI1_SS0          | /dev/spidev3.0   |  | J5:14        | SPI2_SS0          | /dev/spidev1.0   |
+--------------+-------------------+                  +  +--------------+-------------------+                  +
| J5:6         | SPI1_SCLK         |                  |  | J5:16        | SPI2_SCLK         |                  |
+--------------+-------------------+                  +  +--------------+-------------------+                  +
| J5:8         | SPI1_MOSI         |                  |  | J5:18        | SPI2_MOSI         |                  |
+--------------+-------------------+                  +  +--------------+-------------------+                  +
| J5:10        | SPI1_MISO         |                  |  | J5:20        | SPI2_MISO         |                  |
+--------------+-------------------+------------------+--+--------------+-------------------+------------------+

**Function Test**

  1) Description: Send a string through the SPI interface.

  .. note:: There is a spidev_test.c test program in the tools/spi/ directory of the kernel source code, which can be compiled by yourself.

  2) Operation

  - Use a jumper to connect MISO and MOSI of SPI2.

  - Enter the command to run the test program:

  .. code-block:: shell

     ./spidev_test -D /dev/spidev1.0 -v -p my_spi_test_string

  .. note:: "my_spi_test_string" is the string sent through SPI.

  - The output information can be seen as follows:

  .. code-block:: text

      spi mode: 0x0
      bits per word: 8
      max speed: 500000 Hz (500 KHz)
      TX | 6D 79 5F 73 70 69 5F 74 65 73 74 5F 73 74 72 69 6E 67 __ __ __ __ __ __ __ __ __ __ __ __ __ __  | my_spi_test_string
      RX | 6D 79 5F 73 70 69 5F 74 65 73 74 5F 73 74 72 69 6E 67 __ __ __ __ __ __ __ __ __ __ __ __ __ __  | my_spi_test_string

  3) Result: The output information seen meets the correct expectations, indicating successful transmission.


Audio
-------

+ System interface: wm8960-audio

**Functional Test**

  1) Description: Test by playing audio files.

  2) Operations

    a) Insert headphones or speakers into the interface corresponding to the silkscreen P1.

    b) Enter the command for testing:

    .. code-block:: shell

      aplay /usr/share/sounds/alsa/Front_Center.wav

  3) Result: When executing the test command, sound can be heard through the headphones, indicating the function is normal.


TF Card
---------

+ Interface silkscreen: J5

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
  
    a) Press the TF card inward in the insertion direction (release after hearing a "click" sound, and the TF card will pop out).

    b) The output information is similar to the following:

    .. code-block:: text

      ...
      mmc1: card 0001 removed
      ...

  3) Result: The phenomenon during the operation meets the correct expectations, indicating that the TF hot swapping is normal.


USB
-----

+ Interface silkscreen: J18

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


RTC
-----

+ Device interface: /dev/rtc

+ Test description: RTC test requires installing a button battery, and the battery is located at the silkscreen BT1.

**Functional Test**

+ **RTC Time**
  
  1) Description: First read the RTC time, then set the RTC time, and then check the RTC time after power-off and restart.

  2) Operations

    a) Read the RTC time, the specific operations are as follows:

    + Enter the command:

    .. code-block:: shell

       hwclock -f /dev/rtc1

    + You can see the time stored in RTC, similar to the following:

    .. code-block:: text

      1970-01-01 00:00:21.530265+00:00

    b) Set the RTC time, the specific operations are as follows:

    + Enter the command to update the system time:

    .. code-block:: shell

       date -s "2023-02-06 12:34:56"

    + You can see that the current system time is updated to the set time:

    .. code-block:: text

      Mon Feb  6 12:34:56 UTC 2023

    + Enter the command to set the system time to RTC:

    .. code-block:: shell

      hwclock -w -f /dev/rtc1

    c) Power off and restart the device.

    d) Check the RTC time, the specific operations are as follows:

    + Enter the command:

    .. code-block:: shell

       hwclock -f /dev/rtc1

    + You can see that the time stored in RTC is basically the same as the time we set, similar to the following:

    .. code-block:: text

      2023-02-06 12:35:34.485664+00:00

  3) Result: After performing the operations, checking that the RTC time is basically correct and the output during the operation meets the expectations indicates that the function is normal.

+ **wakealarm Function**
  
  1) Description: The RTC of the device can generate a wakealarm, which can be used to wake the device from sleep.

  2) Operations

    a) Set a wakealarm signal to be generated after 10 seconds, enter the following command:

    .. code-block:: shell

       echo +10 > /sys/class/rtc/rtc1/wakealarm

    b) Put the system into sleep mode, enter the following command:

    .. code-block:: shell

       echo freeze > /sys/power/state

  3) Result: After executing the above two commands, the system will not respond to serial terminal input. After the wakealarm wakes up the system, the serial terminal can continue to operate, indicating the test is normal.


Watchdog 
----------

+ System device: /dev/watchdog

**Functional Test** 

1. Watchdog Timeout Reset

   1) Description: Set the watchdog feeding interval to be less than the sleep time, and the watchdog will timeout and reset.

   2) Operations: Enter the following command in the command line interface and observe the device:

   .. code-block:: text

    /unit_tests/Watchdog/wdt_driver_test.out 5 10 0 &

   3) Result: The device restarts 5 seconds after executing the command, indicating the function is normal.

2. Watchdog Feeding Maintenance

   1) Description: Set the watchdog feeding time to be greater than the sleep time, and the device will run normally.

   2) Operations: Enter the following command in the command line interface:

   .. code-block:: text

    /unit_tests/Watchdog/wdt_driver_test.out 2 1 0
    
   3) Result: The system continues to run without restarting, indicating the function is normal.

   .. note:: After pressing *Ctrl+C* to abort the watchdog program, the device restarts within 2 seconds (Note: Once the hardware watchdog is enabled, it will not be turned off. Closing the program will stop feeding the dog, leading to a timeout restart).