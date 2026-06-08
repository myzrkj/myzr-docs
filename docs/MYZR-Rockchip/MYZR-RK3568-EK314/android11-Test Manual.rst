Test Manual
=============

RTC
-----

+ Test Description: The RTC test requires installing a button battery, which is located at the silkscreen BT1.

**Functional Test**

+ **RTC Time**

  1) Description: Set the RTC time, then check the RTC time after powering off and restarting.

  2) Operation

    a) Click the Clock APP to view the current time:

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-clock-1.png
      :alt: image-RK3568-android11-clock-1.png

    b) Power off and restart the device.

    c) Check the time again:

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-clock-2.png
      :alt: image-RK3568-android11-clock-2.png

  3) Result: After performing the operations, if the RTC time is basically correct and the output during the operation meets expectations, the function is normal.


Ethernet Port
---------------

  + Interface Silkscreen: J13 (ETH1), J14 (ETH2)
  + System Interface: eth0 (ETH1), eth1 (ETH2)

**Functional Test**

+ **Ethernet Port 1**

  1) Description: Test by sending ICMP packets from the development board to the PC.

  2) Operation

    a) Configure the PC's wired network card IP to 192.168.137.99.

    b) Connect this Ethernet port of the development board to the PC's Ethernet port with a network cable.

    c) Execute the Ethernet port test command

    + Input command:

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

    b) Connect this Ethernet port of the development board to the PC's Ethernet port with a network cable.

    c) Execute the Ethernet port test command

    + Input command:

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


RS485
-------

  + Interface Silkscreen: J29
  + System Interface: ttyS7


**Functional Test**
  1) Use a 485-232 converter to connect B1 and A1, and connect the other end to the computer's USB port.

  2) Open the serial port debugging assistant, set the baud rate to 9600, no parity bit, 8 data bits, and 1 stop bit.

  3) The development board receives data, and the computer sends data:

  .. code-block:: shell

    cat /dev/ttyS7 

  The development board can receive the string "0123456789abcdefghijklmnopqrstuvwxyz"

  .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-RS485-1.png
   :alt: image-RK3568-RS485-1.png

  4) The development board sends data, and the computer receives data:

  .. code-block:: shell

    echo 22 > /sys/class/gpio/export
    echo  out > /sys/class/gpio/gpio22/direction 
    echo 1 > /sys/class/gpio/gpio22/value
    echo jkljkl > /dev/ttyS7

  The serial assistant can receive the data:

  .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-RS485-2.png
   :alt: image-RK3568-RS485-2.png


USB Drive Connection
----------------------

+ Interface Silkscreen: P4

**Functional Test**

1) Description: Test by plugging and unplugging a USB storage device (USB drive).

2) Operation:

  a) Insert the USB drive into the base board's USB interface.

  b) The drop-down notification bar displays the USB drive information.

  .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-USB-1.jpg
    :alt: image-RK3568-android11-USB-1.jpg    

  c) To remove the USB drive, click the eject button.


Mouse and Keyboard Connection
-------------------------------

+ Interface Silkscreen: P4/J2

**Functional Test**

  1) Operation:

    a) Insert the mouse interface into the P4 USB 2.0 interface, and the keyboard interface into the J2 USB 3.0 interface.

    b) Connect the P1 jumper cap's USB OTG to GND to enter USB host mode.

    c) Click the search bar, the keyboard pops up, and test whether the mouse and keyboard are usable.

  .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-USB-2.jpg
   :alt: image-RK3568-android11-USB-2.jpg    


Image Viewing
---------------

**Functional Test**

  1) Operation:

    a) Put images into the USB drive and connect the USB drive.

    b) In File Explorer 》USB, enter the USB drive directory.

      .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-picture-1.jpg
        :alt: image-RK3568-android11-picture-1.jpg 

    c) Open the image.

      .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-picture-2.jpg
        :alt: image-RK3568-android11-picture-2.jpg 


Audio Playback
----------------

**Functional Test**

  1) Operation:

    a) Put audio files into the USB drive and connect the USB drive.

    b) In File Explorer 》USB, enter the USB drive directory.

    c) Open the audio file.

      .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-music-1.jpg
        :alt: image-RK3568-android11-music-1.jpg


Video Playback
----------------

