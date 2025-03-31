
MYZR-I.MX6-DEMO Android5.1.1环境搭建
=======================================

安装ubuntu12.04
-----------------

|   在这里建议用户使用64bit的ubuntu12.04的操作系统，已经真机编译验证过。

安装openjdk1.7
----------------

|   运行一下命令安装openjdk1.7

.. code-block:: shell

    sudo add-apt-repository "deb http://archive.canonical.com/ lucid partner"
    sudo apt-get update
    sudo apt-get install openjdk-7-jdk
    $ sudo gedit /etc/profile

|   `Link text <http://archive.canonical.com/>`_

|   增加以下环境变量

.. code-block:: shell

    export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin
    $ source /etc/profile
    $ java –version

|   （看到版本为1.7.0_101就表示成功）

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY_I.MX6_DEMO_Android5.1.1_1.png
   :alt: MY_I.MX6_DEMO_Android5.1.1_1.png

安装编译Android系统所需要的库
-----------------------------

|   (详细信息，请看网站 `http://source.android.com/source/initializing.html <http://source.android.com/source/initializing.html/>`_ )

.. code-block:: shell

    $ sudo apt-get install git gnupg flex bison gperf build-essential zip curl libc6-dev libncurses5-dev:i386 x11proto-core-dev libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-glx:i386 libgl1-mesa-dev g++-multilib mingw32 tofrodos python-markdown libxml2-utils xsltproc zlib1g-dev:i386
    $ sudo ln -s /usr/lib/i386-linux-gnu/mesa/libGL.so.1 /usr/lib/i386-linux-gnu/libGL.so
    $ sudo apt-get install uuid uuid-dev
    $ sudo apt-get install zlib1g-dev liblz-dev
    $ sudo apt-get install liblzo2-2 liblzo2-dev
    $ sudo apt-get install lzop
    $ sudo apt-get install git-core curl
    $ sudo apt-get install u-boot-tools
    $ sudo apt-get install mtd-utils
    $ sudo apt-get install android-tools-fsutils

下载源码并解压源码
------------------

4.1下载源码
~~~~~~~~~~~~

|   登陆 `http://www.myzr.com.cn <http://www.myzr.com.cn/>`_ 下载专区下载Android5.1源码

|   Android5.1.1的分卷压缩解压后的源码包：myzr_android-5.1.1.tar.bz2

解压源码
~~~~~~~~~

.. code-block:: shell

    $ mkdir ~/myandroid5.1
    $ cd ~
    $ tar -jxvf myzr_android-5.1.1_r1.tar.bz2

编译源码（Android系统）
~~~~~~~~~~~~~~~~~~~~~~~~

**设置环境变量**

.. code-block:: shell

    $ export ARCH=arm
    $ export CROSS_COMPILE=~/myandroid5.1/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi-
    $ export PATH=~/myandroid5.1/bootable/bootloader/uboot-imx/tools:$PATH

**编译uboot**

.. code-block:: shell

    $ cd ~/myandroid5.1/bootable/bootloader/uboot-imx
    $ make distclean
    $ make myimx6ek200-6q_android_defconfig (EK200-6Q-1G配置)
    或 $ make myimx6ek200-6q-2g_android_defconfig (EK200-6Q-2G配置)
    或 $ make myimx6ek200-6qp_android_defconfig (EK200-6QP-1G配置)
    或 $ make myimx6ek200-6s-1g_android_defconfig (EK200-6S-1G配置)
    或 $ make myimx6ek200-6u_android_defconfig (EK200-6U-1G配置)
    或 $ make myimx6ek314-6q-2g_android_defconfig (EK314-6Q-2G配置)
    或 $ make myimx6ek314-6q_android_defconfig (EK314-6Q-1G配置)
    或 $ make myimx6ek314-6u_android_defconfig (EK314-6U-2G配置)
    $ make

**编译kernel**

.. code-block:: shell

    $ cd ~/myandroid5.1/kernel_imx
    $ cp myzr.config .config
    $ make uImage LOADADDR=0x10008000

**编译bootimg (uImage和ramdisk)**

.. code-block:: shell

    $ cd ~/myandroid5.1
    $ source build/envsetup.sh
    $ lunch myimx6ek_6dq-user
    $ make bootimage

**编译system**

.. code-block:: shell

    $ cd ~/myandroid5.1
    $ source build/envsetup.sh
    $ lunch myimx6ek_6dq-user
    $ make

|   结果如下图所示：

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY_I.MX6_DEMO_Android5.1.1_2.png
   :alt: MY_I.MX6_DEMO_Android5.1.1_2.png

|   注意：生成的u-boot.imx在~/myandroid/bootable/bootloader/uboot-imx目录下，boot.img和recovery.img和system.img在~/myandroid/out/target/product/myimx6ek_6dq目录下。

启动环境变量设置
----------------

单屏显示
~~~~~~~~~

**LVDS设置**

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 init=/init video=mxcfb0:dev=ldb,bpp=32 video=mxcfb1:off video=mxcfb2:off video=mxcfb3:off vmalloc=256M androidboot.console=ttymxc0 consoleblank=0 androidboot.hardware=freescale cma=384M(不能用调试串口)
    setenv bootargs console=ttymxc0,115200 init=/init video=mxcfb0:dev=ldb,bpp=32
    video=mxcfb1:off video=mxcfb2:off video=mxcfb3:off vmalloc=256M androidboot.console=ttymxc0 consoleblank=0 androidboot.hardware=freescale cma=384M androidboot.selinux=disabled androidboot.dm_verity=disabled（可以用调试串口）

**HDMI设置**

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 androidboot.console=ttymxc0 consoleblank=0 vmalloc=256M init=/init video=mxcfb0:dev=hdmi,1920x1080M@60,bpp=32 video=mxcfb1:off video=mxcfb2:off video=mxcfb3:off androidboot.hardware=freescale cma=384M
    (不能用调试串口)
    setenv bootargs console=ttymxc0,115200 androidboot.console=ttymxc0 consoleblank=0 vmalloc=256M init=/init video=mxcfb0:dev=hdmi,1920x1080M@60,bpp=32 video=mxcfb1:off video=mxcfb2:off video=mxcfb3:off androidboot.hardware=freescale cma=384M
    androidboot.selinux=disabled androidboot.dm_verity=disabled（可以用调试串口）

双屏显示
~~~~~~~~~

**LVDS+HDMI设置**

.. code-block:: shell

    setenv bootargs console=ttymxc0,115200 androidboot.console=ttymxc0 consoleblank=0 vmalloc=256M init=/init video=mxcfb0:dev=ldb,bpp=32 video=mxcfb1:dev=hdmi,
    1920x1080M@60,bpp=32 video=mxcfb2:off video=mxcfb3:off androidboot.hardware=freescale cma=384M (不能用调试串口)
    setenv bootargs console=ttymxc0,115200 androidboot.console=ttymxc0 consoleblank=0 vmalloc=256M init=/init video=mxcfb0:dev=ldb,bpp=32 video=mxcfb1:dev=hdmi,1920x1080M@60,bpp=32 video=mxcfb2:off video=mxcfb3:off androidboot.hardware=freescale cma=384M androidboot.selinux=disabled androidboot.dm_verity=disabled （可以用调试串口）