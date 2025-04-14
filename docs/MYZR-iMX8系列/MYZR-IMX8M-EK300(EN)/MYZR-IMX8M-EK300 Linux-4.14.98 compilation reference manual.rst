
MYZR-IMX8M-EK300 Linux-4.14.98 compilation reference manual
===============================================================

Install the cross compilation toolchain
-------------------------------------------

- Create installation directory

.. code-block:: shell
   
   =====> Input:
   mkdir ~/my-work/03_toolchain -p
   cd ~/my-work/03_toolchain

- Download cross compilation tools

.. code-block:: shell
   
   =====> Input:
   wget https://releases.linaro.org/components/toolchain/binaries/7.3-2018.05/aarch64-linux-gnu/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.tar.xz

- Decompression cross compilation tool

.. code-block:: shell
   
   =====> Input:
   tar xf gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.tar.xz -C ~/my-work/03_toolchain  

- Create cross compilation tool configuration script

.. code-block:: shell

   =====> Input:
   cat << EOF > ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env
   #!/bin/sh

   export PATH=${HOME}/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu/bin:${PATH}
   export ARCH=arm64
   export CROSS_COMPILE=aarch64-linux-gnu-
   EOF

   =====> Input: 
   chmod +x ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

- Configure cross compilation environment variables

.. code-block:: shell

   =====> Input:
   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env  

- Check the installation


.. code-block:: shell

   =====> Input:
   ${CROSS_COMPILE}gcc -v

   =====> Input:
   Using built-in specs.
   COLLECT_GCC=aarch64-linux-gnu-gcc
   COLLECT_LTO_WRAPPER=/home/myzr/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu/bin/../libexec/gcc/aarch64-linux-gnu/7.3.1/lto-wrapper
   Target: aarch64-linux-gnu
   Configured with: '/home/tcwg-buildslave/workspace/tcwg-make-release/builder_arch/amd64/label/tcwg-x86_64-build/target/aarch64-linux-gnu/snapshots/gcc.git~linaro-7.3-2018.05/configure' SHELL=/bin/bash --with-mpc=/home/tcwg- 
   buildslave/workspace/tcwg-make-release/builder_arch/amd64/label/tcwg-x86_64-build/target/aarch64-linux-gnu/_build/builds/destdir/x86_64-unknown-linux-gnu --with-mpfr=/home/tcwg-buildslave/workspace/tcwg-make- 
   release/builder_arch/amd64/label/tcwg-x86_64-build/target/aarch64-linux-gnu/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gmp=/home/tcwg-buildslave/workspace/tcwg-make-release/builder_arch/amd64/label/tcwg-x86_64- 
   build/target/aarch64-linux-gnu/_build/builds/destdir/x86_64-unknown-linux-gnu --with-gnu-as --with-gnu-ld --disable-libmudflap --enable-lto --enable-shared --without-included-gettext --enable-nls --with-system-zlib --disable-sjlj- 
   exceptions --enable-gnu-unique-object --enable-linker-build-id --disable-libstdcxx-pch --enable-c99 --enable-clocale=gnu --enable-libstdcxx-debug --enable-long-long --with-cloog=no --with-ppl=no --with-isl=no --disable-multilib -- 
   enable-fix-cortex-a53-835769 --enable-fix-cortex-a53-843419 --with-arch=armv8-a --enable-threads=posix --enable-multiarch --enable-libstdcxx-time=yes --enable-gnu-indirect-function --with-build-sysroot=/home/tcwg- 
   buildslave/workspace/tcwg-make-release/builder_arch/amd64/label/tcwg-x86_64-build/target/aarch64-linux-gnu/_build/sysroots/aarch64-linux-gnu --with-sysroot=/home/tcwg-buildslave/workspace/tcwg-make- 
   release/builder_arch/amd64/label/tcwg-x86_64-build/target/aarch64-linux-gnu/_build/builds/destdir/x86_64-unknown-linux-gnu/aarch64-linux-gnu/libc --enable-checking=release --disable-bootstrap --enable-languages=c,c++,fortran,lto -- 
   build=x86_64-unknown-linux-gnu --host=x86_64-unknown-linux-gnu --target=aarch64-linux-gnu --prefix=/home/tcwg-buildslave/workspace/tcwg-make-release/builder_arch/amd64/label/tcwg-x86_64-build/target/aarch64-linux- 
   gnu/_build/builds/destdir/x86_64-unknown-linux-gnu
   Thread model: posix
   gcc version 7.3.1 20180425 [linaro-7.3-2018.05 revision d29120a424ecfbc167ef90065c0eeb7f91977701] (Linaro GCC 7.3-2018.05)


