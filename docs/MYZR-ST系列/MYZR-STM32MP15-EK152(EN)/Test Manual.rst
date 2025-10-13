Test Manual
=============

Test Environment
~~~~~~~~~~~~~~~~~~

- Development Board Model: MYZR-STM32MP15-EK152
- Kernel Version: Linux-5.4.31
- File System:

 |  st-image-bootfs-openstlinux-weston-stm32mp1.ext4;
 |  st-image-vendorfs-openstlinux-weston-stm32mp1.ext4;
 |  st-image-weston-openstlinux-weston-stm32mp1.ext4;
 |  st-image-userfs-openstlinux-weston-stm32mp1.ext4;

Interface Identification Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32mp1-Front-view.png
   :alt: Stm32mp1-Front-view.png

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/Stm32mp1-Back-view.png
   :alt: Stm32mp1-Back-view.png

Ethernet Port Test
~~~~~~~~~~~~~~~~~~~~

|  [Test Description]: The test is performed by sending ICMP packets from the development board to the PC
|  [Interface Identification]: ETH10/100/1000M
|  [Interface Silkscreen]: U4
|  [System Interface]: eth0

**Test Operations**

|  1. Configure the PC's wired network card IP to 192.168.137.99
|  2. Connect the board's Ethernet port to the PC's Ethernet port with a network cable
|  3. Enter the following command to communicate with the PC:

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

|  "0% packet loss" indicates the test is passed.

USB Test
~~~~~~~~~~

|  [Test Description]: The test is performed by plugging and unplugging a USB storage device (USB flash drive)
|  [Interface Identification]: USB2.0
|  [Interface Silkscreen]: P5

**Test Operations**

1. Insert the USB device into the USB interface of the base board, and the system will output information similar to the following:

.. code-block:: shell

   root@stm32mp1:~# [ 3288.330096] usb 2-1.4: new high-speed USB device number 3 using ehci-platform
   [ 3288.396730] usb-storage 2-1.4:1.0: USB Mass Storage device detected
   [ 3288.413395] scsi host0: usb-storage 2-1.4:1.0
   [ 3288.595095] usbcore: registered new interface driver uas
   [ 3289.452460] scsi 0:0:0:0: Direct-Access     Generic- SD/MMC           1.00 PQ: 0 ANSI: 4
   [ 3289.468478] sd 0:0:0:0: Attached scsi generic sg0 type 0
   [ 3290.224654] sd 0:0:0:0: [sda] 60932096 512-byte logical blocks: (31.2 GB/29.1 GiB)
   [ 3290.232024] sd 0:0:0:0: [sda] Write Protect is off
   [ 3290.236486] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, does\'t support DPO or FUA
   [ 3290.307279] sda: sda1
   [ 3290.314548] sd 0:0:0:0: [sda] Attached SCSI removable disk

2. Unplug the USB device from the base board, and the system will output information similar to the following:

.. code-block:: shell

   root@stm32mp1:~# [ 3343.077203] usb 2-1.4: USB disconnect, device number 3

SD Interface Test
~~~~~~~~~~~~~~~~~~~

|  [Test Description]: The test is performed by inserting and recognizing a TF card
|  [Interface Identification]: TF
|  [Interface Silkscreen]: P3

**Test Operations**

1. Install the TF card into the SD interface, and the development board will output the following information:

.. code-block:: shell
   
   root@stm32mp1:~# [ 3697.015101] mmc1: new high speed SDHC card at address 1234
   [ 3697.035081] mmcblk1: mmc1:1234 SA32G 29.1 GiB 
   [ 3697.042740]  mmcblk1: p1

2. The corresponding SD interface device can be viewed with the following command:

.. code-block:: shell
   
   # ls /dev/mmcblk1*
   /dev/mmcblk1  /dev/mmcblk1p1

3. Unplug the TF card, and the following information will be output:

.. code-block:: shell
   
   root@stm32mp1:~# [ 3985.400589] mmc1: card 1234 removed

GPIO Test
~~~~~~~~~~~

|  [Test Description]: Control the output/input level of GPIO
|  [Interface Identification]: GPIO/SPI/UART
|  [Interface Silkscreen]: P21
|  [System Interface]: /dev/gpiochipx

**Test Operations**

