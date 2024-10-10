Linux-3.14.52 编译参考手册 v2.0
================================

下载相关文件
-------------

**交叉编译工具链**

|   A9系列：打开网盘到 2.2_OS_Linux-3.14.52 -> 03_toolchain，下载 MY-IMX-A9 目录。

**源码**

|   u-boot：打开网盘到 2.2_OS_Linux-3.14.52 -> 02_source，下载 u-boot-2016.03-\*.tar.bz2 (源码包版本号需svn315及以上)。
|   Kernel：打开网盘到 2.2_OS_Linux-3.14.52 -> 02_source，下载 linux-3.14.52-\*.tar.bz2 (源码包版本号需svn369及以上) 。


安装交叉编译工具链
-------------------

- 执行安装

.. code:: shell

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

- source 工具链配置文件

.. code:: shell

    =====> Input:
    source /home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1/environment-setup-cortexa9hf-vfp-neon-poky-linux-gnueabi

- 检验交叉编译工具安装

.. code:: shell

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

**Note: CC是设置的宏，$CC中的"$"不能去掉**


u-boot编译
------------

**编译前的准备**

- 创建编译工作目录

.. code:: shell

  =====> Input:
  mkdir ~/my-work/02_source/ -p

- 解压源码包到工作目录

.. code:: shell

  =====> Input:
  tar xf u-boot-2016.03-svn*.tar.bz2 -C ~/my-work/02_source/

**编译u-boot目标文件**

- 进入源码目录

.. code:: shell

  =====> Input:
  cd ~/my-work/02_source/u-boot-2016.03

- 生成目标开发板的 .config 文件

.. code:: shell

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

| 【注意】：上面 **make** 后面的 **myimx6ek200-6q-1g_defconfig** 改为与开发板型号对应的配置文件。

.. code:: shell

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

- 执行编译

.. code:: shell

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

**Note: 如果有提示 “cc1: error”，通常是交叉编译工具的配置没生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤。**

- u-boot 目标文件

**u-boot.imx** 即目标文件。

**编译u-boot环境变量脚本**

.. code:: shell

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

**目标文件**

| u-boot.imx 和 my_environment.scr 即编译得到的目标文件，保存这两个文件


内核编译
---------

**编译前的准备**

- 创建编译工作目录

.. code:: shell

  =====> Input:
  mkdir ~/my-work/02_source/ -p

- 解压源码包到工作目录

.. code:: shell

  =====> Input:
  tar xf linux-3.14.52-svn*.tar.bz2 -C ~/my-work/02_source/

**编译内核目标文件**

- 进入内核源码目录

.. code:: shell

  =====> Input:
  cd ~/my-work/02_source/linux-3.14.52

- 生成目标平台的 .config 文件

.. code:: shell

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

**Note: 如果有“Can't find default configuration "arch/x86/configs” 的错误，是因为交叉编译工具链的配置没有生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤**

- 编译内核目标文件

.. code:: shell

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

- 内核目标文件

| arch/arm/boot/zImage 即内核目标文件

**编译设备树目标文件**

- 执行编译命令

.. code:: shell

  =====> Input:
  make myimx6ek200-6q-1g.dtb

  =====> Output: 
    DTC     arch/arm/boot/dts/myimx6ek200-6q-1g.dtb
  【注意】：上面 make 后面的 myimx6ek200-6q-1g.dtb 改为与开发板型号对应的配置文件。

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

- 复制设备树目标文件

.. code:: shell

  =====> Input:
  cp arch/arm/boot/dts/myimx6ek200-6q-1g.dtb ./

**编译内核模块包**

- 执行编译

.. code:: shell

  =====> Input:
  make modules

  =====> Output: 
    CHK     include/config/kernel.release
    CHK     include/generated/uapi/linux/version.h
    CHK     include/generated/utsrelease.h
  make[1]: “include/generated/mach-types.h”是最新的。
    CALL    scripts/checksyscalls.sh
    ......
    LD [M]  sound/core/snd-rawmidi.ko
    LD [M]  sound/usb/snd-usb-audio.ko
    LD [M]  sound/usb/snd-usbmidi-lib.ko

- 创建内核模块的保存目录

.. code:: shell

  =====> Input:
  mkdir modules

- 安装内核模块到指定目录

.. code:: shell

  =====> Input:
  make modules_install INSTALL_MOD_PATH=./modules

  =====> Output: 
    INSTALL crypto/tcrypt.ko
    INSTALL drivers/i2c/algos/i2c-algo-pca.ko
    ......
    INSTALL sound/usb/snd-usbmidi-lib.ko
    DEPMOD  3.14.52-myimx6-svn369

- 打包内核模块文件

.. code:: shell

  =====> Input:
  tar cjf kernel-modules.tar.bz2 -C modules lib

