MYZR-RZFIVE-EK200 Linux-5.10 编译参考手册
===========================================

下载相关文件
-------------

**交叉编译工具链**

|   RZFIVE系列：打开网盘到 **MYZR-RZ -> 03_SDK**，下载 **oecore-x86_64-riscv64-toolchain-nodistro.0.sh**。

**源码**

|   u-boot源码：打开网盘到 **MYZR-RZ -> 02_源码**，下载 **myzr-rzfive_uboot-Release.xxx.tar.bz2**。
|   Kernel源码：打开网盘到 **MYZR-RZ -> 02_源码**，下载 **myzr-rzfive_linux-5.10-Release.xxx.tar.bz2**。

安装交叉编译工具链
------------------

**执行安装**

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~$ mkdir ~/riscv64-gcc
  linyn@linyn-VirtualBox:~$ chmod +x oecore-x86_64-riscv64-toolchain-nodistro.0.sh 
  linyn@linyn-VirtualBox:~$ ./oecore-x86_64-riscv64-toolchain-nodistro.0.sh

  =====> Output:（安装路径我这边设置为/home/linyn/riscv64-gcc，可以自定义路径）
  OpenEmbedded SDK installer version nodistro.0
  =============================================
  Enter target directory for SDK (default: /usr/local/oecore-x86_64): /home/linyn/riscv64-gcc/
  You are about to install the SDK to "/home/linyn/riscv64-gcc". Proceed [Y/n]? y
  Extracting SDK.......................................................................done
  Setting it up...done
  SDK has been successfully set up and is ready to be used.
  Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
   $ . /home/linyn/riscv64-gcc/environment-setup-riscv64-oe-linux

**设置交叉编译工具**

.. code-block:: shell

  =====> Input
  linyn@linyn-VirtualBox:~$ source /home/linyn/riscv64-gcc/environment-setup-riscv64-oe-linux

**验证交叉编译工具是否设置成功**

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~$ $CC -v
  
  =====> Output: 
  Using built-in specs.
  COLLECT_GCC=riscv64-oe-linux-gcc
  COLLECT_LTO_WRAPPER=/home/linyn/riscv64-gcc/sysroots/x86_64-oesdk-linux/usr/libexec/riscv64-oe-linux/gcc/riscv64-oe-linux/8.3.0/lto-wrapper
  Target: riscv64-oe-linux
  Configured with: ../../../../../../work-shared/gcc-8.3.0-r0/gcc-8-8.3.0/src/configure 
  --build=x86_64-linux --host=x86_64-oesdk-linux --target=riscv64-oe-linux 
  --prefix=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr 
  --exec_prefix=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr 
  --bindir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr/bin/riscv64-oe-linux 
  --sbindir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr/bin/riscv64-oe-linux 
  --libexecdir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr/libexec/riscv64-oe-linux 
  --datadir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr/share 
  --sysconfdir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/etc 
  --sharedstatedir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/com 
  --localstatedir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/var 
  --libdir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr/lib/riscv64-oe-linux 
  --includedir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr/include 
  --oldincludedir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr/include 
  --infodir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr/share/info 
  --mandir=/usr/local/oe-sdk-hardcoded-buildpath/sysroots/x86_64-oesdk-linux/usr/share/man 
  --disable-silent-rules --disable-dependency-tracking 
  --with-libtool-sysroot=/b4741516c0d3/lyn-work/RENESAS/RZFive/RTK0EF0126Z0000AZJ-v1.0update1/source/build/tmp-glibc/work/x86_64-nativesdk-oesdk-linux/gcc-cross-canadian-riscv64/8.3.0-r0/recipe-sysroot 
  --with-gnu-ld --enable-shared --enable-languages=c,c++ --enable-threads=posix --enable-multilib --enable-default-pie --enable-c99 --enable-long-long 
  --enable-symvers=gnu --enable-libstdcxx-pch --program-prefix=riscv64-oe-linux- --without-local-prefix --disable-install-libiberty --enable-lto 
  --disable-libssp --enable-libitm --disable-bootstrap --disable-libmudflap --with-system-zlib --with-linker-hash-style=gnu --enable-linker-build-id 
  --with-ppl=no --with-cloog=no --enable-checking=release --enable-cheaders=c_global --without-isl --with-gxx-include-dir=/not/exist/usr/include/c++/8.3.0 
  --with-build-time-tools=/b4741516c0d3/lyn-work/RENESAS/RZFive/RTK0EF0126Z0000AZJ-v1.0update1/source/build/tmp-glibc/work/x86_64-nativesdk-oesdk-linux/gcc-cross-canadian-riscv64/8.3.0-r0/recipe-sysroot-native/usr/riscv64-oe-linux/bin 
  --with-sysroot=/not/exist --with-build-sysroot=/b4741516c0d3/lyn-work/RENESAS/RZFive/RTK0EF0126Z0000AZJ-v1.0update1/source/build/tmp-glibc/work/x86_64-nativesdk-oesdk-linux/gcc-cross-canadian-riscv64/8.3.0-r0/recipe-sysroot 
  --enable-poison-system-directories --disable-static --enable-nls --with-glibc-version=2.28 --enable-initfini-array --enable-__cxa_atexit
  Thread model: posix
  gcc version 8.3.0 (GCC) 

