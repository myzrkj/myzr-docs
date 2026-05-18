Software Development Guide
============================

.. include:: /docs/COMMON/MYZR-RK3588-EK360 Dev Env Setup Manual.rst


Linux Source Code Compilation
-------------------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The compilation host must run on an Ubuntu system with a version of **Ubuntu 20.04 or higher**. The author's host system is Ubuntu 20.04.
2. The host must have access to the external network, as downloading certain files is required during the system compilation process.

Downloading the Source Code Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the RK3562 source code package from the path: 3. Software Materials --> 3.1 Source Code --> rk3562-linux.tar.xz
2. Create a compilation directory:

.. code-block:: shell

    mkdir -p ~/my-work/RK3562/02_sources/

3. Place the source code in the newly created directory and extract it:

.. code-block:: shell

    tar xvf rk3562-linux.tar.xz -C ~/my-work/RK3562/02_sources/

Dependency Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~

|   For the first compilation, you may need to install certain dependencies. The following are some dependencies that the host may require:

.. code-block:: shell

    sudo apt-get install -y git ssh make gcc libssl-dev liblz4-tool expect expect-dev g++ patchelf 
    chrpath gawk texinfo chrpath diffstat binfmt-support qemu-user-static live-build bison flex 
    fakeroot rsync cmake gcc-multilib g++-multilib unzip device-tree-compiler ncurses-dev 
    libgucharmap-2-90-dev bzip2 expat gpgv2 cpp-aarch64-linux-gnu libgmp-dev libmpc-dev bc 
    python-is-python3 python2 libpkgconf-dev

SDK Configuration Loading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   For the first compilation, you need to load the SDK configuration file. Navigate to the rk3562_sdk directory and enter the following command to load the configuration file:

.. code-block:: shell

    ./build.sh myzr_rk3562_evb_defconfig
    cd buildroot/
    ./envsetup.sh rockchip_rk3562

Full Compilation
~~~~~~~~~~~~~~~~~~

1. Return to the main SDK directory and run the full compilation (the compilation process takes a long time) by entering the following command:

.. code-block:: shell

    cd ../
    ./build.sh

2. After successful compilation, you can find the relevant images in the rockdev/ directory, where **update.img** is a collection of all images.

Independent U-Boot Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear the generated files before compilation:

.. code-block:: shell

    cd u-boot/
    make clean

2. Return to the main SDK directory and compile U-Boot independently:

.. code-block:: shell

    cd ../
    ./build.sh uboot

Independent Kernel Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear the generated files before compilation:

.. code-block:: shell

    cd kernel/
    make clean

2. Return to the main SDK directory and compile the Kernel independently:

.. code-block:: shell

    cd ../
    ./build.sh kernel

Independent Recovery Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~

1. Package the images into update.img in the output/update/Image directory under the SDK.
2. Enter the following command in the main SDK directory:

.. code-block:: shell

    ./build.sh updateimg

|   After completing the above operations, you can re-flash the device according to the flashing manual.


Android Source Code Compilation
---------------------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The compilation host must run on an Ubuntu system with a version of **Ubuntu 20.04 or higher**. The author's host system is Ubuntu 20.04.
2. The host must have access to the external network, as downloading certain files is required during the system compilation process.

Downloading the Source Code Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the RK3562 source code package from the path: 3. Software Materials --> 3.1 Source Code --> rk3562-linux.tar.xz
2. Create a compilation directory:

.. code-block:: shell

    mkdir -p ~/my-work/RK3562/02_sources/

3. Place the source code in the newly created directory and extract it:

.. code-block:: shell

    tar xvf rk3562-linux.tar.xz -C ~/my-work/RK3562/02_sources/

Dependency Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~

|   For the first compilation, you may need to install certain dependencies. The following are some dependencies that the host may require:

.. code-block:: shell

    sudo apt-get install -y git ssh make gcc libssl-dev liblz4-tool expect expect-dev g++ patchelf 
    chrpath gawk texinfo chrpath diffstat binfmt-support qemu-user-static live-build bison flex 
    fakeroot rsync cmake gcc-multilib g++-multilib unzip device-tree-compiler ncurses-dev 
    libgucharmap-2-90-dev bzip2 expat gpgv2 cpp-aarch64-linux-gnu libgmp-dev libmpc-dev bc 
    python-is-python3 python2 libpkgconf-dev

