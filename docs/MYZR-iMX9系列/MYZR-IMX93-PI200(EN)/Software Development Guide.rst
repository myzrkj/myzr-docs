.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Software Development Guide
==========================

Building the Manual
-------------------

Preparing the Compilation Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install Dependency Package

.. code-block:: text

   sudo apt install libssh-dev

Install gcc-linaro cross-compilation tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To Prepare Cross-Compile Tool Files:

#. Net disk download method:

Transfer the file to the x86_64 Linux host after downloading "gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.tar.xz" on the network disk.

Performing the Installation

.. code-block:: text

   # Create installation directory
   mkdir ~/work/toolchain/gcc-linaro -p
   
   # Installation Instructions
   tar xf gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.tar.xz -C ~/work/toolchain/gcc-linaro

#. Create cross-compilation tool profile

.. code-block:: text

   # Create a Configuration File
   cat << EOF > ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env
   #!/bin/sh
   export PATH=${HOME}/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu/bin:${PATH}
   export ARCH=arm64
   export CROSS_COMPILE=aarch64-linux-gnu-
   EOF
   
   # Configure Executable Permissions
   chmod +x ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

#. Configure Tool Environment Variables

.. code-block:: text

   source ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

#. Check the installation

.. code-block:: text

   ${CROSS_COMPILE}gcc -v

#. Extension Information

.. code-block:: text

   Use built-in specs.
   COLLECT_GCC=aarch64-linux-gnu-gcc
   COLLECT_LTO_WRAPPER=/home/tangbin/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu/bin/../libexec/gcc/aarch64-linux-gnu/7.5.0/lto-wrapper
   Target: aarch64-linux-gnu
   Configured as: '/home/tcwg-buildslave/workspace/tcwg-make-release_0/snapshots/gcc.git~linaro-7.5-2019.12/configure' SHELL = /bin/bash --with-mpc = /home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu --with-mpfr = /home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gmp = /home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gnu-as --with-gnu-ld --disable-libmudflap --enable-lto --enable-shared --without included-gettext --enable-nls --with-system-zlib --disable-sjlj-exceptions --enable-gnu-unique-object --enable-linker-build-id --disable-libstdcxx-pch --en-c99 --enable-clocale = gnu --enable-libstdxx-debugu --en-long-long --clowith og = no --with-ppl = no --with-isl = no --disable-multilib --enable-fix-cortex-a53-835769 --enable-fix-cortex-a53-843419 --with-arch = armv8-a --enable-threads = posix --enable-multiarch --enable-libstdcxx-time = yes --enable-gnu-indirect-function --with-build-sysroot = /home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/sysroots/aarch64-linux-gnu --sysroot = /home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu/aarch64-linux-gnu/libc --enable-checking = release --disable-bootstrap --enable-languages = c, c + +, fortran, lto --build = x86_64-unknown-linux-gnu --host = x86_64-unknown-linux-gnu -- target = aarch64-linux-gnu --prefix = /home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu
   Thread Model: posix
   gcc version 7.5.0 (Linaro GCC 7.5-2019.12)

Compiling a U-Boot File
~~~~~~~~~~~~~~~~~~~~~~~

#. Download the U-Boot source code package file from the net drive and extract it.

#. Configure compiler environment variables

.. code-block:: text

   source ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

#. Target file compilation

.. code-block:: text

   cd ~/imx-uboot-6.6.52
   make myzr_imx93-pi200_defconfig O=build
   cd build
   make -j24

#. Target Document Description

u-boot-nodtb.bin, spl /u-boot-spl.bin, arch /arm/dts/myzr-imx93-pi200.dtb is the target file, which will be relied on when compiling the boot file in the next step.

Compile BOOT file
~~~~~~~~~~~~~~~~~

#. Download the Boot compiler and unzip it.

#. Compile Boot File

.. code-block:: text

   # Copy the target file to mkimage first
   cp ../imx-mkimage-6.12.49/build/spl/u-boot-spl.bin iMX8M/u-boot-spl.bin
   cp ../imx-mkimage-6.12.49/build/u-boot-nodtb.bin iMX8M/u-boot-nodtb.bin
   cp ../imx-mkimage-6.12.49/build/arch/arm/dts/myimx8mpwfpd.dtb iMX8M/myimx8mpwfpd.dtb
   
   # compiled
   cd ~/imx-mkimage-6.12.49
   cp -f u-boot.bin u-boot.bin.orig
   cat u-boot-nodtb.bin myzr-imx93-pi200.dtb > u-boot.bin
   cd ..
   make SOC=iMX9 V=1 flash_singleboot

#. Target Document Description

The final generated file is [flash.bin]. Under the imx-mkimage-6.12.49 /iMX93 directory, you can modify the compiled target file to replace the file that needs to be used by the burning tool.

Compiling the Linux kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Download the Linux source package file and extract it.

#. To configure the compiler environment variables:

.. code-block:: text

   source ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

#. Linux Image File Compilation:

.. code-block:: text

   cd ~/work/linux/imx-linux-6.6.52
   make ARCH=arm64 myzr_imx_defconfig
   make Image -j24

#. Linux Device Tree File Compilation

.. code-block:: text

   make myzr/myzr-imx93-pi200.dts

#. Linux Module Compilation

.. code-block:: text

   make modules -j24
   if [ -d modules ]; then rm -rf modules; fi; mkdir modules
   make modules_install INSTALL_MOD_PATH=./modules
   tar cjf kernel-modules.tar.bz2 -C modules lib
