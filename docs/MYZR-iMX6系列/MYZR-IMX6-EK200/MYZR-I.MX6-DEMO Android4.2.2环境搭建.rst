
MYZR-I.MX6-DEMO Android4.2.2环境搭建
======================================

安装ubuntu12.04
----------------

|   在这里建议用户使用64bit的ubuntu12.04的操作系统，已经真机编译验证过。

安装JDK1.6 SE
--------------

|   登陆http://www.myzr.com.cn的下载专区，下载jdk-6u45-linux-x64.bin文件

.. code:: shell

    $ cd /usr
    $ sudo mkdir java
    $ cd java
    $ sudo cp ~ /jdk-6u45-linux-x64.bin ./
    $ sudo chmod 777 ./jdk-6u45-linux-x64.bin
    $ sudo ./jdk-6u45-linux-x64.bin
    $ sudo gedit /etc/profile

|   增加以下环境变量

.. code:: shell

    export JAVA_HOME=/usr/java/jdk1.6.0_45
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin
    $ source /etc/profile
    $ java -version

|   （看到版本为1.6.0_45就表示成功）

安装编译Android系统所需要的库
-----------------------------

|   (详细信息，请看网站[http://source.android.com/source/initializing.html])

.. code:: shell

    $ sudo apt-get install git gnupg flex bison gperf build-essential zip curl libc6-dev libncurses5-dev:i386 x11proto-core-dev libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-glx:i386 libgl1-mesa-dev g++-multilib mingw32 tofrodos python-markdown libxml2-utils xsltproc zlib1g-dev:i386
    $ sudo ln -s /usr/lib/i386-linux-gnu/mesa/libGL.so.1 /usr/lib/i386-linux-gnu/libGL.so
    $ sudo apt-get install gcc:i386 linux-libc-dev:i386
    $ sudo apt-get install uuid uuid-dev
    $ sudo apt-get install zlib1g-dev liblz-dev
    $ sudo apt-get install liblzo2-2 liblzo2-dev
    $ sudo apt-get install uuid-dev:i386
    $ sudo apt-get install liblzo2-dev:i386
    $ sudo ln -sf /lib/i386-linux-gnu/libuuid.so.1 /usr/lib/libuuid.so

下载源码并解压源码
------------------

下载源码
~~~~~~~~~

|   登陆http://www.myzr.com.cn下载专区下载Android4.2源码
|   Android4.2的源码包：myzr_android4_2_2_1_1_0.tar.bz2

解压源码
~~~~~~~~~

.. code:: shell

    $ mkdir ~/myandroid
    $ cd ~
    $ tar -jxvf myzr_android4_2_2_1_1_0.tar.bz2 -C ~/myandroid

编译源码（Android系统）
~~~~~~~~~~~~~~~~~~~~~~~

**设置环境变量**

.. code:: shell

    $ export ARCH=arm
    $ export CROSS_COMPILE=~/myandroid/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi- $ export PATH=~/myandroid/bootable/bootloader/uboot-imx/tools:$PATH

**编译uboot**

.. code:: shell

    $ cd ~/myandroid/bootable/bootloader/uboot-imx
    $ make distclean
    $ make mx6q_sabresd_android_config
    $ make

**编译kernel**

.. code:: shell

    $ cd ~/myandroid/kernel_imx
    $ make imx6_android_defconfig
    $ make uImage

**编译bootimg (uImagel和ramdisk)**

.. code:: shell

    $ cd ~/myandroid
    $ source build/envsetup.sh
    $ lunch sabresd_6dq-eng (此为调试版本，发布版本改成lunch sabresd_6dq-usr)
    $ make bootimage

**编译system**

.. code:: shell

    $ cd ~/myandroid
    $ source build/envsetup.sh
    $ lunch sabresd_6dq-eng (此为调试版本，发布版本改成lunch sabresd_6dq-usr)
    $ make