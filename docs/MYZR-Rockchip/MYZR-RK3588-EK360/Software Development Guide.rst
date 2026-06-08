Software Development Guide
============================

.. include:: /docs/COMMON/MYZR-RK3588-EK360 Dev Env Setup Manual.rst

Linux Source Code Compilation
--------------------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The compilation host must run on an Ubuntu system with version 20.04 or higher. The author's host system is Ubuntu 20.04.
2. The host must have internet access, as the compilation process requires downloading certain files.

Downloading Source Code Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the rk3588 source code package from the path: 3. Software Materials --> 3.1 Source Code --> rk3588-linux.tar.xz
2. Create a compilation directory:

.. code-block:: shell

    mkdir -p ~/my-work/RK3588/02_sources/

3. Place the source code in the newly created directory and extract it:

.. code-block:: shell

    tar xvf rk3588-linux.tar.xz -C ~/my-work/RK3588/02_sources/

Dependency Installation
~~~~~~~~~~~~~~~~~~~~~~~~~

|   First-time compilation may require installing certain dependencies. Below are some dependencies that the host may need:

.. code-block:: shell

    sudo apt-get install uuid uuid-dev zlib1g-dev liblz-dev liblzo2-2 liblzo2-dev lzop \
    git curl u-boot-tools mtd-utils openjdk-8-jdk device-tree-compiler \
    gdisk m4 zlib1g-dev git gnupg flex bison gperf libsdl1.2-dev libesd-java \
    squashfs-tools build-essential zip curl libncurses5-dev zlib1g-dev pngcrush schedtool \
    libxml2 libxml2-utils xsltproc lzop libc6-dev schedtool g++-multilib lib32z1-dev \
    lib32ncurses-dev lib32readline-dev gcc-multilib libswitch-perl libssl-dev unzip \
    zip liblz4-tool git ssh make gcc libssl-dev liblz4-tool vim expect \
    g++ patchelf chrpath gawk texinfo chrpath diffstat binfmt-support \
    qemu-user-static live-build bison flex fakeroot cmake gcc-multilib g++-multilib \
    unzip device-tree-compiler python3-pip libncurses5-dev rsync subversion python-protobuf \
    sed make binutils build-essential gcc g++ wget python-is-python2 libncurses5 bzr cvs git mercurial \
    patch gzip bzip2 perl tar cpio unzip rsync file bc wget qemu-user-static live-build android-sdk-libsparse-utils android-sdk-ext4-utils -y libicu-dev


Overall Compilation
~~~~~~~~~~~~~~~~~~~~~

1. Run the overall compilation (which takes a long time) with the following commands:

buildroot
^^^^^^^^^^^

.. code-block:: shell

    ./build.sh buildroot_update

ubuntu20
^^^^^^^^^^

.. code-block:: shell

    ./build.sh ubuntu20_update

ubuntu22
^^^^^^^^^^

.. code-block:: shell

    ./build.sh ubuntu22_update

debian11
^^^^^^^^^^

.. code-block:: shell

    ./build.sh debian11_update

debian12
^^^^^^^^^^

.. code-block:: shell

    ./build.sh debian12_update

2. After successful compilation, relevant images can be found in the rockdev/ directory, where update.img is a collection of all images.


Compile uboot separately
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear generated files before compilation

.. code-block:: shell

    cd u-boot/
    make clean

2. Return to the SDK main directory and compile uboot separately

.. code-block:: shell

    cd ../
    ./build.sh uboot

Compile the Kernel separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear generated files before compilation

.. code-block:: shell

    cd kernel/
    make clean

2. Return to the SDK main directory and compile kernel separately

.. code-block:: shell

    cd ../
    ./build.sh kernel

Compile recovery separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Enter the following command in the SDK main directory:

.. code-block:: shell

    ./build.sh recovery


Compile rootfs separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Enter the following command in the SDK main directory:

buildroot
^^^^^^^^^^^

.. code-block:: shell

    ./build.sh rootfs

ubantu20
^^^^^^^^^^

.. code-block:: shell

    ./build.sh ubuntu20

