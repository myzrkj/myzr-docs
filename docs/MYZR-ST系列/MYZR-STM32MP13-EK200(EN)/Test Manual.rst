Test Manual
=============


Reset Button
--------------

+ Interface Silkscreen: SW2

**Function Test**

  1) Description: A short press on the reset button resets the device power.

  2) Operation: When the mainboard power is on, a short press on SW1 will reset the device power.

  3) Result: When pressed, the mainboard indicator light should turn off; when released, the mainboard indicator light should turn on. If this happens, the function is normal.


RTC
-----

+ Device Interface: /dev/rtc

+ Test Description: RTC testing requires installing a button battery, which is located at the silkscreen marked BT1.

**Function Test**

+ **RTC Time**

  1) Description: Set the RTC time, then power off and restart the device to verify the RTC time.

  2) Operation

    a) Set the RTC time with the following specific operations:

    + Enter the command to update the system time:

    .. code-block:: shell

       date -s "2023-02-06 12:34:56"

    + The current system time should update to the set time, as shown below:

    .. code-block:: text

      Mon Feb  6 12:34:56 UTC 2023

    + Enter the command to set the system time to RTC:

    .. code-block:: shell

      hwclock -w -f /dev/rtc

    b) Power off and restart the device.

    c) Verify the RTC time with the following specific operations:

    + Enter the command:

    .. code-block:: shell

       hwclock -f /dev/rtc

    + The time stored in RTC should be approximately the same as the time we set, similar to the following:

    .. code-block:: text

      2023-02-06 12:35:34.485664+00:00

  3) Result: After performing the operations, if the verified RTC time is basically correct and the output during the operation meets expectations, the function is normal.


Ethernet Port
----------------

  + Interface Silkscreen: U8 (ETH1), U12 (ETH2)
  + System Interface: eth0 (ETH1), eth1 (ETH2)

**Function Test**

+ **Ethernet Port 1**

  1) Description: Test by sending ICMP packets from the development board to the PC.

  2) Operation

    a) Configure the PC's wired network card IP to 192.168.137.99.

    b) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

    c) Configure the IP of the development board's Ethernet port with the following specific configuration commands:

    .. code-block:: shell

      ifconfig eth1 down
      ifconfig eth0 up
      ifconfig eth0 192.168.137.81

    d) Execute the Ethernet port test command

    + Enter the command:

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4

    + Output information:

    .. code-block:: text

      PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
      64 bytes from 192.168.137.99: icmp_seq-1 ttl-64 time-1.35 ms
      64 bytes from 192.168.137.99: icmp_seq-2 ttl-64 time-1.35 ms

      --- 192.168.137.99 ping statistics ---
      2 packets transmitted, 2 received, 0% packet loss, time 1002ms
      rtt min/avg/max/mdev - 1.347/1.347/1.348/0.000 ms

  3) Result: "0% packet loss" indicates the test is passed.

+ **Ethernet Port 2**

  1) Description: Test by sending ICMP packets from the development board to the PC.

  2) Operation

    a) Configure the PC's wired network card IP to 192.168.137.99.

    b) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

    c) Configure the IP of the development board's Ethernet port with the following specific configuration commands:

    .. code-block:: shell

      ifconfig eth0 down
      ifconfig eth1 up
      ifconfig eth1 192.168.137.82

    d) Execute the Ethernet port test command

    + Enter the command:

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4

    + Output information:

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

| The silkscreen for the two sets of CAN interfaces can be found on the back of the development board.

**Function Test**

  1) Description: Test by using two sets of CAN buses to send and receive data from each other.

  2) Operation

    a) Use Dupont wires to connect J8: CAN2_H to CAN1_H, and CAN2_L to CAN1_L.

    b) Enter commands in the serial terminal to configure the CAN interfaces:

    .. code-block:: shell

      ip link set can0 up type can bitrate 125000
      ip link set can1 up type can bitrate 125000

    .. note:: You should see output similar to the following in the terminal: link becomes ready

    c) Enter the command in the serial terminal to make CAN1 (can0) receive data in the background:

    .. code-block:: shell

       candump can0 &

    d) Enter the command in the serial terminal to make CAN2 (can1) send test data:

    + Enter the command:

    .. code-block:: shell

       cansend can1 1F334455#1122334455667788

    + Output information:

    .. code-block:: text

      can0  1F334455   [8]  11 22 33 44 55 66 77 88

  3) Result: If the output information during the operation in step "d)" is correct, the function is normal.


