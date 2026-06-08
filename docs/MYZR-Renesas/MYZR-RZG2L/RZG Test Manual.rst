RZG Test Manual
=================

Test Environment
------------------

| Both RZG2L and RZG2UL use the same set of kernel and U-Boot source codes. RZG2L uses the system image `core-image-qt-myzr-rzg2l-Release.xxx.tar.bz2`, while RZG2UL uses `core-image-bsp-myzr-rzg2ul-Release.xxx.tar.bz2`.

**After receiving the development board, directly use the factory default image system to perform the following functional tests for verification. Proceed with subsequent development only after confirming the development board works normally.**

RZG2L Test Environment
~~~~~~~~~~~~~~~~~~~~~~~~

| 【Development Board Model】: MYZR-RZG2L-MB200 + MYZR-G2L-CB200
| 【Kernel Version】: Linux-5.10.131-Release.xxx.tar.bz2
| 【U-Boot Version】: u-boot-Release.xxx.tar.bz2
| 【File System】: core-image-qt-myzr-rzg2l-Release.xxx.tar.bz2

RZG2UL Test Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~

| 【Development Board Model】:

- MYZR-RZG2UL-MB200-ETH + MYZR-G2UL-CB200
- MYZR-RZG2UL-MB200-LCD + MYZR-G2UL-CB200

| 【Kernel Version】: Linux-5.10.131-Release.xxx.tar.bz2
| 【U-Boot Version】: u-boot-Release.xxx.tar.bz2
| 【File System】: core-image-bsp-myzr-rzg2ul-Release.xxx.tar.bz2

Interface Identification Diagram
-----------------------------------

**rzg2l**

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2l_zheng.jpg
   :alt: 1200px-Myzr_rzg2l_zheng.jpg

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2l_bei.jpg
   :alt: 1200px-Myzr_rzg2l_bei.jpg

**rzg2ul-eth**

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2ul-eth_zheng.jpg
   :alt: 1200px-Myzr_rzg2ul-eth_zheng.jpg

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2ul-eth_bei.jpg
   :alt: 1200px-Myzr_rzg2ul-eth_bei.jpg

**rzg2ul-lcd**

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2ul-lcd_zheng.jpg
   :alt: 1200px-Myzr_rzg2ul-lcd_zheng.jpg

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/1200px-Myzr_rzg2ul-lcd_bei.jpg
   :alt: 1200px-Myzr_rzg2ul-lcd_bei.jpg

Ethernet Port 0 Test
----------------------

**Description**

| 【Test Description】: Test by sending ICMP packets from the development board to a PC
| 【Interface Identification】: ETH10/100/1000M
| 【System Interface】: eth0
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200: U10
- MYZR-RZG2UL-MB200-ETH: U10
- MYZR-RZG2UL-MB200-LCD: U9

| Note: A static IP address (192.168.137.81) is configured for eth0.

**Test Operations**

1. Configure the PC's wired network card IP to 192.168.137.99
2. Connect the development board's Ethernet port to the PC's Ethernet port using a network cable
3. Enter the following command to communicate with the PC:

.. code-block:: shell

   =====> Input:
   # ping 192.168.137.99

   =====> Output:
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=0.758 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.306 ms
   64 bytes from 192.168.137.99: icmp_seq=3 ttl=128 time=0.467 ms
   ^C
   --- 192.168.137.99 ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 0.306/0.510/0.758/0.187 ms

| "0% packet loss" indicates the test is passed.

Ethernet Port 1 Test
----------------------

**Description**

| 【Test Description】: Test by sending ICMP packets from the development board to a PC
| 【Interface Identification】: ETH10/100/1000M
| 【System Interface】: eth1
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200: U13
- MYZR-RZG2UL-MB200-ETH: U14

**Test Operations**

1. Configure the PC's wired network card IP to 192.168.137.99
2. Connect the development board's Ethernet port to the PC's Ethernet port using a network cable
3. Enter the following command to communicate with the PC:

.. code-block:: shell

   =====> Input:
   # ifconfig eth1 192.168.137.81
   # ping 192.168.137.99

   =====> Output:
   PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
   64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=0.758 ms
   64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.306 ms
   64 bytes from 192.168.137.99: icmp_seq=3 ttl=128 time=0.467 ms
   ^C
   --- 192.168.137.99 ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2003ms
   rtt min/avg/max/mdev = 0.306/0.510/0.758/0.187 ms

| "0% packet loss" indicates the test is passed.

USB Test
-----------

**Description**

| 【Test Description】: Test by plugging and unplugging a USB storage device (e.g., USB flash drive)
| 【Interface Identification】: USB2.0
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200: J4
- MYZR-RZG2UL-MB200-ETH: J4
- MYZR-RZG2UL-MB200-LCD: J4

**Test Operations**

1. Insert the USB device into the USB port of the baseboard. The system will output information similar to the following:

.. code-block:: shell

   root@myzr-rzg2l:~# [   41.664942] usb 1-1.1: new high-speed USB device number 4 using ehci-platform
   [   41.796776] usb-storage 1-1.1:1.0: USB Mass Storage device detected
   [   41.803713] scsi host0: usb-storage 1-1.1:1.0
   [   42.819899] scsi 0:0:0:0: Direct-Access     Generic- SD/MMC           1.00 PQ: 0 ANSI: 4
   [   43.591013] sd 0:0:0:0: [sda] 60932096 512-byte logical blocks: (31.2 GB/29.1 GiB)
   [   43.599368] sd 0:0:0:0: [sda] Write Protect is off
   [   43.605215] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn\'t support DPO or FUA
   [   43.642283]  sda: sda1
   [   43.653982] sd 0:0:0:0: [sda] Attached SCSI removable disk

2. Unplug the USB device from the baseboard. The system will output information similar to the following:

.. code-block:: shell

   root@myzr-rzg2l:~# [   55.524114] usb 1-1.1: USB disconnect, device number 4

SD Interface Test
-------------------

**Description**

| 【Test Description】: Test by inserting and detecting a TF card
| 【Interface Identification】: TF
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200: J8
- MYZR-RZG2UL-MB200-ETH: J7
- MYZR-RZG2UL-MB200-LCD: J7

**Test Operations**

1. Install the TF card into the SD interface. The development board will output the following information:

.. code-block:: shell

   root@myzr-rzg2l:~# [  178.279039] mmc1: new high speed SDHC card at address 1234
   [  178.290822] mmcblk1: mmc1:1234 SA32G 29.1 GiB 
   [  178.298039]  mmcblk1: p1

2. Check the corresponding SD interface device:

.. code-block:: shell

   # ls /dev/mmcblk1*
   /dev/mmcblk1  /dev/mmcblk1p1

3. Remove the TF card. The following information will be output:

.. code-block:: shell
   
   root@myzr-rzg2l:~# [  195.429099] mmc1: card 1234 removed

GPIO Test
------------

**Description**

| 【Test Description】: Control the output/input level of GPIO
| 【Interface Identification】: GPIO/SPI/UART
| 【System Interface】: /sys/class/gpio/
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200: P3 (GPIOx_x)
- MYZR-RZG2UL-MB200-ETH: P2 (GPIOx_x)
- MYZR-RZG2UL-MB200-LCD: J12 (GPIOx_x)

| Note: The GPIO number calculation methods for RZG2L and RZG2UL are different.

**Test Operations**

**RZG2L**

1. Export the GPIO interface to be tested, taking GPIO47_2 in P3 as an example. GPIO47_2 corresponds to the core board pin P47_2, and the corresponding GPIO number = (47*8 + 2) + 120 = 498. Enter the following command to export the node:

.. code-block:: shell

   # echo 498 > /sys/class/gpio/export 
   # ls /sys/class/gpio/
   P47_2  export  gpiochip120  unexport

2. Configure the GPIO47_2 pin as an output pin:

.. code-block:: shell

   # echo out > /sys/class/gpio/P47_2/direction

