MYZR-SAMA5 Linux-3.18 编译手册
================================

文档说明
---------

系统环境说明
~~~~~~~~~~~~~

- 编译主机CPU架构：64位
- 编译主机系统：Linux
- Linux发行版：Ubuntu
- Ubuntu版本类型：服务器版
- Ubuntu版本号：12.04.5
- Ubuntu系统类型：x86-64

|  注意：开发主机请使用ubuntu 12.04.5 x86-64（桌面版或服务器版均可），使用其他发行版的Linux或Ubuntu的其它版本可能会遇到的不必要的问题。

操作说明
~~~~~~~~~

|  1）文档中以“$”开头的行，其后是Linux命令。
|  2）文档中所有的Linux命令建议手动输入到Linux主机执行（直接复制、粘贴到Linux主机上执行，可能会执行失败）。
|  3）文档中的Linux执行命令，如果空格后的下一个字符是“-”的（如：sudo apt-get –y install之类的），请手动输入到Linux主机执行（直接复制、粘贴到Linux主机上执行，通常会执行失败）。
|  4）文档中所有一行没写完的Linux命令请手动输入到Linux主机执行，（因为复制、粘贴命令不能包含类似“换行符”之类的特殊字符）。
|  5）按文档输入并执行Linux命令时注意观察命令的执行结果与文档图片中的是否一致，以确认命令是否输入有误及是否执行失败。
|  6）第一遍编译请严格按照文档进行，否则可能出现莫名其妙的错误。

截图说明
~~~~~~~~~

|  为使视图看起来简洁整齐，截图中的命令提示符统一使用myzr$。

图片中的Linux命令
~~~~~~~~~~~~~~~~~~

|  在文档的图片中观察“myzr$”开头的行可以直观的看到输入的Linux命令。

重要信息说明
~~~~~~~~~~~~~


**为避免各位客户在搭建开发环境及编译过程中遇到不必要的问题浪费时间和精力，推荐使用明远智睿发布的“vb43-u12045-serv-amd64”虚拟机系统。**

|  具体参见 《MYZR虚拟机系统指导》

安装并配置交叉编译工具链
------------------------

准备交叉编译工具链安装包
~~~~~~~~~~~~~~~~~~~~~~~~

|  1）下载交叉编译工具
|  交叉编译工具：gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.tar.xz
|  交叉编译工具配置文件：gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config
|  2）在虚拟机系统创建工具目录

.. code-block:: shell

   $ mkdir ~/my-sama5/03_tools -p

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_3.1.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_3.1.0.1.png

|  3）复制文件到虚拟机系统
|  把交叉编译工具和配置文件复制到 ~/my-sama5/03_tools
|  自己采取合适的方式完成。

安装交叉编译工具
~~~~~~~~~~~~~~~~~

|  1）进入交叉编译工具链目录

.. code-block:: shell

   $ cd ~/my-sama5/03_tools/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_3.2.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_3.2.0.1.png

|  2）解压（安装）交叉编译工具

.. code-block:: shell

   $ tar xf gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.tar.xz

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_3.2.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_3.2.0.2.png

|  3）检查安装
|  查看交叉编译工具链的版本信息以验证交叉编译工具链安装正常。

.. code-block:: shell

   $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config
   $ ${CROSS_COMPILE}gcc -v

|  执行命令后会出现类似如下的信息：

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_3.3.0.7.png
   :alt: MY-SAMA5_Linux-3.18_build_3.3.0.7.png

|  以及在最后一行会出现 gcc 版本相关的信息

.. code-block:: shell

   gcc version 4.9.3 20141031 (prerelease) (Linaro GCC 2014.11)

AT91Bootstrap编译
-------------------

准备源码
~~~~~~~~~

|  1）下载源码
|  文件名：at91bootstrap-3.7.2.tar.bz2
|  AT91Bootstrap 是二级引导装载程序，为Atmel AT91 SoC提供了一套算法来管理硬件初始化。如时钟速度配置，PIO设置，内存初始化，从指定的引导介质下载主应用程序到主内存并启动。
|  2）创建工作目录

.. code-block:: shell

   $ mkdir ~/my-sama5/02_source -p

|  3）将源码复制到工作目录
|  这一步自己采取合适的方式将AT91Bootstrap源码复制到“~/my-sama5/02_source”。也可以参照“2.3 常用功能演示”。
|  4）解压源码

- 进入工作目录

.. code-block:: shell

   $ cd ~/my-sama5/02_source/

- 执行解压命令

.. code-block:: shell

   $ tar jxf at91bootstrap-3.7.2.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.1.0.3.png
   :alt: MY-SAMA5_Linux-3.18_build_4.1.0.3.png

编译
~~~~~~

|  1）进入源码目录

.. code-block:: shell

   $ cd ~/my-sama5/02_source/at91bootstrap-3.7.2/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.1.png

|  2）使编译配置文件生效

.. code-block:: shell

   $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config

|  3）清除代码中可能存在的临时文件

.. code-block:: shell

   $ make mrproper

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.3.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.3.png

