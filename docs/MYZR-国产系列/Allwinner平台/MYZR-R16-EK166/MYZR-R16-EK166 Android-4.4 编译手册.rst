
MYZR-R16-EK166 Android-4.4 编译手册
=====================================

环境搭建
----------

安装ubuntu12.04
~~~~~~~~~~~~~~~~

| 在这里建议用户使用64bit的ubuntu12.04的操作系统，已经真机编译验证过。

安装JDK6
~~~~~~~~~

.. attention::
   注意，版本一定要是jdk6,其他版本都会有问题


| 下载jdk-6u45-linux-x64.bin文件并安装

.. code:: shell

   $ cd /usr
   $ sudo mkdir java
   $ cd java
   $ sudo cp ~ /jdk-6u45-linux-x64.bin ./
   $ sudo chmod 777 ./jdk-6u45-linux-x64.bin
   $ sudo ./jdk-6u45-linux-x64.bin

| 打开profile文件并添加环境变量

.. code:: shell
   
   $ sudo gedit /etc/profile
   export JAVA_HOME=/usr/java/jdk1.6.0_45
   export JRE_HOME=$JAVA_HOME/jre
   export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
   export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin
   $ source /etc/profile

| 查看jdk版本

.. code:: shell

   $ java -version

| java version "1.6.0_45"能看到版本为1.6.0_45就表示安装成功。

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android2-1.png
   :alt: MY-R16-CB166_Android2-1.png

安装编译Android系统需要的库
----------------------------

.. code:: shell

   sudo apt-get install git gnupg flex bison gperf build-essential \
   zip curl libc6-dev libncurses5-dev:i386 x11proto-core-dev \
   libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-glx:i386 \
   g++-multilib mingw32 tofrodos gcc-multilib ia32-libs \
   python-markdown libxml2-utils xsltproc zlib1g-dev:i386 \
   lzop libssl1.0.0 libssl-dev uboot-mkimage

下载源码并解压
----------------

| 下载android.tar.bz2.0 ，android.tar.bz2.1 ，android.tar.bz2.2三个文件。并用如下的命令解压

.. code:: shell

   $ cat android.tar.bz2.* | tar -jxv

| 解压完成后会有一个名叫R16的目录，目录里有一个android跟lichee目录。
| android目录是安卓系统源码，lichee目录放的uboot跟内核。

编译内核与Uboot
----------------

配置平台信息
~~~~~~~~~~~~

.. code:: shell

   $ cd ~/R16/android
   $ source build/envsetup.sh
   $ lunch astar_evb30-eng
   $ cd ~/R16/lichee/
   $ ./build.sh config

   Welcome to mkscript setup progress
   All available chips:
   0. sun8iw5p1
   Choice: 0
   All available platforms:
   0. android
   1. dragonboard
   2. linux
   3. tina
   Choice: 0
   All available kernel:
   0. linux-3.4
   Choice: 0
   All available boards:
   0. bell-one
   1. evb
   2. evb-20
   3. evb-30
   4. evb-rtl8723bs
   5. sc3813r
   Choice: 3

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android4-1.png
   :alt: MY-R16-CB166_Android4-1.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android4-2.png
   :alt: MY-R16-CB166_Android4-2.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android4-3.png
   :alt: MY-R16-CB166_Android4-3.png


编译内核
~~~~~~~~~

.. code:: shell

   $ cd ~/R16/lichee
   $ ./build.sh

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android4-4.png
   :alt: MY-R16-CB166_Android4-4.png


编译Uboot
~~~~~~~~~~~

.. code:: shell

   $ cd ~/R16/lichee/brandy/u-boot-2011.09/
   $ make distclean
   $ make sun8iw5p1_config
   $ make

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android4-5.png
   :alt: MY-R16-CB166_Android4-5.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android4-6.png
   :alt: MY-R16-CB166_Android4-6.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android4-7.png
   :alt: MY-R16-CB166_Android4-7.png


编译android系统
~~~~~~~~~~~~~~~~

.. code:: shell

   $ cd ~/R16/android/
   $ extract-bsp
   $ make

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android5-1.png
   :alt: MY-R16-CB166_Android5-1.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android5-2.png
   :alt: MY-R16-CB166_Android5-2.png


打包
~~~~~~

.. code:: shell

   $ cd ~/R16/android
   $ pack

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_Android5-2.png
   :alt: MY-R16-CB166_Android5-2.png

| 打包的最终文件在~/R16/lichee/tools/pack下的sun8iw5p1_android_evb-30_uart0.img
| 将该文件复制到电脑上就可以烧写到开发板上。烧写请参考《R16烧录手册》。


::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2023/5/08  
   * Supporter: Zhong JiaYi
   --------------------------------------------------------------------------------