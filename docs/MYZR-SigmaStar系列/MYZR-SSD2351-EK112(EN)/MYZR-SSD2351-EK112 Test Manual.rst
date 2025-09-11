MYZR-SSD2351-EK112 Test Manual
================================

UART Test
~~~~~~~~~~~

UART4 Configuration and Test
------------------------------

|  【Test Description】: Short the J4:3 (UART4_RX) pin and J4:5 (UART4_TX) pin.
|  【Interface Identification】: J4
|  【System Device】: /dev/ttyS4
|  【Interface Silkscreen】: UART4_TX and UART4_RX

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

UART3 Configuration and Test
-------------------------------

.. code-block:: shell

   #Configuration (disabled by default, configured as MIPI interface; if to be used, need to enable the configuration and shield others)
   $ vim arch/arm/boot/dts/pcupid-ssm001c-s01a-voip-padmux.dtsi

|  Add (need to shield other pin configurations of PAD_OUTP_CH0 and PAD_OUTN_CH0)
|                   //UART3 Mode2
|                   <PAD_OUTP_CH0            PINMUX_FOR_FUART3_2W_MODE_2        MDRV_PUSE_UART3_TX>,
|                   <PAD_OUTN_CH0            PINMUX_FOR_FUART3_2W_MODE_2        MDRV_PUSE_UART3_RX>,

|  【Test Description】: Short the J19:5 (MIPITX_D0P) pin and J19:6 (MIPITX_D0M) pin.
|  【Interface Identification】: J19
|  【System Device】: /dev/ttyS3
|  【Interface Silkscreen】: MIPITX_D0M and MIPITX_D0P

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


UART2 Configuration and Test
------------------------------

|  【Test Description】: Short the J4:7 (FUART2_RX) pin and J4:8 (FUART2_TX) pin.
|  【Interface Identification】: J4
|  【System Device】: /dev/ttyS2
|  【Interface Silkscreen】: FUART2_TX and FUART2_RX

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


UART1 Configuration and Test
------------------------------

|  【Test Description】: Short the J4:9 (FUART1_RX) pin and J4:10 (FUART1_TX) pin.
|  【Interface Identification】: J4
|  【System Device】: /dev/ttyS1
|  【Interface Silkscreen】: FUART1_TX and FUART1_RX

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

UART5 Configuration and Test
------------------------------

|  【Test Description】: Short the J18:1 (UART5_TX) pin and J18:2 (UART5_RX) pin.
|  【Interface Identification】: J18
|  【System Device】: /dev/ttyS5
|  【Interface Silkscreen】: UART5_TX and UART5_RX

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

UART6 Configuration and Test
------------------------------

|  【Test Description】: Short the J4:35 (UART0_TX) pin and J4:38 (UART0_RX) pin.
|  【Interface Identification】: J4
|  【System Device】: /dev/ttyS5
|  【Interface Silkscreen】: UART0_TX and UART0_RX

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

UART7 Configuration and Test
------------------------------

|  【Test Description】: Short the J4:37 (UART7_TX) pin and J4:40 (UART7_RX) pin.
|  【Interface Identification】: J4
|  【System Device】: /dev/ttyS7
|  【Interface Silkscreen】: UART7_TX and UART7_RX

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

I2C2 Configuration and Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  【Test Description】: Connect the J19:11 (I2C2_SDA) pin and J19:13 (I2C2_SCL) pin to the hym8563 module, along with power and ground. I2C2 is connected to the hym8563 RTC clock module, and 0x51 is the setting address of hym8563. If the module does not exist, an error will be reported; otherwise, a normal prompt will be given.
|  【Interface Identification】: J19
|  【System Device】: /dev/i2c2
|  【Interface Silkscreen】: I2C2_SDA and I2C2_SCL

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

   #2.Test hym8563 real-time clock
   #Device interface: /dev/rct1
   #Test description: Detect and set the clock
   $ dmesg | grep rtc
   #Output information:
   sstar,rtcpwc 1f006800.rtcpwc: registered as rtc0
   sstar,rtcpwc 1f006800.rtcpwc: setting system clock to 1970-01-01T04:41:54 UTC (16914)
   input: rtcpwc as /devices/soc0/soc/1f