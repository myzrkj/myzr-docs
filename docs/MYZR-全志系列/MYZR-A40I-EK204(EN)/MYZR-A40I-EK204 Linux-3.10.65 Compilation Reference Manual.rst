MYZR-A40I-EK204 Linux-3.10.65 Compilation Reference Manual
=============================================================

|  The source code package must be downloaded from the network disk we provide. After downloading to your computer, you need to copy it to the virtual machine via Samba or other methods.
|  We can create a directory dedicated to A40I to store related source code, compilation tools, and other things that will be used later. For example, my directory is: /home/liangyh/my-work/A40I, and under this directory I have created 4 subdirectories:

.. code-block:: shell

   =====> Input:
   liangyh@FS12:~/my-work/A40I$ ls
   01_image 02_sources 03_toolchain 04_app

|  Directory 01 can be used to place the compiled images (will be explained later when used)
|  Directory 02 is used to place source code
|  Directory 03 is used to place cross-compilation tool configuration scripts
|  Directory 04 can be used to place our own applications (allocated by the user)
|  Use Samba or other methods to copy the source code package to the ~/my-work/A40I/02_sources directory in the virtual machine, then extract the source code package to the current directory:

.. code-block:: shell

   =====> Input:
   ~/my-work/A40I/02_sources$ cat repo_A40I.tar.bz2a* | tar xjv

|  Create cross-compilation tool configuration script

.. code-block:: shell

   =====> 输入指令：
   cat << EOF > ~/my-work/A40I/03_toolchain/arm-openwrt-linux-muslgnueabi.sh
   #!/bin/sh
   export PATH=${HOME}/my-work/A40I/02_sources/repo_A40I/prebuilt/gcc/linux-x86/arm/toolchain-sunxi-musl/toolchain/bin/:${PATH}
   export ARCH=arm
   export CROSS_COMPILE=${HOME}/my-work/A40I/02_sources/repo_A40I/prebuilt/gcc/linux-x86/arm/toolchain-sunxi-musl/toolchain/bin/arm-openwrt-linux-muslgnueabi-
   export CC=${HOME}/my-work/A40I/02_sources/repo_A40I/prebuilt/gcc/linux-x86/arm/toolchain-sunxi-musl/toolchain/bin/arm-openwrt-linux-muslgnueabi-gcc
   EOF

|  Get executable permission

.. code-block:: shell

   chmod +x ~/my-work/A40I/03_toolchain/arm-openwrt-linux-muslgnueabi.sh

tina Source Code Compilation
------------------------------

|  The source code is compiled using scripts, which automatically configure the cross-compilation tools, compile the source code, and finally package to generate the board img image file.

1. Set up the environment

.. code-block:: shell

   =====> Input:
   $ sudo apt-get install libssl-dev
   $ sudo apt-get install gperf
   $ sudo apt-get install lib32stdc++6

   =====> Input:
   $ source build/envsetup.sh

   =====> Output:
   Setup env done! Please run lunch next.

2. Set the compilation platform

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

3. Compile uboot

.. code-block:: shell

   =====> Input:
   $ muboot

4. Compile kernel

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

5. Package the firmware

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

|  Generated firmware address:

.. code-block:: shell

   repo_A40I/out/r40-m2ultra/tina_r40-m2ultra_uart0.img


Application Programming Example
---------------------------------

|  Use Samba or other methods to copy the source code package to the ~/my-work/A40I/04_app directory in the virtual machine.

1. Configure cross-compilation tools

.. code-block:: shell

   =====> Input:
   $ source ~/my-work/A40I/03_toolchain/arm-openwrt-linux-muslgnueabi.sh 

2. Verify cross-compilation tool configuration

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

3. Start compilation

.. code-block:: shell

   =====> Input:
   ${CC} hello_world.c -o hello_world

4. Execute

|  Move the compiled binary file hello_world to the development board (refer to the file transfer in the previous experience section for the moving method).
|  Grant executable permission and execute the file

.. code-block:: shell

   =====> Input:
   # chmod +x hello_world
   # ./hello_world

   =====> Output:
   hello world!!!

|  After successful operation, the "hello world" message will be output successfully.