I2C
-----

**Function Test**

  1) Description: Execute the I2C detection command and observe the result.

  2) Operation

    a) Detect the I2C buses of the system

    + Enter the command:

    .. code-block:: shell

        i2cdetect -l

    + The output information will be similar to the following, indicating that I2C 0, 1, 2, and HDMI adapters are detected.

    .. code-block:: text

      i2c-0	i2c       	STM32F7 I2C(0x40012000)         	I2C adapter
      i2c-3	i2c       	STM32F7 I2C(0x4c005000)         	I2C adapter
      i2c-4	i2c       	STM32F7 I2C(0x4c006000)         	I2C adapter

    b) Detect I2C devices on the bus

    + Enter the command:

    .. code-block:: shell

      i2cdetect -y 4

    .. note:: The parameter "4" in i2cdetect can be any of the bus numbers detected in the previous step, such as 0, 3, or 4.

    + The output will be similar to the following; values other than "\--" indicate that a device is detected at the corresponding address on the I2C bus.

    .. code-block:: text

           0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
      00:                         -- -- -- -- -- -- -- --
      10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
      20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
      30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
      40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
      50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
      60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- UU
      70: -- -- -- -- -- -- -- --

  3) Result: If the output information during the operation is basically consistent with expectations, the function is normal.


UART
------

+--------------+-------------------+------------------+
| Pin Location | Pin Configuration | System Interface |
+--------------+-------------------+------------------+
| P3:30        | UART7_TXD         | /dev/ttySTM7     |
+--------------+-------------------+                  +
| P3:28        | UART7_RXD         |                  |
+--------------+-------------------+                  +
| P3:26        | UART7_RTS         |                  |
+--------------+-------------------+                  +
| P3:24        | UART7_CTS         |                  |
+--------------+-------------------+------------------+
| P3:29        | UART8_TXD         | /dev/ttySTM8     |
+--------------+-------------------+                  +
| P3:27        | UART8_RXD         |                  |
+--------------+-------------------+                  +
| P3:25        | UART8_RTS         |                  |
+--------------+-------------------+                  +
| P3:23        | UART8_CTS         |                  |
+--------------+-------------------+------------------+

**Function Test**

  1) Description: Test by using the serial port to send and receive data internally (self-transmit and self-receive).

  2) Operation

    a) Use a Dupont wire to connect P3:30 and P3:28.

    b) Run the test program:

    + Enter the command:

    .. code-block:: shell

      /usr/local/my-demo/serial_test.out /dev/ttySTM7 "www.myzr.com.cn"

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

  3) Result: After performing the test operation, if the input information meets the correct expectations, the function is normal.


RS232
-------

+--------------+-------------------+------------------+
| Pin Location | Pin Configuration | System Interface |
+--------------+-------------------+------------------+
| J8:20        | RS232_RTS2        | /dev/ttySTM2     |
+--------------+-------------------+                  +
| J8:19        | RS232_CTS2        |                  |
+--------------+-------------------+                  +
| J8:18        | RS232_TX2         |                  |
+--------------+-------------------+                  +
| J8:17        | RS232_RX2         |                  |
+--------------+-------------------+------------------+
| J8:15        | RS232_TX5         | /dev/ttySTM5     |
+--------------+-------------------+                  +
| J8:14        | RS232_RX5         |                  |
+--------------+-------------------+------------------+

**Function Test**

  1) Description: Test by using the serial port to send and receive data internally (self-transmit and self-receive).

  2) Operation

    a) Use a Dupont wire to connect J8:18 and J8:17.

    b) Run the test program:

    + Enter the command:

    .. code-block:: shell

      /usr/local/my-demo/serial_test.out /dev/ttySTM2 "www.myzr.com.cn"

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

  3) Result: After performing the test operation, if the input information meets the correct expectations, the function is normal.


RS485
-------

+--------------+-------------------+------------------+
| Pin Location | Pin Configuration | System Interface |
+--------------+-------------------+------------------+
| J8:12        | B1                | /dev/ttySTM1     |
+--------------+-------------------+                  +
| J8:11        | A1                |                  |
+--------------+-------------------+------------------+
| J8:9         | B6                | /dev/ttySTM6     |
+--------------+-------------------+                  +
| J8:8         | A6                |                  |
+--------------+-------------------+------------------+

**Function Test**
  1) Use a 485-232 converter to connect B1 and A1, and connect the other end to the PC's USB port.

  2) Open the serial port debugging assistant, set the baud rate to 9600, no parity bit, 8 data bits, and 1 stop bit.

  3) Log in to the development board via SSH and send data to the PC:

  .. code-block:: shell

    echo 12323 > /dev/ttySTM1

  You should see the string "12323" received in the serial port assistant.

  4) For the development board to receive data, send data from the PC side:

  .. code-block:: shell

    cat /dev/ttySTM1 

  When the serial port assistant sends a string, the development board will receive the data:

  .. code-block:: shell

    cat /dev/ttySTM4 
    myzr 


GPIO
------

**Function Test**

+ GPIO Output Test

  1) Description: Control the output level of GPIO through the system interface.

  2) Operation

    a) List all gpiochips on the system:

    .. code-block:: shell

      gpiodetect  

    Output information:

    .. code-block:: shell

      gpiochip0 [GPIOA] (16 lines)
      gpiochip1 [GPIOB] (16 lines)
      gpiochip2 [GPIOC] (16 lines)
      gpiochip3 [GPIOD] (16 lines)
      gpiochip4 [GPIOE] (16 lines)
      gpiochip5 [GPIOF] (16 lines)
      gpiochip6 [GPIOG] (16 lines)
      gpiochip7 [GPIOH] (15 lines)
      gpiochip8 [GPIOI] (8 lines)

    b) Enter the command to control the IO to output high level, taking pin P1:6 as an example:

    .. code-block:: shell

       gpioset gpiochip0 15=1

    .. note:: At this time, using a multimeter to test P1:6, the voltage should be 3.3V.

    c) Control the IO to output low level:

    .. code-block:: shell

       gpioset gpiochip0 15=0

    .. note:: At this time, using a multimeter to test P1:6, the voltage should be 0V.

  3) Result: During the test operation, when controlling the IO level, if the measured voltage matches the expected value, the function is normal.

+ GPIO Input Test

  1) Description: Configure and read the input level of GPIO through the system interface.

  2) Operation

    a) Use a Dupont wire or jumper cap to connect pins P1:34 and P1:36.

    b) Enter the following command to read the level of pin P1:34, which is PH8.

    .. code-block:: shell

      gpioget gpiochip7 8

    Output information:

    .. code-block:: shell

      0

    This indicates that the PH8 pin is read as low level.

    c) Use a Dupont wire to connect P1:34 and P1:4 to apply 3.3V voltage, and enter the following command again

    .. code-block:: shell

      gpioget gpiochip7 8

    Output information:

    .. code-block:: shell

      1

    This indicates that high level is read.

  3) Result: During the test operation, if the read level meets the correct expectations, the function is normal.


SPI
-----

**Function Test**

  1) Description: Send a string through the SPI interface.

  2) Operation

    a) Short-circuit pins P3:6 and P3:8, and enter the following command:

    .. code-block:: shell

      /usr/local/my-demo/spidev_test.out -D /dev/spidev0.0

    b) The following output information indicates that SPI sending and receiving are normal:

    .. code-block:: shell

      spi mode: 0
      bits per word: 8
      max speed: 500000 Hz (500 KHz)

      FF FF FF FF FF FF 
      40 00 00 00 00 95 
      FF FF FF FF FF FF 
      FF FF FF FF FF FF 
      FF FF FF FF FF FF 
      DE AD BE EF BA AD 
      F0 0D 

  3) Result: If the displayed output information meets the correct expectations, it indicates that the transmission is successful.


