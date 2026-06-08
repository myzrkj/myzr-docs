
MYZR-IMX6 Android-4.4.2 Build Manual
======================================

Install ubuntu12.04
----------------------

|   If virtual machine downloaded from MYZR is going to be used,please skip to the section"download source code and decompress"
|   Here it is recommended to users to use operating system of 64bit ubuntu12.04 of which has been proven in compilation by real machine.


Install JDK1.6 SE
-------------------

|   Login in downloads of www.myzr.com.cn, to download jdk-6u45-linux-x64.bin

.. code-block:: shell

    $ cd /usr
    $ sudo mkdir java
    $ cd java
    $ sudo cp ~ /jdk-6u45-linux-x64.bin ./
    $ sudo chmod 777 ./jdk-6u45-linux-x64.bin
    $ sudo ./jdk-6u45-linux-x64.bin
    $ sudo gedit /etc/profile

|   Add the following environment variables

.. code-block:: shell

    export JAVA_HOME=/usr/java/jdk1.6.0_45
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin
    $ source /etc/profile
    $ java -version

|   (When version 1.6.0_45 is seen,which represent a success.)


Install libraries needed to compile Android system
------------------------------------------------------

|   For detailed information, please visit [http://source.android.com/source/initializing.html]

.. code-block:: shell

    For detailed information, please visit http://source.android.com/source/initializing.html
    $ sudo apt-get install git gnupg flex bison gperf build-essential zip curl libc6-dev libncurses5-dev:i386 x11proto-core-dev libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-glx:i386 libgl1-mesa-dev g++-multilib mingw32 tofrodos python-markdown libxml2-utils xsltproc zlib1g-dev:i386
    $ sudo ln -s /usr/lib/i386-linux-gnu/mesa/libGL.so.1 /usr/lib/i386-linux-gnu/libGL.so
    $ sudo apt-get install gcc:i386 linux-libc-dev:i386
    $ sudo apt-get install uuid uuid-dev
    $ sudo apt-get install zlib1g-dev liblz-dev
    $ sudo apt-get install liblzo2-2 liblzo2-dev
    $ sudo apt-get install uuid-dev:i386
    $ sudo apt-get install liblzo2-dev:i386
    $ sudo ln -sf /lib/i386-linux-gnu/libuuid.so.1 /usr/lib/libuuid.so

Download source code and decompress
--------------------------------------

Download source code
~~~~~~~~~~~~~~~~~~~~~~

|   Login downloads in http://www.myzr.com.cn to download source code of Android4.2
|   Android4.2 source code package：myzr_android4_2_2_1_1_0.tar.bz2

Decompress source code
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ mkdir ~/myandroid
    $ cd ~
    $ tar -jxvf myzr_android4_2_2_1_1_0.tar.bz2 -C ~/myandroid

Compile source code(Android system)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Set environment variables**

.. code-block:: shell

    $ export ARCH=arm
    $ export CROSS_COMPILE=~/myandroid/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi- $ export PATH=~/myandroid/bootable/bootloader/uboot-imx/tools:$PATH

**Compile uboot**

.. code-block:: shell

    $ cd ~/myandroid/bootable/bootloader/uboot-imx
    $ make distclean
    $ make mx6q_sabresd_android_config
    $ make

**Compile kernel**

.. code-block:: shell

    $ cd ~/myandroid/kernel_imx
    $ make imx6_android_defconfig
    $ make uImage

**Compile bootimg (uImagel and ramdisk)**

.. code-block:: shell

    $ cd ~/myandroid
    $ source build/envsetup.sh
    $ lunch sabresd_6dq-eng ( this is debug version,release version is changed to be lunch sabresd_6dq-usr)
    $ make bootimage

**Compile system**

.. code-block:: shell

    $ cd ~/myandroid
    $ source build/envsetup.sh
    $ lunch sabresd_6dq-eng ( this is debug version,release version is changed to be lunch sabresd_6dq-usr)
    $ make

|   Note: u-boot.bin generated is in the directory of ~/myandroid/bootable/bootloader/uboot-imx,boot.img and recovery.img and system.img are in the directory of ~/myandroid/out/target/product/sabresd_6dq