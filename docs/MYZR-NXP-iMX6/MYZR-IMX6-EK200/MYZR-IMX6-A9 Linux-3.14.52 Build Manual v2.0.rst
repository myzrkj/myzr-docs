MYZR-IMX6-A9 Linux-3.14.52 Build Manual v2.0
================================================

Download relevant documents
-----------------------------

**Cross-compile tool chain**

|   A9 series：Open the network disk to 2.2_OS_Linux-3.14.52 -> 03_toolchain，Download MY-IMX-A9 Directory.

**Source code**

|   u-boot：Open the network disk to 2.2_OS_Linux-3.14.52 -> 02_source，Download u-boot-2016.03-\*.tar.bz2 (Source package version number svn315 and above).
|   Kernel：Open the network disk to 2.2_OS_Linux-3.14.52 -> 02_source，Download linux-3.14.52-\*.tar.bz2 (Source package version number svn369 and above).


Install cross compilation tool chain
----------------------------------------

1. Execute installation

.. code-block:: shell

    =====> Input:
    ./fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1.sh 

    =====> Output: 
    Enter target directory for SDK (default: /opt/fsl-imx-fb/3.14.52-1.1.1):
    =====> Input:
    /home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1
    =====> Output: 
    You are about to install the SDK to "/home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1". Proceed[Y/n]?
    =====> Input:
    y
    =====> Output: 
    Extracting SDK...done
    Setting it up...done
    SDK has been successfully set up and is ready to be used.

2. source Toolchain Profile

.. code-block:: shell

    =====> Input:
    source /home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1/environment-setup-cortexa9hf-vfp-neon-poky-linux-gnueabi

3. Verify cross compilation tool installation

.. code-block:: shell

    =====> Input:
    $CC -v
    
    =====> Output:
    Using built-in specs.
    COLLECT_GCC=arm-poky-linux-gnueabi-gcc
    COLLECT_LTO_WRAPPER=/home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1/sysroots/x86_64-pokysdk-
    linux/usr/bin/arm-poky-linux-gnueabi/../../libexec/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/4.9.2/lto-wrapper
    Target: arm-poky-linux-gnueabi
    Configured with: /home/myzr/my-yocto/imx-3.14.52-1.1.0_ga/imx6qdlsolo__fsl-imx-fb/tmp/work-shared/gcc-4.9.2-r0/gcc-4.9.2/configure --build=x86_64-linux --host=x86_64-
    pokysdk-linux --target=arm-poky-linux-gnueabi --prefix=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr --exec_prefix=/opt/fsl-imx-fb/3.14.52-
    1.1.1/sysroots/x86_64-pokysdk-linux/usr --bindir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi --sbindir=/opt/fsl-imx-
    fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi --libexecdir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr/libexec/arm-
    poky-linux-gnueabi --datadir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr/share --sysconfdir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-
    linux/etc --sharedstatedir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/com --localstatedir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/var
    --libdir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr/lib/arm-poky-linux-gnueabi --includedir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-
    linux/usr/include --oldincludedir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr/include --infodir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-
    linux/usr/share/info --mandir=/opt/fsl-imx-fb/3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr/share/man --disable-silent-rules --disable-dependency-tracking --with-
    libtool-sysroot=/home/myzr/my-yocto/imx-3.14.52-1.1.0_ga/imx6qdlsolo__fsl-imx-fb/tmp/sysroots/x86_64-nativesdk-pokysdk-linux --with-gnu-ld --enable-shared --enable-
    languages=c,c++ --enable-threads=posix --enable-multilib --enable-c99 --enable-long-long --enable-symvers=gnu --enable-libstdcxx-pch --program-prefix=arm-poky-linux-
    gnueabi- --without-local-prefix --enable-target-optspace --enable-lto --enable-libssp --disable-bootstrap --disable-libmudflap --with-system-zlib --with-linker-hash-
    style=gnu --enable-linker-build-id --with-ppl=no --with-cloog=no --enable-checking=release --enable-cheaders=c_global --with-gxx-include-
    dir=/not/exist/usr/include/c++/4.9.2 --with-build-time-tools=/home/myzr/my-yocto/imx-3.14.52-1.1.0_ga/imx6qdlsolo__fsl-imx-fb/tmp/sysroots/x86_64-linux/usr/arm-poky-linux-
    gnueabi/bin --with-sysroot=/not/exist --with-build-sysroot=/home/myzr/my-yocto/imx-3.14.52-1.1.0_ga/imx6qdlsolo__fsl-imx-fb/tmp/sysroots/imx6qdlsolo --enable-poison-
    system-directories --with-mpfr=/home/myzr/my-yocto/imx-3.14.52-1.1.0_ga/imx6qdlsolo__fsl-imx-fb/tmp/sysroots/x86_64-nativesdk-pokysdk-linux --with-mpc=/home/myzr/my-
    yocto/imx-3.14.52-1.1.0_ga/imx6qdlsolo__fsl-imx-fb/tmp/sysroots/x86_64-nativesdk-pokysdk-linux --enable-nls --with-arch=armv7-a
    Thread model: posix
    gcc version 4.9.2 (GCC)

