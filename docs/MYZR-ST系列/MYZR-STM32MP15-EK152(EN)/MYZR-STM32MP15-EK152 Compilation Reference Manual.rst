MYZR-STM32MP15-EK152 Compilation Reference Manual
===================================================

Cross-Compilation Toolchain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| When we want to compile the source code or the source code modified by ourselves, the first step to take is to configure the corresponding cross-compilation toolchain. For this set of source code, we base our compilation on the cross-compilation toolchain provided by ST's official SDK.

Download and Installation of the Compilation Toolchain
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Download:**

| The cross-compilation toolchain must be downloaded from the network disk we provide, and its corresponding network disk directory is **03_Compilation_Tools**. After downloading it to your computer, you need to copy it to the virtual machine via Samba or other methods.

| We can create a dedicated directory for stm32mp157a to store related source code, compilation tools, and other items that will be used later. For example, my directory is: **/home/kuangwh/my-work/stm32mp1** , and under this directory, I have created 4 subdirectories:

.. code-block:: shell

   =====> Input:
   $ ls
   01_image  02_sources  03_sdk  04_app

| The 01 directory can be used to place the compiled images (details will be provided when used later)

| The 02 directory is used to place the source code

| The 03 directory is used to place the cross-compilation toolchain we just downloaded

| The 04 directory can be used to place our own apps (allocated by users themselves)

| After placing the toolchain in the 03 directory, proceed to install the toolchain.

**Installation:**

| Run this toolchain script in the 03 directory and enter the following command:

.. code-block:: shell
   
   =====> Input:
   $ ./st-image-weston-openstlinux-weston-stm32mp1-x86_64-toolchain-3.1-openstlinux-5.4-dunfell-mp1-20-06-24.sh

| Enter the installation directory: /home/kuangwh/my-work/stm32mp1/03_sdk/

.. code-block:: shell
   
   ST OpenSTLinux - Weston - (A Yocto Project Based Distro) SDK installer version 3.1-openstlinux-5.4-dunfell-mp1-20-06-24
   =======================================================================================================================
   Enter target directory for SDK (default: /opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-mp1-20-06-24): /home/kuangwh/my-work/stm32mp1/03_sdk/

| Enter "y"

.. code-block:: shell
   
   You are about to install the SDK to "/home/kuangwh/my-work/stm32mp1/03_sdk". Proceed [Y/n]? y

| The installation process requires patience. Wait until the "successfully installed" message appears.

.. code-block:: shell

   =====> Output:
   Extracting SDK......................................................................................................
   done
   Setting it up...done
   SDK has been successfully set up and is ready to be used.
   Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
   $ . /home/kuangwh/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi

Configuration of the Cross-Compilation Toolchain
""""""""""""""""""""""""""""""""""""""""""""""""""

| After successful installation, there is a script named "environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi" in the 03 directory. Enter the following command:

.. code-block:: shell

   =====> Input:
   $ source environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi

| After running "source", check the cross-compilation toolchain version and other information.

.. code-block:: shell

   =====> Input:
   $ $CC -v

   =====> Output: 
   Using built-in specs.
   COLLECT_GCC=arm-ostl-linux-gnueabi-gcc
   COLLECT_LTO_WRAPPER=/sdc1/kwh-work/stm32mp1/03_sdk/sysroots/x86_64-ostl_sdk-linux/usr/bin/arm-ostl-linux-gnueabi/../../libexec/arm-ostl-linux-gnueabi/gcc/arm-ostl-linux-gnueabi/9.3.0/lto-wrapper
   Target: arm-ostl-linux-gnueabi
   Configured with: ../../../../../../work-shared/gcc-9.3.0-r0/gcc-9.3.0/configure --build=x86_64-linux --host=x86_64-ostl_sdk-linux --target=arm-ostl-linux-gnueabi --prefix=/opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-mp1-20-06-24/sysroots/x86_64-ostl_sdk-linux/usr --exec_prefix=/opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-mp1-20-06-24/sysroots/x86_64-ostl_sdk-linux/usr --bindir=/opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-mp1-20-06-24/sysroots/x86_64-ostl_sdk-linux/usr/bin/arm-ostl-linux-gnueabi --sbindir=/opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-
   。。。。。。
   gcc version 9.3.0 (GCC) 

**Note: CC is a defined macro, and the "$" in "$CC" cannot be omitted.**

| After seeing the version information, the compilation toolchain is configured successfully, and you can proceed to the source code compilation steps. It should be noted that you need to run the "source" configuration once every time you open a terminal window.

Compiling TF-A
~~~~~~~~~~~~~~~~~

**Download the Source Code Package**

| Download the source code package from the provided network disk. The network disk directory is **02_Source_Code/tf-a-stm32mp-2.2-Release.xxx.tar.bz2** , and copy the source code package to the ~/my-work/stm32mp1/02_sources directory in the virtual machine via Samba or other methods.
| (xxx represents the version date. The version will be updated in the future, so the specific version date is not listed here.)

