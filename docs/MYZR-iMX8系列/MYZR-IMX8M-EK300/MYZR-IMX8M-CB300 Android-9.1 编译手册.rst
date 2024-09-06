
MYZR-IMX8M-CB300 Android-9.1 编译手册
=======================================

安装ubuntu16.04
-----------------

|  (如果使用下载明远智睿的虚拟机，请直接跳到 下载源码并解压 这一节)
|  在这里建议用户使用64bit的ubuntu16.04的操作系统，已经真机编译验证过。

安装openjdk8
--------------

依赖包安装
~~~~~~~~~~~

.. code-block:: shell

   => sudo apt-get install uuid uuid-dev
   => sudo apt-get install zlib1g-dev liblz-dev
   => sudo apt-get install liblzo2-2 liblzo2-dev
   => sudo apt-get install lzop
   => sudo apt-get install git-core curl
   => sudo apt-get install u-boot-tools
   => sudo apt-get install mtd-utils
   => sudo apt-get install android-tools-fsutils
   => sudo apt-get install openjdk-8-jdk
   => sudo apt-get install device-tree-compiler
   => sudo apt-get install gdisk
   => sudo apt-get install m4
   => sudo apt-get install libz-dev

安装openjdk8
~~~~~~~~~~~~~~

.. code-block:: shell

   => sudo add-apt-repository ppa:openjdk-r/ppa
   => sudo apt-get update
   => sudo apt-get install openjdk-8-jdk

|  编辑用户目录下的.profile文件中添加下面内容

.. code-block:: shell

   => vim ~/.profile
   #在文件未尾添加下面内容
   export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
   export JRE_HOME=$JAVA_HOME/jre
   export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
   export PATH=$JAVA_HOME/bin:$PATH:$JRE_HOME/bin

|  重新加载.profile文件

.. code-block:: shell

   => source ~/.profile
   # 查看jdk版本，验证安装
   => java -version
   openjdk version "1.8.0_242"
   OpenJDK Runtime Environment (build 1.8.0_242-8u242-b08-0ubuntu3~16.04-b08)
   OpenJDK 64-Bit Server VM (build 25.242-b08, mixed mode)

下载源码并解压源码
-------------------

下载源码
~~~~~~~~~

|  到百度网盘MYZR-iMX8-201907/2.2_OS_Android9.1/02_Source目录下载
|  imx8mq_android9.tar.bz2*的所有压缩包

解压源码
~~~~~~~~~

.. code-block:: shell

   => cat imx8mq_android9.tar.bz2* | tar zvxf

修改源码
~~~~~~~~~

.. code-block:: shell

   vi ~/imx8mq-anroid9/imx8mq_android9/vendor/nxp-opensource/imx-mkimage/Makefile
   - @echo -n '#define MKIMAGE_COMMIT 0x2020' > src/build_info.h
   - @git rev-parse --short=8 HEAD >> src/build_info.h
   + @echo -n '#define MKIMAGE_COMMIT 0x2020' > src/build_info.h
   + #@git rev-parse --short=8 HEAD >> src/build_info.h

编译源码（Android系统）
------------------------

设置环境变量
~~~~~~~~~~~~~

.. code-block:: shell

   => export ANDROID_HOME=~/imx8mq_android9
   => export ARCH=arm64
   => export CROSS_COMPILE=~/imx8mq_android9/prebuilts/gcc/linuxx86/aarch64/aarch64-linux-android-4.9/bin/aarch64-linux-android-
   => source build/envsetup.sh
   => lunch evk_8mq-userdebug

编译system
~~~~~~~~~~~~

|  选择编译imx8mq-ek300

