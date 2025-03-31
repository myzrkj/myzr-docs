
MYZR-I.MX6-DEMO Android4.4.2环境搭建
=======================================

安装ubuntu12.04
----------------

|   在这里建议用户使用64bit的ubuntu12.04的操作系统，已经真机编译验证过。

安装JDK1.6 SE
--------------

|   登陆http://www.myzr.com.cn的下载专区，下载jdk-6u45-linux-x64.bin文件

.. code-block:: shell

    $ cd /usr
    $ sudo mkdir java
    $ cd java
    $ sudo cp ~ /jdk-6u45-linux-x64.bin ./
    $ sudo chmod 777 ./jdk-6u45-linux-x64.bin
    $ sudo ./jdk-6u45-linux-x64.bin
    $ sudo gedit /etc/profile

|   增加以下环境变量

.. code-block:: shell

    export JAVA_HOME=/usr/java/jdk1.6.0_45
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin
    $ source /etc/profile
    $ java –version

|   （看到版本为1.6.0_45就表示成功）

安装编译Android系统所需要的库
-----------------------------

|   (详细信息，请看网站[http://source.android.com/source/initializing.html])

.. code-block:: shell

    $ sudo apt-get install git gnupg flex bison gperf build-essential zip curl libc6-dev libncurses5-dev:i386 x11proto-core-dev libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-glx:i386 libgl1-mesa-dev g++-multilib mingw32 tofrodos python-markdown libxml2-utils xsltproc zlib1g-dev:i386
    $ sudo ln -s /usr/lib/i386-linux-gnu/mesa/libGL.so.1 /usr/lib/i386-linux-gnu/libGL.so
    $ sudo apt-get install uuid uuid-dev
    $ sudo apt-get install zlib1g-dev liblz-dev
    $ sudo apt-get install liblzo2-2 liblzo2-dev
    $ sudo add-apt-repository ppa:git-core/ppa
    $ sudo apt-get update
    $ sudo apt-get install git-core curl

下载源码并解压源码
------------------

下载源码
~~~~~~~~~

|   登陆http://www.myzr.com.cn=下载专区下载Android4.2源码
|   Android4.4的分卷压缩解压后的源码包：myzr_android-4.4.2_r1.tar.bz2

解压源码
~~~~~~~~~

.. code-block:: shell

    $ mkdir ~/myandroid
    $ cd ~
    $ tar -jxvf myzr_android-4.4.2_r1.tar.bz2 –C ~/myandroid

编译源码（Android系统）
~~~~~~~~~~~~~~~~~~~~~~~

**设置环境变量**

.. code-block:: shell

    $ export ARCH=arm
    $ export CROSS_COMPILE=~/myandroid/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi- $ export PATH=~/myandroid/bootable/bootloader/uboot-imx/tools:$PATH

**编译uboot**

.. code-block:: shell

    $ cd ~/myandroid/bootable/bootloader/uboot-imx
    $ make distclean
    $ make mx6q_sabresd_android_config (四核配置)
    或 $ make mx6dl_sabresd_android_config (双核简化配置)
    或 $ make mx6solo_sabresd_android_config (单核配置)
    $ make

**编译kernel**

.. code-block:: shell

    $ cd ~/myandroid/kernel_imx
    $ make imx6_android_defconfig
    $ make uImage

**编译bootimg (uImagel和ramdisk)**

.. code-block:: shell

    $ cd ~/myandroid
    $ source build/envsetup.sh
    $ lunch sabresd_6dq-user (此为发布版本，调试版本改成lunch sabresd_6dq-eng)
    $ make bootimage

**编译system**

.. code-block:: shell

    $ cd ~/myandroid
    $ source build/envsetup.sh
    $ lunch sabresd_6dq-user (此为发布版本，调试版本改成lunch sabresd_6dq-eng)
    $ make

|   注意：生成的u-boot.bin在~/myandroid/bootable/bootloader/uboot-imx目录下，boot.img和recovery.img和system.img在~/myandroid/out/target/product/sabresd_6dq目录下。