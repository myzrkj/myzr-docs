MYZR Windows-10 VirtualBox-5.2.12 Ubuntu-14.04.5 64位开发环境指导
=================================================================

文件下载
---------

| 　打开网站：wiki.myzr.com.cn，点击MYZR 通用资源。 虚拟机软件及系统：打开网盘到 MYZR-COMMON-20181007 -> 1.1_虚拟机软件及系统，下载 VirtualBox-5.2.12 目录。

虚拟机软件安装
--------------

| 　打开下载的 VirtualBox-5.2.12 文件夹，双击 VirtualBox-5.2.12-122591-Win.exe，参照 01_VB5212_Installation 安装。

为虚拟机配置 Windows
---------------------

添加 Windows 网卡
~~~~~~~~~~~~~~~~~~

| 　打开下载的 VirtualBox-5.2.12 文件夹，参照 03_WIN10_LoopbackAdapterAdd，把 Loopback Adapter 添加到 Windows。

配置 Windows 网卡
~~~~~~~~~~~~~~~~~~

| 　打开下载的 VirtualBox-5.2.12 文件夹，参照 04_WIN10_LoopbackAdapterSettings，在 Windows 下配置 Loopback Adapter。

导入虚拟机系统
~~~~~~~~~~~~~~

| 　打开下载的 VirtualBox-5.2.12 文件夹，参照 07_VB5212_ImportVirtualAppliance_U14045，把虚拟机系统导入到 VirtualBox。

虚拟机设置
-----------

| 　打开下载的 VirtualBox-5.2.12 文件夹，参照 08_VB5212_VirtualMachineSettings_U14045，配置好虚拟机。

虚拟机与PC互传文件
------------------

| 　打开下载的 VirtualBox-5.2.12 文件夹，参照 09_VB5212_file transfer_U14045，用Samba或SSH传送文件。

虚拟机使用
-----------

用户和密码
~~~~~~~~~~~

| 　默认用户：tangb，UserName：myzr，Password：myzr2012
| 　超级用户：root，UserName：root，Password：myzr2012