u-boot compilation
---------------------

**Preparation before compilation**

- Create a compile working directory

.. code-block:: shell

  =====> Input:
  mkdir ~/my-work/02_source/ -p

- Unpack source code to working directory

.. code-block:: shell

  =====> Input:
  tar xf u-boot-2016.03-svn*.tar.bz2 -C ~/my-work/02_source/

**Compilation of u-book target files**

- Enter source directory

.. code-block:: shell

  =====> Input:
  cd ~/my-work/02_source/u-boot-2016.03

- Generate the target development board ”. config“ file

.. code-block:: shell

  =====> Input:
  make myimx6ek200-6q-1g_defconfig

  =====> Output: 
    HOSTCC  scripts/basic/fixdep
    HOSTCC  scripts/kconfig/conf.o
    SHIPPED scripts/kconfig/zconf.tab.c
    SHIPPED scripts/kconfig/zconf.lex.c
    SHIPPED scripts/kconfig/zconf.hash.c
    HOSTCC  scripts/kconfig/zconf.tab.o
    HOSTLD  scripts/kconfig/conf
  #
  # configuration written to .config
  #

| 【Note】： myimx6ek200-6q-1g_defconfig after make is changed to a configuration file corresponding to the development board model.

.. code-block:: shell

  ********** MYZR-IMX6-EK200 **********
  myimx6ek200-6q-1g_defconfig     myimx6ek200-6q-2g_defconfig     myimx6ek200-6q-512m_defconfig  
  myimx6ek200-6u-1g_defconfig     myimx6ek200-6u-2g_defconfig     myimx6ek200-6u-512m_defconfig  
  myimx6ek200-6s-512m_defconfig   myimx6ek200-6s-1g_defconfig     myimx6ek200-6s-128m_defconfig  
  myimx6ek200-6qp-1g_defconfig    myimx6ek200-6qp-2g_defconfig    myimx6ek200-6qp-512m_defconfig  

  ********** MYZR-IMX6-EK314 **********
  myimx6ek314-6q-1g_defconfig     myimx6ek314-6q-2g_defconfig     myimx6ek314-6q-512m_defconfig  
  myimx6ek314-6u-1g_defconfig     myimx6ek314-6u-2g_defconfig     myimx6ek314-6u-512m_defconfig  
  myimx6ek314-6s-512m_defconfig   myimx6ek314-6s-1g_defconfig     myimx6ek314-6s-128m_defconfig  
  myimx6ek314-6qp-1g_defconfig    myimx6ek314-6qp-2g_defconfig    myimx6ek314-6qp-512m_defconfig  

  ********** MYZR-IMX6-EK336 **********
  myimx6ek336-6q-1g_defconfig     myimx6ek336-6q-2g_defconfig     myimx6ek336-6q-512m_defconfig  

- Compiling

.. code-block:: shell

  =====> Input:
  make 

  =====> Output: 
  scripts/kconfig/conf  --silentoldconfig Kconfig
    CHK     include/config.h
    UPD     include/config.h
    GEN     include/autoconf.mk
    GEN     include/autoconf.mk.dep
    CHK     include/config/uboot.release
    CHK     include/generated/timestamp_autogenerated.h
    CFG     u-boot.cfg
    ......
    LD      u-boot
    OBJCOPY u-boot-nodtb.bin
    OBJCOPY u-boot.srec
    SYM     u-boot.sym
    COPY    u-boot.bin
    CFGS    board/myzr/myimx6/myimx6a9-6q-ddr3.cfg.cfgtmp
    MKIMAGE u-boot.imx

**Note: If there's a hint “cc1: error”，Usually the configuration of the cross-compilation tool does not work, and you can perform this step after pressing the "source toolchain configuration file" operation in the previous "cross compilation tool chain installation".**

- u-boot Target File

| u-boot.imxis the target file.

