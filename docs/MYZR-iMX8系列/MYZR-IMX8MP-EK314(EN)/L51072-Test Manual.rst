Test Manual
=============

Test Overview
---------------

+---------------+-------------+-----------------+----------------+-----------------+-------------+
|   Test Item   | Test Result |    Test Item    |  Test Result   |    Test Item    | Test Result |
+===============+=============+=================+================+=================+=============+
| Power Button  | Pass        | Reset Button    | Pass           | Indicator Light | Pass        |
+---------------+-------------+-----------------+----------------+-----------------+-------------+
| Watchdog      | Pass        | Sleep & Wake-up | Pass           | RTC             | PASS        |
+---------------+-------------+-----------------+----------------+-----------------+-------------+
| Ethernet Port | Pass        | CAN             | Pass           | I2C             | Pass        |
+---------------+-------------+-----------------+----------------+-----------------+-------------+
| UART          | Pass        | GPIO            | Pass           | PWM             | Pass        |
+---------------+-------------+-----------------+----------------+-----------------+-------------+
| SPI           | \--\--      | QSPI            | Pass           | Audio           | Pass        |
+---------------+-------------+-----------------+----------------+-----------------+-------------+
| USB WiFi      | Pass        | TF Card         | Pass           | USB 3.0         | Pass        |
+---------------+-------------+-----------------+----------------+-----------------+-------------+
| HDMI          | Pass        | LVDS            | Pending Screen | MIPI DSI        |             |
+---------------+-------------+-----------------+----------------+-----------------+-------------+
| MIPI CSI      | Pass        | PCIe            | Pass           | M2 5G           | Pass        |
+---------------+-------------+-----------------+----------------+-----------------+-------------+

Power Button
--------------

+ Interface Silkscreen: SW2

**Function Test**

+ **Power Off**

  1) Description: Long-press the power button to turn off the device power.

  2) Operation: When the main power of the device is connected and the main power switch is turned on, press and hold the SW2 button for about 5 seconds to turn off the device power.

  3) Result: The function is normal if the motherboard indicator light goes off.

+ **Power On**

  1) Description: Short-press the power button to turn on the device power.

  2) Operation: When the power is off (as in the previous step), press and hold the SW2 button for about 1 second to turn on the device power.

  3) Result: The function is normal if the motherboard indicator light turns on.


Reset Button
--------------

+ Interface Silkscreen: SW1

**Function Test**

  1) Description: Short-press the reset button to reset the device power.

  2) Operation: When the motherboard power is on, short-press SW1 to reset the device power.

  3) Result: The function is normal if the motherboard indicator light goes off when pressed and turns on when released.


Indicator Light
------------------

**System Interface**:

  Core Board Indicator Light: /sys/class/leds/core_board_heartbeat

  Motherboard Indicator Light: /sys/class/pwm/pwmchip0

**Function Test**

+ **Core Board Indicator Light**

  1) Description: The core board indicator light is used to check if the system is running.

  2) Operation: None

  3) Result: After the device is powered on, the LED light on the core board flashes within 10 seconds, indicating the system is running and the function is normal.


+ **Motherboard Indicator Light**

  1) Description: The motherboard indicator light is controlled by the PWM pin output of the CPU.

  2) Operation: Refer to the PWM test below.

  3) Result: After configuring different parameters, the lighting pattern of the motherboard indicator light changes, indicating the function is normal.

  .. note:: The motherboard indicator light can be configured by the user. For the configuration method, refer to the PWM test below.


Watchdog
----------

+ System Device: /dev/watchdog

**Function Test**

+ **Watchdog Timeout Reset**

  1) Description: If the watchdog feeding interval is set shorter than the sleep time, the watchdog will reset due to timeout.

  2) Operation: Enter the following command in the command line interface and observe the device:

  .. code-block:: shell

     /unit_tests/Watchdog/wdt_driver_test.out 5 10 0 &

  3) Result: The device restarts 5 seconds after executing the command, indicating the function is normal.

+ **Watchdog Feeding Maintenance**

  1) Description: If the watchdog feeding time is set longer than the sleep time, the device will operate normally.

  2) Operation: Enter the following command in the command line interface:

  .. code-block:: shell

     /unit_tests/Watchdog/wdt_driver_test.out 2 1 0

  3) Result: The system continues to run without restarting, indicating the function is normal.

  .. note:: After pressing *Ctrl+C* to stop the watchdog program, the device will restart within 2 seconds (Note: Once the hardware watchdog is enabled, it cannot be turned off. Stopping the program will stop feeding the watchdog, leading to timeout and restart).


Sleep & Wake-up
-----------------

+ System Interface: /sys/power/state

**Function Test**

+ **freeze (S0) Mode Sleep**

  1) Description: The device can enter sleep mode through the system interface.

  2) Operation

  + Enter the following command in the command line interface:

  .. code-block:: shell

     echo freeze > /sys/power/state

  + Output Information:

  .. code-block:: text

     PM: suspend entry (s2idle)
     ...
     Freezing user space processes ... (elapsed 0.000 seconds) done.
     ...
     Freezing remaining freezable tasks ... (elapsed 0.001 seconds) done.
     ...

  3) Result: The output information after executing the command basically matches the above, and the core board indicator light goes off, indicating the function is normal.