3. Configure the GPIO47_2 pin to output a high level:

.. code-block:: shell

   # echo 1 > /sys/class/gpio/P47_2/value

| Use a multimeter to measure the GPIO47_2 pin; a voltage of approximately 3.3V (high level) should be detected.

4. Configure the GPIO47_2 pin to output a low level:

.. code-block:: shell

   # echo 0 > /sys/class/gpio/P47_2/value

| Use a multimeter to measure the GPIO47_2 pin; a voltage of approximately 0V (low level) should be detected.

5. Configure the GPIO47_2 pin as an input, ground the pin, and read its value:

.. code-block:: shell

   # echo in > /sys/class/gpio/P47_2/direction
   # cat /sys/class/gpio/P47_2/value 
   0

**RZG2UL**

1. Export the GPIO interface to be tested, taking GPIO7_3 in J12 of the LCD board as an example. GPIO7_3 corresponds to the core board pin P7_3, and the corresponding GPIO number = (7*8 + 3) + 360 = 419. Enter the following command to export the node:

.. code-block:: shell

   # echo 419 > /sys/class/gpio/export 
   # ls /sys/class/gpio/
   P7_3  export  gpiochip360  unexport

2. Configure the GPIO7_3 pin as an output pin:

.. code-block:: shell

   # echo out > /sys/class/gpio/P7_3/direction

3. Configure the GPIO7_3 pin to output a high level:

.. code-block:: shell

   # echo 1 > /sys/class/gpio/P7_3/value

| Use a multimeter to measure the GPIO7_3 pin; a voltage of approximately 3.3V (high level) should be detected.

4. Configure the GPIO7_3 pin to output a low level:

.. code-block:: shell

   # echo 0 > /sys/class/gpio/P7_3/value

| Use a multimeter to measure the GPIO7_3 pin; a voltage of approximately 0V (low level) should be detected.

5. Configure the GPIO7_3 pin as an input, ground the pin, and read its value:

.. code-block:: shell

   # echo in > /sys/class/gpio/P7_3/direction
   # cat /sys/class/gpio/P7_3/value 
   0

UART Test
------------

**Description**

| 【Test Description】: Test by means of UART self-transmission and self-reception
| 【Interface Identification】: GPIO/SPI/UART
| 【System Device】:

- MYZR-RZG2L-MB200: /dev/ttySC2
- MYZR-RZG2UL-MB200-ETH: /dev/ttySC3
- MYZR-RZG2UL-MB200-LCD: NULL

| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200: P3 (UART2)
- MYZR-RZG2UL-MB200-ETH: P2 (UART3)
- MYZR-RZG2UL-MB200-LCD: NULL

**Test Operations**

| Take the MYZR-RZG2L-MB200 baseboard as an example:

1. Short-circuit pins P3-7 and P3-9 (i.e., UART2_RXD and UART2_TXD).
2. Enter the following command to perform UART2 transmission and reception test:

.. code-block:: shell

   =====> Input:
   # /my-demo/serial_test.out /dev/ttySC2 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x0   Character:  

| After executing the test command, the application outputs information similar to the above, indicating normal operation. Press Ctrl+C to exit after the test.


RS232 Test
------------

**Description**

|  [Test Description]: Test is performed using the serial port's self-transmit and self-receive method
|  [Interface Identification]: RS232
|  [System Devices]:

- MYZR-RZG2L-MB200: /dev/ttySC0 (debug serial port), /dev/ttySC1, /dev/ttySC3
- MYZR-RZG2UL-MB200-ETH: /dev/ttySC0 (debug serial port), /dev/ttySC1, /dev/ttySC4
- MYZR-RZG2UL-MB200-LCD: /dev/ttySC0 (debug serial port), /dev/ttySC1, /dev/ttySC4

|  [Interface Silkscreen]:

