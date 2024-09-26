MYZR-IMX Linux-4.9.88 编译参考手册
===================================

必要的说明
-----------

|  A7系列 包括 MYZR-IMX6-EK140、MYZR-IMX6-EK140P。
|  A9系列 包括 MYZR-IMX6-EK200、MYZR-IMX6-EK314、MYZR-IMX6-EK336。


下载相关的文件
---------------

**交叉编译工具链**

|  A7系列：打开网盘到 2.4_OS_Linux-4.9.88 -> 03_toolchain，下载 MY-IMX-A7 目录。
|  A9系列：打开网盘到 2.4_OS_Linux-4.9.88 -> 03_toolchain，下载 MY-IMX-A9 目录。

**源码**

|  u-boot：打开网盘到 2.4_OS_Linux-4.9.88 -> 02_source，下载 u-boot-2016.03-\*.tar.bz2。
|  Kernel：打开网盘到 2.4_OS_Linux-4.9.88 -> 02_source，下载 linux-4.9.88-\*.tar.bz2。


安装交叉编译工具链
-------------------

MYZR-IMX-A7 系列交叉编译工具链安装
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 执行安装

.. code:: shell

  =====> Input:
  ./fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0.sh
  
  =====> Output: 
  NXP i.MX Release Distro SDK installer version 4.9.88-2.0.0
  ==========================================================
  Enter target directory for SDK (default: /opt/fsl-imx-x11/4.9.88-2.0.0): 
  =====> Input:
  /home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0
  
  =====> Output: 
  You are about to install the SDK to "/home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0". Proceed[Y/n]? 
  =====> Input:
  y
  
  =====> Output: 
  Extracting SDK....................................................................................................................................................................................................done
  Setting it up...done
  SDK has been successfully set up and is ready to be used.
  Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
   $ . /home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/environment-setup-cortexa7hf-neon-poky-linux-gnueabi

2. source 工具链配置文件

.. code:: shell

  =====> Input:
  source /home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/environment-setup-cortexa7hf-neon-poky-linux-gnueabi

3. 检验交叉编译工具安装

.. code:: shell

  =====> Input:
  $CC -v

  =====> Output: 
  Using built-in specs.
  COLLECT_GCC=arm-poky-linux-gnueabi-gcc
  COLLECT_LTO_WRAPPER=/home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/libexec/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/lto-wrapper
  Target: arm-poky-linux-gnueabi
  Configured with: ../../../../../../work-shared/gcc-7.3.0-r0/gcc-7.3.0/configure --build=x86_64-linux --host=x86_64-pokysdk-linux --target=arm-poky-linux-gnueabi --prefix=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr --exec_prefix=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr --bindir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi --sbindir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi --libexecdir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/libexec/arm-poky-linux-gnueabi --datadir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/share --sysconfdir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/etc --sharedstatedir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/com --localstatedir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/var --libdir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/lib/arm-poky-linux-gnueabi --includedir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/include --oldincludedir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/include --infodir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/share/info --mandir=/opt/fsl-imx-x11/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/share/man --disable-silent-rules --disable-dependency-tracking --with-libtool-sysroot=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6ul7d__fsl-imx-x11/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot --with-gnu-ld --enable-shared --enable-languages=c,c++ --enable-threads=posix --enable-multilib --enable-c99 --enable-long-long --enable-symvers=gnu --enable-libstdcxx-pch --program-prefix=arm-poky-linux-gnueabi- --without-local-prefix --enable-lto --enable-libssp --enable-libitm --disable-bootstrap --disable-libmudflap --with-system-zlib --with-linker-hash-style=gnu --enable-linker-build-id --with-ppl=no --with-cloog=no --enable-checking=release --enable-cheaders=c_global --without-isl --with-gxx-include-dir=/not/exist/usr/include/c++/7.3.0 --with-build-time-tools=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6ul7d__fsl-imx-x11/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot-native/usr/arm-poky-linux-gnueabi/bin --with-sysroot=/not/exist --with-build-sysroot=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6ul7d__fsl-imx-x11/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot --without-long-double-128 --enable-poison-system-directories --with-mpfr=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6ul7d__fsl-imx-x11/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot --with-mpc=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6ul7d__fsl-imx-x11/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot --enable-nls --enable-initfini-array
  Thread model: posix
  gcc version 7.3.0 (GCC) 

MYZR-IMX-A9 系列交叉编译工具链安装
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 执行安装

