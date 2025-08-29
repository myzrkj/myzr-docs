Test Guide
============

LED Test
----------

|   Interface Silkscreen: LED4, LED5
|   Test Description: Control the LED to turn on and off for testing
|   Test Operation:
|   Execute the following command to turn off LED4

.. code-block:: shell

    echo 0 > /sys/class/leds/heartbeat/brightness

|   Execute the following command to turn on LED4

.. code-block:: shell

    echo 1 > /sys/class/leds/heartbeat/brightness

|   Execute the following command to turn on LED5

.. code-block:: shell

    echo 1 > /sys/class/leds/disk/brightness

|   Execute the following command to turn off LED5

.. code-block:: shell

    echo 0 > /sys/class/leds/disk/brightness


Key Test
----------

|   Interface Silkscreen: KEY1: RESET, KEY2: MASKROM, KEY3: USER1
|   Test Description: The base board includes 1 system reset key (RESET), 1 Maskrom key (Maskrom), and 1 user input key (USER1); check the event number corresponding to the input key, execute the od command, and press the corresponding key for testing
|   Test Operation:

1. System Reset Key Test

|   Power on the evaluation board, press the system reset key RESET (KEY1), the on-board LED1 of the core board stops blinking; after releasing the key, the system will restart

2. Maskrom Key Test

.. code-block:: shell

    =====> Input:
    od -x /dev/input/event1
    =====> Output:
    0000000 00ad 0000 0000 0000 2ce3 0007 0000 0000
    0000020 0001 0094 0001 0000 00ad 0000 0000 0000
    0000040 2ce3 0007 0000 0000 0000 0000 0000 0000
    0000060 00ad 0000 0000 0000 5423 000a 0000 0000
    0000100 0001 0094 0000 0000 00ad 0000 0000 0000
    0000120 5423 000a 0000 0000 0000 0000 0000 0000
    ^C

3. USER1 Key Test

.. code-block:: shell

    =====> Input:
    od -x /dev/input/event2
    =====> Output:
    0000000 00d6 0000 0000 0000 bbdd 0004 0000 0000
    0000020 0001 0094 0001 0000 00d6 0000 0000 0000
    0000040 bbdd 0004 0000 0000 0000 0000 0000 0000
    0000060 00d6 0000 0000 0000 4f7e 0006 0000 0000
    0000100 0001 0094 0000 0000 00d6 0000 0000 0000
    0000120 4f7e 0006 0000 0000 0000 0000 0000 0000
    ^C

Network Port Test
-------------------

Network Port 1
~~~~~~~~~~~~~~~~

|   Interface Silkscreen: J13
|   System Interface: eth0
|   Test Description: Test by sending ICMP packets from the development board to the PC
|   Test Operation:

1. Configure the PC's wired network card IP to 192.168.137.99
2. Use a network cable to connect the development board's network port to the PC's network port; the serial port displays the following information:

.. code-block:: shell

    [  275.170629] rk_gmac-dwmac fe1c0000.ethernet eth0: Link is Up - 1Gbps/

3. To view the information of Network Port 1 on the development board, enter the following command:

.. code-block:: shell

    ifconfig eth0

4. Configure the IPv4 IP of Network Port 1 by entering the following command:

.. code-block:: shell

    ifconfig eth0 192.168.137.81 netmask 255.255.255.0

5. View the information of Network Port 1 on the development board again to confirm whether the IPv4 address is configured successfully. If the configuration fails, re-execute the operations starting from Step 4. Enter the following command:

.. code-block:: shell

    ifconfig eth0

6. Enter the following command to verify Network Port 1:

.. code-block:: shell

    ping -I eth0 192.168.137.99 -c 2 -w 4

|   "0% packet loss" indicates the test is passed
|   If "100% packet loss" occurs, first confirm whether all firewalls on the PC are disabled

Network Port 2
~~~~~~~~~~~~~~~~

|   Interface Silkscreen: J14
|   System Interface: eth1
|   Test Description: Test by sending ICMP packets from the development board to the PC
|   Test Operation:

1. Configure the PC's wired network card IP to 192.168.137.99
2. Use a network cable to connect the development board's network port to the PC's network port; the serial port displays the following information:

.. code-block:: shell

    [  528.550794] IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready

3. To view the information of Network Port 2 on the development board, enter the following command:

.. code-block:: shell

    ifconfig eth1

4. By default, the IP is obtained automatically, but for the test, a static IP is configured. The specific configuration command is as follows:

.. code-block:: shell

    ifconfig eth1 192.168.137.81 netmask 255.255.255.0

5. View the information of Network Port 2 on the development board again to confirm whether the IPv4 address is configured successfully. If the configuration fails, re-execute the operations starting from Step 4. Enter the following command:

.. code-block:: shell

    ifconfig eth1

6. Enter the following command to verify Network Port 2:

.. code-block:: shell

    ping -I eth1 192.168.137.99 -c 2 -w 4

|   "0% packet loss" indicates the test is passed
|   If "100% packet loss" occurs, first confirm whether all firewalls on the PC are disabled

GPIO Test
-----------

|   Test Description:
|   Use the GPIO sysfs interface to control IO. Take GPIO1_C1 as an example. If you need to test other GPIOs, modify the corresponding PIN value according to the mapping relationship in the following table

+----------+-----------+
| GPIO Pin | Pin Value |
+----------+-----------+
| GPIO3_A0 | 96        |
+----------+-----------+
| GPIO3_A1 | 97        |
+----------+-----------+
| GPIO1_C1 | 49        |
+----------+-----------+
| GPIO1_C2 | 50        |
+----------+-----------+
| GPIO1_C3 | 51        |
+----------+-----------+
| GPIO1_C4 | 52        |
+----------+-----------+
| GPIO1_C5 | 53        |
+----------+-----------+
| GPIO1_C6 | 54        |
+----------+-----------+
| GPIO4_B6 | 142       |
+----------+-----------+
| GPIO3_D2 | 122       |
+----------+-----------+
| GPIO3_D3 | 123       |
+----------+-----------+
| GPIO3_B7 | 111       |
+----------+-----------+
| GPIO3_C0 | 112       |
+----------+-----------+

|   Test Operation
|   Enter the following commands to set GPIO1_C1 to low level

.. code-block:: shell

    echo 49 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio49/direction
    echo 0 > /sys/class/gpio/gpio49/value
    cat /sys/class/gpio/gpio49/value

|   The output information is similar to the following:

.. code-block:: shell

    0

|   Enter the following commands to set GPIO1_C1 to high level

.. code-block:: shell

    echo 1 > /sys/class/gpio/gpio49/value
    cat /sys/class/gpio/gpio49/value

|   The output information is similar to the following:

.. code-block:: shell

    1

UART Test
-----------

|   Interface Silkscreen: J8
|   Test Description: Test by means of UART self-transmission and self-reception
|   Test Operation

1. Short-circuit the pins J8-7 (UART6_TX_M0) and J8-9 (UART6_RX_M0)
2. In the /test_app directory, enter the following command to perform the transmission and reception test:

.. code-block:: shell

    ./test_app/serial_test.out /dev/ttyS6 "myzr"

|   The output information is similar to the following:

.. code-block:: shell

    Starting send data...finish
    Starting receive data:
    ASCII: 0x6d          Character: m 
    ASCII: 0x79          Character: y 
    ASCII: 0x7a          Character: z 
    ASCII: 0x72          Character: r 
    ASCII: 0x0           Character: 

|   If the output shows the same ASCII characters for transmission and reception without error messages, the UART test is passed. Press 'Ctrl + C' to exit

SPI Interface Test
---------------------

|   Interface Silkscreen: J9
|   Test Description: Test by means of SPI self-transmission and self-reception
|   Test Operation

1. Short-circuit the pins J9-17 (GPIO3_B7) and J9-19 (GPIO3_C0)
2. In the /test_app directory, enter the following command to perform the transmission and reception test:

.. code-block:: shell

    ./test_app/spidev_test.out -D /dev/spidev0.0

|   The output information is similar to the following:

.. code-block:: shell

    spi mode: 0
    bits per word: 8
    max speed: 500000 Hz (500 KHz)
    00 24 00 00 00 00 
    00 3F FC 00 00 00 
    7F F8 00 00 00 00 
    00 00 00 00 00 00 
    00 00 00 00 00 00 
    00 0F 87 D0 7E 1F 
    87 F8

|   After executing the test command, if the terminal displays the above output information without error messages, the SPI test is passed

Audio Playback Test
----------------------

|   Interface Silkscreen: CON10
|   Test Description: Verify the audio playback function of the evaluation board by playing audio files
|   Test Operation

1. Connect headphones to the interface corresponding to the silkscreen
2. Enter the following commands for testing:

.. code-block:: shell

    amixer -c 0 cset name='Playback Path' 'HP'
    amixer -c 0 cset name='Playback Volume' 255
    aplay  /usr/share/sounds/alsa/Rear_Center.wav

3. Result: The audio playback test is passed if sound is output from the headphones


SPEAKER Test
--------------

|   Interface Silkscreen: J1
|   Test Description: The interface has 2 pins; connect the speaker to the interface corresponding to silkscreen J1
|   Test Operation

1. Enter the following commands

.. code-block:: shell

    amixer -c 0 cset name='Playback Path' 'SPK'
    amixer -c 0 cset name='Playback Volume' 255
    aplay /usr/share/sounds/alsa/Rear_Center.wav

|   The test is passed if the speaker produces sound


Recording Test
-----------------

|   Interface Silkscreen: J2
|   Test Description: Test by recording and playing back the recorded file
|   Test Operation

1. Insert a microphone into the interface corresponding to the silkscreen
2. Enter the following command to record for 10 seconds:

.. code-block:: shell

    amixer -c 0 cset name='Capture MIC Path' 'Main Mic'
    amixer -c 0 cset name='Capture Volume' 255
    arecord -c 1 -f S16_LE -r 44100 -d 10 -t wav /userdata/test.wav

3. Connect headphones or a speaker to the interfaces corresponding to silkscreens CON10 and J2 to play the recorded audio file. Enter the following command:

.. code-block:: shell

    aplay /userdata/test.wav

|   The recording test is passed if the recorded sound is output from the headphones or speaker


SD Interface Test
-------------------

|   Interface Silkscreen: CON5
|   Test Description: Test by inserting and removing the TF card
|   Test Operation:

1. Insert the TF card into the SD interface; the development board will output the following information:

|   [  380.723829] dwmmc_rockchip fe2c0000.mmc: could not set regulator OCR (-22)[  380.723921] dwmmc_rockchip fe2c0000.mmc: failed to enable vmmc regulator
|   [  380.736730] mmc_host mmc1: Bus speed (slot 0) = 400000Hz (slot req 400000Hz, actual 400000HZ div = 0)[  380.892477] mmc_host mmc1: Bus speed (slot 0) = 49500000Hz (slot req 50000000Hz, actual 49500000HZ div = 0)[  380.892687] mmc1: new high speed SDHC card at address 0001[  380.894512] mmcblk1: mmc1:0001 TF 4G 3.68 GiB
|   [  380.896321]  mmcblk1: p1
|   [  381.134266] FAT-fs (mmcblk1p1): utf8 is not a recommended IO charset for FAT filesystems, filesystem will be case sensitive!
|   [  381.140831] FAT-fs (mmcblk1p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

|   Result: If the output information matches the expected correct result after the operation, it indicates that the TF card is correctly recognized.

2. Remove the TF card; the output information is as follows:

|   [  376.270975] mmc1: card 0001 removed


USB Test
----------

|   Interface Silkscreen: CON7
|   Test Description: Test by inserting and removing a USB storage device (USB flash drive)
|   Test Operation:

1. Insert the USB device into the USB interface of the base board; the system will output information similar to the following:

|   [ 2649.580746] usb 2-1.1: new high-speed USB device number 3 using ehci-platform
|   [ 2649.735676] usb-storage 2-1.1:1.0: USB Mass Storage device detected
|   [ 2649.752030] scsi host0: usb-storage 2-1.1:1.0
|   [ 2649.951147] usbcore: registered new interface driver uas
|   [ 2650.801744] scsi 0:0:0:0: Direct-Access     aigo     U330             2.00 PQ: 0 ANSI: 4
|   [ 2650.822371] sd 0:0:0:0: [sda] 61440000 512-byte logical blocks: (31.5 GB/29.3 GiB)
|   [ 2650.830508] sd 0:0:0:0: Attached scsi generic sg0 type 0
|   [ 2650.851173] sd 0:0:0:0: [sda] Write Protect is off
|   [ 2650.871241] sd 0:0:0:0: [sda] No Caching mode page found
|   [ 2650.875217] sd 0:0:0:0: [sda] Assuming drive cache: write through
|   [ 2650.896991]  sda: sda1
|   [ 2650.916261] sd 0:0:0:0: [sda] Attached SCSI removable disk

2. Remove the USB device from the base board; the system will output information similar to the following:

|   [ 2690.764161] usb 2-1.1: USB disconnect, device number 3


Display Screen
-----------------

|   Interface Silkscreen: CON14
|   Test Description: Check whether the display screen shows normally when the development board is powered on and started
|   Test Operation

1. Connect an HDMI interface screen to the HDMI interface on the development board, and start the development board

|   The test is passed if the display screen shows normally

Multi-channel Video Playback Test
------------------------------------

|   Test Description:
|   Open multivideoplayer on the HDMI interface and play 9-channel videos in a loop


GPU Test
------------

|   Test Description:
|   On the HDMI interface, open the program with the 3D icon in the lower left corner. After opening, the CPU temperature will be relatively high.
|   After the test is completed, the following information will be displayed:

|   =======================================================
|                           glmark2 Score: 
|   2281=======================================================
|   child 1905 exited


mpp Test
-----------

|   Test Operation

1. To decode the video, enter the following command in the serial terminal:

.. code-block:: shell

    mpi_dec_test -i /oem/200frames_count.h264 -t 7 -n 250 -o /test.yuv -w 640 -h 480

|   Convert H.264 to YUV, and generate test.yuv in the current directory

2. To encode the video, enter the following command in the serial terminal:

.. code-block:: shell

    mpi_enc_test -i /test.yuv -t 7 -n 250 -o /test.h264 -w 640 -h 480 -fps 25

|   Convert YUV to H.264, and generate test.h264 in the current directory.

Backlight Test
-----------------

|   The brightness setting range of the backlight is (0--255), where 255 indicates the highest brightness and 0 indicates turning off the backlight brightness. After entering the system, enter the following commands in the terminal to perform the backlight test.
|   Enter the following command to view the current screen backlight value

.. code-block:: shell

    cat /sys/class/backlight/ffb10000.dsi.0/brightness

|   The output information is similar to the following:

.. code-block:: shell

    200

|   Enter the following command to turn off the backlight

.. code-block:: shell

    echo 0 > /sys/class/backlight/ffb10000.dsi.0/brightness

|   Enter the following command to turn on the backlight

.. code-block:: shell

    echo 200 > /sys/class/backlight/ffb10000.dsi.0/brightness

USB Camera Test
------------------

|   Test Description: Verify the camera function by displaying the image captured by the camera on the display screen
|   Test Operation

1. Connect a USB camera to one of the USB interfaces.
2. View the camera device:

.. code-block:: shell

    v4l2-ctl --list-devices

|   Bottom of the output information:

.. code-block:: shell

    Full HD webcam: Full HD webcam (usb-xhci-hcd.10.auto-1):
        /dev/video36
        /dev/video37
        /dev/media4

3. Command to view camera formats:

.. code-block:: shell

    v4l2-ctl --list-formats-ext -d /dev/video36

4. Command to query camera acquisition format:

.. code-block:: shell

    v4l2-ctl -V -d /dev/video36

5. Command to play the captured image (take the video36 node as an example):

.. code-block:: shell

    gst-launch-1.0 v4l2src device=/dev/video36 \
    ! 'image/jpeg,width=1920,height=1080,framerate=30/1' \
    ! jpegdec \
    ! videoconvert \
    ! autovideosink

|   The output information is as follows:

.. code-block:: shell

    Setting pipeline to PAUSED ...
    Pipeline is live and does not need PREROLL ...
    Pipeline is PREROLLED ...
    Setting pipeline to PLAYING ...
    New clock: GstSystemClock
    Redistribute latency...
    0:00:07.6 / 99:99:99.

|   The camera image will appear on the HDMI interface.

eMMC Test
------------

|   Perform a simple test on the read and write speeds of eMMC, taking the ext4 file system as an example
|   Enter the following command to test the write speed:

.. code-block:: shell

    dd if=/dev/zero of=/test bs=1M count=500 conv=fsync

|   The output information is as follows:

.. code-block:: shell

    500+0 records in
    500+0 records out
    524288000 bytes (524 MB, 500 MiB) copied, 14.2694 s, 36.7 MB/s

|   Enter the following command to test the read speed:

.. code-block:: shell

    dd if=/test of=/dev/null bs=1000M

|   The output information is as follows:

.. code-block:: shell

    0+1 records in
    0+1 records out
    524288000 bytes (524 MB, 500 MiB) copied, 0.819405 s, 640 MB/s


SARADC Interface Test
------------------------

|   Interface Silkscreen: J9
|   Test Description: Test by obtaining the voltage value. This operation takes pin3 (SARADC0_IN2) of the EXPORT1 (J9) interface as an example. If you need to test other channels, modify the corresponding device node according to the mapping relationship in the following table

+-------------+--------------------+---------------------------------------------------+
| ADC Channel | ADC Interface (J9) | Device Node                                       |
+-------------+--------------------+---------------------------------------------------+
| SARADC0_IN2 | pin3               | /sys/bus/iio/devices/iio\:device0/in_voltage2_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC0_IN3 | pin5               | /sys/bus/iio/devices/iio\:device0/in_voltage3_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC0_IN4 | pin7               | /sys/bus/iio/devices/iio\:device0/in_voltage4_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC0_IN5 | pin9               | /sys/bus/iio/devices/iio\:device0/in_voltage5_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC0_IN6 | pin11              | /sys/bus/iio/devices/iio\:device0/in_voltage6_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC0_IN7 | pin13              | /sys/bus/iio/devices/iio\:device0/in_voltage7_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC1_IN0 | pin4               | /sys/bus/iio/devices/iio\:device1/in_voltage0_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC1_IN1 | pin6               | /sys/bus/iio/devices/iio\:device1/in_voltage1_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC1_IN2 | pin8               | /sys/bus/iio/devices/iio\:device1/in_voltage2_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC1_IN3 | pin10              | /sys/bus/iio/devices/iio\:device1/in_voltage3_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC1_IN4 | pin12              | /sys/bus/iio/devices/iio\:device1/in_voltage4_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC1_IN5 | pin14              | /sys/bus/iio/devices/iio\:device1/in_voltage5_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC1_IN6 | pin16              | /sys/bus/iio/devices/iio\:device1/in_voltage6_raw |
+-------------+--------------------+---------------------------------------------------+
| SARADC1_IN7 | pin18              | /sys/bus/iio/devices/iio\:device1/in_voltage7_raw |
+-------------+--------------------+---------------------------------------------------+


|   Test Operation
|   a) Use a Dupont wire to connect pin3 (SARADC0_IN2) of the EXPORT1 (J9) interface on the board to pin1 (VDD_1V8_MAIN, with a level of 1.8V). 
|   b) Enter the board's file system and execute the following command to test the input voltage

.. code-block:: shell

    cat /sys/bus/iio/devices/iio\:device0/in_voltage2_raw

|   The output information is similar to the following:

.. code-block:: shell

    1023

|   c) Power off the board, and use a Dupont wire to connect pin3 (SARADC0_IN2) of the EXPORT1 (J9) interface on the evaluation board to pin2 (GND).
|   d) Enter the board's file system and execute the following command to test the ground connection

.. code-block:: shell

    cat /sys/bus/iio/devices/iio\:device0/in_voltage2_raw

|   The output information is similar to the following:

.. code-block:: shell

    0

|   The actual input voltage value Vin = 1023 x [1.8 / (2^10 - 1)] ≈ 1.79V, and the result is close to the input voltage. The test is passed if the output information for the voltage test is around 1000 and the output information for the ground connection test is 0.