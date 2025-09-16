Test Manual
=============

Serial Port
-------------

+ Interface silk screen: J26

**Functional Test**

  1) Description: Test using the serial port's self-transmit and self-receive method.

  2) Operation

    a) Use a DuPont line to connect the RX and TX pins of J26 UART4.

    b) Run the test program:

    + Enter the command:

    .. code-block:: shell

      ./serial_test.out /dev/ttyS4 "www.myzr.com"

    + Output information:

    .. code-block:: text

      send dat/a...finish
      Starting receive data:
      serial@fe680000' missing or empty
      [ 1827.195188] ttyS4 - failed to request DMA, use interrupt mode
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
      ASCII: 0x0 	 Character:  

  3) Result: After performing the test operation, if the input information matches the correct expectations, the function is normal.

RTC
-----

+ Device interface: /dev/rtc

+ Test description: The RTC test requires installing a button battery, and the battery is located at the silk screen BT1.

**Functional Test**

+ **RTC Time**

  1) Description: Set the RTC time, then power off and restart to check the RTC time.

  2) Operation

    a) Set the RTC time, with specific operations as follows:

    + Enter the command to update the system time:

    .. code-block:: shell

       date -s "2023-02-06 12:34:56"

    + You can see that the current system time is updated to the set time:

    .. code-block:: text

      Mon Feb  6 12:34:56 UTC 2023

    + Enter the command to set the system time to RTC:

    .. code-block:: shell

      hwclock -w -f /dev/rtc1

    b) Power off and restart the device.

    c) Check the RTC time, with specific operations as follows:

    + Enter the command:

    .. code-block:: shell

       hwclock -f /dev/rtc1

    + You can see that the time stored in RTC is basically the same as the time we set, similar to the following:

    .. code-block:: text

      2023-02-06 12:35:34.485664+00:00

  3) Result: After performing the operation, if the checked RTC time is basically correct and the output during the operation meets expectations, the function is normal.


Ethernet Port
---------------

  + Interface silk screen: J13 (ETH1), J14 (ETH2)
  + System interface: eth1 (ETH1), eth0 (ETH2)

**Functional Test**

+ **Ethernet Port 1**

  1) Description: Test by sending ICMP packets from the development board to the PC.

  2) Operation

    a) Configure the computer's wired network card IP to 192.168.137.99.

    b) Connect this Ethernet port of the development board to the computer's Ethernet port with a network cable.

    c) Configure the development board's Ethernet port IP, with specific configuration commands as follows:

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

    a) Configure the computer's wired network card IP to 192.168.137.99.

    b) Connect this Ethernet port of the development board to the computer's Ethernet port with a network cable.

    c) Configure the development board's Ethernet port IP, with specific configuration commands as follows:

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

  + Interface silk screen: J3
  + System interface: can0

**Functional Test**

  1) Description: Test using two development boards with CAN bus for mutual transmission and reception.

  2) Operation

    a) Use DuPont lines to connect CAN_L to CAN_L and CAN_H to CAN_H.

    b) Enter commands in the serial terminals of the two development boards to configure the CAN interface:

    .. code-block:: shell

      ip link set can0 up type can bitrate 1000000 dbitrate 3000000 fd on

    .. note:: You can see the terminal output similar to: link becomes ready

    c) Enter the command in one of the serial terminals to enable background reception:

    .. code-block:: shell

       candump can0 &

    d) Enter the command in the other serial terminal to send test data:

    + Enter the command:

    .. code-block:: shell

       cansend can0 1F334455#1122334455667788

    + Output information:

    .. code-block:: text

      can0  1F334455   [8]  11 22 33 44 55 66 77 88

  3) Result: If the output information is correct during operation "d)", the function is normal.



RS485
-------

  + Interface silk screen: J29
  + System interface: ttyS7


