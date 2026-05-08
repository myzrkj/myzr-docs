Compilation Manual
====================

Compilation Environment
-------------------------

- Ubuntu Version: Ubuntu 20.04
- Software Package Installation:

.. code-block:: shell
  
  sudo apt-get install libc6-dev-i386 lib32z1 libuuid1 cmake libncurses5-dev libncursesw5-dev bc xz-utils automake libtool libevdev-dev pkg-config mtd-utils bison flex libssl-dev libmpc-dev squashfs-tools gawk make gcc git python rename

- The compilation script uses **bash** by default. The system default shell must be bash. Run `ls -la /bin/sh` to check. Taking Ubuntu as an example, newer Ubuntu versions use dash as the default shell. Modify it as follows:

.. code-block:: shell

  $ ls -la /bin/sh
  lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> dash

  $ sudo dpkg-reconfigure dash
  # Select <NO> in the pop-up interface

  $ ls -la /bin/sh
  lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> bash

| Set the default Python version to Python 2.x(No configuration required for Ubuntu 20.04; Python 2.x is default)
| There are syntax differences between Python 2 and Python 3. The SDK compilation script follows Python 2 syntax, so the system default Python must be set to Python 2.x. Refer to online documents for configuration methods, such as using the `update-alternatives` tool.

Source Code & Cross Compilation
---------------------------------

.. code-block:: shell

  $ mkdir ~/ssd2355/source -p
  $ tar zxvf boot-Pcupid_DLD00V2.3.3.tar.gz -C ~/ssd2355/source
  $ tar zxvf kernel-Pcupid_DLD00V2.3.3.tar.gz -C ~/ssd2355/source
  $ tar zxvf project-Pcupid_DLD00V2.3.3.tar.gz -C ~/ssd2355/source
  $ tar zxvf sdk-Pcupid_DLD00V2.3.3.tar.gz -C ~/ssd2355/source
  $ mkdir ~/ssd2355/tool/toolchain -p
  $ tar -xvf ./aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu.tar.gz -C ~/ssd2355/tool/toolchain

- Configure Cross Compilation Toolchain

.. code-block:: shell

  export PATH=/home/surs/my-work/ssd2355/tool/toolchain/aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu/bin:$PATH
  export CROSS_COMPILE=aarch64-unknown-linux-gnu-12.4.0-
  export ARCH=arm64
  ${CROSS_COMPILE}gcc -v

Global Compilation
--------------------

.. code-block:: shell

  # Global compilation: compile boot, kernel, project and SDK altogether
  $ cd ~/ssd2355/source/project/
  make dispcam_pcupid.spinand.glibc-12.4.0-squashfs.ssz001a.1024.bga_ddr4_riscv_defconfig
  make image -j16
  ./image/makefiletools/script/make_usb_factory_sigmastar.sh

  # Compiled images are generated under project/image/output/images
  # Note: For the first compilation, execute make clean; make image -j8 under project for full compilation (including full build of boot/kernel)
  # To improve debugging efficiency, after the first compilation, you can compile modified modules separately and repackage quickly during subsequent debugging, for example:

  # Compile kernel only:
  $ cd ~/ssd2355/source/project/
  $ make linux-kernel_clean;make linux-kernel -j8

  # Compile boot only:
  $ cd ~/ssd2355/source/project/
  $ make boot_clean;make boot -j8

  # Quick repackage SDK image only:
  $ cd ~/ssd2355/source/project/
  $ make image-fast-nocheck -j8

- Kernel Device Tree Files

.. code-block:: shell

  ssd2355/source/kernel/arch/arm64/boot/dts/sstar/pcupid.dtsi
  ssd2355/source/kernel/arch/arm64/boot/dts/sstar/pcupid-ssz001a-s01a.dts
  ssd2355/source/kernel/arch/arm64/boot/dts/sstar/pcupid-ssz001a-s01a-padmux.dtsi

- Menuconfig Configuration

.. code-block:: shell

  # Boot
  make ARCH=arm64 menuconfig
  make savedefconfig
  cp defconfig configs/pcupid_ssz001a_s01a_spinand_arm64_defconfig

  # Kernel
  make ARCH=arm64 menuconfig
  make savedefconfig
  cp defconfig arch/arm64/configs/pcupid_ssz001a_s01a_spinand_defconfig
