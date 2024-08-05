编译手册
========


编译环境要求
-------------

1. 编译主机需在ubuntu系统中进行，且版本需Ubuntu 20.04以上，本人主机系统为Ubuntu 20.04

2. 主机需可连接外网，因为编译系统过程需要下载某些文件。


下载源码包
-----------

1. 网盘中02_源码目录下，下载源码包 MYZR-RK3588_Android12_20240110.tar.bz2 

2. 创建编译目录：

.. code:: shell

    mkdir ~/my-work/RK3588/05_android -p

3. 把源码放到此目录中，并进行解压：

.. code:: shell

    tar xvf MYZR-RK3588_Android12_20240110.tar.bz2 -C ~/my-work/RK3588/05_android/



配置编译环境
------------

1. 每次打开一个新的终端，都需要进行一个环境配置

2. 进入3588-android12目录

3. 输入如下命令配置java环境：

.. code:: shell

    source javaenv.sh

4. 输入如下命令配置编译环境：

.. code:: shell

    source build/envsetup.sh

5. 输入如下命令配置平台环境：

.. code:: shell

    lunch rk3588_s-userdebug


整体编译
-----------

1. 整体编译将整个android系统，包括kernel、uboot、android、recovery。

2. 输入如下命令：

.. code:: shell

    ./build.sh -AUCKu

3. 编译时间较长，本人使用16线程主机编译需要4个小时时间（仅作参考！）

4. 成功编译后在rockdev/Image-rk3588_s/目录下可看到相关镜像，其中update.img是所有镜像的集合。


单独编译 uboot 
--------------

1. 编译前可先清除生成文件

.. code:: shell

    cd u-boot/
    make clean

2. 回到SDK主目录，并进行uboot单独编译

.. code:: shell

    cd ../
    ./build.sh -U


单独编译 Kernel
---------------

1. 编译前可先清除生成文件

.. code:: shell

    cd kernel-5.10/
    make clean

2. 回到SDK主目录，并进行kernel单独编译

.. code:: shell

    cd ../
    ./build.sh -CKA

3. 或使用如下命令：

需要先安装gcc编译器

.. code:: shell

    sudo apt-get install gcc-aarch64-linux-gnu

输入如下命令编译：

.. code:: shell

    cd kernel-5.10/
    export PATH=../prebuilts/clang/host/linux-x86/clang-r416183b/bin:$PATH
    alias msk='make CROSS_COMPILE=aarch64-linux-gnu- LLVM=1 LLVM_IAS=1'
    msk ARCH=arm64 rockchip_defconfig
    msk ARCH=arm64 BOOT_IMG=../rockdev/Image-rk3588_s/boot.img myzr-rk3588.img -j24

编译完成手动赋值镜像：

.. code:: shell

    cp boot.img ../rockdev/Image-rk3588_s/boot.img

    
单独编译 android
------------------

1. 在android12主目录下

.. code:: shell

    ./build.sh -A


打包update.img
--------------

1. 在rockdev将镜像打包成update.img

2. 在android12主目录下

.. code:: shell

    ./build.sh -u


--------------------------------------------------------------------------------

::

    --------------------------------------------------------------------------------
    * 珠海明远智睿科技有限公司
    * ZhuHai MYZR Technology CO.,LTD.
    * Latest Update: 2024/1/10
    * Supporter: Kuangwh
    --------------------------------------------------------------------------------
