
MYZR-IMX8M-EK300 Devices and Drivers
=======================================

Document description
-----------------------

System environment description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Compile host CPU architecture: 64-bit
- Compile the host system：Linux
- Linux distribution: Ubuntu
- Ubuntu version type: server version
- Ubuntu version number: 14.04.1
- Ubuntu system type: x86-64

|  ``note：Please use ubuntu 14.04.1 x86-64 as the development host (desktop or server version). If you use other distributions of Linux or other versions of Ubuntu, you may encounter unnecessary problems.``

Instructions
~~~~~~~~~~~~~~

|   1）Lines in the document that begin with "$" followed by Linux commands。
|   2）All Linux commands in the document are recommended to be manually entered into the Linux host for execution (copy and paste directly to the Linux host for execution, and execution may fail)。
|   3）The Linux execution command in the document. If the next character after the space is "-" (such as: sudo apt-get -y install and the like), please manually enter it to execute on the Linux host (copy and paste directly to the Linux host Execution, usually fails).
|   4）Please enter all Linux commands that have not been written in one line in the document and execute them on the Linux host (because the copy and paste commands cannot contain special characters like "newline characters").
|   5）When entering and executing a Linux command according to a document, observe whether the command execution result is consistent with that in the picture of the document to confirm whether the command is entered incorrectly and whether the execution fails.
|   6） Please compile the first pass strictly according to the documentation, otherwise inexplicable errors may occur.

Screenshot description
~~~~~~~~~~~~~~~~~~~~~~~~~

|  To make the view look neat and tidy, the command prompt in the screenshot is used uniformly myzr$。

Drivers and related device files
----------------------------------

|  The Linux-4.14.98 version corresponding to the evaluation board and the corresponding source files and devices are shown in the table below.：

+-------------+-----------------------------------------------------------------------------------------+---------------------------+
|  Features   |                                     Source location                                     | Linux Devices and folders |
+=============+=========================================================================================+===========================+
| GPIO        | drivers/gpio/gpio-mxc.c                                                                 | /sys/class/gpio/          |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| UART        | drivers/tty/serial/imx.c                                                                | /dev/ttymxc*              |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| I2C         | drivers/i2c/busses/i2c-imx.c                                                            | /dev/i2c-*                |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| SPI         | drivers/mtd/spi-nor/fsl-quadspi.c                                                       | NC                        |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| MMC/SD/SDIO | drivers/mmc/host/                                                                       | /sys/bus/mmc/             |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| FEC         | drivers/net/ethernet/freescale/fec_main.c                                               | eth0                      |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| PWM         | drivers/pwm/pwm-imx.c                                                                   | /sys/class/pwm            |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| HDMI        | drivers/gpu/drm/imx/hdp/imx-hdp.c                                                       | /dev/mxc_hantro           |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| GPU         | drivers/mxc/gpu-viv/hal/os/linux/kernel/platform/freescale/gc_hal_kernel_platform_imx.c | /dev/galcore              |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| VPU         | drivers/mxc/hantro/hantrodec.c                                                          | /dev/mxc_hantro           |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| MIPI CSI    | drivers/media/platform/imx8/mxc-mipi-csi2_yav.c                                         | NC                        |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| PCIE        | drivers/pci/host/pci-imx6.c                                                             | /sys/class/pci_bus        |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| WM8524      | sound/soc/fsl/imx-wm8524.c                                                              | /dev/snd                  |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| USB         | drivers/usb/dwc3/dwc3-of-simple.c                                                       | /sys/bus/usb/             |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| AP6354      | drivers/net/wireless/bcmdhd/                                                            | wlan0                     |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+
| USDHC       | drivers/mmc/host/sdhci-esdhc-imx.c                                                      | NC                        |
+-------------+-----------------------------------------------------------------------------------------+---------------------------+

- Device tree main file: arch / arm64 / boot / dts / myzr / myimx8mek300-8mq.dts
- Device tree registration information file: arch / arm / boot / dts / myzr / myimx8mq.dtsi
- Device tree pin configuration file: arch / arm / boot / dts / myzr / myimx8mq.dtsi
- Pin function predefined file: include / dt-bindings / pinctrl / pins-imx8mq.h

|  ``Note: If you want to view the register in detail, please see the "IMX8MDQLQRM_Rev0.pdf" file。``