**Compile U-boot environment variable scripts**

.. code-block:: shell

  =====> Input:
  mkimage -A arm -O linux -T script -C none -a 0 -e 0 -n "myzr bootscripts" -d board/myzr/bootscripts/myimx6a9_l31452_script.cmd my_environment.scr

  =====> Output: 
  Image Name:   myzr bootscripts
  Created:      Wed Jan  2 09:40:07 2019
  Image Type:   ARM Linux Script (uncompressed)
  Data Size:    2327 Bytes = 2.27 kB = 0.00 MB
  Load Address: 00000000
  Entry Point:  00000000
  Contents:
     Image 0: 2319 Bytes = 2.26 kB = 0.00 MB

**Target File**

| "u-boot.imx "and "my_environment_emmc.scr" That is, the compiled target files, save the two files


Kernel compilation
-------------------

**Preparation before compilation**

- Create a compile working directory

.. code-block:: shell

  =====> Input:
  mkdir ~/my-work/02_source/ -p

- Unpack source code to working directory

.. code-block:: shell

  =====> Input:
  tar xf linux-3.14.52-svn*.tar.bz2 -C ~/my-work/02_source/

**Compiles kernel target files**

- Enter the kernel source directory

.. code-block:: shell

  =====> Input:
  cd ~/my-work/02_source/linux-3.14.52

- To generate the target platform .config file

.. code-block:: shell

  =====> Input:
  make myimx6a9_defconfig

  =====> Output: 
    HOSTCC  scripts/basic/fixdep
    HOSTCC  scripts/kconfig/conf.o
    SHIPPED scripts/kconfig/zconf.tab.c
    SHIPPED scripts/kconfig/zconf.lex.c
    SHIPPED scripts/kconfig/zconf.hash.c
    HOSTCC  scripts/kconfig/zconf.tab.o
    HOSTLD  scripts/kconfig/conf
  #
  # configuration written to .config
  #

**Note: If there is an error in“Can't find default configuration "arch/x86/configs” ，it is because the configuration of the cross-compilation tool chain is not effective. You can do this after pressing the Source Toolchain Profile in the previous Cross Compiler Toolchain Installation**

- Compiles kernel target files

.. code-block:: shell

  =====> Input:
  make zImage

  =====> Output: 
  scripts/kconfig/conf --silentoldconfig Kconfig
    CHK     include/config/kernel.release
    UPD     include/config/kernel.release
    WRAP    arch/arm/include/generated/asm/auxvec.h
    ......
    AS      arch/arm/boot/compressed/piggy.lzo.o
    LD      arch/arm/boot/compressed/vmlinux
    OBJCOPY arch/arm/boot/zImage
    Kernel: arch/arm/boot/zImage is ready

- Kernel target file

| arch/arm/boot/zImage is the kernel target file

**Build Device Tree Target File**

- Execute compile command

.. code-block:: shell

  =====> Input:
  make myimx6ek200-6q-1g.dtb

  =====> Output: 
    DTC     arch/arm/boot/dts/myimx6ek200-6q-1g.dtb
  
| 【Note】：The myimx6ek200-6q-1g.dtb after make is changed to the configuration file corresponding to the development board model.

.. code-block:: shell

  ********** MYZR-IMX6-EK200 **********
  myimx6ek200-6q-1g.dtb     myimx6ek200-6q-2g.dtb     myimx6ek200-6q-512m.dtb  
  myimx6ek200-6u-1g.dtb     myimx6ek200-6u-2g.dtb     myimx6ek200-6u-512m.dtb  
  myimx6ek200-6s-512m.dtb   myimx6ek200-6s-1g.dtb     myimx6ek200-6s-128m.dtb  
  myimx6ek200-6qp-1g.dtb    myimx6ek200-6qp-2g.dtb    myimx6ek200-6qp-512m.dtb  

  ********** MY-IMX6-EK314 **********
  myimx6ek314-6q-1g.dtb     myimx6ek314-6q-2g.dtb     myimx6ek314-6q-512m.dtb  
  myimx6ek314-6u-1g.dtb     myimx6ek314-6u-2g.dtb     myimx6ek314-6u-512m.dtb  
  myimx6ek314-6s-512m.dtb   myimx6ek314-6s-1g.dtb     myimx6ek314-6s-128m.dtb  
  myimx6ek314-6qp-1g.dtb    myimx6ek314-6qp-2g.dtb    myimx6ek314-6qp-512m.dtb  

  ********** MYZR-IMX6-EK336 **********
  myimx6ek336-6q-1g.dtb     myimx6ek336-6q-2g.dtb     myimx6ek336-6q-512m.dtb  

