Compilation Manual
=====================

Preparing the Compilation Environment
---------------------------------------

Installing Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    # =====> Input:
    sudo apt install libssh-dev

Installing gcc-linaro Cross-Compilation Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Prepare cross-compilation tool files

　　Can be downloaded from network disk or online.

-  Network disk download method:

　　After downloading "gcc-linaro-7.5.0-2019.12-x86\_64\_aarch64-linux-gnu.tar.xz" from the network disk, transfer the file to the x86_64 Linux host.

-  Online download method:

.. code-block:: shell

    # =====> Input:
    wget https://releases.linaro.org/components/toolchain/binaries/7.5-2019.12/aarch64-linux-gnu/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.tar.xz

2. Execute installation

.. code-block:: shell

    # =====> Input:

    # Create installation directory
    mkdir ~/work/toolchain/gcc-linaro -p

    # Installation command
    tar xf gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.tar.xz -C ~/work/toolchain/gcc-linaro

3. Create cross-compilation tool configuration file

.. code-block:: shell

    # =====> Input:
    # Create configuration file
    cat << EOF > ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env
    #!/bin/sh
    export PATH=${HOME}/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu/bin:${PATH}
    export ARCH=arm64
    export CROSS_COMPILE=aarch64-linux-gnu-
    EOF

    # Configure executable permissions
    chmod +x ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

4. Configure tool environment variables

.. code-block:: shell

    # =====> Input:
    source ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

5. Check installation

.. code-block:: shell

    # =====> Input:
    ${CROSS_COMPILE}gcc -v

6. Tool information

.. code:: text

    Using built-in specs.
        COLLECT_GCC=aarch64-linux-gnu-gcc
        COLLECT_LTO_WRAPPER=/home/tangbin/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu/bin/../libexec/gcc/aarch64-linux-gnu/7.5.0/lto-wrapper
        Target: aarch64-linux-gnu
        Configured with: '/home/tcwg-buildslave/workspace/tcwg-make-release_0/snapshots/gcc.git~linaro-7.5-2019.12/configure' SHELL=/bin/bash --with-mpc=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu --with-mpfr=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gmp=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gnu-as --with-gnu-ld --disable-libmudflap --enable-lto --enable-shared --without-included-gettext --enable-nls --with-system-zlib --disable-sjlj-exceptions --enable-gnu-unique-object --enable-linker-build-id --disable-libstdcxx-pch --enable-c99 --enable-clocale=gnu --enable-libstdcxx-debug --enable-long-long --with-cloog=no --with-ppl=no --with-isl=no --disable-multilib --enable-fix-cortex-a53-835769 --enable-fix-cortex-a53-843419 --with-arch=armv8-a --enable-threads=posix --enable-multiarch --enable-libstdcxx-time=yes --enable-gnu-indirect-function --with-build-sysroot=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/sysroots/aarch64-linux-gnu --with-sysroot=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu/aarch64-linux-gnu/libc --enable-checking=release --disable-bootstrap --enable-languages=c,c++,fortran,lto --build=x86_64-unknown-linux-gnu --host=x86_64-unknown-linux-gnu --target=aarch64-linux-gnu --prefix=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu
        Thread model: posix
        gcc version 7.5.0 (Linaro GCC 7.5-2019.12)

Compiling Boot Files
----------------------

Compiling U-Boot Files
~~~~~~~~~~~~~~~~~~~~~~~~

1. Prepare U-Boot source package file

    - Open the network disk and navigate to the path "2.1_OS_Linux-4.14.98 -> 02_Source", then download the file "uboot-2018.03*.tar.bz2".
    - Transfer the file "uboot-2018.03*.tar.bz2" to the x86_64 Linux host.

2. Extract source package

.. code-block:: shell

    # =====> Input:
    tar xf uboot-2018.03*.tar.bz2 -C ~/work/linux/imx-linux-4.14.98

3. Configure compilation tool environment variables

.. code-block:: shell

    # =====> Input:
    ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

4. Target file compilation

.. note:: You can also compile the boot file by executing ./make_uboot.sh and following the prompts.

.. code-block:: shell

   cd ~/work/linux/imx-linux-4.14.98/uboot-2018.03
   make myimx8mmek200-2g_defconfig O=build-myimx8mmek240-2g
   cd build-myimx8mmek240-2g; make -j24

