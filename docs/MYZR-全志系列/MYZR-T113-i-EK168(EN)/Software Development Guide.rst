Software Development Guide
============================

Compilation Manual
---------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The compilation host must run the Ubuntu system. The author's host uses Ubuntu 20.04. It is recommended to use the same Ubuntu version as the author to avoid compatibility issues with some tools due to different versions.
2. The host must be able to connect to the external network, as the compilation process needs to download some files.
3. The code syntax of some files conflicts with Python 3, so it is recommended to use Python 2.

Downloading the Source Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the Tina5.0 source package.
2. Create a compilation directory:

.. code-block:: shell

   mkdir -p ~/my-work/Tina5.0/

3. Place the source code into the newly created directory and extract it:

.. code-block:: shell

   tar xvf 133-tina5.0-20240926-v1.1.tar.gz -C ~/my-work/Tina5.0/

Compilation and Generation of Linux System Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Compilation Environment Configuration

|  Enter the Tina5.0 directory and execute the following commands to clear old compilation and configuration files and initialize environment variables:

.. code-block:: shell

   cd Tina5.0
   ./build.sh distclean

   cd Tina5.0
   source build/envsetup.sh

2. Development Board Model Selection

|  Execute the following command to select the development board model:

.. code-block:: shell

   lunch

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/编译手册1.png
   :alt: 编译手册1.jpg

3. Configuration Information

|  Execute the following command to configure the relevant information of the development board:

.. code-block:: shell

   ./build.sh config

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/编译手册2.png
   :alt: 编译手册2.jpg

4. Compile LinuxSDK

|  Execute the following command to compile the entire LinuxSDK:

.. code-block:: shell

   ./build.sh

5. Package the Image

|  Execute the following command to package and generate the Linux system image:

.. code-block:: shell

   ./build.sh pack

6. Partial Compilation

|  Execute the following command in the Tina5.0 directory to compile the kernel separately:

.. code-block:: shell

   ./build.sh kernel

|  Package and generate the boot.fex file, whose path is: /out/t113_i/evb1_auto/pack_out

.. code-block:: shell

   ./build.sh pack

|  Add boot.fex to the system files and execute the following command:

.. code-block:: shell

   dd if=boot.fex of=/dev/mmcblk1p4

   reboot

|  Execute the following command in the Tina5.0 directory to compile the bootloader separately:

.. code-block:: shell

   ./build.sh buildroot_rootfs


Possible Issues During Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Path error when executing ./build.sh

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/编译手册3.png
   :alt: 编译手册3.jpg

|  Execute the following command

.. code-block:: shell

   cd ./rtos/lichee/rtos

   make distclean

|  If a syntax problem is encountered when executing make distclean:

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/编译手册4.png
   :alt: 编译手册4.jpg

|  Execute the following command to check the currently used Python version. If Python 3 is currently used, it needs to be changed to Python 2.

.. code-block:: shell

   python --version

2. Error: Unable to find the file drv_type.h:

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/编译手册5.png
   :alt: 编译手册5.jpg

|  Execute the following command:

.. code-block:: shell

   vim ./kernel/linux-5.4/drivers/net/wireless/realtek/rtl8723du/Makefile

|  Find the following code:

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/编译手册6.png
   :alt: 编译手册6.jpg

|  Modify the code as shown in the following figure, or modify it to the absolute path of the current PC:

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/编译手册7.png
   :alt: 编译手册7.jpg


Development Guide
-------------------

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

- U-Boot device tree files: /brandy/brandy-2.0/u-boot-2018/arch/arm/dts/sun8iw20p1-soc-system.dts
  /device/config/chips/t113_i/configs/evb1_auto/uboot-board.dts

- U-Boot board-level configuration file: /brandy/brandy-2.0/u-boot-2018/include/configs/sun8iw20p1.h
- U-Boot board-level compilation configuration file: /brandy/brandy-2.0/u-boot-2018/configs/sun8iw20p1_auto_t113_i_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Kernel board-level compilation configuration file: device/config/chips/t113_i/configs/evb1_auto/linux-5.4/board.dts
- Kernel board-level device tree file: device/config/chips/t113_i/configs/evb1_auto/linux-5.4/config-5.4

CAN
~~~~~

1. CAN Introduction

|  CAN (Controller Area Network) bus is a serial communication network that effectively supports distributed control or real-time control. The CAN bus is a widely adopted bus protocol in automobiles and is designed for microcontroller communication in the automotive environment. For more information, you can refer to the CAN application report.

2. DTS Node Configuration

|  Kernel device tree: device/config/chips/t113_i/configs/evb1_auto/linux-5.4/board.dts

.. code-block:: shell

   can0: can@0x0 {
                   #address-cells = <1>;
                   #size-cells = <0>;
                   compatible = "allwinner,sun8i-awlink";
                   device_type = "awlink0";
                   id = <0>;
                   /*
                   status = "disabled";
                   */
                   status = "okay";
           };
   can1: can@0x1 {
                   #address-cells = <1>;
                   #size-cells = <0>;
                   compatible = "allwinner,sun8i-awlink";
                   device_type = "awlink1";
                   id = <1>;
                   /*
                   status = "disabled";/
                   */
                   status = "okay";
           };

3. More Commands