- MYZR-RZG2L-MB200: J10-11 (debug serial port/RS232_RX0), J10-12 (debug serial port/RS232_TX0), J10-14 (RS232_RX3), J10-15 (RS232_TX3), J10-19 (RS232_RX1), J10-20 (RS232_TX1)
- MYZR-RZG2UL-MB200-ETH: J16 (RS232_0 (debug serial port), RS232_1, RS232_4)
- MYZR-RZG2UL-MB200-LCD: J16 (RS232_0 (debug serial port), RS232_1, RS232_4)

|  Note: The debug serial port does not require testing.

**Test Operations**

|  Take the MYZR-RZG2L-MB200 baseboard as an example:

1. Short-circuit TX3 and RX3 of J10
2. Enter the following command to perform RS232 transmission and reception test:

.. code-block:: shell

   =====> Input:
   # /my-demo/serial_test.out /dev/ttySC3 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m
   ASCII: 0x79      Character: y
   ASCII: 0x7a      Character: z
   ASCII: 0x72      Character: r
   ASCII: 0x0   Character:

|  After executing the test command, if the application outputs information similar to the above, it is normal. Press Ctrl+c to exit after the test.

RS485 Test
------------

**Description**

|  [Test Description]: RS485 uses differential signals and cannot be tested using the self-transmit and self-receive method.
|  [Interface Identification]: RS485
|  [System Devices]:

- MYZR-RZG2L-MB200: /dev/ttySC4
- MYZR-RZG2UL-MB200-ETH: /dev/ttySC2
- MYZR-RZG2UL-MB200-LCD: /dev/ttySC2

|  [Interface Silkscreen]:

- MYZR-RZG2L-MB200: J10-8 (B), J10-9 (A)
- MYZR-RZG2UL-MB200-ETH: J16 (A, B)
- MYZR-RZG2UL-MB200-LCD: J16 (A, B)

**Test Operations**

|  Take the MYZR-RZG2UL-MB200-ETH baseboard as an example:

1. Use a 485-232 converter to connect the J16 (A, B) pins to the computer's USB-to-serial cable
2. Open the serial port debugging assistant, set the baud rate to 9600, no parity bit, 8 data bits, and 1 stop bit.
3. Log in to the development board using SSH and send data to the computer:

.. code-block:: shell

   # echo 123 > /dev/ttySC2

|  You can see that the serial port assistant receives the string "123"

4. The development board receives data, and the computer sends data:

.. code-block:: shell

   # cat /dev/ttySTM2

|  When the serial port assistant sends a string, the development board will receive the data:

.. code-block:: shell

   # cat /dev/ttySTM2
   myzr

.. image:: /image/MYZR-瑞萨系列/MYZR-RZG2L/MYZR-RZG_rs485.png
   :alt: MYZR-RZG_rs485.png

CAN Test
----------

**Description**

|  [Test Description]: CAN ports send data to each other
|  [Interface Identification]: CAN
|  [System Devices]: can0, can1
|  [Interface Silkscreen]:

- MYZR-RZG2L-MB200: J10-1 (can0_H), J10-3 (can0_L), J10-4 (can1_H), J10-6 (can0_L),
- MYZR-RZG2UL-MB200-ETH: J16 (can0, can1)
- MYZR-RZG2UL-MB200-LCD: J16 (can0)

|  Note: The MYZR-RZG2UL-MB200-LCD baseboard has only one CAN port and cannot perform self-transmission and self-reception tests. Two development boards can be used for CAN port interconnection.

**Test Operations**

|  Take the MYZR-RZG2L-MB200 baseboard as an example:

1. Connect the CAN ports: connect CAN0_L to CAN1_L; connect CAN0_H to CAN1_H.
2. Configure can0 and can1:

.. code-block:: shell

   # ip link set can0 up type can bitrate 500000 dbitrate 1000000 fd on
   # ip link set can1 up type can bitrate 500000 dbitrate 1000000 fd on

3. Configure can0 for reception:

.. code-block:: shell

   # candump can0 &

4. can1 sends data:

.. code-block:: shell

   # cansend can1 1F334455#1122334455667788

5. The following data can be received:

