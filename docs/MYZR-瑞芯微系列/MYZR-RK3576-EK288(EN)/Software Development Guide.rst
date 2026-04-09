Software Development Guide
=============================

.. include:: /docs/COMMON/MYZR-RK3588-EK360 Development Environment.rst


Source Code Compilation
-------------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Compilation must be performed on a host in a Linux environment; Ubuntu 20.04 is recommended.
2. The host must have internet access, as certain files need to be downloaded during system compilation.

Download Source Code Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. From the network disk directory, download the source code package MYZR-RK3576_Android14_20260407.tar.gz (please download all split volumes from the network disk and merge them to obtain this archive).
2. Create a compilation directory:

.. code-block:: shell

    mkdir ~/my-work/rk3576/05_android -p

3. Place the source code in this directory and extract it:

.. code-block:: shell

    tar xvf MYZR-RK3576_Android14_20260407.tar.gz -C ~/my-work/rk3576/05_android/

Configure Compilation Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Environment configuration is required every time a new terminal is opened.
2. Enter the rk3576_android14 directory.
3. Run the following command to configure the Java environment:

.. code-block:: shell

    source javaenv.sh

4. Run the following command to configure the compilation environment:

.. code-block:: shell

    source build/envsetup.sh

5. Run the following command to configure the platform environment:

.. code-block:: shell

    lunch myzr_rk3576-userdebug

|   Or run the compilation script directly in the SDK:

.. code-block:: shell

    ./make_rk3576.sh

Full Compilation
~~~~~~~~~~~~~~~~~~

1. Full compilation builds the entire Android system, including kernel, u-boot, Android, and recovery.
2. Run the following command:

.. code-block:: shell

    ./build.sh -AUCKu

3. Compilation takes a long time. Compilation on a 16-thread host takes about 4 hours (for reference only!).
4. After successful compilation, the relevant images can be found in the rockdev/Image-myzr_rk3576/ directory, where update.img is the combined image of all components.

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

3. Or compile using the kernel script:

.. code-block:: shell

    cd kernel-6.1/
    ./makekernel.sh

Compile Android Separately
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In the SDK root directory:

.. code-block:: shell

    ./build.sh -A

Package update.img
~~~~~~~~~~~~~~~~~~

1. Package images into update.img in the rockdev directory.
2. In the SDK root directory:

.. code-block:: shell

    ./build.sh -u

Development Guide
--------------------

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

- U-Boot board-level file location: board/myzr/myzr_rk3576
- U-Boot board-level configuration file: include/configs/myzr_rk3576.h
- U-Boot board-level compilation configuration file: configs/myzr_rk3576_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Kernel board-level compilation configuration file: arch/arm64/configs/myzr_linux_defconfig
- Kernel board-level device tree file: arch/arm64/boot/dts/rockchip/myzr-*.dts*
- Kernel development reference manual: 《*Reference Manual*.pdf》 in the network disk

Ethernet
~~~~~~~~~~

|   The development board has two network ports: J11 and J12. J11 is used as an example, and J12 is similar.

1. DTS configuration

**1.1 Common configuration**

|   kernel/arch/arm64/boot/dts/rockchip/rk3576.dtsi

