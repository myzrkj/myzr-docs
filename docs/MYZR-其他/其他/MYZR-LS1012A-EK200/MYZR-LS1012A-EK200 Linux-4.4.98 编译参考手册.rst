
MYZR-LS1012A-EK200 Linux-4.4.98 编译参考手册
==============================================

下载相关文件
--------------

交叉编译工具链
~~~~~~~~~~~~~~~

|  LS1012A系列：打开网盘到 MY-LS1012A-EK200 -> 03_交叉编译工具，下载 fsl-qoriq-glibc-x86_64-aarch64-toolchain-2.0.sh。

源码
~~~~~~

|  rcw： 打开网盘到 MY-LS1012A-EK200 -> 02_源码，下载 rcw.tar.bz2。
|  u-boot：打开网盘到 MY-LS1012A-EK200 -> 02_源码，下载 qoriq-uboot-2016.09-20170322.archived.tar.bz2。
|  Kernel：打开网盘到 MY-LS1012A-EK200 -> 02_源码，下载 qoriq-linux-4.4.98-20171212.archived.tar.bz2。
|  ppa: 打开网盘到 MY-LS1012A-EK200 -> 02_源码，下载 ppa.tar.bz2。

安装交叉编译工具链
-------------------

- 执行安装

.. code-block:: shell

   =====> Input:
   ./fsl-qoriq-glibc-x86_64-aarch64-toolchain-2.0.sh  （不要安装到/opt目录）

   =====> Output: 
   Freescale i.MX Release Distro SDK installer version 4.1.15-2.1.0
   ================================================================
   Enter target directory for SDK (default: /opt/fsl-imx-x11/4.1.15-2.1.0): 
   =====> Input:
   /home/myzr/my-work/03_toolchain/fsl-qoriq/2.0/
   =====> Output: 
   You are about to install the SDK to "/home/myzr/my-work/03_toolchain/fsl-qoriq/2.0". Proceed[Y/n]? 
   =====> Input:
   y
   =====> Output: 
   Extracting SDK...............................................................................................................................................................done
   Setting it up...done
   SDK has been successfully set up and is ready to be used.
   Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
    $ . /home/myzr/my-work/03_toolchain/fsl-qoriq/2.0/environment-setup-aarch64-fsl-linux

- 修改配置文件

.. code-block:: shell

   =====> Input:
   echo "unset LDFLAGS" >> ~/my-work/03_toolchain/fsl-qoriq/2.0/environment-setup-aarch64-fsl-linux

- source 工具链配置文件

.. code-block:: shell

   =====> Input:
   source  /home/myzr/my-work/03_toolchain/fsl-qoriq/2.0/environment-setup-aarch64-fsl-linux

- 检验交叉编译工具安装

.. code-block:: shell

   =====> Input:
   $CC -v

   =====> Output: 
   Using built-in specs.
   COLLECT_GCC=aarch64-fsl-linux-gcc
   COLLECT_LTO_WRAPPER=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/libexec/aarch64-fsl-linux/gcc/aarch64-fsl-linux/4.9.3/lto-wrapper
   Target: aarch64-fsl-linux
   Configured with: /home/linyn/ls1012/QorIQ-SDK-V2.0-20160527-yocto/build_ls1012ardb/tmp/work-shared/gcc-linaro-4.9-r2015.03/gcc-linaro-4.9-2015.03/configure --build=x86_64-linux --host=x86_64-fslsdk-linux --target=aarch64-fsl-linux --prefix=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr --exec_prefix=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr --bindir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/bin/aarch64-fsl-linux --sbindir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/bin/aarch64-fsl-linux --libexecdir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/libexec/aarch64-fsl-linux --datadir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/share --sysconfdir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/etc --sharedstatedir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/com --localstatedir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/var --libdir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/lib/aarch64-fsl-linux --includedir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/include --oldincludedir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/include --infodir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/share/info --mandir=/opt/fsl-qoriq/2.0/sysroots/x86_64-fslsdk-linux/usr/share/man --disable-silent-rules --disable-dependency-tracking --with-libtool-sysroot=/home/linyn/ls1012/QorIQ-SDK-V2.0-20160527-yocto/build_ls1012ardb/tmp/sysroots/x86_64-nativesdk-fslsdk-linux --with-gnu-ld --enable-shared --enable-languages=c,c++ --enable-threads=posix --enable-multilib --enable-c99 --enable-long-long --enable-symvers=gnu --enable-libstdcxx-pch --program-prefix=aarch64-fsl-linux- --without-local-prefix --enable-target-optspace --enable-lto --enable-libssp --disable-bootstrap --disable-libmudflap --with-system-zlib --with-linker-hash-style=gnu --enable-linker-build-id --with-ppl=no --with-cloog=no --enable-checking=release --enable-cheaders=c_global --with-gxx-include-dir=/not/exist/usr/include/c++/4.9.3 --with-build-time-tools=/home/linyn/ls1012/QorIQ-SDK-V2.0-20160527-yocto/build_ls1012ardb/tmp/sysroots/x86_64-linux/usr/aarch64-fsl-linux/bin --with-sysroot=/not/exist --with-build-sysroot=/home/linyn/ls1012/QorIQ-SDK-V2.0-20160527-yocto/build_ls1012ardb/tmp/sysroots/ls1012ardb --enable-poison-system-directories --with-mpfr=/home/linyn/ls1012/QorIQ-SDK-V2.0-20160527-yocto/build_ls1012ardb/tmp/sysroots/x86_64-nativesdk-fslsdk-linux --with-mpc=/home/linyn/ls1012/QorIQ-SDK-V2.0-20160527-yocto/build_ls1012ardb/tmp/sysroots/x86_64-nativesdk-fslsdk-linux --enable-nls --enable-__cxa_atexit
   Thread model: posix
   gcc version 4.9.3 20150311 (prerelease) (Linaro GCC 4.9-2015.03) 