U-BOOT编译
------------

**编译前的准备**

- 创建编译工作目录

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~$ mkdir ~/source/ -p

- 解压源码包到工作目录

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~$ tar jxvf myzr-rzfive_uboot-Release.*.tar.bz2 -C ~/source/

**编译U-BOOT目标文件**

- 进入源码目录

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~$ cd ~/source/myzr-rzfive_uboot-2020.10

- 清除配置

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_uboot-2020.10$ ./build.sh rzfive 2g clean

  =====> Output:
  ============Start build clean============
    CLEAN   dts/../arch/riscv/dts
    CLEAN   dts
    CLEAN   examples/standalone
    CLEAN   tools
    CLEAN   tools/lib tools/common
    CLEAN   spl/arch spl/board spl/cmd spl/common spl/disk spl/drivers spl/dts spl/env spl/fs spl/lib spl/u-boot.cfg spl/u-boot-spl spl/u-boot-spl.bin spl/u-boot-spl.dtb spl/u-boot-spl-dtb.bin spl/u-boot-spl.lds spl/u-boot-spl.map spl/u-boot-spl-nodtb.bin
    CLEAN   u-boot.lds u-boot.dtb u-boot.cfg.configs u-boot-dtb.img u-boot.map u-boot.itb u-boot.its u-boot.srec u-boot.cfg u-boot.bin u-boot-dtb.bin u-boot-nodtb.bin u-boot u-boot.img u-boot-spl_bp.bin u-boot.sym System.map
    CLEAN   scripts/basic
    CLEAN   scripts/dtc
    CLEAN   scripts/kconfig
    CLEAN   include/config include/generated spl
    CLEAN   .config .config.old include/autoconf.mk include/autoconf.mk.dep include/config.h
  ====Build clean ok!====

- 生成目标开发板的 .config 文件

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_uboot-2020.10$ ./build.sh rzfive 2g config

  =====> Output: 
  ============Start build config============
    HOSTCC  scripts/basic/fixdep
    HOSTCC  scripts/kconfig/conf.o
    YACC    scripts/kconfig/zconf.tab.c
    LEX     scripts/kconfig/zconf.lex.c
    HOSTCC  scripts/kconfig/zconf.tab.o
    HOSTLD  scripts/kconfig/conf
  #
  # configuration written to .config
  #
  ====Build config ok!====

| 【注意】：上面2g 是内存配置，改为与开发板型号对应的配置文件，还有内存1g的配置。

.. code-block:: shell

  ********** MYZR-RZFIVE-EK200 **********
  myzr-rzfive-1g_defconfig  myzr-rzfive-2g_defconfig

- 执行编译

.. code-block:: shell
  
  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_uboot-2020.10$ ./build.sh rzfive 2g uboot
  
  =====> Output: 
  ==========Start build uboot==========
  scripts/kconfig/conf  --silentoldconfig Kconfig
  ......
    CC      spl/drivers/mmc/sh_sdhi.o
    LD      spl/drivers/timer/built-in.o
    LD      spl/drivers/mmc/built-in.o
    LD      spl/drivers/built-in.o
    LD      spl/u-boot-spl
    OBJCOPY spl/u-boot-spl-nodtb.bin
    CAT     spl/u-boot-spl-dtb.bin
    COPY    spl/u-boot-spl.bin
  ====Build uboot ok!====
  ===target image:spl-myzr-rzfive-2g.srec and fit-myzr-rzfive-2g.srec=====
  
- 目标文件

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_uboot-2020.10$ ls EK200_IMAGE/
  
  =====> Output: 
  fit-myzr-rzfive-2g.srec  spl-myzr-rzfive-2g.srec
  

