MYZR-RK3399-EK314 Android-8.1 Build Manual
===========================================

**Install ubuntu14.04**

|   Development Environment Guide： :doc:`《Ubuntu14.04+Win10 (Recommended)》 <../../COMMON/MYZR Windows-10 VirtualBox-5.2.12 Ubuntu-14.04.5 64-bit dev env Manual>`

Configuring the compilation environment
-----------------------------------------

Build a compilation environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Install and compile the required libraries（Ubuntu14.04）

.. code:: shell
    
    $sudo apt-get install git-core gnupg flex bison gperf libsdl1.2-dev \
    libesd0-dev libwxgtk2.8-dev squashfs-tools build-essential zip curl \
    libncurses5-dev zlib1g-dev pngcrush schedtool libxml2 libxml2-utils \
    xsltproc lzop libc6-dev schedtool g++-multilib lib32z1-dev \
    lib32ncurses5-dev lib32readline-gplv2-dev gcc-multilib libswitch-perl \
    libssl1.0.0 libssl-dev

- Install OpenJDK8

.. code:: shell
    
    $sudo apt-get install openjdk-8-jdk

|   在用户目录的.profile文件中添加下面内容：

.. code:: shell

    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin

|   Save the file, execute source .profile for the file to take effect, and then execute java -version to see if the java version is correct:

.. code:: shell

    $java -version
    openjdk version "1.8.0_222-ea"
    OpenJDK Runtime Environment (build 1.8.0_222-ea-8u222-b05-1~14.04-b05)
    OpenJDK 64-Bit Server VM (build 25.222-b05, mixed mode)

Download source code and extract it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Open the network disk to 02_源码 ->android-8.1
|   Download source package myrk3399_android8.tar.bz2 for all files

.. code:: shell
    
    $ mkdir rk3399
    $ cat myrk3399_android8.tar.bz2* | tar xj -C rk3399

Compile
~~~~~~~~

- Compile uboot

.. code:: shell
    
    $cd u-boot
    $make clean
    $make myzr-rk3399_defconfig
    $make ARCHV=aarch64 -j8

- Compile the kernel

.. code:: shell
    
    $cd kernel
    $make ARCH=arm64 myzr_defconfig -j8
    $make -j8 ARCH=arm64 rk3399-myzr-hdmi.img

- Compile android

.. code:: shell

    $cd android8.1
    $source build/envsetup.sh
    $lunch rk3399-userdebug
    $make -j8

Package image
~~~~~~~~~~~~~~~

.. code:: shell

    $./mkimage.sh

|   Get the target file in the rockdev / Image-rk3399 directory:

.. code:: shell

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

Packed into unified firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell
    
    $./MYTools/mkupdate.sh update

|   Get the target file in the rockdev / Image-rk3399 directory:

.. code:: shell
    
    rk3399_Android8.1.0_191030.img