RCW编译
---------

编译前的准备
~~~~~~~~~~~~~

- 创建编译工作目录

.. code-block:: shell

   =====> Input:
   mkdir ~/my-work/02_source/ -p

- 解压源码包到工作目录

.. code-block:: shell

   =====> Input:
   tar jxf rcw.tar.bz2 -C ~/my-work/02_source/

编译rcw目标文件
~~~~~~~~~~~~~~~~

- 进入源码目录

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/rcw

- 执行编译

.. code-block:: shell

   =====> Input:
   make 

   =====> Output: 
   make[1]: Entering directory `/home/linyn/MY-LS1012A/my-test/reslese/rcw/ls1012a-ek200'
   python2 ../rcw.py -i N_SSNP_3305/rcw_800.rcw -o N_SSNP_3305/rcw_800.bin
   /home/linyn/MY-LS1012A/my-test/reslese/rcw/ls1012a-ek200/../qspi_swap.sh /home/linyn/MY-LS1012A/my-test/reslese/rcw/ls1012a-ek200/../qspi_swap_list.txt
   N_SSNP_3305/rcw_800.bin N_SSNP_3305/rcw_800.bin.swapped 8

   make[1]: Leaving directory `/home/linyn/MY-LS1012A/my-test/reslese/rcw/ls1012a-ek200'

`Note: 如果有提示 “cc1: error”，通常是交叉编译工具的配置没生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤。`

- rcw 目标文件

|  rcw_800.bin.swapped 即目标文件。

u-boot编译
------------

编译前的准备
~~~~~~~~~~~~~

- 创建编译工作目录

.. code-block:: shell

   =====> Input:
   mkdir ~/my-work/02_source/ -p

- 解压源码包到工作目录

.. code-block:: shell

   =====> Input:
   tar jxf qoriq-uboot-2016.09-20170322.archived.tar.bz2 -C ~/my-work/02_source/

编译u-boot目标文件
~~~~~~~~~~~~~~~~~~~

- 进入源码目录

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/qoriq-uboot-2016.09-20170322.archived/

- 清除配置

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh clean  

   =====> Output: 
   ============Start build clean============
   ====Build clean ok!====

- 生成目标开发板的 .config 文件

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh config

   =====> Output: 
   ============Start build config============
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
   ====Build config ok!====

- 执行编译

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh uboot

   =====> Output: 
     SHIPPED dts/dt.dtb
     CAT     u-boot-dtb.bin
     COPY    u-boot.dtb
     COPY    u-boot.bin
   ====Build uboot ok!====

全局编译
~~~~~~~~~

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh all

   =====> Output: 
   SHIPPED dts/dt.dtb
     CAT     u-boot-dtb.bin
     COPY    u-boot.dtb
     COPY    u-boot.bin
   ====Build uboot ok!====
   =========build all ok========= 

`Note: 如果有提示 “cc1: error”，通常是交叉编译工具的配置没生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤。`

- u-boot 目标文件

|  u-boot.bin 即目标文件。

PPA编译
----------

编译前的准备
~~~~~~~~~~~~~