+ **mem (S2) Mode Sleep**

  1) Description: In mem (S2) mode, the device enters low-power mode.

  2) Operation

  + Enter the following command in the command line interface:

  .. code-block:: shell

     echo mem > /sys/power/state

  + Output Information:

  .. code-block:: text

     PM: suspend entry (s2idle)
     ...
     Freezing user space processes ... (elapsed 0.000 seconds) done.
     ...
     Freezing remaining freezable tasks ... (elapsed 0.001 seconds) done.
     ...

  3) Result: The output information after executing the command basically matches the above, and the core board indicator light goes off, indicating the function is normal.

  .. note:: After entering sleep mode, the device can be woken up by short-pressing SW2.


RTC
-----

+ Device Interface: /dev/rtc

+ Test Description: A button battery is required for the RTC test. The battery is located at the silkscreen BT1.

**Function Test**

+ **RTC Time**

  1) Description: First read the RTC time, then set the RTC time, and finally check the RTC time again after power-off and restart.

  2) Operation

    a) Read the RTC time, with specific operations as follows:

    + Enter the command:

    .. code-block:: shell

       hwclock -f /dev/rtc

    + The RTC-stored time will be displayed, similar to the following:

    .. code-block:: text

      1970-01-01 00:00:21.530265+00:00

    b) Set the RTC time, with specific operations as follows:

    + Enter the command to update the system time:

    .. code-block:: shell

       date -s "2023-02-06 12:34:56"

    + The current system time will be updated to the set time, as shown below:

    .. code-block:: text

      Mon Feb  6 12:34:56 UTC 2023

    + Enter the command to set the system time to RTC:

    .. code-block:: shell

      hwclock -w -f /dev/rtc

    c) Power off and restart the device.

    d) Check the RTC time, with specific operations as follows:

    + Enter the command:

    .. code-block:: shell

       hwclock -f /dev/rtc

    + The RTC-stored time will be basically the same as the set time, similar to the following:

    .. code-block:: text

      2023-02-06 12:35:34.485664+00:00

  3) Result: After performing the operations, the checked RTC time is basically correct, and the output during the operation meets the expectations, indicating the function is normal.

+ **wakealarm Function**

  1) Description: The RTC of the device can generate a wakealarm, which can be used to wake the device from sleep.

  2) Operation

    a) Set a wakealarm signal to be generated after 10 seconds, and enter the following command:

    .. code-block:: shell

       echo +10 > /sys/class/rtc/rtc1/wakealarm

    b) Put the system into sleep mode, and enter the following command:

    .. code-block:: shell

       echo freeze > /sys/power/state

  3) Result: After executing the above two commands, the system will not respond to the serial terminal input. After the system is woken up by the wakealarm, the serial terminal can continue to operate, indicating the test is normal.



Ethernet Port
---------------

  + Interface Silkscreen: U12 (Ethernet Port 1), U9 (Ethernet Port 2)
  + System Interface: eth0 (Ethernet Port 1), eth1 (Ethernet Port 2)

**Function Test**

+ **Ethernet Port 1**

  1) Description: The test is performed by sending ICMP packets from the development board to the PC.

  2) Operation

    a) Configure the PC's wired network card IP to 192.168.137.99.

    b) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

    c) Configure the development board's Ethernet port IP, with specific configuration commands as follows:

    .. code-block:: shell

      ifconfig eth1 down
      ifconfig eth0 up
      ifconfig eth0 192.168.137.81

    d) Execute the Ethernet port test command

    + Enter the command:

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4

    + Output Information:

    .. code-block:: text

      PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
      64 bytes from 192.168.137.99: icmp_seq-1 ttl-64 time-1.35 ms
      64 bytes from 192.168.137.99: icmp_seq-2 ttl-64 time-1.35 ms

      --- 192.168.137.99 ping statistics ---
      2 packets transmitted, 2 received, 0% packet loss, time 1002ms
      rtt min/avg/max/mdev - 1.347/1.347/1.348/0.000 ms

  3) Result: "0% packet loss" indicates the test is passed.

+ **Ethernet Port 2**

  1) Description: The test is performed by sending ICMP packets from the development board to the PC.

  2) Operation

    a) Configure the PC's wired network card IP to 192.168.137.99.

    b) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

    c) Configure the development board's Ethernet port IP, with specific configuration commands as follows:

    .. code-block:: shell

      ifconfig eth0 down
      ifconfig eth1 up
      ifconfig eth1 192.168.137.82

    d) Execute the Ethernet port test command

    + Enter the command:

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4

    + Output Information:

    .. code-block:: text

      PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
      64 bytes from 192.168.137.99: icmp_seq-1 ttl-64 time-0.595 ms
      64 bytes from 192.168.137.99: icmp_seq-2 ttl-64 time-0.843 ms

      --- 192.168.137.99 ping statistics ---
      2 packets transmitted, 2 received, 0% packet loss, time 1001ms
      rtt min/avg/max/mdev - 0.595/0.719/0.843/0.124 ms

  3) Result: "0% packet loss" indicates the test is passed.


CAN
-----

+--------------+-------------------+------------------+
| Pin Location | Pin Configuration | System Interface |
+--------------+-------------------+------------------+
| J14:1        | CAN1H             | can0             |
+--------------+-------------------+                  +
| J14:3        | CAN1L             |                  |
+--------------+-------------------+------------------+
| J14:4        | CAN2H             | can1             |
+--------------+-------------------+                  +
| J14:6        | CAN2L             |                  |
+--------------+-------------------+------------------+

