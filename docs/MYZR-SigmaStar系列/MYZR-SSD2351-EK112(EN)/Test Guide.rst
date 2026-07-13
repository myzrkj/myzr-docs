
.. raw:: html

   <style>
   h1 {
       color: #4CAF50;  /* Heading level 1 font color */
   }
   </style>


Test Guide
=====================
Note: The following applies to ubifs version systems

UART Test
-----------

**UART1 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS1
   #Test description: Short pin J4:9(OUTP_RX0_CH0_FUART1_RX) and pin J4:10(OUTN_RX0_CH0_FUART1_TX).
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
   ASCII: 0x0       Character:

**UART2 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS2
   #Test description: Short pin J4:7(OUTP_RX0_CH2_FUART2_RX) and pin J19:8(OUTN_RX0_CH2_FUART2_TX).
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
   ASCII: 0x0       Character:

**UART3 Configuration and Test**

.. code-block:: shell

   #Configuration (disabled by default, configured as MIPI interface. If needed, enable the configuration and uncomment)
   $ vim arch/arm/boot/dts/pcupid-ssm001c-s01a-voip-padmux.dtsi
   
   #Add (need to mask out other pin configurations of PAD_OUTP_CH0 and PAD_OUTN_CH0)
   //UART3 Mode2
   <PAD_OUTP_CH0  MDRV_PUSE_UART3_TX>,
   <PAD_OUTN_CH0  MDRV_PUSE_UART3_RX>,
   
   #Device interface: /dev/ttyS3
   #Test description: Short pin J19:5(OUTP_TX0_CH0_MIPITX_D0P) and pin J19:6(OUTN_TX0_CH0_MIPITX_D0N).
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS3 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x2e    Character: .
   ASCII: 0x6d    Character: m
   ASCII: 0x79    Character: y
   ASCII: 0x7a    Character: z
   ASCII: 0x72    Character: r
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6f    Character: o
   ASCII: 0x6d    Character: m
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6e    Character: n
   ASCII: 0x0     Character:

**UART4 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS1
   #Test description: Short pin J4:9(OUTP_RX0_CH0_FUART1_RX) and pin J4:10(OUTN_RX0_CH0_FUART1_TX).
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
   ASCII: 0x0       Character:

**UART5 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS5
   #Test description: Short pin J18:1(GPIOE_07_UART5_TX) and pin J18:2(GPIOE_06_UART5_RX).
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS5 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x2e    Character: .
   ASCII: 0x6d    Character: m
   ASCII: 0x79    Character: y
   ASCII: 0x7a    Character: z
   ASCII: 0x72    Character: r
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6f    Character: o
   ASCII: 0x6d    Character: m
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6e    Character: n
   ASCII: 0x0     Character:

**UART6 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS6
   #Test description: Short pin J4:35(UART0_TX) and pin J4:38(UART0_RX).
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS6 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x2e    Character: .
   ASCII: 0x6d    Character: m
   ASCII: 0x79    Character: y
   ASCII: 0x7a    Character: z
   ASCII: 0x72    Character: r
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6f    Character: o
   ASCII: 0x6d    Character: m
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6e    Character: n
   ASCII: 0x0     Character:

**UART7 Configuration and Test**

.. code-block:: shell

   #Device interface: /dev/ttyS7
   #Test description: Short pin J4:37(ADC_PWM_OUT01_UART7_TX) and pin J4:40(ADC_PWM_OUT00_UART7_RX).
   $ cd /customer/app/
   $ ./serial_test.out /dev/ttyS7 "www.myzr.com.cn"
   Starting send data...finish
   Starting receive data:
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x77    Character: w
   ASCII: 0x2e    Character: .
   ASCII: 0x6d    Character: m
   ASCII: 0x79    Character: y
   ASCII: 0x7a    Character: z
   ASCII: 0x72    Character: r
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6f    Character: o
   ASCII: 0x6d    Character: m
   ASCII: 0x2e    Character: .
   ASCII: 0x63    Character: c
   ASCII: 0x6e    Character: n
   ASCII: 0x0     Character:
   
I2C2 Configuration and Test
-----------
.. code-block:: shell

   #1.i2ctool test
   #Device interface: /dev/i2c2
   #Test description: Connect the hym8563 module to pin J19:11(GPIOE_10_I2C2_SDA) and pin J19:13(GPIOE_09_I2C2_SCL), plus power and ground. i2c2 is connected to the hym8563 RTC clock module, 0x51 is the hym8563 device address. If the module is not present, an error will be reported. Normal output is as follows:
   $ cd /customer/app/
   $ ./i2cdump -f -y 2 0x51
   
   #Output:
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
   
   #2.Test hym8563 real-time clock
   #Device interface: /dev/rtc1
   #Test description: Detect and set the clock
   $ dmesg | grep rtc
   
   #Output:
   sstar,rtcpwc 1f006800.rtcpwc: registered as rtc0
   sstar,rtcpwc 1f006800.rtcpwc: setting system clock to 1970-01-01T04:41:54 UTC
   (16914)
   input: rtcpwc as /devices/soc0/soc/1f006800.rtcpwc/input/input0
   rtc-hym8563 2-0051: registered as rtc1
   
   #Test hym8563 clock
   #a.Set system clock to 2025-03-01 12:34:19
   $ date
   Thu Jan  1 04:59:47 UTC 1970
   $ date -s "2025-03-01 12:34:19"
   Sat Mar  1 12:34:19 UTC 2025
   
   #b.Write system clock to hardware clock
   $ hwclock -w -f /dev/rtc1
   
   #c.Read hardware clock to verify correctness
   $ hwclock -r -f /dev/rtc1
   Sat Mar  1 12:35:07 2025  0.000000 seconds

SPI0 Configuration and Test
-----------
.. code-block:: shell

   #Device interface: /dev/spidev0.0
   #Test description: Short pin J18:16(GPIOA_15_MSPI0_MISO) and pin J18:17(GPIOA_14_MSPI0_MOSI).
   $ cd /customer/app/
   $ /customer/tools # ./spidev_test.out -D /dev/spidev0.0
   
   #Output
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
   
   #Note: If not shorted, the following output is shown:
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
PWM Configuration and Test
-----------
**Interface Silkscreen**: PM_PWM0_OUT, PM_PWM1_OUT, EMMC_D4, EMMC_D5, EMMC_D6

.. code-block:: shell

   #Device interface: # PAD_PM_PWM0_OUT: corresponds to device node /sys/class/sstar/pwm/pwm18
   # PAD_PM_PWM1_OUT: corresponds to device node /sys/class/sstar/pwm/pwm19
   # PAD_EMMC_D4: corresponds to device node /sys/class/sstar/pwm/group3/pwm14
   # PAD_EMMC_D5: corresponds to device node /sys/class/sstar/pwm/group3/pwm15
   # PAD_EMMC_D6: corresponds to device node /sys/class/sstar/pwm/group3/pwm16
   #Test description: Check with an oscilloscope. Take J18:7(EMMC_D4_PWM_OUT[14]) as an example, output 100Hz, 50% duty cycle, normal polarity waveform
   $ cd /sys/class/sstar/pwm/group3/pwm14
   $ echo 1000000  > period
   $ echo 500000   > duty
   $ echo normal   > polarity
   $ echo 1        > enable
GPIO Configuration and Test
-----------
**Interface Silkscreen**: EMMC_CMD, EMMC_D5, EMMC_D3, EMMC_D0, EMMC_D1

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;  /* Header centered */
   }
     td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;  /* First row content centered */
   }

   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Unified width */
       border-collapse: collapse;
       table-layout: auto;  /* Column width auto-distributed */
   }
   td {
       word-wrap: break-word;  /* Auto-wrap long content */
   }
   </style>