- 创建编译工作目录

.. code-block:: shell

   =====> Input:
   mkdir ~/my-work/02_source/ -p

- 解压源码包到工作目录

.. code-block:: shell

   =====> Input:
   tar jxf ppa.tar.bz2 -C ~/my-work/02_source/

编译PPA目标文件
~~~~~~~~~~~~~~~~

- 进入源码目录

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/ppa/soc-ls1012

- 执行编译

.. code-block:: shell

   =====> Input:
   make rdb-fit 

   =====> Output: 
   mkimage -f build/src/ppa.its build/obj/ppa.itb
   FIT description: PPA Firmware
   Created:         Fri Nov  1 10:58:17 2019
    Image 0 (firmware@1)
     Description:  PPA Firmware: Version 0.2
     Created:      Fri Nov  1 10:58:17 2019
     Type:         Firmware
     Compression:  uncompressed
     Data Size:    88064 Bytes = 86.00 kB = 0.08 MB
     Architecture: AArch64
     Load Address: unavailable
    Default Configuration: 'config@1'
    Configuration 0 (config@1)
     Description:  Boot PPA firmware
     Kernel:       unavailable

`Note: 如果有提示 “cc1: error”，通常是交叉编译工具的配置没生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤。`

- ppa 目标文件

|  ppa.itb 即目标文件。

内核编译
----------

编译前的准备
~~~~~~~~~~~~~

- 创建编译工作目录

.. code-block:: shell

   =====> Input:
   mkdir ~/my-work/02_source/ -p

- 解压源码包到工作目录

.. code-block:: shell

   =====> Input:
   tar jxf qoriq-linux-4.4.98-20171212.archived.tar.bz2 -C ~/my-work/02_source/

编译内核目标文件
~~~~~~~~~~~~~~~~~

- 进入内核源码目录

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/qoriq-linux-4.4.98-20171212.archived

- 清除配置

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh clean  

   =====> Output: 
   ============Start build clean============
   ====Build clean ok!====
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

- 编译内核目标文件

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh kernel

   =====> Output: 
     GEN     .version
     CHK     include/generated/compile.h
     UPD     include/generated/compile.h
     CC      init/version.o
     LD      init/built-in.o
     KSYM    .tmp_kallsyms1.o
     KSYM    .tmp_kallsyms2.o
     LD      vmlinux
     SORTEX  vmlinux
     SYSMAP  System.map
     OBJCOPY arch/arm64/boot/Image
   ====Build kerenl ok!====

- 内核目标文件

|  EK200_IMAGE/Image 即目标文件

编译设备树目标文件
~~~~~~~~~~~~~~~~~~

- 执行编译命令

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh dtb

   =====> Output: 
   ==========Start build dtb==========
     DTC     arch/arm64/boot/dts/freescale/myzr-ls1012a.dtb
   ====Build dtb ok!====

- 设备树目标文件

|  EK200_IMAGE/ls1012a.dtb 即目标文件

编译内核模块包
~~~~~~~~~~~~~~~

- 执行编译

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh modules

   =====> Output: 
     INSTALL net/netfilter/xt_TPROXY.ko
     INSTALL net/netfilter/xt_hashlimit.ko
     INSTALL net/netfilter/xt_socket.ko
     INSTALL sound/core/snd-hwdep.ko
     INSTALL sound/core/snd-rawmidi.ko
     INSTALL sound/usb/snd-usb-audio.ko
     INSTALL sound/usb/snd-usbmidi-lib.ko
     DEPMOD  4.4.98
   ====Build modules ok!====

- 内核模块目标文件

|  EK200_IMAGE/modules-4.4.98.tar.bz2和firmware-4.4.98.tar.bz2 即目标文件

全局编译
---------

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh all

Linux C程序编译
-----------------

准备源码
~~~~~~~~~

|  打开网盘到 5_MY-Demo -> MY-Linux-C-Demo，下载 hello.c 文件，并复制到虚拟机。

编译目标文件
~~~~~~~~~~~~~

.. code-block:: shell

   =====> Input:
   $CC hello.c -o hello.out

`Note: 如果有“未找到命令”的信息，是因为交叉编译工具链的配置没有生效，可以按前面 “交叉编译工具链安装” 中的 “source 工具链配置文件” 操作一次后再执行此步骤`

运行Linux C目标程序
~~~~~~~~~~~~~~~~~~~~

- 把编译得到的 hello.out 复制到开发板上
- 在开发板上运行Linux C目标程序

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