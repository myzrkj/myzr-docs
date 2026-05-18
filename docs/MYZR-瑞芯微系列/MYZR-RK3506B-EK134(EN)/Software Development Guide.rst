Software Development Guide
============================

.. include:: /docs/COMMON/MYZR-RK3588-EK360 Dev Env Setup Manual.rst


Source Code Compilation
--------------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The compilation host must run an Ubuntu system with a version of **Ubuntu 20.04 or higher**. The author's host system uses Ubuntu 20.04.
2. The host must have access to the external network, as downloading certain files is required during the system compilation process.

Downloading the Source Code Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the RK3506 source code package from the path: 3. Software Materials --> 3.1 Source Code --> rk3506-buildroot-20250606.tar.xz
2. Create a compilation directory:

.. code-block:: shell

    mkdir -p ~/my-work/RK3506/02_sources/

3. Move the source code package to the newly created directory and extract it:

.. code-block:: shell

    tar xvf rk3506-buildroot-20250606.tar.xz -C ~/my-work/RK3506/02_sources/

Dependency Installation
~~~~~~~~~~~~~~~~~~~~~~~~~

|   For the first-time compilation, you may need to install certain dependencies. The following are the dependencies that the host may require:

.. code-block:: shell

    sudo apt-get install git bc bison build-essential curl flex g++-
    multilib gcc-multilib gnupg gperf imagemagick lib32ncurses5-dev 
    lib32readline-dev lib32z1-dev liblz4-tool libncurses5-dev 
    libsdl1.2-dev libssl-dev libxml2 libxml2-utils lzop pngcrush 
    rsync schedtool squashfs-tools xsltproc yasm zip zlib1g-dev 
    python device-tree-compiler expect g++ patchelf gawk texinfo 
    chrpath diffstat binfmt-support qemu-user-static live-build 
    fakeroot cmake ssh make gcc g++ unzip ncurses-dev python3-pip 
    libncurses5 libc6:i386 genext2fs u-boot-tools  mtools parted 
    libudev-dev libusb-1.0-0-dev autoconf autotools-dev libsigsegv2 
    m4 intltool libdrm-dev  sed binutils wget libglib2.0-dev 
    libgtk2.0-dev libglade2-dev cvs mercurial gcc-arm-none-eabi 
    gcc-arm-linux-gnueabi openjdk-8-jdk openssh-client subversion 
    asciidoc w3m dblatex graphviz device-tree-compiler flex bison 
    openssl libssl-dev unzip git-lfs ccache libelf-dev default-jdk 
    mtd-utils scons

SDK Configuration Loading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   For the first-time compilation, you need to load the SDK configuration file. Navigate to the rk3506_sdk directory and enter the following command to load the configuration file:

.. code-block:: shell

    ./build.sh myzr_rk3506_ek200_defconfig

Full Compilation
~~~~~~~~~~~~~~~~~~

1. Run the full compilation (the compilation process takes a long time) by entering the following command:

.. code-block:: shell

    ./build.sh

2. After successful compilation, relevant images can be found in the rockdev/ directory, where **update.img** is a collection of all images.


Independent U-Boot Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear generated files before compilation:

.. code-block:: shell

    cd u-boot/
    make clean

2. Return to the main SDK directory and compile U-Boot independently:

.. code-block:: shell

    cd ../
    ./build.sh uboot

Independent Kernel Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear generated files before compilation:

.. code-block:: shell

    cd kernel/
    make clean

2. Return to the main SDK directory and compile the Kernel independently:

.. code-block:: shell

    cd ../
    ./build.sh kernel

Independent Recovery Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Enter the following command in the main SDK directory:

.. code-block:: shell

    ./build.sh recovery

Independent Buildroot Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Enter the following command in the main SDK directory:

.. code-block:: shell

    ./build.sh rootfs

Firmware Packaging
~~~~~~~~~~~~~~~~~~~~

|   Enter the following command in the main SDK directory:

.. code-block:: shell

    ./build.sh firmware

update.img Packaging
~~~~~~~~~~~~~~~~~~~~~~~

1. Package the images into update.img in the rockdev directory.
2. Enter the following command in the main SDK directory:

.. code-block:: shell

    ./build.sh updateimg

|   After completing the above operations, you can reflash the device according to the flashing manual.


