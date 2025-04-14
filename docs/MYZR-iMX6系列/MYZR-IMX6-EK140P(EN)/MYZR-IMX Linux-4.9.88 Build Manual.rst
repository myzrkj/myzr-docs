MYZR-IMX Linux-4.9.88 Build Manual
======================================

Necessary explanation
------------------------

| A7 series includes MYZR-IMX6-EK140、MYZR-IMX6-EK140P.
| A9 series includes MYZR-IMX6-EK200、MYZR-IMX6-EK314、MYZR-IMX6-EK336.


Download relevant files
----------------------------

**Cross-compile tool chain**

| IMX8M：Open the disk to 2.4_OS_Linux-4.9.88 -> 03_toolchain，Download ** MYZR-IMX8M ** Directory.
| A7 series：Open the network disk to2.4_OS_Linux-4.9.88 -> 03_toolchain，Download MYZR-IMX-A7 Directory.
| A9 series：Open the network disk to2.4_OS_Linux-4.9.88 -> 03_toolchain，Download MYZR-IMX-A9 Directory.

**Source code**

| u-boot：Open the network disk to 2.4_OS_Linux-4.9.88 -> 02_source，Download u-boot-2016.03-\*.tar.bz2.
| Kernel：Open the network disk to 2.4_OS_Linux-4.9.88 -> 02_source，Download linux-4.9.88-\*.tar.bz2.


Install cross compilation tool chain
----------------------------------------

**MYZR-IMX8M series cross compilation tool chain installation**

1. Execute installation

.. code-block:: shell

  =====> Input:
  ./fsl-imx-xwayland-glibc-x86_64-meta-toolchain-qt5-aarch64-toolchain-4.9.88-2.0.0.sh

  =====> Output: 
  NXP i.MX Release Distro SDK installer version 4.9.88-2.0.0
  ==========================================================
  Enter target directory for SDK (default: /opt/fsl-imx-xwayland/4.9.88-2.0.0): 
  =====> Input:
  /home/myzr/my-work/03_toolchain/fsl-imx-xwayland-glibc-x86_64-meta-toolchain-qt5-aarch64-toolchain-4.9.88-2.0.0

  =====> Output: 
  You are about to install the SDK to "/home/myzr/my-work/03_toolchain/fsl-imx-xwayland-glibc-x86_64-meta-toolchain-qt5-aarch64-toolchain-4.9.88-2.0.0". Proceed[Y/n]?
  =====> Input:
  y

  =====> Output: 
  Extracting SDK.......................................................................................................................................................................................................................done
  Setting it up...done
  SDK has been successfully set up and is ready to be used.
  Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
   $ . /home/myzr/my-work/03_toolchain/fsl-imx-xwayland-glibc-x86_64-meta-toolchain-qt5-aarch64-toolchain-4.9.88-2.0.0/environment-setup-aarch64-poky-linux

2. source Toolchain Profile

.. code-block:: shell

  =====> Input:
  source /home/myzr/my-work/03_toolchain/fsl-imx-xwayland-glibc-x86_64-meta-toolchain-qt5-aarch64-toolchain-4.9.88-2.0.0/environment-setup-aarch64-poky-linux

3. Verify cross compilation tool installation

