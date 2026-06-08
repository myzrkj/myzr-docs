MYZR-IMX28系列评估板 Linux-2.6.35 编译手册
===========================================

文档说明
---------

系统环境说明
~~~~~~~~~~~~~~

- 编译主机CPU架构：64位
- 编译主机系统：Linux
- Linux发行版：Ubuntu
- Ubuntu版本类型：服务器版
- Ubuntu版本号：12.04.5
- Ubuntu系统类型：x86-64

``注意：开发主机请使用ubuntu 12.04.5 x86-64（桌面版或服务器版均可），使用其他发行版的Linux或Ubuntu的其它版本可能会遇到的不必要的问题。``

操作说明
~~~~~~~~~~

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

|  在文档的图片中观察“linyn@u12045-serv:~$”开头的行可以直观的看到输入的linux命令。

准备源码及相关文件
-------------------

源码文件
~~~~~~~~~

|  评估板对应的Linux版本及对应的源码文件见下表：

+----------------+----------------+-----------------------------------+------------------------+
| 评估板型号     | 支持的系统版本 | u-boot源码文件                    | linux源码文件          |
+================+================+===================================+========================+
| MYZR-IMX28-EVK | Linux-2.6.35   | u-boot-2009.08.tar.bz2            | linux-2.6.35.3.tar.bz2 |
+                +                +                                   +                        +
|                |                | imx-bootlets-src-10.12.01.tar.bz2 |                        |
+----------------+----------------+-----------------------------------+------------------------+

交叉编译工具文件
~~~~~~~~~~~~~~~~~

|  Linux程序交叉编译工具：gcc-4.4.4-glibc-2.11.1-multilib-1.0.tar.bz2
|  Linux交叉编译工具配置文件：gcc-4.4.4-glibc-2.11.1-multilib-env

创建工作目录
~~~~~~~~~~~~~

|  1）源码目录

.. code-block:: shell
   
   $ mkdir -p ~/my-imx28/02_source

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_2.3.0.1.png
   :alt: IMX28_2635_build_2.3.0.1.png

|  2）工具目录

.. code-block:: shell

   $ mkdir -p ~/my-imx28/03_tools

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_2.3.0.2.png
   :alt: IMX28_2635_build_2.3.0.2.png

|  3）镜像目录

.. code-block:: shell

   $ mkdir -p ~/my-imx28/04_image

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_2.3.0.3.png
   :alt: IMX28_2635_build_2.3.0.3.png

|  4）应用程序目录

.. code-block:: shell

   $ mkdir -p ~/my-imx28/01_application

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_2.3.0.4.png
   :alt: IMX28_2635_build_2.3.0.4.png

准备开发环境
-------------

更新主机的源列表
~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get update

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.1.0.1.png
   :alt: IMX28_2635_build_3.1.0.1.png

|  更新完成后如下图所示：

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.1.0.2.png
   :alt: IMX28_2635_build_3.1.0.2.png

安装aptitude包管理工具和ia32-libs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  提示：如果编译主机的Linux是32位的，可以跳过此步骤。

安装aptitude包管理工具
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get -y install aptitude

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.2.1.1.png
   :alt: IMX28_2635_build_3.2.1.1.png

|  提示：上图为安装过aptitude后，再次执行安装命令的截图。

使用aptitude安装ia32-libs
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo aptitude -y install ia32-libs

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.2.2.1.png
   :alt: IMX28_2635_build_3.2.2.1.png

|  提示：上图为安装过aptitude和ia32-libs后，再次执行安装命令的截图。

安装mkimage工具
~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get -y install uboot-mkimage

|  提示：下图为安装过mkimage工具后，再次执行安装命令的截图。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.3.0.1.png
   :alt: IMX28_2635_build_3.3.0.1.png

安装ncurses-dev
~~~~~~~~~~~~~~~~~

|  make menuconfig对其具有依赖性质

.. code-block:: shell

   $ sudo aptitude -y install ncurses-dev

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.4.0.1.png
   :alt: IMX28_2635_build_3.4.0.1.png

|  提示：上图为安装过ncurses-dev工具后，再次执行安装命令的截图。

安装配置交叉编译工具链
----------------------

安装Linux交叉编译工具链
~~~~~~~~~~~~~~~~~~~~~~~~

