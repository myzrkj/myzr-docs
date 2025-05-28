MYZR-A40I-EK204 Linux-3.10.65 编译参考手册
===========================================

|  源码包的下载需到我们提供的网盘上来进行下载 。下载到电脑后，需要通过Samba或其他方法将其复制到虚拟机上来。
|  ​我们可以创建一个A40I专属的目录来存放相关的源码，编译工具和以后用到的一些东西。如我的目录为：/home/liangyh/my-work/A40I，在此目录下我又创建了4个子目录：

.. code-block:: shell

   =====> Input:
   liangyh@FS12:~/my-work/A40I$ ls
   01_image 02_sources 03_toolchain 04_app

|  01目录可以用来放置我们编译好的镜像（以后用到会说明）
|  02目录则是用来放置源码
|  03目录则是放置交叉编译工具配置脚本
|  04目录我们可以用来放置自己的应用（用户自己分配）
|  使用Samba或其他方法将源码包复制到虚拟机中的~/my-work/A40I/02_sources目录下后将源码包解压到当前目录下：

.. code-block:: shell

   =====> Input:
   ~/my-work/A40I/02_sources$ cat repo_A40I.tar.bz2a* | tar xjv

|  创建交叉编译工具配置脚本

.. code-block:: shell

   =====> 输入指令：
   cat << EOF > ~/my-work/A40I/03_toolchain/arm-openwrt-linux-muslgnueabi.sh
   #!/bin/sh
   export PATH=${HOME}/my-work/A40I/02_sources/repo_A40I/prebuilt/gcc/linux-x86/arm/toolchain-sunxi-musl/toolchain/bin/:${PATH}
   export ARCH=arm
   export CROSS_COMPILE=${HOME}/my-work/A40I/02_sources/repo_A40I/prebuilt/gcc/linux-x86/arm/toolchain-sunxi-musl/toolchain/bin/arm-openwrt-linux-muslgnueabi-
   export CC=${HOME}/my-work/A40I/02_sources/repo_A40I/prebuilt/gcc/linux-x86/arm/toolchain-sunxi-musl/toolchain/bin/arm-openwrt-linux-muslgnueabi-gcc
   EOF

|  获取可执行权限

.. code-block:: shell

   chmod +x ~/my-work/A40I/03_toolchain/arm-openwrt-linux-muslgnueabi.sh

tina 源码编译
---------------

|  源码使用脚本编译，自动配置交叉编译工具，编译源码，最后打包生成板子 img 镜像文件。

1. 设置环境

.. code-block:: shell

   =====> Input:
   $ sudo apt-get install libssl-dev
   $ sudo apt-get install gperf
   $ sudo apt-get install lib32stdc++6

   =====> Input:
   $ source build/envsetup.sh

   =====> Output:
   Setup env done! Please run lunch next.

2. 设置编译平台

.. code-block:: shell

   =====> Input:
   $ lunch r40_m2ultra-tina

   =====> Output:
   ============================================
   TINA_BUILD_TOP=/home/liangyh/my-work/A40I/02_sources/repo_A40I
   TINA_TARGET_ARCH=arm
   TARGET_PRODUCT=r40_m2ultra
   TARGET_PLATFORM=r40
   TARGET_BOARD=r40-m2ultra
   TARGET_PLAN=m2ultra
   TARGET_BUILD_VARIANT=tina
   TARGET_BUILD_TYPE=release
   TARGET_KERNEL_VERSION=3.10
   TARGET_UBOOT=u-boot-2014.07
   TARGET_CHIP=sun8iw11p1
   ============================================

3. 编译uboot

.. code-block:: shell

   =====> Input:
   $ muboot

4. 编译kernel

.. code-block:: shell

   =====> Input:
   $ make 

   =====> Output:
   Checking 'working-make'... ok.
   Checking 'case-sensitive-fs'... ok.
   Checking 'gcc'... ok.
   Checking 'working-gcc'... ok.

   ......

   #### make completed successfully (23:30 (mm:ss)) ####

5. 打包固件

.. code-block:: shell

   =====> Input:
   $ pack

   =====> Output:
   No kernel param, parse it from r40
   copying tools file
   copying configs file

   ......

   /home/liangyh/my-work/A40I/02_sources/repo_A40I/out/r40-m2ultra/tina_r40-m2ultra_uart0.img

   pack finish

|  生成固件地址：

.. code-block:: shell

   repo_A40I/out/r40-m2ultra/tina_r40-m2ultra_uart0.img


应用编程示例
-------------

|  使用Samba或其他方法将源码包复制到虚拟机中的~/my-work/A40I/04_app目录下。

1. 配置交叉编译工具

.. code-block:: shell

   =====> Input:
   $ source ~/my-work/A40I/03_toolchain/arm-openwrt-linux-muslgnueabi.sh 

2. 检验交叉编译工具配置

.. code-block:: shell

   =====> Input:
   $CC -v

   =====> Output:
   Reading specs from /home/liangyh/my-work/A40I/02_sources/repo_A40I/prebuilt/gcc/linux-x86/arm/toolchain-sunxi-musl/toolchain/bin/../lib/gcc/arm-openwrt-linux-muslgnueabi/6.4.1/specs
   COLLECT_GCC=arm-openwrt-linux-muslgnueabi-gcc.bin
   COLLECT_LTO_WRAPPER=/home/liangyh/my-work/A40I/02_sources/repo_A40I/prebuilt/gcc/linux-x86/arm/toolchain-sunxi-musl/toolchain/bin/../libexec/gcc/arm-openwrt-linux-muslgnueabi/6.4.1/lto-wrapper
   Target: arm-openwrt-linux-muslgnueabi
   Configured with: /home/caiyongheng/tina/out/astar-parrot/compile_dir/toolchain/gcc-linaro-6.4-2017.11/configure --with-bugurl=https://dev.openwrt.org/ --with-pkgversion='OpenWrt/Linaro GCC 6.4-2017.11 2017-11' --prefix=/home/caiyongheng/tina/out/astar-parrot/staging_dir/toolchain --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=arm-openwrt-linux-muslgnueabi --with-gnu-ld --enable-target-optspace --enable-libgomp --disable-libmudflap --disable-multilib --disable-nls --without-isl --without-cloog --with-host-libstdcxx=-lstdc++ --with-gmp=/home/caiyongheng/tina/out/host --with-mpfr=/home/caiyongheng/tina/out/host --with-mpc=/home/caiyongheng/tina/out/host --disable-decimal-float --with-diagnostics-color=auto-if-env --disable-libssp --enable-__cxa_atexit --with-arch=armv7-a --with-float=hard --with-headers=/home/caiyongheng/tina/out/astar-parrot/staging_dir/toolchain/include --disable-libsanitizer --enable-languages=c,c++ --enable-shared --enable-threads --with-slibdir=/home/caiyongheng/tina/out/astar-parrot/staging_dir/toolchain/lib --enable-lto --with-libelf=/home/caiyongheng/tina/out/host
   Thread model: posix
   gcc version 6.4.1 (OpenWrt/Linaro GCC 6.4-2017.11 2017-11)

3. 开始编译

.. code-block:: shell

   =====> Input:
   ${CC} hello_world.c -o hello_world

4. 执行

|  将编译出的二进制文件hello_world移动到开发板（移动方法参考前面体验篇的文件传输）。
|  给予可执行权限并执行文件

.. code-block:: shell

   =====> Input:
   # chmod +x hello_world
   # ./hello_world

   =====> Output:
   hello world!!!

|  成功运行后成功输出 hello world 的信息。