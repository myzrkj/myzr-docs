Test Manual
=============

Ethernet Port 0
-----------------

|  **Test Description**: Test by sending ICMP packets from the development board to PC
|  **Interface Label**: ETH1
|  **System Device**: eth0
|  **Test Procedure**:

1. Connect the Ethernet port of the development board to the PC Ethernet port with a network cable, enter the following command to enable Ethernet Port 0

.. code-block:: shell

   ifconfig eth0 up

|  Output information is as follows

.. code-block:: shell

   [emac_phy_link_adjust] EMAC Link Up

2. Enter the following command to obtain the Ethernet port IP

.. code-block:: shell

   udhcpc -i eth0 -s /etc/init.d/udhcpc.script

|  Output information is as follows

.. code-block:: shell

   / # udhcpc -i eth0 -s /etc/init.d/udhcpc.script
   udhcpc (v1.20.2) started
   Setting IP address 0.0.0.0 on eth0
   Sending discover...
   Sending select for 192.168.128.40...
   Lease of 192.168.128.40 obtained, lease time 300
   Setting IP address 192.168.128.40 on eth0
   Deleting routers
   route: SIOCDELRT: No such process
   Adding router 192.168.128.1
   Recreating /customer/resolv.conf
    Adding DNS server 192.168.128.1

3. Enter the following command for Ethernet port verification

.. code-block:: shell

   ping baidu.com -c 4

|  Output information is as follows: "0% packet loss" indicates the test passes

.. code-block:: shell

    # ping baidu.com -c 4
   PING baidu.com (124.237.177.164): 56 data bytes
   64 bytes from 124.237.177.164: seq=0 ttl=53 time=35.747 ms
   64 bytes from 124.237.177.164: seq=1 ttl=53 time=35.424 ms
   64 bytes from 124.237.177.164: seq=2 ttl=53 time=35.335 ms
   64 bytes from 124.237.177.164: seq=3 ttl=53 time=35.782 ms
   --- baidu.com ping statistics ---
   4 packets transmitted, 4 packets received, 0% packet loss

Ethernet Port 1
-----------------

|  **Test Description**: Test by sending ICMP packets from the development board to PC
|  **Interface Label**: ETH2
|  **System Device**: eth1
|  **Test Procedure**:

1. Connect the Ethernet port of the development board to the PC Ethernet port with a network cable, enter the following command to enable Ethernet Port 1

.. code-block:: shell

   ifconfig eth1 up

|  Output information is as follows

.. code-block:: shell

   [emac_phy_link_adjust] EMAC Link Up

2. Enter the following command to obtain the Ethernet port IP

.. code-block:: shell

   udhcpc -i eth1 -s /etc/init.d/udhcpc.script

|  Output information is as follows

.. code-block:: shell

   / # udhcpc -i eth1 -s /etc/init.d/udhcpc.script
   udhcpc (v1.20.2) started
   Setting IP address 0.0.0.0 on eth1
   Sending discover...
   Sending select for 192.168.128.40...
   Lease of 192.168.128.40 obtained, lease time 300
   Setting IP address 192.168.128.40 on eth1
   Deleting routers
   route: SIOCDELRT: No such process
   Adding router 192.168.128.1
   Recreating /customer/resolv.conf
    Adding DNS server 192.168.128.1
   mount: mounting /customer/resolv.conf on /etc/resolv.conf failed: No such file or directory

3. Enter the following command for Ethernet port verification

.. code-block:: shell

   ping baidu.com -c 4

|  Output information is as follows: "0% packet loss" indicates the test passes

.. code-block:: shell

    # ping baidu.com -c 4
   PING baidu.com (124.237.177.164): 56 data bytes
   64 bytes from 124.237.177.164: seq=0 ttl=53 time=35.747 ms
   64 bytes from 124.237.177.164: seq=1 ttl=53 time=35.424 ms
   64 bytes from 124.237.177.164: seq=2 ttl=53 time=35.335 ms
   64 bytes from 124.237.177.164: seq=3 ttl=53 time=35.782 ms
   --- baidu.com ping statistics ---
   4 packets transmitted, 4 packets received, 0% packet loss