|  1）进入交叉编译工具链目录

.. code-block:: shell

   $ cd ~/my-imx28/03_tools/

|  2）复制Linux交叉编译工具到目录
|  将gcc-4.4.4-glibc-2.11.1-multilib-1.0.tar.bz2复制到“~/my-imx28/03_tools”，这一步自己采取相应的方式完成。
|  3）解压Linux交叉编译工具

.. code-block:: shell

   $ tar jxf gcc-4.4.4-glibc-2.11.1-multilib-1.0.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_4.1.0.1.png
   :alt: IMX28_2635_build_4.1.0.1.png

|  4）复制交叉编译工具配置文件
|  将gcc-4.4.4-glibc-2.11.1-multilib-env复制到“~/my-imx28/03_tools”，这一步自己采取相应的方式完成。
|  5）检查安装

.. code-block:: shell

   $ source gcc-4.4.4-glibc-2.11.1-multilib-env
   $ ${CROSS_COMPILE}gcc -v

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_4.1.0.2.png
   :alt: IMX28_2635_build_4.1.0.2.png

U-Boot编译
------------

准备编译
~~~~~~~~~

**复制源码包到开发主机中**

|  将下载的“u-boot源码”复制到Linux开发主机的“~/my-imx28/02_source”。
|  这一步自己采取相应的方式完成。

**解压u-boot源码包**

.. code-block:: shell

   $ cd ~/my-imx28/02_source/
   $ tar jxf u-boot-2009.08.tar.bz2
   $ tar jxf imx-bootlets-src-10.12.01.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.1.2.1.png
   :alt: IMX28_2635_build_5.1.2.1.png

编译
~~~~~

**使编译配置文件生效**

.. code-block:: shell

   $ source ~/my-imx28/03_tools/gcc-4.4.4-glibc-2.11.1-multilib-env

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.1.1.png
   :alt: IMX28_2635_build_5.2.1.1.png

**进入u-boot源码目录**

.. code-block:: shell

   $ cd ~/my-imx28/02_source/u-boot-2009.08

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.2.1.png
   :alt: IMX28_2635_build_5.2.2.1.png

**清除u-boot临时文件**

.. code-block:: shell

   $ make distclean

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.3.1.png
   :alt: IMX28_2635_build_5.2.3.1.png

**配置u-boot**

+----------------+------------------+------------------+
| 评估板主型号   | CPU类型-内存容量 | 对应的u-boot配置 |
+================+==================+==================+
| MYZR-IMX28-EVK | MX283/7, 128M    | mx28_evk_config  |
+----------------+------------------+------------------+

- MYZR-IMX28-EVK配置示例：

.. code-block:: shell

   $ make mx28_evk_config

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.4.1.png
   :alt: IMX28_2635_build_5.2.4.1.png

**执行编译**

.. code-block:: shell

   $ make

|  提示：这里为了提高编译速度，在make后面加了“-j4”。这里编译的Linux主机是双核4线程的，所以“-j”后面用了4，也就是采用4线程编译。“-j”后面的数字可以根据系统资源分配，但是不应该超过编译主机最大支持的线程数。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.5.1.png
   :alt: IMX28_2635_build_5.2.5.1.png

- 编译imx28_ivt_uboot.sb

|  提示：imx28_ivt_uboot.sb是烧写的镜像。

.. code-block:: shell

   $ cp u-boot ../imx-bootlets-src-10.12.01
   $ cd ../imx-bootlets-src-10.12.01/
   $ sudo cp elftosb /usr/bin/
   $ ./build

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.5.2.png
   :alt: IMX28_2635_build_5.2.5.2.png

目标文件
~~~~~~~~~

- 编译文件

|  编译完成后通过ls命令即可看到编译得到的文件imx28_ivt_uboot.sb

.. code-block:: shell

   $ ls

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.3.0.1.png
   :alt: IMX28_2635_build_5.3.0.1.png

- 目标文件

|  MYZR-IMX28系列评估板的u-boot配置对应的目标文件名见下表：

===============  ==================
  u-boot配置          目标文件
===============  ==================
mx28_evk_config  imx28_ivt_uboot.sb
===============  ==================

编译内核
----------

准备编译
~~~~~~~~~

**复制源码包到开发主机中**