1. List all gpiochips on the system:

.. code-block:: shell
   
   =====> Input:
   # gpiodetect 

   =====> Output:
   gpiochip0 [GPIOA] (16 lines)
   gpiochip1 [GPIOB] (16 lines)
   gpiochip2 [GPIOC] (16 lines)
   gpiochip3 [GPIOD] (16 lines)
   gpiochip4 [GPIOE] (16 lines)
   gpiochip5 [GPIOF] (16 lines)
   gpiochip6 [GPIOG] (16 lines)
   gpiochip7 [GPIOH] (16 lines)
   gpiochip8 [GPIOI] (16 lines)
   gpiochip9 [GPIOZ] (16 lines)

2. Configure pin P21-38 (i.e., PF15) to output high level:

.. code-block:: shell
   
   # gpioset gpiochip5 15=1

|  Use a multimeter to measure pin P21-38, and a voltage of 3.3V (i.e., high level) should be detected.

3. Configure pin P21-38 (i.e., PF15) to output low level:

.. code-block:: shell
   
   # gpioset gpiochip5 15=0

|  Use a multimeter to measure pin P21-38, and a voltage of 0V (i.e., low level) should be detected.

4. Configure pin P21-38 (i.e., PF15) as input and read its value:

.. code-block:: shell
   
   =====> Input:
   # gpioget  gpiochip5 15

   =====> Output:
   0

Serial Port Test
~~~~~~~~~~~~~~~~~~

**UART**

|  [Test Description]: The test is performed by self-transmitting and self-receiving via the serial port
|  [Interface Identification]: GPIO/SPI/UART
|  [Interface Location]: P21
|  [System Device]: /dev/ttySTM6 (uart7), /dev/ttySTM7 (uart8)

**Test Operations**

1. Short-circuit pins P21-11 and P21-13, i.e., uart7_rx and uart7_tx
2. Enter the following command to perform uart7 transmission and reception test:

.. code-block:: shell
   
   =====> Input:
   # /usr/local/myzr-demo/serial_test.out /dev/ttySTM6 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x0   Character:  

|  After executing the test command, if the application outputs information similar to the above, it indicates normal operation.

3. Enter the following command to perform uart8 transmission and reception test:

.. code-block:: shell

   =====> Input:
   # /usr/local/myzr-demo/serial_test.out /dev/ttySTM7 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x0   Character:

|  After executing the test command, if the application outputs information similar to the above, it indicates normal operation.

**RS232**

|  [Test Description]: The test is performed by self-transmitting and self-receiving via the serial port
|  [Interface Identification]: RS232
|  [Interface Location]: P16
|  [System Device]: /dev/ttySTM2 (usart3)

**Test Operations**

1. Short-circuit pins P16-1 and P16-2, i.e., TX and RX
2. Enter the following command to perform RS232 transmission and reception test:

.. code-block:: shell
   
   =====> Input:
   # /usr/local/myzr-demo/serial_test.out /dev/ttySTM2 "myzr"

   =====> Output:
   Starting send data...finish
   Starting receive data:
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x0   Character:  

|  After executing the test command, if the application outputs information similar to the above, it indicates normal operation.

**RS485**

|  [Test Description]: RS485 uses differential signals and cannot be tested by self-transmitting and self-receiving.
|  [Interface Identification]: RS485
|  [Interface Location]: P17
|  [System Device]: /dev/ttySTM4 (uart5)

**Test Operations**

1. Use a 485-232 converter to connect pins P17-A/B to the PC's USB-to-serial cable
2. Open the serial port debugging assistant, set the baud rate to 9600, no parity bit, 8 data bits, and 1 stop bit.
3. Log in to the development board via SSH and send data to the PC:

.. code-block:: shell
   
   # echo 123 > /dev/ttySTM4

|  The serial port assistant should receive the string "123".

4. The development board receives data, and the PC sends data:

.. code-block:: shell
   
   # cat /dev/ttySTM4

|  When the serial port assistant sends a string, the development board will receive the data:

.. code-block:: shell
   
   # cat /dev/ttySTM4 
   myzr

CAN Test
~~~~~~~~~~

|  Note: Only the core boards of stm32mp157/stm32mp153 have CAN functionality, and two boards need to be connected for the test.

