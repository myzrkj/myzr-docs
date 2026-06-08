MYZR-RZG-EK200 Compilation Reference Manual
=============================================

Cross Compilation
-------------------

|  When we want to compile the source code or compile the source code we have modified, the first step is to configure the corresponding cross-compilation tool. For this set of source code, we compile based on the official Renesas Yocto-compiled SDK.

SDK Download and Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Download**

|  The SDK installation package is located in the MYZR-RZ -> 03_SDK directory. We generally use **poky-glibc-x86_64-core-image-qt-aarch64-smarc-rzg2l-toolchain-3.1.17.sh** for installation.
|  We can create a dedicated directory for rz on the host to store related source code, compilation tools, and other things that will be used later. For example, the directory I created is: /home/myzr/my-work/renesas, and under this directory I created 4 subdirectories:

.. code-block:: shell

   $ ls
   01_image  02_sources  03_sdk  04_app

|  Directory 01 can be used to place the compiled images
|  Directory 02 is used to place the source code
|  Directory 03 is used to place the cross-compilation tools we just downloaded
|  Directory 04 can be used to place our own apps
|  After placing the tools in directory 03, proceed with the tool installation.

**Installation:**

|  Run this toolchain script in directory 03, enter the following command:

.. code-block:: shell

   $ chmod +x poky-glibc-x86_64-core-image-qt-aarch64-smarc-rzg2l-toolchain-3.1.17.sh 
   $ ./poky-glibc-x86_64-core-image-qt-aarch64-smarc-rzg2l-toolchain-3.1.17.sh

|  Enter the installation directory /home/myzr/my_work/renesas/03_sdk

.. code-block:: shell

   Poky (Yocto Project Reference Distro) SDK installer version 3.1.17
   ==================================================================
   Enter target directory for SDK (default: /opt/poky/3.1.17): /home/myzr/my_work/renesas/03_sdk

|  Enter y and wait for the installation until "successfully" appears indicating successful installation

.. code-block:: shell

   You are about to install the SDK to "/home/myzr/my_work/renesas/03_sdk". Proceed [Y/n]? y
   Extracting SDK.......................

Cross Compilation Tool Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  After successful installation, there is an environment-setup-aarch64-poky-linux script in directory 03. Enter the following command:

.. code-block:: shell

   $ source environment-setup-aarch64-poky-linux

|  After sourcing, check the cross-compilation tool version and other information

.. code-block:: shell

   =====> Input:
   $ $CC -v

   =====> Output: 
   Using built-in specs.
   COLLECT_GCC=aarch64-poky-linux-gcc
   COLLECT_LTO_WRAPPER=/home/kuangwh/my-work/rzg2l/03_sdk/sysroots/x86_64-pokysdk-linux/usr/libexec/aarch64-poky-linux/gcc/aarch64-poky-linux/8.3.0/lto-wrapper
   Target: aarch64-poky-linux
   。。。。
   gcc version 8.3.0 (GCC)

`Note: CC is a set macro, the "$" in $CC cannot be removed`

|  After seeing the version information, the compilation tool is configured successfully, and you can proceed to the source code compilation steps. Note that you need to perform the source configuration once every time you open a terminal window.

Compiling U-Boot
------------------

Downloading U-Boot Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The U-Boot source code directory is in MYZR-RZ -> 02_源码 -> u-boot-Release.xxx.tar.bz2. ("Release.xxx" indicates the version of the source code) Copy the source code to the host's /home/myzr/my_work/renesas/02_sources directory
|  Extract the source code package to the 02_sources directory:

.. code-block:: shell

   $ tar xvf u-boot-Release.xxx.tar.bz2

Compilation
~~~~~~~~~~~~~

|  Enter the U-Boot directory

.. code-block:: shell

   $ cd u-boot/

|  First configure the cross-compilation tool

.. code-block:: shell

   $ source ../../03_sdk/environment-setup-aarch64-poky-linux

|  Use build.sh for the entire configuration and compilation process.

