.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Test Guide
==========

Network Port Test
-----------------

System Login
~~~~~~~~~~~~

.. code-block:: text

   linaro
   linaro
   sudo -i
   linaro

Network Port 0 Test
~~~~~~~~~~~~~~~~~~~~

[Test Description]: Test by sending ICMP packets from the development board to PC

[Interface Label]: J12

[System Device]: eth0

[Test Steps]:

1. Network Port 0 is configured for automatic IP acquisition. Connect to a switch or router and enter the following command

.. code-block:: text

   ping baidu.com -c 3

2. Output information is as follows

.. code-block:: text

   root@sophon:~$ ping baidu.com -c 3
   PING baidu.com (124.237.177.164) 56(84) bytes of data.
   64 bytes from 124.237.177.164 (124.237.177.164): icmp_seq=1 ttl=53 time=38.8 ms
   64 bytes from 124.237.177.164 (124.237.177.164): icmp_seq=2 ttl=53 time=38.6 ms
   64 bytes from 124.237.177.164 (124.237.177.164): icmp_seq=3 ttl=53 time=38.6 ms
   
   --- baidu.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms

Network Port 1 Test
~~~~~~~~~~~~~~~~~~~~

[Test Description]: Test by sending ICMP packets from the development board to PC

[Interface Label]: J13

[System Device]: eth1

[Test Steps]:

1. Connect the network port and enter the following command

.. code-block:: text

   dhclient -r eth1
   dhclient eth1
   ping baidu.com -c 3

2. Output information is as follows

.. code-block:: text

   root@sophon:~$ ping baidu.com -c 3
   PING baidu.com (124.237.177.164) 56(84) bytes of data.
   64 bytes from 124.237.177.164 (124.237.177.164): icmp_seq=1 ttl=53 time=38.8 ms
   64 bytes from 124.237.177.164 (124.237.177.164): icmp_seq=2 ttl=53 time=38.6 ms
   64 bytes from 124.237.177.164 (124.237.177.164): icmp_seq=3 ttl=53 time=38.6 ms
   
   --- baidu.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms

SD Card Test
------------

[Test Description]: Test by viewing SD card device information

[Interface Label]: U11

[System Device]: /dev/mmcblk1p1

[Test Steps]:

1. Insert the SD card into the slot and enter the following command to view SD card information

.. code-block:: text

   fdisk -l

2. Output information is as follows

.. code-block:: shell

   Device            Start      End  Sectors  Size Type
   /dev/mmcblk0p1     8192   270335   262144  128M Microsoft basic data
   /dev/mmcblk0p2   270336   532479   262144  128M Microsoft basic data
   /dev/mmcblk0p3   532480   552959    20480   10M Microsoft basic data
   /dev/mmcblk0p4   552960  6844415  6291456    3G Microsoft basic data
   /dev/mmcblk0p5  6844416 25427327 18582912  8.9G Microsoft basic data
   /dev/mmcblk0p6 25427328 61063134 35635807   17G Microsoft basic data
   
   
   Disk /dev/mmcblk1: 7.4 GiB, 7948206080 bytes, 15523840 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disklabel type: dos
   Disk identifier: 0x22bac834
   
   Device         Boot Start     End Sectors  Size Id Type
   /dev/mmcblk1p1      40960 4112383 4071424  1.9G  e W95 FAT16 (LBA)

USB Test
--------

[Test Description]: Test by plugging and unplugging USB flash drive

[Interface Label]: J5 J6

[System Device]: usb

[Test Steps]:

1. Enter the following commands

.. code-block:: text

   JavaScript
   cvi_pinmux -r IIC5_SCL
   cvi_pinmux -w IIC5_SCL/GPIO104
   echo 392 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio392/direction
   echo 1 > /sys/class/gpio/gpio392/value

2. Insert a USB flash drive into the device, example as follows (Note: The upper USB interface of J6 is the download interface and is generally not used)

.. code-block:: text

   root@sophon:/# lsusb
   Bus 004 Device 002: ID 05e3:0620 Genesys Logic, Inc. USB3.0 Hub
   Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 002 Device 004: ID 14cd:1212 Super Top microSD card reader (SY-T18)
   Bus 002 Device 002: ID 05e3:0610 Genesys Logic, Inc. Hub
   Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
   Bus 003 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
   Bus 001 Device 002: ID 0bda:d723 Realtek Semiconductor Corp. 802.11n WLAN Adapter
   Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
   root@sophon:/#
   You can see the USB device I inserted: ID 14cd:1212 Super Top microSD card reader (SY-T18)