Development Guide
-------------------

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   U-Boot board-level files: u-boot/board/rockchip/myzr_rk3506
|   U-Boot board-level configuration file: include/configs/myzr_rk3506.h
|   U-Boot board-level compilation configuration file: configs/myzr_rk3506_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Kernel board-level compilation configuration file: kernel-6.1/arch/arm/configs/rk3506_defconfig
|   Kernel board-level device tree file: kernel-6.1/arch/arm/boot/dts/rockchip/myzr-rk3506-ek200.dts
|   Kernel development reference manual: 《Reference Manual.pdf》 in the network drive

GPIO
~~~~~~

1. GPIO Driver Architecture

|   GPIO is the abbreviation of **General Purpose I/O** (General Purpose Input/Output). Simply put, it refers to pins that can be controlled by an MCU/CPU. These pins usually have multiple functions; the most basic ones are detecting high/low level input and outputting high/low levels. Some pins are also bound to on-chip peripherals of the main controller, such as being used as communication pins for UART, I2C, network, and voltage detection. Linux provides a GPIO subsystem driver framework, and using this framework allows flexible control of the GPIOs on the board.

2. Pin Naming Convention

|   The GPIOs of RK3506 are divided into 4 groups (GPIO0 ~ GPIO3), and each group is further distinguished by numbers A0~A7, B0~B7, C0~C7, and D0~D7. For example:

- GPIO0_C2 refers to the 2nd pin in group C of the 0th group (GPIO0).
- GPIO3_B5 refers to the 5th pin in group B of the 3rd group (GPIO3).

3. Calculation Formula for GPIO Pin Numbering

|   bank: GPIO group number (0 ~ 3).
|   group: The sequence number corresponding to the letter within the group (A=0, B=1, C=2, D=3).
|   X: Specific number within the group (0 ~ 7).
|   number: Number within the group, calculated using the following formula:
|   GPIO subgroup number calculation formula: number = group * 8 + X
|   GPIO pin number calculation formula: pin = bank * 32 + number
|   The following demonstrates the calculation method for the GPIO0_C2 pin:
|   bank = 0 (GPIO0).
|   group = 2 (group C corresponds to 2).
|   X = 2 (the "2" in C2).
|   number = group * 8 + X = 2 * 8 + 2 = 18.
|   pin = bank * 32 + number = 0 * 32 + 18 = 18.

4. Controlling GPIO via the /sys/class/gpio Directory

.. code-block:: shell

|   In Linux, the most common way to read and write GPIOs is by using the **GPIO sysfs interface**, which is implemented by operating files such as export, unexport, gpio{N}/direction, and gpio{N}/value (replace {N} with the actual pin number) under the /sys/class/gpio directory. This method is often used in shell scripts.
|   echo 18 > /sys/class/gpio/export     # Enable the GPIO0_C2 pin
|   echo out > gpio18/direction          # Set the pin to output mode
|   echo 1 > gpio18/value                # Set the pin to high level
|   cat /sys/class/gpio/gpio18/value  # Read the value of the pin
|   echo 18 > /sys/class/gpio/unexport   # Release the GPIO
|   Note: Some GPIOs cannot be exported because they are multiplexed for other functions (such as UART, I2C). You need to confirm their actual usage through the device tree.


UART
~~~~~~

1. Device Tree Configuration (Taking UART3_M0 as an example, which corresponds to pins 5 and 6 on the J17 expansion interface)

.. code-block:: shell

    &uart3 {
        status = "okay";
        pinctrl-names = "default";
        pinctrl-0 = <&rm_io14_uart3_tx &rm_io15_uart3_rx>;
    };

|   The function of `pinctrl-0 = <&rm_io14_uart3_tx &rm_io15_uart3_rx>;` is to bind the TX/RX pins of UART3 to the rm_io14 and rm_io15 multiplexing groups.
|   uart3m0_xfer has been defined in rk3506-pinctrl-rmio.dtsi:

.. code-block:: shell

    rm_io14_uart3_tx: rm-io14-uart3-tx {
                rockchip,pins =
                    <0 RK_PB6 20 &pcfg_pull_none>;
    };
    rm_io15_uart3_rx: rm-io15-uart3-rx {
                rockchip,pins =
                    <0 RK_PB7 21 &pcfg_pull_up>;
    };

|   After the device tree is configured, UART3 is registered as /dev/ttyS3 in the system. You can verify this by running `ls /dev/ttyS*`.

2. Debugging Tools

|   Short-circuit the RX and TX pins of UART3, and use the test files placed in the file system to perform transceiving tests:

.. code-block:: shell

    =====> Input:
    # /myzr_test/uart/serial_test.out /dev/ttyS3 "myzr"
    =====> Output:
    Starting send data...finish
    Starting receive data:
    ASCII: 0x6d          Character: m 
    ASCII: 0x79          Character: y 
    ASCII: 0x7a          Character: z 
    ASCII: 0x72          Character: r 
    ASCII: 0x0            Character:

CAN
~~~~~

1. CAN Introduction

|   CAN (Controller Area Network) bus is a serial communication network that effectively supports distributed control or real-time control. It is a bus protocol widely used in automobiles and is designed for microcontroller communication in automotive environments. For more information, you can refer to the CAN application report.

2. DTS Node Configuration

- Public configuration: kernel/arch/arm/boot/dts/rk3506.dtsi

.. code-block:: shell

    can0: can@ff320000 {
               compatible = "rockchip,rk3506-canfd", "rockchip,rk3576-canfd";
               reg = <0xff320000 0x1000>;
               interrupts = <GIC_SPI 45 IRQ_TYPE_LEVEL_HIGH>;
               clocks = <&cru CLK_CAN0>, <&cru HCLK_CAN0>;
               clock-names = "baudclk", "apb_pclk";
               resets = <&cru SRST_CAN0>, <&cru SRST_H_CAN0>;
               reset-names = "can", "can-apb";
               status = "disabled";
        };
       
- Board-level configuration: arch/arm/boot/dts/rockchip/myzr-rk3506-ek200.dts

.. code-block:: shell

    &can0 {
        status = "okay";
        assigned-clocks = <&cru CLK_CAN0>;
        assigned-clock-rates = <200000000>;
        pinctrl-names = "default";
        pinctrl-0 = <&rm_io19_can0_tx &rm_io20_can0_rx>;
    };

3. Additional Commands

.. code-block:: shell

    1、 ip link set canX down                 // Disable the CAN device;
    2、 ip link set canX up                   // Enable the CAN device;
    3、 ip -details link show canX            // Display detailed information about the CAN device;
    4、 candump canX                          // Receive data from the CAN bus;
    5、 ifconfig canX down                    // Disable the CAN device for configuration;
    6、 ip link set canX up type can bitrate 250000 // Set the CAN baud rate;
    7、 canconfig canX bitrate + baud_rate;   // Set the CAN baud rate (alternative command);
    8、 canconfig canX start                  // Start the CAN device;
    9、 canconfig canX ctrlmode loopback on   // Enable loopback test;
    10、canconfig canX restart                // Restart the CAN device;
    11、canconfig canX stop                   // Stop the CAN device;
    12、canecho canX                          // Check the bus status of the CAN device;
    13、cansend canX --identifier=ID+data     // Send data;
    14、candump canX --filter=ID:mask         // Receive data matching the ID using a filter;

4. Delayed or No Reception After Message Transmission

|   Check the CAN_H and CAN_L lines of the bus to see if the Dupont wires are loose or reversed.

Ethernet
~~~~~~~~~~

|   The development board has two network ports: J14 and J15. The following description takes J14 as an example, and the configuration for J15 is similar.
|   Both network ports support connecting to the external network.

1. DTS Configuration

|   1.1 Public configuration
|   kernel-6.1/arch/arm/boot/dts/rockchip/rk3506.dtsi

.. code-block:: shell

    gmac0: ethernet@ff4c8000 {
            compatible = "rockchip,rk3506-gmac", "snps,dwmac-4.20a";
            reg = <0xff4c8000 0x2000>;
            interrupts = <GIC_SPI 66 IRQ_TYPE_LEVEL_HIGH>,
                         <GIC_SPI 69 IRQ_TYPE_LEVEL_HIGH>;
            interrupt-names = "macirq", "eth_wake_irq";
            rockchip,grf = <&grf>;
            clocks = <&cru CLK_MAC0>, <&cru CLK_MAC0_PTP>,
                     <&cru PCLK_MAC0>, <&cru ACLK_MAC0>;
            clock-names = "stmmaceth", "ptp_ref",
                          "pclk_mac", "aclk_mac";
            resets = <&cru SRST_A_MAC0>;
            reset-names = "stmmaceth";

            snps,mixed-burst;
            snps,tso;

            snps,axi-config = <&gmac0_stmmac_axi_setup>;
            snps,mtl-rx-config = <&gmac0_mtl_rx_setup>;
            snps,mtl-tx-config = <&gmac0_mtl_tx_setup>;

            phy-mode = "rmii";
            status = "disabled";

            mdio0: mdio {
                    compatible = "snps,dwmac-mdio";
                    #address-cells = <0x1>;
                    #size-cells = <0x0>;
            };

            gmac0_stmmac_axi_setup: stmmac-axi-config {
                    snps,wr_osr_lmt = <4>;
                    snps,rd_osr_lmt = <8>;
                    snps,blen = <0 0 0 0 16 8 4>;
            };

            gmac0_mtl_rx_setup: rx-queues-config {
                    snps,rx-queues-to-use = <1>;
                    queue0 {
                            status = "okay";
                    };
            };

            gmac0_mtl_tx_setup: tx-queues-config {
                    snps,tx-queues-to-use = <1>;
                    queue0 {
                            status = "okay";
                    };
            };
    };

