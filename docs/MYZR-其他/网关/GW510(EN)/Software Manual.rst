.. raw:: html

   <style>
   h1 {
       color: #4CAF50;  /* Level 1 heading font color */
   }
   </style>


Software Manual
===============

Compilation Guide
-----------------
**Install Software Packages**

Ubuntu Version: Ubuntu 20.04

Package Installation:

.. code-block:: shell

    $ sudo apt-get install libc6-dev-i386 lib32z1 libuuid1 cmake libncurses5-dev libncursesw5-dev bc xz-utils automake libtool libevdev-dev 
    pkg-config mtd-utils bison flex libssl-dev libmpc-dev squashfs-tools gawk make gcc git python rename

Additional Configuration:

a. Default Shell Configuration

The build scripts use bash by default. The system's default shell must be bash. Verify with `ls -la /bin/sh`. For Ubuntu, newer versions default to dash. Change it as follows:

.. code-block:: shell

    # ls -la /bin/sh
    lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> dash
   
    # sudo dpkg-reconfigure dash
    # Select <NO> in the dialog
    # ls -la /bin/sh
    lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> bash

b. Set Default Python Version to Python 2.x (Not required for Ubuntu 20.04, which defaults to Python 2.x)

There are semantic differences between Python 2 and Python 3. The SDK build scripts use Python 2 semantics. Set the default Python version to 2.x. Refer to online documentation for methods, such as using the update-alternatives tool.

**Extract Source Code and Cross-compilation**

- boot-Pcupid_DLD00V2.3.3*.tar.gz: Uboot source code
- kernel-Pcupid_DLD00V2.3.3*.gz: Kernel source code
- project-Pcupid_DLD00V2.3.3*.tar.gz: Image building components, including non-open source lib/ko and external API header files (squashfs produces a read-only system, ubifs produces a read-write system. UBIFS is recommended)
- sdk-Pcupid_DLD00V2.3.3*.tar.gz: Test demos and application packaging framework
- aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu.tar.xz: Cross-compilation toolchain

.. code-block:: shell

    $ mkdir ~/ssd2351/source -p
    $ tar zxvf boot-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source
    $ tar zxvf kernel-Pcupid_DLD00V2.3.3*.gz -C ~/ssd2351/source
    $ tar zxvf project-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source
    $ tar zxvf sdk-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source
    $ mkdir ~/ssd2351/tool/toolchain -p
    $ tar -xvf aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu.tar.xz -C ~/ssd2351/tool/toolchain

**Set Up Cross-compilation Toolchain**

.. code-block:: shell

    $ export PATH=~/ssd2351/tool/toolchain/aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu/bin:$PATH
    $ export CROSS_COMPILE=aarch64-unknown-linux-gnu-12.4.0-
    $ export ARCH=arm64
    $ ${CROSS_COMPILE}gcc -v

**Full Build**

# Full build will compile boot, kernel, project, and sdk

.. code-block:: shell

    $ cd ~/ssd2351/source/project/
    $ make myzr-ssd2351-ek112_128m_defconfig    (DDR: 128M)
    or
    $ make myzr-ssd2351-ek112_256m_defconfig    (DDR: 256M)
    $ make clean;make image -j8   

# Compiled images are located in project/image/output/images

# Note:

# For the first build, execute `make clean;make image -j8` in the project directory for a complete build (includes boot/kernel)

# For improved debug efficiency after the initial build, you can compile specific modified modules directly in the project directory and repackage quickly:

# Compile only kernel:

.. code-block:: shell

    $ cd ~/ssd2351/source/project/
    $ make linux-kernel_clean;make linux-kernel -j8

# Compile only boot:

.. code-block:: shell

    $ cd ~/ssd2351/source/project/
    $ make boot_clean;make boot -j8

# Quick package sdk image only:

.. code-block:: shell

    $ cd ~/ssd2351/source/project/
    $ make image-fast-nocheck -j8

**Standalone Boot Compilation**

# The SDK build in project already includes boot compilation. It is recommended to compile boot using `make boot` in the project directory after modification. No manual release to project path is needed; simply repackage the project.

.. code-block:: shell

    $ cd ~/ssd2351/source/boot
    $ make pcupid_ssm001c_s01a_spinand_arm64_defconfig
    $ make clean;make -j8;

# Note: When compiling separately in the boot directory, you must manually release the generated image to the corresponding project directory before packaging.

.. code-block:: shell

    $ cp ~/ssd2351/source/boot/u-boot_spinand.xz.img.bin ~/ssd2351/source/project/board/uboot/u-boot.xz.img.bin

**Standalone Kernel Compilation**

# The SDK build in project already includes kernel compilation. It is recommended to compile kernel using `make linux-kernel` in the project directory after modification. No manual release to project path is needed; simply repackage the project.

.. code-block:: shell

    $ cd ~/ssd2351/source/kernel
    $ make pcupid_ssm001c_s01a_spinand_voip_defconfig
    $ make clean;make image -j8;

# Note: The project packaging uses symbolic links to the kernel directory, so no manual release is needed. Simply run the project packaging.

# If adding new kernel modules, add them to kernel_mod_list/kernel_mod_list_late (ko files in kernel_mod_list_late will be loaded after mi modules)

# Path: project/kbuild/customize/6.1/pcupid/dispcam/kernel_mod_list

**Generate USB Programming Image**

# Build the complete SDK following the normal process to generate image upgrade files.

# After successful SDK build, execute the script ./image/makefiletools/script/make_usb_factory_sigmastar.sh

# Choose full upgrade or partial partition upgrade: (Y for full, N for partial)

.. code-block:: shell

    $ cd ~/ssd2351/source/project/
    $ ./image/makefiletools/script/make_usb_factory_sigmastar.sh

Output:

.. code-block:: shell

    Full or Optional Upgrade ? (Y/N)y
    using alone TF-A:u-bl31.bin
    USB Factory Image Generating.....
    success, usb factory image have generated:
          path:./image/output/images/SstarUsbImage_202502280425.bin
          size:48439296 byte
          md5sum:057c1f55ecbe0a4ecaaa916a8612bfe2

**U-Boot Configuration, Device Tree, and Kernel Configuration**

.. code-block:: shell

    # U-Boot configuration:
    Config: pcupid_ssm001c_s01a_spinand_arm64_defconfig
    Device Tree: pcupid-ssm001c-s01a.dts
    # Kernel configuration
    Config: pcupid_ssm001c_s01a_spinand_voip_defconfig
    Device Tree: pcupid-ssm001c-s01a-voip.dts

**Kernel Configuration**

.. code-block:: shell

    # Set cross-compilation toolchain environment variables (omitted)
    $ cd kernel
    # Enter kernel configuration and save
    $ make menuconfig
    # Save configuration
    $ make savedefconfig
    # Copy to default configuration
    $ cp defconfig arch/arm64/configs/pcupid_ssm001c_s01a_spinand_voip_defconfig