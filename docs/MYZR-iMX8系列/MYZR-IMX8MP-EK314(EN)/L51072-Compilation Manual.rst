Compilation Manual
=====================

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

　　You can download it from a network drive or online.

- Network drive download method:

　　After downloading "gcc-linaro-7.5.0-2019.12-x86\_64\_aarch64-linux-gnu.tar.xz" from the network drive, transfer the file to the x86_64 Linux host.

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

6. Tool information

.. code:: text

    Using built-in specs.
    COLLECT_GCC=aarch64-linux-gnu-gcc
    COLLECT_LTO_WRAPPER=/home/tangbin/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu/bin/../libexec/gcc/aarch64-linux-gnu/7.5.0/lto-wrapper
    Target: aarch64-linux-gnu
    Configured with: '/home/tcwg-buildslave/workspace/tcwg-make-release_0/snapshots/gcc.git~linaro-7.5-2019.12/configure' SHELL=/bin/bash --with-mpc=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu --with-mpfr=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gmp=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gnu-as --with-gnu-ld --disable-libmudflap --enable-lto --enable-shared --without-included-gettext --enable-nls --with-system-zlib --disable-sjlj-exceptions --enable-gnu-unique-object --enable-linker-build-id --disable-libstdcxx-pch --enable-c99 --enable-clocale=gnu --enable-libstdcxx-debug --enable-long-long --with-cloog=no --with-ppl=no --with-isl=no --disable-multilib --enable-fix-cortex-a53-835769 --enable-fix-cortex-a53-843419 --with-arch=armv8-a --enable-threads=posix --enable-multiarch --enable-libstdcxx-time=yes --enable-gnu-indirect-function --with-build-sysroot=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/sysroots/aarch64-linux-gnu --with-sysroot=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu/aarch64-linux-gnu/libc --enable-checking=release --disable-bootstrap --enable-languages=c,c++,fortran,lto --build=x86_64-unknown-linux-gnu --host=x86_64-unknown-linux-gnu --target=aarch64-linux-gnu --prefix=/home/tcwg-buildslave/workspace/tcwg-make-release_0/_build/builds/destdir/x86_64-unknown-linux-gnu
    Thread model: posix
    gcc version 7.5.0 (Linaro GCC 7.5-2019.12) 

Installing the QT5 SDK
~~~~~~~~~~~~~~~~~~~~~~~~

1. Prepare the cross-compilation tool file

　　After downloading "fsl-imx-xwayland-glibc-x86\_64-imx-image-full-cortexa53-crypto-imx8mp-ddr4-evk-toolchain-5.10-hardknott.sh" from the network drive, transfer the file to the x86_64 Linux host.

2. Execute the installation command

.. code-block:: shell

    # =====> Input:
    ./fsl-imx-xwayland-glibc-x86_64-imx-image-full-cortexa53-crypto-imx8mp-ddr4-evk-toolchain-5.10-hardknott.sh

3. Select the installation path

　　Press Enter when the following information appears (keep the default installation path)

.. code:: text

    NXP i.MX Release Distro SDK installer version 5.10-hardknott
    ============================================================
    Enter target directory for SDK (default: /opt/fsl-imx-xwayland/5.10-hardknott):

4. Confirm the installation path

　　Press Enter when the following information appears (keep the default option)

.. code:: text

    You are about to install the SDK to "/opt/fsl-imx-xwayland/5.10-hardknott". Proceed [Y/n]

5. Wait for the installation

　　The installation process may take several minutes, and the information displayed during the installation will be similar to the following:

.. code:: text

    Extracting SDK...............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................done
    Setting it up...done
    SDK has been successfully set up and is ready to be used.
    Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
    $ . /opt/fsl-imx-xwayland/5.10-hardknott/environment-setup-cortexa53-crypto-poky-linux

6. Configure the tool environment variables

.. code:: text

    # =====> Input:
    . /opt/fsl-imx-xwayland/5.10-hardknott/environment-setup-cortexa53-crypto-poky-linux

7. Check the installation

.. code-block:: shell

    # =====> Input:
    ${CROSS_COMPILE}gcc -v

8. Tool information

.. code:: text

    Using built-in specs.
    COLLECT_GCC=aarch64-poky-linux-gcc
    COLLECT_LTO_WRAPPER=/opt/fsl-imx-xwayland/5.10-hardknott/sysroots/x86_64-pokysdk-linux/usr/libexec/aarch64-poky-linux/gcc/aarch64-poky-linux/10.2.0/lto-wrapper
    Target: aarch64-poky-linux
    Configured with: ../../../../../../work-shared/gcc-10.2.0-r0/gcc-10.2.0/configure --build=x86_64-linux --host=x86_64-pokysdk-linux --target=aarch64-poky-linux --prefix=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr --exec_prefix=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr --bindir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr/bin/aarch64-poky-linux --sbindir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr/bin/aarch64-poky-linux --libexecdir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr/libexec/aarch64-poky-linux --datadir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr/share --sysconfdir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/etc --sharedstatedir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/com --localstatedir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/var --libdir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr/lib/aarch64-poky-linux --includedir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr/include --oldincludedir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr/include --infodir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr/share/info --mandir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-pokysdk-linux/usr/share/man --disable-silent-rules --disable-dependency-tracking --with-libtool-sysroot=/home/HDWD110/yocto/imx-5.10.72-2.2.2-20220712/build--fsl-imx-xwayland/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-aarch64/10.2.0-r0/recipe-sysroot --with-gnu-ld --enable-shared --enable-languages=c,c++ --enable-threads=posix --enable-multilib --enable-default-pie --enable-c99 --enable-long-long --enable-symvers=gnu --enable-libstdcxx-pch --program-prefix=aarch64-poky-linux- --without-local-prefix --disable-install-libiberty --disable-libssp --enable-libitm --enable-lto --disable-bootstrap --with-system-zlib --with-linker-hash-style=gnu --enable-linker-build-id --with-ppl=no --with-cloog=no --enable-checking=release --enable-cheaders=c_global --without-isl --with-gxx-include-dir=/not/exist/usr/include/c++/10.2.0 --with-build-time-tools=/home/HDWD110/yocto/imx-5.10.72-2.2.2-20220712/build--fsl-imx-xwayland/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-aarch64/10.2.0-r0/recipe-sysroot-native/usr/aarch64-poky-linux/bin --with-sysroot=/not/exist --with-build-sysroot=/home/HDWD110/yocto/imx-5.10.72-2.2.2-20220712/build--fsl-imx-xwayland/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-aarch64/10.2.0-r0/recipe-sysroot --enable-poison-system-directories --disable-static --enable-nls --with-glibc-version=2.28 --enable-initfini-array --enable-__cxa_atexit
    Thread model: posix
    Supported LTO compression algorithms: zlib
    gcc version 10.2.0 (GCC) 