**Function Test**

  1) Description: The test is performed by mutual reception between two groups of CAN buses.

  2) Operation

    a) Use a Dupont wire to connect J14:1 to J14:4, and J14:3 to J14:6.

    b) Enter commands in the serial terminal to configure the CAN interface and set it to UP:

    .. code-block:: shell

      ip link set can0 type can bitrate 500000
      ip link set can0 up
      ip link set can1 type can bitrate 500000
      ip link set can1 up

    .. note:: You can see the terminal output similar information: link becomes ready

    c) Enter the command in the serial terminal to make CAN1 (can0) receive in the background:

    .. code-block:: shell

       candump can0 &

    d) Enter the command in the serial terminal to make CAN2 (can1) send test data:

    + Enter the command:

    .. code-block:: shell

       cansend can1 1F334455#1122334455667788

    + Output Information:

    .. code-block:: text

      can0  1F334455   [8]  11 22 33 44 55 66 77 88

  3) Result: The output information is correct during the operation in "d)", indicating the function is normal.


I2C
-----

**Function Test**

  1) Description: Execute the I2C detection command and observe the results.

  2) Operation

    a) Detect the I2C bus of the system

    + Enter the command:

    .. code-block:: shell

        i2cdetect -l

    + The output information is similar to the following, indicating that I2C 0, 1, 2 and HDMI adapters are detected.

    .. code-block:: text

      i2c-1	i2c       	30a30000.i2c                    	I2C adapter
      i2c-6	i2c       	DesignWare HDMI                 	I2C adapter
      i2c-2	i2c       	30a40000.i2c                    	I2C adapter
      i2c-0	i2c       	30a20000.i2c                    	I2C adapter

    b) Detect I2C devices on the bus

    + Enter the command:
    
    .. code-block:: shell

      i2cdetect -y 2

    .. note:: The parameter "2" in i2cdetect can be the bus number detected in the previous step, such as 0, 1, or 6.

    + The output is similar to the following information; non "\--" indicates that a device is detected at the corresponding address of the I2C bus.

    .. code-block:: text

           0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
      00:                         -- -- -- -- -- -- -- --
      10: -- -- -- -- -- -- -- -- -- -- UU -- -- -- -- --
      20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
      30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
      40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
      50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
      60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 6f
      70: -- -- -- -- -- -- -- --

  3) Result: The output information during the operation is basically consistent with the expectation, indicating that the function is normal.

UART
------

+--------------+-------------------+------------------+
| Pin Position | Pin Configuration | System Interface |
+--------------+-------------------+------------------+
| J14:8        | UART1_TXD         | /dev/ttymxc0     |
+--------------+-------------------+                  +
| J14:9        | UART1_RXD         |                  |
+--------------+-------------------+                  +
| J14:10       | UART1_CTS         |                  |
+--------------+-------------------+                  +
| J14:11       | UART1_RTS         |                  |
+--------------+-------------------+------------------+

**Function Test**

  1) Description: Test using the UART loopback (self-transmit and self-receive) method.

  2) Operation

    a) Use a Dupont wire to connect J14:8 and J14:9.

    b) Run the test program:

    + Enter the command:

    .. code-block:: shell

      ./serial_test_arm64.out /dev/ttymxc0 "www.myzr.com.cn"

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

  3) Result: After executing the test operation, if the input information matches the correct expectation, the function is normal.

GPIO
------

+--------------+-------------------+-----------+--------------+-------------------+-----------+
| Pin Position | Pin Configuration | IO Number | Pin Position | Pin Configuration | IO Number |
+--------------+-------------------+-----------+--------------+-------------------+-----------+
| J13:13       | GPIO4_IO18        | 114       | J13:26       | GPIO4_IO01        | 97        |
+--------------+-------------------+-----------+--------------+-------------------+-----------+
| J13:15       | GPIO4_IO19        | 115       | J13:28       | GPIO4_IO00        | 96        |
+--------------+-------------------+-----------+--------------+-------------------+-----------+
| J13:16       | GPIO2_IO20        | 52        | J13:32       | GPIO4_IO20        | 116       |
+--------------+-------------------+-----------+--------------+-------------------+-----------+

**Function Test**

+ GPIO Output Test

  1) Description: Control the output level of GPIO through the system interface.

  2) Operation

    a) Enter commands to export the IO operation interface and configure it as output:

    .. code-block:: shell

        export OUT_IO_OUT_NUM=114
        echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
        echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction

    b) Enter the command to control the IO to output high level:

    .. code-block:: shell

       echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

    .. note:: At this time, use a multimeter to test J13:13; the voltage should be 3.3V.

    c) Control the IO to output low level:

    .. code-block:: shell

       echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

    .. note:: At this time, use a multimeter to test J13:13; the voltage should be 0V.

  3) Result: During the test operation, when controlling the IO level, if the measured voltage matches the expectation, the function is normal.