.. code:: shell

  =====> Input:
  ./fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-neon-toolchain-4.9.88-2.0.0.sh

  =====> Output: 
  NXP i.MX Release Distro SDK installer version 4.9.88-2.0.0
  ==========================================================
  Enter target directory for SDK (default: /opt/fsl-imx-x11/4.9.88-2.0.0): 
  =====> Input:
  /home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-neon-toolchain-4.9.88-2.0.0

  =====> Output: 
  You are about to install the SDK to "/home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-neon-toolchain-4.9.88-2.0.0
  ". Proceed[Y/n]? 
  =====> Input:
  y

  =====> Output: 
  Extracting SDK..................................................................................................................................................................................................done
  Setting it up...done
  SDK has been successfully set up and is ready to be used.
  Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
   $ . /home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-neon-toolchain-4.9.88-2.0.0/environment-setup-cortexa9hf-neon-poky-linux-gnueabi

2. source 工具链配置文件

.. code:: shell

  =====> Input:
  source /home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-neon-toolchain-4.9.88-2.0.0/environment-setup-cortexa9hf-neon-poky-linux-gnueabi 

3. 检验交叉编译工具安装

.. code:: shell

  =====> Input:
  $CC -v

  =====> Output: 
  Using built-in specs.
  COLLECT_GCC=arm-poky-linux-gnueabi-gcc
  COLLECT_LTO_WRAPPER=/home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-neon-toolchain-4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/libexec/arm-poky-linux-gnueabi/gcc/arm-poky-linux-gnueabi/7.3.0/lto-wrapper
  Target: arm-poky-linux-gnueabi
  Configured with: ../../../../../../work-shared/gcc-7.3.0-r0/gcc-7.3.0/configure --build=x86_64-linux --host=x86_64-pokysdk-linux --target=arm-poky-linux-gnueabi --prefix=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr --exec_prefix=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr --bindir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi --sbindir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/bin/arm-poky-linux-gnueabi --libexecdir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/libexec/arm-poky-linux-gnueabi --datadir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/share --sysconfdir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/etc --sharedstatedir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/com --localstatedir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/var --libdir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/lib/arm-poky-linux-gnueabi --includedir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/include --oldincludedir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/include --infodir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/share/info --mandir=/opt/fsl-imx-fb/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/share/man --disable-silent-rules --disable-dependency-tracking --with-libtool-sysroot=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6qpdlsolox__fsl-imx-fb/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot --with-gnu-ld --enable-shared --enable-languages=c,c++ --enable-threads=posix --enable-multilib --enable-c99 --enable-long-long --enable-symvers=gnu --enable-libstdcxx-pch --program-prefix=arm-poky-linux-gnueabi- --without-local-prefix --enable-lto --enable-libssp --enable-libitm --disable-bootstrap --disable-libmudflap --with-system-zlib --with-linker-hash-style=gnu --enable-linker-build-id --with-ppl=no --with-cloog=no --enable-checking=release --enable-cheaders=c_global --without-isl --with-gxx-include-dir=/not/exist/usr/include/c++/7.3.0 --with-build-time-tools=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6qpdlsolox__fsl-imx-fb/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot-native/usr/arm-poky-linux-gnueabi/bin --with-sysroot=/not/exist --with-build-sysroot=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6qpdlsolox__fsl-imx-fb/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot --without-long-double-128 --enable-poison-system-directories --with-mpfr=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6qpdlsolox__fsl-imx-fb/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot --with-mpc=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx6qpdlsolox__fsl-imx-fb/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-arm/7.3.0-r0/recipe-sysroot --enable-nls --enable-initfini-array
  Thread model: posix
  gcc version 7.3.0 (GCC) 

u-boot编译
------------

| 说明：MYZR-IMX8M 不需要编译此 u-boot。

编译前的准备
~~~~~~~~~~~~~

- 创建编译工作目录

.. code:: shell

  =====> Input:
  mkdir ~/my-work/02_source/ -p

- 解压源码包到工作目录

.. code:: shell

  =====> Input:
  tar xf u-boot-2016.03-svn*.tar.bz2 -C ~/my-work/02_source/

编译u-boot目标文件
~~~~~~~~~~~~~~~~~~~

- 进入源码目录

.. code:: shell

  =====> Input:
  cd ~/my-work/02_source/u-boot-2016.03

- 生成目标开发板的 .config 文件

.. code:: shell

  =====> Input:
  make myimx6ek140p-6y-256m-emmc_defconfig

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

