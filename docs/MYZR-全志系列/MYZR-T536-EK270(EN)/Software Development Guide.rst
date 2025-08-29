Software Development Guide
=============================

.. include:: /docs/COMMON/MYZR-RK3588-EK360 Development Environment.rst

Source Code Compilation
-------------------------

Compilation Environment Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The compilation host must run on the Ubuntu system, with a version of **Ubuntu 22.04 or higher**. The author's host system is Ubuntu 22.04.

Dependency Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  For the first compilation, you may need to install certain dependencies. The following are the dependencies that the host may need to install:

.. code-block:: shell

  sudo apt-get install build-essential subversion git-core libncurses5-dev zlib1g-dev gawk flex quilt libssl-dev xsltproc \
  libxml-parser-perl mercurial bzr ecj cvs unzip lib32z1 lib32z1-dev lib32stdc++6 libstdc++6 libc6:i386 libstdc++6:i386 \
  lib32ncurses-dev lib32z1 ncurses-term bison libexpat1-dev -y

Full Compilation
~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

  ./build.sh config

.. code-block:: shell

  All available platform:
     0. android
     1. linux
  Choice [linux]: 1
  All available linux_dev:
     0. bsp
     1. ubuntu
     2. buildroot
  Choice [buildroot]: 2
  All available ic:
     0. t536
  Choice [t536]: 0
  All available board:
     0. demo
     1. demo_amp
     2. demo_kylo
     3. demo_nand
     4. demo_nor
     5. demo_raw_nand
     6. myzr_t536
  Choice [myzr_t536]: 6
  All available flash:
     0. default
     1. nor
  Choice [default]: 0
  All available kern_name:
     0. linux-5.10-euler
     1. linux-5.10-origin
     2. linux-5.10-rt
     3. linux-5.10-xenomai
     4. linux-5.15-origin
  Choice [linux-5.10-origin]: 1
  ./build.sh
  ./build.sh pack

Individual Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~

|  Compile bootloader individually

.. code-block:: shell

  ./build.sh bootloader

|  Compile kernel individually

.. code-block:: shell

  ./build.sh kernel

|  Compile buildroot rootfs individually

.. code-block:: shell

  ./build.sh buildroot_rootfs

|  Packaging

.. code-block:: shell

  ./build.sh pack

More Compilation Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

  source build/envsetup.sh

Location of Compiled Images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

  out/t536_linux_demo_uart0_linux-5.10-origin.img


Development Guide
--------------------

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Location of U-Boot board-level files: brandy/brandy-2.0/u-boot-bsp/board/sunxi
- U-Boot board-level configuration files: brandy/brandy-2.0/u-boot-bsp/include/configs/
- U-Boot core compilation configuration file: brandy/brandy-2.0/u-boot-bsp/configs/sun55iw6p1_t536_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Kernel board-level compilation configuration file: device/config/chips/t536/configs/myzr_t536/linux-5.10-origin/buildroot_linux_defconfig
- Kernel board-level device tree file: device/config/chips/t536/configs/myzr_t536/linux-5.10-origin/board.dts
- Kernel development reference manual: *Reference Manual*.pdf in the network disk

Ethernet
~~~~~~~~~~

|  The development board has two Ethernet ports: J11 and J12. The following description takes J11 as an example, and the same applies to J12.

1. DTS Configuration

|  1.1 Common configuration
|  kernel/arch/arm64/boot/dts/rockchip/rk3576.dtsi

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

|  1.2 Board-level configuration
|  kernel/arch/arm64/boot/dts/rockchip/myzr-rk3576-linux.dts

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

2. Ethernet Port Fails to Obtain IP Automatically

|  Wait for a moment, or disable the network sharing of the network adapter on your computer that has internet access to the Ethernet port, then re-enable sharing. Restart the board, and it will be able to obtain an IP address automatically.

RTC Usage
~~~~~~~~~~

1. Overview

|  The MYZR-RK3576 development board uses HYM8563 as the RTC (Real Time Clock). HYM8563 is a low-power CMOS real-time clock/calendar chip. It provides a programmable clock output, an interrupt output, and a power-fail detector. All addresses and data are transmitted serially through the I2C bus interface. The maximum bus speed is 400Kbits/s. After each data read/write operation, the built-in word address register increments automatically.

- Capable of timing seconds, minutes, hours, weekdays, days, months, and years based on a 32.768kHz crystal
- Wide operating voltage range: 1.0~5.5V
- Low sleep current: typical value of 0.25μA (VDD = 3.0V, TA = 25°C)
- Internally integrated oscillation capacitor
- Open-drain interrupt pin

2. RTC Driver

|  Driver reference: kernel/drivers/rtc/rtc-hym8563.c

3. Interface Usage

|  Linux provides three user-space calling interfaces.

- SYSFS interface: /sys/class/rtc/rtc0/
- PROCFS interface: /proc/driver/rtc
- IOCTL interface: /dev/rtc0

4. SYSFS Interface

|  You can directly use `cat` and `echo` to operate the interfaces under /sys/class/rtc/rtc0/.
|  For example, to view the current date and time of the RTC:

.. code-block:: shell

  root@root:/# date -s "2025-05-7 10:00:00"
  Wed May  7 10:00:00 UTC 2025
  root@root:/# cat /sys/class/rtc/rtc0/time
  10:00:24

5. PROCFS Interface

|  Print RTC-related information:

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

|  You can use `ioctl` to control /dev/rtc0.
|  For detailed usage instructions, please refer to the document kernel/Documentation/admin-guide/rtc.rst.

7. FAQs

**Q1: The time is not synchronized after the development board is powered on?**

|  A1: Check whether the RTC battery is properly connected.