.. code-block:: shell

   can0  1F334455   [8]  11 22 33 44 55 66 77 88

SPI Test
----------

**Description**

|  [Test Description]: Test is performed using the self-transmit and self-receive method.
|  [Interface Identification]: GPIO/SPI/UART
|  [System Device]: /dev/spidev1.0
|  [Interface Silkscreen]:

- MYZR-RZG2L-MB200: P3 (SPI1)
- MYZR-RZG2UL-MB200-ETH: NULL
- MYZR-RZG2UL-MB200-LCD: NULL

**Test Operations**

1. Short-circuit SPI1_MOSI and SPI1_MISO of P3, and enter the command:

.. code-block:: shell

   =====> Input:
   # /my-demo/spidev_test.out -D /dev/spidev1.0

   =====> Output:
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

RTC Test
---------

**Description**

|  [Test Description]: Read and set the time, and check if the time is correct after power-off and restart.
|  [Interface Identification]: RTC_Battery
|  [System Device]: /dev/rtc0
|  [Interface Silkscreen]: BT1

**Test Operations**

1. Power off and restart the device, then check the current system time and hardware time:

.. code-block:: shell

   =====> Input:
   # date

   =====> Output:
   Wed Feb  8 11:17:01 UTC 2023

2. Check the current RTC chip clock:

.. code-block:: shell

   =====> Input:
   # hwclock

   =====> Output:
   2023-02-08 11:17:13.930687+00:00

3. Set the system clock:

.. code-block:: shell

   =====> Input:
   # date -s "2023-02-08 15:00:00"

   =====> Output:
   Wed Feb  8 15:00:00 UTC 2023

4. Write the system clock to the hardware clock:

.. code-block:: shell

   # hwclock -w

5. Power off and restart the development board, then check the current system clock and hardware clock:

.. code-block:: shell

   =====> Input:
   # date

   =====> Output:
   Wed Feb  8 15:01:00 UTC 2023
   =====> Input:
   # hwclock

   =====> Output:
   2023-02-08 15:01:11.537317+00:00

Audio Playback Test
---------------------

**Description**

|  [Test Description]: Verify the audio playback function of the evaluation board by playing audio files.
|  [Interface Identification]: AUDIO
|  [System Device]: wm8960-audio
|  [Interface Silkscreen]:

- MYZR-RZG2L-MB200: P2
- MYZR-RZG2UL-MB200-ETH: P1
- MYZR-RZG2UL-MB200-LCD: P2

**Test Operations**

1. Insert headphones into the "AUDIO" port of the development board. Execute the following command to play audio:

.. code-block:: shell

   =====> Input:
   # aplay /usr/share/sounds/alsa/Front_Center.wav

   =====> Output:
   Playing WAVE '/usr/share/sounds/alsa/Front_Center.wav' : Signed 16 bit Little Endian, Rate 48000 Hz, Mono

2. The following command can be used to adjust the volume:

.. code-block:: shell

   # alsamixer

Recording Test
----------------

**Description**

|  [Test Description]: Verify the audio recording function of the evaluation board by recording and playing the recorded file.
|  [Interface Identification]: AUDIO
|  [System Device]: wm8960-audio
|  [Interface Silkscreen]:

- MYZR-RZG2L-MB200: P3
- MYZR-RZG2UL-MB200-ETH: P1
- MYZR-RZG2UL-MB200-LCD: P2

**Test Operations**

1. Insert headphones with a MIC into the headphone jack of the development board
2. Enter the following command to record for 4 seconds:

.. code-block:: shell

   =====> Input:
   # arecord -d 4 record.wav

   =====> Output:
   Recording WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

3. Play the recorded audio:

.. code-block:: shell

   =====> Input:
   # aplay record.wav

   =====> Output:
   Playing WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo


WIFI Test
-----------

**Description**

| 【Test Description】: After the WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal.
| 【Interface Identification】: WIFI&BT
| 【System Device】: wlan0
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200: U22, E2 (Antenna Interface)
- MYZR-RZG2UL-MB200-ETH: U24, E2 (Antenna Interface)
- MYZR-RZG2UL-MB200-LCD: U19, E2 (Antenna Interface)