Heat Dissipation Fan Test
--------------------------

[Test Description]: Test by pulling the pin high

[Interface Label]: J2

[System Device]: fan

[Test Steps]:

.. code-block:: text

   JavaScript
   cvi_pinmux -r PWM0
   cvi_pinmux -w PWM0/GPIO75
   echo 427 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio427/direction
   echo 1 > /sys/class/gpio/gpio427/value (ON)
   echo 0 > /sys/class/gpio/gpio427/value (OFF)

LED1 Test
--------

[Test Description]: Test by pulling the pin high and low

[Interface Label]: LED1

[System Device]:

[Test Steps]:

.. code-block:: text

   cvi_pinmux -r GPIO2
   echo 401 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio401/direction
   echo 1 > /sys/class/gpio/gpio401/value (ON)
   echo 0 > /sys/class/gpio/gpio401/value (OFF)

LED2 Test
--------

[Test Description]: Test by pulling the pin high and low

[Interface Label]: LED2

[System Device]:

[Test Steps]:

.. code-block:: text

   TypeScript
   echo 402 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio402/direction
   echo 1 > /sys/class/gpio/gpio402/value (ON)
   echo 1 > /sys/class/gpio/gpio402/value (OFF)

ADC Test
--------

[Test Description]: Test by reading voltage values

[Interface Label]: J1

[System Device]:

[Test Steps]:

1. Connect ADC1 (second header) to 1.8V for testing, output as follows

.. code-block:: text

   echo 1 > /sys/bus/iio/devices/iio:device0/in_voltage1_raw
   cat /sys/bus/iio/devices/iio:device0/in_voltage1_raw
   4095

ADC1 (second header) grounded for testing, output as follows

.. code-block:: text

   cat /sys/bus/iio/devices/iio:device0/in_voltage1_raw
   0 (or a few tens close to 0)

2. Connect ADC2 (third header) to 1.8V for testing, output as follows

.. code-block:: text

   echo 1 > /sys/bus/iio/devices/iio:device0/in_voltage2_raw
   cat /sys/bus/iio/devices/iio:device0/in_voltage2_raw
   4095

ADC2 (third header) grounded for testing, output as follows

.. code-block:: text

   cat /sys/bus/iio/devices/iio:device0/in_voltage2_raw
   0 (or a few tens close to 0)

IO Test
-------

[Test Description]: Test by pulling the pin high

[Interface Label]: U28

[System Device]: /sys/class/gpio/

[Test Steps]:

.. code-block:: text

   JavaScript
   cvi_pinmux -w IIC2_SDA/GPIO99 (IO2)
   echo 387 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio387/direction
   echo 1 > /sys/class/gpio/gpio387/value
   cat /sys/class/gpio/gpio387/value
   Output: 1
   echo 0 > /sys/class/gpio/gpio387/value
   cat /sys/class/gpio/gpio387/value
   Output: 0
   
   cvi_pinmux -w IIC2_SCL/GPIO100 (IO1)
   echo 388 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio388/direction
   echo 1 > /sys/class/gpio/gpio388/value
   cat /sys/class/gpio/gpio388/value
   Output: 1
   echo 0 > /sys/class/gpio/gpio388/value
   cat /sys/class/gpio/gpio388/value
   Output: 0
   
   cvi_pinmux -w UART4_TX/GPIO91 (IO4)
   echo 443 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio443/direction
   echo 1 > /sys/class/gpio/gpio443/value
   cat /sys/class/gpio/gpio443/value
   Output: 1
   echo 0 > /sys/class/gpio/gpio443/value
   cat /sys/class/gpio/gpio443/value
   Output: 0
   
   cvi_pinmux -w UART4_RX/GPIO92
   echo 444 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio444/direction
   echo 1 > /sys/class/gpio/gpio444/value
   cat /sys/class/gpio/gpio444/value
   Output: 1
   echo 0 > /sys/class/gpio/gpio444/value
   cat /sys/class/gpio/gpio444/value
   Output: 0

UART2 Test
----------

[Test Description]: Test by shorting TX and RX

[Interface Label]: J3

[System Device]: /dev/ttyS2

[Test Steps]:

1. Short the middle two pins of J3, enter the command, and receive output information

.. code-block:: text

   cvi_pinmux -w UART2_TX/UART2_TX
   cvi_pinmux -w UART2_RX/UART2_RX
   serial_test.out /dev/ttyS2 123

RS232-2 Test
------------

[Test Description]: Test by shorting TX and RX

