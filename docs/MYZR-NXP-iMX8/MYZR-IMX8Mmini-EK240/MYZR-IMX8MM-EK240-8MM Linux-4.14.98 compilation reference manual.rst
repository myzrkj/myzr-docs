MYZR-IMX8MM-EK240-8MM Linux-4.14.98 compilation reference manual
===================================================================

Install the cross-compilation tool
-------------------------------------

- Create the installation directory

|  ====> input :

.. code-block:: shell

   mkdir ~/my-work/03_toolchain -p

|  ====> input :

.. code-block:: shell
   
   cd ~/my-work/03_toolchain

- Download the cross-compile tool

|  ====> input :

.. code-block:: shell
   
   wget https://releases.linaro.org/components/toolchain/binaries/7.3-2018.05/aarch64-linux-gnu/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.tar.xz

- Unzip the cross-compilation tool

|  ====> input :

.. code-block:: shell

   tar xf gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.tar.xz -C ~/my-work/03_toolchain

- Create a cross-compile tool configuration script

|  ====> input :

.. code-block:: shell

   cat << EOF > ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env
   #!/bin/sh
   export PATH=${HOME}/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu/bin:${PATH}
   export ARCH=arm64
   export CROSS_COMPILE=aarch64-linux-gnu-
   EOF

|  ====> input :

.. code-block:: shell
   
   chmod +x ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

- Configure cross-compiled environment variables

|  ====> input :

.. code-block:: shell

   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

- Check installation

|  ====> input :

.. code-block:: shell
   
   ${CROSS_COMPILE}gcc -v

|  ====> output information:
|  Using built-in specs.

.. code-block:: shell

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

**library installation**

|  ====> input :

.. code-block:: shell

   sudo apt install zlib1g 
   sudo apt install zlib1g-dev 
   apt-get install device-tree-compiler

Compile the kernel file
--------------------------

**Preparation before compilation**

- Create a working directory

|  ====> input :

.. code-block:: shell

   mkdir ~/my-work/02_source/ -p

- Download kernel source code

|  Open the network disk to "2.1_OS\ _linux-4.14.98-> 02_Source" and download "linux-4.14.98.*. Tar. Bz2" and "build.sh".
|  Copy to the "~/ My-work /02_source/" of the virtual machine and unzip (unzip commands are as follows) :

|  ====> input :

.. code-block:: shell

   cd ~/my-work/02_source
   tar xf linux-4.14.98.*.tar.bz2

- Enter the kernel source directory

|  ====> input :

.. code-block:: shell

   cd ~/my-work/02_source/

- Configure cross-compiled environment variables

|  ====> input :

.. code-block:: shell

   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

**Compile the kernel target file**

|  ====> input :

.. code-block:: shell

   ./build.sh 8mmek240 2g kernel

|  EVK_MODE: Supports Settings of 8MEVK, 8MEK300, 8mMEK240;
|  EVK_MEM: Supported Settings are 2G, 1G, 3G, 4G.

**Compile the device tree object file**

|  ====> input :

.. code-block:: shell

   ./build.sh 8mmek240 2g dts

**Compile the kernel module package**

|  ====> input :

.. code-block:: shell

   ./build.sh 8mmek240 2g modules

**Target file**

|  Image, \*.dTB and Kernel-Modules.tar.bz2 in the out directory are the compiled target files

Compile the U-boot file
-------------------------

**Preparation before compilation**

- Download u-boot source code

|  Open the network disk to "2.1_OS\ _linux-4.14.98-> 02_Source" and download "u-boot-2018.03.*. Tar. Bz2", "build.sh" and "mkimage-imx_4.14.98.*. Tar. Bz2".
|  Copy to the "~/ My-work /02_source/" of the virtual machine and unzip (unzip commands are as follows) :
|  ====> input :

.. code-block:: shell

   tar xf u-boot-2018.03..tar.bz2
   tar xf mkimage-imx_4.14.98..tar.bz2

- Enter the kernel source directory

|  ====> input :

.. code-block:: shell

   cd ~/my-work/02_source/

- Configure cross-compiled environment variables

|  ====> input :

.. code-block:: shell

   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

**compile u-bootfile destination**

|  ====> input :

.. code-block:: shell

   ./build.sh 8mmek240 2g uboot

|  EVK_MODE: Supports Settings of 8MEVK, 8MEK300, 8mMEK240;
|  EVK_MEM: Supported Settings are 2G, 1G, 3G, 4G.

**Object file**

|  . Bin in out directory is the compiled target file

Compile all target files
--------------------------

|  ====> input :

.. code-block:: shell

   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env
   ./build.sh 8mmek240 2g all

|  EVK_MODE: Supports Settings of 8MEVK, 8MEK300, 8mMEK240;
|  EVK_MEM: Supported Settings are 2G, 1G, 3G, 4G.