+ GPIO Input Test

  1) Description: Configure and read the input level of GPIO through the system interface.

  2) Operation

    a) Use a Dupont wire or jumper cap to connect pins 15 and 13 of J13.

    b) Enter commands to export the IO operation interface and configure it as input:

    .. code-block:: shell

        export OUT_IO_IN_NUM=115
        echo ${OUT_IO_IN_NUM} > /sys/class/gpio/export
        echo "in" > /sys/class/gpio/gpio${OUT_IO_IN_NUM}/direction

    c) Enter commands to control J13:13 to output high level and read the input level of J13:15:

    .. code-block:: shell

       # Comment: Control J13:13 IO to output high level
       echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
       # Comment: Read the input level of IO
       cat /sys/class/gpio/gpio${OUT_IO_IN_NUM}/value

    .. note:: At this time, the command line interface terminal should output the character "1" (indicating high level).

    d) Enter commands to control J13:13 to output low level and read the input level of J13:15:

    .. code-block:: shell

       # Comment: Control J13:13 IO to output low level
       echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
       # Comment: Read the input level of IO
       cat /sys/class/gpio/gpio${OUT_IO_IN_NUM}/value

    .. note:: At this time, the command line interface terminal should output the character "0" (indicating low level).

  3) Result: During the test operation, if the read level matches the correct expectation, the function is normal.

PWM
-----

+ Interface Position: J13:27

+ System Interface: /sys/class/pwm/pwmchip0

**Function Test**

  1) Description: Configure PWM and observe the result.

  2) Operation

    a) Enter commands to configure PWM:

    .. code-block:: shell

      # Comment: Export the operation interface of PWM (PWM1)
      echo 0 > /sys/class/pwm/pwmchip0/export
      # Comment: Configure the PWM period, in nanoseconds
      echo 1000000000 > /sys/class/pwm/pwmchip0/pwm0/period
      # Comment: Configure the PWM duty cycle, in nanoseconds (must be less than the period)
      echo 500000000 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle
      # Comment: Enable PWM
      echo 1 > /sys/class/pwm/pwmchip0/pwm0/enable

    b) Use an oscilloscope to detect J13:27; periodic level changes should be observed.

  3) Result: When using an oscilloscope to detect J13:27, if periodic level changes are observed, the function is normal.

SPI
-----

**Function Test**

  1) Description: Send a string through the SPI interface.

  2) Operation

  + Enter the command to run the test program:

  .. code-block:: shell

     ./spidev_test.gcc7_arm64.out -D /dev/spidev1.0 -v -p my_spi_test_string

  .. note:: "my_spi_test_string" is the string sent through SPI.

  + The output information should be similar to the following:

  .. code-block:: text

     spi mode: 0x4
     bits per word: 8
     max speed: 500000 Hz (500 kHz)
     TX | 6D 79 5F 73 70 69 5F 74 65 73 74 5F 73 74 72 69 6E 67 __ __ __ __ __ __ __ __ __ __ __ __ __ __  |my_spi_test_string|
     RX | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 __ __ __ __ __ __ __ __ __ __ __ __ __ __  |..................|

  3) Result: If the observed output information matches the correct expectation, it indicates successful transmission.

QSPI
------

+ Device Interface: /dev/mtd0

**Function Test**

  1) Description: Verify the function by writing and reading files.

  2) Operation

    a) Enter commands to prepare the QSPI Flash device:

    .. code-block:: shell

      # Comment: Format the QSPI Flash device
      flash_erase /dev/mtd0 0 0
      # Comment: Mount the Flash device
      mount -t jffs2 /dev/mtdblock0 /mnt
      # Comment: Check the mounted device
      df -h

    .. note:: Output information similar to the following should be visible:

      /dev/mtdblock0   32M  904K   32M   3% /mnt

    b) Enter commands to write and read files:

    .. code-block:: shell

      # Comment: Write a file to Flash
      echo "Flash Test" > /mnt/test.txt
      # Comment: Synchronize data
      sync
      # Comment: Read the file
      cat /mnt/test.txt

    .. note:: The output information should be visible: Flash Test

  3) Result: After executing the commands, if the output information matches the correct expectation, the function is normal.

Audio
-------

+ System Interface: wm8960-audio

**Function Test**

  1) Description: Test by playing an audio file.

  2) Operation

    a) Insert headphones or a speaker into the interface corresponding to the silkscreen "P1".

    b) Enter the command to perform the test:

    .. code-block:: shell

      aplay -D hw:0 /unit_tests/ASRC/audio8k16S.wav

  3) Result: When executing the test command, if sound can be heard from the headphones, the function is normal.



WiFi Test
------------

+ Interface Silkscreen: U21

**Function Test**

  1) Description: After the WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal.

  2) Operation:

      a) Connect the WIFI antenna to the "E3" interface.

      b) Generate the WPA PSK file for the SSID.

      .. code-block:: shell

        wpa_passphrase command format: wpa_passphrase + wifi name + wifi password > /etc/wpa_supplicant.conf

      + Enter the command:

      .. code-block:: shell

        wpa_passphrase MYZR-WIFI-2.4G myzr2012 > /etc/wpa_supplicant.conf

      c) Connection:

      + Enter the command:

        .. code-block:: shell

          wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

      d) Obtain IP:

       + Enter the command:

       .. code-block:: shell

          udhcpc -i wlan0

      The output will have information similar to the following:

       .. code-block:: text

          udhcpc: started, v1.33.1
          udhcpc: sending discover
          udhcpc: sending select for 172.16.0.121
          udhcpc: lease of 172.16.0.121 obtained, lease time 86940
          /etc/udhcpc.d/50default: Adding DNS 114.114.114.114
          /etc/udhcpc.d/50default: Adding DNS 8.8.8.8

      e) Test the connection:

          Add the following content to /etc/resolv.conf:

       .. code-block:: text

          nameserver 8.8.8.8
          nameserver 114.114.114.114

       + Enter the command:

       .. code-block:: shell

          ping -I wlan0 www.baidu.com


       Output information:

       .. code-block:: text

          PING www.a.shifen.com (157.148.69.80) from 172.16.0.121 wlan0: 56(84) bytes of data.
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=1 ttl=54 time=9.08 ms
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=2 ttl=54 time=7.94 ms
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=3 ttl=54 time=8.10 ms
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=4 ttl=54 time=8.15 ms
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=5 ttl=54 time=9.94 ms
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=6 ttl=54 time=11.7 ms
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=7 ttl=54 time=9.75 ms
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=8 ttl=54 time=9.03 ms
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=9 ttl=54 time=8.29 ms
          64 bytes from 157.148.69.80 (157.148.69.80): icmp_seq=10 ttl=54 time=8.92 ms
          --- www.a.shifen.com ping statistics ---
          10 packets transmitted, 10 received, 0% packet loss, time 9016ms
          rtt min/avg/max/mdev = 7.944/9.092/11.733/1.095 ms
    

  3) Result: "0% packet loss" indicates that the WIFI connection is normal.


