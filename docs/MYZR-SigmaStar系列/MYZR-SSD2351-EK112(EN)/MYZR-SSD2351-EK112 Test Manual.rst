MYZR-SSD2351-EK112 Test Manual
==================================

UART Test
~~~~~~~~~~~

UART4 Configuration and Testing
----------------------------------

|  【Test instructions】: Short connect the J4:3 (UART4_RX) pin and the J4:5 (UART4_TX) pin.
|  【Interface ID】: J4
|  【System equipment】: /dev/ttyS4
|  【Interface Silk Printing】: UART4_TX and UART4_RX

.. code-block:: shell

   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS4 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x2e      Character: . 
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6f      Character: o 
   ASCII: 0x6d      Character: m 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6e      Character: n 
   ASCII: 0x0      Character:  

UART3 Configuration and Testing
-----------------------------------

.. code-block:: shell

   #Configuration (disabled by default, configured as MIPI interface, if you want to use it, you need to turn on the configuration, block)
   $ vim arch/arm/boot/dts/pcupid-ssm001c-s01a-voip-padmux.dtsi

|  #Increase (need to shield to PAD_OUTP_CH0 and PAD_OUTN_CH0 other pin configurations)
|                   //UART3 Mode2
|                   <PAD_OUTP_CH0            PINMUX_FOR_FUART3_2W_MODE_2        MDRV_PUSE_UART3_TX>,
|                   <PAD_OUTN_CH0            PINMUX_FOR_FUART3_2W_MODE_2        MDRV_PUSE_UART3_RX>,

|  【Test instructions】: Short connect the J19:5 (MIPITX_D0P) pin and the J19:6 (MIPITX_D0M) pin.
|  【Interface ID】: J19
|  【System equipment】: /dev/ttyS3
|  【Interface Silk Printing】: MIPITX_D0M and MIPITX_D0P

.. code-block:: shell

   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS3 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x2e      Character: . 
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6f      Character: o 
   ASCII: 0x6d      Character: m 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6e      Character: n 
   ASCII: 0x0      Character:


UART2 Configuration and Testing
-----------------------------------

|  【Test instructions】: Short connect the J4:7 (FUART2_RX) pin and the J4:8 (FUART2_TX) pin.
|  【Interface ID】: J4
|  【System equipment】: /dev/ttyS2
|  【Interface Silk Printing】: FUART2_TX and FUART2_RX

.. code-block:: shell

   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS2 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x2e      Character: . 
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6f      Character: o 
   ASCII: 0x6d      Character: m 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6e      Character: n 
   ASCII: 0x0      Character:  


UART1 Configuration and Testing
-----------------------------------

|  【Test instructions】: Short connect the J4:9 (FUART1_RX) pin and the J4:10 (FUART1_TX) pin.
|  【Interface ID】: J4
|  【System equipment】: /dev/ttyS1
|  【Interface Silk Printing】: FUART1_TX and FUART1_RX

.. code-block:: shell

   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS1 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x2e      Character: . 
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6f      Character: o 
   ASCII: 0x6d      Character: m 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6e      Character: n 
   ASCII: 0x0      Character:  

UART5 Configuration and Testing
----------------------------------

|  【Test instructions】: Short connect the J18:1 (UART5_TX) pin and the J18:2 (UART5_RX) pin.
|  【Interface Identification】: J18
|  【System equipment】: /dev/ttyS5
|  【Interface Silk Screen】: UART5_TX and UART5_RX

.. code-block:: shell

   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS5 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x2e      Character: . 
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6f      Character: o 
   ASCII: 0x6d      Character: m 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6e      Character: n 
   ASCII: 0x0      Character:  

UART6 Configuration and Testing
----------------------------------

|  【Test instructions】: Short connect the J4:35 (UART0_TX) pin and the J4:38 (UART0_RX) pin.
|  【Interface ID】: J4
|  【System equipment】: /dev/ttyS5
|  【Interface Silk Printing】: UART0_TX and UART0_RX

.. code-block:: shell

   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS6 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x2e      Character: . 
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6f      Character: o 
   ASCII: 0x6d      Character: m 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6e      Character: n 
   ASCII: 0x0      Character:  

UART7 Configuration and Testing
----------------------------------

|  【Test instructions】: Short connect the J4:37 (UART7_TX) pin and the J4:40 (UART7_RX) pin.
|  【Interface ID】: J4
|  【System equipment】: /dev/ttyS7
|  【Interface Silk Printing】: UART7_TX and UART7_RX