[Interface Label]: CON3

[System Device]: /dev/ttyS5

[Test Steps]:

1. Use a pointed Dupont wire to short the second and third holes on the top row, enter the command, and receive output information

.. code-block:: text

   cvi_pinmux -w IIC4_SDA/UART5_TX
   cvi_pinmux -w IIC4_SCL/UART5_RX
   serial_test.out /dev/ttyS5 123

RS232-1/RS485 Test
------------------

[Test Description]: Test RS232-1 by shorting TX and RX, test RS485 using RS485 to USB module

[Interface Label]: CON2

[System Device]: /dev/ttyS7

[Test Steps]:

Find the DIP switch U17 nearby

When DIP 1 is ON and DIP 2 is OFF, SLE1 is high, switching to RS232-1

When DIP 1 is OFF and DIP 2 is ON, SLE1 is low, switching to RS485

1. Switch to RS232-1, use a pointed Dupont wire to short the second and third holes on the top row, enter the command, and receive output information

.. code-block:: text

   cvi_pinmux -w PAD_VIVO0_D15/UART7_TX
   cvi_pinmux -w PAD_VIVO0_D16/UART7_RX
   ./serial_test.out /dev/ttyS7 123

2. Switch to RS485, use the RS485 to USB module, connect the A of the RS485 to USB module to the second hole on the top row, connect B to the third hole on the top row. Start the RS485 terminal and enter the following command in the system terminal. The RS485 terminal can receive information. Enter 123 in the RS485 terminal (input status not displayed), the system can receive the information

.. code-block:: text

   cvi_pinmux -w PAD_VIVO0_D15/UART7_TX
   cvi_pinmux -w PAD_VIVO0_D16/UART7_RX
   ./serial_test.out /dev/ttyS7 123

I2C4 Test
---------

[Test Description]: Test by reading I2C device address

[Interface Label]: U32

[System Device]: /dev/i2c-4

[Test Steps]:

1. Connect the SCL of the I2C device to pin 1 on the bottom left, connect SDA to pin 2 on the bottom left, output device address information

.. code-block:: text

   cvi_pinmux -w PCIE0_L0_CLKREQ_IN_X/IIC4_SCL
   cvi_pinmux -w PCIE0_L0_WAKEUP_X/IIC4_SDA
   i2cdetect -y -r 4

User Button Test
----------------

[Test Description]: Test by reading I2C device address

[Interface Label]: SW2

[System Device]:

[Test Steps]:

1. Enter the command, press the button as needed. When the button is released, it can output 0 and 1 information

.. code-block:: text

   cvi_pinmux -w GPIO0/GPIO111
   echo 399 > /sys/class/gpio/export
   echo in > /sys/class/gpio/gpio399/direction
   cat /sys/class/gpio/gpio399/value

M.2 Test
--------

[Test Description]: Test by checking device information

[Interface Label]: J8

[System Device]:

[Test Steps]:

.. code-block:: text

   # Or more directly view partitions, file systems and sizes
   root@sophon:~# fdisk -l
   You can see the device /dev/nvme0n1p1

WIFI Test
---------

[Test Description]: After WiFi connection is successful, the development board sends ICMP packets to the external network to verify the connection is normal

[Interface Label]: U41

[System Device]: wlan0

[Test Steps]:

1. Connect the antenna to U40

.. code-block:: text

   insmod /mnt/system/ko/8723du.ko
   wpa_passphrase "iQOO" "12345678" > /etc/wpa_supplicant.conf
   # Connect to WiFi
   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
   # Get IP address
   dhclient wlan0
   # Test
   ping -I wlan0 baidu.com -c 3

Bluetooth Test
--------------

[Test Description]: After Bluetooth connection is successful, the development board sends ICMP packets to the external network to verify the connection is normal

[Interface Label]: U41

[System Device]: wlan0

[Test Steps]:

.. code-block:: text

   insmod /mnt/system/ko/rtk_btusb.ko
   hciconfig hci0 up
   hcitool scan
   Scanning ...
   A8:13:06:20:06:54        iQOO Neo5
   DC:0D:30:5C:4C:93        XP-236B-L
   l2ping A8:13:06:20:06:54
   Ping: A8:13:06:20:06:54 from 84:FC:14:4E:2D:3D (data size 44) ...
   44 bytes from A8:13:06:20:06:54 id 0 time 40.02ms
   44 bytes from A8:13:06:20:06:54 id 1 time 52.26ms
   ^C2 sent, 2 received, 0% loss