| 【注意】：上面 make 后面的 myimx6ek140p-6y-256m-emmc_defconfig 改为与开发板型号对应的配置文件。

.. code:: shell

  ********** MYZR-IMX6-EK140 **********
  myimx6ek140-6g-128m-emmc_defconfig  myimx6ek140-6y-128m-emmc_defconfig
  myimx6ek140-6g-128m-nand_defconfig  myimx6ek140-6y-128m-nand_defconfig
  myimx6ek140-6g-256m-emmc_defconfig  myimx6ek140-6y-256m-emmc_defconfig
  myimx6ek140-6g-256m-nand_defconfig  myimx6ek140-6y-256m-nand_defconfig
  myimx6ek140-6g-512m-emmc_defconfig  myimx6ek140-6y-512m-emmc_defconfig
  myimx6ek140-6g-512m-nand_defconfig  myimx6ek140-6y-512m-nand_defconfig

  ********** MYZR-IMX6-EK140P **********
  myimx6ek140p-6g-128m-emmc_defconfig  myimx6ek140p-6y-128m-emmc_defconfig
  myimx6ek140p-6g-128m-nand_defconfig  myimx6ek140p-6y-128m-nand_defconfig
  myimx6ek140p-6g-256m-emmc_defconfig  myimx6ek140p-6y-256m-emmc_defconfig
  myimx6ek140p-6g-256m-nand_defconfig  myimx6ek140p-6y-256m-nand_defconfig
  myimx6ek140p-6g-512m-emmc_defconfig  myimx6ek140p-6y-512m-emmc_defconfig
  myimx6ek140p-6g-512m-nand_defconfig  myimx6ek140p-6y-512m-nand_defconfig

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
    CFGS    board/myzr/myimx6/myimx6a7-6y-ddr3.cfg.cfgtmp
    MKIMAGE u-boot.imx

**Note: 如果有提示 “cc1: error”，通常是交叉编译工具的配置没生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤。**

- u-boot 目标文件

| u-boot.imx 即目标文件。

编译u-boot环境变量脚本
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

  ********** MYZR-IMX6-A7 **********
  emmc:
  =====> Input:
  mkimage -A arm -O linux -T script -C none -a 0 -e 0 -n "myzr bootscripts" -d board/myzr/bootscripts/myimx6a7_l4988_emmc_script.cmd my_environment_emmc.scr

  =====> Output: 
  Image Name:   myzr bootscripts
  Created:      Wed Jan  2 09:41:00 2019
  Image Type:   ARM Linux Script (uncompressed)
  Data Size:    1450 Bytes = 1.42 kB = 0.00 MB
  Load Address: 00000000
  Entry Point:  00000000
  Contents:
     Image 0: 1442 Bytes = 1.41 kB = 0.00 MB

  nand:
  =====> Input:
  mkimage -A arm -O linux -T script -C none -a 0 -e 0 -n "myzr bootscripts" -d board/myzr/bootscripts/myimx6a7_l4988_nand_script.cmd my_environment_nand.scr

  =====> Output:
  Image Name:   myzr bootscripts
  Created:      Wed May 22 06:35:57 2019
  Image Type:   ARM Linux Script (uncompressed)
  Data Size:    1484 Bytes = 1.45 kB = 0.00 MB
  Load Address: 00000000
  Entry Point:  00000000
  Contents:
     Image 0: 1476 Bytes = 1.44 kB = 0.00 MB

  ********** MYZR-IMX6-A9 **********
  =====> Input:
  mkimage -A arm -O linux -T script -C none -a 0 -e 0 -n "myzr bootscripts" -d board/myzr/bootscripts/myimx6a9_l4988_script.cmd my_environment.scr

  =====> Output:
  Image Name:   myzr bootscripts
  Created:      Wed May 22 06:37:40 2019
  Image Type:   ARM Linux Script (uncompressed)
  Data Size:    2294 Bytes = 2.24 kB = 0.00 MB
  Load Address: 00000000
  Entry Point:  00000000
  Contents:
     Image 0: 2286 Bytes = 2.23 kB = 0.00 MB

目标文件
~~~~~~~~~

| u-boot.imx 和 my_environment.scr(my_environment_nand.scr,my_environment_emmc.scr) 即编译得到的目标文件，保存这两个文件


内核编译
----------

编译前的准备
~~~~~~~~~~~~~

- 创建编译工作目录

.. code:: shell

  =====> Input:
  mkdir ~/my-work/02_source/ -p