- Copy the device tree target file

.. code-block:: shell

  =====> Input:
  cp arch/arm/boot/dts/myimx6ek200-6q-1g.dtb ./

**Build kernel module package**

- Compiling

.. code-block:: shell

  =====> Input:
  make modules

  =====> Output: 
    CHK     include/config/kernel.release
    CHK     include/generated/uapi/linux/version.h
    CHK     include/generated/utsrelease.h
  make[1]: “include/generated/mach-types.h"Is the latest.
    CALL    scripts/checksyscalls.sh
    ......
    LD [M]  sound/core/snd-rawmidi.ko
    LD [M]  sound/usb/snd-usb-audio.ko
    LD [M]  sound/usb/snd-usbmidi-lib.ko

- Create a save directory for the kernel module

.. code-block:: shell

  =====> Input:
  mkdir modules

- Install kernel module to specified directory

.. code-block:: shell

  =====> Input:
  make modules_install INSTALL_MOD_PATH=./modules

  =====> Output: 
    INSTALL crypto/tcrypt.ko
    INSTALL drivers/i2c/algos/i2c-algo-pca.ko
    ......
    INSTALL sound/usb/snd-usbmidi-lib.ko
    DEPMOD  3.14.52-myimx6-svn369

- Package the kernel module files

.. code-block:: shell

  =====> Input:
  tar cjf kernel-modules.tar.bz2 -C modules lib

**Target File**

| zImage、myimx6ek*.dtb and ernel-modules.tar.bz2 is the target file compiled and the three files are saved.


Linux C Program compilation
------------------------------

**Prepare source code**

| Open the disk to 5_MY-Demo -> MY-Linux-C-Demo，download hello.c file and copy to virtual machine.

**Compile the target file**

.. code-block:: shell

  =====> Input:
  $CC hello.c -o hello.out

| Note: If you have "no command found" information because the configuration of the cross-compilation tool chain is not effective, you can perform this step after pressing the "source tool chain profile" operation in the previous "cross compilation tool chain installation"

**Run Linux C Target Program**

| Copy the compiled hello.out to the development board
| Run the Linux C target program on the development board

.. code-block:: shell

  =====> Input:
  chmod +x ./hello.out
  ./hello.out

  =====> Output:
  MYZR Technology Co.,Ltd.

  Web:  http://www.myzr.com.cn/
  Wiki: http://wiki.myzr.com.cn/
  BBS:  http://bbs.myzr.com.cn/

  Tel: 0756-3628023/3628021
  E-mail: service@myzr.com.cn

Linux QT5 program compilation
--------------------------------

**Prepare source code**

| Open the disk to 5_MY-Demo，Download MY-Linux-QT5-Demo-AboutUs-svn*.tar.bz2 file and copy to virtual machine.

.. code-block:: shell

  =====> Input:
  tar xf MY-Linux-QT5-Demo-AboutUs-svn*.tar.bz2 -C ~/my-work/02_source/


- QT Program compilation

**QT Program compilation**

- Enter source directory

.. code-block:: shell

  =====> Input:
  cd ~/my-work/02_source/AboutUs/

- Generate Makefile file

.. code-block:: shell

  =====> Input:
  qmake

| Note: If there is information that the 'qamke' command is not found because the configuration of the cross-compilation tool chain is not effective, you can perform this step after pressing the "source tool chain configuration file" operation in the previous "cross compilation tool chain installation"

**Compile the target file**

.. code-block:: shell

  =====> Input:
  make

  =====> Output: 
  /home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr/bin/qt5/uic widget.ui -o ui_widget.h
  ......
  arm-poky-linux-gnueabi-g++  -march=armv7-a -mfloat-abi=hard -mfpu=neon -mtune=cortex-a9 --sysroot=/home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1/sysroots/cortexa9hf-vfp-neon-poky-linux-gnueabi -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed -Wl,-O1 -o AboutUs main.o widget.o qrc_source.o moc_widget.o   -lQt5Widgets -lQt5Gui -lQt5Core -lGLESv2 -lEGL -lpthread 

**Run on MI-IMX6-A9 device**

| Copy the compiled AboutUs to the development board
| Run QT5 target program on development board

.. code-block:: shell

  =====> Input:
  chmod +x ./AboutUs
  ./AboutUs -platform eglfs

**Running results**

| You can see that the MYZR logo and some information are output on the development board display.