|  [Test Description]: Send data to each other between CAN ports
|  [Interface Identification]: CAN
|  [Interface Location]: P13
|  [System Device]: can0

**Test Operations**

1. Prepare two development boards, connect their CAN ports: connect CAN_L to CAN_L, and CAN_H to CAN_H.
2. Configure can0 on both boards:

.. code-block:: shell
   
   # ip link set can0 up type can bitrate 125000

3. Configure one of the boards as the receiver:

.. code-block:: shell
   
   # candump can0

4. Configure the other board to send data:

.. code-block:: shell
   
   # cansend can0 1F334455#1122334455667788

5. The receiver should receive the following data:

.. code-block:: shell
   
   can0  1F334455   [8]  11 22 33 44 55 66 77 88

SPI Test
~~~~~~~~~~

|  [Test Description]: The test is performed by self-transmitting and self-receiving.
|  [Interface Identification]: GPIO/SPI/UART
|  [Interface Location]: P21
|  [System Device]: /dev/spidev0.0 (SPI1), /dev/spidev1.0 (SPI5)

**Test Operations**

1. Short-circuit pins P21-2 and P21-4, i.e., SPI1_MOSI and SPI1_MISO, and enter the command:

.. code-block:: shell
   
   =====> Input:
   # /usr/local/myzr-demo/spidev_test.out -D /dev/spidev0.0

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

2. Short-circuit pins P21-1 and P21-3, i.e., SPI5_MOSI and SPI5_MISO, and enter the command:

.. code-block:: shell

   =====> Input:
   # /usr/local/myzr-demo/spidev_test.out -D /dev/spidev1.0

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
~~~~~~~~~~

|  [Test Description]: Read and set the time, then check if the time is correct after power-off and restart
|  [Interface Identification]: RTC_Battery
|  [Interface Location]: BT1
|  [System Device]: /dev/rtc0

**Test Operations**

1. Power off and restart the device, then check the current system time and hardware time:

.. code-block:: shell

   =====> Input:
   # date

   =====> Output:
   Fri Feb  7 15:51:25 UTC 2020

2. Check the current RTC chip clock:

.. code-block:: shell

   =====> Input:
   # hwclock

   =====> Output:
   hwclock: ioctl(RTC_RD_TIME) to /dev/rtc0 to read the time failed: Invalid argument

3. Set the system clock:

.. code-block:: shell

   =====> Input:
   # date -s "2021-04-08 15:00:00"

   =====> Output:
   Thu Apr  8 15:00:00 UTC 2021

4. Write the system clock to the hardware clock:

.. code-block:: shell
   
   # hwclock -w

5. Power off and restart the development board, then check the current system clock and hardware clock:

.. code-block:: shell

   =====> Input:
   # date

   =====> Output:
   Thu Apr  8 15:04:49 UTC 2021
   =====> Input:
   # hwclock

   =====> Output:
   2021-04-08 15:05:09.146857+00:00

Audio Playback Test
~~~~~~~~~~~~~~~~~~~~~

|  [Test Description]: Verify the audio playback function of the evaluation board by playing audio files.
|  [Interface Identification]: AUDIO
|  [Interface Location]: P10
|  [System Device]: wm8960-audio

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

Audio Recording Test
~~~~~~~~~~~~~~~~~~~~~~

|  [Test Description]: Verify the audio recording function of the evaluation board by recording and playing back the recorded file.
|  [Interface Identification]: AUDIO
|  [Interface Location]: P10, P11
|  [System Device]: wm8960-audio

**Test Operations**

1. Insert a headphone with a MIC into the headphone jack of the development board, or use the built-in MIC (P11) on the development board directly.

2. Enter the following command to record audio for 8 seconds:

.. code-block:: shell
   
   =====> Input:
   # arecord -D hw:0,1 -f cd -d 8  record.wav

   =====> Output:
   Recording WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

3. Play back the recorded audio:

.. code-block:: shell
   
   =====> Input:
   # aplay record.wav

   =====> Output:
   Playing WAVE 'record.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

WIFI Test
~~~~~~~~~~~

|  [Test Description]: After WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal.
|  [Interface Identification]: WIFI&BT
|  [Interface Silkscreen]: U12, E1
|  [System Device]: wlan0