.. code-block:: shell

   $ ./build.sh rzg2l all

|  The first parameter is the board CPU model, choose rzg2l or rzg2ul; the second parameter has the following options:

.. code-block:: shell

   config--Generate the corresponding .config file according to the first parameter rzg2l/rzg2ul
   make--Compile according to the current configuration file .config
   clean--Clear compiled files
   pack--Package the compiled uboot image
   all--Perform all the previous operations

|  Later, when we develop and debug ourselves, we can perform different compilation configurations according to the parameters.
|  The finally packaged image files are in the fpack directory:

.. code-block:: shell

   $ ls fpack/
   bin  bl31.bin  fip.bin  fip-myzr-rzg2l.srec  fip-myzr-rzg2ul.srec  lib

|  fip-myzr-rzg2l.srec/fip-myzr-rzg2ul.srec are the image files that we can burn to the development board.

Compiling the Kernel
----------------------

Downloading Kernel Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The U-Boot source code directory is in MYZR-RZ -> 02_源码 -> linux-5.10-Release.xxx.tar.bz2. ("Release.xxx" indicates the version of the source code) Copy the source code to the host's /home/myzr/my_work/renesas/02_sources directory
|  Extract the source code package to the 02_sources directory:

.. code-block:: shell

   $ tar xvf linux-5.10-Release.xxx.tar.bz2

Installing Libraries
~~~~~~~~~~~~~~~~~~~~~~

|  When compiling the kernel for the first time, you need to install the corresponding libraries on the Ubuntu virtual machine

.. code-block:: shell

   $ sudo apt-get update
   $ sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib \
   build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
   xz-utils debianutils iputils-ping libsdl1.2-dev xterm p7zip-full libyaml-dev libssl-dev

Compiling Image
~~~~~~~~~~~~~~~~~

|  Enter the linux-5.10 directory

.. code-block:: shell

   $ cd linux-5.10/

|  First configure the cross-compilation tool

.. code-block:: shell

   $ source ../../03_sdk/environment-setup-aarch64-poky-linux

|  Generate the .config file

.. code-block:: shell

   $ make myzr-rz_defconfig

|  Compile Image

.. code-block:: shell

   $ make Image -j24

|  The kernel image compilation takes a long time. After successful compilation, **arch/arm64/boot/Image** is the kernel target file.

Compiling Device Tree
~~~~~~~~~~~~~~~~~~~~~~~

|  Enter the following command to compile the device tree file:

.. code-block:: shell

   $ make renesas/myzr-rzg2l-dsi.dtb

|  The dtb files are compiled according to different models of the development board: myzr-rzg2l-dsi.dtb, myzr-rzg2l-dsi.dtb, myzr-rzg2ul-eth.dtb, myzr-rzg2ul-lcd.dtb
|  The device tree dtb files are generated in **arch/arm64/boot/dts/renesas/*.dtb**

Compiling Kernel Module Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Execute compilation

.. code-block:: shell

   $ make modules

|  Install kernel modules to the specified directory

.. code-block:: shell

   make INSTALL_MOD_PATH="$PWD/install_modules" modules_install

|  Delete source and build directories

.. code-block:: shell

   $ rm install_modules/lib/modules/5.10.131-cip13-yocto-standard/source
   $ rm install_modules/lib/modules/5.10.131-cip13-yocto-standard/build

|  Strip kernel modules

.. code-block:: shell

   $ find install_modules/ -name "*.ko" | xargs $STRIP --strip-debug --remove-section=.comment --remove-section=.note --preserve-dates

|  Package kernel modules

.. code-block:: shell

   $ cd install_modules
   $ tar cjf modules.tar.bz2 *

|  Copy the kernel module package modules.tar.bz2 to the development board and extract it to the root directory

.. code-block:: shell

   # tar xvf modules.tar.bz2 -C /

|  Sync data

.. code-block:: shell

   # depmod -a
   # sync
   # reboot