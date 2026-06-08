MYZR-A40I-EK204 Android Compilation Reference Manual
======================================================

| The source code package needs to be downloaded from the network disk we provide. After downloading to your computer, you need to copy it to the virtual machine via Samba or other methods.
| We can create a directory dedicated to A40I to store related source code, compilation tools, and other things that will be used later. For example, my directory is: /home/liangyh/my-work/A40I, and under this directory I have created 4 subdirectories:

.. code-block:: shell

   =====> Input:
   liangyh@FS12:~/my-work/A40I$ ls
   01_image 02_sources 03_toolchain 04_app

| Directory 01 can be used to place the compiled images (will be explained later when used)
| Directory 02 is used to place the source code
| Directory 03 is used to place the cross-compilation tool configuration scripts
| Directory 04 can be used to place our own applications (allocated by the user)
| Use Samba or other methods to copy the source code package to the ~/my-work/A40I/02_sources directory in the virtual machine, then extract the source code package to the current directory:

.. code-block:: shell

   =====> Input:
   ~/my-work/A40I/02_sources$ cat android7.1_v3.tar.bz2* | tar xjv


Android Source Code Compilation
----------------------------------

**The source code is compiled using scripts, which automatically configure the cross-compilation tools, compile the source code, and finally package to generate the board img image file.**

1. Compile lichee

.. code-block:: shell

   =====> Input:
   $ cd ~/my-work/A40I/02_sources/android7.1_v3/lichee
   $ ./build.sh
   =====> Output:
   INFO: ----------------------------------------
   INFO: build lichee ...
   INFO: chip: sun8iw11p1
   INFO: platform: androidm
   INFO: kernel: linux-3.10
   INFO: board: a40-myzr
   INFO: output: out/sun8iw11p1/androidm/a40-myzr
   INFO: ----------------------------------------

   ......

   #### make completed successfully (23:30 (mm:ss)) ####

2. Compile Android

.. code-block:: shell

   =====> Input:
   $ cd ../android
   $ source build/envsetup.sh

   =====> Output:
   including device/asus/fugu/vendorsetup.sh
   including device/generic/mini-emulator-arm64/vendorsetup.sh
   including device/generic/mini-emulator-armv7-a-neon/vendorsetup.sh
   including device/generic/mini-emulator-mips64/vendorsetup.sh

   ......

   =====> Input:
   $ lunch a40_myzr-user

   =====> Output:
   ============================================
   PLATFORM_VERSION_CODENAME=REL
   PLATFORM_VERSION=7.1.1
   TARGET_PRODUCT=a40_myzr

   ......

| Match the compiled image in lichee

.. code-block:: shell

   =====> Input:
   $ extract-bsp

   =====> Output:
   /home/liangyh/my-work/A40I/02_sources/android7.1_v3/android/device/softwinner/a40-myzr/bImage copied!
   /home/liangyh/my-work/A40I/02_sources/android7.1_v3/android/device/softwinner/a40-myzr/modules copied!

| Compile:

.. code-block:: shell

   =====> Input:
   $ make -j16

   =====> Output:
   ......

   Creating filesystem with parameters:
       Size: 1610612736
       Block size: 4096
       Blocks per group: 32768
       Inodes per group: 8192
       Inode size: 256
       Journal blocks: 6144
       Label: system
       Blocks: 393216
       Block groups: 12
       Reserved block group size: 95
   Created filesystem with 2442/98304 inodes and 171693/393216 blocks
   [100% 28462/28462] Install system fs image: out/target/product/a40-myzr/system.img
   out/target/product/a40-myzr/system.img+out/target/product/a40-myzr/obj/PACKAGING/recovery_patch_intermediates/recovery_from_boot.p maxsize=1644331392 blocksize=4224 total=680351248 reserve=16612992

   #### make completed successfully (01:02:01 (hh:mm:ss)) ####

| Package the firmware:

.. code-block:: shell

   =====> Input:
   $ pack
   
   =====> Output:
   ......
   
   Dragon execute image.cfg SUCCESS !
   ----------image is at----------
   
   /home/liangyh/my-work/A40I/02_sources/android7.1_v3/lichee/tools/pack/sun8iw11p1_androidm_a40-myzr_uart0.img
   
   pack finish