.. code-block:: shell

   1、 ip link set awlinkX down                 // Turn off the CAN device;
   2、 ip link set awlinkX up                   // Turn on the CAN device;
   3、 ip -details link show awlinkX            // Display detailed information of the CAN device;
   4、 candump awlinkX                          // Receive data from the CAN bus;
   5、 ifconfig awlinkX down                    // Turn off the CAN device for configuration;
   6、 ip link set canX up type can bitrate 250000 // Set the CAN baud rate;
   7、 canconfig awlinkX bitrate + baud rate;
   8、 canconfig awlinkX start                  // Start the CAN device;
   9、 canconfig awlinkX ctrlmode loopback on   // Loopback test;
   10、canconfig awlinkX restart                // Restart the CAN device;
   11、canconfig awlinkX stop                   // Stop the CAN device;
   12、canecho awlinkX                          // Check the status of the CAN device bus;
   13、cansend awlinkX --identifier=ID+data     // Send data;
   14、candump awlinkX --filter=ID:mask         // Receive data with matching ID using a filter

UART
~~~~~~

1. UART Introduction

|  UART (Universal Asynchronous Receiver/Transmitter) is a type of universal asynchronous serial communication interface.

2. DTS Node Configuration

|  Kernel device tree: device/config/chips/t113_i/configs/evb1_auto/linux-5.4/board.dts

.. code-block:: shell

   &uart0 {
       pinctrl-names = "default", "sleep";
       pinctrl-0 = <&uart0_pins_a>;
       pinctrl-1 = <&uart0_pins_b>;
           status = "okay";
   };
   
   &uart1 {
           pinctrl-names = "default", "sleep";
           pinctrl-0 = <&uart1_pins_a>;
           pinctrl-1 = <&uart1_pins_b>;
           status = "okay";
   };
   
   &uart2 {
           pinctrl-names = "default", "sleep";
           pinctrl-0 = <&uart2_pins_a>;
           pinctrl-1 = <&uart2_pins_b>;
           /*
           status = "disabled";
           */
           status = "okay";
   };
   
   &uart3 {
           pinctrl-names = "default", "sleep";
           pinctrl-0 = <&uart3_pins_a>;
           pinctrl-1 = <&uart3_pins_b>;
       /*
       status = "disabled";
       */
       status = "okay";
   };
   
   
   &uart4 {
           pinctrl-names = "default", "sleep";
           pinctrl-0 = <&uart4_pins_a>;
           pinctrl-1 = <&uart4_pins_b>;
           status = "okay";
   };
   
   &uart5 {
           pinctrl-names = "default", "sleep";
           pinctrl-0 = <&uart5_pins_a>;
           pinctrl-1 = <&uart5_pins_b>;
           status = "okay";
   };

GPIO
~~~~~~

1. GPIO Introduction

|  GPIO, short for General-Purpose Input/Output, is a type of general-purpose pin that can be dynamically configured and controlled during software operation. All GPIOs are in input mode after power-on. They can be set to pull-up or pull-down via software, or set as interrupt pins. The drive strength is programmable. The core is to fill the methods and parameters of the GPIO bank and call gpiochip_add to register it in the kernel.

2. GPIO Pin Number Calculation

|  GPIO pin calculation formula: pin = bank * 32 + number
|  The pins are named as follows: PB x, PC x, PD x, PE x, PF x, PG x.
|  The following demonstrates the calculation method for the PC0 pin:
|  Since there are no pins named PA, the bank of the PC0 pin is 2.
|  Pin = 2 * 32 + 0 = 64

3. Interrupt

|  IRQ_TYPE_LEVEL_LOW means the interrupt is triggered by a low level. When the pin receives a low-level signal, it can trigger the interrupt function. It can also be configured as follows:
|  IRQ_TYPE_NONE // Default value, no defined interrupt trigger type
|  IRQ_TYPE_EDGE_RISING // Triggered on rising edge
|  IRQ_TYPE_EDGE_FALLING // Triggered on falling edge
|  IRQ_TYPE_EDGE_BOTH // Triggered on both rising and falling edges
|  IRQ_TYPE_LEVEL_HIGH // Triggered by high level
|  IRQ_TYPE_LEVEL_LOW // Triggered by low level

4. GPIO Debug Interface

|  The purpose of the Debugfs file system is to provide developers with more kernel data for easy debugging. The debugging of GPIO here can also use the Debugfs file system to obtain more kernel information. The interface of GPIO in the Debugfs file system is /sys/kernel/debug/gpio. You can read the information of this interface as follows:

.. code-block:: shell

   ## Manually mount debugfs
   mount -t debugfs none /sys/kernel/debug

   cat sys/kernel/debug/gpio
   gpiochip0: GPIOs 0-223, parent: platform/2000000.pinctrl, 2000000.pinctrl:
    gpio-44  (                    |usb0-vbus           ) out lo 
    gpio-64  (                    |heartbeat           ) out lo 
    gpio-65  (                    |disk                ) out lo 
    gpio-108 (                    |bt_hostwake         ) in  hi 
    gpio-109 (                    |bt_wake             ) out lo 
    gpio-130 (                    |otg_id              ) in  hi IRQ 
    gpio-166 (                    |cd                  ) in  hi ACTIVE LOW
    gpio-203 (                    |user-led0           ) out lo 

HDMI
~~~~~~

|  There is an HDMI display output interface on the hardware, which realizes MIPI to HDMI display output through the LT8912B chip.
|  Kernel driver file: kernel/linux-5.4/drivers/video/fbdev/sunxi/disp2/disp/lcd/lt8912b.c
|  U-Boot driver file: brandy/brandy-2.0/u-boot-2018/drivers/video/sunxi/disp2/disp/lcd/lt8912b.c