5. Target files

.. code-block:: shell

   cd ..
   mkdir image-uboot
   cp build-myimx8mmek240-2g/spl/u-boot-spl.bin image-uboot
   cp build-myimx8mmek240-2g/u-boot-nodtb.bin image-uboot
   cp build-myimx8mmek240-2g/arch/arm/dts/myimx8mmek240.dtb image-uboot

Compiling Boot Files
~~~~~~~~~~~~~~~~~~~~~~

1. Prepare Boot compilation tools

|   Transfer the file "mkimage-4.14.98\*.tar.bz2" to the x86\_64 Linux host.

2. Extract Boot compilation tools

.. code-block:: shell

    # =====> Input:
    tar xf mkimage-4.14.98*.tar.bz2 -C ~/work/linux/imx-linux-4.14.98

3. Compile Boot files

.. note::  You can also compile the imkimage file by executing ./make_boot.sh and following the prompts.

.. code-block:: shell

    cd mkimage-4.14.98
    cp ../uboot-2018.03/image-uboot/u-boot-nodtb.bin ./iMX8M/myimx8mmek200-2g-nodtb.bin
    cp ../uboot-2018.03/image-uboot/u-boot-spl.bin ./iMX8M/myimx8mmek200-2g-spl.bin
    cp ../uboot-2018.03/image-uboot/myimx8mmek200.dtb ./iMX8M/myimx8mmek200.dtb
    make myimx8mm SOC=iMX8MM DTB=myimx8mmek200.dtb OUTIMG=myimx8mmek200-2g.bin

4. Target file description

|   iMX8M/myimx8mmek200-2g.bin is the target file. You can replace the file with the same name in the burning tool with the compiled target file.  


Compiling Linux Kernel
-------------------------

1. Prepare Linux source package file

|   Transfer the file "linux-4.14.98\*.tar.bz2" to the x86\_64 Linux host.

2. Extract source package

.. code-block:: shell

    # =====> Input:
    tar xf linux-4.14.98*.tar.bz2 -C ~/work/linux/imx-linux-4.14.98

3. Configure compilation tool environment variables

.. code-block:: shell

    # =====> Input:
    ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

4. Linux Image file compilation

.. note::  You can also compile the kernel file by executing make_kern.sh and following the prompts.

-  Execute compilation

.. code-block:: shell

    # =====> Input:

    cd ~/work/linux/imx-linux-4.14.98/linux-4.14.98

    make myimx8mm_defconfig O=build_myimx8mm

    cd build_myimx8mm; make Image -j24

-  The output information during Image compilation is similar to the following:

.. code:: text

     MODPOST vmlinux.o
     KSYM    .tmp_kallsyms1.o
     KSYM    .tmp_kallsyms2.o
     LD      vmlinux
     SORTEX  vmlinux
     SYSMAP  System.map
     OBJCOPY arch/arm64/boot/Image

5. Linux device tree file compilation

-  Execute compilation

.. code-block:: shell

    # =====> Input:
    make myzr/myimx8mmek200.dtb

-  When the device tree is compiled successfully for the first time, the output information is similar to the following:

.. code:: text

    DTC     arch/arm64/boot/dts/myzr/myimx8mmek200.dtb

6. Linux module compilation

-  Execute compilation

.. code-block:: shell

    # =====> Input:
    make modules -j24

-  The output information when module compilation is successful is similar to the following:

.. code:: text

    ......
    LD [M]  sound/usb/snd-usb-audio.ko
    LD [M]  sound/usb/snd-usbmidi-lib.ko

-  Install kernel modules to specified directory

.. code-block:: shell

    # =====> Input:
    if [ -d modules ]; then rm -rf modules; fi; mkdir modules
    make modules_install INSTALL_MOD_PATH=./modules

-  Module installation output information is similar to the following:

.. code:: text

    ......
    INSTALL sound/usb/snd-usbmidi-lib.ko
    DEPMOD  4.14.98-gda548b57eb4f

-  Package kernel module files

.. code-block:: shell

    # =====> Input:
    tar cjf kernel-modules.tar.bz2 -C modules lib

7. Target file description

|   Image, myimx8mmek200.dtb, kernel-modules.tar.bz2 are the target files. You can replace the files with the same names in the burning tool with the compiled target files.