ubantu22
^^^^^^^^^^

.. code-block:: shell

    ./build.sh ubuntu22

debian11
^^^^^^^^^^

.. code-block:: shell

    ./build.sh debian11

debian12
^^^^^^^^^^

.. code-block:: shell

    ./build.sh debian12


Package firmware
~~~~~~~~~~~~~~~~~~

|   Enter the following command in the SDK main directory:

.. code-block:: shell

    ./mkfirmware.sh

Package update.img
~~~~~~~~~~~~~~~~~~~~~

1. Package the image into update.img in rockdev
2. Enter the following command in the SDK main directory:

.. code-block:: shell

    ./build.sh updateimg

|   After completing the above operations, you can re-flash the device according to the flashing manual
|   Finally, remind the user that they should re-flash and test the device.


Android Source Code Compilation
---------------------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Compilation must be performed on a host in a Linux environment; Ubuntu 20.04 is recommended.
2. The host must have internet access, as certain files need to be downloaded during system compilation.

Downloading Source Code Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. From the network disk directory, download the source code package MYZR-RK3588-EK360_Android12_20260108.tar.bz2 (please download all split volumes from the network disk and merge them to obtain this archive).
2. Create a compilation directory:

.. code-block:: shell

    mkdir ~/my-work/rk3588/05_android -p

3. Place the source code in this directory and extract it:

.. code-block:: shell

    tar xvf MYZR-RK3588-EK360_Android12_20260108.tar.bz2  -C ~/my-work/rk3588/05_android/

Configure Compilation Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Environment configuration is required every time a new terminal is opened.
2. Enter the 3588-android12 directory.
3. Run the following command to configure the Java environment:

.. code-block:: shell

    source javaenv.sh

4. Run the following command to configure the compilation environment:

.. code-block:: shell

    source build/envsetup.sh

5. Run the following command to configure the platform environment:

.. code-block:: shell

    lunch myzr_rk3588-userdebug

Full Compilation
~~~~~~~~~~~~~~~~~~

1. Full compilation builds the entire Android system, including kernel, u-boot, Android, and recovery.
2. Run the following command:

.. code-block:: shell

    ./build.sh -AUCKu

3. Compilation takes a long time. Compilation on a 16-thread host takes about 4 hours (for reference only!).
4. After successful compilation, the relevant images can be found in the rockdev/Image-myzr_rk3588/ directory, where update.img is the combined image of all components.

Compile U-Boot Separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear generated files before compilation:

.. code-block:: shell

    cd u-boot/
    make clean

2. Return to the SDK root directory and compile U-Boot separately:

.. code-block:: shell

    cd ../
    ./build.sh -U

Compile Kernel Separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clear generated files before compilation:

.. code-block:: shell

    cd kernel/
    make clean

2. Return to the SDK root directory and compile the kernel separately:

.. code-block:: shell

    cd ../
    ./build.sh -CKA

Compile Android Separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In the SDK root directory:

.. code-block:: shell

    ./build.sh -A

Package update.img
~~~~~~~~~~~~~~~~~~~~

1. Package images into update.img in the rockdev directory.
2. In the SDK root directory:

.. code-block:: shell

    ./build.sh -u


Development Guide
-------------------

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

- U-Boot board-level file location: board/myzr/myzr_rk3588
- U-Boot board-level configuration file: include/configs/myzr_rk3588.h
- U-Boot board-level compilation configuration file: configs/myzr_rk3588_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Kernel board-level compilation configuration file: arch/arm64/configs/myzr_linux_defconfig
- Kernel board-level device tree files: arch/arm64/boot/dts/rockchip/myzr-*.dts*
- Kernel development reference manual: 《*Reference Manual*.pdf》 in the network disk


Ethernet
~~~~~~~~~~

|   The development board has two network ports: J13 and J14. J13 is used as an example, and J14 works similarly.
|   Both network ports support connecting to the external network.

1. dts configuration

|   1.1 Common configuration
|   kernel/arch/arm64/boot/dts/rockchip/rk3588.dtsi

