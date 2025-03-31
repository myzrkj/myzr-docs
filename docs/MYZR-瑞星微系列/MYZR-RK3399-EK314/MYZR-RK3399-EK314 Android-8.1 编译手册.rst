Android-8.1 编译手册
======================

**安装ubuntu14.04**

|   开发环境指导手册：:doc:`《Ubuntu14.04+Win10 (推荐)》 </docs/COMMON/MYZR Windows-10 VirtualBox-5.2.12 Ubuntu-14.04.5 64位开发环境指导>`


**配置编译环境**

搭建编译环境
~~~~~~~~~~~~

- 安装编译所需库（Ubuntu14.04）

.. code-block:: shell
    
    $sudo apt-get install git-core gnupg flex bison gperf libsdl1.2-dev \
    libesd0-dev libwxgtk2.8-dev squashfs-tools build-essential zip curl \
    libncurses5-dev zlib1g-dev pngcrush schedtool libxml2 libxml2-utils \
    xsltproc lzop libc6-dev schedtool g++-multilib lib32z1-dev \
    lib32ncurses5-dev lib32readline-gplv2-dev gcc-multilib libswitch-perl \
    libssl1.0.0 libssl-dev

- 安装OpenJDK8

.. code-block:: shell
    
    $sudo apt-get install openjdk-8-jdk

|   在用户目录的.profile文件中添加下面内容：

.. code-block:: shell

    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin

|   保存文件，执行source .profile让文件生效然后执行java -version查看java版本是否正确：

.. code-block:: shell

    $java -version
    openjdk version "1.8.0_222-ea"
    OpenJDK Runtime Environment (build 1.8.0_222-ea-8u222-b05-1~14.04-b05)
    OpenJDK 64-Bit Server VM (build 25.222-b05, mixed mode)

下载源码并解压
~~~~~~~~~~~~~~

|   打开网盘到 02_源码 ->android-8.1
|   下载源码包myrk3399_android8.tar.bz2的所有文件

.. code-block:: shell
    
    $ mkdir rk3399
    $ cat myrk3399_android8.tar.bz2* | tar xj -C rk3399

编译
~~~~~

- 编译uboot

.. code-block:: shell
    
    $cd u-boot
    $make clean
    $make myzr-rk3399_defconfig
    $make ARCHV=aarch64 -j8

- 编译kernel

.. code-block:: shell
    
    $cd kernel
    $make ARCH=arm64 myzr_defconfig -j8
    $make -j8 ARCH=arm64 rk3399-myzr-hdmi.img

- 编译android

.. code-block:: shell

    $cd android8.1
    $source build/envsetup.sh
    $lunch rk3399-userdebug
    $make -j8

打包镜像
~~~~~~~~

.. code-block:: shell

    $./mkimage.sh

|   于rockdev/Image-rk3399目录得到目标文件：

.. code-block:: shell

    boot.img  
    kernel.img  
    MiniLoaderAll.bin  
    misc.img  
    oem.img  
    parameter.txt    
    recovery.img  
    resource.img  
    system.img  
    trust.img 
    uboot.img  
    vendor.img

打包成统一固件
~~~~~~~~~~~~~~~

.. code-block:: shell
    
    $./MYTools/mkupdate.sh update

|   于rockdev/Image-rk3399目录得到目标文件：

.. code-block:: shell
    
    rk3399_Android8.1.0_191030.img