USB
-----

|  **Test Description**: Test by hot-plugging method
|  **Interface Label**: HOST
|  **System Device**: /dev/sda1
|  **Test Procedure**:

1. Pull up PM_SAR_GPIO4 to recognize the device, enter the following commands

.. code-block:: shell

   echo 147 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio147/direction
   echo 1 > /sys/class/gpio/gpio147/value

2. Insert the U disk and enter the following command to view U disk information

.. code-block:: shell

   fdisk -l

|  Output information is as follows

.. code-block:: shell

   Disk /dev/sda: 247.9 GB, 247993466880 bytes
   256 heads, 63 sectors/track, 30032 cylinders
   Units = cylinders of 16128 * 512 = 8257536 bytes
      Device Boot      Start         End      Blocks  Id System
   /dev/sda1               1       30033   242181088+ 83 Linux

SD Card
---------

|  **Test Description**: Test by hot-plugging method
|  **Interface Label**: SD
|  **System Device**: /dev/mmcblk0p1
|  **Test Procedure**:

1. Insert the SD card, enter the following command to view SD card information

.. code-block:: shell

   fdisk -l

|  Output information is as follows

.. code-block:: shell

   Disk /dev/mmcblk0: 7746 MB, 7746879488 bytes
   256 heads, 63 sectors/track, 938 cylinders
   Units = cylinders of 16128 * 512 = 8257536 bytes

           Device Boot      Start         End      Blocks  Id System
   /dev/mmcblk0p1   *           1         939     7564288   c Win95 FAT32 (LBA)
   Partition 1 has different physical/logical beginnings (non-Linux?):
        phys=(1023, 255, 63) logical=(0, 32, 33)
   Partition 1 has different physical/logical endings:
        phys=(1023, 255, 63) logical=(938, 40, 40)

GPIO
-------

|  **Test Description**: Test by pulling high and pulling low the pin level
|  **Interface Label**:
|  **System Device**: /sys/class/gpio/
|  **Test Procedure**:
|  GPIOE_01 (Pin No.4 on the left header facing the Ethernet port)

1. Enter the following commands to pull up GPIOE_01

.. code-block:: shell

   echo 10 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio10/direction
   echo 1 > /sys/class/gpio/gpio10/value
   cat /sys/class/gpio/gpio10/value

|  Measure this pin with a multimeter, the level is 3.3V high level

2. Enter the following commands to pull down GPIOE_01

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio10/value
   cat /sys/class/gpio/gpio10/value

|  Measure this pin with a multimeter, the level is 0V low level
|  GPIOE_02 (Pin opposite No.6 on the left header facing the Ethernet port)

1. Enter the following commands to pull up GPIOE_02

.. code-block:: shell

   echo 11 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio11/direction
   echo 1 > /sys/class/gpio/gpio11/value
   cat /sys/class/gpio/gpio11/value

|  Measure this pin with a multimeter, the level is 3.3V high level

2. Enter the following commands to pull down GPIOE_02

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio11/value
   cat /sys/class/gpio/gpio11/value

|  Measure this pin with a multimeter, the level is 0V low level
|  GPIOE_03 (Pin opposite No.5 on the left header facing the Ethernet port)

1. Enter the following commands to pull up GPIOE_03

.. code-block:: shell

   echo 12 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio12/direction
   echo 1 > /sys/class/gpio/gpio12/value
   cat /sys/class/gpio/gpio12/value

|  Measure this pin with a multimeter, the level is 3.3V high level

2. Enter the following commands to pull down GPIOE_03

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio12/value
   cat /sys/class/gpio/gpio12/value

|  Measure this pin with a multimeter, the level is 0V low level
|  GPIOE_04 (Pin No.-6 on the left header facing the Ethernet port)

1. Enter the following commands to pull up GPIOE_04

.. code-block:: shell

   echo 13 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio13/direction
   echo 1 > /sys/class/gpio/gpio13/value
   cat /sys/class/gpio/gpio13/value

