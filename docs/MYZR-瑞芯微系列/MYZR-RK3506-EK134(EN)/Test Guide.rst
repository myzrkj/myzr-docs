Test Guide
============

Ethernet Port Test
--------------------

Ethernet Port 1
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: U9
|   System Interface: eth0
|   Test Description: Test by sending ICMP packets from the development board to the PC

|   Test Operations

1. Configure the PC's wired network card IP to 192.168.137.99
2. Use an Ethernet cable to connect the development board's Ethernet port to the PC's Ethernet port
3. Check the information of Ethernet Port 1 on the development board, enter the following command:

.. code-block:: shell

    ifconfig eth0

4. Configure the IPv4 IP of Ethernet Port 1, enter the following command:

.. code-block:: shell

    ifconfig eth0 192.168.137.18 netmask 255.255.255.0

5. Check the information of Ethernet Port 1 on the development board again to confirm whether the IPv4 address is configured successfully. If the configuration fails, re-execute the operations starting from Step 4. Enter the following command:

.. code-block:: shell

    ifconfig eth0

6. Enter the following command to verify Ethernet Port 1:

.. code-block:: shell

    ping -I eth0 192.168.137.99 -c 3

|   "0% packet loss" indicates the test is passed


Ethernet Port 2
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: U5
|   System Interface: eth1
|   Test Description: Test by sending ICMP packets from the development board to the PC

|   Test Operations

1. Configure the PC's wired network card IP to 192.168.137.99
2. Use an Ethernet cable to connect the development board's Ethernet port to the PC's Ethernet port
3. Check the information of Ethernet Port 2 on the development board, enter the following command:

.. code-block:: shell

    ifconfig eth1

4. Configure the IPv4 IP of Ethernet Port 2, enter the following command:

.. code-block:: shell

    ifconfig eth1 192.168.137.22 netmask 255.255.255.0

5. Check the information of Ethernet Port 2 on the development board again to confirm whether the IPv4 address is configured successfully. If the configuration fails, re-execute the operations starting from Step 4. Enter the following command:

.. code-block:: shell

    ifconfig eth1

6. Enter the following command to verify Ethernet Port 2:

.. code-block:: shell

    ping -I eth1 192.168.137.99 -c 3

|   "0% packet loss" indicates the test is passed


USB Test
-----------

|   Interface Silkscreen: J1
|   Test Description: Test by plugging and unplugging a USB storage device (USB flash drive)

|   Test Operations

1. Insert the USB flash drive into the USB interface of the baseboard, and the system will output information similar to the following:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/测试1.png
   :alt: 测试1.png

2. Unplug the USB flash drive from the baseboard, and the system will output information similar to the following:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/测试2.png
   :alt: 测试2.png

SD Interface Test
--------------------

|   Interface Silkscreen: J12
|   Test Description: Test by plugging and unplugging a TF card

|   Test Operations

1. Install the TF card into the SD interface, and the development board will output the following information:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/测试3.png
   :alt: 测试3.png

2. Unplug the TF card, and the output information is as follows:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/测试4.png
   :alt: 测试4.png

Audio Playback Test
----------------------

|   Interface Silkscreen: P1
|   Test Description: Verify the audio playback function of the development board by playing audio files

|   Test Operations

1. Connect headphones or a speaker to the interface corresponding to the silkscreen
2. Enter the following command to perform the test:

.. code-block:: shell

    aplay ./mytest.wav

|   Audio output from the headphones or speaker indicates the audio playback test is passed

Recording Test
----------------

|   Interface Silkscreen: P1
|   Test Description: Test by recording and playing back the recorded file

|   Test Operations

1. Insert headphones with a MIC into the interface corresponding to the silkscreen
2. Enter the following command to record for 4 seconds:

.. code-block:: shell

    arecord -d 4 -f S16_LE record.wav

3. Play back the recorded audio file, enter the following command:

.. code-block:: shell

    aplay record.wav

|   Playback of the recorded sound from the headphones indicates the recording test is passed


M.2 Interface Test
---------------------

|   Interface Silkscreen: J7
|   Test Description: Check the mounting status after mounting the hard drive

|   Test Operations

1. Power off the development board, connect the M.2 interface hard drive, and then start the development board
2. Create a mount point and mount the hard drive, enter the following commands:

.. code:: shell

    mkdir /nvme    
    mount /dev/nvme0n1p1 /nvme/

3. Check the mounting status, enter the following command:

.. code:: shell

    df -h

4. If the mounting is successful, output information similar to the following can be obtained:

.. code:: shell

    /dev/nvme0n1p1  499M  10M  490M  2%  /nvme

5. Unmount the hard drive, enter the following command:

.. code:: shell

    umount /nvme

UART Test
-----------

|   Interface Silkscreen: J14
|   Test Description: Test by means of UART self-transmission and self-reception

|   Test Operations

1. Short-circuit the pins J14-33 (UART3_TX_M1) and J14-35 (UART3_RX_M1)
2. Enter the following command to perform the transmission and reception test:

.. code-block:: shell

    ./serial_test.out /dev/ttyS3 "myzr"

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/测试5.png
   :alt: 测试5.png

|   After executing the test command, output of information similar to the above indicates the UART test is passed. Press 'Ctrl + C' to exit.


SPI Interface Test
--------------------

|   Interface Silkscreen: J14
|   Test Description: Test by means of SPI self-transmission and self-reception

|   Test Operations

1. Short-circuit the pins J14-19 (HDMIRX_INT_L_GPIO4_C3) and J14-21 (UART9_TX_M1)
2. Enter the following command to perform the transmission and reception test:

.. code-block:: shell

    ./spidev_test -D /dev/spidev3.0

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK320/测试6.png
   :alt: 测试6.png

|   After executing the test command, output of information similar to the above indicates the SPI test is passed.


Infrared Test
----------------

|   Interface Silkscreen: IR1
|   Test Description: Receive infrared information and print the corresponding data

|   Test Operations

1. Prepare an infrared remote control or a mobile phone with an infrared remote control app
2. Enable the relevant print switch, enter the following commands:

.. code-block:: shell

    echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/code_print
    echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/dbg_level

3. Aim the remote control at the infrared interface and press any button
4. The development board successfully receives the infrared signal if it displays the corresponding button information.


Display Screen
-----------------

|   Interface Silkscreen: J2
|   Test Description: Check whether the display screen shows normally when the development board is powered on and started

|   Test Operations

1. Connect an HDMI interface screen to the HDMI interface on the development board, and start the development board

|   Normal display on the screen indicates the test is passed