.. code-block:: shell

    gmac0: ethernet@2a220000 {
                    compatible = "rockchip,rk3576-gmac", "snps,dwmac-4.20a";
                    reg = <0x0 0x2a220000 0x0 0x10000>;
                    interrupts = <GIC_SPI 293 IRQ_TYPE_LEVEL_HIGH>,
                                 <GIC_SPI 298 IRQ_TYPE_LEVEL_HIGH>;
                    interrupt-names = "macirq", "eth_wake_irq";
                    rockchip,grf = <&sdgmac_grf>;
                    rockchip,php_grf = <&ioc_grf>;
                    clocks = <&cru CLK_GMAC0_125M_SRC>, <&cru CLK_GMAC0_RMII_CRU>,
                             <&cru PCLK_GMAC0>, <&cru ACLK_GMAC0>,
                             <&cru CLK_GMAC0_PTP_REF>;
                    clock-names = "stmmaceth", "clk_mac_ref",
                                  "pclk_mac", "aclk_mac",
                                  "ptp_ref";
                    resets = <&cru SRST_A_GMAC0>;
                    reset-names = "stmmaceth";
                    power-domains = <&power RK3576_PD_SDGMAC>;

                    dma-coherent;
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

                    gmac0_stmmac_axi_setup: stmmac-axi-config {
                            snps,wr_osr_lmt = <4>;
                            snps,rd_osr_lmt = <8>;
                            snps,blen = <0 0 0 0 16 8 4>;
                    };

                    gmac0_mtl_rx_setup: rx-queues-config {
                            snps,rx-queues-to-use = <1>;
                            queue0 {};
                    };

                    gmac0_mtl_tx_setup: tx-queues-config {
                            snps,tx-queues-to-use = <1>;
                            queue0 {};
                    };
            };

**1.2 Board-level configuration**

|   kernel/arch/arm64/boot/dts/rockchip/myzr-rk3576-linux.dts

.. code-block:: shell

    &gmac0 {
        /* Use rgmii-rxid mode to disable rx delay inside Soc */
        phy-mode = "rgmii-rxid";
        clock_in_out = "output";

        snps,reset-gpio = <&gpio2 RK_PB5 GPIO_ACTIVE_LOW>;
        snps,reset-active-low;
        /* Reset time is 20ms, 100ms for rtl8211f */
        snps,reset-delays-us = <0 20000 100000>;

        pinctrl-names = "default";
        pinctrl-0 = <&eth0m0_miim
                 &eth0m0_tx_bus2
                 &eth0m0_rx_bus2
                 &eth0m0_rgmii_clk
                 &eth0m0_rgmii_bus
                 &ethm0_clk0_25m_out>;

        tx_delay = <0x21>;
        /* rx_delay = <0x3f>; */

        phy-handle = <&rgmii_phy0>;
        status = "okay";
    };

2. The network port cannot obtain an IP address automatically

|   Wait, or turn off the sharing of the network adapter that can access the Internet on the computer to the Ethernet port, then re-enable the sharing, and restart the board to automatically obtain an IP address.

RTC Usage
~~~~~~~~~~

1. Introduction

|   The MYZR-RK3576 development board uses HYM8563 as RTC (Real Time Clock). HYM8563 is a low-power CMOS real-time clock/calendar chip. It provides a programmable clock output, an interrupt output and a power-down detector. All addresses and data are serially transmitted through the I2C bus interface. The maximum bus speed is 400Kbits/s. After each data read and write, the embedded word address register will automatically increment.

- It can count seconds, minutes, hours, days of the week, days, months and years based on a 32.768kHz crystal.
- Wide operating voltage range: 1.0~5.5V
- Low sleep current: typical value is 0.25μA (VDD =3.0V, TA =25°C)
- Internally integrated oscillation capacitor
- Open-drain interrupt pin

2. RTC Driver

|   Driver reference: kernel/drivers/rtc/rtc-hym8563.c

3. Interface Usage

|   Linux provides three user-space calling interfaces.

- SYSFS interface: /sys/class/rtc/rtc0/
- PROCFS interface: /proc/driver/rtc
- IOCTL interface: /dev/rtc0

4. SYSFS Interface

|   You can directly use cat and echo to operate the interfaces under /sys/class/rtc/rtc0/.
|   For example, check the current RTC date and time:

.. code-block:: shell

    root@root:/# date -s "2025-05-7 10:00:00"
    Wed May  7 10:00:00 UTC 2025
    root@root:/# cat /sys/class/rtc/rtc0/time
    10:00:24

5. PROCFS Interface

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

6. IOCTL Interface

|   You can use ioctl to control /dev/rtc0.
|   For detailed usage instructions, please refer to the document kernel/Documentation/admin-guide/rtc.rst.

7. FAQs

|   Q1: The time is not synchronized after the development board is powered on?
|   A1: Check whether the RTC battery is correctly connected.