|  将下载的“linux源码”复制到Linux开发主机的“~/my-imx28/02_source”。
|  这一步自己采取相应的方式完成。

**解压linux源码包**

.. code-block:: shell

   $ cd ~/my-imx28/02_source/
   $ tar jxf linux-2.6.35.3.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.1.2.1.png
   :alt: IMX28_2635_build_6.1.2.1.png

内核编译配置
~~~~~~~~~~~~~

**使编译配置文件生效**

.. code-block:: shell

   $ source ~/my-imx28/03_tools/gcc-4.4.4-glibc-2.11.1-multilib-env

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.2.1.1.png
   :alt: IMX28_2635_build_6.2.1.1.png

**清除内核临时文件**

- 进入linux源码目录

.. code-block:: shell

   $ cd ~/my-imx28/02_source/linux-2.6.35.3

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.2.2.1.png
   :alt: IMX28_2635_build_6.2.2.1.png

- 清除临时文件

.. code-block:: shell

   $ make distclean

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.2.2.2.png
   :alt: IMX28_2635_build_6.2.2.2.png

- 内核配置

.. code-block:: shell

   $ cp .mx28_config .config

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.2.3.1.png
   :alt: IMX28_2635_build_6.2.3.1.png

编译内核
~~~~~~~~~

- 执行编译

.. code-block:: shell

   $ make zImage -j4

- 编译完成

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.3.0.1.png
   :alt: IMX28_2635_build_6.3.0.1.png

- 编译完成

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.3.0.2.png
   :alt: IMX28_2635_build_6.3.0.2.png

- 目标文件

|  arch/arm/boot/uImage即为编译得到的内核文件，使用ls命令可查看文件信息。

.. code-block:: shell

   $ ls arch/arm/boot/uImage -la

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.3.0.3.png
   :alt: IMX28_2635_build_6.3.0.3.png

编译模块
~~~~~~~~~~

- 编译模块命令

.. code-block:: shell

   $ make modules

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.4.0.1.png
   :alt: IMX28_2635_build_6.4.0.1.png

|  安装模块到指定目录

.. code-block:: shell

   $ make modules_install INSTALL_MOD_PATH=./modules

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.4.0.2.png
   :alt: IMX28_2635_build_6.4.0.2.png

- 打包模块文件

.. code-block:: shell

   $ cd modules
   $ tar cjf ../modules.tar.bz2 *

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.4.0.3.png
   :alt: IMX28_2635_build_6.4.0.3.png

应用程序编译
-------------

Linux应用程序编译
~~~~~~~~~~~~~~~~~~

**编写应用程序**

- 进入工作目录

.. code-block:: shell

   $ cd ~/my-imx28/01_application/

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.1.1.png
   :alt: IMX28_2635_build_7.1.1.1.png

- 编写源代码

.. code-block:: shell

   $ vim hello.c

|  写入以下代码并保存

.. code:: c

   include <stdio.h>
   int main(int argc, char **argv)
   {
      printf("Hello, MYZR!\n");
      return;
   }

- 查看代码

.. code-block:: shell

   $ cat hello.c

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.1.2.png
   :alt: IMX28_2635_build_7.1.1.2.png

**编译应用程序**

- 配置环境变量

.. code-block:: shell

   $ source ~/my-imx28/03_tools/gcc-4.4.4-glibc-2.11.1-multilib-env

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.2.1.png
   :alt: IMX28_2635_build_7.1.2.1.png

- 编译

.. code-block:: shell

   $ ${CROSS_COMPILE}gcc hello.c -o hello.out

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.2.2.png
   :alt: IMX28_2635_build_7.1.2.2.png

|  注意：上面的命令有包含“$”号，即“${CROSS_COMPILE}gcc”，是引用我们source时产生的环境变量。

- 目标文件

.. code-block:: shell

   $ file hello.out

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.2.3.png
   :alt: IMX28_2635_build_7.1.2.3.png

|  可以看到目标文件 hello.out 的属性。

文件系统
---------

文件系统rootfs.tar.bz2
~~~~~~~~~~~~~~~~~~~~~~~

|  用以下的方式增加自己的应用：（把MY-IMX28_Born_Tool\Profiles\MX28 Linux Update\OS Firmware\files\image-linux-2635/rootfs.tar.bz2复制到“~/my-imx28/04_image/”目录下）。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_8.1.0.1.png
   :alt: IMX28_2635_build_8.1.0.1.png

