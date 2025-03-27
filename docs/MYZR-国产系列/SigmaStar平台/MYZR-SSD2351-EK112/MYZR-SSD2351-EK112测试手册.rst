MYZR-SSD2351-EK112测试手册
============================

UART测试
~~~~~~~~~~

UART4配置和测试
-----------------

.. code:: shell

   #设备接口：/dev/ttyS4
   #测试说明：把J4:3(GPIOA_16_UART4_RX)管脚和J4:5(GPIOA_17_UART4_TX)管脚短接.
   $ ./serial_test.out /dev/ttyS4 "www.myzr.com.cn"
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


UART3配置和测试
-----------------

.. code:: shell

   #配置(默认禁止，配置为MIPI接口，如果要用，需要打开配置,屏蔽)
   $ vim arch/arm/boot/dts/pcupid-ssm001c-s01a-voip-padmux.dtsi

   #增加（需要屏蔽到PAD_OUTP_CH0和PAD_OUTN_CH0其他管脚配置）
   //UART3 Mode2      
   <PAD_OUTP_CH0  MDRV_PUSE_UART3_TX>,
   <PAD_OUTN_CH0  MDRV_PUSE_UART3_RX>,
    
   #设备接口：/dev/ttyS3
   #测试说明：把J19:5(OUTP_TX0_CH0_MIPITX_D0P)管脚和J19:6(OUTN_TX0_CH0_MIPITX_D0N)管脚短接.
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


UART2配置和测试
-----------------

.. code:: shell

   #设备接口：/dev/ttyS2
   #测试说明：把J4:7(OUTP_RX0_CH2_FUART2_RX)管脚和J19:8(OUTN_RX0_CH2_FUART2_TX)管脚短接.
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


UART1配置和测试
----------------

.. code:: shell

   #设备接口：/dev/ttyS1
   #测试说明：把J4:9(OUTP_RX0_CH0_FUART1_RX)管脚和J4:10(OUTN_RX0_CH0_FUART1_TX)管脚短接.
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


UART5配置和测试
-----------------

.. code:: shell

   #设备接口：/dev/ttyS5
   #测试说明：把J18:1(GPIOE_07_UART5_TX)管脚和J18:2(GPIOE_06_UART5_RX)管脚短接.
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

UART6配置和测试
-----------------

.. code:: shell

   #设备接口：/dev/ttyS6
   #测试说明：把J4:35(UART0_TX)管脚和J4:38(UART0_RX)管脚短接.
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

UART7配置和测试
-----------------

.. code:: shell

   #设备接口：/dev/ttyS7
   #测试说明：把J4:37(ADC_PWM_OUT01_UART7_TX)管脚和J4:40(ADC_PWM_OUT00_UART7_RX)管脚短接.
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


I2C2配置和测试
~~~~~~~~~~~~~~~~

.. code:: shell

   #1.i2ctool测试
   #设备接口：/dev/i2c2
   #测试说明：把J19:11(GPIOE_10_I2C2_SDA)管脚和J19:13(GPIOE_09_I2C2_SCL)接上hym8563模块，还有电源和地.i2c2接了hym8563的rtc时钟模块，0x51是hym8563的设置地址，如果模块不存在，会报错。正常提示一下：
   $ ./i2cdump -f -y 2 0x51

   #输出信息：
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
   sstar,rtcpwc 1f006800.rtcpwc: setting system clock to 1970-01-01T04:41:54 UTC 
   (16914)
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

.. code:: shell

   #设备接口：/dev/spidev0.0
   #测试说明：把J18:16(GPIOA_15_MSPI0_MISO)管脚和J18:17(GPIOA_14_MSPI0_MOSI)管脚短接.
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

   #注意：如果没有短接，输出以下信息：
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

.. code:: shell

   #设备接口：
   # PAD_PM_PWM0_OUT：对应设备节点/sys/class/sstar/pwm/pwm18
   # PAD_PM_PWM1_OUT：对应设备节点/sys/class/sstar/pwm/pwm19
   # PAD_EMMC_D4：对应设备节点/sys/class/sstar/pwm/group3/pwm14
   # PAD_EMMC_D5：对应设备节点/sys/class/sstar/pwm/group3/pwm15
   # PAD_EMMC_D6：对应设备节点/sys/class/sstar/pwm/group3/pwm16
   #测试说明：用示波器查看,以J18:7(EMMC_D4_PWM_OUT[14])为例输出100HZ，50%占空比，极性normal的波形
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


