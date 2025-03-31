MYZR VMware-10.0.5 Ubutnu-12.04.5 64位虚拟机开发环境手册（旧的）
=================================================================

安装并运行虚拟机系统
---------------------

|  建议使用我们提供的虚拟机系统作为开发主机，本节针对我们提供的虚拟机进行指导。
|  如需要自己搭建开发环境的朋友，也请先按手册操作过一遍之后再自行搭建开发环境，以免在操作过程中浪费不必要的时间和精力。

准备虚拟机系统和软件
~~~~~~~~~~~~~~~~~~~~

|  1）下载虚拟机系统
|  文件名：vm10-u12045-serv-amd64.rar
|  这是安装配置好的Ubuntu 12.04.5 Server版的工作环境。
|  2）下载虚拟机软件
|  文件名：VMware-workstation-full-10.0.5-2443746.exe
|  这是虚拟机软件VMware workstation。

安装虚拟机
~~~~~~~~~~~

|  1）解压虚拟机系统
|  在Windows下解压vm10-u12045-serv-amd64.rar到当前文件夹。
|  2）安装虚拟机软件
|  参照 vm10-u12045-serv-amd64 目录下的“00.vmware10安装”安装VMware-workstation-full-10.0.5-2443746.exe。

运行虚拟机系统
~~~~~~~~~~~~~~~

|  1）启动VMware Workstation软件
|  2）装载虚拟机系统
|  在VMware Workstation菜单栏依次操作：文件 -> 打开 -> 找到vm10-u12045-serv-amd64目录，选择“vm10-u12045-serv-amd64.vmx” -> 打开
|  3）启动虚拟机系统

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.1.3.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.1.3.1.png

|  点击“开启此虚拟机”

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.1.3.2.png
   :alt: MY-SAMA5_Linux-3.18_build_2.1.3.2.png

|  选择“我已复制该虚拟机”
|  4）登录虚拟机系统
|  用户名：myzr
|  密码：myzr123

配置开发环境
-------------

更新虚拟机系统的源列表
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get update

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.2.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.0.1.png

|  更新完成后如下图所示：

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.2.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.0.2.png

更新虚拟机系统
~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get -y dist-upgrade

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.2.2.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.2.1.png

|  上图是更新虚拟机系统后再执行更新命令的截图。

安装aptitude包管理工具和ia32-libs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1）安装aptitude包管理工具

.. code-block:: shell

   $ sudo apt-get -y install aptitude

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.2.3.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.3.1.png

|  提示：上图为安装过aptitude后，再次执行安装命令的截图。
|  2）使用aptitude安装ia32-libs

.. code-block:: shell

   $ sudo aptitude -y install ia32-libs

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.2.3.2.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.3.2.png

|  提示：上图为安装过aptitude和ia32-libs后，再次执行安装命令的截图。

安装mkimage工具(install mkimage tool)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get -y install uboot-mkimage

|  提示：下图为安装过mkimage工具后，再次执行安装命令的截图。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.2.4.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.4.1.png

安装ncurses-dev
~~~~~~~~~~~~~~~~~

|  make menuconfig对其具有依赖性质

.. code-block:: shell

   $ sudo aptitude -y install ncurses-dev

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.2.5.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.5.1.png

|  提示：上图为安装过ncurses-dev工具后，再次执行安装命令的截图。

常用功能演示
-------------

|  我们提供的虚拟机系统中已经配置好samba服务、tftp服务、nfs服务、GUI桌面等功能。具体可查看vm10-u12045-serv-amd64目录下03.* ~ 05.* 的文件。

在Windows与虚拟机系统之间复制文件
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  由于在开发过程中需要经常在Windows和虚拟机系统之间共享文件，所以这里对这种操作进行演示和说明。
|  1）在windows下打开虚拟机系统的共享目录
|  说明：在虚拟机系统中“/home/myzr”被配置为有权限的、可通过网络访问的共享目录，访问路径为“虚拟主机名/myzr.d”或“虚拟主机IP/myzr.d”。
|  打开windows的“计算机或我的电脑”，在地址栏输入“\\u12045\myzr.d”（注意：windows系统下路径使用的是反斜杠）。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.3.1.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.3.1.1.png

|  2）输入虚拟机系统的用户名和密码（myzr : myzr123）

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.3.1.2.png
   :alt: MY-SAMA5_Linux-3.18_build_2.3.1.2.png

|  3）输入正确的用户名和密码点击确定后共享目录即可访问
|  即可在Windows和虚拟机系统之间复制文件。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY-SAMA5_Linux-3.18_build_2.3.1.3.png
   :alt: MY-SAMA5_Linux-3.18_build_2.3.1.3.png