.. code-block:: shell

  =====> Input:
  $CC -v

  =====> Output: 
  Using built-in specs.
  COLLECT_GCC=aarch64-poky-linux-gcc
  COLLECT_LTO_WRAPPER=/home/myzr/my-work/03_toolchain/fsl-imx-xwayland-glibc-x86_64-meta-toolchain-qt5-aarch64-toolchain-4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/libexec/aarch64-poky-linux/gcc/aarch64-poky-linux/7.3.0/lto-wrapper
  Target: aarch64-poky-linux
  Configured with: ../../../../../../work-shared/gcc-7.3.0-r0/gcc-7.3.0/configure --build=x86_64-linux --host=x86_64-pokysdk-linux --target=aarch64-poky-linux --prefix=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr --exec_prefix=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr --bindir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/bin/aarch64-poky-linux --sbindir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/bin/aarch64-poky-linux --libexecdir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/libexec/aarch64-poky-linux --datadir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/share --sysconfdir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/etc --sharedstatedir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/com --localstatedir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/var --libdir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/lib/aarch64-poky-linux --includedir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/include --oldincludedir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/include --infodir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/share/info --mandir=/opt/fsl-imx-xwayland/4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/share/man --disable-silent-rules --disable-dependency-tracking --with-libtool-sysroot=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx8mqevk__fsl-imx-xwayland/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-aarch64/7.3.0-r0/recipe-sysroot --with-gnu-ld --enable-shared --enable-languages=c,c++ --enable-threads=posix --enable-multilib --enable-c99 --enable-long-long --enable-symvers=gnu --enable-libstdcxx-pch --program-prefix=aarch64-poky-linux- --without-local-prefix --enable-lto --enable-libssp --enable-libitm --disable-bootstrap --disable-libmudflap --with-system-zlib --with-linker-hash-style=gnu --enable-linker-build-id --with-ppl=no --with-cloog=no --enable-checking=release --enable-cheaders=c_global --without-isl --with-gxx-include-dir=/not/exist/usr/include/c++/7.3.0 --with-build-time-tools=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx8mqevk__fsl-imx-xwayland/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-aarch64/7.3.0-r0/recipe-sysroot-native/usr/aarch64-poky-linux/bin --with-sysroot=/not/exist --with-build-sysroot=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx8mqevk__fsl-imx-xwayland/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-aarch64/7.3.0-r0/recipe-sysroot --without-long-double-128 --enable-poison-system-directories --with-mpfr=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx8mqevk__fsl-imx-xwayland/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-aarch64/7.3.0-r0/recipe-sysroot --with-mpc=/home/myzr/my-work/imx-4.9.88-2.0.0_ga/imx8mqevk__fsl-imx-xwayland/tmp/work/x86_64-nativesdk-pokysdk-linux/gcc-cross-canadian-aarch64/7.3.0-r0/recipe-sysroot --enable-nls --enable-initfini-array --enable-__cxa_atexit
  Thread model: posix
  gcc version 7.3.0 (GCC) 

**MYZR-IMX-A7 Series cross compilation tool chain installation**

1. Execute installation

.. code-block:: shell

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

2. source Toolchain Profile

.. code-block:: shell

  =====> Input:
  source /home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/environment-setup-cortexa7hf-neon-poky-linux-gnueabi

3. Verify cross compilation tool installation

.. code-block:: shell

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

**MYZR-IMX-A9 series cross compilation tool chain installation**

1. Execute installation

.. code-block:: shell

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

2. source Toolchain Profile

.. code-block:: shell

  =====> Input:
  source /home/myzr/my-work/03_toolchain/fsl-imx-fb-glibc-x86_64-meta-toolchain-qt5-cortexa9hf-neon-toolchain-4.9.88-2.0.0/environment-setup-cortexa9hf-neon-poky-linux-gnueabi 

3. Verify cross compilation tool installation

.. code-block:: shell

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

U-book compilation
--------------------

| Description：MYZR-IMX8M does not need to compile this u-book.
| Preparation before compilation

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

| 【Note】： myimx 6ek140p-6y-256m-emmc_defconfig after make is changed to a configuration file corresponding to the development board model.

.. code-block:: shell

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
    CFGS    board/myzr/myimx6/myimx6a7-6y-ddr3.cfg.cfgtmp
    MKIMAGE u-boot.imx

| Note: If there's a hint “cc1: error”，Usually the configuration of the cross-compilation tool does not work, and you can perform this step after pressing the "source toolchain configuration file" operation in the previous "cross compilation tool chain installation".

| u-boot Target File
| u-boot.imx is the target file.

**Compile U-boot environment variable scripts**

.. code-block:: shell

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

**Target File**

| "u-boot.imx "and "my_environment_emmc.scr" That is, the compiled target files, save the two files

Kernel compilation
---------------------

**Preparation before compilation**

- Create a compile working directory

.. code-block:: shell

  =====> Input:
  mkdir ~/my-work/02_source/ -p

- Unpack source code to working directory

.. code-block:: shell

  =====> Input:
  tar xf linux-4.9.88-svn*.tar.bz2 -C ~/my-work/02_source/

**Compiles kernel target files**

- Enter the kernel source directory

.. code-block:: shell

  =====> Input:
  cd ~/my-work/02_source/linux-4.9.88

- To generate the target platform .config file

.. code-block:: shell

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

| Note: If there is an error in “Can't find default configuration "arch/x86/configs” ，because the configuration of the cross compilation tool chain did not work，you can press "Source Toolchain Profile" in the previous "Cross Compiler Toolchain Installation" to perform this step after one operation **
| 【Note】：myimx6a7_defconfig** after make is changed to a configuration file corresponding to the development board model.

.. code-block:: shell

  ********** MYZR-IMX6-EK140、MYZR-IMX6-EK140P **********
  myimx6a7_defconfig  

  ********** MYZR-IMX6-EK200、MYZR-IMX6-EK314、MYZR-IMX6-EK336 **********
  myimx6a9_defconfig  

  ********** MYZR-IMX8M-EK314 **********
  my_defconfig  

- Compiles kernel target files

.. code-block:: shell

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

