Android-5.1 编译手册
======================

安装ubuntu12.04
----------------

|   (如果使用下载明远智睿的虚拟机，请直接跳到 下载源码并解压 这一节)
|   在这里建议用户使用64bit的ubuntu12.04的操作系统，已经真机编译验证过。

安装openjdk1.7
----------------

|   运行一下命令安装openjdk1.7

.. code-block:: shell

    sudo add-apt-repository "deb http://archive.canonical.com/ lucid partner"
    sudo apt-get update
    sudo apt-get install openjdk-7-jdk
    sudo gedit /etc/profile

|   增加以下环境变量

.. code-block:: shell

    export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/
    export JRE_HOME=$JAVA_HOME/jre
    export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
    export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin
    $ source /etc/profile
    $ java –version

|   （看到版本为1.7.0_121就表示成功）

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_2.1.1.png
   :alt: My-rk32-ek314_android_2.1.1.png


安装编译Android系统所需要的库
------------------------------

|   (详细信息，请看网站http://source.android.com/source/initializing.html)

.. code-block:: shell

    sudo apt-get install git gnupg flex bison gperf build-essential \ 
     zip curl libc6-dev libncurses5-dev:i386 x11proto-core-dev \ 
     libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-glx:i386 \ 
     g++-multilib mingw32 tofrodos gcc-multilib ia32-libs \ 
     python-markdown libxml2-utils xsltproc zlib1g-dev:i386 \ 
     lzop libssl1.0.0 libssl-dev

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_3.1.1.png
   :alt: My-rk32-ek314_android_3.1.1.png

下载源码并解压源码
------------------

下载源码
~~~~~~~~~

|   登陆http://www.myzr.com.cn下载专区下载Android5.1源码
|   Android5.1.1的分卷压缩解压后的源码包：rk32-myzr_android5.1_20180328.tar.bz2

解压源码
~~~~~~~~~

.. code-block:: shell

    $ mkdir ~/rk3288-myzr
    $ tar jxvf rk32-myzr_android5.1_20180328.tar.bz2 -C ~/rk3288-myzr/


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_5.1.1.png
   :alt: My-rk32-ek314_android_5.1.1.png


编译源码（Android系统）
------------------------

设置环境变量
~~~~~~~~~~~~~

.. code-block:: shell

    $ export ARCH=arm
    $ export CROSS_COMPILE=~/rk3288-myzr/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi-

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.1.1.png
   :alt: My-rk32-ek314_android_6.1.1.png

.. code-block:: shell

    $ ${CROSS_COMPILE}gcc -v

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.1.2.png
   :alt: My-rk32-ek314_android_6.1.2.png

编译uboot
~~~~~~~~~~

- 进入U-BOOT代码目录

.. code-block:: shell

    $ cd ~/rk3288-myzr/u-boot/

- 设置配置文件

.. code-block:: shell

    $ make rk3288_defconfig

- 编译

.. code-block:: shell

    $ make

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.2.1.png
   :alt: My-rk32-ek314_android_6.2.1.png

- 目标文件

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.2.2.png
   :alt: My-rk32-ek314_android_6.2.2.png

编译kernel
~~~~~~~~~~~

|   不同的显示屏类型对于不同的镜像，在下表中列出。

+-------------------+-----------------+----------------------------+
|    评估板型号     |       LCD       |            配置            |
+===================+=================+============================+
| MYZR-RK3288-EK314 | LVDS(1024X600)  | rk3288-myzr_rh568_lvds.img |
+                   +-----------------+----------------------------+
|                   | HDMI(1920X1080) | rk3288-myzr_rh568_hdmi.img |
+                   +-----------------+----------------------------+
|                   | EDP(1920X1080)  | rk3288-myzr_rh568_edp.img  |
+-------------------+-----------------+----------------------------+

- 进入内核代码目录

.. code-block:: shell

    $ cd ~/rk3288-myzr/kernel/

- 清除内核配置

.. code-block:: shell

    $ make distclean

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.3.1.png
   :alt: My-rk32-ek314_android_6.3.1.png

- 设置配置文件

.. code-block:: shell

    $ make rk3288-myzr_defconfig

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.3.2.png
   :alt: My-rk32-ek314_android_6.3.2.png

- 编译(以LVDS为例)

.. code-block:: shell

    $ make -j8 rk3288-myzr_rh568_lvds.img

|   说明：截图中使用了8线程编译。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.3.3.png
   :alt: My-rk32-ek314_android_6.3.3.png

- 编译完成

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.3.4.png
   :alt: My-rk32-ek314_android_6.3.4.png

- 目标文件

|   kernel.img和resource.img即为编译得到的目标文件，使用ls命令可查看文件信息。

.. code-block:: shell

    $ ls

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.3.5.png
   :alt: My-rk32-ek314_android_6.3.5.png


编译android源码
-----------------

- 设置android环境变量

.. code-block:: shell

    $ cd ~/rk3288-myzr/
    $ source build.sh

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.4.1.png
   :alt: My-rk32-ek314_android_6.4.1.png

- 设置android版本配置

.. code-block:: shell

    $ lunch rk3288_box-userdebug

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.4.2.png
   :alt: My-rk32-ek314_android_6.4.2.png

- 编译

.. code-block:: shell

    $ make -j16

|   说明：截图中使用了16线程编译。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.4.3.png
   :alt: My-rk32-ek314_android_6.4.3.png

- 编译完成

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.4.4.png
   :alt: My-rk32-ek314_android_6.4.4.png


- 目标文件

|   boot.img，misc.img，kernel.img，resource.img，recovery.img，system.img即为编译得到的目标文件，使用ls命令可查看文件信息。

.. code-block:: shell

    $ ./mkimage.sh
    $ ls rockdev/Image-rk3288_box/

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_6.4.5.png
   :alt: My-rk32-ek314_android_6.4.5.png


打包批量文件relase_android_update.img
---------------------------------------

编译打包工具
~~~~~~~~~~~~~

|   注意：如果编译了rk2918_tools.tar.bz2，就不需要重新编译了，可以跳过这个步骤。
|   默认复制rk2918_tools.tar.bz2到目录~/rk3288-myzr/rockdev下

.. code-block:: shell

    $ cd ~/rk3288-myzr/rockdev
    $ tar jxf rk2918_tools.tar.bz2
    $ cd rk2918_tools/
    $ make -j4
    $ sudo cp afptool img_unpack img_maker mkkrnlimg /usr/local/bin/


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_7.1.1.jpg
   :alt: My-rk32-ek314build_7.1.1.jpg


新建文件夹和复制镜像
~~~~~~~~~~~~~~~~~~~~

|   rockdev/Image-rk3288_box/的文件对应烧写工具Image\android文件夹中，rk3288box-3.10-uboot-ubuntu.parameter.txt重命名为parameter，RK3288UbootLoader_V2.30.10.bin对应RKLoader.bin，update-script和recover-script在烧写工具里面复制。package-file的内容重新按对应的文件重命名，如下：

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_7.1.1.png
   :alt: My-rk32-ek314_android_7.1.1.png

.. code-block:: shell

    $ mkdir -p rockdev/android/Image
    $ cd rockdev/android/Image/
    $ cp ~/rk3288-myzr/rockdev/Image-rk3288_box/* ./
    $ rm pc*
    $ $ ls

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_7.1.2.png
   :alt: My-rk32-ek314_android_7.1.2.png

打包relase_android_update.img文件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ afptool -pack . ../update.img
    $ img_maker -rk32 RKLoader.bin update.img relase_android_update.img

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_android_7.1.3.png
   :alt: My-rk32-ek314_android_7.1.3.png