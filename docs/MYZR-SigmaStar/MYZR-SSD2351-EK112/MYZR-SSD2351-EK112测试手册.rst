MYZR-SSD2351-EK112测试手册
============================

UART测试
~~~~~~~~~~

UART4配置和测试
-----------------

|  【测试说明】：把J4:3(UART4_RX)管脚和J4:5(UART4_TX)管脚短接。
|  【接口标识】：J4
|  【系统设备】：/dev/ttyS4
|  【接口丝印】：UART4_TX和UART4_RX

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

UART3配置和测试
-----------------

.. code-block:: shell

   #配置(默认禁止，配置为MIPI接口，如果要用，需要打开配置,屏蔽)
   $ vim arch/arm/boot/dts/pcupid-ssm001c-s01a-voip-padmux.dtsi

|  增加（需要屏蔽到PAD_OUTP_CH0和PAD_OUTN_CH0其他管脚配置）
|                   //UART3 Mode2
|                   <PAD_OUTP_CH0            PINMUX_FOR_FUART3_2W_MODE_2        MDRV_PUSE_UART3_TX>,
|                   <PAD_OUTN_CH0            PINMUX_FOR_FUART3_2W_MODE_2        MDRV_PUSE_UART3_RX>,

|  【测试说明】：把J19:5(MIPITX_D0P)管脚和J19:6(MIPITX_D0M)管脚短接。
|  【接口标识】：J19
|  【系统设备】：/dev/ttyS3
|  【接口丝印】：MIPITX_D0M和MIPITX_D0P

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



UART2配置和测试
-----------------

|  【测试说明】：把J4:7(FUART2_RX)管脚和J4:8(FUART2_TX)管脚短接。
|  【接口标识】：J4
|  【系统设备】：/dev/ttyS2
|  【接口丝印】：FUART2_TX和FUART2_RX

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


UART1配置和测试
----------------

|  【测试说明】：把J4:9(FUART1_RX)管脚和J4:10(FUART1_TX)管脚短接。
|  【接口标识】：J4
|  【系统设备】：/dev/ttyS1
|  【接口丝印】：FUART1_TX和FUART1_RX

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

UART5配置和测试
-----------------

|  【测试说明】：把J18:1(UART5_TX)管脚和J18:2(UART5_RX)管脚短接。
|  【接口标识】：J18
|  【系统设备】：/dev/ttyS5
|  【接口丝印】：UART5_TX和UART5_RX

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

UART6配置和测试
-----------------

|  【测试说明】：把J4:35(UART0_TX)管脚和J4:38(UART0_RX)管脚短接。
|  【接口标识】：J4
|  【系统设备】：/dev/ttyS5
|  【接口丝印】：UART0_TX和UART0_RX

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

UART7配置和测试
-----------------

|  【测试说明】：把J4:37(UART7_TX)管脚和J4:40(UART7_RX)管脚短接。
|  【接口标识】：J4
|  【系统设备】：/dev/ttyS7
|  【接口丝印】：UART7_TX和UART7_RX

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

I2C2配置和测试
~~~~~~~~~~~~~~~~

|  【测试说明】：把J19:11(I2C2_SDA)管脚和J19:13(I2C2_SCL)接上hym8563模块模块，还有电源和地.i2c2接了hym8563的rtc时钟模块，0x51是hym8563的设置地址，如果模块不存在，会报错。正常提示一下。
|  【接口标识】：J19
|  【系统设备】：/dev/i2c2
|  【接口丝印】：I2C2_SDA和I2C2_SCL

.. code-block:: shell

   #1.i2ctool测试
   $ cd /customer/app/
   $ ./i2cdump -f -y 2 0x51
   输出信息：
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

   #2.测试hym8563实时时钟
   #设备接口：/dev/rct1
   #测试说明：检测和设置时钟
   $ dmesg | grep rtc
   #输出信息：
   sstar,rtcpwc 1f006800.rtcpwc: registered as rtc0
   sstar,rtcpwc 1f006800.rtcpwc: setting system clock to 1970-01-01T04:41:54 UTC (16914)
   input: rtcpwc as /devices/soc0/soc/1f006800.rtcpwc/input/input0
   rtc-hym8563 2-0051: registered as rtc1

   #测试hym8563时钟
   #a.设置系统时钟2025-03-01 12:34:19
   $ date 
   Thu Jan  1 04:59:47 UTC 1970
   $ date -s "2025-03-01 12:34:19"
   Sat Mar  1 12:34:19 UTC 2025
   #b.把系统时钟写到硬件时钟
   $ hwclock -w -f /dev/rtc1
   #c.读取硬件时钟是否正确
   $ hwclock -r -f /dev/rtc1
   Sat Mar  1 12:35:07 2025  0.000000 seconds

