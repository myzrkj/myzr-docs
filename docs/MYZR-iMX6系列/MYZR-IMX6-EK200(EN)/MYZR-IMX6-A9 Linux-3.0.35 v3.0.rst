MYZR-IMX6-A9 Linux-3.0.35 v3.0
================================

Download relevant documents
-----------------------------

**Cross-compile tool chain**

|   A9 series：Open the network disk to 2.1_OS_Linux-3.0.35 -> 03_toolchain，Download MY-IMX-A9 Directory.

**Source code**

|   u-boot：Open the network disk to 2.1_OS_Linux-3.0.35 -> 02_source，Download u-boot-2016.03-\*.tar.bz2 (Source package version number svn315 and above). 
|   Kernel：Open the network disk to 2.1_OS_Linux-3.0.35 -> 02_source，Download linux-3.0.35-\*.tar.bz2 (Source package version number svn31 and above).


Install cross compilation tool chain
---------------------------------------

- Unload cross compilation tool chain

.. code-block:: shell

    =====> Input:
    tar xf gcc-4.6.2-glibc-2.13-linaro-multilib-2011.12.tar.bz2 -C /home/myzr/my-work/03_toolchain

- Copy the tool chain configuration file

.. code-block:: shell

    =====> Input:
    cp environment-setup-gcc-4.6-arm.sh /home/myzr/my-work/03_toolchaingcc-4.6.2-glibc-2.13-linaro-multilib-2011.12/

- Source Toolchain Profile

.. code-block:: shell

    =====> Input:
    source /home/myzr/my-work/03_toolchain/gcc-4.6.2-glibc-2.13-linaro-multilib-2011.12/environment-setup-gcc-4.6-arm.sh

- Verify cross compilation tool installation

.. code-block:: shell

    =====> Input:
    ${CROSS_COMPILE}gcc -v

    =====> Output: 
    Using built-in specs.
    COLLECT_GCC=arm-fsl-linux-gnueabi-gcc
    COLLECT_LTO_WRAPPER=/home/myzr/my-work/03_toolchain/gcc-4.6.2-glibc-2.13-linaro-multilib-2011.12/fsl-linaro-toolchain/bin/../libexec/gcc/arm-fsl-linux-gnueabi/4.6.2/lto-wrapper
    Target: arm-fsl-linux-gnueabi
    Configured with: /work/build/.build/src/gcc-linaro-4.6-2011.06-0/configure --build=i686-build_pc-linux-gnu --host=i686-build_pc-linux-gnu --target=arm-fsl-linux-gnueabi --prefix=/work/fsl-linaro-toolchain-2.13 --with-sysroot=/work/fsl-linaro-toolchain-2.13/arm-fsl-linux-gnueabi/multi-libs --enable-languages=c,c++ --with-pkgversion='Freescale MAD -- Linaro 2011.07 -- Built at 2011/08/10 09:20' --enable-__cxa_atexit --disable-libmudflap --disable-libgomp --disable-libssp --with-gmp=/work/build/.build/arm-fsl-linux-gnueabi/build/static --with-mpfr=/work/build/.build/arm-fsl-linux-gnueabi/build/static --with-mpc=/work/build/.build/arm-fsl-linux-gnueabi/build/static --with-ppl=/work/build/.build/arm-fsl-linux-gnueabi/build/static --with-cloog=/work/build/.build/arm-fsl-linux-gnueabi/build/static --with-libelf=/work/build/.build/arm-fsl-linux-gnueabi/build/static --with-host-libstdcxx='-static-libgcc -Wl,-Bstatic,-lstdc++,-Bdynamic -lm -L/work/build/.build/arm-fsl-linux-gnueabi/build/static/lib -lpwl' --enable-threads=posix --enable-target-optspace --enable-plugin --enable-multilib --with-local-prefix=/work/fsl-linaro-toolchain-2.13/arm-fsl-linux-gnueabi/multi-libs --disable-nls --enable-c99 --enable-long-long --with-system-zlib
    Thread model: posix
    gcc version 4.6.2 20110630 (prerelease) (Freescale MAD -- Linaro 2011.07 -- Built at 2011/08/10 09:20) 

u-boot compilation
----------------------

**Preparation before compilation**

- Create a compile working directory

.. code-block:: shell

    =====> Input:
    mkdir ~/my-work/02_source/ -p

- Unpack source code to working directory

.. code-block:: shell

    =====> Input:
    tar xf u-boot-2016.03-svn*.tar.bz2 -C ~/my-work/02_source/

**Compile the u-boot target file**

- Enter source directory

.. code-block:: shell

    =====> Input:
    cd ~/my-work/02_source/u-boot-2016.03

- Generate the target development board. config file

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

|   【Note】：myimx6ek200-6q-1g_defconfig above make after change to the configuration file corresponding to the development board model.

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

- compiling

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