Bluetooth Test
----------------

+ Interface Silkscreen: U21

**Function Test**

  1) Description: After scanning for Bluetooth devices, send an L2CAP response request and receive the reply.

  2) Operation:

      a) Connect the antenna to the "E3" interface.

      b) Start Bluetooth:

      + Enter the command:

      .. code-block:: shell

        hciconfig hci0 up
        hciconfig 

      c) Scan for external Bluetooth devices:

      + Enter the command:

      .. code-block:: shell

        hcitool scan

      The output information is similar to the following:

      .. code-block:: text

        Scanning ...
            88:46:04:4C:11:A7   Redmi K40


      d) Send an L2CAP packet for testing:

      + Enter the command:

      .. code-block:: shell

        l2ping 88:46:04:4C:11:A7
      

      Output information:

        .. code-block:: text

          Ping: 88:46:04:4C:11:A7 from B0:F1:EC:A7:E8:03 (data size 44) ...
          44 bytes from 88:46:04:4C:11:A7 id 0 time 44.84ms
          44 bytes from 88:46:04:4C:11:A7 id 1 time 28.58ms
          44 bytes from 88:46:04:4C:11:A7 id 2 time 46.05ms
          44 bytes from 88:46:04:4C:11:A7 id 3 time 44.86ms
          44 bytes from 88:46:04:4C:11:A7 id 4 time 44.67ms
          44 bytes from 88:46:04:4C:11:A7 id 5 time 52.32ms
          44 bytes from 88:46:04:4C:11:A7 id 6 time 24.86ms
          44 bytes from 88:46:04:4C:11:A7 id 7 time 59.71ms
          ^C8 sent, 8 received, 0% loss


  3) Result: "0% packet loss" indicates that the Bluetooth connection is normal.


4G Module (EC20) Test
-----------------------

+ Interface Silkscreen: J11

**Function Test**

1) Description: After the 4G connection is successful, the development board sends ICMP packets to the external network to verify that the connection is normal.

2) Operation:

  a) Obtain IP

    + Enter the command

      .. code-block:: shell

        udhcpc -i usb0

  b) Test the connection status

    Add the following content to /etc/resolv.conf:

      .. code-block:: text

        nameserver 8.8.8.8
        nameserver 114.114.114.114
    
    + Enter the command:

      .. code-block:: shell

        ping -I usb0 www.baidu.com
  
  The output will have information similar to the following:

    .. code-block:: text

        PING www.baidu.com(240e:ff:e020:9ae:0:ff:b014:8e8b (240e:ff:e020:9ae:0:ff:b014:8e8b)) from 240e:47e:2228:19a:44f2:65ff:fe3e:7abe usb0: 56 data bytes
        64 bytes from 240e:ff:e020:9ae:0:ff:b014:8e8b (240e:ff:e020:9ae:0:ff:b014:8e8b): icmp_seq=1 ttl=53 time=39.1 ms
        64 bytes from 240e:ff:e020:9ae:0:ff:b014:8e8b (240e:ff:e020:9ae:0:ff:b014:8e8b): icmp_seq=2 ttl=53 time=27.6 ms
        64 bytes from 240e:ff:e020:9ae:0:ff:b014:8e8b (240e:ff:e020:9ae:0:ff:b014:8e8b): icmp_seq=3 ttl=53 time=45.3 ms
        64 bytes from 240e:ff:e020:9ae:0:ff:b014:8e8b (240e:ff:e020:9ae:0:ff:b014:8e8b): icmp_seq=4 ttl=53 time=43.9 ms
        64 bytes from 240e:ff:e020:9ae:0:ff:b014:8e8b (240e:ff:e020:9ae:0:ff:b014:8e8b): icmp_seq=5 ttl=53 time=32.4 ms
        64 bytes from 240e:ff:e020:9ae:0:ff:b014:8e8b (240e:ff:e020:9ae:0:ff:b014:8e8b): icmp_seq=6 ttl=53 time=40.3 ms
        64 bytes from 240e:ff:e020:9ae:0:ff:b014:8e8b (240e:ff:e020:9ae:0:ff:b014:8e8b): icmp_seq=7 ttl=53 time=55.4 ms
        --- www.baidu.com ping statistics ---
        7 packets transmitted, 7 received, 0% packet loss, time 6011ms
        rtt min/avg/max/mdev = 27.625/40.563/55.443/8.375 ms

  