Audio Test
----------

[Test Description]: Play audio files for testing and verification

[Interface Label]: J4

[System Device]:

[Test Steps]:

1. Connect headphones and enter the following command to play audio

.. code-block:: text

   cd /mnt/system
   tinyplay 16k_2ch32.wav -D 1 -d 0

5G Test
-------

[Test Description]: After Bluetooth connection is successful, the development board sends ICMP packets to the external network to verify the connection is normal

[Interface Label]: U42

[System Device]: usb0

[Test Steps]:

1. Insert the SIM card into U43. The 4G module must be connected to an antenna

.. code-block:: text

   quectel-CM &
   ping -I wwan0 www.baidu.com -c 4

Camera Test
-----------

[Test Description]: Capture camera images to verify the connection is normal

[Interface Label]: J10, J11

[System Device]: stream0

[Test Steps]:

Download VLC software on your computer

1. Connect to J10 (i2c0), connect camera connector pin 1 to board connector pin 1

.. code-block:: text

   insmod v4l2_os04a10_j10.ko
   /opt/sophon/sophon-soc-libisp_1.0.0/bin/CviIspTool.sh
   Output: rtsp://192.168.128.174:8554/stream0, view with VLC

2. Connect to J11 (i2c1), connect camera connector pin 1 to board connector pin 1

.. code-block:: text

   insmod v4l2_os04a10_j11.ko
   /opt/sophon/sophon-soc-libisp_1.0.0/bin/CviIspTool.sh
   Output: rtsp://192.168.128.174:8554/stream0, view with VLC

HDMI Test
---------

[Test Description]: Connect HDMI screen to verify display works

[Interface Label]: J9

[System Device]:

[Test Steps]:

1. Connect the HDMI screen and power on to display the image

CAN Test
--------

[Test Description]: Test CAN communication between two boards

[Interface Label]: U32

[System Device]:

[Test Steps]:

Power on two boards. Connect board 1 U32 top-left pin 1 to board 2 U32 top-left pin 1. Connect board 1 U32 top-left pin 2 to board 2 U32 top-left pin 2

1. Board 1 receives, board 2 sends

Board 1 configuration is as follows

.. code-block:: shell

   busybox devmem 0x2810450c 32 0x3838
   busybox devmem 0x27011004 32 0x800
   busybox devmem 0x27011000 32 0x0
   
   ip link set can0 down
   ip link set can0 type can bitrate 500000
   ip link set can0 up
   Board 1 enters receiving state
   candump can0

Board 2 configuration is as follows

.. code-block:: shell

   busybox devmem 0x2810450c 32 0x3838
   busybox devmem 0x27011004 32 0x800
   busybox devmem 0x27011000 32 0x0
   
   ip link set can0 down
   ip link set can0 type can bitrate 500000
   ip link set can0 up
   Board 2 enters sending state
   cansend can0 -e -i 0x1F334455 0x11 0x22 0x33 0x44 0x55 0x66 0x77 0x88

At this time, board 1 terminal will receive data sent from board 2

.. code-block:: text

   root@sophon:~# candump can0
   interface = can0, family = 29, type = 3, proto = 1
   
   <0x1f334455> [8] 11 22 33 44 55 66 77 88

2. Board 1 sends, board 2 receives

Board 2 configuration for receiving

.. code-block:: text

   root@sophon:~# candump can0

Board 1 configuration for sending

.. code-block:: text

   cansend can0 -e -i 0x1F334455 0x11 0x22 0x33 0x44 0x55 0x66 0x77 0x88

At this time, board 2 terminal will receive data sent from board 1

.. code-block:: text

   root@sophon:~# cansend can0 -e -i 0x1F334455 0x11 0x22 0x33 0x44 0x55 0x66 0x77 0x88
   interface = can0, family = 29, type = 3, proto = 1
   root@sophon:~# candump can0
   interface = can0, family = 29, type = 3, proto = 1
   <0x1f334455> [8] 11 22 33 44 55 66 77 88

RTC Test
--------

[Test Description]: Read and set the time, check if the time is correct after power off and restart

[Interface Label]: U13

[System Device]: /dev/rtc0

[Test Steps]:

1. Install the button battery on U13 and enter the following commands

.. code-block:: text

   timedatectl set-ntp false
   date -s "2025-5-14 10:30:00"
   date
   hwclock -w
   hwclock -w
   hwclock -r
   hwclock -r

2. Power off the board for a while, then power on and boot to check if the clock continues to run

.. code-block:: text

   hwclock -r
   date