|  Measure this pin with a multimeter, the level is 3.3V high level

2. Enter the following commands to pull down GPIOE_04

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio13/value
   cat /sys/class/gpio/gpio13/value

|  Measure this pin with a multimeter, the level is 0V low level
|  GPIOE_05 (Pin opposite No.-5 on the left header facing the Ethernet port)

1. Enter the following commands to pull up GPIOE_05

.. code-block:: shell

   echo 14 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio14/direction
   echo 1 > /sys/class/gpio/gpio14/value
   cat /sys/class/gpio/gpio14/value

|  Measure this pin with a multimeter, the level is 3.3V high level

2. Enter the following commands to pull down GPIOE_05

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio14/value
   cat /sys/class/gpio/gpio14/value

|  Measure this pin with a multimeter, the level is 0V low level

LED
------

|  **Test Description**: Test by pulling high and pulling low the pin level
|  **Interface Label**: led2 ,led3,led4
|  **System Device**:
|  **Test Procedure**:
|  led2

1. Enter the following commands to turn on led2

.. code-block:: shell

   echo 75 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio75/direction
   echo 1 > /sys/class/gpio/gpio75/value

2. Enter the following commands to turn off led2

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio75/value

|  LED3

1. Enter the following commands to turn on led3

.. code-block:: shell

   echo 74 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio74/direction
   echo 1 > /sys/class/gpio/gpio74/value

2. Enter the following commands to turn off led3

.. code-block:: shell

   echo 0 > /sys/class/gpio/gpio74/value

|  LED4

1. Enter the following commands to turn on led4

.. code-block:: shell

   echo 69 > /sys/class/gpio/export
   echo out > /sys/class/gpio/gpio69/direction
   echo 1 > /sys/class/gpio/gpio69/value

1. Enter the following commands to turn off led4

.. code-block:: shell

   echo 0  > /sys/class/gpio/gpio69/value

I2C
------

|  **Test Description**: Test by reading I2C device address
|  **Interface Label**:
|  **System Device**: ttyS2,ttyS3,ttyS4
|  **Test Procedure**:
|  i2c2

1. Enter the test directory and input the following command

.. code-block:: shell

   cd /customer

2. Connect SCL and SDA pins of the I2C device to SCL and SDA of i2c0, connect GND to development board GND. The address of the test I2C device is 0x3c, enter the following command to read the I2C device

.. code-block:: shell

   ./i2cdump -f -y 2 0x3c

|  Output information is as follows

.. code-block:: shell

   /customer # ./i2cdump -f -y 2 0x3c
   No size specified (using byte-data access)
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
   00: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   10: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   20: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   30: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   40: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   50: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   60: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   70: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   80: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   90: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   a0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   b0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   c0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   d0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   e0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   f0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB

|  i2c3

1. Enter the test directory and input the following command

.. code-block:: shell

   cd /customer

2. Connect SCL and SDA pins of the I2C device to SCL and SDA of i2c0, connect GND to development board GND. The address of the test I2C device is 0x3c, enter the following command to read the I2C device

.. code-block:: shell

   ./i2cdump -f -y 3 0x3c

|  Output information is as follows

.. code-block:: shell

   /customer # ./i2cdump -f -y 3 0x3c
   No size specified (using byte-data access)
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
   00: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   10: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   20: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   30: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   40: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   50: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   60: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   70: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   80: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   90: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   a0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   b0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   c0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   d0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   e0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   f0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB

|  i2c4

1. Enter the test directory and input the following command

.. code-block:: shell

   cd /customer

2. Connect SCL and SDA pins of the I2C device to SCL and SDA of i2c0, connect GND to development board GND. The address of the test I2C device is 0x3c, enter the following command to read the I2C device

.. code-block:: shell

   ./i2cdump -f -y 4 0x3c

|  Output information is as follows

.. code-block:: shell

   /customer # ./i2cdump -f -y 4 0x3c
   No size specified (using byte-data access)
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
   00: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   10: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   20: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   30: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   40: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   50: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   60: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   70: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   80: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   90: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   a0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   b0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   c0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   d0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   e0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
   f0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB

WiFi
-------

|  **Test Description**: Connect 2.4G antenna to development board WIFI(CON23) interface. Verify network connectivity by sending ICMP packets from the development board to external network.
|  **Interface Label**: u23
|  **System Device**: wlan0
|  **Test Procedure**
|  WiFi Password Modification

.. code-block:: shell

   # 1. Edit configuration file (confirm ssid and psk match hotspot settings)
   vi /customer/wifi/wpa_supplicant.conf
   # Configuration file content (no modification needed, ensure ssid="iQOO", psk="1234567890")
   ctrl_interface=/tmp/wifi/run/wpa_supplicant
   update_config=1
   network={
   ssid="iQOO"//WiFi Name
   psk="1234567890"//WiFi Password
   }

1. Enter the following command to set environment path

.. code-block:: shell

   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/customer/wifi/

2. Enter the following command to enable WiFi

.. code-block:: shell

   ifconfig wlan0 up

|  Output information is as follows, press Enter

.. code-block:: shell

   RTW: ==> rtl8723du_hal_deinit
   RTW: CardDisableRTL8723du(wlan0): bMacPwrCtrlOn=1
   RTW: SetHwReg: bMacPwrCtrlOn=0
   RTW: <=== rtw_ips_pwr_down..................... in 40ms
   Press Enter

3. Enter the following command to create interface directory

.. code-block:: shell

   mkdir -p /tmp/wifi/run

4. Enter the following command to start WiFi service

.. code-block:: shell

   /customer/wifi/wpa_supplicant -Dnl80211 -i wlan0 -c /customer/wifi/wpa_supplicant.conf -d &

|  Output information is as follows, press Enter

.. code-block:: shell

   RTW: WARN Invalid hw_rate 0xff in hw_rate_to_m_rate
   RTW: WARN Invalid hw_rate 0xff in hw_rate_to_m_rate
   EAPOL: startWhen --> 0
   EAPOL: disable timer tick
   RTW: rtw_set_ps_mode(wlan0) Enter 802.11 power save - WIFI-TRAFFIC_IDLE
   RTW: rtl8723d_set_FwPwrMode_cmd(): FW LPS mode = 2, SmartPS=2
   Press Enter

5. Enter the following command to obtain WiFi IP

.. code-block:: shell

   udhcpc -q -i wlan0 -s /etc/init.d/udhcpc.script &

|  Output information is as follows, press Enter

.. code-block:: shell

   Lease of 192.168.112.202 obtained, lease time 3599
   Setting IP address 192.168.112.202 on wlan0
   Deleting routers
   route: SIOCDELRT: No such process
   Adding router 192.168.112.210
   Recreating /customer/resolv.conf
    Adding DNS server 192.168.112.210
   RTW: rtw_set_ps_mode(wlan0) Enter 802.11 power save - WIFI-TRAFFIC_IDLE
   RTW: rtl8723d_set_FwPwrMode_cmd(): FW LPS mode = 2, SmartPS=2
   RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 SeqNum = 5
   Press Enter

5. Enter the following command to verify WiFi connection

.. code-block:: shell

   ping www.baidu.com -c 3

|  Output information is as follows, 0% packet loss indicates normal, press Enter

.. code-block:: shell

   / # ping www.baidu.com -c 3
   PING www.baidu.com (183.2.172.177): 56 data bRTW: rtw_set_ps_mode(wlan0) Leave 802.11 power save - WIFI-LPS_CTRL_LEAVE
   RTW: rtl8723d_set_FwPwrMode_cmd(): FW LPS mode = 0, SmartPS=2
   ytes
   64 bytes from 183.2.172.177: seq=0 ttl=52 time=56.453 ms
   64 bytes from 183.2.172.177: seq=1 ttl=52 time=34.263 ms
   64 bytes from 183.2.172.177: seq=2 ttl=52 time=35.835 ms

   --- www.baidu.com ping statistics ---
   3 packets transmitted, 3 packets received, 0% packet loss
   round-trip min/avg/max = 34.263/42.183/56.453 ms
   / # RTW: rtw_set_ps_mode(wlan0) Enter 802.11 power save - WIFI-TRAFFIC_IDLE
   RTW: rtl8723d_set_FwPwrMode_cmd(): FW LPS mode = 2, SmartPS=2
   RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 SeqNum = 11
   RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 Se