3) Result: "0% packet loss" indicates that the 4G connection is normal.


TF Card
----------

+ Interface Silkscreen: J10

**Function Test**

  .. note:: The TF card interface of the device supports hot-swapping, and the TF card slot is a pop-up type.

+ TF Card Insertion Test

  1) Description: Insert the TF card and check if the device can correctly recognize the card.

  2) Operation

    a) Take a TF card and insert it into the TF card interface of the device.

    b) The output information is similar to the following:

    .. code-block:: text

      ...
      mmc1: new ultra high speed SDR104 SDHC card at address 0001
      mmcblk1: mmc1:0001 SD16G 14.9 GiB
      ...

  3) Result: If the output information after the operation matches the expected correct result, it indicates that the TF card is correctly recognized.

+ TF Card Ejection Test

  1) Eject the TF card and check if the device can respond correctly.

  2) Operation

    a) Press the TF card inward in the insertion direction (release it when a "click" sound is heard, and the TF card will pop out).

    b) The output information is similar to the following:

    .. code-block:: text

      ...
      mmc1: card 0001 removed
      ...

  3) Result: If the phenomenon during the operation matches the expected correct result, it indicates that the TF card hot-swapping function is normal.


USB 3.0
---------

+ Interface Silkscreen: J3

**Function Test**

  1) Description: Test by plugging and unplugging a USB storage device (USB flash drive).


  2) Operation:

    a) Insert the USB device into the USB interface of the baseboard, and the system will output information similar to the following:

      .. code-block:: text

        [ 2649.580746] usb 2-1.1: new high-speed USB device number 3 using ehci-platform
        [ 2649.735676] usb-storage 2-1.1:1.0: USB Mass Storage device detected
        [ 2649.752030] scsi host0: usb-storage 2-1.1:1.0
        [ 2649.951147] usbcore: registered new interface driver uas
        [ 2650.801744] scsi 0:0:0:0: Direct-Access     aigo     U330             2.00 PQ: 0 ANSI: 4
        [ 2650.822371] sd 0:0:0:0: [sda] 61440000 512-byte logical blocks: (31.5 GB/29.3 GiB)
        [ 2650.830508] sd 0:0:0:0: Attached scsi generic sg0 type 0
        [ 2650.851173] sd 0:0:0:0: [sda] Write Protect is off
        [ 2650.871241] sd 0:0:0:0: [sda] No Caching mode page found
        [ 2650.875217] sd 0:0:0:0: [sda] Assuming drive cache: write through
        [ 2650.896991]  sda: sda1
        [ 2650.916261] sd 0:0:0:0: [sda] Attached SCSI removable disk

    b) Unplug the USB device from the baseboard, and the system will output information similar to the following:

      .. code-block:: text

        [ 2690.764161] usb 2-1.1: USB disconnect, device number 3


  3) Phenomenon: If the phenomenon during the operation matches the expected correct result, it indicates normal functionality.


USB Recognized as USB Flash Drive
-----------------------------------

+ Interface Silkscreen: J16

**Function Test**

  1) Description: Recognize the development board as a USB flash drive on the PC via a USB cable.


  2) Operation:


    a) Create a 10M file:

    + Enter the command:

     .. code-block:: shell

      dd if=/dev/zero of=/dev/shm/disk bs=1024 count=10240

    
    The output is similar to the following information:

     .. code-block:: text

       10240+0 records in
       10240+0 records out

    b) Load the module

    + Enter the command:

     .. code-block:: shell

       modprobe g_mass_storage stall=0 file=/dev/shm/disk removable=1
    
    c) Recognize the USB flash drive

      At this time, a USB flash drive drive letter will appear in "My Computer" on the PC. After formatting it, you can read and write to it.
    
    d) Mount

    + Enter the command

      .. code-block:: shell

        mount /dev/shm/disk /mnt
    
  3) Result:

    Files written on the computer can be seen in the /mnt directory after remounting. Files written on the development board can be seen on the PC after re-plugging the USB cable. This indicates that the function is normal.

USB recognized as network interface
--------------

+ Interface silkscreen: J16

**Functional Test**

1) Description: Recognize USB as a network interface via USB cable

2) Operation:

   a) Load module:

    + Enter command:

     .. code-block:: shell
  
       modprobe g_ether

   b) Set IP:

    + Enter command:

     .. code-block:: shell

      ifconfig usb0 192.168.7.2
    
    Set the local connection IP of rndis recognized by PC to 192.168.7.8

  
   c) Test network interface:

    + Enter command:

     .. code-block:: shell

        ping 192.168.7.8 -c 2 -w 4
      
    Output information:

      .. code-block:: text

        PING 192.168.7.8 (192.168.7.8) 56(84) bytes of data.
        64 bytes from 192.168.7.8: icmp_seq=1 ttl=128 time=0.789 ms
        64 bytes from 192.168.7.8: icmp_seq=2 ttl=128 time=0.505 ms

        --- 192.168.7.8 ping statistics ---
        2 packets transmitted, 2 received, 0% packet loss, time 1002ms
        rtt min/avg/max/mdev = 0.505/0.647/0.789/0.142 ms


3) Result:

  "0% packet loss" indicates the test passed

Note: If WIN10 recognizes rndis as a COM port, you need to download the driver kindle_rndis.inf_amd64-v1.0.0.1.zip, unzip it, run 5-runasadmin_register-CA-cer.cmd with administrator privileges, then double-click on the COM port, find the unzipped driver in the computer, and there will be an rndis network.






