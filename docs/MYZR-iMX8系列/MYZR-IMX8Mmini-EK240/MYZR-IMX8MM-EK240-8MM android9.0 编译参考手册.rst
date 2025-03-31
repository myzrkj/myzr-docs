MYZR-IMX8MM-EK240-8MM android9.0 编译参考手册
===============================================

i.Mx8mm android9.0编译手册
----------------------------

编译环境搭建
~~~~~~~~~~~~~

- ubuntu16.04
- openjdk8

**依赖包安装**

.. code-block:: shell

    sudo apt-get install uuid uuid-dev
    sudo apt-get install zlib1g-dev liblz-dev
    sudo apt-get install liblzo2-2 liblzo2-dev
    sudo apt-get install lzop
    sudo apt-get install git-core curl
    sudo apt-get install u-boot-tools
    sudo apt-get install mtd-utils
    sudo apt-get install android-tools-fsutils
    sudo apt-get install openjdk-8-jdk
    sudo apt-get install device-tree-compiler
    sudo apt-get install gdisk
    sudo apt-get install m4
    sudo apt-get install libz-dev

**安装openjdk8**

.. code-block:: shell

    sudo add-apt-repository ppa:openjdk-r/ppa
    sudo apt-get update
    sudo apt-get install openjdk-8-jdk

- 编辑用户目录下的.profile文件中添加下面内容

.. code-block:: shell

    vim ~/.profile

在文件未尾添加下面内容
----------------------

.. code-block:: shell

    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin

- 重新加载.profile文件

.. code-block:: shell

    source ~/.profile

查看jdk版本，验证安装
---------------------

.. code-block:: shell

    java -version

    openjdk version "1.8.0_242"
    OpenJDK Runtime Environment (build 1.8.0_242-8u242-b08-0ubuntu3~16.04-b08)
    OpenJDK 64-Bit Server VM (build 25.242-b08, mixed mode)

准备源码包
~~~~~~~~~~~

**下载源码包**

- 到百度网盘MYZR-iMX8-201907/2.2_OS_Android9.1/02_Source目录下载imx8mm_android9.tar.bz2*的所有压缩包

**解压源码**

.. code-block:: shell

    cat imx8mm_android9.tar.bz2* | tar xvj

编译
~~~~~

**设置环境变量**

.. code-block:: shell

    export ANDROID_HOME=~/imx8mm_android
    export ARCH=arm64
    export CROSS_COMPILE=~/imx8mm_android/prebuilts/gcc/linux-x86/aarch64/aarch64-linux-android-4.9/bin/aarch64-linux-android-
    source build/envsetup.sh
    lunch evk_8mm-userdebug

**编译system**

- 开始编译

.. code-block:: shell

    cd $ANDROID_HOME
    make 2>&1 -j8 | tee build-log.txt

**编译uboot**

.. code-block:: shell

    cd $ANDROID_HOME
    make bootloader -j8

**编译内核**

.. code-block:: shell

    cd $ANDROID_HOME
    cd vendor/nxp-opensource/kernel_imx
    make myzr_imx8mm_android_defconfig
    make KCFLAGS=-mno-android -j8

**编译bootimage**

.. code-block:: shell

    cd $ANDROID_HOME
    make bootimage -j8

**编译dtboimage**

.. code-block:: shell

    cd $ANDROID_HOME
    make dtboimage -j8

**目标文件**

.. code-block:: shell

    cd $ANDROID_HOME
    cd out/target/product/evk_8mm

|   下面是我们需要的文件

|   boot.img
|   dtbo-imx8mm.img
|   system.img
|   partition-table.img
|   u-boot-imx8mm.imx
|   u-boot-imx8mm-evk-uuu.imx
|   vbmeta-imx8mm.img
|   vendor.img