Headphone Test
----------------

|  **Test Description**: Test headphones with audio files
|  **Interface Label**: J3
|  **System Device**:
|  **Test Procedure**:

1. Insert headphones and enter the following command

.. code-block:: shell

   cd customer
   ./prog_audio_ai_ao_demo playback -i dac -f ./sample-9s.wav -a 0 -d 0 -c 2 -t 20 -v 60

2. Both left and right channels of the headphone can play sound normally

SPEAKER*2
------------

|  **Test Description**: Test speakers with audio files
|  **Interface Label**: P1,P2
|  **System Device**:
|  **Test Procedure**:

1. Connect speakers and enter the following command

.. code-block:: shell

   cd customer
   ./prog_audio_ai_ao_demo playback -i dac -f ./sample-9s.wav -a 0 -d 0 -c 2 -t 20 -v 60

2. Both SPK1 and SPK2 can play sound normally

Recording
-----------

|  **Test Description**: Generate recording files and playback for testing
|  **Interface Label**: J3 (Headphone MIC1), MIC0, MIC2
|  **System Device**:
|  **Test Procedure**:

1. Insert headphones and enter the following command

.. code-block:: shell

   cd /customer
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic1.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60

2. Speak to the headphone microphone until recording finishes
3. After recording completes, enter the following command to playback the recorded audio

.. code-block:: shell

   ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic1.wav -a 0 -d 0 -c 2 -t 20 -v 80

4. Connect speaker to SPK1 or insert headphone, speaker outputs sound and headphone right channel outputs sound
5. Connect recording device to MIC0 and enter the following command

.. code-block:: shell

   cd /customer
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic0.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60

6. Speak to the recording device until recording finishes
7. After recording completes, enter the following command to playback the recorded audio

.. code-block:: shell

   ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic0.wav -a 0 -d 0 -c 2 -t 20 -v 80

8. Connect speaker to SPK2 or insert headphone, speaker outputs sound and headphone left channel outputs sound
9. Connect recording device to MIC2 and enter the following command

.. code-block:: shell

   cd /customer
   ./prog_audio_ai_ao_demo capture -i adc_b -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60

10. Speak to the recording device until recording finishes
11. After recording completes, enter the following command to playback the recorded audio

.. code-block:: shell

   ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic2.wav -a 0 -d 0 -c 2 -t 20 -v 80

12. Connect speakers to SPK1/SPK2 or insert headphone, speakers and both headphone channels output sound normally

.. code-block:: shell

   #MIC0
   Recording Test
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic0.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60
   #MIC1
   Recording Test
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60
   #MIC2
   Recording Test
   ./prog_audio_ai_ao_demo capture -i adc_b -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60
   Play Recording
   ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic0.wav -a 0 -d 0 -c 2 -t 20 -v 80
   ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic1.wav -a 0 -d 0 -c 2 -t 20 -v 80
   ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic2.wav -a 0 -d 0 -c 2 -t 20 -v 80

PWM
------

|  **Test Description**: Observe PWM pin waveform with oscilloscope
|  **Interface Label**:
|  **System Device**: sys/class/sstar/pwm/
|  **Test Procedure**:
|  General PWM

1. Enter the following commands to configure pwm3

.. code-block:: shell

   cd sys/class/sstar/pwm/group0
   /sys/devices/virtual/sstar/pwm/group2 # cd pwm3
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 1000000  > period
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 500000   > duty
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo normal   > polarity
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 1        > enable

|  Face the Ethernet port towards you, test the 3rd pin from right below the upper row header with oscilloscope, stable waveform can be observed

1. Enter the following commands to configure pwm6

.. code-block:: shell

   cd sys/class/sstar/pwm/group1
   /sys/devices/virtual/sstar/pwm/group2 # cd pwm6
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 1000000  > period
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 500000   > duty
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo normal   > polarity
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 1        > enable

|  Face the Ethernet port towards you, test the 2nd pin from right below the upper row header with oscilloscope, stable waveform can be observed

2. Enter the following commands to configure pwm7

.. code-block:: shell

   cd sys/class/sstar/pwm/group1
   /sys/devices/virtual/sstar/pwm/group2 # cd pwm7
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 1000000  > period
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 500000   > duty
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo normal   > polarity
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 1        > enable

|  Face the Ethernet port towards you, test the 4th pin from right below the upper row header with oscilloscope, stable waveform can be observed

2. Enter the following commands to configure pwm8

.. code-block:: shell

   cd sys/class/sstar/pwm/group2
   /sys/devices/virtual/sstar/pwm/group2 # cd pwm8
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 1000000  > period
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 500000   > duty
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo normal   > polarity
   /sys/devices/virtual/sstar/pwm/group2/pwm8 # echo 1        > enable

|  Face the Ethernet port towards you, test the 6th pin from right below the upper row header with oscilloscope, stable waveform can be observed

RS232
--------

|  **Test Description**: Perform self-transceiver test by shorting 232_TX1&232_RX1, 232_TX2&232_RX2
|  **Interface Label**: 232_TX1,232_RX1  232_TX2,232_RX2
|  **System Device**: /dev/ttyS4,ttyS5
|  **Test Procedure**:
|  232-1

1. Short 232_TX1 and 232_RX1 with DuPont line
2. Enter test directory and input the following command:

.. code-block:: shell

   cd customer/

3. Run test program with the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS3 12345

|  Output information is as follows:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x31          Character: 1 
   ASCII: 0x32          Character: 2 
   ASCII: 0x33          Character: 3 
   ASCII: 0x34          Character: 4 
   ASCII: 0x35          Character: 5 

|  232-2

1. Short 232_TX2 and 232_RX2 with DuPont line
2. Enter test directory and input the following command:

.. code-block:: shell

   cd customer/

3. Run test program with the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS2 12345

|  Output information is as follows:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x31          Character: 1 
   ASCII: 0x32          Character: 2 
   ASCII: 0x33          Character: 3 
   ASCII: 0x34          Character: 4 
   ASCII: 0x35          Character: 5 

RS485
--------

|  **Test Description**: Transceive test between development board and PC via 485-USB converter
|  **Interface Label**: 485_A1,485_B1,485_A2,485_B2
|  **System Device**: /dev/ttyS1,ttyS8
|  **Test Procedure**:
|  rs485-1

1. Connect development board and PC with 485-USB converter (A to A, B to B)
2. Open corresponding serial port with Xshell, set baud rate to 115200, data bit 8, stop bit 1
3. Enter test directory and input the following command:

.. code-block:: shell

   cd customer/

4. Run test with the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS1 12345

|  Output can be seen in 485 serial terminal

.. code-block:: shell

   Connecting to COM5...
   Connected.

   12345

5. Input 6 in 485 serial terminal (no echo display), 6 can be received on development board terminal

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x36          Character: 6 

|  rs485-2

1. Connect development board and PC with 485-USB converter (A to A, B to B)
2. Open corresponding serial port with Xshell, set baud rate to 115200, data bit 8, stop bit 1
3. Enter test directory and input the following command:

.. code-block:: shell

   cd /customer/

4. Run test with the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS8 12345

|  Output can be seen in 485 serial terminal

.. code-block:: shell

   Connecting to COM5...
   Connected.

   12345

5. Input 6 in 485 serial terminal (no echo display), 6 can be received on development board terminal

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x36          Character: 6 

UART
------

|  **Test Description**: Perform self-transceiver test by shorting related pins
|  **Interface Label**:
|  **System Device**: /dev/ttyS4,ttyS5,ttyS7
|  **Test Procedure**:
|  uart4