|  4）生成配置文件

.. code-block:: shell

   $ make mysama5ek200_defconfig

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.4.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.4.png

|  5）执行编译

.. code-block:: shell

   $ make -j4

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.5.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.5.png

|  6）编译完成

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.6.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.6.png

目标文件
~~~~~~~~~

|  1）目标文件
|  编译完成后会在源码的binaries目录下产生我们需要的目标文件。
|  通过ls命令可以看到，其中mysama5ek200-dataflashboot-uboot-3.7.2.bin 即是我们需要的文件。

.. code-block:: shell

   $ ls binaries/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.3.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_4.3.0.1.png

|  2）重命令目标文件
|  我们在烧录的时候需要使用到这些目标文件。为了烧录的方便，我们需要将目标文件修改为我们需要的文件名，即bootstrap-mysama5ek200.*。

.. code-block:: shell

   $ cd binaries/
   $ rename 's/mysama5ek200-dataflashboot-uboot-3.7.2/bootstrap-mysama5ek200/' *
   $ ls -1

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.3.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_4.3.0.2.png

|  3）保存目标文件
|  将bootstrap-mysama5ek200.* 保存。

u-boot编译
------------

准备源码
~~~~~~~~~

|  1）下载源码
|  文件名：u-boot-at91-linux4sam_4.7.tar.bz2
|  U-Boot在Atmel AT91 SoC上作为第三阶段引导加载程序。它负责配置主要接口，并引导Linux系统。
|  2）将源码复制到工作目录
|  这一步自己采取合适的方式将u-boot源码复制到“~/my-sama5/02_source”。也可以参照“2.3 常用功能演示”。
|  3）解压源码

- 进入工作目录

.. code-block:: shell

   $ cd ~/my-sama5/02_source/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.1.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_5.1.0.1.png

- 执行解压命令

.. code-block:: shell

   $ tar jxf u-boot-at91-linux4sam_4.7.tar.bz2

编译
~~~~~~

|  1）进入u-boot源码目录

.. code-block:: shell

   $ cd ~/my-sama5/02_source/u-boot-at91-linux4sam_4.7/

|  2）使编译配置文件生效

.. code-block:: shell

   $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config

|  3）清除代码中可能存在的临时文件

.. code-block:: shell

   $ make distclean

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.2.0.3.png
   :alt: MY-SAMA5_Linux-3.18_build_5.2.0.3.png

|  4）生成配置文件

.. code-block:: shell

   $ make mysama5ek200_defconfig

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.2.0.4.png
   :alt: MY-SAMA5_Linux-3.18_build_5.2.0.4.png

|  5）执行编译

.. code-block:: shell

   $ make -j4

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.2.0.5.png
   :alt: MY-SAMA5_Linux-3.18_build_5.2.0.5.png

|  6）编译完成

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.2.0.6.png
   :alt: MY-SAMA5_Linux-3.18_build_5.2.0.6.png

目标文件
~~~~~~~~~

|  编译完成后会在源码的目录下产生我们需要的目标文件。
|  通过ls命令可以看到。其中u-boot.bin 即是我们需要的文件。

.. code-block:: shell

   $ ls u-boot* -1

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.3.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_5.3.0.1.png

|  2）重命令目标文件
|  我们在烧录的时候需要使用到这些目标文件。为了烧录的方便，我们需要将目标文件修改为我们需要的文件名，即uboot-mysama5ek200.bin。

.. code-block:: shell

   $ mv u-boot.bin uboot-mysama5ek200.bin
   $ ls uboot-mysama5ek200.bin

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.3.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_5.3.0.2.png

|  3）保存目标文件
|  将uboot-mysama5ek200.bin 保存。

内核编译
---------

准备源码
~~~~~~~~~

|  1）下载源码
|  文件名：linux-at91-linux4sam_4.7.tar.bz2
|  2）将源码复制到工作目录
|  这一步自己采取合适的方式将内核源码复制到“~/my-sama5/02_source”。也可以参照“2.3 常用功能演示”。
|  3）解压源码

- 进入工作目录

.. code-block:: shell

   $ cd ~/my-sama5/02_source/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.1.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_6.1.0.1.png

- 执行解压命令

.. code-block:: shell

   $ tar jxf linux-at91-linux4sam_4.7.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.1.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_6.1.0.2.png

编译
~~~~~

|  1）进入内核源码目录

.. code-block:: shell

   $ cd ~/my-sama5/02_source/linux-at91-linux4sam_4.7/

|  2）使编译配置文件生效

.. code-block:: shell

   $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config

|  3）清除代码中可能存在的临时文件

.. code-block:: shell

   $ make distclean

**编译内核文件**

|  1）生成内核配置文件

.. code-block:: shell

   $ make ARCH=arm mysama5ek200_defconfig

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.1.1.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.1.1.png

|  2）执行内核文件编译命令

.. code-block:: shell

   $ make -j4 ARCH=arm zImage

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.1.2.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.1.2.png

|  3）内核文件编译完成

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.1.3.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.1.3.png

|  4）内核目标文件