Compiling Boot Files
----------------------

Compiling U-Boot Files
~~~~~~~~~~~~~~~~~~~~~~~~

1. Prepare the U-Boot source package file

| 　　① Open the network drive to "3.2_OS_Linux-5.10.72 -> 02_source" and download "uboot-2021.04\*.tar.bz2".
| 　　② Transfer the file "uboot-2021.04\*.tar.bz2" to the x86_64 Linux host.

2. Extract the source package

.. code-block:: shell

    # =====> Input:
    tar xf uboot-2021.04*.tar.bz2 -C ~/work/linux/imx-linux-5.10.72

3. Configure the compilation tool environment variables

.. code-block:: shell

    # =====> Input:
    source ~/work/toolchain/gcc-linaro/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu.env

4. Compile the target file

.. code-block:: shell

    cd ~/work/linux/imx-linux-5.10.72/uboot-2021.04
    make myimx8mpek314_defconfig O=build
    cd build
    make -j24

5. Description of the target file

　　u-boot-nodtb.bin, spl/u-boot-spl.bin, and arch/arm/dts/myimx8mpek314.dtb are the target files, which will be dependent on when compiling the Boot file in the next step.

Compiling Boot Files
~~~~~~~~~~~~~~~~~~~~~~

1. Prepare the Boot compilation tool

　　Transfer the file "mkimage-5.10.72\*.tar.bz2" to the x86\_64 Linux host.

2. Extract the Boot compilation tool

.. code-block:: shell

    # =====> Input:
    tar xf mkimage-5.10.72*.tar.bz2 -C ~/work/linux/imx-linux-5.10.72

3. Compile the Boot file

.. code-block:: shell

    cd ~/work/linux/imx-linux-5.10.72/mkimage-5.10.72
    make SOC=iMX8MP dtbs=myimx8mpek314.dtb flash_ddr4_evk OUTIMG=boot-myimx8mpek314.bin

4. Description of the target file

　　iMX8M/boot-myimx8mpek314.bin is the target file, and you can replace the file with the same name in the burning tool with the compiled target file.  


Compiling the Linux Kernel
----------------------------

1. Prepare the Linux source code package file

　　Transfer the file "imx-linux-5.10.72\*.tar.bz2" to the x86\_64 Linux host.

2. Extract the source code package

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

- The output information during the Image compilation process is similar to the following:

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
    make myzr/myimx8mpek314.dtb myzr/myimx8mpek314-ov2775-ov5640.dtb

- When the device tree is successfully compiled for the first time, the output information is similar to the following:

.. code:: shell

    DTC     arch/arm64/boot/dts/myzr/myimx8mpek314.dtb
    DTC     arch/arm64/boot/dts/myzr/myimx8mpek314-ov2775-ov5640.dtb


- Compiling the Linux MIPI Screen Device Tree File 

- Execute the compilation

.. code-block:: shell

    # =====> Input:
    make myzr/myimx8mpek314-mipi.dtb

- When the device tree is successfully compiled for the first time, the output information is similar to the following:

.. code:: text

   DTC     arch/arm64/boot/dts/myzr/myimx8mpek314-mipi.dtb 

- On the ARM board, mount `mmcblk2p1` with the following operation:

.. code-block:: shell

    mount /dev/mmcblk2p1 /mnt/

- Upload the compiled `myimx8mpek314-mipi.dtb` file to the `/mnt` directory of the ARM board.


- Restart the ARM board, and press `Enter` to enter `uboot` during the startup process.

- Enter the following commands in `uboot`:

.. code-block:: shell

  # =====> Input:
  setenv fdtfile myimx8mpek314-mipi.dtb
  saveenv
  boot


6. Compile the Linux Module

- Execute the compilation

.. code-block:: shell

    # =====> Input:
    make modules -j24

- The output information when the module compilation is successful is similar to the following:

.. code:: text

    ......
    LD [M]  sound/usb/snd-usb-audio.ko
    LD [M]  sound/usb/snd-usbmidi-lib.ko

- Install the kernel module to the specified directory

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

7. Description of Target Files

　　Image, myimx8mpek314.dtb, myimx8mpek314-ov2775-ov5640.dtb, and kernel-modules.tar.bz2 are the target files. You can replace the files with the same names in the flashing tool with the compiled target files.