|   1.2 Board-level configuration
|   kernel-6.1/arch/arm/boot/dts/rockchip/myzr-gmac0-100m.dtsi

.. code-block:: shell

    &gmac0 {
        status = "okay";
        phy-mode = "rmii";
        clock_in_out = "output";
        snps,reset-gpio = <&nca9555_gpio IO_00 GPIO_ACTIVE_LOW>;
        snps,reset-active-low;
        snps,reset-delays-us = <0 10000 100000>;
        compatible = "rockchip,rk3506-gmac", "snps,dwmac-4.20a";
        tx_delay = <0x1a>;
        rx_delay = <0x21>;
        phy-handle = <&rmii_phy0>;
        pinctrl-names = "default";    
        pinctrl-0 = <&gmac_rmii0_miim_pins
                    &gmac_rmii0_tx_bus2_pins
                    &gmac_rmii0_rx_bus2_pins
                    &gmac_rmii0_clk_pins>;                
    };

2. If the Network Port Fails to Obtain an IP Address Automatically

|   Wait for a moment, or disable the network sharing of the host's network adapter that has internet access to the Ethernet port and re-enable sharing. Then restart the board, and it will automatically obtain an IP address.

I2C
~~~~~

1. Overview of the I2C Subsystem Architecture

|   In the RK3506 platform, the I2C controller is implemented based on the standard Linux I2C framework. Its core is divided into a hardware abstraction layer (adapter driver) and a device driver layer. The hardware layer abstracts the I2C bus controller through `i2c_adapter`, the device layer describes the slave device through `i2c_client`, and the two layers implement the driver logic through `i2c_driver`. The I2C controller of RK3562 supports multi-master mode, clock division (up to 400kHz), and interrupt/DMA transmission. Its physical layer follows the open-drain output characteristic, and the SCL/SDA signals are implemented through GPIO multiplexing.

2. I2C Device Tree Configuration

|   Taking the GT9 touch chip mounted on I2C1 as an example, open myzr-lcd-mipi-7-1024-600.dtsi for configuration:

.. code-block:: shell

    &i2c2 {
        status = "okay";
        pinctrl-names = "default";

        goodix_ts: goodix_ts@5d {
            compatible = "goodix,gt9xx";
            reg = <0x5d>;  
            gtp_resolution_x = <1024>;
            gtp_resolution_y = <600>;    
            gtp_int_tarigger = <1>;
            gtp_change_x2y = <0>;
            gtp_overturn_x = <0>;
            gtp_overturn_y = <0>;
            gtp_send_cfg = <1>;
            gtp_touch_wakeup = <1>;

            goodix_rst_gpio = <&gpio0 RK_PA7 GPIO_ACTIVE_HIGH>;
            goodix_irq_gpio = <&gpio0 RK_PA6 IRQ_TYPE_EDGE_FALLING>;
              goodix,cfg-group0 = [    //old touch
            ...
            ];

            goodix,cfg-group5 = [    //new touch
            ...
            ];      
        };
    };

|   In this node, the kernel matches the driver through the `compatible` string. For example, the gt9xx.c file in the driver code must define the same `of_device_id` table:

.. code-block:: shell

    static struct of_device_id goodix_ts_dt_ids[] = {
        { .compatible = "goodix,gt9xx" },
        { }
    };

|   The address of the device on the I2C bus is 0x5d, and the driver obtains the `reg` address through the `i2c_client` structure. The `pinctrl-*` references the `touch_gpio` node to configure the multiplexing function and electrical properties of the GPIO.
|   When the driver matches the device tree (i.e., the `compatible` value matches the driver), the kernel calls the `.probe()` function. In the `probe` function, the driver will obtain configurations from the device tree, including pin configurations, chip model, and other information.
|   After the device is successfully registered on the I2C bus, use the following command:
|   `i2cdetect -y 1`
|   You can see the letter "UU" appear at address 5d on I2C1, which indicates that the device is successfully mounted on the I2C bus.