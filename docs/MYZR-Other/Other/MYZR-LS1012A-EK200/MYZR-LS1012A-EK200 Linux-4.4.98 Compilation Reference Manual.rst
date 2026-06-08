MYZR-LS1012A-EK200 Linux-4.4.98 Compilation Reference Manual
===============================================================

Download Related Files
-------------------------

Cross-Compilation Toolchain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| For LS1012A series: Open the network disk and navigate to MY-LS1012A-EK200 -> 03_Cross-Compilation Tools, then download `fsl-qoriq-glibc-x86_64-aarch64-toolchain-2.0.sh`.

Source Code
~~~~~~~~~~~~~

| RCW: Open the network disk and navigate to MY-LS1012A-EK200 -> 02_Source Code, then download `rcw.tar.bz2`.
| U-Boot: Open the network disk and navigate to MY-LS1012A-EK200 -> 02_Source Code, then download `qoriq-uboot-2016.09-20170322.archived.tar.bz2`.
| Kernel: Open the network disk and navigate to MY-LS1012A-EK200 -> 02_Source Code, then download `qoriq-linux-4.4.98-20171212.archived.tar.bz2`.
| PPA: Open the network disk and navigate to MY-LS1012A-EK200 -> 02_Source Code, then download `ppa.tar.bz2`.


Install Cross-Compilation Toolchain
-------------------------------------

- Execute installation

.. code-block:: shell

   =====> Input:
   ./fsl-qoriq-glibc-x86_64-aarch64-toolchain-2.0.sh  (Do not install to the /opt directory)

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

- Modify configuration file

.. code-block:: shell

   =====> Input:
   echo "unset LDFLAGS" >> ~/my-work/03_toolchain/fsl-qoriq/2.0/environment-setup-aarch64-fsl-linux

- Source the toolchain configuration file

.. code-block:: shell

   =====> Input:
   source  /home/myzr/my-work/03_toolchain/fsl-qoriq/2.0/environment-setup-aarch64-fsl-linux

- Verify cross-compilation tool installation

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


RCW Compilation
-----------------

Preparation Before Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Create a compilation working directory

.. code-block:: shell

   =====> Input:
   mkdir ~/my-work/02_source/ -p

- Extract the source code package to the working directory

.. code-block:: shell

   =====> Input:
   tar jxf rcw.tar.bz2 -C ~/my-work/02_source/

Compile RCW Target File
~~~~~~~~~~~~~~~~~~~~~~~~~

- Enter the source code directory

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/rcw

- Execute compilation

.. code-block:: shell

   =====> Input:
   make 

   =====> Output: 
   make[1]: Entering directory `/home/linyn/MY-LS1012A/my-test/reslese/rcw/ls1012a-ek200'
   python2 ../rcw.py -i N_SSNP_3305/rcw_800.rcw -o N_SSNP_3305/rcw_800.bin
   /home/linyn/MY-LS1012A/my-test/reslese/rcw/ls1012a-ek200/../qspi_swap.sh /home/linyn/MY-LS1012A/my-test/reslese/rcw/ls1012a-ek200/../qspi_swap_list.txt
   N_SSNP_3305/rcw_800.bin N_SSNP_3305/rcw_800.bin.swapped 8

   make[1]: Leaving directory `/home/linyn/MY-LS1012A/my-test/reslese/rcw/ls1012a-ek200'

`Note: If the prompt "cc1: error" appears, it is usually because the cross-compilation tool configuration is not effective. You can perform the "source the toolchain configuration file" operation in the previous "Cross-Compilation Toolchain Installation" section and then execute this step again.`

- RCW target file

| `rcw_800.bin.swapped` is the target file.


U-Boot Compilation
---------------------

Preparation Before Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Create a compilation working directory

.. code-block:: shell

   =====> Input:
   mkdir ~/my-work/02_source/ -p

- Extract the source code package to the working directory

.. code-block:: shell

   =====> Input:
   tar jxf qoriq-uboot-2016.09-20170322.archived.tar.bz2 -C ~/my-work/02_source/

Compile U-Boot Target File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Enter the source code directory

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/qoriq-uboot-2016.09-20170322.archived/

- Clean configuration

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh clean  

   =====> Output: 
   ============Start build clean============
   ====Build clean ok!====

- Generate the .config file for the target development board

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

- Execute compilation

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh uboot

   =====> Output: 
     SHIPPED dts/dt.dtb
     CAT     u-boot-dtb.bin
     COPY    u-boot.dtb
     COPY    u-boot.bin
   ====Build uboot ok!====

Global Compilation
~~~~~~~~~~~~~~~~~~~~

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

`Note: If the prompt "cc1: error" appears, it is usually because the cross-compilation tool configuration is not effective. You can perform the "source the toolchain configuration file" operation in the previous "Cross-Compilation Toolchain Installation" section and then execute this step again.`

- U-Boot target file

| `u-boot.bin` is the target file.

---

PPA Compilation
------------------

Preparation Before Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Create a compilation working directory

.. code-block:: shell

   =====> Input:
   mkdir ~/my-work/02_source/ -p

- Extract the source code package to the working directory

.. code-block:: shell

   =====> Input:
   tar jxf ppa.tar.bz2 -C ~/my-work/02_source/

Compile PPA Target File
~~~~~~~~~~~~~~~~~~~~~~~~~

- Enter the source code directory

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/ppa/soc-ls1012

- Execute compilation

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

`Note: If the prompt "cc1: error" appears, it is usually because the cross-compilation tool configuration is not effective. You can perform the "source the toolchain configuration file" operation in the previous "Cross-Compilation Toolchain Installation" section and then execute this step again.`

- PPA target file

| `ppa.itb` is the target file.


Kernel Compilation
--------------------

Preparation Before Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Create a compilation working directory

.. code-block:: shell

   =====> Input:
   mkdir ~/my-work/02_source/ -p

- Extract the source code package to the working directory

.. code-block:: shell

   =====> Input:
   tar jxf qoriq-linux-4.4.98-20171212.archived.tar.bz2 -C ~/my-work/02_source/

Compile Kernel Target File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Enter the kernel source code directory

.. code-block:: shell

   =====> Input:
   cd ~/my-work/02_source/qoriq-linux-4.4.98-20171212.archived

- Clean configuration

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

- Compile kernel target file

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

- Kernel Object File

| The target file is **EK200_IMAGE/Image**


Compile Device Tree Object File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Execute the compilation command

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh dtb

   =====> Output: 
   ==========Start build dtb==========
     DTC     arch/arm64/boot/dts/freescale/myzr-ls1012a.dtb
   ====Build dtb ok!====

- Device Tree Object File

| The target file is **EK200_IMAGE/ls1012a.dtb**


Compile Kernel Module Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Execute the compilation

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

- Kernel Module Object Files

| The target files are **EK200_IMAGE/modules-4.4.98.tar.bz2** and **firmware-4.4.98.tar.bz2**


Global Compilation
--------------------

.. code-block:: shell

   =====> Input:
   ./ek200_build.sh all


Linux C Program Compilation
-----------------------------

Prepare Source Code
~~~~~~~~~~~~~~~~~~~~~

| Open the network disk, navigate to **5_MY-Demo -> MY-Linux-C-Demo**, download the **hello.c** file, and copy it to the virtual machine.


Compile Object File
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   =====> Input:
   $CC hello.c -o hello.out

`Note: If a "command not found" message appears, it is because the cross-compilation toolchain configuration has not taken effect. You can follow the "source toolchain configuration file" step in the previous "Cross-Compilation Toolchain Installation" section before re-executing this step`


Run the Linux C Target Program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Copy the compiled **hello.out** to the development board
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
