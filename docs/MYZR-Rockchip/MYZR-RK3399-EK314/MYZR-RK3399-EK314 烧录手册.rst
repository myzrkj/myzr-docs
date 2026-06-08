MYZR-RK3399-EK314 烧录手册
===========================

下载烧录工具
-------------

|   下载烧录工具压缩包：AndroidTool_Release_v2.58.zip 解压AndroidTool_Release_v2.58.zip

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.1.png
   :alt: My-rk3399-ek314_download_3.1.1.png

下载usb驱动
------------

|   下载usb驱动压缩包：DriverAssitant_v4.5.rar 安装解压DriverAssitant_v4.5.rar

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.2.png
   :alt: My-rk3399-ek314_download_3.1.2.png

|   双击红色箭头文件打开烧录工具

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.3.png
   :alt: My-rk3399-ek314_download_3.1.3.png

烧写说明
---------

- 若要烧写所有镜像的统一固件，则跳到“烧写同一固件”那一节中操作。
- 若要单独烧写内核，u-boot或文件系统，则跳到“单独烧写内核，u-boot或文件系统”那一节中操作。

烧写统一固件
-------------

- 点击升级固件
- 点击“固件”选择要烧录的固件
- 使用usb数据线连接开发板和电脑
- 长按开发板的vol+按键，打开开发板电源，在烧写工具出现“发现一个LOADER设备”时松开vol+按键
- 点击升级进行烧写

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.4.png
   :alt: My-rk3399-ek314_download_3.1.4.png

**注意**

|   从android系统烧录成ubuntu系统要先擦除Flash后才能烧写，从ubuntu系统烧录成android系统也要先进行擦除再烧写


单独烧写内核，u-boot或文件系统
------------------------------

- 点击下载镜像
- 在表格位置右击选择导入配置，选择配置文件，配置文件在烧写工具根目录。rk3399-config.cfg是ubuntu16.04的配置，rk3399-android81.cfg是android8.1的配置
- 导入配置后在需要烧写的镜像前的勾选上

.. code-block:: shell
    
    Loader：MiniLoaderAll.bin
    Parameter：parameter.txt
    Uboot：uboot.img
    Trust：trust.img
    Boot：boot.img
    Rootfs：rootfs.img

- 用usb数据线连接开发板与电脑
- 长按开发板的vol+按键，打开开板电源，直到烧写工具出现“发现一个LOADER设备”时松开vol+按键
- 点击执行开始烧写

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3399-EK314/My-rk3399-ek314_download_3.1.5.png
   :alt: My-rk3399-ek314_download_3.1.5.png