文件系统rootfs.ubifs
~~~~~~~~~~~~~~~~~~~~~

|  复制mkfs.ubifs，ubinize到电脑的“/usr/bin”目录下（如果电脑有这两个应用就不需要复制了）；复制build_rootfs和ubinize.cfg到“~/my-imx28/04_image/”目录。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_8.2.0.1.png
   :alt: IMX28_2635_build_8.2.0.1.png

烧写方式
---------

|  至此，我们在“~/my-imx28/02_source/”得到了除文件系统以外的一套烧录文件。包括“imx28_ivt_uboot.sb”、“uImage”、“rootfs.tar.bz2”。

使用MFGTOOL烧写
~~~~~~~~~~~~~~~~

|  把文件“imx28_ivt_uboot.sb”、“uImage”、“rootfs.tar.bz2复制到“MY-IMX28_Born_Tool\Profiles\MX28 Linux Update\OS Firmware\files\image-linux-2635”目录下。按住REC按键，插上MINI USB线和电源线，接着打开MfgTool.exe,点击“扫描设备”，检测到HID设备时，松开REC按键,如下所示：

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_9.1.0.1.png
   :alt: IMX28_2635_build_9.1.0.1.png

|  点击菜单的“Options”，然后在选项“Profiles”选择“MY-IMX28-2.6.35 NAND with uboot”，接着点击“确定”，最后点击“开始”。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_9.1.0.2.png
   :alt: IMX28_2635_build_9.1.0.2.png

|  烧写成功后，点击“停止”就OK了。
|  when programming is succeeded,click"stop",to finish

``注意：如果你用的文件系统是rootfs-qt.tar.bz2，请选择“QT-MY-IMX28-2.6.35 NAND with uboot”烧写镜像。``

|  note: if the file system you are using is rootfs-qt.tar.bz2,please choose “QT-MY-IMX28-2.6.35 NAND with uboot”as programming image

使用网络烧写
~~~~~~~~~~~~~

**搭建TFTP (ubuntu系统)**

|  (1) Setup tftp server files （下载并安装tftp）

.. code-block:: shell

   $ sudo apt-get install tftpd tftp openbsd-inetd

|  (2) make a tftp directory (新建tftp目录和改变其属性)
|  Here we make /home/myzr/tftpt be a tftp directory.

.. code-block:: shell

   $ mkdir /home/myzr/tftp
   $ chmod 777 /home/myzr/tftp

|  (3) Open /etc/inetd.conf and edit it (修改配置文件的tftp目录)

.. code-block:: shell

   $ sudo gedit /etc/inetd.conf

|  Coment this line :
|  tftp dgram udp wait nobody /usr/sbin/tcpd /usr/sbin/in.tftpd /srv/tftp
|  Add new line:
|  tftp dgram udp wait nobody /usr/sbin/tcpd /usr/sbin/in.tftpd /home/myzr/tftp
|  (4)Restarting tftp service （重启tftp）

.. code-block:: shell

   $ sudo /etc/init.d/openbsd-inetd restart

**搭建NFS (网络烧写不需要用到nfs)**

|  (1) Install NFS server package （下载并安装nfs）

.. code-block:: shell

   $ sudo apt-get install nfs-kernel-server

|  (2) Create NFS directory:/home/myzr/nfsroot (新建nfs目录)

.. code-block:: shell

   $ mkdir /home/myzr/nfsroot

(3) Configure mounted directory and authority （修改配置文件的nfs目录）

.. code-block:: shell

   $ sudo gedit /etc/exports

|  Add the following line at the end of the file:
|  /home/myzr/nfsroot \*(rw,sync,no_root_squash)

|  (4) Restart the NFS service （重启nfs）

.. code-block:: shell

   $ sudo /etc/init.d/portmap restart
   $ sudo /etc/init.d/nfs-kernel-server restart

**tftp下载**

|  (1) 把“uImage”和“rootfs.ubifs”复制到“/home/myzr/tftp”目录下。
|  (2) 设置环境变量(板子和电脑网线直连)

.. code-block:: shell

   $ setenv ipaddr 192.168.3.104 （板子IP）
   $ setenv serverip 192.168.3.110 （电脑IP）

|  (3) 烧写