| Extract the TF-A source code package to the current directory:

.. code-block:: shell

   =====> Input:
   $ tar xvf tf-a-stm32mp-2.2-Release.xxx.tar.bz2

**Compilation**

| Enter the directory "tf-a-stm32mp-2.2"

.. code-block:: shell

   =====> Input:
   $ cd tf-a-stm32mp-2.2/
   $ ls
   Makefile.sdk  tf-a-stm32mp-2.2.r1

| First, configure the cross-compilation toolchain

.. code-block:: shell

   =====> Input:
   $ source ~/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi 

| Enter the directory "tf-a-stm32mp-2.2.r1"

.. code-block:: shell

   =====> Input:
   $ cd tf-a-stm32mp-2.2.r1/

| Clean up before compilation

.. code-block:: shell

   =====> Input:
   $ make -f ../Makefile.sdk clean

| Compile with "make"

.. code-block:: shell

   =====> Input:
   $ make -f ../Makefile.sdk all

| After a few minutes, the compilation will be successful. A directory named "build/trusted" will appear in the parent directory, which contains the compiled image files: **tf-a-myzr-stm32mp15-256m-trusted.stm32/tf-a-myzr-stm32mp15-512m-trusted.stm32**.

Compiling U-Boot
~~~~~~~~~~~~~~~~~~

**Download the U-Boot Source Code**

| Download the source code package from the provided network disk. The network disk directory is **02_Source_Code/u-boot-stm32mp-2020.01-Release.xxx.tar.bz2** , and copy the source code package to the ~/my-work/stm32mp1/02_sources directory in the virtual machine via Samba or other methods.

| Extract the source code package "u-boot-stm32mp-2020.01-Release.xxx.tar.bz2"

.. code-block:: shell

   =====> Input:
   $ tar xvf u-boot-stm32mp-2020.01-Release.xxx.tar.bz2

**Compilation**

| Enter the directory "u-boot-stm32mp-2020.01"

.. code-block:: shell

   =====> Input:
   $ cd u-boot-stm32mp-2020.01/

| First, configure the cross-compilation toolchain

.. code-block:: shell

   =====> Input:
   $ source ~/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi 

| Clean up the configuration before compilation

.. code-block:: shell

   =====> Input:
   $ make distclean

| Generate the .config file

.. code-block:: shell

   =====> Input:
   $ make myzrstm32mp15_defconfig

   =====> Output: 
   #
   # configuration written to .config
   #

| Compile with "make". For boards with 512MB memory, run "make DEVICE_TREE=myzr-stm32mp15-512m"; for boards with 256MB memory, run "make DEVICE_TREE=myzr-stm32mp15-256m".

.. code-block:: shell

   =====> Input:
   $ make DEVICE_TREE=myzr-stm32mp15-256m
   =====> or
   $ make DEVICE_TREE=myzr-stm32mp15-512m

   =====> Output:
   scripts/kconfig/conf  --syncconfig Kconfig
     CHK     include/config.h
     UPD     include/config.h
     CFG     u-boot.cfg
     。。。
     MKIMAGE u-boot.stm32
     OBJCOPY u-boot.srec
     SYM     u-boot.sym
     COPY    u-boot.dtb
     CFGCHK  u-boot.cfg

| "u-boot.stm32" is the compiled target file.

.. code-block:: shell

   $ ls u-boot.stm32
   u-boot.stm32

Compiling the Kernel
~~~~~~~~~~~~~~~~~~~~~~

**Download the Kernel Source Code**

| Download the source code package from the provided network disk. The network disk directory is **02_Source_Code/linux-5.4.31-Release.xxx.tar.bz2** , and copy the source code package to the ~/my-work/stm32mp1/02_sources directory in the virtual machine via Samba or other methods.

| Extract the source code package "linux-5.4.31-Release.xxx.tar.bz2"

.. code-block:: shell

   =====> Input:
   $ tar xvf linux-5.4.31-Release.xxx.tar.bz2

**Install Libraries**

| When compiling the kernel for the first time, you need to install the corresponding libraries in the Ubuntu virtual machine.

.. code-block:: shell

   $ sudo apt-get install libncurses5-dev libncursesw5-dev libyaml-dev
   $ sudo apt-get install u-boot-tools
   $ sudo apt-get install libyaml-dev

**Compiling the Kernel**

| Enter the directory "linux-5.4.31"

.. code-block:: shell

   =====> Input:
   ~/my-work/stm32mp1/02_sources$ cd linux-5.4.31/

| First, configure the cross-compilation toolchain

.. code-block:: shell

   =====> Input:
   $ source ~/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi 

| Generate the .config file

