Software Development Guide
============================

Compilation Manual
--------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The compilation host must run on the Ubuntu system, with a version of **Ubuntu 20.04 or higher**. The author's host system is Ubuntu 20.04.
2. The host must have access to the external network, as downloading certain files is required during the system compilation process.

Downloading the Source Code Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the Tina5.0 source code package.
2. Create a compilation directory:

.. code-block:: shell

   mkdir -p ~/my-work/Tina5.0/

3. Place the source code into the newly created directory and extract it:

.. code-block:: shell

   tar xvf 133-tina5.0-20240926-v1.1.tar.gz -C ~/my-work/Tina5.0/

Compilation and Generation of Linux System Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Compilation Environment Configuration

|  Navigate to the Tina5.0 directory and execute the following command to initialize environment variables:

.. code-block:: shell

   source build/envsetup.sh

2. Development Board Model Selection

|  Execute the following command to select the development board model:

.. code-block:: shell

   lunch

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/编译手册1.jpg
   :alt: 编译手册1.jpg

3. Configuration Information

|  Execute the following command to configure the relevant information of the development board:

.. code-block:: shell

   ./build.sh config

.. image:: /image/MYZR-全志系列/MYZR-T113-i-EK168/编译手册2.jpg
   :alt: 编译手册2.jpg

4. Compile LinuxSDK

|  Execute the following command to perform an overall compilation of the LinuxSDK:

.. code-block:: shell

   ./build.sh

5. Image Packaging

|  Execute the following command to package and generate the Linux system image:

.. code-block:: shell

   ./build.sh pack

6. Partial Compilation

|  In the Tina5.0 directory, execute the following command to compile the kernel independently:

.. code-block:: shell

   ./build.sh kernel

|  Package and generate the `boot.fex` file. The path is: `/out/t113_i/evb1_auto/pack_out`

.. code-block:: shell

   ./build.sh pack

|  Add `boot.fex` to the system files and execute the following commands:

.. code-block:: shell

   dd if=boot.fex of=/dev/mmcblk1p4
   reboot

|  In the Tina5.0 directory, execute the following command to compile the bootloader independently:

.. code-block:: shell

   ./build.sh bootloader

|  In the Tina5.0 directory, execute the following command to compile buildroot independently:

.. code-block:: shell

   ./build.sh buildroot_rootfs


Development Guide
--------------------

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

- U-Boot device tree files: 
  `/brandy/brandy-2.0/u-boot-2018/arch/arm/dts/sun8iw20p1-soc-system.dts`
  `/device/config/chips/t113_i/configs/evb1_auto/uboot-board.dts`

- U-Boot board-level configuration file: 
  `/brandy/brandy-2.0/u-boot-2018/include/configs/sun8iw20p1.h`

- U-Boot board-level compilation configuration file: 
  `/brandy/brandy-2.0/u-boot-2018/configs/sun8iw20p1_auto_t113_i_defconfig`

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Kernel board-level compilation configuration file: 
  `device/config/chips/t113_i/configs/evb1_auto/linux-5.4/board.dts`

- Kernel board-level device tree file: 
  `device/config/chips/t113_i/configs/evb1_auto/linux-5.4/config-5.4`

CAN
~~~~~

1. CAN Introduction

|  CAN (Controller Area Network) bus is a serial communication network that effectively supports distributed control or real-time control. As a bus protocol widely used in automobiles, the CAN bus is designed for microcontroller communication in the automotive environment. For more information, please refer to the CAN application report.

2. DTS Node Configuration

|  Kernel device tree: `device/config/chips/t113_i/configs/evb1_auto/linux-5.4/board.dts`

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
                   status = "disabled";
                   */
                   status = "okay";
           };

3. Additional Commands

.. code-block:: shell

   1、 ip link set awlinkX down                 // Disable the CAN device;
   2、 ip link set awlinkX up                   // Enable the CAN device;
   3、 ip -details link show awlinkX            // Display detailed information of the CAN device;
   4、 candump awlinkX                          // Receive data from the CAN bus;
   5、 ifconfig awlinkX down                    // Disable the CAN device for configuration;
   6、 ip link set canX up type can bitrate 250000 // Set the CAN baud rate;
   7、 canconfig awlinkX bitrate + [baud rate];  // Set the CAN baud rate (alternative command);
   8、 canconfig awlinkX start                 // Start the CAN device;
   9、 canconfig awlinkX ctrlmode loopback on   // Perform loopback test;
   10、canconfig awlinkX restart                // Restart the CAN device;
   11、canconfig awlinkX stop                   // Stop the CAN device;
   12、canecho awlinkX                          // Check the bus status of the CAN device;
   13、cansend awlinkX --identifier=ID+[data]   // Send data via the CAN bus;
   14、candump awlinkX --filter=ID:[mask]       // Receive data matching the ID using a filter;

UART
~~~~~~

1. UART Introduction

|  UART (Universal Asynchronous Receiver/Transmitter) is a type of universal asynchronous serial communication interface.

2. DTS Node Configuration

|  Kernel device tree: `device/config/chips/t113_i/configs/evb1_auto/linux-5.4/board.dts`

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
~~~~~~~

1. GPIO Introduction

|  GPIO, short for General-Purpose Input/Output, refers to universal pins that can be dynamically configured and controlled during software operation. All GPIOs are in input mode by default after power-on. They can be set to pull-up or pull-down mode via software, or configured as interrupt pins. Their driving strength is programmable. The core operation involves populating the methods and parameters of the GPIO bank and calling `gpiochip_add` to register them with the kernel.

2. GPIO Pin Number Calculation

|  GPIO pin calculation formula: `pin = bank * 32 + number`
|  The pin naming conventions are: PB x, PC x, PD x, PE x, PF x, PG x.
|  The following is an example of calculating the PC0 pin:
|  Since there are no pins named "PA", the bank value for the PC0 pin is 2.
|  Therefore, `Pin = 2 * 32 + 0 = 64`

3. Interrupts

|  `IRQ_TYPE_LEVEL_LOW` indicates that the interrupt is triggered by a low level. An interrupt function can be triggered when the pin receives a low-level signal. It can also be configured as follows:
|  `IRQ_TYPE_NONE` // Default value, no defined interrupt trigger type
|  `IRQ_TYPE_EDGE_RISING` // Triggered on the rising edge
|  `IRQ_TYPE_EDGE_FALLING` // Triggered on the falling edge
|  `IRQ_TYPE_EDGE_BOTH` // Triggered on both rising and falling edges
|  `IRQ_TYPE_LEVEL_HIGH` // Triggered by a high level
|  `IRQ_TYPE_LEVEL_LOW` // Triggered by a low level

4. GPIO Debug Interface

|  The purpose of the Debugfs file system is to provide developers with more kernel data for easier debugging. GPIO debugging can also use the Debugfs file system to obtain additional kernel information. The GPIO interface in the Debugfs file system is `/sys/kernel/debug/gpio`. You can read information from this interface as follows:

.. code-block:: shell

   ## Manually mount Debugfs
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
~~~~~~~

|  There is one HDMI display output interface in the hardware, which implements MIPI-to-HDMI display output through the LT8912B chip.
|  Kernel driver file: `kernel/linux-5.4/drivers/video/fbdev/sunxi/disp2/disp/lcd/lt8912b.c`
|  U-Boot driver file: `brandy/brandy-2.0/u-boot-2018/drivers/video/sunxi/disp2/disp/lcd/lt8912b.c`