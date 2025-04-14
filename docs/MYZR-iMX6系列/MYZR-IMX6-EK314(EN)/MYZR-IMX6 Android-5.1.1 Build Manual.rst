MYZR-IMX6 Android-5.1.1 Build Manual
=======================================

Install ubuntu12.04
----------------------

|   (If virtual machine downloaded from MYZR is going to be used,please skip to the section"download source code and decompress")
|   Here it is recommended to users to use operating system of 64bit ubuntu12.04 of which has been proven in compilation by real machine.

Install openjdk1.7
---------------------

|   Execute command to install openjdk1.7

.. code-block:: shell

    $ sudo add-apt-repository "deb http://archive.canonical.com/lucid partner"
    $ sudo apt-get update
    $ sudo apt-get install openjdk-7-jdk
    $ sudo gedit /etc/profile

|   Add the following environment variables

.. code-block:: shell

    $ export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/
    $ export JRE_HOME=$JAVA_HOME/jre
    $ export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    $ export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin
    $ source /etc/profile
    $ java -version

|   (when version 1.6.0_45 is seen,which represent a success)


Install libraries needed to compile Android system
-----------------------------------------------------

|   (For detailed information, please visit "http://source.android.com/source/initializing.html")

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

Download source code and decompress
--------------------------------------

4.1 download source code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Login downloads in "http://www.myzr.com.cn" to download source code of Android5.1
|   The Android5.1.1 sub-volume compression decompressed source package: myzr_android-5.1.1.tar.bz2

Decompress source code
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ mkdir ~/myandroid5.1
    $ cd ~
    $ tar -jxvf myzr_android-5.1.1_r1.tar.bz2

Compile source code(Android system)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**set environment variables**

.. code-block:: shell

    $ export ARCH=arm
    $ export CROSS_COMPILE=~/myandroid5.1/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi-
    $ export PATH=~/myandroid5.1/bootable/bootloader/uboot-imx/tools:$PATH

**Compile uboot**

.. code-block:: shell

    $ cd ~/myandroid5.1/bootable/bootloader/uboot-imx
    $ make distclean
    $ make myimx6ek200-6q_android_defconfig (EK200-6Q-1G configuration)
    or $ make myimx6ek200-6q-2g_android_defconfig (EK200-6Q-2G configuration)
    or $ make myimx6ek200-6qp_android_defconfig (EK200-6QP-1 configuration)
    or $ make myimx6ek200-6s-1g_android_defconfig (EK200-6S-1G configuration)
    or $ make myimx6ek200-6u_android_defconfig (EK200-6U-1G configuration)
    or $ make myimx6ek314-6q-2g_android_defconfig (EK314-6Q-2G configuration)
    or $ make myimx6ek314-6q_android_defconfig (EK314-6Q-1G configuration)
    or $ make myimx6ek314-6u_android_defconfig (EK314-6U-2G configuration)
    $ make

**Compile kernetl**

.. code-block:: shell

    $ cd ~/myandroid5.1/kernel_imx
    $ cp myzr.config .config
    $ make uImage LOADADDR=0x10008000

**Compile bootimg (uImage and ramdisk)**

.. code-block:: shell

    $ cd ~/myandroid5.1
    $ source build/envsetup.sh
    $ lunch myimx6ek_6dq-user
    $ make bootimage

**Compile system**

.. code-block:: shell

    $ cd ~/myandroid5.1
    $ source build/envsetup.sh
    $ lunch myimx6ek_6dq-user
    $ make

|   Results as the following figures showed:

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/MY_I.MX6_DEMO_Android5.1.1_2.png
   :alt: MY_I.MX6_DEMO_Android5.1.1_2.png

|   Note:u-boot.imx generated is in the directory of ~/myandroid/bootable/bootloader/uboot-imx，boot.img and recovery.img and system.img are in the directory of ~/myandroid/out/target/product/myimx6ek_6dq

Start up the setting of environment variables
------------------------------------------------

Single screen display
~~~~~~~~~~~~~~~~~~~~~~~~~

**LVDS setting**

|   setenv bootargs console=ttymxc0,115200 init=/init video=mxcfb0:dev=ldb,bpp=32 video=mxcfb1:off video=mxcfb2:off video=mxcfb3:off vmalloc=256M
|   androidboot.console=ttymxc0 consoleblank=0 androidboot.hardware=freescale cma=384M(debug serial port can't be used).
|   setenv bootargs console=ttymxc0,115200 init=/init video=mxcfb0:dev=ldb,bpp=32
|
|   video=mxcfb1:off video=mxcfb2:off video=mxcfb3:off vmalloc=256M androidboot.console=ttymxc0 consoleblank=0 androidboot.hardware=freescale cma=384M
|   androidboot.selinux=disabled androidboot.dm_verity=disabled（debug serial port can be used）

**HDMI setting**

|   setenv bootargs console=ttymxc0,115200 androidboot.console=ttymxc0 consoleblank=0 vmalloc=256M init=/init video=mxcfb0:dev=hdmi,
|   1920x1080M@60,bpp=32 video=mxcfb1:off video=mxcfb2:off video=mxcfb3:off androidboot.hardware=freescale cma=384M(serial port can't be use)
|
|   setenv bootargs console=ttymxc0,115200 androidboot.console=ttymxc0 consoleblank=0 vmalloc=256M init=/init video=mxcfb0:dev=hdmi,
|   1920x1080M@60,bpp=32 video=mxcfb1:off video=mxcfb2:off video=mxcfb3:off androidboot.hardware=freescale cma=384M androidboot.selinux=disabled androidboot.dm_verity=disabled（serial port can be used）

Dual screen display
~~~~~~~~~~~~~~~~~~~~~~

**LVDS+HDMI setting**

|   setenv bootargs console=ttymxc0,115200 androidboot.console=ttymxc0 consoleblank=0 vmalloc=256M init=/init video=mxcfb0:dev=ldb,bpp=32 video=mxcfb1:dev=hdmi,
|   1920x1080M@60,bpp=32 video=mxcfb2:off video=mxcfb3:off androidboot.hardware=freescale cma=384M (serial port can't be used)
|
|   setenv bootargs console=ttymxc0,115200 androidboot.console=ttymxc0 consoleblank=0 vmalloc=256M init=/init video=mxcfb0:dev=ldb,bpp=32 video=mxcfb1:dev=hdmi,
|   1920x1080M@60,bpp=32 video=mxcfb2:off video=mxcfb3:off androidboot.hardware=freescale cma=384M androidboot.selinux=disabled androidboot.dm_verity=disabled （serial port can be used）