**Test Operations**

1. Connect the WIFI antenna to the "E1/E2" interface.
2. Generate the WPA PSK file for the SSID.

.. code-block:: shell

   wpa_passphrase command format: wpa_passphrase + wifi name + wifi password > /etc/wpa_supplicant.conf

   =====> Input:
   # wpa_passphrase MYZR-WIFI-2.4G myzr2012 > /etc/wpa_supplicant.conf

3. Connect:

.. code-block:: shell

   =====> Input:
   # wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf 

   =====> Output:
   Successfully initialized wpa_supplicant
   [  487.018569] [dhd] dhd_open: Enter wlan0
   [  487.021051] [dhd] dhd_open : no mutex held. set lock
   [  487.026667] [dhd] 
   [  487.026667] Dongle Host Driver, version 100.10.545.18 (r826445-20210204-2)
   [  487.034982] [dhd-wlan0] wl_android_wifi_on : in g_wifi_on=0
   [  487.040477] [dhd] wifi_platform_set_power = 1, delay: 200 msec
   [  487.046317] [dhd] ======== PULL WL_REG_ON(62) HIGH! ========
   [  487.369854] sdio_reset_comm():
   [  487.450144] mmc0: queuing unknown CIS tuple 0x80 (2 bytes)
   [  487.465654] mmc0: queuing unknown CIS tuple 0x80 (3 bytes)
   。。。。。。

4. Obtain IP:

.. code-block:: shell

   =====> Input:
   # udhcpc -i wlan0

   =====> Output:
   udhcpc: started, v1.31.1
   udhcpc: sending discover
   udhcpc: sending select for 192.168.9.169
   udhcpc: lease of 192.168.9.169 obtained, lease time 86400
   /etc/udhcpc.d/50default: Adding DNS 192.168.9.1

5. Test Connection:

.. code-block:: shell

   =====> Input:
   # ping -I wlan0 www.baidu.com

   =====> Output:
   [   39.924248] RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 SeqNum = 40
   PING www.baidu.com (163.177.151.109): 56 data bytes
   [   40.813870] RTW: OnAction_back
   [   40.816968] RTW: OnAction_back, action=0
   [   40.821089] RTW: Drop duplicate management frame with seq_num = 668.
   64 bytes from 163.177.151.109: seq=0 ttl=56 time=233.235 ms
   [   40.832117] RTW: issue_addba_rsp_wait_ack(wlan0) ra=40:77:a9:64:76:b2 status:=0 tid=4 size:64, acked, 1/3 in 12 ms
   64 bytes from 163.177.151.109: seq=1 ttl=56 time=22.882 ms
   64 bytes from 163.177.151.109: seq=2 ttl=56 time=8.862 ms
   64 bytes from 163.177.151.109: seq=3 ttl=56 time=9.219 ms
   64 bytes from 163.177.151.109: seq=4 ttl=56 time=7.952 ms
   64 bytes from 163.177.151.109: seq=5 ttl=56 time=400.328 ms
   64 bytes from 163.177.151.109: seq=6 ttl=56 time=11.634 ms
   ^C
   --- www.baidu.com ping statistics ---
   7 packets transmitted, 7 packets received, 0% packet loss
   round-trip min/avg/max = 7.952/99.158/400.328 ms

| "0% packet loss" indicates that the WIFI connection is normal.

Bluetooth Test
----------------

**Description**

| 【Test Description】: After scanning for Bluetooth devices, send an L2CAP response request and receive the reply.
| 【Interface Identification】: WIFI&BT
| 【System Device】: hci0
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200: U22, E2 (Antenna Interface)
- MYZR-RZG2UL-MB200-ETH: U24, E2 (Antenna Interface)
- MYZR-RZG2UL-MB200-LCD: U19, E2 (Antenna Interface)

**Test Operations**