|   Note: If there is a prompt “cc1: error”，usually the configuration of the cross-compilation tool does not work, you can perform this step after pressing the "source tool chain profile” operation in the previous "cross compile tool chain installation".

- u-boot Target File

|   u-boot.imx is the target file.

**Compile U-boot environment variable scripts**

.. code-block:: shell

    =====> Input:
    mkimage -A arm -O linux -T script -C none -a 0 -e 0 -n "myzr bootscripts" -d board/myzr/bootscripts/myimx6a9_l3035_script.cmd my_environment.scr

    =====> Output: 
    Image Name:   myzr bootscripts
    Created:      Wed Jan  2 09:39:38 2019
    Image Type:   ARM Linux Script (uncompressed)
    Data Size:    2090 Bytes = 2.04 kB = 0.00 MB
    Load Address: 00000000
    Entry Point:  00000000
    Contents:
       Image 0: 2082 Bytes = 2.03 kB = 0.00 MB

**Target File**

|   "u-boot.imx " and " my_environment.scr" That is, the compiled target file, saving the two files


Kernel compilation
---------------------

**Preparation before compilation**

- Create a compile working directory

.. code-block:: shell

    =====> Input:
    mkdir ~/my-work/02_source/ -p

- Unzip the source package to the working directory

.. code-block:: shell

    =====> Input:
    tar xf linux-3.0.35-svn*.tar.bz2 -C ~/my-work/02_source/

**Compile the kernel target file**

- Enter source directory

.. code-block:: shell

    =====> Input:
    cd ~/my-work/02_source/linux-3.0.35

- To generate the target platform". config "file

.. code-block:: shell

    =====> Input:
    make myimx6a9_defconfig

    =====> Output: 
      HOSTCC  scripts/basic/fixdep
      HOSTCC  scripts/kconfig/conf.o
      SHIPPED scripts/kconfig/zconf.tab.c
      SHIPPED scripts/kconfig/lex.zconf.c
      SHIPPED scripts/kconfig/zconf.hash.c
      HOSTCC  scripts/kconfig/zconf.tab.o
      HOSTLD  scripts/kconfig/conf
    #
    # configuration written to .config
    #

|   Note: If there is an error“Can't find default configuration "arch/x86/configs” ，because the configuration of the cross compilation tool chain did not work,You can do this step again after you have done it once in the "source toolchain configuration file" in "cross-compile toolchain installation earlier"

- Compiles kernel target files

.. code-block:: shell

    =====> Input:
    make zImage

    =====> Output: 
    scripts/kconfig/conf --silentoldconfig Kconfig
      CHK     include/linux/version.h
      UPD     include/linux/version.h
      CHK     include/generated/utsrelease.h
      UPD     include/generated/utsrelease.h
      Generating include/generated/mach-types.h
      CC      kernel/bounds.s
      ......
      AS      arch/arm/boot/compressed/piggy.gzip.o
      LD      arch/arm/boot/compressed/vmlinux
      OBJCOPY arch/arm/boot/zImage
      Kernel: arch/arm/boot/zImage is ready

- Kernel target file

|   arch/arm/boot/zImage is the kernel target file

**Compile the kernel module package**

- Compiling

.. code-block:: shell

    =====> Input:
    make modules

    =====> Output: 
      CHK     include/linux/version.h
      CHK     include/generated/utsrelease.h
    make[1]: “include/generated/mach-types.h”是最新的。
      CALL    scripts/checksyscalls.sh
      CC [M]  fs/autofs4/init.o
      ......
      LD [M]  drivers/usb/gadget/g_serial.ko
      LD [M]  fs/nls/nls_ascii.ko
      LD [M]  fs/autofs4/autofs4.ko
      LD [M]  fs/nls/nls_utf8.ko

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
      INSTALL drivers/gpu/drm/drm.ko
      INSTALL drivers/gpu/drm/vivante/vivante.ko
      ......
      INSTALL fs/autofs4/autofs4.ko
      INSTALL fs/nls/nls_ascii.ko
      INSTALL fs/nls/nls_utf8.ko
      DEPMOD  3.0.35-myimx6a9-svn42

- Package the kernel module files

.. code-block:: shell

    =====> Input:
    tar cjf kernel-modules.tar.bz2 -C modules lib

**Target File**

|   "zImage" and "kernel-modules.tar.bz2" are the target files compiled and the two files are saved


Linux C program compilation
------------------------------

**Prepare source code**

|   Open the disk to 5_MY-Demo -> MY-Linux-C-Demo，Download hello.c file and copy to virtual machine.

**Compile target file**

.. code-block:: shell

    =====> Input:
    ${CROSS_COMPILE}gcc hello.c -o hello.out

|   Note: If you have "no command found" information because the configuration of the cross-compilation tool chain is not effective, you can perform this step after pressing the "source tool chain profile" operation in the previous "cross compilation tool chain installation"

**Run Linux C Target Program**

- Copy the compiled" hello.out" to the development board
- Run the Linux C target program on the development board

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