.. code-block:: shell

    gmac0: ethernet@fe1b0000 {
        compatible = "rockchip,rk3588-gmac", "snps,dwmac-4.20a";
        reg = <0x0 0xfe1b0000 0x0 0x10000>;
        interrupts = <GIC_SPI 227 IRQ_TYPE_LEVEL_HIGH>,
                 <GIC_SPI 226 IRQ_TYPE_LEVEL_HIGH>;
        interrupt-names = "macirq", "eth_wake_irq";
        rockchip,grf = <&sys_grf>;
        rockchip,php_grf = <&php_grf>;
        clocks = <&cru CLK_GMAC_125M>, <&cru CLK_GMAC_50M>,
             <&cru PCLK_GMAC0>, <&cru ACLK_GMAC0>,
             <&cru CLK_GMAC0_PTP_REF>;
        clock-names = "stmmaceth", "clk_mac_ref",
                  "pclk_mac", "aclk_mac",
                  "ptp_ref";
        resets = <&cru SRST_A_GMAC0>;
        reset-names = "stmmaceth";
        power-domains = <&power RK3588_PD_GMAC>;

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

|   1.2 Board-level configuration
|   kernel/arch/arm64/boot/dts/rockchip/myzr-rk3588-linux.dts

.. code-block:: shell

    //Wired network card configuration
    &gmac0 {
            /* Use rgmii-rxid mode to disable rx delay inside Soc */
            phy-mode = "rgmii-rxid";
            clock_in_out = "output";

            snps,reset-active-low;
            /* Reset time is 20ms, 100ms for rtl8211f */
            snps,reset-delays-us = <0 20000 100000>;

            pinctrl-names = "default";
            pinctrl-0 = <&gmac0_miim
                         &gmac0_tx_bus2
                         &gmac0_rx_bus2
                         &gmac0_rgmii_clk
                         &gmac0_rgmii_bus>;
            tx_delay = <0x44>;
            /* rx_delay = <0x4f>; */

            phy-handle = <&rgmii_phy0>;
            status = "okay";
    };

2. The network port does not automatically obtain an IP

|   Wait or disable the network adapter on your computer that can access the internet, stop sharing to the Ethernet port, re-enable sharing, and then restart the board to automatically obtain an IP.


RTC 使用
~~~~~~~~~~

1. Introduction

|   The MYZR-RK3588-EK360 development board uses HYM8563 as RTC (Real Time Clock). HYM8563 is a low-power CMOS real-time clock/calendar chip. It provides a programmable clock output, an interrupt output, and a power-down detector. All addresses and data are serially transmitted through the I2C bus interface. The maximum bus speed is 400Kbits/s. After each read/write operation, the built-in word address register automatically increments.

- Can time seconds, minutes, hours, days of the week, days, months, and years based on a 32.768kHz crystal
- Wide operating voltage range: 1.0~5.5V
- Low sleep current: typically 0.25μA (VDD = 3.0V, TA = 25°C)
- Internally integrated oscillation capacitor
- Open-drain interrupt pin

2. RTC driver

|   Driver reference: kernel/drivers/rtc/rtc-hym8563.c

3. Interface usage

|   Linux provides three user-space calling interfaces. The corresponding paths on the MYZR-RK3588-EK360 development board are:


- SYSFS interface: /sys/class/rtc/rtc0/
- PROCFS interface: /proc/driver/rtc
- IOCTL interface: /dev/rtc0

4. SYSFS interface

|   You can directly use cat and echo to operate the interfaces under /sys/class/rtc/rtc0/.
|   For example, check the current RTC date and time:

.. code-block:: shell

    root@root:/# date -s "2025-05-7 10:00:00"
    Wed May  7 10:00:00 UTC 2025
    root@root:/# cat /sys/class/rtc/rtc0/time
    10:00:24


5. PROCFS interface

|   Print RTC-related information:

.. code-block:: shell

    root@root:/# cat /proc/driver/rtc
    rtc_time        : 10:03:19
    rtc_date        : 2025-05-07
    alrm_time        : 10:04:00
    alrm_date        : 2025-05-07
    alarm_IRQ        : no
    alrm_pending        : no
    update IRQ enabled        : no
    periodic IRQ enabled        : no
    periodic IRQ frequency        : 1
    max user IRQ frequency        : 64
    24hr                : yes

6. IOCTL interface

|   You can use ioctl to control /dev/rtc0.
|   For detailed usage instructions, please refer to the document kernel/Documentation/admin-guide/rtc.rst.

7. FAQs

|   Q1: The time is not synchronized after the development board is powered on?
|   A1: Check if the RTC battery is properly connected.


GPIO
~~~~~~

1. Introduction

|   GPIO, short for General-Purpose Input/Output, is a type of general-purpose pin that can be dynamically configured and controlled during software operation. All GPIOs are in input mode by default after power-on. They can be set as pull-up or pull-down through software, or as interrupt pins. The drive strength is programmable. The core is to fill the method and parameters of the GPIO bank and call gpiochip_add to register it in the kernel.

2. GPIO pin calculation

|   RK3588 has 6 groups of GPIO banks: GPIO0~GPIO5. Each group is distinguished by numbers A0~A7, B0~B7, C0~C7, D0~D7. The following formula is commonly used to calculate pins:
|   GPIO pin calculation formula: pin = bank * 32 + number
|   GPIO group number calculation formula: number = group * 8 + X
|   The following demonstrates the calculation method for GPIO2_C4 pin:
|   bank = 2;      //GPIO2_C4 => 2, bank ∈ [0,5]
|   group = 2;      //GPIO2_C4 => 2, group ∈ {(A=0), (B=1), (C=2), (D=3)}
|   X = 0;       //GPIO2_C4 => 4, X ∈ [0,7]
|   number = group * 8 + X = 2 * 8 + 4 = 20
|   pin = bank*32 + number= 2 * 32 + 20 = 56;
|   The device tree attribute description corresponding to GPIO2_C4 is: <&gpio2 20 GPIO_ACTIVE_HIGH>. As known from the macro definition in kernel/include/dt-bindings/pinctrl/rockchip.h, GPIO2_C4 can also be described as <&gpio2 RK_PC4 GPIO_ACTIVE_HIGH>.

.. code-block:: shell

    #define RK_PA0          0
    #define RK_PA1          1
    #define RK_PA2          2
    #define RK_PA3          3
    #define RK_PA4          4
    #define RK_PA5          5
    #define RK_PA6          6
    #define RK_PA7          7
    #define RK_PB0          8
    ...

|   When the GPIO2_C4 pin is not multiplexed by other peripherals, we can export this pin for use through export.

3. Interrupt

.. code-block:: shell

    interrupt-parent = <&gpio0>;
    interrupts = <RK_PB0 IRQ_TYPE_LEVEL_LOW>;

|   IRQ_TYPE_LEVEL_LOW means the interrupt is triggered by a low level. The interrupt function can be triggered when the pin receives a low-level signal. It can also be configured as follows:
|   IRQ_TYPE_NONE         //Default value, undefined interrupt trigger type
|   IRQ_TYPE_EDGE_RISING  //Triggered on rising edge
|   IRQ_TYPE_EDGE_FALLING //Triggered on falling edge
|   IRQ_TYPE_EDGE_BOTH    //Triggered on both rising and falling edges
|   IRQ_TYPE_LEVEL_HIGH   //Triggered on high level
|   IRQ_TYPE_LEVEL_LOW    //Triggered on low level

4. Multiplexing

|   This case is for reference only, and the actual hardware interface shall prevail.
|   In addition to general input/output and interrupt functions, GPIO ports may have other multiplexing functions. Taking GPIO2_C4 as an example, there are the following functions:
|   To change the multiplexing of gpio, you can search for the node by entering 4 RK_PA3 in rk3588-linux\kernel\arch\arm64\boot\dts\rockchip\rk3588-vccio3-pinctrl.dtsi, then reference and configure it.

.. code-block:: shell

            /omit-if-no-ref/
            uart0m2_xfer: uart0m2-xfer {
                rockchip,pins =
                    /* uart0_rx_m2 */
                    <4 RK_PA4 10 &pcfg_pull_up>,
                    /* uart0_tx_m2 */
                    <4 RK_PA3 10 &pcfg_pull_up>;
            };

            //485
    &uart0 {
            status = "okay";
            pinctrl-names = "default";
            pinctrl-0 = <&uart0m2_xfer>;
    };

5. GPIO debugging interface

|   The purpose of the Debugfs file system is to provide developers with more kernel data for debugging. GPIO debugging can also use the Debugfs file system to obtain more kernel information. The interface of GPIO in the Debugfs file system is /sys/kernel/debug/gpio. You can read the information of this interface as follows:

.. code-block:: shell

    root@topeet:/# cat sys/kernel/debug/gpio
    gpiochip0: GPIOs 0-31, parent: platform/fd8a0000.gpio, gpio0:
     gpio-15  (                    |vcc-3v3-sd-s0-regula) out lo 

    gpiochip1: GPIOs 32-63, parent: platform/fec20000.gpio, gpio1:
     gpio-43  (                    |vcc3v3-lcd0-n       ) out hi 
     gpio-52  (                    |hp-det              ) in  hi ACTIVE LOW
     gpio-61  (                    |hdmirx-det          ) in  hi ACTIVE LOW

    gpiochip2: GPIOs 64-95, parent: platform/fec30000.gpio, gpio2:
    ...

485
~~~~~

DTS Configuration
^^^^^^^^^^^^^^^^^^^^

|   File path: kernel/arch/arm64/boot/dts/rockchip/myzr-rk3588-linux.dts

.. code-block:: shell

    //485
    &uart0 {
            status = "okay";
            pinctrl-names = "default";
            pinctrl-0 = <&uart0m2_xfer>;
    };

|   After configuring the serial port, the hardware interface corresponds to the node in the software:

.. code-block:: shell

    UART0:   /dev/ttyS0


CAN
~~~~~

1. CAN Introduction


|   CAN (Controller Area Network) bus is a serial communication network that effectively supports distributed control or real-time control. CAN bus is a widely used bus protocol in automobiles, designed for microcontroller communication in the automotive environment. For more information, you can refer to the CAN application report.

2. DTS Node Configuration

- Common configuration: kernel/arch/arm64/boot/dts/rockchip/rk3588s.dtsi

.. code-block:: shell

    can1: can@fea60000 {
        compatible = "rockchip,can-2.0";
        reg = <0x0 0xfea60000 0x0 0x1000>;
        interrupts = <GIC_SPI 342 IRQ_TYPE_LEVEL_HIGH>;
        clocks = <&cru CLK_CAN1>, <&cru PCLK_CAN1>;
        clock-names = "baudclk", "apb_pclk";
        resets = <&cru SRST_CAN1>, <&cru SRST_P_CAN1>;
        reset-names = "can", "can-apb";
        pinctrl-names = "default";
        pinctrl-0 = <&can1m0_pins>;
        tx-fifo-depth = <1>;
        rx-fifo-depth = <6>;
        status = "disabled";
    };

- Board-level configuration: arch/arm64/boot/dts/rockchip/myzr-rk3588-linux.dts

.. code-block:: shell

    //can
    &can1 {
            status = "okay";
            compatible = "rockchip,can-2.0"; //Using can
            pinctrl-0 = <&can1m1_pins>;
            assigned-clocks = <&cru CLK_CAN1>;
            assigned-clock-rates = <100000000>;
    };

3. More Commands

.. code-block:: shell

    1、 ip link set canX down                 //Shut down the can device;
    2、 ip link set canX up                   //Start the can device;
    3、 ip -details link show canX                 //Display detailed information of the can device;
    4、 candump canX                          //Receive data from the can bus;
    5、 ifconfig canX down                         //Shut down the can device for configuration;
    6、 ip link set canX up type can bitrate 250000 //Set can baud rate
    7、 conconfig canX bitrate + baud rate；
    8、 canconfig canX start                 //Start the can device;
    9、 canconfig canX ctrlmode loopback on //Loopback test;
    10、canconfig canX restart                 // Restart the can device;
    11、canconfig canX stop                 //Stop the can device;
    12、canecho canX                         //Check the can device bus status;
    13、cansend canX --identifier=ID+data         //Send data;
    14、candump canX --filter=ID：mask        //Receive data with matching ID using filter

4. Messages are received long after being sent, or not received at all.

|   Check the bus CAN_H and CAN_L, whether the DuPont line is loose or connected in reverse.


HDMI
~~~~~~

1. HDMI Interface Configuration

|   There are two HDMI display output interfaces on the hardware.
|   Enabling the HDMI interface is as follows:

- /rk3588-linux/kernel/arch/arm64/boot/dts/rockchip/myzr-screen-lcds.dts

.. code-block:: shell

    //#define LCD_TYPE_MIPI0  //VP2
    //#define LCD_TYPE_LVDS_10_1_1280x800_GT911  //VP2
    //#define LCD_TYPE_LVDS_10_1_1280x800_GT9271 //VP2
    //#define LCD_TYPE_LVDS_10_1_1024x600_GT911  //VP2
    //#define LCD_TYPE_LVDS_7_0  //VP2
    #define LCD_TYPE_HDMI1  //VP1
    #define LCD_TYPE_HDMI0  //VP0
    //#define LCD_TYPE_TYPEC_DP  //VP1
    //#define LCD_TYPE_MIPI1    //VP3

|   If both HDMI interfaces are connected to screens, dual-screen mirroring is enabled by default.

|   1.1. Software Configuration

.. code-block:: shell

    #if defined(LCD_TYPE_HDMI0)
    //Enable hdmi0 hardware phy
    &hdptxphy_hdmi0 {
            status = "okay";
    };
    //Enable HDMI0
    &hdmi0 {
            enable-gpios = <&gpio4 RK_PB1 GPIO_ACTIVE_HIGH>;
            status = "okay";
    };
    //Configure HDMI0 to VP0
    &hdmi0_in_vp0 {
            status = "okay";
    };
    //Enable HDMI0 sound
    &hdmi0_sound {
            status = "okay";
    };
    //Configure boot logo display on HDMI0
    &route_hdmi0 {
            status = "okay";
    };

    #endif

.. code-block:: shell

    #if defined(LCD_TYPE_HDMI1)
    //Enable HDMI1
    &hdptxphy_hdmi1 {
            status = "okay";
    };
    &hdmi1 {
            enable-gpios = <&gpio4 RK_PA2 GPIO_ACTIVE_HIGH>;
            status = "okay";
    };
    //Configure HDMI1 to VP1
    &hdmi1_in_vp1 {
            status = "okay";
    };
    //Enable HDMI1 sound
    &hdmi1_sound {
            status = "okay";
    };
    //Configure boot logo display on HDMI1
    &route_hdmi1 {
            status = "okay";
    };

    #endif


Watchdog
~~~~~~~~~~

1. Introduction

|   A watchdog is actually a timer that starts counting after being activated. The system or software needs to communicate with the watchdog (commonly known as feeding the dog) within a specified time to reset the counting, and this process is repeated to confirm that the system and software are running normally.
|   If the dog is not fed within the specified time, the watchdog times out, indicating that the system or application is stuck in a loop or has crashed. At this time, the watchdog will send a reset signal to reset the main controller to get out of the crash.

2. DTS Configuration

|   The watchdog DTS node of MYZR-RK3588-EK360 is defined in the file kernel/arch/arm64/boot/dts/rockchip/rk3588s.dtsi, as shown below:

.. code-block:: shell

        wdt: watchdog@feaf0000 {
        compatible = "snps,dw-wdt";
        reg = <0x0 0xfeaf0000 0x0 0x100>;
        clocks = <&cru TCLK_WDT0>, <&cru PCLK_WDT0>;
        clock-names = "tclk", "pclk";
        interrupts = <GIC_SPI 315 IRQ_TYPE_LEVEL_HIGH>;
        status = "okay";
    };

|   The watchdog driver file is kernel/drivers/watchdog/dw_wdt.c.