.. code-block:: shell

   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS7 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x77      Character: w 
   ASCII: 0x2e      Character: . 
   ASCII: 0x6d      Character: m 
   ASCII: 0x79      Character: y 
   ASCII: 0x7a      Character: z 
   ASCII: 0x72      Character: r 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6f      Character: o 
   ASCII: 0x6d      Character: m 
   ASCII: 0x2e      Character: . 
   ASCII: 0x63      Character: c 
   ASCII: 0x6e      Character: n 
   ASCII: 0x0      Character:  

I2C2 Configuration and Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instructions】: Connect the J19:11 (I2C2_SDA) pin and J19:13 (I2C2_SCL) to the hym8563 module module, as well as the power supply and ground. i2c2 is connected to the RTC clock module of hym8563, 0x51 is the setting address of hym8563, if the module does not exist, an error will be reported. Normal reminder.
|  【Interface ID】: J19
|  【System Equipment】: /dev/i2c2
|  【Interface silk screen】：I2C2_SDA和I2C2_SCL

.. code-block:: shell

   #1.i2ctool test
   $ cd /customer/app/
   $ ./i2cdump -f -y 2 0x51
   Output information:
   No size specified (using byte-data access)
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
   00: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   10: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   20: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   30: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   40: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   50: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   60: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   70: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   80: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   90: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   a0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   b0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   c0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   d0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   e0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.
   f0: 80 00 47 04 00 01 00 01 00 80 80 81 80 80 03 00    ?.G?.?.?.??????.

   #2. Test the HYM8563 real-time clock
   #Device interface: /dev/rct1
   #Test Instructions: Detect and set the clock
   $ dmesg | grep rtc
   #Output information:
   sstar,rtcpwc 1f006800.rtcpwc: registered as rtc0
   sstar,rtcpwc 1f006800.rtcpwc: setting system clock to 1970-01-01T04:41:54 UTC (16914)
   input: rtcpwc as /devices/soc0/soc/1f006800.rtcpwc/input/input0
   rtc-hym8563 2-0051: registered as rtc1

   #Test the HYM8563 clock
   #a. Set the system clock2025-03-01 12:34:19
   $ date 
   Thu Jan  1 04:59:47 UTC 1970
   $ date -s "2025-03-01 12:34:19"
   Sat Mar  1 12:34:19 UTC 2025
   #b. Write the system clock to the hardware clock
   $ hwclock -w -f /dev/rtc1
   #c. Whether the hardware clock is read correctly
   $ hwclock -r -f /dev/rtc1
   Sat Mar  1 12:35:07 2025  0.000000 seconds

SPI0 Configuration and Testing 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test instructions】: Short connect the J18:16 (MSPI0_MISO) pin and the J18:17 (MSPI0_MOSI) pin.
|  【Interface identification】：J18
|  【System Equipment】：/dev/spidev0.0
|  【Interface silk screen】：MSPI0_MISO和MSPI0_MOSI

.. code-block:: shell

   $ cd /customer/app/
   $ /customer/tools # ./spidev_test.out -D /dev/spidev0.0 
   #Output information
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
   Note: If there is no short connection, output the following information:
   spi mode: 0
   bits per word: 8
   max speed: 500000 Hz (500 KHz)

   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 00 00 00 00 
   00 00 

PWM Configuration and Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test Instructions】: Pull the PWM pin down (0V) or up (1.8V).
|  【Interface identification】：J18,J4
|  【System Equipment】：/sys/class/sstar/pwm
|  【Interface silk screen】：PM_PWM0_OUT和PM_PWM1_OUT和EMMC_D4和EMMC_D5和EMMC_D6

.. code-block:: shell

   # Device interface: # PAD_PM_PWM0_OUT: Corresponding device node /sys/class/sstar/pwm/pwm18
   # PAD_PM_PWM1_OUT: Corresponding device nodes/sys/class/sstar/pwm/pwm19
   # PAD_EMMC_D4: The corresponding device node /sys/class/sstar/pwm/group3/pwm14
   # PAD_EMMC_D5: Corresponding device node /sys/class/sstar/pwm/group3/pwm15
   # PAD_EMMC_D6: The corresponding device node /sys/class/sstar/pwm/group3/pwm16
   # Test description: Check with an oscilloscope, take J18:7 (EMMC_D4) as an example to output a waveform of 100HZ, 50% duty cycle, and normal polarity
   $ cd /sys/class/sstar/pwm/group3/pwm14
   $ echo 1000000  > period
   $ echo 500000   > duty
   $ echo normal   > polarity
   $ echo 1        > enable


