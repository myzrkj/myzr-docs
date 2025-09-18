Software Development Guide
============================

.. include:: /docs/COMMON/MYZR-RK3588-EK360 Development Environment.rst


Source Code Compilation
-------------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The compilation host must run on the Ubuntu system, with a version of Ubuntu 20.04 or higher. The author's host system is Ubuntu 20.04.
2. The host must be connected to the external network because some files need to be downloaded during the system compilation process.

Downloading the Source Code Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the rk3568 source code package from the path: 3. Software Materials --> 3.1 Source Code --> MYZR-RK3568pi_Linux-4.19_20250417.tar.bz
2. Create a compilation directory:

.. code-block:: shell

    mkdir -p ~/my-work/RK3568/02_sources/

3. Place the source code in the newly created directory and decompress it:

.. code-block:: shell

    tar xvf MYZR-RK3568pi_Linux-4.19_20250417.tar.bz -C ~/my-work/RK3568/02_sources/

Dependency Installation
~~~~~~~~~~~~~~~~~~~~~~~~~

   For the first compilation, some dependencies may need to be installed. The following are some dependencies that the host may need to install:

.. code-block:: shell

    sudo apt-get install git ssh make gcc libssl-dev liblz4-tool \
    expect g++ patchelf chrpath gawk texinfo chrpath diffstat binfmt-support \
    qemu-user-static live-build bison flex fakeroot cmake gcc-multilib g++-multilib \
    unzip \
    device-tree-compiler libncurses-dev \
    time python3 rsync python-is-python3

SDK Configuration Loading
~~~~~~~~~~~~~~~~~~~~~~~~~~~

   For the first compilation, you need to load the SDK configuration file. Enter the RK356X_Linux directory and enter the following command to load the configuration file:

.. code-block:: shell

    cd RK356X_Linux
    ./build.sh BoardConfig-rk3568-myzr.mk

Overall Compilation
~~~~~~~~~~~~~~~~~~~~~

1. Run the overall compilation (the compilation time is relatively long) by entering the following command:

.. code-block:: shell

    ./build.sh

2. After successful compilation, you can see the relevant images in the rockdev/ directory, where update.img is a collection of all images.


Compiling U-Boot Separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. You can clear the generated files before compilation.

.. code-block:: shell

    cd u-boot/
    make clean

2. Return to the SDK main directory and compile U-Boot separately.

.. code-block:: shell

    cd ../
    ./build.sh uboot

Compiling Kernel Separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. You can clear the generated files before compilation.

.. code-block:: shell

    cd kernel/
    make clean

2. Return to the SDK main directory and compile the kernel separately.

.. code-block:: shell

    cd ../
    ./build.sh kernel

Compiling Recovery Separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Enter the following command in the SDK main directory:

.. code-block:: shell

    ./build.sh recovery

Compiling Buildroot Separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Enter the following command in the SDK main directory:

.. code-block:: shell

    ./build.sh rootfs

Packaging Firmware
~~~~~~~~~~~~~~~~~~~~

   Enter the following command in the SDK main directory:

.. code-block:: shell

    ./mkfirmware.sh

Packaging update.img
~~~~~~~~~~~~~~~~~~~~~~

1. In the rockdev directory under the SDK, you can see the packaged image update.img.
2. Enter the following command in the SDK main directory to complete the image packaging:

.. code-block:: shell

    ./build.sh updateimg

   After completing the above operations, you can re-flash the device according to the flashing manual.
   Finally, it is prompted that the user should re-flash and test.


Development Guide
-------------------

UBOOT Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~

   The location of U-Boot board-level files: u-boot/board/rockchip/myzr_rk3568
   U-Boot board-level configuration file: u-boot/include/configs/myzr_rk3568.h
   U-Boot board-level compilation configuration file: u-boot/configs/myzr-rk3568_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   Kernel board-level compilation configuration file: kernel/arch/arm64/configs/myzr_rk_defconfig
   Kernel board-level device tree files: kernel/arch/arm64/boot/dts/rockchip/myzr*.dts
   Kernel development reference manual: "Reference Manual.pdf" in the network disk

GPIO
~~~~~

1. GPIO Driver Architecture

   The GPIO function of RK3568 is implemented through a three-level architecture: The hardware layer is directly managed by the chip's built-in 5 groups of GPIO controllers (corresponding to device nodes gpiochip0~4) for 32 pins in each group, and the manufacturer has provided the underlying register driver; The kernel layer abstracts hardware differences through the Linux GPIO subsystem and provides standard APIs (such as gpiod interfaces) upward, allowing kernel drivers to operate any pin in a unified way (such as setting direction, reading and writing levels); The user layer imports the GPIO subsystem interface into user space with the help of the Sysfs module (/sys/class/gpio), enabling direct control of pins through the command line (exporting, direction configuration, level reading and writing) without writing code. In the entire mechanism, the hardware driver is completed by the chip manufacturer, the Linux kernel implements general abstraction, and developers can either control GPIO based on kernel API programming or quickly debug through Sysfs.
   Here, let's talk about how to directly control GPIO (direction/level) through the command line at the user layer.

