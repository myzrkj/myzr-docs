MYZR-STM32MP15-EK152编译参考手册
=================================

交叉编译工具
~~~~~~~~~~~~

|  当我们想要编译源码或者编译自己修改的源码时，首先要做的第一步就是配置对应的交叉编译工具。对于本套源码，我们是以st官方SDK提供的交叉编译工具为基础来进行编译的。

编译工具下载和安装
""""""""""""""""""

**下载：**

|  交叉编译工具的下载需到我们提供的网盘上来进行下载，其对应的网盘目录为 **03_编译工具**。下载到电脑后，需要通过Samba或其他方法将其复制到虚拟机上来。

|  我们可以创建一个stm32mp157a专属的目录来存放相关的源码，编译工具和以后用到的一些东西。如我的目录为： **/home/kuangwh/my-work/stm32mp1** ，在此目录下我又创建了4个子目录：

.. code:: shell

   =====> Input:
   $ ls
   01_image  02_sources  03_sdk  04_app

|  01目录可以用来放置我们编译好的镜像（以后用到会说明）

|  02目录则是用来放置源码

|  03目录则是放置我们刚才下载好的交叉编译工具

|  04目录我们可以用来放置自己的app（用户自己分配）

|  把工具放到03目录下后，接下来进行工具的安装。

**安装：**

|  在03目录下运行此工具链脚本，输入如下命令：

.. code:: shell
   
   =====> Input:
   $ ./st-image-weston-openstlinux-weston-stm32mp1-x86_64-toolchain-3.1-openstlinux-5.4-dunfell-mp1-20-06-24.sh

|  输入安装目录/home/kuangwh/my-work/stm32mp1/03_sdk/

.. code:: shell
   
   ST OpenSTLinux - Weston - (A Yocto Project Based Distro) SDK installer version 3.1-openstlinux-5.4-dunfell-mp1-20-06-24
   =======================================================================================================================
   Enter target directory for SDK (default: /opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-mp1-20-06-24): /home/kuangwh/my-work/stm32mp1/03_sdk/

|  输入y

.. code:: shell
   
   You are about to install the SDK to "/home/kuangwh/my-work/stm32mp1/03_sdk". Proceed [Y/n]? y

|  安装过程需要耐心等待，直达出现successfully安装成功

.. code:: shell

   =====> Output:
   Extracting SDK......................................................................................................
   done
   Setting it up...done
   SDK has been successfully set up and is ready to be used.
   Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
   $ . /home/kuangwh/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi

交叉编译工具配置
"""""""""""""""""

|  安装成功后，在03目录下有一个environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi脚本，输入如下命令：

.. code:: shell

   =====> Input:
   $ source environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi

|  source后检查交叉编译工具版本等信息

.. code:: shell

   =====> Input:
   $ $CC -v

   =====> Output: 
   Using built-in specs.
   COLLECT_GCC=arm-ostl-linux-gnueabi-gcc
   COLLECT_LTO_WRAPPER=/sdc1/kwh-work/stm32mp1/03_sdk/sysroots/x86_64-ostl_sdk-linux/usr/bin/arm-ostl-linux-gnueabi/../../libexec/arm-ostl-linux-gnueabi/gcc/arm-ostl-linux-gnueabi/9.3.0/lto-wrapper
   Target: arm-ostl-linux-gnueabi
   Configured with: ../../../../../../work-shared/gcc-9.3.0-r0/gcc-9.3.0/configure --build=x86_64-linux --host=x86_64-ostl_sdk-linux --target=arm-ostl-linux-gnueabi --prefix=/opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-mp1-20-06-24/sysroots/x86_64-ostl_sdk-linux/usr --exec_prefix=/opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-mp1-20-06-24/sysroots/x86_64-ostl_sdk-linux/usr --bindir=/opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-mp1-20-06-24/sysroots/x86_64-ostl_sdk-linux/usr/bin/arm-ostl-linux-gnueabi --sbindir=/opt/st/stm32mp1/3.1-openstlinux-5.4-dunfell-
   。。。。。。
   gcc version 9.3.0 (GCC) 

**Note: CC是设置的宏，$CC中的"$"不能去掉**

|  看到版本信息后，编译工具配置成功，接下来就可以进行源码的编译步骤。需要注意的是，在每次打开终端窗口后都需要进行一次source配置。

编译TF-A
~~~~~~~~~~

**下载源码包**

|  到提供的网盘上下载源码包，网盘目录为 **02_源码/tf-a-stm32mp-2.2-Release.xxx.tar.bz2** ，并使用Samba或其他方法将源码包复制到虚拟机中的~/my-work/stm32mp1/02_sources目录下。
|  （xxx为版本日期，以后会更新版本，所以这里不写具体版本日期）

|  将源码包tf-a解压到当前目录下：

.. code:: shell

   =====> Input:
   $ tar xvf tf-a-stm32mp-2.2-Release.xxx.tar.bz2

**编译**

|  进入目录tf-a-stm32mp-2.2

.. code:: shell

   =====> Input:
   $ cd tf-a-stm32mp-2.2/
   $ ls
   Makefile.sdk  tf-a-stm32mp-2.2.r1

|  先配置交叉编译工具

.. code:: shell

   =====> Input:
   $ source ~/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi 

|  进入tf-a-stm32mp-2.2.r1目录

.. code:: shell

   =====> Input:
   $ cd tf-a-stm32mp-2.2.r1/

|  编译前先clean

.. code:: shell

   =====> Input:
   $ make -f ../Makefile.sdk clean

|  make编译

.. code:: shell

   =====> Input:
   $ make -f ../Makefile.sdk all

|  几分钟后，编译成功，会在上级目录出现一个build/trusted目录，里面存放的就是编译出的镜像文件 **tf-a-myzr-stm32mp15-256m-trusted.stm32/tf-a-myzr-stm32mp15-512m-trusted.stm32**。

编译u-boot
~~~~~~~~~~~

**下载uboot源码**

|  到提供的网盘上下载源码包，网盘目录为 **02_源码/u-boot-stm32mp-2020.01-Release.xxx.tar.bz2** ，并使用Samba或其他方法将源码包复制到虚拟机中的~/my-work/stm32mp1/02_sources目录下。

|  将源码包u-boot-stm32mp-2020.01-Release.xxx.tar.bz2解压

.. code:: shell

   =====> Input:
   $ tar xvf u-boot-stm32mp-2020.01-Release.xxx.tar.bz2

**编译**

|  进入目录u-boot-stm32mp-2020.01

.. code:: shell

   =====> Input:
   $ cd u-boot-stm32mp-2020.01/

|  先配置交叉编译工具

.. code:: shell

   =====> Input:
   $ source ~/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi 

|  编译前先清除配置

.. code:: shell

   =====> Input:
   $ make distclean

|  生成.config文件

.. code:: shell

   =====> Input:
   $ make myzrstm32mp15_defconfig

   =====> Output: 
   #
   # configuration written to .config
   #

|  make编译，512m内存的板子make DEVICE_TREE=myzr-stm32mp15-512m，256m的板子make DEVICE_TREE=myzr-stm32mp15-256m

.. code:: shell

   =====> Input:
   $ make DEVICE_TREE=myzr-stm32mp15-256m
   =====> or
   $ make DEVICE_TREE=myzr-stm32mp15-512m

   =====> Output:
   scripts/kconfig/conf  --syncconfig Kconfig
     CHK     include/config.h
     UPD     include/config.h
     CFG     u-boot.cfg
     。。。
     MKIMAGE u-boot.stm32
     OBJCOPY u-boot.srec
     SYM     u-boot.sym
     COPY    u-boot.dtb
     CFGCHK  u-boot.cfg

|  u-boot.stm32即为编译出的目标文件

.. code:: shell

   $ ls u-boot.stm32
   u-boot.stm32

编译kernel
~~~~~~~~~~~~

**下载kernel源码**

|  到提供的网盘上下载源码包，网盘目录为 **02_源码/linux-5.4.31-Release.xxx.tar.bz2** ，并使用Samba或其他方法将源码包复制到虚拟机中的~/my-work/stm32mp1/02_sources目录下。

|  将源码包linux-5.4.31-Release.xxx.tar.bz2解压

.. code:: shell

   =====> Input:
   $ tar xvf linux-5.4.31-Release.xxx.tar.bz2

**安装库**

|  第一次编译内核时，需要在虚拟机ubuntu下安装相应的库

.. code:: shell

   $ sudo apt-get install libncurses5-dev libncursesw5-dev libyaml-dev
   $ sudo apt-get install u-boot-tools
   $ sudo apt-get install libyaml-dev

**编译内核**

|  进入目录linux-5.4.31

.. code:: shell

   =====> Input:
   ~/my-work/stm32mp1/02_sources$ cd linux-5.4.31/

|  先配置交叉编译工具

.. code:: shell

   =====> Input:
   $ source ~/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi 

|  生成.config文件

.. code:: shell

   =====> Input:
   $ make myzrstm32mp15_defconfig

   =====> Output: 
     HOSTCC  scripts/basic/fixdep
     HOSTCC  scripts/kconfig/conf.o
     HOSTCC  scripts/kconfig/confdata.o
     HOSTCC  scripts/kconfig/expr.o
     LEX     scripts/kconfig/lexer.lex.c
     YACC    scripts/kconfig/parser.tab.[ch]
     HOSTCC  scripts/kconfig/lexer.lex.o
     HOSTCC  scripts/kconfig/parser.tab.o
     HOSTCC  scripts/kconfig/preprocess.o
     HOSTCC  scripts/kconfig/symbol.o
     HOSTLD  scripts/kconfig/conf
   #
   # configuration written to .config
   #

|  编译内核目标文件

.. code:: shell

   =====> Input:
   $ make uImage LOADADDR=0xC2000040

   =====> Output: 
   。。。
     UIMAGE  arch/arm/boot/uImage
   Image Name:   Linux-5.4.31
   Created:      Mon Oct 19 07:14:40 2020
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    7312904 Bytes = 7141.51 KiB = 6.97 MiB
   Load Address: c2000040
   Entry Point:  c2000040
     Kernel: arch/arm/boot/uImage is ready

|  内核镜像编译的时间比较久，编译成功后arch/arm/boot/uImage 即内核目标文件。

**编译设备树**

|  输入如下命令单独编译出设备树

.. code:: shell

   =====> Input:
   $ make myzr-stm32mp15.dtb

   =====> Output: 
     DTC     arch/arm/boot/dts/myzr/myzr-stm32mp15.dtb

|  设备树dtb文件生成在 **arch/arm/boot/dts/myzr/myzr-stm32mp15.dtb** 。

|  编译使用hdmi显示的设备树：

.. code:: shell

   =====> Input:
   $ make myzr-stm32mp15-hdmi.dts

   =====> Output: 
     DTC     arch/arm/boot/dts/myzr/myzr-stm32mp15-hdmi.dtb

**编内核模块包**

|  执行编译

.. code:: shell

   =====> Input:
   $ make modules

   =====> Output: 
   。。。
     CC [M]  sound/usb/snd-usb-audio.mod.o
     LD [M]  sound/usb/snd-usb-audio.ko
     CC [M]  sound/usb/snd-usbmidi-lib.mod.o
     LD [M]  sound/usb/snd-usbmidi-lib.ko

|  安装内核模块到指定目录

.. code:: shell

   =====> Input:
   $ make INSTALL_MOD_PATH="$PWD/install_artifact" modules_install

   =====> Output: 
     INSTALL sound/soc/fsl/snd-soc-fsl-sai.ko
     INSTALL sound/soc/generic/snd-soc-simple-card.ko
     INSTALL sound/usb/snd-usb-audio.ko
     INSTALL sound/usb/snd-usbmidi-lib.ko
     DEPMOD  5.4.31

|  删除source和build目录

.. code:: shell

   =====> Input:
   $ rm install_artifact/lib/modules/5.4.31/source
   $ rm install_artifact/lib/modules/5.4.31/build

|  strip内核模块

.. code:: shell

   =====> Input:
   $ find install_artifact/ -name "*.ko" | xargs $STRIP --strip-debug --remove-section=.comment --remove-section=.note --preserve-dates

|  打包内核模块

.. code:: shell

   =====> Input:
   $ cd install_artifact
   $ tar cjf modules.tar.bz2 *

|  解压内核模块包到开发板

|  将内核模块包复制到开发板中并解压到根目录

.. code:: shell

   =====> Input:
   # tar xvf modules.tar.bz2 -C /

|  同步数据（256m ddr的板子不需同步）

.. code:: shell

   =====> Input:
   # depmod -a
   # sync
   # reboot

应用编程示例
~~~~~~~~~~~~~

|  到提供的网盘上下载应用程序代码，网盘目录为 **05_其它->hello_world.tar.bz2** ，并使用Samba或其他方法将源码包复制到虚拟机中的~/my-work/stm32mp1/04_app目录下。

|  进入hello_world目录

.. code:: shell

   =====> Input:
   $ cd hello_world/

|  先配置交叉编译工具

.. code:: shell

   =====> Input:
   $ source ~/my-work/stm32mp1/03_sdk/environment-setup-cortexa7t2hf-neon-vfpv4-ostl-linux-gnueabi 

|  编译gtk_hello_world.c

.. code:: shell

   =====> Input:
   $ make

|  将编译出的二进制文件gtk_hello_world移动到开发板（移动方法参考前面体验篇的文件传输），开发板需接上显示屏。

|  给以可执行权限并执行文件

.. code:: shell

   =====> Input:
   $ chmod +x gtk_hello_world
   $ ./gtk_hello_world

   =====> Output: 
   (gtk_hello_world:6370): dbind-WARNING **: 18:17:49.914: Error retrieving accessibility bus address: org.a11y.Bus.Error: Failed to execute chi)

|  成功运行后可在屏幕上显示出hello world窗口。