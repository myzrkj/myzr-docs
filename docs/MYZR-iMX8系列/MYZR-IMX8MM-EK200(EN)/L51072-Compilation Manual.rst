Compilation Manual
====================

Preparing the Compilation Environment
---------------------------------------

Installing Dependent Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    # =====> Input:
    sudo apt install libssh-dev

Installing the gcc-linaro Cross-Compilation Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Prepare the cross-compilation tool file

　　You can download it from a network disk or online.

- Network disk download method:

　　After downloading "gcc-linaro-7.5.0-2019.12-x86\_64\_aarch64-linux-gnu.tar.xz" from the network disk, transfer the file to the x86_64 Linux host.

- Online download method:

.. code-block:: shell

    # =====> Input:
    wget https://releases.linaro.org/components/toolchain/binaries/7.5-2019.12/aarch64-linux-gnu/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.tar.xz

2. Execute the installation

.. code-block:: shell

    # =====> Input:

    # Create the installation directory
    mkdir ~/work/toolchain/gcc-linaro -p

    # Installation command
    tar xf gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.tar.xz -C ~/work/toolchain/gcc-linaro

3. Create the cross-compilation tool configuration file

.. code-block:: shell

    # =====> Input:
    # Create the configuration file
    cat << EOF > ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env
    #!/bin/sh
    export PATH=${HOME}/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu/bin:${PATH}
    export ARCH=arm64
    export CROSS_COMPILE=aarch64-linux-gnu-
    EOF

    # Configure executable permissions
    chmod +x ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

4. Configure the tool environment variables

.. code-block:: shell

    # =====> Input:
    source ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

5. Check the installation

.. code-block:: shell

    # =====> Input:
    ${CROSS_COMPILE}gcc -v

6. Tool Information

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

1. Prepare the U-Boot source package file

| 　　① Open the network disk to "3.2_OS_Linux-5.10.72 -> 02_source" and download "uboot-2021.04\*.tar.bz2".
| 　　② Transfer the file "uboot-2021.04\*.tar.bz2" to the x86_64 Linux host.

2. Extract the source package

.. code-block:: shell

    # =====> Input:
    tar xf uboot-2021.04*.tar.bz2 -C ~/work/linux/imx-linux-5.10.72

3. Configure the compilation tool environment variables

.. code-block:: shell

    # =====> Input:
    source ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

4. Compile the target files

.. code-block:: shell

    cd ~/work/linux/imx-linux-5.10.72/uboot-2021.04
    make myimx8mmek200_defconfig O=build
    cd build
    make -j24

5. Description of the target files

　　u-boot-nodtb.bin, spl/u-boot-spl.bin, and arch/arm/dts/myimx8mmek200.dtb are the target files, which will be dependent on when compiling the Boot files in the next step.

Compiling Boot Files
~~~~~~~~~~~~~~~~~~~~~~~

1. Prepare the Boot compilation tool

  Transfer the file "mkimage-5.10.72\*.tar.bz2" to the x86\_64 Linux host.

2. Extract the Boot compilation tool

.. code-block:: shell

    # =====> Input:
    tar xf mkimage-5.10.72*.tar.bz2 -C ~/work/linux/imx-linux-5.10.72

3. Compile the Boot files

.. code-block:: shell

    cd ~/work/linux/imx-linux-5.10.72/mkimage-5.10.72
    make SOC=iMX8MM dtbs=myimx8mmek200.dtb flash_ddr4_evk OUTIMG=boot-myimx8mmek200.bin

4. Description of the target file

　　iMX8M/boot-myimx8mmek200.bin is the target file, and you can replace the file with the same name in the burning tool with the compiled target file.  


Compiling the Linux Kernel
-----------------------------

1. Prepare the Linux source package file

　　Transfer the file "imx-linux-5.10.72\*.tar.bz2" to the x86\_64 Linux host.

2. Extract the source package

.. code-block:: shell

    # =====> Input:
    tar xf linux-5.10.72*.tar.bz2 -C ~/work/linux/imx-linux-5.10.72

3. Configure the compilation tool environment variables

.. code-block:: shell

    # =====> Input:
    source ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

4. Compile the Linux Image file

- Execute the compilation

.. code-block:: shell

    # =====> Input:

    cd ~/work/linux/imx-linux-5.10.72/linux-5.10.72
    make imx_v8_defconfig
    make Image -j24

- The output information during the Image compilation is similar to the following:

.. code:: text

    WRAP    arch/arm64/include/generated/uapi/asm/kvm_para.h
    WRAP    arch/arm64/include/generated/uapi/asm/errno.h
    ......
    KSYMS   .tmp_vmlinux.kallsyms2.S
    AS      .tmp_vmlinux.kallsyms2.S
    LD      vmlinux
    SORTTAB vmlinux
    SYSMAP  System.map
    OBJCOPY arch/arm64/boot/Image

5. Compile the Linux Device Tree file

- Execute the compilation

.. code-block:: shell

    # =====> Input:
    make myzr/myimx8mmek200.dtb

- When the device tree is compiled successfully for the first time, the output information is similar to the following:

.. code:: text

    DTC     arch/arm64/boot/dts/myzr/myimx8mmek200.dtb

6. Compile the Linux Modules

- Execute the compilation

.. code-block:: shell

    # =====> Input:
    make modules -j24

- The output information when the modules are compiled successfully is similar to the following:

.. code:: text

    ......
    LD [M]  sound/usb/snd-usb-audio.ko
    LD [M]  sound/usb/snd-usbmidi-lib.ko

- Install the kernel modules to the specified directory

.. code-block:: shell

    # =====> Input:
    if [ -d modules ]; then rm -rf modules; fi; mkdir modules
    make modules_install INSTALL_MOD_PATH=./modules

- The output information of the module installation is similar to the following:

.. code:: text

    ......
    INSTALL sound/usb/snd-usbmidi-lib.ko
    DEPMOD  5.10.72-g5a70c7927261

- Package the kernel module files

.. code-block:: shell

    # =====> Input:
    tar cjf kernel-modules.tar.bz2 -C modules lib

7. Description of the target files

　　Image, myimx8mmek200.dtb, and kernel-modules.tar.bz2 are the target files, and you can replace the files with the same names in the burning tool with the compiled target files.