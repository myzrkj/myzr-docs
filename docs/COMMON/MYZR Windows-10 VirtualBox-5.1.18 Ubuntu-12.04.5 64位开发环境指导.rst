MYZR Windows-10 VirtualBox-5.1.18 Ubuntu-12.04.5 64位开发环境指导
===================================================================


文件下载
~~~~~~~~~

**通用资源**

- MYZR-通用资源

 |  位置：打开网站：wiki.myzr.com.cn， 点击"MYZR-通用资源"

**虚拟机软件**

- VirtualBox-5.1.18

 |  位置：MYZR-通用资源 -> MYZR-COMMON-20181007 -> 1.1_虚拟机软件及系统 -> 1.1_VirtualBox-5.1.18__ubuntu-12.04.5__WIN10

**虚拟机系统**

- Ubuntu-12.04.5

 |  位置：MYZR-通用资源 -> MYZR-COMMON-20181007 -> 1.1_虚拟机软件及系统 -> 1.2_VirtualBox-4.3.40__ubuntu-12.04.5__WIN7 -> vb43-u12045-serv-amd64.ova

虚拟机软件安装
~~~~~~~~~~~~~~~

 |  打开下载的 “VirtualBox-5.1.18” 文件夹，双击 “VirtualBox-5.1.18-114002-Win.exe”，参照 “01_VB5118_Installation” 安装。


为虚拟机配置 Windows
~~~~~~~~~~~~~~~~~~~~~

**添加 Windows 网卡**

 |  打开下载的 “VirtualBox-5.1.18” 文件夹，参照 “03_WIN10_LoopbackAdapterAdd” ，把 Loopback Adapter 添加到 Windows。

**配置 Windows 网卡**

 |  打开下载的 “VirtualBox-5.1.18” 文件夹，参照 “04_WIN10_LoopbackAdapterSettings” ，在 Windows 下配置 Loopback Adapter。

**导入虚拟机系统**

 |  打开下载的 “VirtualBox-5.1.18” 文件夹，参照 “07_VB5118_ImportVirtualAppliance” ，把虚拟机系统导入到 VirtualBox。

虚拟机设置
~~~~~~~~~~

 |  打开下载的 “VirtualBox-5.1.18” 文件夹，参照 “08_VB5118_VirtualMachineSettings” ，配置好虚拟机。

虚拟机与PC互传文件
~~~~~~~~~~~~~~~~~~

 |  打开下载的 “VirtualBox-5.1.18” 文件夹，参照 “09_VB5118_file transfer_U12045”，用Samba或SSH传送文件。

虚拟机使用
~~~~~~~~~~

**登录**

- 用户名

 |  tangb

- 密码

 |  myzr2012