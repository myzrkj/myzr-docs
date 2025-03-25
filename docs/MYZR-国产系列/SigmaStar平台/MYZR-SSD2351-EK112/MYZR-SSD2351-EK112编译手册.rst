MYZR-SSD2351-EK112编译手册
============================

安装软件包
----------------

|  ubuntu版本：ubuntu20.04
|  软件包安装：

.. code:: shell

   $ sudo apt-get install libc6-dev-i386 lib32z1  libuuid1 cmake libncurses5-dev 
   libncursesw5-dev bc xz-utils automake libtool libevdev-dev pkg-config mtd-utils  
   bison flex libssl-dev libmpc-dev squashfs-tools gawk make gcc git python rename

|  其他配置：
|  a.默认shell配置

|  编译脚本默认使用的是bash，要求系统的默认shell为bash，可通过ls -la /bin/sh命令来确认。以最常用的Ubuntu为例，高版本的Ubuntu默认shell为dash，修改方式如下：

.. code:: shell

   # ls -la /bin/sh
    lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> dash

    # sudo dpkg-reconfigure dash
    #在弹出的界面选择<NO>

    # ls -la /bin/sh
    lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> bash

|  b.设置默认python版本为python2.x (ubuntu20.04不需要配置，默认是python2.x)

|  python2与python3的语义有差别，SDK编译脚本使用的是python2的语义，因此需要将系统默认python版本设置为python2.x，修改方式请参考网络上的相关文档，比如使用update-alternatives工具来配置。

解压源码和交叉编译
-------------------

|  boot-Pcupid_DLD00V2.2.9.tar.gz: Uboot源码  
|  kernel-Pcupid_DLD00V2.2.9.tar.gz: kernel源码  
|  project-Pcupid_DLD00V2.2.9.tar.gz:编译制作image的部分，包含非开源部分的lib/ko，以及对外api头文件参考
|  sdk-Pcupid_DLD00V2.2.9.tar.gz:测试Demo/应用打包框架部分
|  arm-sigmastar-linux-gcc-12.4.0-uclibc-1.0.46-gnueabihf.tar.xz:  交叉编译工具

.. code:: shell

   $ mkdir ~/ssd2351/source -p
   $ tar zxvf boot-Pcupid_DLD00V2.2.9*.tar.gz -C ~/ssd2351/source 
   $ tar zxvf kernel-Pcupid_DLD00V2.2.9*.tar.gz -C ~/ssd2351/source
   $ tar zxvf project-Pcupid_DLD00V2.2.9*.tar.gz -C ~/ssd2351/source 
   $ tar zxvf sdk-Pcupid_DLD00V2.2.9*.tar.gz -C ~/ssd2351/source
   $ mkdir ~/ssd2351/tool/toolchain -p
   $ tar -xvf ./arm-sigmastar-linux-gcc-12.4.0-uclibc-1.0.46-gnueabihf.tar.xz -C ~/ssd2351/tool/toolchain

设置交叉编译工具
-----------------

.. code:: shell

   $ export PATH=~/ssd2351/tool/toolchain/arm-sigmastar-linux-gcc-12.4.0-uclibc-1.0.46-gnueabihf/bin:$PATH
   $ export CROSS_COMPILE=arm-sigmastar-linux-uclibcgnueabihf-12.4.0-
   $ export ARCH=arm
   $ ${CROSS_COMPILE}gcc -v

全局编译
---------

|  #全局编译，只要运行，会把boot,kernel，project，sdk编译

.. code:: shell

   $ cd ~/ssd2351/source/project/
   $ make dispcam_pcupid.spinand.uclibc-12.4.0-arm-squashfs.ssm001c.128.voip.qfn128_ddr3_defconfig
   $ make clean;make image -j8

|  #编译完成后生成的images在project/image/output/images
|  #注意：
|  #首次编译请务必在project下执行make clean;make image -j8命令完整编译（包含整编boot/kernel）
|  #为增加调试效率，除首次编译外，后续debug可以直接在project下编译对应修改模块然后重新快速打包即可，例如：
|  #仅编译kernel：

.. code:: shell

   $ cd ~/ssd2351/source/project/
   $ make linux-kernel_clean;make linux-kernel -j8

|  #仅编译boot：

.. code:: shell

   $ cd ~/ssd2351/source/project/
   $ make boot_clean;make boot -j8

|  #仅快速打包sdk image：

.. code:: shell

   $ cd ~/ssd2351/source/project/
   $ make image-fast-nocheck -j8


分立编译boot
--------------

|  #project下SDK编译已经添加boot编译选项，因此建议boot修改之后，直接在project下编译使用make boot编译boot，编译后不需要手动release到project下的路径，直接重新打包project即可

.. code:: shell

   $ cd ~/ssd2351/source/boot
   $ make pcupid_ssm001c_s01a_spinand_defconfig
   $ make clean;make -j8;

|  #注意：在boot目录下单独编译需要先将生成image手动release到project对应目录之后打包才行

.. code:: shell

   $ cp ~/ssd2351/source/boot/u-boot_spinand.xz.img.bin ~/ssd2351/source/project/board/uboot/u-boot.xz.img.bin

分立编译kernel
-----------------

|  #project下SDK编译已经添加kernel编译选项，因此建议kernel修改之后，直接在project下编译使用make linux-kernel编译kernel，编译后不需要手动release到project下的路径，直接重新打包project即可

.. code:: shell

   $ cd ~/ssd2351/source/kernel
   $ make pcupid_ssm001c_s01a_spinand_voip_defconfig
   $ make clean;make image -j8;

|  #注意：project中打包是直接软链接指向的kernel目录，所以kernel不需要再手动release，直接做project打包动作即可
|  #如果kernel 有新增kernel modules需要将相应的module添加到kernel_mod_list/kernel_mod_list_late（kernel_mod_list_late里的ko会在mi module之后装载）
|  #修改路径：project/kbuild/customize/6.1/pcupid/dispcam/kernel_mod_list

生成usb烧录镜像
-----------------

|  #按正常流程编译整包sdk，生成image升级文件。
|  #整包sdk编译成功后，执行./image/makefiletools/script/make_usb_factory_sigmastar.sh 脚本
|  #可以选择全部升级和部分分区升级：(y是全部更新，n是部分更新)

.. code:: shell

   $ cd ~/ssd2351/source/project/
   $ ./image/makefiletools/script/make_usb_factory_sigmastar.sh

|  提示：

.. code:: shell

   Full or Optional Upgrade ? (Y/N)y
   using alone TF-A:u-bl31.bin
   USB Facotry Image Generating.....
   success, usb factory image have generated:
         path:./image/output/images/SstarUsbImage_202502280425.bin
         size:48439296 byte
         md5sum:057c1f55ecbe0a4ecaaa916a8612bfe2