2. Pin Naming Rules

   The GPIO of RK3568 is divided into 5 groups (GPIO0~GPIO4), and each group contains 32 pins: A0-A7, B0-B7, C0-C7, D0-D7. For example:

- GPIO4_D5 indicates the 5th pin of group D in the 4th group (GPIO4).
- GPIO0_B7 indicates the 7th pin of group B in the 0th group (GPIO0).

3. Calculation Formula for GPIO Pin Number

.. code-block:: shell

    pin = bank * 32 + number

   bank: GPIO group number (0~4).
   number: intra-group number, calculated by the following formula:

.. code-block:: shell

    number = group * 8 + X

   group: the intra-group sequence number corresponding to the letter (A=0, B=1, C=2, D=3).
   X: the specific number within the group (0~7).
   For example, GPIO4_D5:
   bank = 4 (GPIO4).
   group = 3 (group D corresponds to 3).
   X = 5 (the 5 in D5).
   number = 3*8 +5 = 29.
   pin = 4*32 +29 = 157.

4. Controlling GPIO through the /sys/class/gpio Directory

.. code-block:: shell

    echo 157 > /sys/class/gpio/export     # Export GPIO157
    echo out > gpio157/direction          # Set to output mode
    echo 1 > gpio157/value                # Output high level
    echo 157 > /sys/class/gpio/unexport   # Release GPIO

   Note: Some GPIOs cannot be exported may be multiplexed for other functions (such as UART, I2C), so you need to confirm the actual use through the device tree.

PWM
~~~~~

1. PWM Hardware and Driver Framework

   On the RK3568 platform, the PWM hardware driver works together through counters and comparators: The APB bus clock source is adjusted by a frequency divider to drive the counter to increment/decrement periodically, and automatically resets to generate a basic signal after reaching the preset period value; The comparator compares the counter value with the duty cycle threshold in real-time, outputs high and low levels, and switches between normal (high active) or inversed (low active) modes through the polarity control bit. The user layer controls through the /sys/class/pwm interface or kernel API (such as pwm_config). The core layer manages controller resources and registers interfaces through pwm_chip, and the underlying hardware adaptation layer needs to implement the pwm_ops operation set (including config, enable and other functions) to directly operate PWM registers to complete frequency, duty cycle and enable configuration.

2. PWM Device Tree Configuration (taking PWM14_M0 as an example, corresponding to pin 12 on the J14 expansion interface)

   Configure the clock and pins in the rk3568.dtsi file:

.. code-block:: shell

    pwm14: pwm@fe700020 {
            compatible = "rockchip,rk3568-pwm", "rockchip,rk3328-pwm";
            reg = <0x0 0xfe700020 0x0 0x10>;
            #pwm-cells = <3>;
            pinctrl-names = "active";
            pinctrl-0 = <&pwm14m0_pins>;
            clocks = <&cru CLK_PWM3>, <&cru PCLK_PWM3>;
            clock-names = "pwm", "pclk";
            status = "disabled";
    };

   Add a node in myzr-rk3568.dtsi:

.. code-block:: shell

    &pwm14 {
        status = "okay";
        pinctrl-names = "active";
        pinctrl-0 = <&pwm14m0_pins>;  // Ensure the pin multiplexing configuration is correct
    };

   Add a PWM client device node.
   Reference the PWM controller and set parameters in the device node that needs to use PWM (such as backlight, buzzer, etc.) (If the device is not needed, no configuration is required). The following is a general configuration example:

.. code-block:: shell

    // Example: Configure PWM14_M0 output to a device (such as backlight)
    / {
        pwm_dev: pwm-dev {
            compatible = "pwm-device";
            pwms = <&pwm14 0 10000000 1>; // Key parameter settings
            duty-cycle = <5000000>;    // 50% duty cycle
            pinctrl-names = "default";
            pinctrl-0 = <&pwm14m0_pins>;// Ensure consistency with the controller configuration
        };
    };

   Driver matching: compatible = "pwm-device" triggers the PWM driver corresponding to compatible in the kernel. After the driver matches the node through the of_device_id table, it calls the probe function to initialize the hardware.
   PWM parameter transmission: pwms = <&pwm14 0 10000000 1> binds channel 0 of the pwm14 controller, sets the period to 10ms (10000000ns, corresponding to 100Hz frequency), and the polarity to 1 (high level active).
   duty_ns = 5000000 specifies the initial duty cycle as 5ms (50% duty cycle), and the driver writes to the hardware register through pwm_config().
   Controller enabling: &pwm14 { status="okay" } enables the PWM14 hardware controller inside the SoC. The underlying driver will initialize its clock and reset signal, and map the physical address of the register to the kernel virtual address.
   The entire process transmits hardware parameters directly to the driver through the device tree to realize PWM waveform output (PWM is initialized and configured to a frequency of 100Hz, a duty cycle of 50%, and inverted polarity).