**Functional Test**

  1) Use a 485-232 converter to connect B1 and A1, and connect the other end to the computer's USB port.

  2) Open the serial debugging assistant, set the baud rate to 9600, no parity bit, 8 data bits, and 1 stop bit.

  3) The development board receives data, and the computer sends data:

  .. code-block:: shell

    cat /dev/ttyS7 

  You can see that the development board receives the string "0123456789abcdefghijklmnopqrstuvwxyz"

  .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-RS485-1.png
   :alt: image-RK3568-RS485-1.png

  4) The development board sends data, and the computer receives data:

  .. code-block:: shell

    echo 22 > /sys/class/gpio/export
    echo  out > /sys/class/gpio/gpio22/direction 
    echo 1 > /sys/class/gpio/gpio22/value
    echo jkljkl > /dev/ttyS7

  You can see that the serial assistant receives the data:

  .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-RS485-2.png
   :alt: image-RK3568-RS485-2.png


Audio
-------

+ Interface silk screen: P15

**Functional Test**

  1) Description: Test by playing an audio file.

  2) Operation

    a) Insert headphones or a speaker into the interface corresponding to the silk screen P15.

    b) Enter the command to test:

    .. code-block:: shell

      aplay /mytest.wav

  3) Result: When executing the test command, if sound can be heard from the headphones, the function is normal.


Recording
-----------

+ Interface silk screen: P15

**Functional Test**

  1) Description: Test by recording and playing the recorded file.

  2) Operation

    a) Insert headphones or a speaker into the interface corresponding to the silk screen P15.

    b) Enter the command to test:

    .. code-block:: shell

      arecord -d 4 record.wav
      aplay record.wav

  3) Result: When executing the test command, if the recorded sound can be heard from the headphones, the function is normal.


USB 2.0
---------

+ Interface silk screen: P4

**Functional Test**

  1) Description: Test by plugging and unplugging a USB storage device (USB flash drive).

  2) Operation:

    a) Insert the USB device into the bottom board's USB interface, and the system will output information similar to the following:

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

    b) Pull the USB device out of the bottom board, and the system will output information similar to the following:

    .. code-block:: text

      [ 2690.764161] usb 2-1.1: USB disconnect, device number 3


TF Card
---------

+ Interface silk screen: J12

**Functional Test**

  .. note:: The TF card interface of the device supports hot swapping, and the TF card slot is self-ejecting.

+ TF Card Insertion Test

  1) Description: Insert the TF card and observe whether the device can correctly recognize the card.

  2) Operation

    a) Take a TF card and insert it into the device's TF card interface.

    b) The output information is similar to the following:

    .. code-block:: text

      ...
      mmc1: new ultra high speed SDR104 SDHC card at address 0001
      mmcblk1: mmc1:0001 SD16G 14.9 GiB
      ...

  3) Result: After the operation, if the output information meets the correct expectations, it indicates that the TF card is correctly recognized.

+ TF Card Ejection Test

  1) Eject the TF card and observe whether the device can respond correctly.

  2) Operation

    a) Press inward in the direction of TF card insertion (release after hearing a "click" sound, and the TF card will pop out).

    b) The output information is similar to the following:

    .. code-block:: text

      ...
      mmc1: card 0001 removed
      ...

  3) Result: If the phenomenon during the operation meets the correct expectations, it indicates that the TF hot swapping is normal.


Infrared
----------

+ Interface silk screen: IR1

**Functional Test**

1) Description: Print corresponding data by receiving infrared information.

  2) Operation

    a) Prepare an infrared remote control or a mobile phone's infrared remote control app.

    b) Turn on the relevant print switch on the development board:

    .. code-block:: text

      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/code_print
      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/dbg_level

    c) Use the remote control to point at the infrared interface and press any button.

    d) If the development board returns relevant button information, it means the reception is successful.


WiFi
------

+ Interface silk screen: U2

**Functional Test**

  1) Description: After the WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal.

  2) Operation:
    a) Connect the WIFI antenna to the "U12" interface.
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


Bluetooth
-----------

+ Interface silk screen: U2

**Functional Test**

  1) Description: After scanning for Bluetooth devices, send an L2CAP echo request and receive the reply.

  2) Operation:
    a) Connect the antenna to the "U12" interface.
    b) Initialize and start Bluetooth:

    .. code-block:: shell
      
      /lib/firmware/bluetooth.sh
      hciconfig hci0 up

    c) Scan for external Bluetooth devices:

    .. code-block:: shell

       hcitool