- 解压源码包到工作目录

.. code:: shell

  =====> Input:
  tar xf linux-4.9.88-svn*.tar.bz2 -C ~/my-work/02_source/

编译内核目标文件
~~~~~~~~~~~~~~~~~

- 进入内核源码目录

.. code:: shell

  =====> Input:
  cd ~/my-work/02_source/linux-4.9.88

- 生成目标平台的 .config 文件

.. code:: shell

  =====> Input:
  make myimx6a7_defconfig

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

| 【注意】：上面 **make** 后面的 **myimx6a7_defconfig** 改为与开发板型号对应的配置文件。

.. code:: shell

  ********** MYZR-IMX6-EK140、MYZR-IMX6-EK140P **********
  myimx6a7_defconfig  

  ********** MYZR-IMX6-EK200、MYZR-IMX6-EK314、MYZR-IMX6-EK336 **********
  myimx6a9_defconfig  

  ********** MYZR-IMX8M-EK314 **********
  my_defconfig

- 编译内核目标文件

.. code:: shell

  =====> Input:
  make zImage

  =====> Output: 
  scripts/kconfig/conf  --silentoldconfig Kconfig
    CHK     include/config/kernel.release
    UPD     include/config/kernel.release
    WRAP    arch/arm/include/generated/asm/bitsperlong.h
    ......
    AS      arch/arm/boot/compressed/piggy.o
    LD      arch/arm/boot/compressed/vmlinux
    OBJCOPY arch/arm/boot/zImage
    Kernel: arch/arm/boot/zImage is ready

- 内核目标文件

| arch/arm/boot/zImage 即内核目标文件

编译设备树目标文件
~~~~~~~~~~~~~~~~~~~

- 执行编译命令

.. code:: shell

  =====> Input:
  make myimx6ek140p-6y-256m-emmc.dtb

  =====> Output: 
    DTC     arch/arm/boot/dts/myimx6ek140p-6y-256m-emmc.dtb

| 【注意】：上面 **make** 后面的 **myimx6ek140p-6y-256m-emmc.dtb** 改为与开发板型号对应的配置文件。

.. code:: shell

  ********** MYZR-IMX6-EK140 **********
  myimx6ek140-6g-128m-emmc.dtb  myimx6ek140-6y-128m-emmc.dtb
  myimx6ek140-6g-128m-nand.dtb  myimx6ek140-6y-128m-nand.dtb
  myimx6ek140-6g-256m-emmc.dtb  myimx6ek140-6y-256m-emmc.dtb
  myimx6ek140-6g-256m-nand.dtb  myimx6ek140-6y-256m-nand.dtb
  myimx6ek140-6g-512m-emmc.dtb  myimx6ek140-6y-512m-emmc.dtb
  myimx6ek140-6g-512m-nand.dtb  myimx6ek140-6y-512m-nand.dtb

  ********** MYZR-IMX6-EK140P **********
  myimx6ek140p-6g-128m-emmc.dtb  myimx6ek140p-6y-128m-emmc.dtb
  myimx6ek140p-6g-128m-nand.dtb  myimx6ek140p-6y-128m-nand.dtb
  myimx6ek140p-6g-256m-emmc.dtb  myimx6ek140p-6y-256m-emmc.dtb
  myimx6ek140p-6g-256m-nand.dtb  myimx6ek140p-6y-256m-nand.dtb
  myimx6ek140p-6g-512m-emmc.dtb  myimx6ek140p-6y-512m-emmc.dtb
  myimx6ek140p-6g-512m-nand.dtb  myimx6ek140p-6y-512m-nand.dtb

  ********** MYZR-IMX6-EK200 **********
  myimx6ek200-6q-1g.dtb     myimx6ek200-6q-2g.dtb     myimx6ek200-6q-512m.dtb  
  myimx6ek200-6u-1g.dtb     myimx6ek200-6u-2g.dtb     myimx6ek200-6u-512m.dtb  
  myimx6ek200-6s-512m.dtb   myimx6ek200-6s-1g.dtb     myimx6ek200-6s-128m.dtb  
  myimx6ek200-6qp-1g.dtb    myimx6ek200-6qp-2g.dtb    myimx6ek200-6qp-512m.dtb  

  ********** MYZR-IMX6-EK314 **********
  myimx6ek314-6q-1g.dtb     myimx6ek314-6q-2g.dtb     myimx6ek314-6q-512m.dtb  
  myimx6ek314-6u-1g.dtb     myimx6ek314-6u-2g.dtb     myimx6ek314-6u-512m.dtb  
  myimx6ek314-6s-512m.dtb   myimx6ek314-6s-1g.dtb     myimx6ek314-6s-128m.dtb  
  myimx6ek314-6qp-1g.dtb    myimx6ek314-6qp-2g.dtb    myimx6ek314-6qp-512m.dtb  

  ********** MYZR-IMX6-EK336 **********
  myimx6ek336-6q-1g.dtb     myimx6ek336-6q-2g.dtb     myimx6ek336-6q-512m.dtb