- Kernel target file

| arch/arm/boot/zImage is the kernel target file

**Build Device Tree Target File**

- Execute compile command

.. code-block:: shell

  =====> Input:
  make myimx6ek140p-6y-256m-emmc.dtb

  =====> Output: 
    DTC     arch/arm/boot/dts/myimx6ek140p-6y-256m-emmc.dtb

| 【Note】：The myimx 6ek140p-6y-256m-emmc. dtb after make is changed to the configuration file corresponding to the development board model.

.. code-block:: shell

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

- Copy the device tree target file

.. code-block:: shell

  =====> Input:
  cp arch/arm/boot/dts/myimx6ek140p-6y-256m-emmc.dtb ./

**Build kernel module package**

- Compiling

.. code-block:: shell

  =====> Input:
  make modules

  =====> Output: 
    CHK     include/config/kernel.release
    CHK     include/generated/uapi/linux/version.h
    ......
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
    INSTALL crypto/echainiv.ko
    INSTALL crypto/tcrypt.ko
    ......
    INSTALL sound/usb/snd-usb-audio.ko
    INSTALL sound/usb/snd-usbmidi-lib.ko
    DEPMOD  4.9.88-myimx6-svn439

- Package the kernel module files

.. code-block:: shell

  =====> Input:
  tar cjf kernel-modules.tar.bz2 -C modules lib

**Target File**

| "zImage、myimx6ek*.dtb" and "kernel-modules.tar.bz2 "is the target file compiled and the three files are saved.


Linux C Program compilation
------------------------------

**Prepare source code**

| Open the disk to 5_MY-Demo -> MY-Linux-C-Demo，download hello.c file and copy to virtual machine.

**Compile the target file**

.. code-block:: shell

  =====> Input:
  $CC hello.c -o hello.out

| 【Note】: If you have "no command found" information because the configuration of the cross-compilation tool chain is not effective, you can perform this step after pressing the "source tool chain profile" operation in the previous "cross compilation tool chain installation"

**Run Linux C Target Program**

- Copy the compiled hello.out to the development board
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

Linux QT5 program compilation
--------------------------------

**Prepare source code**

| Open the disk to 5_MY-Demo，Download MY-Linux-QT5-Demo-AboutUs-svn*.tar.bz2 file and copy to virtual machine.

- Unzip the source package to the working directory

.. code-block:: shell

  =====> Input:
  tar xf MY-Linux-QT5-Demo-AboutUs-svn*.tar.bz2 -C ~/my-work/02_source/

**QT Program compilation**

- Enter source directory

.. code-block:: shell

  =====> Input:
  cd ~/my-work/02_source/AboutUs/

- Generate Makefile file

.. code-block:: shell

  =====> Input:
  qmake

  =====> Output: 
  Info: creating stash file /home/myzr/my-work/02_source/AboutUs/.qmake.stash

| 【Note】: If there is information that the 'qamke' command is not found because the configuration of the cross-compilation tool chain is not effective, you can perform this step after pressing the "source tool chain configuration file" operation in the previous "cross compilation tool chain installation"

- Compile the target file

.. code-block:: shell

  =====> Input:
  make

  =====> Output: 
  /home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/sysroots/x86_64-pokysdk-linux/usr/bin/qt5/uic widget.ui -o ui_widget.h
  ......
  arm-poky-linux-gnueabi-g++  -march=armv7ve -mfpu=neon -mfloat-abi=hard -mcpu=cortex-a7 --sysroot=/home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/sysroots/cortexa7hf-neon-poky-linux-gnueabi -Wl,-O1 -Wl,--hash-style=gnu -Wl,--as-needed --sysroot=/home/myzr/my-work/03_toolchain/fsl-imx-x11-glibc-x86_64-meta-toolchain-qt5-cortexa7hf-neon-toolchain-4.9.88-2.0.0/sysroots/cortexa7hf-neon-poky-linux-gnueabi -Wl,-O1 -o AboutUs main.o widget.o qrc_source.o moc_widget.o   -lQt5Widgets -lQt5Gui -lQt5Core -lGLESv2 -lpthread 


**Run on MI-IMX6-A9 device**

  - Copy the compiled AboutUs to the development board
  - Run QT5 target program on development board
  
.. code-block:: shell
  
    =====> Input:
    chmod +x ./AboutUs
    ./AboutUs -platform eglfs
  
**Run on the my-imx6-a7 device**

- Copy the compiled AboutUs to the development board
- Run QT5 target program on development board

.. code-block:: shell

  =====> Input:
  export DISPLAY=:0.0
  chmod +x AboutUs
  ./AboutUs

**Running results**

| You can see that the MYZR logo and some information are output on the development board display.