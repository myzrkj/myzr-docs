MYZR-IMX28 Linux-3.14.52 Device and Driver
=============================================

Document instruction
----------------------

System environment instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- CPU architecture of compilation host:64 bit
- Compilation host system：Linux
- Linux release version: Ubuntu
- Ubuntu version type: saver version
- Ubuntu version no.: 12.04.5
- Ubuntu system type: x86-64

**Note：for development host please use ubuntu 12.04.5 x86-64（either desktop version or server version is ok），some unneccessory problems may arise if use Linux in other release version or Ubuntu in other versions.**

Operation instruction
~~~~~~~~~~~~~~~~~~~~~~~

|   1）Line start with “$”in the document，following it is Linux command
|   2）All Linux commands are recommended to enter manually to Linux host for execution（direct copy,pasting to Linux host for execution may cause failure.
|   3）If following a space in Linux execution command is “-”（such as：sudo apt-ge t –y install and the like），please enter manually to Linux host for execution（direct copy,pasting to Linux host for execution normally cause failure）.
|   4）Any uncompleted Linux command in all lines in the doucment,please enter manually to the Linux host for execution（because copy,pasting commands don't contain special charater such as“line break”）.
|   5）Observe whether result of command execution is consistent with images in the documents after enter and execute Linux commands as per documents,to ensure whether entering of command is correct or whether there is failure of execution.
|   6）Please follow strictly the documents for the first compilation，otherwise some unexpected errors may arise.

Screenshots instruction
~~~~~~~~~~~~~~~~~~~~~~~~~

|  To make the view look neat and tidy , the command prompt in the screenshot should use myzr$ uniformly.

Linux command in images
~~~~~~~~~~~~~~~~~~~~~~~~~

|  In the image of the document, you can see the input Linux command visually from the lines that start with “linyn@u12045-serv:~$” linux command.

Driving and relevant device file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Source code and device corresponding to version Linux-3.14.54 for evaluation board are refered to below table：

+--------------+-------------------------------------------+-------------------------+
|   Function   |           Source code position            | Linux device and folder |
+==============+===========================================+=========================+
| GPIO         | drivers/gpio/gpiolib.c                    | /sys/class/gpio/        |
+--------------+-------------------------------------------+-------------------------+
| LCD          | drivers/video/                            | /dev/fb0                |
+--------------+-------------------------------------------+-------------------------+
| LED          | drivers/leds/leds-gpio.c                  | /sys/class/leds/        |
+--------------+-------------------------------------------+-------------------------+
| BACKLIGHT    | drivers/video/backlight/pwm_bl.c          | /sys/class/backlight/   |
+--------------+-------------------------------------------+-------------------------+
| UART         | drivers/tty/serial/amba-pl011.c           | /dev/ttyAMA0            |
+              +-------------------------------------------+-------------------------+
|              | drivers/tty/serial/mxs-auart.c            | /dev/ttyAPP*            |
+--------------+-------------------------------------------+-------------------------+
| I2C          | drivers/i2c/i2c-dev.c                     | /dev/i2c-0              |
+--------------+-------------------------------------------+-------------------------+
| SPI          | drivers/spi/spidev.c                      | /dev/spidev1.0          |
+--------------+-------------------------------------------+-------------------------+
| MMC/SD/SDIO  | drivers/mmc/                              | /dev/mmcblk*            |
+--------------+-------------------------------------------+-------------------------+
| NAND GPMI    | drivers/mtd/nand/gpmi-nand/               | /dev/mtd*               |
+--------------+-------------------------------------------+-------------------------+
| TOUCH SCREEN | drivers/staging/iio/adc/mxs-lradc.c       | /dev/input/event0       |
+--------------+-------------------------------------------+-------------------------+
| FEC          | drivers/net/ethernet/freescale/fec_main.c | eth0，eth1              |
+--------------+-------------------------------------------+-------------------------+
| PWM          | drivers/pwm/pwm-mxs.c                     | /sys/class/pwm/         |
+--------------+-------------------------------------------+-------------------------+
| SGTL5000     | sound/soc/codecs/sgtl5000.c               | /dev/snd/               |
+--------------+-------------------------------------------+-------------------------+
| USB          | drivers/usb/                              | NC                      |
+--------------+-------------------------------------------+-------------------------+
| FLEXCAN      | drivers/net/can/flexcan.c                 | can0,can1               |
+--------------+-------------------------------------------+-------------------------+
| WATCHDOG     | drivers/watchdog/stmp3xxx_rtc_wdt.c       | /dev/watchdog           |
+--------------+-------------------------------------------+-------------------------+


- Main file of device tree:arch/arm/boot/dts/imx28-evk.dts
- Basic file of device tree:：arch/arm/boot/dts/imx28.dtsi
- Function file of pin:arch/arm/boot/dts/imx28-pinfunc.h

**Note：please check carefully register，please refer to “MCIMX28RM.pdf”file.**