=============  ===========  =============  ===========  =============  ===========
Pad Name       GPIO Index   Pad Name       GPIO Index   Pad Name       GPIO Index
=============  ===========  =============  ===========  =============  ===========
PAD_EMMC_CMD   52           PAD_EMMC_D5    57           PAD_EMMC_D3    54
PAD_EMMC_D0    56           PAD_EMMC_D1    58
=============  ===========  =============  ===========  =============  ===========
.. code-block:: shell

   #Device interface: /sys/class/gpio
   #Test description: Take J18:10(EMMC_D1_GPIO) as an example
   #Set high and low level
   $ echo 68 > /sys/class/gpio/export
   $ echo out > /sys/class/gpio/gpio58/direction
   $ echo 1 > /sys/class/gpio/gpio58/value
   $ echo 0 > /sys/class/gpio/gpio58/value
   
   #Read pin level
   $ echo in > /sys/class/gpio/gpio58/direction
   $ cat /sys/class/gpio/gpio58/value
TF Card Test
-----------
**Interface Silkscreen**: J12

.. code-block:: shell

   #Device interface: /dev/mmcblk0
   #Test description: Insert TF card
   #Prompt message as follows:
   SDMMC0 >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] HS mode. <<
   
   #Check partitions:
   $ ls /dev/mmcblk0*
   
   #Output:
   /dev/mmcblk0   /dev/mmcblk0p1   /dev/mmcblk0p2
   
   #Mount
   $ mount  /dev/mmcblk0p1  /mnt/
   $ ls /mnt/
   imx6ul~1.dtb   imx6ul~3.dtb    imx6ul~5.dtb    imx6ul~7.dtb    zimage
   imx6ul~2.dtb   imx6ul~4.dtb    imx6ul~6.dtb    system~1
   
   #Unmount
   $ umount /mnt/
USB Flash Drive Test
-----------
**Interface Silkscreen**: J16

.. code-block:: shell

   #Device interface: /dev/sd*
   #Test description: Insert USB flash drive
   $ dmesg | grep sd
   
   #Prompt message as follows:
   sd 0:0:0:0: [sda] 61440000 512-byte logical blocks: (31.5 GB/29.3 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
   sd 0:0:0:0: [sda] No Caching mode page found
   sd 0:0:0:0: [sda] Assuming drive cache: write through
   sda: sda1
   sd 0:0:0:0: [sda] Attached SCSI removable disk
   
   #Check partitions:
   $ ls /dev/sd*
   
   #Output:
   /dev/sda   /dev/sda1
   
   #Mount
   $ mount /dev/sda1 /mnt/
   $ ls /mnt/
   imx6ul~1.dtb  imx6ul~3.dtb  imx6ul~5.dtb  imx6ul~7.dtb  zimage
   imx6ul~2.dtb  imx6ul~4.dtb  imx6ul~6.dtb  system~1
   
   #Unmount
   $ umount /mnt/
Ethernet Test
-----------
**Interface Silkscreen**: CONR1

.. code-block:: shell

   #Device interface: /dev/eth0
   #Test description: Set computer IP to 192.168.137.99, set board IP to 192.168.137.81, test via ping
   $ ifconfig eth0 192.168.137.81
   
   #Output:
   [emac_phy_link_adjust] EMAC Link Down
   [emac_phy_link_adjust] EMAC Link Up
   
   #Test: If no packet loss, it is normal.
   $ ping 192.168.137.99 -c 2 -w 4
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=64 time=0.537 ms
   64 bytes from 192.168.137.99: seq=1 ttl=64 time=0.276 ms
   
   --- 192.168.137.99 ping statistics --
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.276/0.406/0.537 ms
WIFI STA Test
-----------
**Interface Silkscreen**: U12

.. code-block:: shell

   [Test Description]: After WIFI connects to the AP, the development board sends ICMP packets to the external network to verify the connection is normal.
   [Interface Label]: WIFI&BT
   [System Device]: wlan0
   [Interface Silkscreen]: U12
   
   Test Operations
   Connect the antenna to the "U12" interface
   Generate WPA PSK file for SSID
   
   1.Set the WIFI SSID username and password
   wpa_passphrase command format: wpa_passphrase + wifi name + wifi password > /etc/wpa_supplicant.conf
   
   =====> Input:
   wpa_passphrase MYZR-WIFI-2.4G myzr2012 > /etc/wpa_supplicant.conf
   
   2.Connect:
   =====> Input:
   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
   
   =====> Output:
   Successfully initialized wpa_supplicant
   nl80211: kernel reports: Match already configured
   rfkill: Cannot open RFKILL control device
   ......
   
   3.Obtain IP:
   =====> Input:
   $ udhcpc -i wlan0=====> Output:
   udhcpc: started, v1.37.0
   udhcpc: broadcasting discover
   udhcpc: broadcasting discover
   udhcpc: broadcasting select for 192.168.43.74, server 192.168.43.1
   udhcpc: lease of 192.168.43.74 obtained from 192.168.43.1, lease time 3600
   deleting routers
   adding dns 192.168.43.1
   
   4.Test connection
   =====> Input:
   $ ping -I wlan0 www.baidu.com
   
   =====> Output:
   [   39.924248] RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 SeqNum = 40
   PING www.baidu.com (163.177.151.109): 56 data bytes
   [   40.813870] RTW: OnAction_back
   [   40.816968] RTW: OnAction_back, action=0[   40.821089] RTW: Drop duplicate management frame with seq_num = 668.
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
   "0% packet loss" indicates the WIFI connection is normal
WIFI AP Test
-----------
.. code-block:: shell

   [Test Description]: After WIFI connects to the AP, the development board sends ICMP packets to the external network to verify the connection is normal.
   [Interface Label]: WIFI&BT
   [System Device]: wlan0
   [Interface Silkscreen]: U12
   
   Test Operations
   Connect the antenna to the "U12" interface
   Generate WPA PSK file for SSID
   
   1.Create hotspot
   $ Change ssid in /etc/hostapd.conf to MYZR-SSD2351-EK112 and interface to wlan1
   $ ifconfig wlan1 192.168.8.1
   $ hostapd -B /etc/hostapd.conf
   $ dnsmasq --interface=wlan1 --dhcp-range=192.168.8.2,192.168.8.100,24h
   #Mobile phone can detect MYZR-SSD2351-EK112
   
   2.Enable IP forwarding and NAT
   $ echo 1 > /proc/sys/net/ipv4/ip_forward
   $ iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
Bluetooth Test
-----------
.. code-block:: shell

   [Test Description]: After scanning for Bluetooth devices, send L2CAP echo requests and receive responses
   [Interface Label]: WIFI&BT
   [System Device]: hci0
   [Interface Silkscreen]: U12
   
   Test Operations
   Connect the antenna to the "U12" interface
   
   1.Enable Bluetooth:
   =====> Input:
   $ hciconfig hci0 up
   $ hciconfig=====> Output:
   hci0:   Type: Primary  Bus: UART
       BD Address: B0:F1:EC:A7:E8:03  ACL MTU: 1021:8  SCO MTU: 64:1
       UP RUNNING
       RX bytes:1266 acl:0 sco:0 events:66 errors:0
       TX bytes:1138 acl:0 sco:0 commands:66 errors:0
       
   2.Scan for external Bluetooth devices:
   =====> Input:
   $ hcitool scan=====> Output:
   Scanning ...
       88:46:04:4C:11:A7   Redmi K40
   
   3.Send L2CAP packet test:
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
   "0% packet loss" indicates the Bluetooth connection is normal.
   
   4.Bluetooth connection can use the bluetoothctl command
   #Enter terminal;
   [bluetooth]#
   [bluetooth]# show //Check if controller Power is yes. If Power is no, run power on
   [bluetooth]# power on
   [bluetooth]# agent NoInputNoOutput //Other IO caps can be set, such as KeyboardDisplay
   [bluetooth]# default-agent
   [bluetooth]# scan on //After scanning for the corresponding device, use scan off to stop scanning.
   [bluetooth]# pair 00:22:48:DC:89:0F //Pair with remote device.
   [bluetooth]# connect 00:22:48:DC:89:0F //Connect to remote device
MIC Test
-----------
.. code-block:: shell

   #prog_audio_ai_ao_demo is in the SDK
   #MIC0 recording test
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic1.wav -A 0 -D 0 -R 8000 -C 1 -T 10 -V 60
   #MIC1 recording test
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60
   #MIC2 recording test
   ./prog_audio_ai_ao_demo capture -i adc_b -F test_amic3.wav -A 0 -D 0 -R 8000 -C 1 -T 10 -V 60
