MYZR-LS1012A-EK200 L4498 Driver and Device
============================================

Document Description
-----------------------

System Environment Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Compilation Host CPU Architecture: 64-bit
- Compilation Host System: Linux
- Linux Distribution: Ubuntu
- Ubuntu Version Type: Server Edition
- Ubuntu Version Number: 14.04.1
- Ubuntu System Type: x86-64

``Note: Please use Ubuntu 14.04.1 x86-64 (either Desktop Edition or Server Edition) for the development host. Using other Linux distributions or other versions of Ubuntu may lead to unnecessary issues.``

Operation Instructions
~~~~~~~~~~~~~~~~~~~~~~~~

|  (1) Lines starting with "$" in the document are followed by Linux commands.
|  (2) It is recommended to manually enter all Linux commands in the document into the Linux host for execution. Direct copying and pasting into the Linux host may result in execution failure.
|  (3) For Linux execution commands in the document where the character immediately after a space is "-" (e.g., commands like "sudo apt-get –y install"), please manually enter them into the Linux host for execution. Direct copying and pasting into the Linux host usually leads to execution failure.
|  (4) For Linux commands in the document that are not fully contained in a single line, please manually enter them into the Linux host for execution. This is because copied and pasted commands cannot include special characters such as "line breaks".
|  (5) When entering and executing Linux commands according to the document, pay attention to checking whether the execution result matches that shown in the document images. This is to confirm if there are any input errors in the command and whether the command execution failed.
|  (6) Strictly follow the document for the first compilation. Otherwise, inexplicable errors may occur.

Screenshot Description
~~~~~~~~~~~~~~~~~~~~~~~~

|   To make the view concise and neat, the command prompt in all screenshots uniformly uses "myzr$".

Linux Commands in Images
~~~~~~~~~~~~~~~~~~~~~~~~~~

|   In the images of the document, you can directly view the entered Linux commands by looking at the lines starting with "linyn@u14041-serv:~$".

Driver and Related Device Files
---------------------------------

|   The Linux-4.4.98 version corresponding to the evaluation board, as well as the corresponding source code files and devices, are shown in the following table:

+-------------+-------------------------------------------+---------------------------+
|  Function   |             Source Code Path              | Linux Devices and Folders |
+=============+===========================================+===========================+
| GPIO        | drivers/gpio/gpio-mpc8xxx.c               | /sys/class/gpio/          |
+-------------+-------------------------------------------+---------------------------+
| LCD         | drivers/video/fbdev/mxsfb.c               | /dev/fb*                  |
+-------------+-------------------------------------------+---------------------------+
| BACKLIGHT   | drivers/video/backlight/pwm_bl.c          | /sys/class/backlight      |
+-------------+-------------------------------------------+---------------------------+
| UART        | drivers/tty/serial/of_serial.c            | /dev/ttyXRUSB*            |
+-------------+-------------------------------------------+---------------------------+
| I2C         | drivers/i2c/busses/i2c-imx.c              | /dev/i2c-0                |
+-------------+-------------------------------------------+---------------------------+
| MMC/SD/SDIO | drivers/mmc/host/sdhci-of-esdhc.c         | /sys/bus/mmc/             |
+-------------+-------------------------------------------+---------------------------+
| FEC         | drivers/net/ethernet/freescale/fec_main.c | eth0, eth1                |
+-------------+-------------------------------------------+---------------------------+
| USB         | drivers/usb/dwc3/core.c                   | /sys/bus/usb/             |
+-------------+-------------------------------------------+---------------------------+
|             | drivers/usb/host/fsl-mph-dr-of.c          |                           |
+-------------+-------------------------------------------+---------------------------+
| WATCHDOG    | drivers/watchdog/imx2_wdt.c               | /dev/watchdog             |
+-------------+-------------------------------------------+---------------------------+
| RTL8723du   | drivers/net/wireless/rtl8723du/           | wlan0                     |
+-------------+-------------------------------------------+---------------------------+
| Bluetooth   | drivers/bluetooth/rtk_*                   | hci0                      |
+-------------+-------------------------------------------+---------------------------+
| EC20        | drivers/net/usb/ec20/                     | eth2                      |
+-------------+-------------------------------------------+---------------------------+

- Main Device Tree File: arch/arm64/boot/dts/myzr/ls1012a-ek200.dts
- Device Tree Registration Information File: arch/arm64/boot/dts/myzr/ls1012a.dtsi ("***" represents 140, 140p)