485
~~~~~

DTS Configuration
^^^^^^^^^^^^^^^^^^^^

|  File path: kernel/arch/arm64/boot/dts/rockchip/myzr-rk3576-linux.dts

.. code-block:: shell

  &uart5 {
      status = "okay";
      pinctrl-0 = <&uart5m1_xfer>;
  };

|  After configuring the serial port, the software node corresponding to the hardware interface is:

.. code-block:: shell

  /dev/ttyS5

CAN
~~~~~~

1. CAN Overview

|  CAN (Controller Area Network) bus is a serial communication network that effectively supports distributed control or real-time control. It is a bus protocol widely used in automobiles and is designed for microcontroller communication in the automotive environment.

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

  1、 ip link set canX down                 // Disable the CAN device;
  2、 ip link set canX up                   // Enable the CAN device;
  3、 ip -details link show canX            // Display detailed information about the CAN device;
  4、 candump canX                          // Receive data from the CAN bus;
  5、 ifconfig canX down                    // Disable the CAN device for configuration;
  6、 ip link set canX up type can bitrate 250000 // Set the CAN baud rate;
  7、 canconfig canX bitrate + baud_rate;    // Set the CAN baud rate (alternative command);
  8、 canconfig canX start                 // Start the CAN device;
  9、 canconfig canX ctrlmode loopback on   // Perform loopback test;
  10、canconfig canX restart                // Restart the CAN device;
  11、canconfig canX stop                   // Stop the CAN device;
  12、canecho canX                          // Check the CAN bus status;
  13、cansend canX --identifier=ID+data     // Send data;
  14、candump canX --filter=ID:mask         // Receive data matching the ID using a filter;

4. Data is Received After a Long Delay or Not Received at All After Message Transmission

|  Check the CAN_H and CAN_L lines of the bus to see if the Dupont wires are loose or reversed.

GPIO
~~~~~~

1. Overview

|  GPIO, short for General-Purpose Input/Output, is a type of general-purpose pin that can be dynamically configured and controlled during software operation. All GPIOs are in input mode by default after power-on. They can be set to pull-up or pull-down via software, configured as interrupt pins, and their drive strength is programmable. The core operation involves populating the methods and parameters of the GPIO bank and calling `gpiochip_add` to register it with the kernel.

2. GPIO Pin Calculation

|  The RK3576 has 6 groups of GPIO banks: GPIO0~GPIO5. Each group is further identified by numbers A0~A7, B0~B7, C0~C7, and D0~D7. The following formulas are commonly used to calculate pins:
|  GPIO pin calculation formula: pin = bank * 32 + number
|  GPIO group number calculation formula: number = group * 8 + X
|  The following demonstrates the calculation method for the GPIO2_C4 pin:
|  bank = 2;      // GPIO2_C4 => 2, bank ∈ [0,5]
|  group = 2;      // GPIO2_C4 => 2, group ∈ {(A=0), (B=1), (C=2), (D=3)}
|  X = 4;          // GPIO2_C4 => 4, X ∈ [0,7]
|  number = group * 8 + X = 2 * 8 + 4 = 20
|  pin = bank * 32 + number = 2 * 32 + 20 = 56;
|  The device tree attribute description corresponding to GPIO2_C4 is: <&gpio2 20 GPIO_ACTIVE_HIGH>. As defined by the macros in kernel/include/dt-bindings/pinctrl/rockchip.h, GPIO2_C4 can also be described as <&gpio2 RK_PC4 GPIO_ACTIVE_HIGH>.

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

|  When the GPIO2_C4 pin is not multiplexed by other peripherals, we can export this pin for use via `export`.

3. Interrupt

.. code-block:: shell

  interrupt-parent = <&gpio0>;
  interrupts = <RK_PB0 IRQ_TYPE_LEVEL_LOW>;

|  `IRQ_TYPE_LEVEL_LOW` indicates that the interrupt is triggered by a low level. The interrupt function can be triggered when the pin receives a low-level signal. It can also be configured as follows:
|  IRQ_TYPE_NONE         // Default value, no defined interrupt trigger type
|  IRQ_TYPE_EDGE_RISING  // Triggered on rising edge
|  IRQ_TYPE_EDGE_FALLING // Triggered on falling edge
|  IRQ_TYPE_EDGE_BOTH    // Triggered on both rising and falling edges
|  IRQ_TYPE_LEVEL_HIGH   // Triggered by high level
|  IRQ_TYPE_LEVEL_LOW    // Triggered by low level

4. Multiplexing

|  This case is for reference only; the final configuration shall be based on the actual hardware interface.
|  In addition to general input/output and interrupt functions, GPIO pins may have other multiplexing functions. To change the multiplexing of a GPIO, you can refer to kernel\arch\arm64\boot\dts\rockchip\rk3576-pinctrl.dtsi.
|  Search for the node by entering 4 RK_PA3, then reference and configure it.

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

|  The purpose of the Debugfs file system is to provide developers with more kernel data for debugging. Debugging of GPIOs can also use the Debugfs file system to obtain more kernel information. The interface of GPIO in the Debugfs file system is /sys/kernel/debug/gpio, and you can read information from this interface as follows:

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


HDMI
~~~~~~

HDMI Interface Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- kernel/arch/arm64/boot/dts/rockchip/myzr-screen-lcds.dts

.. code-block:: shell

  #define LCD_TYPE_HDMI  // VP0
  //#define LCD_TYPE_MIPI0  // VP1
  // #define LCD_TYPE_LVDS_7_0  // VP1

.. code-block:: shell

  #if defined(LCD_TYPE_HDMI)
  // HDMI Configuration
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