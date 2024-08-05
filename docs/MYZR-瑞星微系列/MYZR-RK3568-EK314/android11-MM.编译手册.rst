编译手册
========


编译环境要求
-------------

1. 编译主机需在ubuntu系统中进行，且版本需Ubuntu 18.04以上，本人主机系统为Ubuntu 18.04

2. 主机需可连接外网，因为编译系统过程需要下载某些文件。


下载源码包
-----------

1. 网盘中02_源码目录下，下载源码包 MYZR-RK3568_Android11_20240109.tar.bz2 

2. 创建编译目录：

.. code:: shell

    mkdir ~/my-work/rk3568/05_android -p

3. 把源码放到此目录中，并进行解压：

.. code:: shell

    tar xvf MYZR-RK3568_Android11_20240109.tar.bz2 -C ~/my-work/rk3568/05_android/



配置编译环境
------------

1. 每次打开一个新的终端，都需要进行一个环境配置

2. 进入RK356X_Android11目录

3. 输入如下命令配置java环境：

.. code:: shell

    source javaenv.sh

4. 输入如下命令配置编译环境：

.. code:: shell

    source build/envsetup.sh

5. 输入如下命令配置平台环境：

.. code:: shell

    lunch rk3568_r-userdebug


整体编译
-----------

1. 整体编译将整个android系统，包括kernel、uboot、android、recovery。

2. 输入如下命令：

.. code:: shell

    ./build.sh -AUCKu

3. 编译时间较长，本人使用16线程主机编译需要4个小时时间（仅作参考！）

4. 成功编译后在rockdev/Image-rk3568_r/目录下可看到相关镜像，其中update.img是所有镜像的集合。


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

    cd kernel/
    make clean

2. 回到SDK主目录，并进行kernel单独编译

.. code:: shell

    cd ../
    ./build.sh -CKA

3. 或使用kernel脚本进行编译

.. code:: shell

    cd kernel/
    ./make.sh
    cp boot.img ../rockdev/Image-rk3568_r/boot.img

    
单独编译 android
------------------

1. 在SDK主目录下

.. code:: shell

    ./build.sh -A


打包update.img
--------------

1. 在rockdev将镜像打包成update.img

2. 在SDK主目录下

.. code:: shell

    ./build.sh -u


--------------------------------------------------------------------------------

::

    --------------------------------------------------------------------------------
    * 珠海明远智睿科技有限公司
    * ZhuHai MYZR Technology CO.,LTD.
    * Latest Update: 2024/1/9
    * Supporter: Kuangwh
    --------------------------------------------------------------------------------