- 复制设备树目标文件

.. code:: shell

  =====> Input:
  cp arch/arm/boot/dts/myimx6ek140p-6y-256m-emmc.dtb ./

编译内核模块包
~~~~~~~~~~~~~~~

- 执行编译

.. code:: shell

  =====> Input:
  make modules

  =====> Output: 
    CHK     include/config/kernel.release
    CHK     include/generated/uapi/linux/version.h
    ......
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
    INSTALL crypto/echainiv.ko
    INSTALL crypto/tcrypt.ko
    ......
    INSTALL sound/usb/snd-usb-audio.ko
    INSTALL sound/usb/snd-usbmidi-lib.ko
    DEPMOD  4.9.88-myimx6-svn439

- 打包内核模块文件

.. code:: shell

  =====> Input:
  tar cjf kernel-modules.tar.bz2 -C modules lib

目标文件
~~~~~~~~~

**zImage、myimx6ek*.dtb 和 kernel-modules.tar.bz2 即编译得到的目标文件，保存这三个文件**


Linux C程序编译
----------------

准备源码
~~~~~~~~~

| 打开网盘到 5_MY-Demo -> MY-Linux-C-Demo，下载 hello.c 文件，并复制到虚拟机。

编译目标文件
~~~~~~~~~~~~~

.. code:: shell

  =====> Input:
  $CC hello.c -o hello.out

**Note: 如果有“未找到命令”的信息，是因为交叉编译工具链的配置没有生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤**

运行Linux C目标程序
~~~~~~~~~~~~~~~~~~~~

- 把编译得到的 hello.out 复制到开发板上
- 在开发板上运行Linux C目标程序

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

准备源码
~~~~~~~~~~

| 打开网盘到 5_MY-Demo，下载 MY-Linux-QT5-Demo-AboutUs-svn*.tar.bz2 文件，并复制到虚拟机。

- 解压源码包到工作目录

.. code:: shell

  =====> Input:
  tar xf MY-Linux-QT5-Demo-AboutUs-svn*.tar.bz2 -C ~/my-work/02_source/

QT程序编译
~~~~~~~~~~~

- 进入源码目录

.. code:: shell

  =====> Input:
  cd ~/my-work/02_source/AboutUs/

- 生成Makefile文件

.. code:: shell

  =====> Input:
  qmake

  =====> Output: 
  Info: creating stash file /home/myzr/my-work/02_source/AboutUs/.qmake.stash
  Note: 如果有“未找到 'qamke' 命令”的信息，是因为交叉编译工具链的配置没有生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤
  编译目标文件
  =====> Input:
  make

  =====> Output: 
  /home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/bin/qt5/uic widget.ui -o ui_widget.h
  ......
  arm-poky-linux-gnueabi-g++  -march=armv7ve -mfpu=neon -mfloat-abi=hard -mcpu=cortex-a7 --sysroot=/home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/sysroots/cortexa7hf-neon-poky-linux-gnueabi -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed --sysroot=/home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/sysroots/cortexa7hf-neon-poky-linux-gnueabi -Wl,-O1 -o AboutUs main.o widget.o qrc_source.o moc_widget.o   -lQt5Widgets -lQt5Gui -lQt5Core -lGLESv2 -lpthread 

在 MYZR-IMX6-A9 设备上运行
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 把编译得到的 AboutUs 复制到开发板上
- 在开发板上运行QT5目标程序

.. code:: shell

  =====> Input:
  chmod +x ./AboutUs
  ./AboutUs -platform eglfs

在 MYZR-IMX6-A7 设备上运行
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- 把编译得到的 AboutUs 复制到开发板上
- 在开发板上运行QT5目标程序

.. code:: shell

  =====> Input:
  export DISPLAY=:0.0
  chmod +x AboutUs
  ./AboutUs

运行结果
~~~~~~~~~

| 可以看到开发板显示屏上输出了 MYZR 的 Logo 和一些信息。