1. Connect the antenna to the "E2" interface.
2. Start Bluetooth:

.. code-block:: shell

   =====> Input:
   # hciconfig hci0 up
   # hciconfig 

   =====> Output:
   hci0:   Type: Primary  Bus: UART
       BD Address: B0:F1:EC:A7:E8:03  ACL MTU: 1021:8  SCO MTU: 64:1
       UP RUNNING 
       RX bytes:1266 acl:0 sco:0 events:66 errors:0
       TX bytes:1138 acl:0 sco:0 commands:66 errors:0

3. Scan for external Bluetooth devices:

.. code-block:: shell

   =====> Input:
   # hcitool scan
   
   =====> Output:
   Scanning ...
       88:46:04:4C:11:A7   Redmi K40

4. Send L2CAP packets for testing:

.. code-block:: shell

   =====> Input:
   # l2ping 88:46:04:4C:11:A7

   =====> Output:
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

| "0% packet loss" indicates that the Bluetooth connection is normal.

4G Module (EC20) Test
------------------------

**Description**

| 【Test Description】: After the 4G connection is successful, the development board sends ICMP packets to the external network to verify that the connection is normal.
| 【Interface Identification】: 4G
| 【System Device】: usb0
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200: J9
- MYZR-RZG2UL-MB200-ETH: J10
- MYZR-RZG2UL-MB200-LCD: J9

**Test Operations**

1. Power off the development board, connect the 4G module, attach the antenna, insert the SIM card, and then start the evaluation board.
2. Use the command to establish a network connection:

.. code-block:: shell

   =====> Input:
   # /myzr-demo/quectel-CM &

   =====> Output:
   [04-08_17:05:13:944] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
   [04-08_17:05:13:945] /usr/local/myzr-demo/quectel-CM profile[1] = (null)/(null)/(null)/0, pincode = (null)
   [04-08_17:05:13:948] Find /sys/bus/usb/devices/2-1.1 idVendor=2c7c idProduct=0125
   [04-08_17:05:13:948] Find /sys/bus/usb/devices/2-1.1:1.4/net/usb0
   [04-08_17:05:13:948] Find usbnet_adapter = usb0
   [04-08_17:05:13:949] Find /sys/bus/usb/devices/2-1.1:1.4/GobiQMI/qcqmi0
   [04-08_17:05:13:949] Find qmichannel = /dev/qcqmi0
   [04-08_17:05:14:014] Get clientWDS = 7
   [04-08_17:05:14:048] Get clientDMS = 8
   [04-08_17:05:14:079] Get clientNAS = 9
   [04-08_17:05:14:111] Get clientUIM = 10
   [04-08_17:05:14:143] Get clientWDA = 11
   [04-08_17:05:14:174] requestBaseBandVersion EC20CEFAR02A10M4G
   [04-08_17:05:14:271] requestGetSIMStatus SIMStatus: SIM_READY
   [04-08_17:05:14:302] requestGetProfile[1] cmnet///0
   [04-08_17:05:14:334] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [04-08_17:05:14:366] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
   [04-08_17:05:14:431] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
   [04-08_17:05:14:974] requestSetupDataCall WdsConnectionIPv4Handle: 0x87206180
   [04-08_17:05:15:071] requestQueryDataCall IPv4ConnectionStatus: CONNECTED
   [04-08_17:05:15:103] ifconfig usb0 up
   [04-08_17:05:15:114] busybox udhcpc -f -n -q -t 5 -i usb0
   udhcpc: started, v1.31.1
   udhcpc: sending discover
   udhcpc: sending select for 10.145.82.192
   udhcpc: lease of 10.145.82.192 obtained, lease time 7200
   [04-08_17:05:15:502] /etc/udhcpc.d/50default: Adding DNS 221.179.38.7
   [04-08_17:05:15:502] /etc/udhcpc.d/50default: Adding DNS 120.196.165.7

3. Connection Test:

.. code-block:: shell

   =====> Input:
   # ping -I usb0 www.baidu.com

   =====> Output:
   PING www.wshifen.com (104.193.88.77) 56(84) bytes of data.
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=1 ttl=42 time=263 ms
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=2 ttl=42 time=233 ms
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=3 ttl=42 time=232 ms
   ^C
   --- www.wshifen.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2000ms
   rtt min/avg/max/mdev = 232.138/242.649/262.712/14.191 ms

| "0% packet loss" indicates that the 4G connection is normal.

DSI Display
-------------

**Description**

| 【Test Description】: To use DSI display, the device tree must be replaced first.
| 【Interface Identification】: DSI
| 【Interface Silkscreen】: J6
| Note: Only the rzg2l supports the DSI display function.

**Test Operations**

1. Start the development board. Before the uboot countdown ends, press the Enter key to enter the uboot command line mode. Enter `printenv fdtfile` to check the current device tree name.

.. code-block:: shell

   => printenv fdtfile 
   fdtfile=myzr-rzg2l-rgb.dtb

2. If the current device tree is not the DSI one, replace it:

.. code-block:: shell

   => setenv fdtfile myzr-rzg2l-dsi.dtb

3. Save the current environment variables.

.. code-block:: shell

   => saveenv 
   Saving Environment to MMC... Writing to MMC(0)... OK

4. Power off the board, connect the DSI display, and start the development board. The boot screen will be displayed on the screen.



RGB Display
-------------

**Description**

| 【Test Description】: The system defaults to RGB display. If HDMI display has been switched to, it needs to be switched back.
| 【Interface Identification】: LCD
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200：P1
- MYZR-RZG2UL-MB200-ETH：NULL
- MYZR-RZG2UL-MB200-LCD：P1

| Note: Only MYZR-RZG2L-MB200 and MYZR-RZG2UL-MB200-LCD have LCD display function. The device tree corresponding to MYZR-RZG2UL-MB200-LCD is: myzr-rzg2ul-lcd.dtb, which does not need to be replaced.

**Test Operation**

| Switch rzg2l to RGB display:

1. Start the development board, press the Enter key before the uboot countdown ends to enter the uboot command line mode, and enter `printenv fdtfile` to check the current device tree name

.. code-block:: shell

   => printenv fdtfile 
   fdtfile=myzr-rzg2l-dsi.dtb

2. If the current device tree is not RGB, replace it:

.. code-block:: shell

   => setenv fdtfile myzr-rzg2l-rgb.dtb

3. Save the current environment variables

.. code-block:: shell

   => saveenv 
   Saving Environment to MMC... Writing to MMC(0)... OK

4. Power off, connect the RGB display screen, and start the development board. The startup screen will be displayed on the display screen.


ADC Test
----------

**Description**

| 【Test Description】: Read the sampling output value of the ADC pin
| 【Interface Identification】: GPIO/SPI/UART
| 【System Device】: /sys/bus/iio/devices/iio:devicex
| 【Interface Silkscreen】:

- MYZR-RZG2L-MB200：J11
- MYZR-RZG2UL-MB200-ETH：P2（ADC_CH0, ADC_CH01）
- MYZR-RZG2UL-MB200-LCD：J12（ADC_CH0, ADC_CH01）

**Test Operation**

| Take the MYZR-RZG2L-MB200 baseboard as an example:

1. Find the peripheral corresponding to ADC:

.. code-block:: shell

   # grep -H "" /sys/bus/iio/devices/*/name | grep adc
   /sys/bus/iio/devices/iio:device0/name:rzg2l-adc

| It can be known that the ADC channel node is in the /sys/bus/iio/devices/iio:device0 directory

2. You can short-circuit the ADC_CH0 channel and pin J11:1 (i.e., short-circuit to ground), then read the ADC value

.. code-block:: shell

   =====> Input:
   # cat /sys/bus/iio/devices/iio\:device0/in_voltage0_raw

   =====> Output:
   0

3. The maximum sampling voltage shall not exceed 1.8V; otherwise, the core board may be damaged. The maximum sampling output value is 4096.