**Test Operations**

1. Connect the WIFI antenna to the "E1" interface.

2. Generate a WPA PSK file for the SSID. Command format: wpa_passphrase [SSID] [passphrase]

.. code-block:: shell
   
   =====> Input:
   # wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf 
   # pkill wpa_supplicant

3. Establish the connection:

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
   ......

4. Obtain an IP address:

.. code-block:: shell

   =====> Input:
   # udhcpc -i wlan0

   =====> Output:
   udhcpc: started, v1.31.1
   udhcpc: sending discover
   udhcpc: sending select for 192.168.9.169
   udhcpc: lease of 192.168.9.169 obtained, lease time 86400
   /etc/udhcpc.d/50default: Adding DNS 192.168.9.1

5. Test the connection:

.. code-block:: shell

   =====> Input:
   # ifconfig eth0 down
   # ping  www.baidu.com

   =====> Output:
   PING www.a.shifen.com (163.177.151.110) 56(84) bytes of data.
   64 bytes from 163.177.151.110 (163.177.151.110): icmp_seq=1 ttl=56 time=10.7 ms
   64 bytes from 163.177.151.110 (163.177.151.110): icmp_seq=2 ttl=56 time=9.29 ms
   64 bytes from 163.177.151.110 (163.177.151.110): icmp_seq=3 ttl=56 time=30.1 ms
   64 bytes from 163.177.151.110 (163.177.151.110): icmp_seq=4 ttl=56 time=9.74 ms

   --- www.a.shifen.com ping statistics ---
   4 packets transmitted, 4 received, 0% packet loss, time 3005ms
   rtt min/avg/max/mdev = 9.288/14.962/30.092/8.750 ms

Bluetooth Test
~~~~~~~~~~~~~~~~

|  [Test Description]: After scanning for Bluetooth devices, send an L2CAP response request and receive the reply.
|  [Interface Identification]: WIFI&BT
|  [Interface Silkscreen]: U12, E1
|  [System Device]: hci0

**Test Operations**

1. Connect the antenna to the "E1" interface.

2. Initialize the Bluetooth device:

.. code-block:: shell

   =====> Input:
   # gpioset gpiochip9 6=1
   # brcm_patchram_plus  --enable_hci -no2bytes --tosleep 200000 --baudrate 115200 --patchram /etc/firmware/bcm43438a1.hcd /dev/ttySTM1 &

3. Start Bluetooth:

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

4. Scan for external Bluetooth devices:

.. code-block:: shell

   =====> Input:
   # hcitool scan

   =====> Output:
   Scanning ...
       88:46:04:4C:11:A7   Redmi K40

5. Send an L2CAP packet for testing:

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
   8 sent, 8 received, 0% loss

|  "0% packet loss" indicates that the Bluetooth connection is normal.


4G Module (EC20) Test
~~~~~~~~~~~~~~~~~~~~~~~

|  [Test Description]: After the 4G connection is successful, the development board sends ICMP packets to the external network to verify that the connection is normal.
|  [Interface Identification]: 4G
|  [Interface Silkscreen]: P7
|  [System Device]: usb0

**Test Operations**

1. Power off the development board, connect the 4G module, attach the antenna, insert the SIM card, and then start the evaluation board.

2. Use the command to establish a network connection:

.. code-block:: shell
   
   =====> Input:
   # /usr/local/myzr-demo/quectel-CM &

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

3. Test the connection:

.. code-block:: shell

   =====> Input:
   # ifconfig eth0 down
   # ping www.baidu.com

   =====> Output:
   PING www.wshifen.com (104.193.88.77) 56(84) bytes of data.
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=1 ttl=42 time=263 ms
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=2 ttl=42 time=233 ms
   64 bytes from 104.193.88.77 (104.193.88.77): icmp_seq=3 ttl=42 time=232 ms

   --- www.wshifen.com ping statistics ---
   3 packets transmitted, 3 received, 0% packet loss, time 2000ms
   rtt min/avg/max/mdev = 232.138/242.649/262.712/14.191 ms

|  "0% packet loss" indicates that the WIFI connection is normal.


Sleep and Wake-up Test
~~~~~~~~~~~~~~~~~~~~~~~~