485
~~~~~

DTS Configuration

|   File path: kernel/arch/arm64/boot/dts/rockchip/myzr-rk3576-linux.dts

.. code-block:: shell

    &uart5 {
        status = "okay";
        pinctrl-0 = <&uart5m1_xfer>;
    };

|   After configuring the serial port, the hardware interface corresponds to the node in the software:

.. code-block:: shell

    /dev/ttyS5

CAN
~~~~~

1. CAN Introduction

|   CAN (Controller Area Network) bus is a serial communication network that effectively supports distributed control or real-time control. The CAN bus is a bus protocol widely used in automobiles and is designed for microcontroller communication in the automotive environment.

2. DTS Node Configuration

- Common configuration: kernel/arch/arm64/boot/dts/rockchip/rk3576.dtsi

.. code-block:: shell

    can0: can@2ac00000 {
            compatible = "rockchip,rk3576-canfd";
            reg = <0x0 0x2ac00000 0x0 0x1000>;
            interrupts = <GIC_SPI 121 IRQ_TYPE_LEVEL_HIGH>;
            clocks = <&cru CLK_CAN0>, <&cru HCLK_CAN0>;
            clock-names = "baudclk", "apb_pclk";
            resets = <&cru SRST_CAN0>, <&cru SRST_H_CAN0>;
            reset-names = "can", "can-apb";
            dmas = <&dmac0 20>;
            dma-names = "rx";
            status = "disabled";
    };

- Board-level configuration: arch/arm64/boot/dts/rockchip/myzr-rk3576-linux.dts

.. code-block:: shell

    &can0 {
        status = "okay";
        assigned-clocks = <&cru CLK_CAN0>;
        assigned-clock-rates = <200000000>;
        pinctrl-names = "default";
        pinctrl-0 = <&can0m2_pins>;
    };

3. More Commands

.. code-block:: shell

    1、 ip link set canX down                 //Turn off the CAN device;
    2、 ip link set canX up                   //Turn on the CAN device;
    3、 ip -details link show canX                 //Display detailed information of the CAN device;
    4、 candump canX                          //Receive data from the CAN bus;
    5、 ifconfig canX down                         //Turn off the CAN device for configuration;
    6、 ip link set canX up type can bitrate 250000 //Set the CAN baud rate
    7、 conconfig canX bitrate + baud rate;
    8、 canconfig canX start                 //Start the CAN device;
    9、 canconfig canX ctrlmode loopback on //Loopback test;
    10、canconfig canX restart                 // Restart the CAN device;
    11、canconfig canX stop                 //Stop the CAN device;
    12、canecho canX                         //Check the CAN device bus status;
    13、cansend canX --identifier=ID+data         //Send data;
    14、candump canX --filter=ID:mask        //Receive data with matching ID using filter

4. Messages are received after a long time or not received at all.

|   Check the bus CAN_H and CAN_L, whether the Dupont line is loose or reversed.

GPIO
~~~~~~

1. Introduction

|   GPIO, short for General-Purpose Input/Output, is a type of general-purpose pin that can be dynamically configured and controlled during software operation. All GPIOs are in input mode by default after power-on. They can be set to pull-up or pull-down via software, configured as interrupt pins, and their driving strength is programmable. The core lies in populating the methods and parameters of the GPIO bank and registering it into the kernel by calling gpiochip_add.

2. GPIO Pin Calculation

