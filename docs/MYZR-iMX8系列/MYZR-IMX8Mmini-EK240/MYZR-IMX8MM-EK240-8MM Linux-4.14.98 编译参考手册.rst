MYZR-IMX8MM-EK240-8MM Linux-4.14.98 编译参考手册
=================================================

工具安装
----------

**安装交叉编译工具**

- 创建安装目录

|  =====> 输入指令：

.. code-block:: shell

   mkdir ~/my-work/03_toolchain -p

|  =====> 输入指令：

.. code-block:: shell
   
   cd ~/my-work/03_toolchain

- 下载交叉编译工具

|  =====> 输入指令：

.. code-block:: shell
   
   wget https://releases.linaro.org/components/toolchain/binaries/7.3-2018.05/aarch64-linux-gnu/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.tar.xz

- 解压交叉编译工具

|  =====> 输入指令：

.. code-block:: shell

   tar xf gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.tar.xz -C ~/my-work/03_toolchain

- 创建交叉编译工具配置脚本

|  =====> 输入指令：

.. code-block:: shell

   cat << EOF > ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env
   #!/bin/sh
   export PATH=${HOME}/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu/bin:${PATH}
   export ARCH=arm64
   export CROSS_COMPILE=aarch64-linux-gnu-
   EOF

|  =====> 输入指令：

.. code-block:: shell
   
   chmod +x ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

- 配置交叉编译环境变量

|  =====> 输入指令：

.. code-block:: shell

   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

- 检查安装

|  =====> 输入指令：

.. code-block:: shell
   
   ${CROSS_COMPILE}gcc -v

|  =====> 输出信息：

.. code-block:: shell

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

**安装库**

|  =====> 输入指令：

.. code-block:: shell

   sudo apt install zlib1g 
   sudo apt install zlib1g-dev 
   apt-get install device-tree-compiler

编译内核文件
-------------

**编译前的准备**

- 创建工作目录

|  =====> 输入指令：

.. code-block:: shell

   mkdir ~/my-work/02_source/ -p

- 下载内核源码

|  打开网盘到 “2.1_OS_Linux-4.14.98 -> 02_Source”，下载 “linux-4.14.98.*.tar.bz2”与"build.sh"。
|  复制到虚拟机的 “~/my-work/02_source/”，并解压（解压命令如下）：

|  =====> 输入指令：

.. code-block:: shell

   cd ~/my-work/02_source
   tar xf linux-4.14.98.*.tar.bz2

- 进入内核源码目录

|  =====> 输入指令：

.. code-block:: shell

   cd ~/my-work/02_source/

- 配置交叉编译环境变量

|  =====> 输入指令：

.. code-block:: shell

   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

**编译内核目标文件**

|  =====> 输入指令：

.. code-block:: shell

   ./build.sh 8mmek240 2g kernel

|  EVK_MODE：支持的设置为 8mevk、8mek300、8mmek240；
|  EVK_MEM：支持的设置为 2g、1g、3g、4g。

**编译设备树目标文件**

|  =====> 输入指令：

.. code-block:: shell

   ./build.sh 8mmek240 2g dts

**编译内核模块包**

|  =====> 输入指令：

.. code-block:: shell

   ./build.sh 8mmek240 2g modules

**目标文件**

|  out 目录中 Image、\*.dtb 和 kernel-modules.tar.bz2 即编译得到的目标文件

编译u-boot文件
---------------

**编译前的准备**

- 下载u-boot源码

|  打开网盘到 “2.1_OS_Linux-4.14.98 -> 02_Source”，下载 “u-boot-2018.03..tar.bz2”、"build.sh"和“mkimage-imx_4.14.98..tar.bz2”。
|  复制到虚拟机的 “~/my-work/02_source/”，并解压（解压命令如下）：
|  =====> 输入指令：

.. code-block:: shell

   tar xf u-boot-2018.03..tar.bz2
   tar xf mkimage-imx_4.14.98..tar.bz2

- 进入内核源码目录

|  =====> 输入指令：

.. code-block:: shell

   cd ~/my-work/02_source/

- 配置交叉编译环境变量

|  =====> 输入指令：

.. code-block:: shell

   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env

**编译u-boot目标文件**

|  =====> 输入指令：

.. code-block:: shell

   ./build.sh 8mmek240 2g uboot

|  EVK_MODE：支持的设置为 8mevk、8mek300、8mmek240；
|  EVK_MEM：支持的设置为 2g、1g、3g、4g。

**目标文件**

|  out目录中 \*.bin 即编译得到的目标文件

编译所有目标文件
----------------

|  =====> 输入指令：

.. code-block:: shell

   source ~/my-work/03_toolchain/gcc-linaro-7.3.1-2018.05-x86_64_aarch64-linux-gnu.env
   ./build.sh 8mmek240 2g all

|  EVK_MODE：支持的设置为 8mevk、8mek300、8mmek240；
|  EVK_MEM：支持的设置为 2g、1g、3g、4g。