
MYZR-RZG-EK200编译参考手册
===========================

交叉编译
---------

|  当我们想要编译源码或者编译自己修改的源码时，首先要做的第一步就是配置对应的交叉编译工具。对于本套源码我们是使用瑞萨官方yocto编译的SDK为基础进行编译。

SDK下载和安装
~~~~~~~~~~~~~~

**下载**

|  SDK安转包在MYZR-RZ - > 03_SDK目录下，我们一般使用 **poky-glibc-x86_64-core-image-qt-aarch64-smarc-rzg2l-toolchain-3.1.17.sh** 来进行安装。
|  我们可以在主机中创建一个rz专属的目录来存放相关的源码，编译工具和以后用到的一些东西。如我创建的目录为：/home/myzr/my-work/renesas，在此目录下我又创建了4个子目录：

.. code:: shell

   $ ls
   01_image  02_sources  03_sdk  04_app

|  01目录可以用来放置我们编译好的镜像
|  02目录则是用来放置源码
|  03目录则是放置我们刚才下载好的交叉编译工具
|  04目录我们可以用来放置自己的app
|  把工具放到03目录下后，接下来进行工具的安装。

**安装：**

|  在03目录下运行此工具链脚本，输入如下命令：

.. code:: shell

   $ chmod +x poky-glibc-x86_64-core-image-qt-aarch64-smarc-rzg2l-toolchain-3.1.17.sh 
   $ ./poky-glibc-x86_64-core-image-qt-aarch64-smarc-rzg2l-toolchain-3.1.17.sh

|  输入安装目录/home/myzr/my_work/renesas/03_sdk

.. code:: shell

   Poky (Yocto Project Reference Distro) SDK installer version 3.1.17
   ==================================================================
   Enter target directory for SDK (default: /opt/poky/3.1.17): /home/myzr/my_work/renesas/03_sdk

|  输入y，等待安装，直到出现successfully安装成功

.. code:: shell

   You are about to install the SDK to "/home/myzr/my_work/renesas/03_sdk". Proceed [Y/n]? y
   Extracting SDK.......................

交叉编译工具配置
~~~~~~~~~~~~~~~~~

|  安装成功后在03目录下有一个environment-setup-aarch64-poky-linux脚本，输入如下命令：

.. code:: shell

   $ source environment-setup-aarch64-poky-linux

|  source后检查交叉编译工具版本等信息

.. code:: shell

   =====> Input:
   $ $CC -v

   =====> Output: 
   Using built-in specs.
   COLLECT_GCC=aarch64-poky-linux-gcc
   COLLECT_LTO_WRAPPER=/home/kuangwh/my-work/rzg2l/03_sdk/sysroots/x86_64-pokysdk-linux/usr/libexec/aarch64-poky-linux/gcc/aarch64-poky-linux/8.3.0/lto-wrapper
   Target: aarch64-poky-linux
   。。。。
   gcc version 8.3.0 (GCC)

`Note: CC是设置的宏，$CC中的"$"不能去掉`

|  看到版本信息后，编译工具配置成功，接下来就可以进行源码的编译步骤。需要注意的是，在每次打开终端窗口后都需要进行一次source配置。

编译u-boot
------------

下载uboot源码
~~~~~~~~~~~~~~

|  U-boot源码目录在 MYZR-RZ -> 02_源码 -> u-boot-Release.xxx.tar.bz2。（“Release.xxx”表示源码的版本）将源码拷贝到主机/home/myzr/my_work/renesas/02_sources目录下
|  将源码包解压到02_sources目录下：

.. code:: shell

   $ tar xvf u-boot-Release.xxx.tar.bz2

编译
~~~~~

|  进入U-boot目录

.. code:: shell

   $ cd u-boot/

|  先配置交叉编译工具

.. code:: shell

   $ source ../../03_sdk/environment-setup-aarch64-poky-linux

|  使用build.sh进行整个流程的配置和编译。

.. code:: shell

   $ ./build.sh rzg2l all

|  第一个参数为板子cpu型号选择rzg2l或rzg2ul；第二个参数有如下选项：

.. code:: shell

   config--根据第一个参数rzg2l/rzg2ul生成对应的.config文件
   make--根据当前的配置文件.config进行编译
   clean--清除编译文件
   pack--打包编译好的uboot镜像
   all--执行前面的所有操作

|  后期我们自己开发调试的时候，可以根据参数进行不同的编译配置。
|  最后打包好的镜像文件在fpack目录下：

.. code:: shell

   $ ls fpack/
   bin  bl31.bin  fip.bin  fip-myzr-rzg2l.srec  fip-myzr-rzg2ul.srec  lib

|  fip-myzr-rzg2l.srec/fip-myzr-rzg2ul.srec就是我们可以烧录到开发板的镜像文件。

编译内核
---------

下载内核源码
~~~~~~~~~~~~~

|  U-boot源码目录在 MYZR-RZ -> 02_源码 -> linux-5.10-Release.xxx.tar.bz2。（“Release.xxx”表示源码的版本）将源码拷贝到主机/home/myzr/my_work/renesas/02_sources目录下
|  将源码包解压到02_sources目录下：

.. code:: shell

   $ tar xvf linux-5.10-Release.xxx.tar.bz2

安装库
~~~~~~~

|  第一次编译内核时，需要在虚拟机ubuntu下安装相应的库

.. code:: shell

   $ sudo apt-get update
   $ sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib \
   build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
   xz-utils debianutils iputils-ping libsdl1.2-dev xterm p7zip-full libyaml-dev libssl-dev

编译Image
~~~~~~~~~~

|  进入linu-5.10目录

.. code:: shell

   $ cd linux-5.10/

|  先配置交叉编译工具

.. code:: shell

   $ source ../../03_sdk/environment-setup-aarch64-poky-linux

|  生成.config文件

.. code:: shell

   $ make myzr-rz_defconfig

|  编译Image

.. code:: shell

   $ make Image -j24

|  内核镜像编译的时间比较久，编译成功后 **arch/arm64/boot/Image** 即内核目标文件。

编译设备树
~~~~~~~~~~~

|  输入如下命令编译出设备树文件：

.. code:: shell

   $ make renesas/myzr-rzg2l-dsi.dtb

|  dtb文件根据开发板不通型号进行编译：myzr-rzg2l-dsi.dtb、myzr-rzg2l-dsi.dtb 、myzr-rzg2ul-eth.dtb、myzr-rzg2ul-lcd.dtb
|  设备树dtb文件生成在 **arch/arm64/boot/dts/renesas/*.dtb**

编译内核模块包
~~~~~~~~~~~~~~~

|  执行编译

.. code:: shell

   $ make modules

|  安装内核模块到指定目录

.. code:: shell

   make INSTALL_MOD_PATH="$PWD/install_modules" modules_install

|  删除source和build目录

.. code:: shell

   $ rm install_modules/lib/modules/5.10.131-cip13-yocto-standard/source
   $ rm install_modules/lib/modules/5.10.131-cip13-yocto-standard/build

|  strip内核模块

.. code:: shell

   $ find install_modules/ -name "*.ko" | xargs $STRIP --strip-debug --remove-section=.comment --remove-section=.note --preserve-dates

|  打包内核模块

.. code:: shell

   $ cd install_modules
   $ tar cjf modules.tar.bz2 *

|  将内核模块包modules.tar.bz2复制到开发板中并解压到根目录

.. code:: shell

   # tar xvf modules.tar.bz2 -C /

|  同步数据

.. code:: shell

   # depmod -a
   # sync
   # reboot