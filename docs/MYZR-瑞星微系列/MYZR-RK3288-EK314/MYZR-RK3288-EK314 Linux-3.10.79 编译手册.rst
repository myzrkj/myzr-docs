Linux-3.10.79 编译手册
========================

**主机环境**

|   ubuntu14.04(64bit),已经真机编译验证过。


准备源码包
------------

3.10.79版本代码
~~~~~~~~~~~~~~~~

**u-boot源码**

- | 文件名

 | rk32-myzr_uboot_2014.10_201803028.tar.bz2

**kernel源码**

- | 文件名

 | rk32-myzr_kernel_3.10_201803028.tar.bz2

**交叉编译工具**

- | 文件名

 | gcc-arm-eabi-4.6.tar.bz2

配置编译环境
-------------

准备源码
~~~~~~~~~~

**准备源码包**

|   1）创建工作目录
|   创建 ~/my-rk3288 作为工作目录

.. code-block:: shell

    $ mkdir ~/my-rk3288

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.1.1.1.jpg
   :alt: My-rk32-ek314build_2.1.1.1.jpg

|   创建 ~/my-rk3288/02_source 作为源码目录

.. code-block:: shell

    $ mkdir ~/my-rk3288/02_source

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.1.1.2.jpg
   :alt: My-rk32-ek314build_2.1.1.2.jpg

|   创建 ~/my-rk3288/03_tools 作为工具目录

.. code-block:: shell
    
    $ mkdir ~/my-rk3288/03_tools

|   2）复制源码包到开发主机中
|   这一步骤自己采取相应的方式进行。

|  说明：这里将网盘中“02_源码”复制到Linux开发主机的“~/my-rk3288/02_source”，将网盘中“03_工具”复制到Linux开发主机的“~/my-rk3288/03_tools”,将网盘中“01_应用”复制到Linux开发主机的“~/my-rk3288/01_application”。


**解压源码包**

|   1）解压u-boot源码和内核源码

.. code-block:: shell

    $ cd ~/my-rk3288/02_source
    $ tar jxf rk32-myzr_uboot_2014.10_201803028.tar.bz2
    $ tar jxf rk32-myzr_kernel_3.10_201803028.tar.bz2

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.1.2.1.jpg
   :alt: My-rk32-ek314build_2.1.2.1.jpg

|   2）解压交叉编译工具

.. code-block:: shell

    $ cd ~/my-rk3288/03_tools/
    $ tar jxf gcc-arm-eabi-4.6.tar.bz2

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.1.2.2.jpg
   :alt: MMy-rk32-ek314build_2.1.2.2.jpg

开发环境配置
~~~~~~~~~~~~~

**安装需要的包**

|   1）更新源列表

.. code-block:: shell

    $ sudo apt-get update

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.1.jpg
   :alt: My-rk32-ek314build_2.2.1.1.jpg

|   更新完成后如下图所示：

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.2.jpg
   :alt: My-rk32-ek314build_2.2.1.2.jpg

|   2）安装aptitude包管理工具和ia32-libs

|  如果编译主机的Linux是32位的，可以跳过此步骤。

- 安装aptitude包管理工具

.. code-block:: shell

   $ sudo apt-get -y install aptitude

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.3.jpg
   :alt: My-rk32-ek314build_2.2.1.3.jpg

- 使用aptitude安装ia32-libs

.. code-block:: shell

   $ sudo aptitude -y install ia32-libs

|  下图为安装过aptitude和ia32-libs后，再次执行安装命令的截图。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.4.jpg
   :alt: My-rk32-ek314build_2.2.1.4.jpg


|   3）安装mkimage工具

.. code-block:: shell

   $ sudo apt-get -y install uboot-mkimage

|  下图为安装过mkimage工具后，再次执行安装命令的截图。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.5.jpg
   :alt: My-rk32-ek314build_2.2.1.5.jpg

|   4）安装ncurses-dev
|   说明：make menuconfig对其具有依赖性质。

.. code-block:: shell

   $ sudo aptitude -y install ncurses-dev

|  下图为安装过ncurses-dev工具后，再次执行安装命令的截图。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.6.jpg
   :alt: My-rk32-ek314build_2.2.1.6.jpg

编译u-boot
------------

进入u-boot源码目录
~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ cd ~/my-rk3288/02_source/rk32-myzr_uboot_2014.10/

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.1.1.jpg
   :alt: My-rk32-ek314build_3.1.1.jpg

使配置文件生效
~~~~~~~~~~~~~~~

- 执行source命令

.. code-block:: shell

   $ source ~/my-rk3288/03_tools/gcc-arm-eabi-4.6-env

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.2.1.jpg
   :alt: My-rk32-ek314build_3.2.1.jpg