GPIO Configuration and Testing 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+------------+-------------+------------+-------------+------------+
|   Pad Name   | GPIO Index |  Pad Name   | GPIO Index |  Pad Name   | GPIO Index |
+==============+============+=============+============+=============+============+
| PAD_EMMC_CMD | 52         | PAD_EMMC_D5 | 57         | PAD_EMMC_D3 | 54         |
+--------------+------------+-------------+------------+-------------+------------+
| PAD_EMMC_D0  | 56         | PAD_EMMC_D1 | 58         |             |            |
+--------------+------------+-------------+------------+-------------+------------+

|  【Test Instructions】：Pull the GPIO pin down or up.
|  【Interface identification】：J18
|  【System Equipment】：/sys/class/gpio
|  【Interface silk screen】：EMMC_CMD和EMMC_D5和EMMC_D3和EMMC_D0和EMMC_D1

.. code-block:: shell

   # Test description: Take J18:10 (EMMC_D1) as an example
   # Set the high and low levels
   $ echo 68 > /sys/class/gpio/export 
   $ echo out > /sys/class/gpio/gpio58/direction 
   $ echo 1 > /sys/class/gpio/gpio58/value 
   $ echo 0 > /sys/class/gpio/gpio58/value 
   # Read the pin level
   $ echo in > /sys/class/gpio/gpio58/direction 
   $ cat /sys/class/gpio/gpio58/value

TF Card Test
~~~~~~~~~~~~~~

|  【Test Instructions】：插入TF卡。
|  【Interface identification】：J12
|  【System Equipment】：/dev/mmcblk0
|  【Interface silk screen】：J12

.. code-block:: shell

   #The prompt message is as follows:
   SDMMC0 >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] HS mode. <<
   #View partitions:
   $ ls /dev/mmcblk0*
   #Output information:
   /dev/mmcblk0    /dev/mmcblk0p1  /dev/mmcblk0p2
   #mount
   $ mount /dev/mmcblk0p1 /mnt/
   $ ls /mnt/
   imx6ul~1.dtb  imx6ul~3.dtb  imx6ul~5.dtb  imx6ul~7.dtb  zimage
   imx6ul~2.dtb  imx6ul~4.dtb  imx6ul~6.dtb  system~1
   #unload
   $ umount /mnt/

USB Flash Drive Test
~~~~~~~~~~~~~~~~~~~~~~

|  【Test Instructions】：插入u盘。
|  【Interface identification】：J16
|  【System Equipment】：/dev/sd*
|  【Interface silk screen】：J16

.. code-block:: shell

   $ dmesg | grep sd
   #The prompt message is as follows:
   sd 0:0:0:0: [sda] 61440000 512-byte logical blocks: (31.5 GB/29.3 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
   sd 0:0:0:0: [sda] No Caching mode page found
   sd 0:0:0:0: [sda] Assuming drive cache: write through
    sda: sda1
   sd 0:0:0:0: [sda] Attached SCSI removable disk

   #View partitions:
   $ ls /dev/sd*
   #Output information:
   /dev/sda   /dev/sda1
   #mount
   $ mount /dev/sda1 /mnt/
   $ ls /mnt/
   imx6ul~1.dtb  imx6ul~3.dtb  imx6ul~5.dtb  imx6ul~7.dtb  zimage
   imx6ul~2.dtb  imx6ul~4.dtb  imx6ul~6.dtb  system~1
   #unload
   $ umount /mnt/

Ethernet Test 
~~~~~~~~~~~~~~~

|  【Test Instructions】：The computer is set to 192.168.137.99 and the board is set to 192.168.137.81, and it passes the ping test.
|  【Interface identification】：CONR1
|  【System Equipment】：/dev/eth0
|  【Interface silk screen】：CONR1

.. code-block:: shell

   $ ifconfig eth0 192.168.137.81
   #Output information:
   [emac_phy_link_adjust] EMAC Link Down 
   [emac_phy_link_adjust] EMAC Link Up
   #Test normal if there is no packet loss.
   $ ping 192.168.137.99 -c 2 -w 4
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=64 time=0.537 ms
   64 bytes from 192.168.137.99: seq=1 ttl=64 time=0.276 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.276/0.406/0.537 ms

WIFI Test
~~~~~~~~~~~

|  【Test Instructions】：After the WIFI is connected to the AP, the board sends ICMP packets to the external network to verify that the connection is normal.
|  【Interface identification】：WIFI&BT
|  【System Equipment】：wlan0
|  【Interface silk screen】：U12

.. code-block:: shell

|  Test operations

1. Connect the antenna to the "U12" port
2. Generate a WPA PSK file for the SSID

|  wpa_passphrase Command format：wpa_passphrase + wifi name + wifi keyword > /etc/wpa_supplicant.conf

.. code-block:: shell

   =====> Input:
   wpa_passphrase MYZR-WIFI-2.4G myzr2012 > /etc/wpa_supplicant.conf

3. Connect:

.. code-block:: shell

   =====> Input:
   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf 

   =====> Output:
   Successfully initialized wpa_supplicant
   nl80211: kernel reports: Match already configured
   rfkill: Cannot open RFKILL control device
   ......

4. Get IP:

.. code-block:: shell

   =====> Input:
   $ udhcpc -i wlan0

   =====> Output:
   udhcpc: started, v1.37.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.43.74, server 192.168.43.1
   udhcpc: lease of 192.168.43.74 obtained from 192.168.43.1, lease time 3600
   deleting routers
   adding dns 192.168.43.1

5. Test Connections:

.. code-block:: shell

   =====> Input:
   $ ping -I wlan0 www.baidu.com

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
   22 packets transmitted, 22 packets received, 0% packet loss
   round-trip min/avg/max = 17.336/38.637/123.220 ms

|  "0% packet loss" indicates that the wifi connection is fine.

WIFI AP Test
---------------

|  【Test Instructions】：After the WIFI is connected to the AP, the board sends ICMP packets to the external network to verify that the connection is normal.
|  【Interface identification】：WIFI&BT
|  【System Equipment】：wlan0
|  【Interface silk screen】：U12

1. Create hotspots

.. code-block:: shell

   $ /etc/hostapd.conf ssid to MYZR-SSD2351-EK112 and interface to wlan1
   $ ifconfig wlan1 192.168.8.1
   $ hostapd -B /etc/hostapd.conf
   $ dnsmasq --interface=wlan1 --dhcp-range=192.168.8.2,192.168.8.100,24h
   # The phone can recognize the MYZR-SSD2351-EK112

2. Enable IP forwarding and NAT

.. code-block:: shell

   $ echo 1 > /proc/sys/net/ipv4/ip_forward
   $ iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE

Bluetooth test
----------------

|  【Test Instructions】：After scanning to a Bluetooth device, send an L2CAP response request and receive a response
|  【Interface identification】：WIFI&BT
|  【System Equipment】：hci0
|  【Interface silk screen】：U12

|  Test operations

1. Connect the antenna to the "U12" port
2. Start Bluetooth:

.. code-block:: shell

   =====> Input:
   $ hciconfig hci0 up
   $ hciconfig 

   =====> Output:
   hci0:   Type: Primary  Bus: UART
       BD Address: B0:F1:EC:A7:E8:03  ACL MTU: 1021:8  SCO MTU: 64:1
       UP RUNNING 
       RX bytes:1266 acl:0 sco:0 events:66 errors:0
       TX bytes:1138 acl:0 sco:0 commands:66 errors:0

3. Scan for external Bluetooth devices:

.. code-block:: shell

   =====> Input:
   $ hcitool scan

   =====> Output:
   Scanning ...
       88:46:04:4C:11:A7   Redmi K40

4. Sending the L2CAP package test:

.. code-block:: shell

   =====> Input:
   $ l2ping 88:46:04:4C:11:A7

   =====> Output:
   Ping: 88:46:04:4C:11:A7 from B0:F1:EC:A7:E8:03 (data size 44) ...
   44 bytes from 88:46:04:4C:11:A7 id 0 time 44.84ms
   44 bytes from 88:46:04:4C:11:A7 id 1 time 28.58ms
   44 bytes from 88:46:04:4C:11:A7 id 2 time 46.05ms
   44 bytes from 88:46:04:4C:11:A7 id 3 time 44.86ms
   44 bytes from 88:46:04:4C:11:A7 id 4 time 44.67ms
   ^C8 sent, 8 received, 0% loss

|  "0% packet loss" means the Bluetooth connection is fine.
|  Connecting to Bluetooth can be done with the command bluetoothctl

.. code-block:: shell

   #Enter the terminal;
   [bluetooth]#
   [bluetooth]# show //See if the controller\'s Power is yes, and if Power is no, run Power On
   [bluetooth]# power on
   [bluetooth]# agent NoInputNoOutput //Other IO caps can be set, such as KeyboardDisplay
   [bluetooth]# default-agent
   [bluetooth]# scan on //After scanning the corresponding device, use Scan Off to turn off the scan.
   [bluetooth]# pair 00:22:48:DC:89:0F //Pair the remote device.
   [bluetooth]# connect 00:22:48:DC:89:0F //Connect remote devices

MIC Test
-----------

.. code-block:: shell

   #MIC0 recording test
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic1.wav -A 0 -D 0 -R 8000 -C 1 -T 10 -V 60
   #MIC1 recording test
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60
   #MIC2 recording test
   ./prog_audio_ai_ao_demo capture -i adc_b -F test_amic3.wav -A 0 -D 0 -R 8000 -C 1 -T 10 -V 60