`Note: 如果有提示 “cc1: error”，通常是交叉编译工具的配置没生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤。`
`注意：还可以一次性完整编译`

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_uboot-2020.10$ ./build.sh all 
  
  =====> Output: 
  =========Start build all=========
  ============Start build clean============
  ====Build clean ok!====
  ============Start build config============
    HOSTCC  scripts/basic/fixdep
  
  ...
  
  ====Build uboot ok!====
  ===target image:spl-myzr-rzfive-2g.srec and fit-myzr-rzfive-2g.srec=====
  =========build all ok=========
  
内核编译
---------

**编译前的准备**

- 创建编译工作目录

.. code-block:: shell

  =====> Input:
  mkdir ~/source/ -p

- 解压源码包到工作目录

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~$ tar jxvf myzr-rzfive_linux-5.10-Release.*.tar.bz2 -C ~/source/ 
  linyn@linyn-VirtualBox:~$ sudo apt-get install libssl-dev

**编译内核目标文件**

- 进入内核源码目录

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~$ cd ~/source/myzr-rzfive_linux-5.10/

- 清除配置

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_linux-5.10$ ./build.sh rzfive 2g clean

  =====> Output: 
   ============Start build clean============
  ====Build clean ok!====

- 编译内核

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_linux-5.10$ ./build.sh rzfive 2g kernel

  =====> Output: 
  ============Start build kernel===========
    HOSTCC  scripts/basic/fixdep
    HOSTCC  scripts/kconfig/conf.o
    HOSTCC  scripts/kconfig/confdata.o
    HOSTCC  scripts/kconfig/expr.o
    LEX     scripts/kconfig/lexer.lex.c

    ......
    LD      vmlinux
    SYSMAP  System.map
    OBJCOPY arch/riscv/boot/Image
    Kernel: arch/riscv/boot/Image is ready
  ====Build kernel ok!====

- 内核目标文件 **EK200_IMAGE/Image** 即内核目标文件

**编译设备树目标文件**

- 执行编译命令

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_linux-5.10$ ./build.sh rzfive 2g dtb

  =====> Output: 
  ==========Start build dtb==========
    DTC     arch/riscv/boot/dts/renesas/myzr-rzfive-2g.dtb
  ====Build dtb ok!====

| 【注意】：上面 2g改为与开发板型号对应的配置文件。

- 目标文件

.. code-block:: shell

  ********** MYZR-RZFIEV-EK200 **********
  EK200_IMAGE/myzr-rzfive-1g.dtb  EK200_IMAGE/myzr-rzfive-2g.dtb

**编译内核模块包**

- 执行编译命令

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_linux-5.10$ ./build.sh rzfive 2g modules

  =====> Output: 
  ==========Start build modules==========
    CALL    scripts/atomic/check-atomics.sh
    CALL    scripts/checksyscalls.sh

    ......

    INSTALL fs/efivarfs/efivarfs.ko
    DEPMOD  5.10.145-cip17-riscv-renesas
  ====Build modules oks!====

- 目标文件

.. code-block:: shell

  EK200_IMAGE/kernel-modules.tar.bz2

| 注意：还可以一次性完整编译

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source/myzr-rzfive_linux-5.10$ ./build.sh rzfive 2g all 

  =====> Output: 
  =========Start build all=========
  ============Start build clean============
    CLEAN   arch/riscv/kernel/vdso
    CLEAN   arch/riscv/kernel
    CLEAN   certs

  ...

    INSTALL fs/configfs/configfs.ko
    INSTALL fs/efivarfs/efivarfs.ko
    DEPMOD  5.10.145-cip17-riscv-renesas
  ====Build modules oks!====
  =========build all ok=========

Linux C程序编译
----------------

**准备源码**

|   打开网盘到 **5_MY-Demo -> MY-Linux-C-Demo**，下载 **hello.c** 文件，并复制到虚拟机。

**编译目标文件**

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source$ $CC hello.c -o hello.out

`Note: 如果有“未找到命令”的信息，是因为交叉编译工具链的配置没有生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤`

**运行Linux C目标程序**

- 把编译得到的 hello.out 复制到开发板上
- 在开发板上运行Linux C目标程序

.. code-block:: shell

  =====> Input:
  linyn@linyn-VirtualBox:~/source$ chmod +x ./hello.out
  linyn@linyn-VirtualBox:~/source$ ./hello.out

  =====> Output:
  MYZR Technology Co.,Ltd.

  Web:  http://www.myzr.com.cn/
  Wiki: http://wiki.myzr.com.cn/
  BBS:  http://bbs.myzr.com.cn/

  Tel: 0756-3628023/3628021
  E-mail: service@myzr.com.cn