- 查看编译配置

.. code-block:: shell

   $ echo $ARCH
   $ echo $CROSS_COMPILE

|  可看到ARCH和CROSS_COMPILE被设置

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.2.2.jpg
   :alt: My-rk32-ek314build_3.2.2.jpg

- 验证交叉编译工具配置

.. code-block:: shell
   
   $ ${CROSS_COMPILE}gcc -v

|  执行命令后可以看到终端显示出交叉编译工具的版本信息。如下图：

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.2.3.jpg
   :alt: My-rk32-ek314build_3.2.3.jpg


清除u-boot配置
~~~~~~~~~~~~~~~

.. code-block:: shell

   $ make distclean

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.3.1.jpg
   :alt: My-rk32-ek314build_3.3.1.jpg


u-boot配置
~~~~~~~~~~~~

- 评估板及对应的 u-boot 编译配置：

+-------------------+--------------------+------------------+
|   评估板主型号    |  CPU类型-内存容量  | 对应的u-boot配置 |
+===================+====================+==================+
| MYZR-RK3288-EK314 | RK3288（四核）- 2G | rk3288_defconfig |
+-------------------+--------------------+------------------+

- MYZR-RK3288-EK314-2G配置示例：

.. code-block:: shell

    $ make rk3288_defconfig


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.4.1.jpg
   :alt: My-rk32-ek314build_3.4.1.jpg

编译
~~~~~~

- 执行编译

.. code-block:: shell

    $ make

|  这里为了提高编译速度，在make后面加了“-j4”。这里编译的Linux主机是双核4线程的，所以“-j”后面用了4，也就是采用4线程编译。“-j”后面的数字可以根据系统资源分配，但是不应该超过编译主机最大支持的线程数。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.5.1.jpg
   :alt: My-rk32-ek314build_3.5.1.jpg

- 编译完成

|  u-boot编译过程大概需要十几秒钟的时间。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.5.2.jpg
   :alt: My-rk32-ek314build_3.5.2.jpg

目标文件
~~~~~~~~~

|   编译完成后通过ls命令即可看到编译得到的目标文件RK3288UbootLoader_V2.30.10.bin

.. code-block:: shell

    $ ls

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.6.1.jpg
   :alt: My-rk32-ek314build_3.6.1.jpg

编译内核
---------

进入内核源码目录
~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ cd ~/my-rk3288/02_source/rk32-myzr_kernel_3.10/

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.1.1.jpg
   :alt: My-rk32-ek314build_4.1.1.jpg


使配置文件生效
~~~~~~~~~~~~~~~

- 执行source命令

.. code-block:: shell

    $ source ~/my-rk3288/03_tools/gcc-arm-eabi-4.6-env

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.2.1.jpg
   :alt: My-rk32-ek314build_4.2.1.jpg

- 查看编译配置

.. code-block:: shell

    $ echo $ARCH
    $ echo $CROSS_COMPILE

|  可看到ARCH和CROSS_COMPILE被设置

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.2.2.jpg
   :alt: My-rk32-ek314build_4.2.2.jpg

- 验证交叉编译工具配置

.. code-block:: shell

    $ ${CROSS_COMPILE}gcc -v

|  执行命令后可以看到终端显示出交叉编译工具的版本信息。如下图：

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.2.3.jpg
   :alt: My-rk32-ek314build_4.2.3.jpg

准备配置内核
~~~~~~~~~~~~~

- 清除内核配置

.. code-block:: shell

    $ make distclean

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.3.1.jpg
   :alt: My-rk32-ek314build_4.3.1.jpg

- 生成.config文件

|  备注：MYZR-RK3288-EK314系列评估板使用的配置文件是rk3288-myzr-linux_defconfig

.. code-block:: shell

    $ make rk3288-myzr-linux_defconfig


.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.3.2.jpg
   :alt: My-rk32-ek314build_4.3.2.jpg

编译内核zImage和设备树dtb
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------+-----------------+----------------------------------+
|   评估板主型号    |   显示屏类型    |         对应的设备树配置         |
+===================+=================+==================================+
| MYZR-RK3288-EK314 | LVDS(1024X600)  | rk3288-myzr_rh568_lvds_linux.img |
+                   +-----------------+----------------------------------+
|                   | HDMI(1920X1080) | rk3288-myzr_rh568_hdmi_linux.img |
+                   +-----------------+----------------------------------+
|                   | EDP(1920X1080)  | rk3288-myzr_rh568_edp_linux.img  |
+-------------------+-----------------+----------------------------------+

- 编译（以下是LVDS屏）