**目标文件**

| zImage、myimx6ek*.dtb 和 kernel-modules.tar.bz2 即编译得到的目标文件，保存这三个文件


Linux C程序编译
----------------

**准备源码**

| 打开网盘到 5_MY-Demo -> MY-Linux-C-Demo，下载 hello.c 文件，并复制到虚拟机。

**编译目标文件**

.. code:: shell

  =====> Input:
  $CC hello.c -o hello.out

.. attention::

  Note: 如果有“未找到命令”的信息，是因为交叉编译工具链的配置没有生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤

**运行Linux C目标程序**

| 把编译得到的 hello.out 复制到开发板上
| 在开发板上运行Linux C目标程序

.. code:: shell

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

Linux QT5程序编译
-------------------

**准备源码**

| 打开网盘到 5_MY-Demo，下载 MY-Linux-QT5-Demo-AboutUs-svn*.tar.bz2 文件，并复制到虚拟机。

- 解压源码包到工作目录

.. code:: shell

  =====> Input:
  tar xf MY-Linux-QT5-Demo-AboutUs-svn*.tar.bz2 -C ~/my-work/02_source/

**QT程序编译**

- 进入源码目录

.. code:: shell

  =====> Input:
  cd ~/my-work/02_source/AboutUs/

- 生成Makefile文件

.. code:: shell

  =====> Input:
  qmake

| Note: 如果有“未找到 'qamke' 命令”的信息，是因为交叉编译工具链的配置没有生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤

**编译目标文件**

.. code:: shell

  =====> Input:
  make

  =====> Output: 
  /home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1/sysroots/x86_64-pokysdk-linux/usr/bin/qt5/uic widget.ui -o ui_widget.h
  ......
  arm-poky-linux-gnueabi-g++  -march=armv7-a -mfloat-abi=hard -mfpu=neon -mtune=cortex-a9 --sysroot=/home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-vfp-neon-toolchain-3.14.52-1.1.1/sysroots/cortexa9hf-vfp-neon-poky-linux-gnueabi -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed -Wl,-O1 -o AboutUs main.o widget.o qrc_source.o moc_widget.o   -lQt5Widgets -lQt5Gui -lQt5Core -lGLESv2 -lEGL -lpthread 

**在 MYZR-IMX6-A9 设备上运行**

| 把编译得到的 AboutUs 复制到开发板上
| 在开发板上运行QT5目标程序

.. code:: shell

  =====> Input:
  chmod +x ./AboutUs
  ./AboutUs -platform eglfs

**运行结果**

| 可以看到开发板显示屏上输出了 MYZR 的 Logo 和一些信息。

在文件系统增加自己的应用
------------------------

**准备工作**

- 创建编译工作目录

.. code:: shell

  =====> Input:
  mkdir ~/my-work/04_image -p

- 将烧录工具上的文件系统 Profiles\Linux\OS Firmware\image-L3.14.52-rootfs\L31452-\*-myimx6a9.tar.bz2 复制到 ~/my-work/04_image
- 创建存放文件系统的目录

.. code:: shell

  =====> Input:
  mkdir  L31452-fsl-image-qt5-myimx6a9

| 【注意】：上面的 L31452-fsl-image-qt5-myimx6a9 改为与文件系统压缩包对应的名称。

.. code:: shell

  L31452-fsl-image-qt5-myimx6a9
  L31452-fsl-image-machine-myimx6a9
  L31452-core-image-base-myimx6a9

| 解压文件系统压缩包并进入到解压目录

.. code:: shell

  =====> Input:
  tar jxvf L31452-*-myimx6a9.tar.bz2 -C L31452-*-myimx6a9/
  cd L31452-*-myimx6a9

- 创建存放应用的目录并将应用复制到此目录

.. code:: shell

  =====> Input:
  mkdir my-demo 
  cp /home/myzr/my-work/02_source/hello.out my-demo

- 重新压缩文件系统

.. code:: shell

  =====> Input:
  sudo tar cjvf ../L31452-fsl-image-qt5-myimx6a9.tar.bz2 *
  cd ..

| 【注意】：上面的 L31452-fsl-image-qt5-myimx6a9.tar.bz2 改为文件系统压缩包对应的名称。

.. code:: shell

  L31452-fsl-image-qt5-myimx6a9.tar.bz2
  L31452-fsl-image-machine-myimx6a9.tar.bz2
  L31452-core-image-base-myimx6a9.tar.bz2

| 最后将压缩好的包复制到烧录工具相应的目录进行烧写

::

  --------------------------------------------------------------------------------
  * 珠海明远智睿科技有限公司  
  * ZhuHai MYZR Technology CO.,LTD.
  * Latest Update: 2019/01/02  
  * Supporter: Tang Bin
  --------------------------------------------------------------------------------