|   RK3576 has 6 groups of GPIO banks: GPIO0~GPIO5. Each group is numbered A0~A7, B0~B7, C0~C7, D0~D7. The following formulas are commonly used to calculate pins:
|   GPIO pin calculation formula: pin = bank * 32 + number
|   GPIO group number calculation formula: number = group * 8 + X
|   The following demonstrates the calculation method for the GPIO2_C4 pin:
|   bank = 2;      // GPIO2_C4 => 2, bank ∈ [0,5]
|   group = 2;      // GPIO2_C4 => 2, group ∈ {(A=0), (B=1), (C=2), (D=3)}
|   X = 4;       // GPIO2_C4 => 4, X ∈ [0,7]
|   number = group * 8 + X = 2 * 8 + 4 = 20
|   pin = bank * 32 + number = 2 * 32 + 20 = 56;
|   The device tree attribute description corresponding to GPIO2_C4 is <&gpio2 20 GPIO_ACTIVE_HIGH>. As can be seen from the macro definition in kernel/include/dt-bindings/pinctrl/rockchip.h, GPIO2_C4 can also be described as <&gpio2 RK_PC4 GPIO_ACTIVE_HIGH>.

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

|   IRQ_TYPE_LEVEL_LOW means the interrupt is triggered by a low level. When the pin receives a low-level signal, it can trigger the interrupt function. It can also be configured as follows:
|   IRQ_TYPE_NONE         // Default value, no defined interrupt trigger type
|   IRQ_TYPE_EDGE_RISING  // Triggered on rising edge
|   IRQ_TYPE_EDGE_FALLING // Triggered on falling edge
|   IRQ_TYPE_EDGE_BOTH    // Triggered on both rising and falling edges
|   IRQ_TYPE_LEVEL_HIGH   // Triggered by high level
|   IRQ_TYPE_LEVEL_LOW    // Triggered by low level

4. Multiplexing

|   This case is for reference only, and the actual hardware interface shall prevail.
|   In addition to general input/output and interrupt functions, GPIO ports may have other multiplexing functions. To change the multiplexing of GPIO, you can search for nodes by entering 4 RK_PA3 in kernel\arch\arm64\boot\dts\rockchip\rk3576-pinctrl.dtsi, then reference and configure them.

.. code-block:: shell

                    /omit-if-no-ref/
                    uart5m1_xfer: uart5m1-xfer {
                            rockchip,pins =
                                    /* uart5_rx_m1 */
                                    <4 RK_PB1 10 &pcfg_pull_up>,
                                    /* uart5_tx_m1 */
                                    <4 RK_PB0 10 &pcfg_pull_up>;
                    };

    &uart5 {
        status = "okay";
        pinctrl-0 = <&uart5m1_xfer>;
    };

5. GPIO Debug Interface

|   The purpose of the Debugfs file system is to provide developers with more kernel data for easy debugging. Here, GPIO debugging can also use the Debugfs file system to obtain more kernel information. The interface of GPIO in the Debugfs file system is /sys/kernel/debug/gpio, and you can read the information of this interface as follows:

.. code-block:: shell

    root@root:/# cat sys/kernel/debug/gpio
    gpiochip0: GPIOs 0-31, parent: platform/27320000.gpio, gpio0:
     gpio-22  (                    |vcc3v3-lcd0-n       ) out lo 
     gpio-23  (                    |vcc5v0-host         ) out hi 
     gpio-25  (                    |vbus5v0-typec       ) out lo 
     gpio-27  (                    |hp-det              ) in  lo IRQ 

    gpiochip1: GPIOs 32-63, parent: platform/2ae10000.gpio, gpio1:
     gpio-57  (                    |vcc3v3-pcie0        ) out hi 

    gpiochip2: GPIOs 64-95, parent: platform/2ae20000.gpio, gpio2:
     gpio-70  (                    |sbu1-dc             ) out lo 
     gpio-71  (                    |sbu2-dc             ) out lo 
     gpio-72  (                    |enable              ) out hi 
     gpio-73  (                    |spk-con             ) out lo 

    gpiochip3: GPIOs 96-127, parent: platform/2ae30000.gpio, gpio3:
     gpio-126 (                    |hp-con              ) out lo 

    gpiochip4: GPIOs 128-159, parent: platform/2ae40000.gpio, gpio4:

    gpiochip5: GPIOs 509-511, parent: platform/rk806-pinctrl.1.auto, rk806-gpio, can sleep:

485
~~~~~

DTS Configuration
^^^^^^^^^^^^^^^^^^^

|   File path: kernel/arch/arm64/boot/dts/rockchip/myzr-rk3576-linux.dts