HDMI
----

+ Interface silkscreen: J4

**Functional Test**

  1) Description: The device will recognize the HDMI display device and enable it. Adapters (such as HDMI to VGA) are not supported.

  2) Operation: Connect the HDMI display, power on the device again, press the Enter key during startup to enter the u-boot command line, and enter the following command:


   .. code-block:: shell

      setenv fdtfile myimx8mpek314.dtb
      saveenv
      boot


  3) Result: The HDMI display shows content during device startup, indicating normal function.
  
  Note: Using myimx8mpek314-mipi.dtb or myimx8mpek314.dtb, the HDMI display will work normally.

LVDS
----

+ Interface silkscreen: J8 (LVDS0), J9 (LVDS1)

**Functional Test**

  1) Description:

  2) Operation:

  3) Phenomenon:

MIPI DSI
--------

+ Interface silkscreen: J5

**Functional Test**

  1) Description: Check if the MIPI screen displays properly.

  2) Operation: Connect the MIPI screen, power on the device again, press the Enter key during startup to enter the u-boot command line, and enter the following command:
    
    .. code-block:: shell

      setenv fdtfile myimx8mpek314-mipi.dtb
      saveenv
      boot 

  3) Result: The MIPI screen shows content during device startup, indicating normal function.

  Note: Using myimx8mpek314-mipi.dtb, the MIPI screen will display normally.

MIPI CSI
--------

+ Interface silkscreen: J6 (CSI1), J7 (CSI2)

**Functional Test**

+ MIPI CSI1

  1) Description:

  2) Operation

    a) Check camera device

    + Enter command:

    .. code-block:: shell

       v4l2-ctl --list-devices

    b) Capture and display camera image

    + Enter command:

    .. code-block:: shell

       gst-launch-1.0 -e v4l2src device-/dev/video3 ! video/x-raw ! autovideosink

    + Output information is similar to:

    .. code-block:: text

       Setting pipeline to PAUSED ...
       Pipeline is live and does not need PREROLL ...
       Pipeline is PREROLLED ...
       Setting pipeline to PLAYING ...
       New clock: GstSystemClock
       [   71.873621] bypass csc
       [   71.876047] input fmt YUV4
       [   71.878792] output fmt YUYV

  3) Result: After execution, the display shows real-time images captured by the camera, indicating normal function.

+ MIPI CSI2

  1) Description:

  2) Operation

    a) Switch device tree file

    .. code-block:: shell

       setenv fdtfile myimx8mpek314-ov2775-ov5640.dtb; boot

    b) Check camera device

    + Enter command:

    .. code-block:: shell

       v4l2-ctl --list-devices

    c) Capture and display camera image

    + Enter command:

    .. code-block:: shell

       gst-launch-1.0 -e v4l2src device-/dev/video2 ! video/x-raw ! autovideosink

    + Output information is similar to:

    .. code-block:: text

       Setting pipeline to PAUSED ...
       Pipeline is live and does not need PREROLL ...
       Pipeline is PREROLLED ...
       Setting pipeline to PLAYING ...
       New clock: GstSystemClock
       [   27.643936] bypass csc
       [   27.646359] input fmt YUV4
       [   27.649107] output fmt YUYV

PCIe
----

+ Interface silkscreen: J11

**Functional Test**

  1) Description: Insert the PCIe module and check if the device can correctly recognize it.

  2) Operation: Insert the PCIe module into the device, power on normally, and enter the command for testing:

    .. code-block:: shell

       lspci

    + Output information is similar to:

    .. code-block:: text

       01:00.0 Multimedia controller: Intersil Techwell Device 6869 (rev 01)
    

  3) Result: The output information after operation meets the expected result, indicating that the module is correctly recognized.

M2 5G
-----

+ Interface silkscreen: J12

**Functional Test**

  1) Description:

  2) Operation:

  3) Phenomenon:



QT Test
-------

**Functional Test**

1) Description: Check if QT can run on the device.

2) Operation: Enter the command for testing:

    .. code-block:: shell

       /usr/share/qt5everywheredemo-1.0/QtDemo

3) Result: The QT interface is normally displayed on the screen, indicating normal function.


Copy Update Image
-------------------

+ Interface silkscreen: J16