.. code-block:: shell

   $ ls arch/arm/boot/zImage

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.1.4.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.1.4.png

**编译设备树文件**

|  1）执行设备树文件编译命令

.. code-block:: shell

   $ make ARCH=arm mysama5ek200-d36.dtb

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.2.1.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.2.1.png

|  2）设备树目标文件

.. code-block:: shell

   $ ls arch/arm/boot/dts/mysama5ek200-d36.dtb

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.2.2.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.2.2.png

**编译内核模块**

|  1）执行内核模块编译命令

.. code-block:: shell

   $ make ARCH=arm modules

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.1.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.1.png

|  2）内核模块编译完成

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.2.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.2.png

|  3）安装内核模块到指定目录

.. code-block:: shell

   $ make ARCH=arm modules_install INSTALL_MOD_PATH=./modules

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.3.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.3.png

|  4）打包内核模块

.. code-block:: shell

   $ tar cjf modules_mysama5ek200.tar.bz2 modules/*

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.4.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.4.png

|  5）模块包

.. code-block:: shell

   $ ls modules_mysama5ek200.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.5.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.5.png

文件系统编译
-------------

注意及说明
~~~~~~~~~~

|  a) 原始编译的过程中的下载量大约4G。（提示：可以使用我们下载好的一些文件，以减少下载量，节约时间，在7.4中会说到）。
|  b) 编译主机的网络连接最好使用能访问www.fackbook.com 的网络，不然可能会受到境内防火墙的限制而无法下载编译需要的软件包。
|  c) 初次编译需要的时间根据网络状态及编译主机的配置需要2小时到无限时间（经粗略统计除去下载时间，在16核CPU、16G内存的主机上编译QT5系统用了大约100分钟。）
|  客户请根据实际情况决定是否自行编译文件系统或使用我们提供的文件系统。

编译前的准备
~~~~~~~~~~~~

**准备Yocto编译环境**

|  说明，Yocto编译依赖一些软件包，所以需要在开发主机上进行安装。

.. code-block:: shell

   $ sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.1.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.1.1.png

.. code-block:: shell

   $ sudo apt-get install libsdl1.2-dev xterm sed cvs subversion coreutils texi2html docbook-utils python-pysqlite2 help2man make gcc g++ desktop-file-utils libgl1-mesa-dev libglu1-mesa-dev mercurial autoconf automake groff curl lzop asciidoc

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.1.2.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.1.2.png

.. code-block:: shell

    sudo apt-get install uboot-mkimage

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.1.3.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.1.3.png

**准备源码**

|  1）下载源码
|  源码包文件名：atmel_fido.tar.bz2
|  2）创建yocto工作目录

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.2.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.2.1.png

|  3）将源码复制到开发主机
|  这一步自己采取合适的方式将源码复制到yocto工作目录（即：/home/myzr/yocto）。也可以参照“2.3 常用功能演示”。
|  4）解压源码包

- 进入用户主目录

.. code-block:: shell

   $ cd ~/yocto

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.2.2.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.2.2.png

- 执行解压命令

.. code-block:: shell

   $ tar jxf atmel_fido.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.2.3.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.2.3.png

**准备软件包**

|  1）创建“/opt/yocto”目录用于存放软件包

.. code-block:: shell

   $ sudo mkdir /opt/yocto

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.3.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.3.1.png

.. code-block:: shell

   $ sudo chmod 777 /opt/yocto

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.3.2.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.3.2.png

|  2）下载软件包
|  在网盘中下载yocto的软件包。
|  软件包相对路径：yocto/downloads，将downloads下载到Windows。
|  3）将软件包复制到开发主机
|  将下载好的“downloads”目录复制到开发主机的“/opt/yocto”。

编译文件系统
~~~~~~~~~~~~~

|  编译前的配置
|  1）准备编译配置文件
|  文件目录：conf。下载conf目录到Windows。
|  2）进入poky目录

.. code-block:: shell

   $ cd ~/yocto/atmel_fido/poky/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.3.1.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.3.1.1.png

.. code-block:: shell

   $ source oe-init-build-env build-atmel

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.3.1.2.png
   :alt: MY-SAMA5_Linux-3.18_build_7.3.1.2.png

|  3）初始化编译目录

.. code-block:: shell

   $ source oe-init-build-env build-atmel

|  4）复制编译配置文件到编译目录
|  将 conf 目录复制到 /home/myzr/yocto/poky/build-atmel 。

**编译QT5文件系统**

.. code-block:: shell

   $ bitbake atmel-qt5-demo-image

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.3.2.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.3.2.1.png

|  提示：整个编译过程除去下载时间，在16核CPU、16G内存的主机上需要1小时左右。

- 目标文件

|  在./tmp/deploy/images/sama5d3xek/目录下可以找到我们编译生成的目标文件。

**编译QT5交叉编译工具**

.. code-block:: shell

   $ bitbake meta-toolchain-qt5

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.3.3.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.3.3.1.png

- 目标文件

|  在./tmp/deploy/images/sama5d3xek/目录下可以找到我们编译生成的目标文件。