1. Short RX4_3 and TX4_3 pins for self-transceiver test
2. Enter test directory and input the following command:

.. code-block:: shell

   cd /customer/

3. Run test with the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS4 12345

|  Output information is as follows:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x31          Character: 1 
   ASCII: 0x32          Character: 2 
   ASCII: 0x33          Character: 3 
   ASCII: 0x34          Character: 4 
   ASCII: 0x35          Character: 5 

|  uart5

1. Short TX5_1 and RX5_1 (up and down of -10) pins for self-transceiver test
2. Enter test directory and input the following command:

.. code-block:: shell

   cd customer/

3. Run test with the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS5 12345

|  Output information is as follows:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x31          Character: 1 
   ASCII: 0x32          Character: 2 
   ASCII: 0x33          Character: 3 
   ASCII: 0x34          Character: 4 
   ASCII: 0x35          Character: 5 

|  uart7

1. Short RX7_3 and TX7_3 pins for self-transceiver test
2. Enter test directory and input the following command:

.. code-block:: shell

   cd /customer/

3. Run test with the following command:

.. code-block:: shell

   ./serial_test.out /dev/ttyS7 12345

|  Output information is as follows:

.. code-block:: shell

   Starting send data...finish
   Starting receive data:
   ASCII: 0x31          Character: 1 
   ASCII: 0x32          Character: 2 
   ASCII: 0x33          Character: 3 
   ASCII: 0x34          Character: 4 
   ASCII: 0x35          Character: 5 


4G
-----

|  **Test Description**: Connect the 2.4G antenna to the EC20 4G module interface. The development board sends ICMP packets to the external network to verify normal network connectivity.
|  **Interface Label**: CON6
|  **System Device**: usb0
|  **Test Procedure**

1. Go to the test application path and enter the following command

.. code-block:: shell

   cd customer/

2. Enter the following command to start 4G network

.. code-block:: shell

   ./4g

**Output information is as follows**

.. code-block:: shell

   /customer # ./4g
   Starting 4G network...
   udhcpc (v1.20.2) started
   Sending discover...
   Sending select for 192.168.225.59...
   Lease of 192.168.225.59 obtained, lease time 43200
   4G network started successfully!
   Current usb0 interface information:
   usb0      Link encap:Ethernet  HWaddr 3A:87:28:7B:48:CE  
             inet addr:192.168.225.59  Bcast:192.168.225.255  Mask:255.255.255.0
             UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
             RX packets:2 errors:0 dropped:0 overruns:0 frame:0
             TX packets:2 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000 
             RX bytes:674 (674.0 B)  TX bytes:656 (656.0 B)


   Resolving IP of www.baidu.com (max 3 retries)...
   1st attempt (ping) to resolve www.baidu.com...
   2nd attempt (ping) to resolve www.baidu.com...
   3rd attempt (ping) to resolve www.baidu.com...

   Ping resolution failed, trying nslookup for resolution...
   Resolution succeeded (nslookup): IP of www.baidu.com is 183.2.172.177

   Routing information:

|  As shown in the above log, the IP address of www.baidu.com is 183.2.172.177. Enter the following command to ping Baidu

.. code-block:: shell

   ping 183.2.172.177

**Output information is as follows; 0% packet loss indicates normal status**

.. code-block:: shell

   /customer # ping 183.2.172.177
   PING 183.2.172.177 (183.2.172.177): 56 data bytes
   64 bytes from 183.2.172.177: seq=0 ttl=52 time=37.138 ms
   64 bytes from 183.2.172.177: seq=1 ttl=52 time=71.735 ms
   64 bytes from 183.2.172.177: seq=2 ttl=52 time=76.311 ms
   64 bytes from 183.2.172.177: seq=3 ttl=52 time=69.584 ms
   64 bytes from 183.2.172.177: seq=4 ttl=52 time=65.987 ms
   64 bytes from 183.2.172.177: seq=5 ttl=52 time=61.267 ms
   ^C
   --- 183.2.172.177 ping statistics ---
   6 packets transmitted, 6 packets received, 0% packet loss

Bluetooth
------------