**Functional Test**

  1) Operation:

    a) Put video files into the USB drive and connect the USB drive.

    b) In File Explorer 》USB, enter the USB drive directory.

    c) Open the video file.

      .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-movies-1.jpg
        :alt: image-RK3568-android11-movies-1.jpg


TF Card
---------

+ Interface Silkscreen: J12

**Functional Test**

1) Description: Insert the TF card and observe whether the device can correctly recognize the card.

2) Operation:

  a) Take a TF card and insert it into the device's TF card interface.

  b) The drop-down notification bar displays the TF card information.

  .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-TFcard-1.jpg
    :alt: image-RK3568-android11-TFcard-1.jpg   

  c) To remove the TF card, click the eject button.


Infrared
----------

+ Interface Silkscreen: IR1

**Functional Test**

1) Description: Receive infrared information and print the corresponding data.

  2) Operation

    a) Prepare an infrared remote control or a mobile phone's infrared remote control app.

    b) Turn on the relevant printing switch on the development board:

    .. code-block:: text

      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/code_print
      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/dbg_level

    c) Aim the remote control at the infrared interface and press any button.

    d) If the development board displays the relevant button information, it means the reception is successful.


M.2 Hard Drive
----------------

+ Interface Silkscreen: J18

**Functional Test**

  1) Connect the M.2 hard drive.

  2) Start the development board.
  
  3) Enter the following command to view PCI bus devices:

  .. code-block:: shell

    lspci

  Output

  .. code-block:: shell

    21:00.0 Class 0108: 126f:2263
    20:00.0 Class 0604: 1d87:3566


  4) The system will automatically mount the hard drive.

  5) Check the mounting status.

  .. code-block:: shell

    df -h

  6) The following similar information can be seen:

  .. code-block:: shell

    /dev/block/vold/public:259,1 119G  108M  119G   1% /mnt/media_rw/BC98ABC698AB7E10

  7) Interface view: The USB folder can be seen in File Explorer, which is the hard drive mounting directory. Its operation is similar to that of a USB drive.


SATA Hard Drive
-----------------

+ Interface Silkscreen: J20, J21

**Functional Test**

  1) Connect the SATA hard drive.

  2) Start the development board.
  
  3) The system will automatically mount the hard drive.

  4) Check the mounting status.

  .. code-block:: shell

    df -h

  5) The following can be seen:

  .. code-block:: shell

    /dev/block/vold/public:8,1 932G   15G  916G   2% /mnt/media_rw/863AAAA43AAA912B

  6) Interface view: The USB folder can be seen in File Explorer, which is the hard drive mounting directory. Its operation is similar to that of a USB drive.


WIFI
-------

+ Interface Silkscreen: U2

**Functional Test**

  1) Operation:

    a) Connect the WIFI antenna to the "U12" interface.

    b) Long-press WLAN in the drop-down box to enter the WIFI settings interface.

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-wifi-1.png
      :alt: image-RK3568-android11-wifi-1.png

    c) Select the WIFI, enter the password to connect.

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-wifi-2.png
      :alt: image-RK3568-android11-wifi-2.png

    d) After successful connection, website browsing can be tested.

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-wifi-4.png
      :alt: image-RK3568-android11-wifi-4.png


Bluetooth
-----------

+ Interface Silkscreen: U2

**Functional Test**

  1) Operation:

    a) Connect the WIFI antenna to the "U12" interface.

    b) Long-press Bluetooth in the drop-down box to enter the Bluetooth settings interface.

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-BL-1.png
      :alt: image-RK3568-android11-BL-1.png

    c) Click "Pair with new device".

    d) Select a mobile phone or other Bluetooth devices to pair.

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-BL-2.png
      :alt: image-RK3568-android11-BL-2.png

    e) After successful pairing with a Bluetooth headset, it will show "In use".

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-BL-3.png
      :alt: image-RK3568-android11-BL-3.png


5G
----

+ Interface Silkscreen: U58

**Functional Test**

  1) Connect the 5G module RM500Q, 5G antenna, and SIM card.

  2) Start the development board.

  3) A 5G icon can be seen in the upper right corner.

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-5g-1.jpg
      :alt: image-RK3568-android11-5g-1.jpg

  4) Website browsing can be tested.

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-5g-2.png
      :alt: image-RK3568-android11-5g-2.png