**Functional Test**

  1) Description: Can update dtb, Image, and kernel modules.

  2) Operation:

    a) Copy the corresponding files to the current directory of the development board, taking tftp as an example.

    Open the tftpd software on the computer and set the address to the directory where the files to be replaced are located. Connect the network port of the development board to the computer's network port with a network cable.

    b) Test connection:

     + Enter command:

      .. code-block:: shell

        ping 192.168.137.99 -c 2 -w 4


     Output information:

      .. code-block:: text

        PING 192.168.137.99 (192.168.137.99): 56 data bytes
        64 bytes from 192.168.137.99: seq=0 ttl=64 time=0.311 ms
        64 bytes from 192.168.137.99: seq=1 ttl=64 time=0.510 ms
        --- 192.168.137.99 ping statistics ---
        2 packets transmitted, 2 packets received, 0% packet loss
        round-trip min/avg/max = 0.311/0.410/0.510 ms
        "0% packet loss" indicates the connection is normal.

    c) Transfer files:

     + Enter command:

      .. code-block:: shell

        tftp -g 192.168.137.99 -r Image
        tftp -g 192.168.137.99 -r myimx8mpek314.dtb
        tftp -g 192.168.137.99 -r kernel-modules.tar.bz2
      
    d) Check if the system automatically mounts the partition

      + Enter command:

        .. code-block:: shell

          ls /run/media/mmcblk2p1

    e) System automatically mounts the partition

      Copy the corresponding files to the /run/media/mmcblk2p1 directory to replace the original files.

      + Enter command:

        .. code-block:: shell

          cp Image /run/media/mmcblk2p1
          cp myimx8mpek314.dtb /run/media/mmcblk2p1
          cp kernel-modules.tar.bz2 /run/media/mmcblk2p1

    f) Unzip and update kernel modules

     + Enter command:

      .. code-block:: shell

        tar xjvf kernel-modules.tar.bz2 -C /

    g) Save and restart

     + Enter command:

      .. code-block:: shell

        reboot

    h) If the system does not automatically mount the partition, check the fat partition address

     + Enter command:

      .. code-block:: shell

        fdisk -l

     Output information:

      .. code-block:: text

        ......
        Device         Boot   Start      End  Sectors  Size Id Type
        /dev/mmcblk2p1        20480  1044479  1024000  500M  c W95 FAT32 (LBA)
        /dev/mmcblk2p2      1228800 30576639 29347840   14G 83 Linux
        ......

    i) Mount manually

     + Enter command:

      .. code-block:: shell

        mount /dev/mmcblk2p1 /mnt/

    j) Copy the corresponding files to the /mnt directory to replace the original files

     + Enter command:

      .. code-block:: shell

        cp Image /mnt
        cp myimx8mpek314-mipi.dtb /mnt
        cp myimx8mpek314.dtb /mnt

    k) Save and restart

     + Enter command:
    
      .. code-block:: shell
        
        reboot

  3) Result:

    The phenomenon during operation meets the expected result, indicating normal function.


QT Test
---------

**Functional Test**

1) Description: Observe whether Qt can run on the device.

2) Procedure: Enter the command for testing:

    .. code-block:: shell

       /usr/share/qt5everywheredemo-1.0/QtDemo

3) Result: The Qt interface is displayed correctly on the screen, indicating normal functionality.




Copy and Update Image
-----------------------

+ Interface Silkscreen: J16

**Functional Test**

  1) Description: Capable of updating dtb, Image, and kernel modules.

  2) Procedure:

    a) Copy the corresponding files to the current directory of the development board, using tftp as an example.

    On the computer side, open the tftpd software and set the address to the directory where the files to be replaced are located. Connect this network port of the development board to the computer's network port using an Ethernet cable.

    b) Test the connection:

     + Enter the command:

      .. code-block:: shell

        ping 192.168.137.99 -c 2 -w 4


     Output information:

      .. code-block:: text

        PING 192.168.137.99 (192.168.137.99): 56 data bytes
        64 bytes from 192.168.137.99: seq=0 ttl=64 time=0.311 ms
        64 bytes from 192.168.137.99: seq=1 ttl=64 time=0.510 ms
        --- 192.168.137.99 ping statistics ---
        2 packets transmitted, 2 packets received, 0% packet loss
        round-trip min/avg/max = 0.311/0.410/0.510 ms
        "0% packet loss" indicates a normal connection.

    c) Transfer files:

     + Enter the command:

      .. code-block:: shell

        tftp -g 192.168.137.99 -r Image
        tftp -g 192.168.137.99 -r myimx8mpek314.dtb
        tftp -g 192.168.137.99 -r kernel-modules.tar.bz2
      
    d) Check if the system has automatically mounted the partition.

      + Enter the command:

        .. code-block:: shell

          ls /run/media/mmcblk2p1

    e) The system automatically mounts the partition.

      Copy the corresponding files to the /run/media/mmcblk2p1 directory to replace the original files.

      + Enter the command:

        .. code-block:: shell

          cp Image /run/media/mmcblk2p1
          cp myimx8mpek314.dtb /run/media/mmcblk2p1
          cp kernel-modules.tar.bz2 /run/media/mmcblk2p1

    f) Extract and update the kernel modules.

     + Enter the command:

      .. code-block:: shell

        tar xjvf kernel-modules.tar.bz2 -C /

    g) Save and restart.

     + Enter the command:

      .. code-block:: shell

        reboot

    h) If the system does not automatically mount the partition, check the FAT partition address.

     + Enter the command:

      .. code-block:: shell

        fdisk -l

     Output information:

      .. code-block:: text

        ......
        Device         Boot   Start      End  Sectors  Size Id Type
        /dev/mmcblk2p1        20480  1044479  1024000  500M  c W95 FAT32 (LBA)
        /dev/mmcblk2p2      1228800 30576639 29347840   14G 83 Linux
        ......

    i) Manual mounting.

     + Enter the command:

      .. code-block:: shell

        mount /dev/mmcblk2p1 /mnt/

    j) Copy the corresponding files to the /mnt directory to replace the original files.

     + Enter the command:

      .. code-block:: shell

        cp Image /mnt
        cp myimx8mpek314-mipi.dtb /mnt
        cp myimx8mpek314.dtb /mnt

    k) Save and restart.

     + Enter the command:
    
      .. code-block:: shell
        
        reboot

  3) Result:

    The observed phenomena during the operation meet the expected correct outcomes, indicating normal functionality.