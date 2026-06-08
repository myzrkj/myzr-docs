MYZR-A40I-EK204 android 编译参考手册
=====================================

|  源码包的下载需到我们提供的网盘上来进行下载 。下载到电脑后，需要通过Samba或其他方法将其复制到虚拟机上来。
|  我们可以创建一个A40I专属的目录来存放相关的源码，编译工具和以后用到的一些东西。如我的目录为：/home/liangyh/my-work/A40I，在此目录下我又创建了4个子目录：

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
   ~/my-work/A40I/02_sources$ cat android7.1_v3.tar.bz2* | tar xjv


android 源码编译
-----------------

**源码使用脚本编译，自动配置交叉编译工具，编译源码，最后打包生成板子 img 镜像文件。**

1. 编译lichee

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

2. 编译Android

.. code-block:: shell

   =====> Input:
   $ cd ../android
   $ source build/envsetup.sh

   =====> Output:
   lincluding device/asus/fugu/vendorsetup.sh
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

|  匹配编译好的lichee里的镜像

.. code-block:: shell

   =====> Input:
   $ extract-bsp

   =====> Output:
   /home/liangyh/my-work/A40I/02_sources/android7.1_v3/android/device/softwinner/a40-myzr/bImage copied!
   /home/liangyh/my-work/A40I/02_sources/android7.1_v3/android/device/softwinner/a40-myzr/modules copied!

|  编译：

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

|  打包固件：

.. code-block:: shell

   =====> Input:
   $ pack
   
   =====> Output:
   ......
   
   Dragon execute image.cfg SUCCESS !
   ----------image is at----------
   
   /home/liangyh/my-work/A40I/02_sources/android7.1_v3/lichee/tools/pack/sun8iw11p1_androidm_a40-myzr_uart0.img
   
   pack finish