SDK Configuration Loading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   For the first compilation, you need to load the SDK configuration file. Navigate to the rk3562_sdk directory and enter the following command to load the configuration file:

.. code-block:: shell

    ./build.sh myzr_rk3562_evb_defconfig
    cd buildroot/
    ./envsetup.sh rockchip_rk3562

Full Compilation
~~~~~~~~~~~~~~~~~~

1. Return to the main SDK directory and run the full compilation (the compilation process takes a long time) by entering the following command:

.. code-block:: shell

    cd ../
    ./build.sh

2. After successful compilation, you can find the relevant images in the rockdev/ directory, where **update.img** is a collection of all images.

Independent U-Boot Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear the generated files before compilation:

.. code-block:: shell

    cd u-boot/
    make clean

2. Return to the main SDK directory and compile U-Boot independently:

.. code-block:: shell

    cd ../
    ./build.sh uboot

Independent Kernel Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear the generated files before compilation:

.. code-block:: shell

    cd kernel/
    make clean

2. Return to the main SDK directory and compile the Kernel independently:

.. code-block:: shell

    cd ../
    ./build.sh kernel

Independent Recovery Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~

1. Package the images into update.img in the output/update/Image directory under the SDK.
2. Enter the following command in the main SDK directory:

.. code-block:: shell

    ./build.sh updateimg

|   After completing the above operations, you can re-flash the device according to the flashing manual.


Development Guide
-------------------

|   Description of key file paths and their functions.

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

|   U-Boot board-level file path: u-boot/board/rockchip/myzr_rk3562
|   U-Boot board-level configuration file: include/configs/myzr_rk3562.h
|   U-Boot board-level compilation configuration file: configs/myzr_rk3562_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Kernel board-level compilation configuration file: kernel-5.10/arch/arm64/configs/rockchip_linux_defconfig
|   Kernel board-level device tree files:

1. kernel-5.10/arch/arm64/boot/dts/rockchip/myzr-rk3562-ek200.dts (default device tree, applicable to HDMI displays)
2. kernel-5.10/arch/arm64/boot/dts/rockchip/myzr-rk3562-ek200-lvds-lcd.dtsi (alternative, applicable to LVDS LCD displays)
3. kernel-5.10/arch/arm64/boot/dts/rockchip/myzr-rk3562-ek200-mipi-lcd.dtsi (alternative, applicable to MIPI LCD displays)

Ethernet
~~~~~~~~~~

|   The development board has two network ports: CON8 and CON9. The following description takes CON8 as an example, and CON9 operates similarly.
|   Both network ports support connection to the external network.

1. DTS Configuration

|   1.1 Common Configuration
|   kernel-5.10/arch/arm64/boot/dts/rockchip/rk3562.dtsi