.. code-block:: shell

   =====> Input:
   $ make myzrstm32mp15_defconfig

   =====> Output: 
     HOSTCC  scripts/basic/fixdep
     HOSTCC  scripts/kconfig/conf.o
     HOSTCC  scripts/kconfig/confdata.o
     HOSTCC  scripts/kconfig/expr.o
     LEX     scripts/kconfig/lexer.lex.c
     YACC    scripts/kconfig/parser.tab.[ch]
     HOSTCC  scripts/kconfig/lexer.lex.o
     HOSTCC  scripts/kconfig/parser.tab.o
     HOSTCC  scripts/kconfig/preprocess.o
     HOSTCC  scripts/kconfig/symbol.o
     HOSTLD  scripts/kconfig/conf
   #
   # configuration written to .config
   #

| Compile the kernel target file

.. code-block:: shell

   =====> Input:
   $ make uImage LOADADDR=0xC2000040

   =====> Output: 
   。。。
     UIMAGE  arch/arm/boot/uImage
   Image Name:   Linux-5.4.31
   Created:      Mon Oct 19 07:14:40 2020
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    7312904 Bytes = 7141.51 KiB = 6.97 MiB
   Load Address: c2000040
   Entry Point:  c2000040
     Kernel: arch/arm/boot/uImage is ready

| The kernel image compilation takes a relatively long time. After successful compilation, "arch/arm/boot/uImage" is the kernel target file.

**Compiling the Device Tree**

| Enter the following command to compile the device tree separately.

.. code-block:: shell

   =====> Input:
   $ make myzr-stm32mp15.dtb

   =====> Output: 
     DTC     arch/arm/boot/dts/myzr/myzr-stm32mp15.dtb

| The device tree DTB file is generated at **arch/arm/boot/dts/myzr/myzr-stm32mp15.dtb** .

| Compile the device tree for HDMI display:

.. code-block:: shell

   =====> Input:
   $ make myzr-stm32mp15-hdmi.dts

   =====> Output: 
     DTC     arch/arm/boot/dts/myzr/myzr-stm32mp15-hdmi.dtb

**Compiling the Kernel Module Package**

| Execute the compilation

.. code-block:: shell

   =====> Input:
   $ make modules

   =====> Output: 
   。。。
     CC [M]  sound/usb/snd-usb-audio.mod.o
     LD [M]  sound/usb/snd-usb-audio.ko
     CC [M]  sound/usb/snd-usbmidi-lib.mod.o
     LD [M]  sound/usb/snd-usbmidi-lib.ko

| Install the kernel modules to the specified directory

.. code-block:: shell

   =====> Input:
   $ make INSTALL_MOD_PATH="$PWD/install_artifact" modules_install

   =====> Output: 
     INSTALL sound/soc/fsl/snd-soc-fsl-sai.ko
     INSTALL sound/soc/generic/snd-soc-simple-card.ko
     INSTALL sound/usb/snd-usb-audio.ko
     INSTALL sound/usb/snd-usbmidi-lib.ko
     DEPMOD  5.4.31

| Delete the "source" and "build" directories

.. code-block:: shell

   =====> Input:
   $ rm install_artifact/lib/modules/5.4.31/source
   $ rm install_artifact/lib/modules/5.4.31/build

| Strip the kernel modules

.. code-block:: shell

   =====> Input:
   $ find install_artifact/ -name "*.ko" | xargs $STRIP --strip-debug --remove-section=.comment --remove-section=.note --preserve-dates

| Package the kernel modules

.. code-block:: shell

   =====> Input:
   $ cd install_artifact
   $ tar cjf modules.tar.bz2 *

| Extract the kernel module package to the development board

| Copy the kernel module package to the development board and extract it to the root directory

.. code-block:: shell

   =====> Input:
   # tar xvf modules.tar.bz2 -C /

| Sync the data (not required for boards with 256MB DDR)

.. code-block:: shell

   =====> Input:
   # depmod -a
   # sync
   # reboot


Application Programming Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Download the application code from the provided network disk. The network disk directory is **05_Others->hello_world.tar.bz2** , and copy the source code package to the ~/my-work/stm32mp1/04_app directory in the virtual machine via Samba or other methods.

| Enter the hello_world directory

.. code-block:: shell

   =====> Input:
   $ cd hello_world/

| First, configure the cross-compilation toolchain

.. code-block:: shell

   =====> Input:
   $ source ~/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi 

| Compile gtk_hello_world.c

.. code-block:: shell

   =====> Input:
   $ make

| Move the compiled binary file gtk_hello_world to the development board (refer to the file transfer section in the previous experience chapter for the transfer method). The development board must be connected to a display.

| Grant executable permission and run the file

.. code-block:: shell

   =====> Input:
   $ chmod +x gtk_hello_world
   $ ./gtk_hello_world

   =====> Output: 
   (gtk_hello_world:6370): dbind-WARNING **: 18:17:49.914: Error retrieving accessibility bus address: org.a11y.Bus.Error: Failed to execute chi)

| After successful execution, a hello world window will be displayed on the screen.
