
MYZR-RK3288-EK314 烧录手册
===========================

适用范围
---------

**评估板所对应的操作系统支持**

+-------------------+-------------------+-----+-----+
| 评估板型号        | Linux系统版本支持             |
+                   +-------------------+-----+-----+
|                   | Linux-3.10.79     | NC  | NC  |
+-------------------+-------------------+-----+-----+
| MYZR-RK3288-EK314 | √                 |     |     |
+-------------------+-------------------+-----+-----+


+-------------------+---------------------+-----+-----+
| 评估板型号        | Android系统版本支持             |
+                   +---------------------+-----+-----+
|                   | Android-5.1.1       | NC  | NC  |
+-------------------+---------------------+-----+-----+
| MYZR-RK3288-EK314 | √                   |     |     |
+-------------------+---------------------+-----+-----+

**操作系统所对应的文件系统支持**

|  由于 Linux 系统与文件系统的关系是一对多，同一个 Linux 系统可以支持不同的文件系统，这里把对应的关系列表如下：
|  另外，文件系统相对比较大，最小的文件虽然只有几MB，但是最大的文件系统有1GB多。为了节省大家的下载时间，大家先根据下表预先选定自己需要的文件系统，在下载文件系统那一步骤的时候就可以只下载自己需要的文件系统。

+---------------+-------------------+--------+--------------------------------+------------------+--------------------+--------------+
| 操作系统      | 文件系统支持                                                | 文件系统的文件名 | 文件系统的文件大小 | 文件系统说明 |
+===============+===================+========+================================+==================+====================+==============+
| linux-3.10.79 | linux-rootfs.img  | 1.25GB | MYZR-RK3288-EK314的ubuntu14.04 |                  |                    |              |
+---------------+-------------------+--------+--------------------------------+------------------+--------------------+--------------+
| Android-5.1.1 | system-ard511.img | 440MB  | Android 5.1.1 系统文件         |                  |                    |              |
+---------------+-------------------+--------+--------------------------------+------------------+--------------------+--------------+


准备烧录工具
-------------

**烧录工具的目录及文件说明**

这里直观的描述出完整的烧录工具目录及文件结构，并简要的对目录及文件进行说明，方便大家理解烧录工具。

.. code:: shell
   
    /
    |-> AndroidTool_Release_v2.35
    |　　 |-> AndroidTool.exe： 烧录工具主程序 (Main program)
    |　　 |-> config.cfg： android配置
    |　　 |-> rk32-myzr-ubuntu.cfg： ubuntu配置
    |-> DriverAssitant_v4.2
    |　　 |-> DriverInstall.exe： RK3288 USB芯片驱动,烧写需要
    |-> rockdev
    |　　 |-> Image
    |　　　　|-> linux
    |　　　　　　|-> RK3288UbootLoader_V2.30.10.bin：u-boot文件
    |　　　　　　|-> rk3288box-3.10-uboot-ubuntu.parameter.txt：环境变量和分区信息
    |　　　　　　|-> linux-boot_lvds.img：lvds内核文件
    |　　　　　　|-> linux-boot_hdmi.img：hdmi内核文件
    |　　　　　　|-> linux-boot_edp.img： edp内核文件
    |　　　　　　|-> linux-rootfs.img：文件系统
    |　　　　|-> android
    |　　　　　　|-> RK3288UbootLoader_V2.30.10.bin：u-boot文件
    |　　　　　　|-> rk3288box-3.10-uboot-android.parameter.txt：环境变量和分区信息
    |　　　　　　|-> resource-lvds.img：lvds设备树文件和图片
    |　　　　　　|-> resource-hdmi.img：hdmi设备树文件和图片
    |　　　　　　|-> resource-edp.img： edp设备树文件和图片
    |　　　　　　|-> boot.img：Android 的初始文件映像，负责初始化并加载 system 分区
    |　　　　　　|-> kernel.img：内核文件
    |　　　　　　|-> misc.img：misc 分区映像，负责启动模式切换和急救模式的参数传递
    |　　　　　　|-> recovery.img：急救模式映像
    |　　　　　　|-> system.img：Android 的 system 分区映像
    |　　　　|-> relase_update.img: ubuntu14.04镜像
    |　　　　|-> relase_android_update.img: android5.1镜像
    |


准备烧写工具和镜像
------------------

**烧写工具**

|  文件名：AndroidTool_Release_v2.35.rar


**预编译镜像**

|  预编译文件夹： Image


安装驱动和导入配置
------------------

**解压AndroidTool_Release_v2.35.rar**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.1.1.png
   :alt: My-rk32-ek314_download_3.1.1.png

**复制下载的Image到相应的目录**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.2.1.png
   :alt: My-rk32-ek314_download_3.2.1.png

**安装驱动**

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.2.1.png
   :alt: My-rk32-ek314_download_3.2.1.png

**导入配置**

| 1）导入android的配置
|  方法一：双击“AndroidTool.exe”
|  方法二：打开“AndroidTool.exe”后，右击“导入配置”，找到目录AndroidTool_Release_v2.35\config.cfg文件

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.4.1.png
   :alt: My-rk32-ek314_download_3.4.1.png

| 2）导入ubuntu的配置
|  打开“AndroidTool.exe”后，右击“导入配置”，找到目录AndroidTool_Release_v2.35\rk32-myzr-ubuntu.cfg文件

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.4.4.png
   :alt: My-rk32-ek314_download_3.4.4.png

**加载镜像**

|  点击“打勾”选项最右边的，对应选择绝对路径“rockdev\Image\android”或者“rockdev\Image\linux”相应的文件
   
|  android镜像：

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.4.2.png
   :alt: My-rk32-ek314_download_3.4.2.png

|  ubuntu镜像：

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.4.5.png
   :alt: My-rk32-ek314_download_3.4.5.png

烧写
------

|  板子接通5V电源,打开电源开关，按”SW4”按键，看到电源指示灯亮了，松开”SW4”按键，软件“AndroidTool.exe”会显示“发现一个LOADER设备”

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_4.1.1.png
   :alt: My-rk32-ek314_download_4.1.1.png

|  点击“执行”开始烧写,烧写完成，会自动重启系统（一般都是100%）

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_4.1.3.png
   :alt: My-rk32-ek314_download_4.1.3.png

批量烧写
----------

|  可以把android或ubuntu的相关镜像打包成relase_android_update.img或release_update.img
|  点击“固件”找到relase_android_update.img或release_update.img的绝对路径

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_4.1.5.png
   :alt: My-rk32-ek314_download_4.1.5.png

|  点击“升级”开始烧写（烧写前先操作，看到“发现一个LOADER设备”）

.. image:: /image/MYZR-瑞星微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_4.1.6.png
   :alt: My-rk32-ek314_download_4.1.6.png