.. code-block:: shell

   => cd $ANDROID_HOME
   => vim device/fsl/imx8m/evk_8mq/BoardConfig.mk
   #修改下面的内容
   #TARGET_BOARD_DTS_CONFIG ?= imx8mq:myimx8mq-evk.dtb
   TARGET_BOARD_DTS_CONFIG += imx8mq:myimx8mq-ek300.dtb
   #TARGET_BOOTLOADER_CONFIG += imx8mq:myimx8mevk-8mq-android_defconfig
   #TARGET_BOOTLOADER_CONFIG += imx8mq-evk-uuu:myimx8mevk-8mq-android-uuu_defconfig
   #TARGET_BOOTLOADER_CONFIG += imx8mq:myimx8mevk-8mq-android-3G_defconfig
   #TARGET_BOOTLOADER_CONFIG += imx8mq-evk-uuu:myimx8mevk-8mq-android-3Guuu_defconfig
   #TARGET_BOOTLOADER_CONFIG += imx8mq:myimx8mevk-8mq-android-4G_defconfig
   #TARGET_BOOTLOADER_CONFIG += imx8mq-evk-uuu:myimx8mevk-8mq-android-4Guuu_defconfig
   TARGET_BOOTLOADER_CONFIG += imx8mq:myimx8mek300-8mq-android_defconfig
   TARGET_BOOTLOADER_CONFIG += imx8mq-evk-uuu:myimx8mek300-8mq-androiduuu_defconfig
   #TARGET_BOOTLOADER_CONFIG += imx8mq:myimx8mek300-8mq-android-3G_defconfig
   #TARGET_BOOTLOADER_CONFIG += imx8mq-evk-uuu:myimx8mek300-8mq-android-3Guuu_defconfig
   #TARGET_BOOTLOADER_CONFIG += imx8mq:myimx8mek300-8mq-android-4G_defconfig
   #TARGET_BOOTLOADER_CONFIG += imx8mq-evk-uuu:myimx8mek300-8mq-android-4Guuu_defconfig

|  开始编译

.. code-block:: shell

   => cd $ANDROID_HOME
   => make 2>&1 -j8 | tee build-log.txt

编译uboot
~~~~~~~~~~

.. code-block:: shell

   => cd $ANDROID_HOME
   => make bootloader -j8

编译kernel
~~~~~~~~~~~~

.. code-block:: shell

   => cd $ANDROID_HOME
   => cd vendor/nxp-opensource/kernel_imx
   => make myzr_android_defconfig
   => make KCFLAGS=-mno-android -j8

编译bootimage
~~~~~~~~~~~~~~

.. code-block:: shell

   => cd $ANDROID_HOME
   => make bootimage -j8

编译dtboimage
~~~~~~~~~~~~~~

|  myimx8mq-ek300 hdmi输出

.. code-block:: shell

   => cd $ANDROID_HOME
   => cd vendor/nxp-opensource/kernel_imx/arch/arm64/boot/dts/myzr
   => vim myimx8mq-ek300.dts
   /* touch */
   /*#include "myimx8mq-ftxx.dtsi"*/
   /*#include "myimx8mq-gt9xx.dtsi"*/
   /* dsi */
   #include "myimx8mq-hdmi.dtsi"
   /*#include "myimx8mq-dcss-hj1010.dtsi"*/
   /*#include "myimx8mq-dcss-khd156.dtsi"*/
   /*#include "myimx8mq-dcss-bi3103s.dtsi"*/

|  myimx8mq-ek300 mipi输出

.. code-block:: shell

   => cd $ANDROID_HOME
   => cd vendor/nxp-opensource/kernel_imx/arch/arm64/boot/dts/myzr
   => vim myimx8mq-ek300.dts
   /* touch */
   #include "myimx8mq-ftxx.dtsi"
   /*#include "myimx8mq-gt9xx.dtsi"*/
   /* dsi */
   /*#include "myimx8mq-hdmi.dtsi"*/
   #include "myimx8mq-dcss-hj1010.dtsi"
   /*#include "myimx8mq-dcss-khd156.dtsi"*/
   /*#include "myimx8mq-dcss-bi3103s.dtsi"*/

|  开始编译

.. code-block:: shell

   => cd $ANDROID_HOME
   => make dtboimage -j8

目标文件
---------

.. code-block:: shell

   => cd $ANDROID_HOME
   => cd out/target/product/evk_8mq
   # 下面是我们需要的文件
   # boot.img
   # dtbo-imx8mq.img
   # system.img
   # u-boot-imx8mq.imx
   # u-boot-imx8mq-evk-uuu.imx
   # vbmeta-imx8mq.img
   # vendor.img