|  [Test Description]: The system enters sleep mode and is woken up using the wake-up button
|  [Interface Identification]: None
|  [Interface Silkscreen]: None

**Test Operations**

1. Put the system into sleep mode

.. code-block:: shell

   =====> Input:
   # echo mem > /sys/power/state

   =====> Output:
   [  100.468138] PM: suspend entry (deep)
   [  100.485714] Filesystems sync: 0.015 seconds
   [  100.492393] Freezing user space processes ... (elapsed 0.002 seconds) done.
   [  100.500456] OOM killer disabled.
   [  100.503573] Freezing remaining freezable tasks ... (elapsed 0.001 seconds) done.
   [  100.511083] printk: Suspending console(s) (use no_console_suspend to debug)

2. Wake up using the sw2 button. After pressing the button, the system resumes:

.. code-block:: shell

   =====> Output:
   NOTICE:  CPU: STM32MP157AAC Rev.Z
   NOTICE:  Model: MYZR STM32MP15 Discovery Board
   INFO:    Reset reason (0x810):
   INFO:    System exits from STANDBY
   INFO:    PMIC version = 0x21
   INFO:    Using SDMMC
   INFO:      Instance 1
   INFO:    Boot used partition fsbl1
   NOTICE:  BL2: v2.2-r1.0(debug):
   NOTICE:  BL2: Built : 07:34:54, Apr 14 2021
   INFO:    Using crypto library 'stm32_crypto_lib'
   INFO:    BL2: Doing platform setup
   INFO:    RAM: DDR3-DDR3L 16bits 533000Khz
   INFO:    BL2 runs SP_MIN setup
   INFO:    BL2: Loading image id 4
   INFO:    Loading image id=4 at address 0x2ffed000
   INFO:    Image id=4 loaded: 0x2ffed000 - 0x2ffff000
   INFO:    BL2: Skip loading image id 5
   NOTICE:  BL2: Booting BL32
   INFO:    Entry point address = 0x2ffed000
   INFO:    SPSR = 0x1d3
   NOTICE:  SP_MIN: v2.2-r1.0(debug):
   NOTICE:  SP_MIN: Built : 07:35:03, Apr 14 2021
   INFO:    ARM GICv2 driver initialized
   INFO:    stm32mp IWDG1 (12): Secure
   INFO:    ETZPC: CRYP1 (9) could be non secure
   INFO:    SP_MIN: Initializing runtime services
   INFO:    SP_MIN: Preparing exit to normal world
   [   77.721158] dwc2 49000000.usb-otg: suspending usb gadget configfs-gadget
   [   77.764676] Disabling non-boot CPUs ...
   [   77.765689] CPU1 killed.
   [   77.775207] Enabling non-boot CPUs ...
   [   77.778224] CPU1 is up
   [   77.795959] dwmac4: Master AXI performs any burst length
   [   77.795994] stm32-dwmac 5800a000.ethernet eth0: No Safety Features support found
   [   77.796061] stm32-dwmac 5800a000.ethernet eth0: configuring for phy/rgmii-id link mode
   [   77.799109] usb usb2: root hub lost power or was reset
   [   77.802455] dwc2 49000000.usb-otg: resuming usb gadget configfs-gadget
   [   78.199987] usb 2-1: reset high-speed USB device number 2 using ehci-platform
   [   78.429336] OOM killer enabled.
   [   78.432502] Restarting tasks ... done.
   [   78.506503] PM: suspend exit

ADC Test
~~~~~~~~~~

|  [Test Description]: Read the sampling output value of the ADC pin
|  [Interface Identification]: GPIO/SPI/UART
|  [Interface Silkscreen]: P21
|  [System Device]: /sys/bus/iio/devices/iio:device*/

**Test Operations**

1. Pin P21:18 (ANA0) is ADC channel 0, and pin P21:17 (ANA1) is ADC channel 1.

2. You can short-circuit channel 0 with pin P21:40 (i.e., short to ground), then read the ADC value:

.. code-block:: shell
   
   =====> Input:
   # cat /sys/bus/iio/devices/iio\:device0/in_voltage0_raw

   =====> Output:
   0

3. The maximum sampling voltage must not exceed 3.3V, otherwise it may cause damage to the core board. The maximum sampling output value is 65535.