.. code-block:: shell

    $ make -j8 rk3288-myzr_rh568_lvds_linux.img

|  截图中使用了8线程编译。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.4.1.jpg
   :alt: My-rk32-ek314build_4.4.1.jpg

- 编译完成

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.4.2.jpg
   :alt: My-rk32-ek314build_4.4.2.jpg

- 目标文件

|   arch/arm/boot/uImage即为编译得到的目标文件，使用ls命令可查看文件信息。

.. code-block:: shell

    $ ls arch/arm/boot/zImage -la

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.4.3.jpg
   :alt: My-rk32-ek314build_4.4.3.jpg

编译模块
~~~~~~~~~~

- 编译

.. code-block:: shell

    $ make modules

|  截图中使用了4线程编译。

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.5.1.jpg
   :alt: My-rk32-ek314build_4.5.1.jpg

- 编译完成

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.5.2.jpg
   :alt: My-rk32-ek314build_4.5.2.jpg

- 目标文件

|   编译完成后各模块的.ko文件位于代码所在的目录，通过find命令可以找出编译完成的模块，参考命令如下：

.. code-block:: shell

    $ find -name *.ko

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.5.3.jpg
   :alt: My-rk32-ek314build_4.5.3.jpg

打包linux-boot.img
--------------------

编译rockchip-mkbootimg
~~~~~~~~~~~~~~~~~~~~~~~~

|   1) 创建应用程序目录

.. code-block:: shell

    $ mkdir ~/my-rk3288/01_application
    $ cd ~/my-rk3288/01_application

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.1.1.jpg
   :alt: My-rk32-ek314build_5.1.1.jpg

|   2) 解压和编译rockchip-mkbootimg

.. code-block:: shell

    $ tar jxf rockchip-mkbootimg.tar.bz2
    $ cd rockchip-mkbootimg/
    $ make && sudo make install

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.1.2.jpg
   :alt: My-rk32-ek314build_5.1.2.jpg


打包initrd.img
~~~~~~~~~~~~~~~~~

|   1) 压缩为img格式

.. code-block:: shell

    $ cd ~/my-rk3288/01_application/
    $ tar jxf initrd.tar.bz2
    $ make -C initrd/

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.2.1.jpg
   :alt: My-rk32-ek314build_5.2.1.jpg

|   2) 显示结果

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.2.2.jpg
   :alt: My-rk32-ek314build_5.2.2.jpg


打包linux-boot.img
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ mkbootimg --kernel ../02_source/rk32-myzr_kernel_3.10/arch/arm/boot/zImage --ramdisk initrd.img \ 
    --second ../02_source/rk32-myzr_kernel_3.10/resource.img -o linux-boot.img

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.3.1.jpg
   :alt: My-rk32-ek314build_5.3.1.jpg


文件系统
~~~~~~~~~

|   文件系统包位于网盘对应的镜像文件夹中。支持的文件系统类型及下载方式可参照《MYZR-RK3288-EK314 烧录手册》。


打包批量文件relase_update.img
-------------------------------

编译打包工具
~~~~~~~~~~~~~

.. code-block:: shell

    $ cd ~/my-rk3288/01_application
    $ tar jxf rk2918_tools.tar.bz2
    $ cd rk2918_tools/
    $ make -j4
    $ sudo cp afptool img_unpack img_maker mkkrnlimg /usr/local/bin/

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_7.1.1.jpg
   :alt: My-rk32-ek314build_7.1.1.jpg


新建文件夹和复制镜像
~~~~~~~~~~~~~~~~~~~~

|   test/Image/的文件对应烧写工具Image\linux文件，rk3288box-3.10-uboot-ubuntu.parameter.txt重命名为parameter，RESERVED是空文件，RK3288UbootLoader_V2.30.10.bin对应RKLoader.bin，update-script和recover-script在烧写工具复制，package-file的内容重新按对应的文件重命名，如下：

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_7.2.1.jpg
   :alt: My-rk32-ek314build_7.2.1.jpg

.. code-block:: shell

    $ mkdir ~/my-rk3288/04_rootfs/
    $ cd ~/my-rk3288/04_rootfs/
    $ mkdir -p ubuntu/Image
    $ cp test/Image/* ubuntu/Image/
    $ cp ubuntu/Image/RKLoader.bin ubuntu/
    $ cd ubuntu/

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_7.2.2.jpg
   :alt: My-rk32-ek314build_7.2.2.jpg


打包relase_update.img文件
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ cd Image/
    $ afptool -pack . ../update.img
    $ cd ..
    $ img_maker -rk32 RKLoader.bin update.img relase_update.img

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314build_7.3.1.jpg
   :alt: My-rk32-ek314build_7.3.1.jpg