3. Operating PWM through Sysfs Interface

1. Find the PWM controller path

   Enter the command:

.. code-block:: shell

    ls /sys/class/pwm  # Display all PWM controllers, such as pwmchip0, pwmchip1, etc.

   The PWM controllers of RK3568 are named pwmchip*. You need to confirm the specific number according to the address of &pwm14 in the device tree. Here, it is assumed that pwm14 corresponds to pwmchip3.

2. Export the PWM channel

.. code-block:: shell

    echo 0 > /sys/class/pwm/pwmchip3/export  # Export channel 0 of pwm14

   After execution, the /sys/class/pwm/pwmchip3/pwm0 directory will be generated.

3. Configure the period and duty cycle

   Enter the command:

.. code-block:: shell

    echo 10000000 > /sys/class/pwm/pwmchip3/pwm0/period    # Set a 10ms period (100Hz)
    echo 5000000 > /sys/class/pwm/pwmchip3/pwm0/duty_cycle  # Set a 5ms duty cycle (50%)
    echo 1 > /sys/class/pwm/pwmchip3/pwm0/enable            # Enable PWM output

   The parameter unit is nanoseconds, and note that the duty cycle cannot exceed the period value.
   Note: If exporting or enabling fails, you need to check to determine whether the channel is occupied by other functions such as the serial port.

4. Dynamically adjust the duty cycle

.. code-block:: shell

    # Adjust to 70% duty cycle

UART
~~~~~~

1. Device Tree Configuration (taking UART3_M1 as an example, corresponding to pins 33 and 35 on the J14 expansion interface)

.. code-block:: shell

    &uart3 {
        status ="okay"; 
        pinctrl-name = "default"; 
        pinctrl-0 = <&uart3m1_xfer>; 
    };

   The role of pinctrl-0 = <&uart3m1_xfer> is to bind the TX/RX pins of UART3 to the uart3m1_xfer multiplexing group.
   uart3m1_xfer has been defined in rk3568-pinctrl.dtsi:

.. code-block:: shell

    uart3m1_xfer: uart3m1-xfer {
        rockchip,pins =
            /* uart3_rxm1 */
            <3 RK_PC0 4 &pcfg_pull_up>,
            /* uart3_txm1 */
            <3 RK_PB7 4 &pcfg_pull_up>;
    };

   After the device tree is configured, UART3 is registered as /dev/ttyS3 in the system, which can be verified by ls /dev/ttyS*.

2. Debugging Tools

   Short-circuit the rx and tx of uart3m1, and use the test file placed in the file system for transceiver testing:

.. code-block:: shell

    =====> Input:
    # /my-demo/serial_test.out /dev/ttyS3 "myzr"
    =====> Output:
    Starting send data...finish
    Starting receive data:
    ASCII: 0x6d      Character: m
    ASCII: 0x79      Character: y
    ASCII: 0x7a      Character: z
    ASCII: 0x72      Character: r
    ASCII: 0x0   Character:

I2C
~~~~~

1. Overview of I2C Subsystem Architecture

   In the RK3568 platform, the I2C controller is implemented based on the standard Linux I2C framework, and its core is divided into a hardware abstraction layer (adapter driver) and a device driver layer. The hardware layer abstracts the I2C bus controller through i2c_adapter, and the device layer describes the slave device through i2c_client. Both implement the driver logic through i2c_driver. The I2C controller of RK3568 supports multi-master mode, clock frequency division (up to 400kHz), and interrupt/DMA transmission. Its physical layer follows the open-drain output characteristic and realizes SCL/SDA signals through GPIO multiplexing.

2. I2C Device Tree Configuration (taking a touch chip mounted on I2C1 as an example)

.. code-block:: shell

    &i2c1 {
        status = "okay";

        gt1x: gt1x@14 {
            compatible = "goodix,gt1x";
            reg = <0x14>;
            pinctrl-names = "default";
            pinctrl-0 = <&touch_gpio>;
            goodix,rst-gpio = <&gpio0 RK_PB6 GPIO_ACTIVE_HIGH>;
            goodix,irq-gpio = <&gpio0 RK_PB5 IRQ_TYPE_LEVEL_LOW>;
        };
    };

   In this node, the kernel matches the driver through the compatible string. For example, the same of_device_id table must be defined in the driver code:

.. code-block:: shell

    static const struct of_device_id gt1x_of_match[] = {
        { .compatible = "goodix,gt1x" },
        {}
    };

   The