SPI0配置和测试
~~~~~~~~~~~~~~~

|  【测试说明】：把J18:16(MSPI0_MISO)管脚和J18:17(MSPI0_MOSI)管脚短接。
|  【接口标识】：J18
|  【系统设备】：/dev/spidev0.0
|  【接口丝印】：MSPI0_MISO和MSPI0_MOSI

.. code-block:: shell

   $ cd /customer/app/
   $ /customer/tools # ./spidev_test.out -D /dev/spidev0.0 
   #输出信息
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
   注意：如果没有短接，输出以下信息：
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

PWM配置和测试
~~~~~~~~~~~~~~

|  【测试说明】：把PWM管脚拉低（0V)或拉高(1.8V)。
|  【接口标识】：J18,J4
|  【系统设备】：/sys/class/sstar/pwm
|  【接口丝印】：PM_PWM0_OUT和PM_PWM1_OUT和EMMC_D4和EMMC_D5和EMMC_D6

.. code-block:: shell

   # PAD_PM_PWM0_OUT：对应设备节点/sys/class/sstar/pwm/pwm18
   # PAD_PM_PWM1_OUT：对应设备节点/sys/class/sstar/pwm/pwm19
   # PAD_EMMC_D4：对应设备节点/sys/class/sstar/pwm/group3/pwm14
   # PAD_EMMC_D5：对应设备节点/sys/class/sstar/pwm/group3/pwm15
   # PAD_EMMC_D6：对应设备节点/sys/class/sstar/pwm/group3/pwm16
   #测试说明：用示波器查看,以J18:7(EMMC_D4)为例输出100HZ，50%占空比，极性normal的波形
   $ cd /sys/class/sstar/pwm/group3/pwm14
   $ echo 1000000  > period
   $ echo 500000   > duty
   $ echo normal   > polarity
   $ echo 1        > enable


GPIO配置和测试
~~~~~~~~~~~~~~~

+--------------+------------+-------------+------------+-------------+------------+
|   Pad Name   | GPIO Index |  Pad Name   | GPIO Index |  Pad Name   | GPIO Index |
+==============+============+=============+============+=============+============+
| PAD_EMMC_CMD | 52         | PAD_EMMC_D5 | 57         | PAD_EMMC_D3 | 54         |
+--------------+------------+-------------+------------+-------------+------------+
| PAD_EMMC_D0  | 56         | PAD_EMMC_D1 | 58         |             |            |
+--------------+------------+-------------+------------+-------------+------------+

|  【测试说明】：把GPIO管脚拉低或拉高。
|  【接口标识】：J18
|  【系统设备】：/sys/class/gpio
|  【接口丝印】：EMMC_CMD和EMMC_D5和EMMC_D3和EMMC_D0和EMMC_D1

.. code-block:: shell

   #测试说明：以J18:10(EMMC_D1)为例
   # 设置高电平和低电平
   $ echo 68 > /sys/class/gpio/export 
   $ echo out > /sys/class/gpio/gpio58/direction 
   $ echo 1 > /sys/class/gpio/gpio58/value 
   $ echo 0 > /sys/class/gpio/gpio58/value 
   #读取管脚电平
   $ echo in > /sys/class/gpio/gpio58/direction 
   $ cat /sys/class/gpio/gpio58/value

TF卡测试
~~~~~~~~~~

|  【测试说明】：插入TF卡。
|  【接口标识】：J12
|  【系统设备】：/dev/mmcblk0
|  【接口丝印】：J12

.. code-block:: shell

   #提示信息如下：
   SDMMC0 >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] HS mode. <<
   #查看分区：
   $ ls /dev/mmcblk0*
   #输出信息：
   /dev/mmcblk0    /dev/mmcblk0p1  /dev/mmcblk0p2
   #挂载
   $ mount /dev/mmcblk0p1 /mnt/
   $ ls /mnt/
   imx6ul~1.dtb  imx6ul~3.dtb  imx6ul~5.dtb  imx6ul~7.dtb  zimage
   imx6ul~2.dtb  imx6ul~4.dtb  imx6ul~6.dtb  system~1
   #卸载
   $ umount /mnt/

U盘测试
~~~~~~~~~

|  【测试说明】：插入u盘。
|  【接口标识】：J16
|  【系统设备】：/dev/sd*
|  【接口丝印】：J16