.. code-block:: shell

   $ run upkernel (烧写uImage)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_9.2.3.1.png
   :alt: IMX28_2635_build_9.2.3.1.png

.. code-block:: shell

   $ run upsystem (烧写文件系统)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_9.2.3.2.png
   :alt: IMX28_2635_build_9.2.3.2.png

登录方式
----------

串口登录
~~~~~~~~~

|  插上USB转串口线和电源，开机后，差不多12秒后，在终端上敲回车键可以进入系统。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_10.1.0.1.png
   :alt: IMX28_2635_build_10.1.0.1.png

ssh登录
~~~~~~~~~

**以太网登录**

|  插上网线和电源，开机后，差不多10秒后，可以软件SecureCRT登录，板子默认以太网的IP为192.168.3.104，你可以设置电脑的IP为192.168.3.110，然后配置SecureCRT，输入用户名是root，密码myzr。如下图：

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_10.2.1.1.png
   :alt: IMX28_2635_build_10.2.1.1.png

|  输入完后，点击”OK“就登录完成。

**USB登录（USB可识别成网口）**

|  插上MINI USB线，开机后，差不多10秒后，可以软件SecureCRT登录。
|  加载驱动和设置IP，如下：

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_10.2.2.1.png
   :alt: IMX28_2635_build_10.2.2.1.png

|  板子USB的IP为192.168.4.104，你可以设置电脑的IP为192.168.4.110，然后配置SecureCRT，输入用户名是root，密码myzr。如下图：
|  输入完后，点击”OK“就登录完成。

测试
------

USB测试
~~~~~~~~

|  直接插上U盘，挂载后可看到U盘的内容。（不是QT系统，会自动挂载）

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.1.0.1.png
   :alt: IMX28_2635_build_11.1.0.1.png

SD卡测试
~~~~~~~~~

|  直接插上SD卡，挂载后可看到SD卡的内容。（不是QT系统，会自动挂载）

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.2.0.1.png
   :alt: IMX28_2635_build_11.2.0.1.png

以太网测试
~~~~~~~~~~~

|  插上网线，直接用ping命令测试eth0和eth1网口。默认eth0的IP为192.168.3.104，我设置eth1为192.168.3.105。如下：

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.3.0.1.png
   :alt: IMX28_2635_build_11.3.0.1.png

uart串口测试
~~~~~~~~~~~~~

|  串口uat0的设备ttySP0,串口uat3的设备ttySP3。测试时，请短接发管脚（J10的5和7号管脚）。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.4.0.1.png
   :alt: IMX28_2635_build_11.4.0.1.png

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.4.0.2.png
   :alt: IMX28_2635_build_11.4.0.2.png

gpio测试
~~~~~~~~~

|  GPIO_2_26已经在驱动配置为GPIO功能了，下面以管脚GPIO_2_26为例，计算GPIO_2_26的管脚号为2*32+26=90,测试如下：（GPIO_2_26对应管脚J16的3脚）

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.5.0.1.png
   :alt: IMX28_2635_build_11.5.0.1.png

spi测试
~~~~~~~~

|  SPI接口为半双工模式，这里你只测发，通过示波器可观察到波形。方法一只发送0x55和0x75；方法二是发送字符串”myzr“（J14的6和8号管脚）。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.6.0.1.png
   :alt: IMX28_2635_build_11.6.0.1.png

watdog测试
~~~~~~~~~~~~

|  “看门狗”，全称Watchdog timer，是一个在软件出错的时候可以复位计算机系统的硬件定时器。通常一个用户空间守护进程会在正常的时间间隔内通过/dev/watchdog 特殊设备文件来通知内核的Watchdog驱动，用户空间一切正常。如果用户空间出现问题（如RAM 错误，内核BUG 等），则通知将会停止，然后硬件Watchdog 将在超时后复位系统。
|  测试程序中打开/dev/watchdog 设备文件，启动了Watchdog，每过一秒钟喂狗一次，系统不会重启。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.7.0.1.png
   :alt: IMX28_2635_build_11.7.0.1.png

|  测试程序中打开了/dev/watchdog 设备文件，启动Watchdog，程序进入循环状态，由于没有喂狗，30 秒后系统复位。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.7.0.2.png
   :alt: IMX28_2635_build_11.7.0.2.png