Compile the kernel file
---------------------------

Preparation before compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Create compilation working directory

.. code-block:: shell

   =====> Input:
   mkdir ~/my-work/02_source/ -p

|  Download the kernel source Open the network disk to "2.1_OS_Linux-4.14.98-> 02_Source" and download "linux-4.14.98.\*.tar.bz2".
|  Copy the source package to "~ / my-work / 02_source /" of the virtual machine and decompress it (the decompression command is as follows):

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source
   tar xf linux-4.14.98.*.tar.bz2

- Enter the kernel source directory

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/linux-4.14.98

- Configure cross compilation environment variables

.. code-block:: shell

   =====> Input:
   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env  

Compile the kernel object file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Generate target .config file

.. code-block:: shell

   =====> Input:
   make myimx8mq_defconfig  

   =====> Output:
     HOSTCC  scripts/basic/fixdep
     HOSTCC  scripts/kconfig/conf.o
     SHIPPED scripts/kconfig/zconf.tab.c
     SHIPPED scripts/kconfig/zconf.lex.c
     HOSTCC  scripts/kconfig/zconf.tab.o
     HOSTLD  scripts/kconfig/conf
   #
   # configuration written to .config
   #

- Compile the kernel object file

.. code-block:: shell

   =====> Input:
   make Image 

   =====> Output: 
   scripts/kconfig/conf  --silentoldconfig Kconfig
      CHK     include/config/kernel.release
      UPD     include/config/kernel.release
      WRAP    arch/arm/include/generated/asm/bitsperlong.h
      ......
      AR      built-in.o
      LD      vmlinux.o
      MODPOST vmlinux.o
      KSYM    .tmp_kallsyms1.o
      KSYM    .tmp_kallsyms2.o
      LD      vmlinux
      SORTEX  vmlinux
      SYSMAP  System.map
      OBJCOPY arch/arm64/boot/Image

- Copy kernel object file

.. code-block:: shell

   =====> Input:
   cp arch/arm64/boot/Image ./

Compile the device tree object file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Set TARGETEVKMODE

.. code-block:: shell

   =====> Input:
   TARGET_EVK_MODE=myimx8mek300-8mq

**【Explanation】: TARGET_EVK_MODE is set according to the development board model and can be set to myimx8mevk-8mq, myimx8mek300-8mq**

- Execute compile command

.. code-block:: shell

   =====> Input:
   make myzr/${TARGET_EVK_MODE}.dtb    

   =====> Output: 
     CHK     scripts/mod/devicetable-offsets.h
     DTC     arch/arm64/boot/dts/myzr/${TARGET_EVK_MODE}.dtb

- Copy Device Tree Object

.. code-block:: shell

   =====> Input:
   cp arch/arm64/boot/dts/myzr/${TARGET_EVK_MODE}.dtb ./

Compile the kernel module package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Perform compilation

.. code-block:: shell

   =====> Input:
   make modules  

   =====> Output: 
     CHK     include/config/kernel.release
     CHK     include/generated/uapi/linux/version.h
     ......
     LD [M]  sound/usb/snd-usb-audio.ko
     LD [M]  sound/usb/snd-usbmidi-lib.ko

- Create a directory for saving kernel modules

.. code-block:: shell

   =====> Input:
   mkdir modules

- Install the kernel module to the specified directory

.. code-block:: shell

   =====> Input:
   make modules_install headers_install INSTALL_MOD_PATH=./modules  

   =====> Output: 
     INSTALL arch/arm64/crypto/aes-neon-blk.ko
     INSTALL arch/arm64/crypto/aes-neon-bs.ko
     ......
     INSTALL sound/usb/snd-usbmidi-lib.ko
     DEPMOD  4.14.98-g2ff648b
     CHK     include/generated/uapi/linux/version.h

- Packaging kernel module files

.. code-block:: shell

   =====> Input:
   tar cjvf kernel-modules.tar.bz2 -C modules lib

target document
~~~~~~~~~~~~~~~~~

**Image, * .dtb and kernel-modules.tar.bz2 are compiled object files. Save these three files**

Compile u-boot file
----------------------

