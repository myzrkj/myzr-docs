
MYZR-RK3288-EK314 MfgTool User Guide
=====================================

Applicable scope
------------------

**The operating system of evaluation board**

+-------------------+--------------------------+-----+-----+
| Evaluation board  | Supported Linux versions             |
+                   +--------------------------+-----+-----+
|                   | Linux-3.10.79            | NC  | NC  |
+-------------------+--------------------------+-----+-----+
| MYZR-RK3288-EK314 | √                        |     |     |
+-------------------+--------------------------+-----+-----+


+-------------------+--------------------------------+-----+-----+
| Evaluation board  | Android System version support             |
+                   +--------------------------------+-----+-----+
|                   | Android-5.1.1                  | NC  | NC  |
+-------------------+--------------------------------+-----+-----+
| MYZR-RK3288-EK314 | √                              |     |     |
+-------------------+--------------------------------+-----+-----+

**Operating system VS file system**

   | Because Linux OS correspond Multiple file system,the following table can support Correspondence:                                                                                                                                                                                                                 |
   | In addition，the size of file system is very big,the minimal file system is only 6.9MB,big file system up to 1GB.In order to save everyone's download time, we first according to the table below the pre-selected file system, in the download file system that step can only download the file systemyou need. |

+------------------+-----------------------+-----------------------+-----------------------------------------------+
| Operating system | File system                                                                                   |
+                  +-----------------------+-----------------------+-----------------------------------------------+
|                  | File system file name | File system file size | File system description                       |
+==================+=======================+=======================+===============================================+
| linux-3.10.79    | linux-rootfs.img      | 1.25GB                | Ubuntu14.04 system file for MYZR-RK3288-EK314 |
+------------------+-----------------------+-----------------------+-----------------------------------------------+
| Android-5.1.1    | system-ard511.img     | 440MB                 | Android 5.1.1 File system                     |
+------------------+-----------------------+-----------------------+-----------------------------------------------+


Prepare MFG Tool
-----------------

**Contents of MFG Tool**

|  In order to easy to understand MFG Tool ，below have a explanation about MFG Tool.

.. code-block:: shell
   
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
   


Configurate MFG Tool
--------------------

**Configuration instructions**

|  File name：AndroidTool_Release_v2.35.rar


**Configuration instructions**

|  Precompiled folder： Image


Configurate MFG Tool
--------------------

**Unzip AndroidTool_Release_v2.35.rar**

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.1.1.png
   :alt: My-rk32-ek314_download_3.1.1.png

**Copy the downloaded Image to the appropriate directory**

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.2.1.png
   :alt: My-rk32-ek314_download_3.2.1.png

**Install driver**

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.2.1.png
   :alt: My-rk32-ek314_download_3.2.1.png

**Import the configuration**

| 1）Import Android configuration

- Method One

|  Double-click “AndroidTool.exe”

- Method TWO

|  After opening“AndroidTool.exe”，right-click "import configuration" and find the directory AndroidTool_Release_v2.35\config.cfg file.

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.4.1.png
   :alt: My-rk32-ek314_download_3.4.1.png

|  2）Import ubuntu configuration
|  After opening“AndroidTool.exe”，right-click "import configuration" and find the directory AndroidTool_Release_v2.35\rk32-myzr-ubuntu.cfg file

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.4.4.png
   :alt: My-rk32-ek314_download_3.4.4.png

**Load image**

|  Clicking on the far right of the "tick" option corresponds to selecting the corresponding file of the absolute path "rockdev Image\android" or "rockdev Image\ Linux" 
|  Android image：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.4.2.png
   :alt: My-rk32-ek314_download_3.4.2.png

|  ubuntu image：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_3.4.5.png
   :alt: My-rk32-ek314_download_3.4.5.png

Configurate MFG Tool
--------------------

| The board is connected to the 5V power supply, turn on the power switch, directly press the “RECOVERY” button, then press the “SW3” button, and see that the power indicator light is on, first release the “SW3” button, then release the “RECOVERY” button, the software "AndroidTool.exe" will display "Discover a LOADER device"

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_4.1.1.png
   :alt: My-rk32-ek314_download_4.1.1.png

| Click "execute" to start writing, and when the writing is finished, the system will be restarted automatically (usually 100%).

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_4.1.3.png
   :alt: My-rk32-ek314_download_4.1.3.png


Bulk burning
------------

| You can package the relevant image of android or ubuntu into relase_android_update.img or release_update.img
| Click "firmware" to find relase_android_update.img or release_update.img absolute path

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_4.1.5.png
   :alt: My-rk32-ek314_download_4.1.5.png

| Click "Upgrade" to start programming (before burning, see "Discover a LOADER device")

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314_download_4.1.6.png
   :alt: My-rk32-ek314_download_4.1.6.png