.. code-block:: shell

   $ dmesg | grep sd
   #提示信息如下：
   sd 0:0:0:0: [sda] 61440000 512-byte logical blocks: (31.5 GB/29.3 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
   sd 0:0:0:0: [sda] No Caching mode page found
   sd 0:0:0:0: [sda] Assuming drive cache: write through
    sda: sda1
   sd 0:0:0:0: [sda] Attached SCSI removable disk

   #查看分区：
   $ ls /dev/sd*
   #输出信息：
   /dev/sda   /dev/sda1
   #挂载
   $ mount /dev/sda1 /mnt/
   $ ls /mnt/
   imx6ul~1.dtb  imx6ul~3.dtb  imx6ul~5.dtb  imx6ul~7.dtb  zimage
   imx6ul~2.dtb  imx6ul~4.dtb  imx6ul~6.dtb  system~1
   #卸载
   $ umount /mnt/

以太网测试
~~~~~~~~~~~

|  【测试说明】：电脑设置为192.168.137.99，板子设置为192.168.137.81，通过ping测试。
|  【接口标识】：CONR1
|  【系统设备】：/dev/eth0
|  【接口丝印】：CONR1

.. code-block:: shell

   $ ifconfig eth0 192.168.137.81
   #输出信息：
   [emac_phy_link_adjust] EMAC Link Down 
   [emac_phy_link_adjust] EMAC Link Up
   #测试 如果没有丢包，正常。
   $ ping 192.168.137.99 -c 2 -w 4
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=64 time=0.537 ms
   64 bytes from 192.168.137.99: seq=1 ttl=64 time=0.276 ms

   --- 192.168.137.99 ping statistics ---
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.276/0.406/0.537 ms

WIFI STA测试
~~~~~~~~~~~~~~

|  【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：WIFI&BT
|  【系统设备】：wlan0
|  【接口丝印】：U12

.. code-block:: shell

|  测试操作

1. 把天线连接到“U12”接口上
2. 生成 SSID 的 WPA PSK 文件

|  wpa_passphrase命令格式：wpa_passphrase + wifi名称 + wifi密码 > /etc/wpa_supplicant.conf

.. code-block:: shell

   =====> Input:
   wpa_passphrase MYZR-WIFI-2.4G myzr2012 > /etc/wpa_supplicant.conf

3. 连接：

.. code-block:: shell

   =====> Input:
   wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf 

   =====> Output:
   Successfully initialized wpa_supplicant
   nl80211: kernel reports: Match already configured
   rfkill: Cannot open RFKILL control device
   ......

4. 获取IP：

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

5. 测试连接：

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

|  “0% packet loss”表示wifi连接正常。

WIFI AP测试
-------------

|  【测试说明】：WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
|  【接口标识】：WIFI&BT
|  【系统设备】：wlan0
|  【接口丝印】：U12

1. 创建热点

.. code-block:: shell

   $ /etc/hostapd.conf的ssid改成MYZR-SSD2351-EK112和interface改成wlan1
   $ ifconfig wlan1 192.168.8.1
   $ hostapd -B /etc/hostapd.conf
   $ dnsmasq --interface=wlan1 --dhcp-range=192.168.8.2,192.168.8.100,24h
   #手机可以识别到MYZR-SSD2351-EK112

2. 启用IP转发与NAT

.. code-block:: shell

   $ echo 1 > /proc/sys/net/ipv4/ip_forward
   $ iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE

蓝牙测试
----------

|  【测试说明】：扫描到蓝牙设备后，发送L2CAP回应请求并接收回答
|  【接口标识】：WIFI&BT
|  【系统设备】：hci0
|  【接口丝印】：U12

|  测试操作

1. 把天线连接到“U12”接口上
2. 启动蓝牙：

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

3. 扫描外部蓝牙设备：

.. code-block:: shell

   =====> Input:
   $ hcitool scan

   =====> Output:
   Scanning ...
       88:46:04:4C:11:A7   Redmi K40

4. 发送发送L2CAP包测试：

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

|  “0% packet loss”表示蓝牙连接正常。
|  连接蓝牙可以用命令 bluetoothctl

.. code-block:: shell

   #进入终端;
   [bluetooth]#
   [bluetooth]# show //查看控制器的 Power 是否为 yes，如果 Power 为 no，则运行 power on
   [bluetooth]# power on
   [bluetooth]# agent NoInputNoOutput //可以设置其他 IO caps, 如 KeyboardDisplay
   [bluetooth]# default-agent
   [bluetooth]# scan on //扫描到对应的设备后，使用 scan off 关闭 scan。
   [bluetooth]# pair 00:22:48:DC:89:0F //配对远端设备。
   [bluetooth]# connect 00:22:48:DC:89:0F //连接远端设备

MIC测试
---------

.. code-block:: shell

   #MIC0录音测试
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic1.wav -A 0 -D 0 -R 8000 -C 1 -T 10 -V 60
   #MIC1录音测试
   ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60
   #MIC2录音测试
   ./prog_audio_ai_ao_demo capture -i adc_b -F test_amic3.wav -A 0 -D 0 -R 8000 -C 1 -T 10 -V 60
