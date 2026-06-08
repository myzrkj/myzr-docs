Test Guide
============

Ethernet Port Test
--------------------

Ethernet Port 1
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: U9
|   System Interface: eth0
|   Test Description: The test is performed by having the development board send ICMP packets to the PC.

|   Test Operations

1. Configure the computer's wired network card IP to 192.168.137.99
2. Use a network cable to connect the development board's Ethernet port to the computer's Ethernet port
3. Check the information of Ethernet Port 1 on the development board by entering the following command:

.. code-block:: shell

    ifconfig eth0

4. Configure the IPv4 address for Ethernet Port 1 by entering the following command:

.. code-block:: shell

    ifconfig eth0 192.168.137.18 netmask 255.255.255.0

5. Check the information of Ethernet Port 1 on the development board again to confirm whether the IPv4 address is successfully configured. If not, re - execute the operation starting from step 4. Enter the following command:

.. code-block:: shell

    ifconfig eth0

6. Enter the following command to verify Ethernet Port 1:

.. code-block:: shell

    ping -I eth0 192.168.137.99 -c 3

|   "0% packet loss" indicates that the test is passed



Ethernet Port 2
~~~~~~~~~~~~~~~~~

|   Interface Silkscreen: U5
|   System Interface: eth1
|   Test Description: The test is performed by having the development board send ICMP packets to the PC.

|   Test Operations

1. Configure the computer's wired network card IP to 192.168.137.99
2. Use a network cable to connect the development board's Ethernet port to the computer's Ethernet port
3. Check the information of Ethernet Port 2 on the development board by entering the following command:

.. code-block:: shell

    ifconfig eth1

4. Configure the IPv4 address for Ethernet Port 2 by entering the following command:

.. code-block:: shell

    ifconfig eth1 192.168.137.22 netmask 255.255.255.0

5. Check the information of Ethernet Port 2 on the development board again to confirm whether the IPv4 address is successfully configured. If not, re - execute the operation starting from step 4. Enter the following command:

.. code-block:: shell

    ifconfig eth1

6. Enter the following command to verify Ethernet Port 2:

.. code-block:: shell

    ping -I eth1 192.168.137.99 -c 3

|   "0% packet loss" indicates that the test is passed


USB Test
----------

|   Interface Silkscreen: J1
|   Test Description: The test is performed by plugging and unplugging a USB storage device (USB flash drive).

|   Test Operations

1. Insert the USB flash drive into the USB interface of the base board, and the system will output information similar to the following


2. Pull the USB flash drive out of the base board, and the system will output information similar to the following


SD Interface Test
--------------------

|   Interface Silkscreen: J12
|   Test Description: The test is performed by plugging and unplugging a TF card.

|   Test Operations

1. Install the TF card into the SD interface, and the development board will output the following information:


2. Pull out the TF card, and the output information is as follows:


Audio Playback Test
---------------------

|   Interface Silkscreen: P1
|   Test Description: Play an audio file to verify the audio playback function of the development board.

|   Test Operations

1. Connect headphones or speakers to the interface corresponding to the silkscreen
2. Enter the following command for testing:

.. code-block:: shell

    aplay ./mytest.wav

|   Sound output from the headphones or speakers indicates that the audio playback test is passed

Recording Test
-----------------

|   Interface Silkscreen: P1
|   Test Description: Record and play the recorded file for testing.

|   Test Operations

1. Insert a headphone with a MIC into the interface corresponding to the silkscreen
2. Enter the following command to record for 4 seconds:

.. code-block:: shell

    arecord -d 4 -f S16_LE record.wav

3. Play the recorded audio file by entering the following command:

.. code-block:: shell

    aplay record.wav

|   The recorded sound output from the headphones indicates that the recording test is passed


M.2 Interface Test
---------------------

|   Interface Silkscreen: J7
|   Test Description: Check the mounting status after mounting the hard disk.

|   Test Operations

1. Power off the development board, connect the M.2 interface hard disk, and then start the development board
2. Create a mount point and mount the hard disk by entering the following commands:

.. code:: shell

    mkdir /nvme    
    mount /dev/nvme0n1p1 /nvme/

3. Check the mounting status by entering the following command:

.. code:: shell

    df -h

4. If the mounting is successful, you can obtain output information similar to the following:

.. code:: shell

    /dev/nvme0n1p1  499M  10M  490M  2%  /nvme

5. Unmount the hard disk by entering the following command:

.. code:: shell

    umount /nvme

UART Test
-----------

|   Interface Silkscreen: J14
|   Test Description: The test is performed by means of UART self - sending and self - receiving.

|   Test Operations

1. Short - circuit the J14 - 33 (UART3_TX_M1) and J14 - 35 (UART3_RX_M1) pins
2. Enter the following command for transceiving test:

.. code-block:: shell

    ./serial_test.out /dev/ttyS3 "myzr"


|   After executing the test command, the output of information similar to the above indicates that the UART test is passed. Press 'Ctrl + C' to exit.


Infrared Test
---------------

|   Interface Silkscreen: IR1
|   Test Description: Receive infrared information and print out the corresponding data.

|   Test Operations

1. Prepare an infrared remote control or an infrared remote control app on a mobile phone
2. Turn on the relevant print switch by entering the following commands:

.. code-block:: shell

    echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/code_print
    echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/dbg_level

3. Aim the remote control at the infrared interface and press any button
4. If the development board sees and returns the relevant button information, it means the infrared signal is successfully received.


Display Screen
-----------------

|   Interface Silkscreen: J2
|   Test Description: Check whether the display screen of the development board displays normally when it is powered on and started.

|   Test Operations

1. Connect a screen with an HDMI interface to the HDMI interface on the development board and start the development board

|   Normal display of the screen indicates that the test is passed