.. code-block:: shell

    gmac0: ethernet@ffa80000 {
        compatible = "rockchip,rk3562-gmac", "snps,dwmac-4.20a";
        reg = <0x0 0xffa80000 0x0 0x10000>;
        interrupts = <GIC_SPI 73 IRQ_TYPE_LEVEL_HIGH>,
                     <GIC_SPI 70 IRQ_TYPE_LEVEL_HIGH>;
        interrupt-names = "macirq", "eth_wake_irq";
        rockchip,grf = <&sys_grf>;
        rockchip,php_grf = <&ioc_grf>;
        clocks = <&cru CLK_GMAC_125M_CRU_I>, <&cru CLK_GMAC_50M_CRU_I>,
                 <&cru PCLK_GMAC>, <&cru ACLK_GMAC>;
        clock-names = "stmmaceth", "clk_mac_ref",
                      "pclk_mac", "aclk_mac";
        resets = <&cru SRST_A_GMAC>;
        reset-names = "stmmaceth";
        rockchip,csu = <&csu CSU_GMAC_ACLK>, <&csu CSU_GMAC_PCLK>;
        rockchip,csu-names = "aclk", "pclk";
        snps,mixed-burst;
        snps,tso;
        snps,axi-config = <&gmac0_stmmac_axi_setup>;
        snps,mtl-rx-config = <&gmac0_mtl_rx_setup>;
        snps,mtl-tx-config = <&gmac0_mtl_tx_setup>;
        status = "disabled";
        mdio0: mdio {
            compatible = "snps,dwmac-mdio";
            #address-cells = <0x1>;
            #size-cells = <0x0>;
    };

|   1.2 Board-Level Configuration
|   kernel-5.10/arch/arm64/boot/dts/rockchip/myzr-rk3562-ek200.dts

.. code-block:: shell

    &gmac0 {
        snps,reset-gpio = <&gpio3 RK_PD0 GPIO_ACTIVE_LOW>;
        snps,reset-delays-us = <20000 20000 100000>;
        tx_delay = <0x38>;
        rx_delay = <0x1e>;
        pinctrl-0 = <&rgmiim0_miim
                    &rgmiim0_tx_bus2
                    &rgmiim0_rx_bus2
                    &rgmiim0_rgmii_clk
                    &rgmiim0_rgmii_bus>;
        phy-handle = <&rgmii_phy>;
    };

2. If the network port fails to obtain an IP address automatically

|   Wait, or disable the network sharing of the host's network adapter that can access the internet to the Ethernet port, then re-enable sharing. Restart the board, and it will automatically obtain an IP address.

GPIO
~~~~~~~

**1. GPIO Driver Architecture**

|   The GPIO function of RK3562 is implemented through a three-level architecture: 

- The hardware layer uses 5 built-in GPIO controllers (corresponding to device nodes gpiochip0~4) to directly manage 32 pins in each group, and the manufacturer provides the underlying register driver. 
- The kernel layer abstracts hardware differences through the Linux GPIO subsystem and provides standard APIs (such as the gpiod interface) upward, allowing kernel drivers to operate any pin in a unified manner (e.g., setting direction, reading/writing levels). 
- The user layer imports the GPIO subsystem interface into user space through the Sysfs module (/sys/class/gpio), enabling direct pin control (exporting, direction configuration, level reading/writing) via the command line without writing code. 

|   In this entire mechanism, the hardware driver is provided by the chip manufacturer, the Linux kernel implements general abstraction, and developers can either program to control GPIO based on kernel APIs or perform quick debugging through Sysfs.
|   The following section explains how to directly control GPIO (direction/level) through the command line at the user layer.

**2. Pin Naming Convention**

|   The GPIOs of RK3562 are divided into 5 groups (GPIO0~GPIO4), and each group is numbered with A0~A7, B0~B7, C0~C7, D0~D7. For example:

- GPIO0_D0 refers to the 0th pin in group D of the 0th group (GPIO0).
- GPIO4_B5 refers to the 5th pin in group B of the 4th group (GPIO4).

**3. Calculation Formula for GPIO Pin Number**

|   bank: GPIO group number (0~4).
|   group: sequence number corresponding to the letter (A=0, B=1, C=2, D=3).
|   X: specific number within the group (0~7).
|   number: number within the group, calculated by the following formula:
|   GPIO subgroup number calculation formula: number = group * 8 + X
|   GPIO pin number calculation formula: pin = bank * 32 + number
|   The following demonstrates the calculation method for the GPIO4_B5 pin:
|   bank = 4 (GPIO4).
|   group = 1 (group B corresponds to 1).
|   X = 5 (the "5" in B5).
|   number = group * 8 + X = 1 * 8 + 5 = 13.
|   pin = bank * 32 + number = 4 * 32 + 13 = 141.

**4. Controlling GPIO via the /sys/class/gpio Directory**

|   In Linux, the most common way to read and write GPIO is using the GPIO sysfs interface, which is implemented by operating files such as export, unexport, gpio{N}/direction, and gpio{N}/value (replace {N} with the actual pin number) in the /sys/class/gpio directory. This method is often used in shell scripts.

.. code-block:: shell

    echo 141 > /sys/class/gpio/export       # Enable the GPIO4_B5 pin
    echo out > gpio141/direction              # Set the pin to output mode
    echo 1 > gpio141/value                     # Set the pin to high level
    cat /sys/class/gpio/gpio141/value        # Read the pin value
    echo 141 > /sys/class/gpio/unexport   # Release the GPIO

|   Note: Some GPIOs may fail to be exported because they are multiplexed for other functions (such as UART, I2C). You need to confirm their actual usage through the device tree.

PWM
~~~~~~

**1. PWM Hardware and Driver Framework**

|   On the RK3562 platform, the PWM hardware driver works collaboratively with counters and comparators: 

- The APB bus clock source drives the counter to increment/decrement periodically after being adjusted by a frequency divider, and automatically resets to generate a basic signal when reaching the preset cycle value. 
- The comparator compares the counter value with the duty cycle threshold in real time, outputs high/low levels, and switches between normal (high-active) or inversed (low-active) modes through the polarity control bit. 

|   The user layer controls PWM through the /sys/class/pwm interface or kernel APIs (such as pwm_config). The core layer manages controller resources and registers interfaces through pwm_chip, while the underlying hardware adaptation layer needs to implement the pwm_ops operation set (including config, enable, and other functions) to directly operate PWM registers for frequency, duty cycle, and enable configuration.

**2. PWM Device Tree Configuration**

|   Taking PWM14_M0 as an example, configure the clock and pins in the rk3562.dtsi file:

.. code-block:: shell

    pwm14: pwm@ff720020 {
            compatible = "rockchip,rk3562-pwm", "rockchip,rk3328-pwm";
            reg = <0x0 0xff720020 0x0 0x10>;
            interrupts = <GIC_SPI 26 IRQ_TYPE_LEVEL_HIGH>;
            #pwm-cells = <3>;
            pinctrl-names = "active";
            pinctrl-0 = <&pwm14m0_pins>;
            clocks = <&cru CLK_PWM3_PERI>, <&cru PCLK_PWM3_PERI>;
            clock-names = "pwm", "pclk";
            status = "disabled";
    };

|   Add a node in myzr-rk3562-ek200-lvds-lcd.dtsi:

.. code-block:: shell

    &pwm14 {
        status = "okay";
        pinctrl-names = "active";
        pinctrl-0 = <&pwm14m0_pins>;  // Ensure correct pin multiplexing configuration
    };

|   Add a PWM client device node
|   Reference the PWM controller and set parameters in the device node that needs to use PWM (such as backlight). If no device needs to be used, no configuration is required. The following is a general configuration example:

.. code-block:: shell

    // Example: Configure PWM14_M0 output to a device (e.g., backlight)
    / {
        pwm_dev: pwm-dev {
            compatible = "pwm-device";
            pwms = <&pwm14 0 10000000 1>; // Key parameter settings
            duty-cycle = <5000000>;    // 50% duty cycle
            pinctrl-names = "default";
            pinctrl-0 = <&pwm14m0_pins>;// Ensure consistency with controller configuration
        };
    };

|   Driver Matching: compatible = "pwm-device" triggers the PWM driver corresponding to the compatible string in the kernel. After the driver matches the node through the of_device_id table, it calls the probe function to initialize the hardware.
|   PWM Parameter Transfer: pwms = <&pwm14 0 10000000 1> binds to channel 0 of the pwm14 controller, sets the period to 10ms (10,000,000ns, corresponding to a frequency of 100Hz), and the polarity to 1 (high-level active). duty_ns = 5000000 specifies an initial duty cycle of 5ms (50%), and the driver writes it to the hardware register through pwm_config().
|   Controller Enable: &pwm14 { status = "okay" } enables the PWM14 hardware controller inside the SoC. The underlying driver initializes its clock and reset signal, and maps the physical address of the register to the kernel virtual address.
|   The entire process uses the device tree to directly pass hardware parameters to the driver, realizing PWM waveform output (PWM is initialized and configured to a frequency of 100Hz, a duty cycle of 50%, and inverted polarity).

**3. PWM Operation via Sysfs Interface**

1. Find the PWM Controller Path

|   Enter the command:

.. code-block:: shell

    ls /sys/class/pwm  # Display all PWM controllers, such as pwmchip0, pwmchip1, etc.

|   The PWM controllers of RK3562 are named pwmchip*. You need to confirm the specific number based on the address of &pwm14 in the device tree. Assume pwm14 corresponds to pwmchip3 here.

2. Export the PWM Channel

.. code-block:: shell

    echo 0 > /sys/class/pwm/pwmchip3/export  # Export channel 0 of pwm14

|   After execution, the /sys/class/pwm/pwmchip3/pwm0 directory will be created.

3. Configure the Period and Duty Cycle

|   Enter the command:

.. code-block:: shell

    echo 10000000 > /sys/class/pwm/pwmchip3/pwm0/period     # Set a period of 10ms (100Hz)
    echo 5000000 > /sys/class/pwm/pwmchip3/pwm0/duty_cycle  # Set a duty cycle of 5ms (50%)
    echo 1 > /sys/class/pwm/pwmchip3/pwm0/enable            # Enable PWM output

|   The parameter unit is nanoseconds, and note that the duty cycle cannot exceed the period value.
|   Note: If export or enable fails, check to ensure that the channel is not occupied by other functions such as serial ports.

4. Dynamically Adjust the Duty Cycle

.. code-block:: shell

    echo 7000000 > /sys/class/pwm/pwmchip3/pwm0/duty_cycle  # Adjust to a 70% duty cycle

I2C
~~~~~

**1. Overview of the I2C Subsystem Architecture**

|   On the RK3562 platform, the I2C controller is implemented based on the standard Linux I2C framework, whose core consists of a hardware abstraction layer (adapter driver) and a device driver layer. The hardware layer abstracts the I2C bus controller through i2c_adapter, and the device layer describes slave devices through i2c_client. The two implement driver logic through i2c_driver. The I2C controller of RK3562 supports multi-master mode, clock division (up to 400kHz), and interrupt/DMA transmission. Its physical layer follows the open-drain output characteristic and implements SCL/SDA signals through GPIO multiplexing.

**2. I2C Device Tree Configuration (Taking the GT911 Touch Chip Mounted on I2C1 as an Example)**

|   Open myzr-rk3562-ek200-lvds-lcd.dts for configuration:

.. code-block:: shell

    &i2c1 {
            gt911@5d {
                    status = "okay";
                    compatible = "goodix,gt911";
                    reg = <0x5d>;
                    pinctrl-names = "default";
                    pinctrl-0 = <&gt911_int>;
                    interrupt-parent = <&gpio4>;
                    interrupts = <8 0>;
                    irq-gpios = <&gpio4 RK_PB0 0>;
                    reset-gpios = <&gpio3 RK_PB0 0>;
            };
    };

|   In this node, the kernel matches the driver through the compatible string. For example, the gt9xx.c file in the driver code needs to define the same of_device_id table:

.. code-block:: shell

    static struct of_device_id goodix_ts_dt_ids[] = {
        { .compatible = "goodix,gt9xx" },
        { }
    };

|   The address of the device on the I2C bus (0x14) is obtained by the driver through the i2c_client structure. pinctrl-* references the touch_gpio node to configure the multiplexing function and electrical properties of the GPIO.
|   When the driver matches the device tree (the compatible value matches the driver), the kernel calls the .probe() function. In the probe function, the driver obtains configurations from the device tree, including pin configurations and chip models.
|   After the device is successfully registered on I2C, use the command:

.. code-block:: shell

    i2cdetect -y 1

|   You can see the letter "UU" appearing at address 5d on I2C1, indicating that the device is successfully mounted on I2C.

SPI
~~~~~~

**1. Overview of the Linux SPI Framework**

|   The Linux SPI framework provides a standardized SPI device driver support system for the kernel, whose core consists of SPI Core, controller driver layer, device abstraction layer, and user-space interface. As the core of the framework, SPI Core undertakes bus management, device registration, and maintenance of standard transmission APIs, and realizes dynamic binding between controllers and slave devices through spi_alloc_device() and spi_add_device(). The SPI controller driver related to hardware needs to implement underlying operations such as clock configuration and data transmission, and each controller corresponds to a struct spi_controller instance; while the connected slave devices are described by the struct spi_device structure, which contains parameters such as device address, chip select, and communication mode. The core mechanism of data transmission triggers the transmission callback function implemented by the controller through synchronous/asynchronous interfaces such as spi_sync(), supporting both DMA and interrupt transmission modes. The framework also opens the SPI interface to user space through the /dev/spidev* device node, enabling hardware register operations from the application layer.

**2. SPI Device Tree Configuration (Taking SPI0_M0 as an Example, with MOSI and MISO pins corresponding to pins 17 and 19 on the J9 expansion interface)**

.. code-block:: shell

    &spi0 {
      status = "okay";
      pinctrl-names = "default";
      pinctrl-0 = <&spi0m0_pins>; // Specify the M0 mode pin group
      #address-cells = <1>;
      #size-cells = <0>;

      spidev@0{
          compatible = "spidev";
          reg = <0>;
          spi-max-frequency = <10000000>;// Maximum frequency of 10MHz
      };
    };

|   When the kernel starts, it parses this node and calls the driver code in drivers/spi/spi-rockchip.c to initialize the SPI0 controller, which is registered as /sys/bus/spi/devices/spi0.0. SPI devices are addressed through the Chip Select (CS) signal. #address-cells=1 means the reg attribute corresponds to the CS number (e.g., reg=<0> means using the CS0 line of SPI0). When generating the SPI device, the kernel controls the corresponding GPIO pin to output a low level according to the reg value to activate the target device.
|   After compatible = "spidev" is successfully matched, the kernel is triggered to load drivers/spi/spidev.c and create the device node /dev/spidev0.0. User-mode programs do not need to develop kernel drivers and can directly initiate SPI data transmission requests through system calls such as ioctl(SPI_IOC_MESSAGE) or write(). After the request is received by the spidev driver, the kernel submits the data transmission task to the SPI controller driver (such as the SPI0 controller) through the spi_async() interface. Finally, the hardware controller generates the SCK signal according to the configured clock polarity, rate, and other parameters, sends the data stream through the MOSI pin, and synchronously reads the response data from the MISO pin to complete full-duplex communication.

**3. Debugging Tools**

|   Short-circuit the MOSI and MISO pins of SPI0_M0, and run the SPI test program in the file system:

.. code-block:: shell

    =====> Input:
    ./test_app/spidev_test -D /dev/spidev0.0
    =====> Output:
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

|   This indicates that the SPI function is normal.

UART
~~~~~~

**1. Device Tree Configuration (Taking UART6_M0 as an Example, with pins corresponding to pins 7 and 9 on the J8 expansion interface)**

.. code-block:: shell

    &uart6 {
        status ="okay";
        pinctrl-name = "default";
        pinctrl-0 = <&uart6m0_xfer>;
    };

|   The function of pinctrl-0 = <&uart6m0_xfer> is to bind the TX/RX pins of UART6 to the uart6m0_xfer multiplexing group.
|   uart6m0_xfer has been defined in rk3562-pinctrl.dtsi:

.. code-block:: shell

    uart6m0_xfer: uart6m0-xfer {
            rockchip,pins =
                    /* uart6_rx_m0 */
                    <0 RK_PC7 1 &pcfg_pull_up>,
                  /* uart6_tx_m0 */
                    <0 RK_PC6 1 &pcfg_pull_up>;
    };

|   After the device tree is configured, UART6 is registered as /dev/ttyS6 in the system, which can be verified by running ls /dev/ttyS*.

**2. Debugging Tools**

|   Short-circuit the RX and TX pins of uart6m0, and use the test file placed in the file system/test_app for transceiving tests:

.. code-block:: shell

    =====> Input:
    # ./test_app/serial_test.out /dev/ttyS6 "myzr"
    =====> Output:
    Starting send data...finish
    Starting receive data:
    ASCII: 0x6d          Character: m 
    ASCII: 0x79          Character: y 
    ASCII: 0x7a          Character: z 
    ASCII: 0x72          Character: r 
    ASCII: 0x0           Character: