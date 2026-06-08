Test Manual
============


RTC
-----

+ Test Description: The RTC test requires installing a button battery, and the battery is located at the silkscreen **BT1**.

**Functional Test**

+ **RTC Time**

  1) Description: Set the RTC time, then power off and restart the device, and check the RTC time again.

  2) Operation

    a) Click the Clock APP to view the current time:

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-clock-1.png
      :alt: image-RK3588-android12-clock-1.png

    b) Power off and restart the device.

    c) Check the time again:

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-clock-2.png
      :alt: image-RK3588-android12-clock-2.png

  3) Result: After performing the operations, if there is no obvious issue with the RTC time and the output during the operation meets expectations, the function is normal.


Ethernet Port
---------------

  + Interface Silkscreen: J14 (ETH1), J15 (ETH2)
  + System Interface: eth0 (ETH1), eth1 (ETH2)

**Functional Test**

+ **Ethernet Port 1**

  1) Description: Test by sending ICMP packets from the development board to the PC.

  2) Operation

    a) Configure the PC's wired network card IP to **192.168.137.99**.

    b) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

    c) Execute the Ethernet port test command

    + Input Command:

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

  1) Description: Test by sending ICMP packets from the development board to the PC.

  2) Operation

    a) Configure the PC's wired network card IP to **192.168.137.99**.

    b) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

    c) Execute the Ethernet port test command

    + Input Command:

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



USB Flash Drive Connection
-----------------------------

+ Interface Silkscreen: P2, P3, J3

**Functional Test**

|  1) Description: Test by plugging and unplugging a USB storage device (USB flash drive).

|  2) Operation:

|    a) Insert the USB flash drive into the USB interface of the baseboard.

|    b) The USB flash drive information appears in the drop-down notification bar.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-USB-1.png
  :alt: image-RK3588-android12-USB-1.png    

|    c) To remove the USB flash drive, click the eject button.


Mouse and Keyboard Connection
--------------------------------

+ Interface Silkscreen: P2, P3, J3

**Functional Test**

|  1) Operation:

|    a) Insert the mouse interface into the P2, P3, or J3 USB interface, and insert the keyboard interface into the P2, P3, or J3 USB interface.

|    b) Click the search bar, the keyboard will pop up, and test whether the mouse and keyboard are usable.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-USB-2.jpg
  :alt: image-RK3568-android11-USB-2.jpg    


Image Viewing
---------------

**Functional Test**

|  1) Operation:

|    a) Place images in the USB flash drive and connect the USB flash drive to the device.

|    b) In File Explorer 》 USB, access the USB flash drive directory.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-picture-1.jpg
  :alt: image-RK3568-android11-picture-1.jpg 

|    c) Open the images.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-picture-2.jpg
  :alt: image-RK3568-android11-picture-2.jpg 


Audio Playback
-----------------

**Functional Test**

|  1) Operation:

|    a) Place audio files in the USB flash drive and connect the USB flash drive to the device.

|    b) In File Explorer 》 USB, access the USB flash drive directory.

|    c) Open the audio files.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-music-1.jpg
  :alt: image-RK3568-android11-music-1.jpg


Video Playback
-----------------

**Functional Test**

|  1) Operation:

|    a) Place video files in the USB flash drive and connect the USB flash drive to the device.

|    b) In File Explorer 》 USB, access the USB flash drive directory.

|    c) Open the video files.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-movies-1.jpg
  :alt: image-RK3568-android11-movies-1.jpg


TF Card
---------

+ Interface Silkscreen: J5

**Functional Test**

|  1) Description: Insert a TF card and check if the device can recognize the card correctly.

|  2) Operation:

|    a) Take a TF card and insert it into the TF card interface of the device.

|    b) The TF card information appears in the drop-down notification bar.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-TFcard-1.png
  :alt: image-RK3588-android12-TFcard-1.png  

|    c) To remove the TF card, click the eject button.


Infrared (IR)
---------------

+ Interface Silkscreen: IR1

**Functional Test**

  1) Description: Receive infrared information and print the corresponding data.

  2) Operation

    a) Prepare an infrared remote control or a mobile phone with an infrared remote control app.

    b) Enable the relevant print switch on the development board:

    .. code-block:: text

      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/code_print
      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/dbg_level

    c) Aim the remote control at the infrared interface and press any button.

    d) If the development board displays the corresponding button information, it means the infrared signal is received successfully.


M2 Hard Drive
---------------

+ Interface Silkscreen: J21

**Functional Test**

  1) Connect the M2 hard drive to the device.

  2) Start the development board.
  
  3) Enter the following command to view PCI bus devices:

  .. code-block:: shell

    lspci

  Output

  .. code-block:: shell

    01:00.0 Class 0108: 126f:2263
    00:00.0 Class 0604: 1d87:3588


  4) The system will automatically mount the hard drive.

  5) Check the mounting status.

  .. code-block:: shell

    df -h

  6) The following similar information should be displayed:

  .. code-block:: shell

    /dev/block/vold/public:259,1 119G 108M  119G   1% /mnt/media_rw/BC98ABC698AB7E10
    /dev/fuse                    119G 108M  119G   1% /mnt/user/0/BC98ABC698AB7E10

  7) Interface Check: A "USB" folder can be found in File Explorer, which is the mount directory of the hard drive. Its operation is similar to that of a USB flash drive.


SATA Hard Drive
-----------------

+ Interface Silkscreen: J18, J2

**Functional Test**

  1) Connect the SATA hard drive to the device.

  2) Start the development board.
  
  3) The system will automatically mount the hard drive.

  4) Check the mounting status.

  .. code-block:: shell

    df -h

  5) The following information should be displayed:

  .. code-block:: shell

    /dev/block/vold/public:8,1 932G  15G  916G   2% /mnt/media_rw/863AAAA43AAA912B
    /dev/fuse                  932G  15G  916G   2% /mnt/user/0/863AAAA43AAA912B

  6) Interface Check: A "USB" folder can be found in File Explorer, which is the mount directory of the hard drive. Its operation is similar to that of a USB flash drive.


WIFI
------

+ Interface Silkscreen: U27

**Functional Test**

|  1) Operation:

|    a) Connect the WIFI antenna to the "ANT2/ANT1" interface.

|    b) On the desktop, click "Settings" 》 "Network & Internet" 》 "Internet".

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-wifi-1.png
  :alt: image-RK3588-android12-wifi-1.png

|    c) Select the WIFI, enter the password, and connect.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-wifi-2.png
  :alt: image-RK3588-android12-wifi-2.png

|    d) After successful connection, perform a website browsing test.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-wifi-3.png
  :alt: image-RK3588-android12-wifi-3.png


Bluetooth
-----------

+ Interface Silkscreen: U27

**Functional Test**

|  1) Operation:

|    a) Connect the WIFI antenna to the "ANT2/ANT3" interface.

|    b) Long-press Bluetooth in the drop-down bar to enter the Bluetooth settings interface.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-BL-1.png
  :alt: image-RK3588-android12-BL-1.png

|    c) Click "Pair new device".

|    d) Select a mobile phone or other Bluetooth devices to pair with.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-BL-2.png
  :alt: image-RK3588-android12-BL-2.png

|    e) After successful pairing with the Bluetooth headset, it will display "In use".

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-BL-3.png
  :alt: image-RK3588-android12-BL-3.png


5G
-----

+ Interface Silkscreen: J19

**Functional Test**

| 1) Connect the 5G module RM500Q, 5G antenna, and SIM card to the device.

| 2) Start the development board.

| 3) A 5G icon should appear in the upper right corner.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-5g-1.jpg
  :alt: image-RK3588-android12-5g-1.jpg

| 4) Perform a website browsing test.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-5g-2.png
  :alt: image-RK3588-android12-5g-2.png