.. code-block:: shell

    &uart5 {
        status = "okay";
        pinctrl-0 = <&uart5m1_xfer>;
    };

|   After configuring the serial port, the hardware interface corresponds to the following node in software:

.. code-block:: shell

    UART0:   /dev/ttyS5

CAN
~~~~~

1. CAN Introduction

|   CAN (Controller Area Network) bus is a serial communication network that effectively supports distributed control or real-time control. CAN bus is a bus protocol widely used in automobiles and is designed for microcontroller communication in the automotive environment.

2. DTS Node Configuration

- Public configuration: kernel/arch/arm64/boot/dts/rockchip/rk3576.dtsi

.. code-block:: shell

    can0: can@2ac00000 {
            compatible = "rockchip,rk3576-canfd";
            reg = <0x0 0x2ac00000 0x0 0x1000>;
            interrupts = <GIC_SPI 121 IRQ_TYPE_LEVEL_HIGH>;
            clocks = <&cru CLK_CAN0>, <&cru HCLK_CAN0>;
            clock-names = "baudclk", "apb_pclk";
            resets = <&cru SRST_CAN0>, <&cru SRST_H_CAN0>;
            reset-names = "can", "can-apb";
            dmas = <&dmac0 20>;
            dma-names = "rx";
            status = "disabled";
    };

- Board-level configuration: kernel/arch/arm64/boot/dts/rockchip/myzr-rk3576-linux.dts

.. code-block:: shell

    &can0 {
        status = "okay";
        assigned-clocks = <&cru CLK_CAN0>;
        assigned-clock-rates = <200000000>;
        pinctrl-names = "default";
        pinctrl-0 = <&can0m2_pins>;
    };

3. More Commands

.. code-block:: shell

    1、 ip link set canX down                 // Turn off the CAN device;
    2、 ip link set canX up                   // Turn on the CAN device;
    3、 ip -details link show canX            // Display detailed information of the CAN device;
    4、 candump canX                          // Receive data from the CAN bus;
    5、 ifconfig canX down                    // Turn off the CAN device for configuration;
    6、 ip link set canX up type can bitrate 250000 // Set the CAN baud rate;
    7、 canconfig canX bitrate + baud rate;
    8、 canconfig canX start                  // Start the CAN device;
    9、 canconfig canX ctrlmode loopback on   // Loopback test;
    10、canconfig canX restart                // Restart the CAN device;
    11、canconfig canX stop                   // Stop the CAN device;
    12、canecho canX                          // Check the CAN bus status;
    13、cansend canX --identifier=ID+data     // Send data;
    14、candump canX --filter=ID:mask         // Receive data with matching ID using filter


4. It takes a long time to receive the message after sending, or the message cannot be received.

|   Check the CAN_H and CAN_L of the bus to see if the Dupont wires are loose or reversed.

HDMI
~~~~~~

HDMI Interface Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- kernel/arch/arm64/boot/dts/rockchip/myzr-screen-lcds.dts

.. code-block:: shell

    #define LCD_TYPE_HDMI  //VP0
    //#define LCD_TYPE_MIPI0  //VP1
    // #define LCD_TYPE_LVDS_7_0  //VP1

.. code-block:: shell

    #if defined(LCD_TYPE_HDMI)
    //HDMI configuration
    &vp0 {
        status = "okay";
    };

    &hdmi {
        status = "okay";
        enable-gpios = <&gpio2 RK_PB0 GPIO_ACTIVE_HIGH>;
        rockchip,sda-falling-delay-ns = <360>;
    };

    &hdmi_in_vp0 {
        status = "okay";
    };

    &hdptxphy_hdmi {
        status = "okay";
    };

    &hdmi_sound {
        status = "okay";
    };

    &route_hdmi {
        status = "okay";
        connect = <&vp0_out_hdmi>;
    };

    &display_subsystem {
        clocks = <&hdptxphy_hdmi>;
        clock-names = "hdmi0_phy_pll";
    };
    #endif