.. code:: shell

   #设备接口：/sys/class/gpio
   #测试说明：以J18:10(EMMC_D1_GPIO)为例
   #设置高电平和低电平
   $ echo 68 > /sys/class/gpio/export 
   $ echo out > /sys/class/gpio/gpio58/direction 
   $ echo 1 > /sys/class/gpio/gpio58/value 
   $ echo 0 > /sys/class/gpio/gpio58/value

   #读取管脚电平
   $ echo in > /sys/class/gpio/gpio58/direction 
   $ cat /sys/class/gpio/gpio58/value


TF卡测试
~~~~~~~~~~

.. code:: shell

   #设备接口：/dev/mmcblk0
   #测试说明：插入TF卡
   #提示信息如下：
   SDMMC0 >> [Hal_CARD_SetBustiming] LS mode. <<
   SDMMC0 >> [Hal_CARD_SetBustiming] HS mode. <<
      
   #查看分区：
   $ ls /dev/mmcblk0*
   
   #输出信息：
   /dev/mmcblk0   /dev/mmcblk0p1   /dev/mmcblk0p2
   
   #挂载
   $ mount  /dev/mmcblk0p1  /mnt/
   $ ls /mnt/
   imx6ul~1.dtb   imx6ul~3.dtb    imx6ul~5.dtb    imx6ul~7.dtb    zimage
   imx6ul~2.dtb   imx6ul~4.dtb    imx6ul~6.dtb    system~1
   
   #卸载
   $ umount /mnt/


U盘测试
~~~~~~~~~

.. code:: shell

   #设备接口：/dev/sd*
   #测试说明：插入U盘
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

.. code:: shell

   #设备接口：/dev/eth0
   ##测试说明：电脑设置为192.168.137.99，板子设置为192.168.137.81，通过ping测试
   $ ifconfig eth0 192.168.137.81
   
   #输出信息：
   [emac_phy_link_adjust] EMAC Link Down 
   [emac_phy_link_adjust] EMAC Link Up
   
   #测试 如果没有丢包，正常。
   $ ping 192.168.137.99 -c 2 -w 4
   PING 192.168.137.99 (192.168.137.99): 56 data bytes
   64 bytes from 192.168.137.99: seq=0 ttl=64 time=0.537 ms
   64 bytes from 192.168.137.99: seq=1 ttl=64 time=0.276 ms
   
   --- 192.168.137.99 ping statistics --
   2 packets transmitted, 2 packets received, 0% packet loss
   round-trip min/avg/max = 0.276/0.406/0.537 ms


WIFI测试
~~~~~~~~~~

.. code:: shell

   #设备接口：/dev/wlan0
   ##测试说明：把WIFI天线接上，WIFI连接到AP后，开发板向外网发送ICMP报文来验证连接正常。
   $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/customer/wifi/
   
   #方法1；
   #a.配置文件：
   $ vi /customer/wifi/wpa_supplicant.conf
   
   #修改ssid和psk
   ctrl_interface=/tmp/wifi/run/wpa_supplicant
   update_config=1
   network={
   ssid="sstest"
   psk="12345678"
   }
   
   #保存
   $ ifconfig wlan0 up
   $ mkdir -p /tmp/wifi/run
   
   #b.连接
   $ /customer/wifi/wpa_supplicant -Dnl80211 -i wlan0 -c $ 
   /customer/wifi/wpa_supplicant.conf -d &
   
   #c.自动获取IP
   $ udhcpc -q -i wlan0 -s /etc/init.d/udhcpc.script &
   
   #方法2；
   #a.配置ssid和密码
   $ wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf
   
   #b.连接
   $ /customer/wifi/wpa_supplicant -Dnl80211 -i wlan0 -B -c /customer/wpa_supplicant.conf
   
   #c.自动获取IP
   $ udhcpc -q -i wlan0 -s /etc/init.d/udhcpc.script &


蓝牙测试
~~~~~~~~~~

.. code:: shell

   #设备接口：hci0
   ##测试说明：描到蓝牙设备后，发送L2CAP回应请求并接收回答。
   #打开蓝牙
   $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/customer/bt
   $ /customer/bt/hciconfig hci0 up
   
   #提示信息如下：
   rtk_btusb: btusb_open hdev->promisc ==0
   $ /customer/bt/hciconfig
   
   #提示信息如下：
   hci0:  Type: Primary  Bus: USB
     BD Address: 38:01:46:43:CF:0B  ACL MTU: 1021:8  SCO MTU: 255:12
     UP RUNNING 
     RX bytes:1170 acl:0 sco:0 events:60 errors:0
     TX bytes:736 acl:0 sco:0 commands:60 errors:0