Preparation before compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Download u-boot source code Open the network disk to "2.1_OS_Linux-4.14.98-> 02_Source" and download "u-boot-2018.03.\*.tar.bz2".

|  Copy the source package to "~ / my-work / 02_source /" of the virtual machine and decompress it (the decompression command is as follows):

.. code-block:: shell

   =====> Input:
   tar xf u-boot-2018.03.*.tar.bz2

- Enter the kernel source directory

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/u-boot-2018.03

- Configure cross compilation environment variables

.. code-block:: shell

   =====> Input:
   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

Compile u-boot object file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Set TARGETEVKMODE

.. code-block:: shell

   =====> Input:
   TARGET_EVK_MODE=myimx8mek300-8mq

**【Description】：TARGET_EVK_MODE is set according to the development board model and can be set to myimx8mevk-8mq,myimx8mek300-8mq**

- Generate target .config file

.. code-block:: shell

   =====> Input:
   make ${TARGET_EVK_MODE}_defconfig 

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

- Compile u-boot object file

.. code-block:: shell

   =====> Input:
   make 

   =====> Output: 
   scripts/kconfig/conf  --silentoldconfig Kconfig
     CHK     include/config.h
     UPD     include/config.h
     CFG     u-boot.cfg
     GEN     include/autoconf.mk
     ......
     LD      spl/u-boot-spl
     OBJCOPY spl/u-boot-spl-nodtb.bin
     COPY    spl/u-boot-spl.bin
     CFGS    arch/arm/mach-imx/spl_sd.cfg.cfgtmp
     MKIMAGE SPL
     CFGCHK  u-boot.cfg

- Copy u-boot target file

.. code-block:: shell

   =====> Input:
   cp arch/arm/dts/${TARGET_EVK_MODE}.dtb ./

target document
~~~~~~~~~~~~~~~~~~

**$ {TARGETEVKMODE} .dtb, u-boot-nodtb.bin and u-boot-spl.bin are the compiled object files. Save these three files, which will be used in the next bootloader compilation**

Compile BootLoader
--------------------

Preparation before compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Download BootLoader compilation tool Open the network disk to "2.1_OS_Linux-4.14.98-> 02Source" and download "mkimage-imx4.14.98.\*.tar.bz2".

|  Copy the source package to "~ / my-work / 02_source /" of the virtual machine and decompress it (the decompression command is as follows):

.. code-block:: shell

   =====> Input:
   tar xf mkimage-imx_4.14.98.*.tar.bz2

- Go to tools directory

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/mkimage-imx_4.14.98

- Set TARGETEVKMODE

.. code-block:: shell

   =====> Input:
   TARGET_EVK_MODE=myimx8mek300-8mq

**【Description】：TARGET_EVK_MODE is set according to the development board model and can be set to myimx8mevk-8mq, myimx8mek300-8mq**

- Copy the dependent files Copy the three files compiled by u-boot

.. code-block:: shell

   =====> Input:
   cp ../u-boot-2018.03/u-boot-nodtb.bin ./iMX8M/${TARGET_EVK_MODE}-nodtb.bin
   cp ../u-boot-2018.03/spl/u-boot-spl.bin ./iMX8M/${TARGET_EVK_MODE}-spl.bin
   cp ../u-boot-2018.03/${TARGET_EVK_MODE}.dtb ./iMX8M/${TARGET_EVK_MODE}.dtb

Compile BootLoader object file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Enter compilation instructions

.. code-block:: shell

   =====> Input:
   make SOC=iMX8M ${TARGET_EVK_MODE%-*} OUTIMG=${TARGET_EVK_MODE}.bin  

   =====> Output: 
   Compiling mkimage_imx8
   PLAT=imx8mq HDMI=yes
   Compiling mkimage_imx8
   ......
   Second Loader IMAGE:
    sld_header_off     0x57c00
    sld_csf_off        0x58c20
    sld hab block:     0x401fcdc0 0x57c00 0x1020

- Copy BootLoader target file

.. code-block:: shell

   =====> Input:
   cp ./iMX8M/${TARGET_EVK_MODE}.bin ./

target document
~~~~~~~~~~~~~~~~~~

**${TARGET_EVK_MODE} .bin is the compiled object file, save this file**

.. code-block:: shell

   Web:  http://www.myzr.com.cn/
   Wiki: http://wiki.myzr.com.cn/
   BBS:  http://bbs.myzr.com.cn/

   Tel: 0756-3628023/3628021
   E-mail: service@myzr.com.cn