USB WiFi
----------

+ Interface Silkscreen: U19

**Function Test**

  1) Description: After the WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal.

  2) Operation:
    a) Connect the WIFI antenna to the "E2" interface
    b) Generate the WPA PSK file for the SSID, enter:

    .. code-block:: shell

      wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf

    c) Connect:

    .. code-block:: shell

      wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf 

    d) Obtain IP:

    .. code-block:: shell

      udhcpc -i wlan0

    e) Test the connection:

    .. code-block:: shell

      ping -I wlan0 www.baidu.com


USB Bluetooth
---------------

+ Interface Silkscreen: U19

**Function Test**

  1) Description: After scanning for Bluetooth devices, send an L2CAP echo request and receive a response.

  2) Operation:
    a) Connect the antenna to the "E2" interface
    b) Start Bluetooth:

    .. code-block:: shell

      hciconfig hci0 up

    c) Scan for external Bluetooth devices:

    .. code-block:: shell

       hcitool scan 

    The Bluetooth address of my phone is scanned:

    .. code-block:: shell

       88:46:04:4C:11:A7   Redmi K40

    d) Send an L2CAP packet test:

    .. code-block:: shell

      l2ping 88:46:04:4C:11:A7

    Successful connection display:

    .. code-block:: shell

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


TF Card
----------

+ Interface Silkscreen: J16

**Function Test**

  .. note:: The TF card interface of the device supports hot swapping, and the TF card slot is self-ejecting.

+ TF Card Insertion Test

  1) Description: Insert the TF card and observe whether the device can correctly recognize the card.

  2) Operation

    a) Take a TF card and insert it into the TF card interface of the device.

    b) The output information will be similar to the following:

    .. code-block:: text

      ...
      mmc1: new ultra high speed SDR104 SDHC card at address 0001
      mmcblk1: mmc1:0001 SD16G 14.9 GiB
      ...

  3) Result: After the operation, if the output information meets the correct expectations, it indicates that the TF card is correctly recognized.

+ TF Card Ejection Test

  1) Eject the TF card and observe whether the device can respond correctly.

  2) Operation

    a) Press inward in the direction of TF card insertion (release after hearing a "click" sound, and the TF card will eject).

    b) The output information will be similar to the following:

    .. code-block:: text

      ...
      mmc1: card 0001 removed
      ...

  3) Result: If the phenomenon during the operation meets the correct expectations, it indicates that the TF hot swapping is normal.


USB 2.0
---------

+ Interface Silkscreen: J4

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


ADC
-----

+ Interface Silkscreen: P1:27, P1:29

**Function Test**

  1) First, find the peripheral corresponding to ADC:

  .. code-block:: shell

    grep -H "" /sys/bus/iio/devices/*/name | grep adc

  Output:

  .. code-block:: shell

    /sys/bus/iio/devices/iio:device0/name:48003000.adc:adc@0

  2) Perform a conversion on the ADC, and read the scale and offset of the ADC:

  .. code-block:: shell

    cd /sys/bus/iio/devices/iio\:device0/
    cat in_voltage6_raw 			//Obtain data on adc1 channel 6 (raw value)
    4095
    cat in_voltage_scale 			//Read scale
    0.805664062
    cat in_voltage_offset 		//Read offset
    0
    awk "BEGIN{printf (\"%d\n\", (4095 + 0) * 0.805664062)}"		//Calculate actual value
    3299			//3299mv


4G Mode EC20
---------------

+ Interface Silkscreen: J7

**Function Test**

  1) Connect the 4G module EC20, connect the 4G antenna and SIM card

  2) Start the development board.
  
  3) Enter the following command to dial:

  .. code-block:: shell

    ./quectel-CM &

  4) Obtain IP

  .. code-block:: shell

    udhcpc -i usb0

  5) Test the connection status

  .. code-block:: shell

    ping -I usb0 www.baidu.com