|  **Test Description**: Connect the 2.4G antenna to the U23 Bluetooth & Wi-Fi module interface. The development board sends ICMP packets to the external network to verify normal connectivity.
|  **Interface Label**: U23
|  **System Device**: hci0
|  **Test Procedure**

1. Enter the following command to enable Bluetooth

.. code-block:: shell

   hciconfig hci0 up

**Output information is as follows**

.. code-block:: shell

   rtk_btusb: btusb_open hdev->promisc ==0

2. Enter the following command to scan Bluetooth devices (enable Bluetooth on your mobile phone first)

.. code-block:: shell

   hcitool scan

**Output information is as follows**

.. code-block:: shell

   Scanning ...
           DC:0D:30:5C:4C:93        n/a
           A8:13:06:20:06:54        iQOO Neo5
           A8:E5:44:99:28:F8        n/a

3. The Bluetooth MAC address of the test mobile phone is A8:13:06:20:06:54 (device name: iQOO Neo5). Enter the following command to establish Bluetooth connection

.. code-block:: shell

   l2ping A8:13:06:20:06:54

**Output information is as follows; 0% loss indicates test passed**

.. code-block:: shell

   / # l2ping A8:13:06:20:06:54
   Ping: A8:13:06:20:06:54 from 94:BA:06:78:1C:E7 (data size 44) ...
   44 bytes from A8:13:06:20:06:54 id 0 time 5.01ms
   44 bytes from A8:13:06:20:06:54 id 1 time 88.41ms
   ^C2 sent, 2 received, 0% loss

MIPI
------

|  Connect the adapter board and cables properly. The test is normal if the logo is displayed after power-on.

Camera
--------

|  **Test Description**: Connect the MIPI screen and camera module properly to verify camera function.
|  **Interface Label**: U19
|  **System Device**:
|  **Test Procedure**:

1. Enter the following command to enable the camera

.. code-block:: shell

   cd customer
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/customer/3rd_party_libs/ffmpeg/lib
   ./prog_disp_sensor2Panel_demo -c 1 -n 0 -p 1 -t 0 -r 90 -d 1 -m model/yolov8n_800x480_P3P_fixed.sim_sgsimg.img -f font/default.ttf

2. The test is normal if the camera preview image is displayed on the MIPI screen.

Touch
--------

|  **Test Description**: Touch the MIPI screen to verify touch function performance.
|  **Interface Label**: CON5 DSI
|  **System Device**: /dev/input/event5
|  **Test Procedure**:

1. Connect the MIPI screen to the development board, then run the following command to enable touch event monitoring

.. code-block:: shell

   cd /customer
   ./my-evtest5

2. After execution, coordinate information will be output when touching the screen, as shown below

.. code-block:: shell

   /customer # ./my-evtest5
   === My EVTest - Touch Screen Debug Tool ===
   Input device ID: bus 0x0018 vendor 0x0000 product 0x0000 version 0x0000
   Input device name: "sitronix_ts_i2c"
   Selected device: /dev/input/event5
   Testing ... (interrupt to exit)

   Event: time 49.628822, type 3 (EV_ABS), code 57 (ABS_MT_TRACKING_ID), value 0
   Event: time 49.629267, type 3 (EV_ABS), code 53 (ABS_MT_POSITION_X), value 132 (X=132)
   Event: time 49.629292, type 3 (EV_ABS), code 54 (ABS_MT_POSITION_Y), value 451 (Y=451)
   Event: time 49.629315, type 3 (EV_ABS), code 48 (UNKNOWN), value 1
   Event: time 49.629336, type 3 (EV_ABS), code 58 (UNKNOWN), value 255
   Event: time 49.629363, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 1 (PRESS)
   Event: time 49.629386, type 0 (EV_SYN), code 0 (UNKNOWN), value 0
   Event: time 49.687312, type 3 (EV_ABS), code 53 (ABS_MT_POSITION_X), value 134 (X=134)
   Event: time 49.687353, type 0 (EV_SYN), code 0 (UNKNOWN), value 0
