Compilation Manual
====================

Preparing the Compilation Environment
----------------------------------------

Installing Cross-Compilation Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Prepare cross-compilation tool files

- Download "st-image-weston-openstlinux-weston-stm32mp1-x86_64-toolchain-4.0.4-openstlinux-5.15-yocto-kirkstone-mp1-v22.11.23.sh" from the network drive, then transfer the file to the x86_64 Linux host.

2. Execute installation

.. code-block:: shell

    # =====> Input:

    # Create an installation directory and place the compilation chain in it
    mkdir ~/my-work/stm32mp13/03_sdk -p

    # Add executable permissions
    chmod +x st-image-weston-openstlinux-weston-stm32mp1-x86_64-toolchain-4.0.4-openstlinux-5.15-yocto-kirkstone-mp1-v22.11.23.sh 

    # Install
    ./st-image-weston-openstlinux-weston-stm32mp1-x86_64-toolchain-4.0.4-openstlinux-5.15-yocto-kirkstone-mp1-v22.11.23.sh 

    # During installation, you will be asked to enter the installation directory, which is also this directory
    Enter target directory for SDK (default: /opt/st/stm32mp1/4.0.4-openstlinux-5.15-yocto-kirkstone-mp1-v22.11.23): /home/kuangwh/my-work/stm32mp13/03_sdk
    

3. Configure the cross-compilation environment

- After successful installation, there is a script named environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi in the 03 directory. Enter the following command:

.. code-block:: shell

    source environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi

4. Verification

.. code-block:: shell

    $CC -v

- The following output indicates that the environment configuration is successful:

.. code-block:: shell

    Using built-in specs.
    COLLECT_GCC=arm-ostl-linux-gnueabi-gcc
    COLLECT_LTO_WRAPPER=/home/kuangwh/my-work/stm32mp13/03_sdk/sysroots/x86_64-ostl_sdk-linux/usr/libexec/arm-ostl-linux-gnueabi/gcc/arm-ostl-linux-gnueabi/11.3.0/lto-wrapper
    Target: arm-ostl-linux-gnueabi
    。。。。
    Supported LTO compression algorithms: zlib zstd
    gcc version 11.3.0 (GCC) 

.. note:: You need to perform the source configuration once every time you open a terminal window.


Downloading Source Code Package
---------------------------------

1. In the 02_Source Code directory on the network drive, download the source code package en.SOURCES-stm32mp1-openstlinux-5.15.tar.bz2 

2. Create a compilation directory:

.. code-block:: shell

    mkdir ~/my-work/stm32mp13/02_sources -p

3. Place the source code in this directory and extract it:

.. code-block:: shell

    tar xvf en.SOURCES-stm32mp1-openstlinux-5.15.tar.bz2 -C ~/my-work/stm32mp13/02_sources/


Compiling tf-a 
----------------

1. Enter the tf-a-stm32mp-v2.6-stm32mp-r2-r0 directory and extract the tf-a source code:

.. code-block:: shell

    tar xvf tf-a-stm32mp-v2.6-stm32mp-r2.tar.bz2 

2. After extraction, enter the tf-a-stm32mp-v2.6-stm32mp-r2 directory

3. In this directory, you can see a compilation script build-512m.sh. Run this script directly to compile:

.. code-block:: shell

    ./build-512m.sh 

4. After compilation is complete, the image will be updated in the ~/my-work/stm32mp13/02_sources/FIP_artifacts directory.


Compiling optee 
-----------------

1. Enter optee-os-stm32mp-3.16.0-stm32mp-r2-r0 and extract the source code:

.. code-block:: shell

    tar xvf optee-os-stm32mp-3.16.0-stm32mp-r2.tar.bz2 

2. After extraction, enter the optee-os-stm32mp-3.16.0-stm32mp-r2 directory

3. In this directory, you can see a compilation script build-512m.sh. Run this script directly to compile:

.. code-block:: shell

    ./build-512m.sh 

4. After compilation is complete, the image will be updated in the ~/my-work/stm32mp13/02_sources/FIP_artifacts directory.


Compiling uboot 
-----------------

1. Enter u-boot-stm32mp-v2021.10-stm32mp-r2-r0 and extract the source code:

.. code-block:: shell

    tar xvf u-boot-stm32mp-v2021.10-stm32mp-r2.tar.bz2 

2. After extraction, enter the u-boot-stm32mp-v2021.10-stm32mp-r2 directory

3. In this directory, enter the following commands for configuration, compilation, packaging, etc.:

.. code-block:: shell

    export FIP_DEPLOYDIR_ROOT=$PWD/../../FIP_artifacts
    make -f $PWD/../Makefile.sdk DEPLOYDIR=$FIP_DEPLOYDIR_ROOT/u-boot UBOOT_CONFIG=trusted UBOOT_DEFCONFIG=myzrstm32mp13_defconfig UBOOT_BINARY=u-boot.dtb DEVICETREE=myzr-stm32mp13-512m all

4. After compilation is complete, the image will be updated in the ~/my-work/stm32mp13/02_sources/FIP_artifacts directory.


Compiling Kernel
------------------

1. Enter linux-stm32mp-5.15.67-stm32mp-r2-r0 and extract the source code:

.. code-block:: shell

    tar xvf linux-5.15.67.tar.bz2

2. After extraction, enter the linux-5.15.67 directory

3. Generate .config file

.. code-block:: shell

    make myzr-stm32mp13_defconfig 

4. Compile kernel target files

.. code-block:: shell

    make -j16 uImage LOADADDR=0xC2000040

5. Compile device tree files

.. code-block:: shell

    make myzr-stm32mp13.dtb

6. Compile kernel module package

.. code-block:: shell

    # Compile
    make -j16 modules
    # Enter installation
    make INSTALL_MOD_PATH="$PWD/install_artifact" modules_install
    # Delete irrelevant directory files
    rm install_artifact/lib/modules/5.15.67/source
    rm install_artifact/lib/modules/5.15.67/build
    # Strip kernel modules
    find install_artifact/ -name "*.ko" | xargs $STRIP --strip-debug --remove-section=.comment --remove-section=.note --preserve-dates
    # Package kernel modules
    cd install_artifact
    tar cjf modules.tar.bz2 *

7. Image files

- Kernel image file is located at: arch/arm/boot/uImage
- Kernel device tree file is located at: arch/arm/boot/dts/myzr/myzr-stm32mp13.dtb
- Kernel module package is located at: install_artifact/modules.tar.bz2

8. Image file update

- Kernel image file update: Copy the kernel image uImage to the development board and replace /boot/uImage
- Kernel device tree file update: Copy the device tree file myzr-stm32mp13.dtb to the development board and replace /boot/myzr-stm32mp13.dtb
- Kernel module package update: Copy the kernel module package to the development board and extract it using the following command:

.. code-block:: shell

    tar xvf modules.tar.bz2 -C /

|   After extraction is complete, enter the following command to restart the development board:

.. code-block:: shell

    depmod  -a
    sync
    reboot
        