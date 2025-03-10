
MYZR-RZ-EK200 烧录手册
=======================

|  烧录的方法有多种，不同的镜像对应的烧录方式也不一样，本篇内容将介绍多种镜像烧录方式，用户可以根据开发的项目条件选择其中的一种或多种方式进行镜像更新。

mytool烧录
------------

**此方法仅用于更新uboot镜像，也是当前版本uboot镜像的唯一更新方式。**

|  软件压缩包在MYZR-RZ -> 05其它 ->mytool.rar。将压缩包解压，进入mytool文件夹。
|  双击打开mytool.exe

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/Mytool_1.png
   :alt: Mytool_1.png

|  点击Browse按钮选择镜像存放的目录(MYZR-RZ -> 01_烧录 -> rzg2l/rzg2ul/rzfive 文件夹)，以烧录rzg2l为例

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/Mytool_2.png
   :alt: Mytool_2.png

|  保证开发板连接好串口线，选择COM口，点击Connect按钮。（需保证开发板的COM口不在其它软件中打开）

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/Mytool_3.png
   :alt: Mytool_3.png

|  保证开发boot启动拨码设置为烧录模式，重新给开发板上电或按下开发板复位按键。mytool上方文本窗口显示出“SCIF Download mode”字样。

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/Mytool_4.png
   :alt: Mytool_4.png

|  点击One-key operation按钮进行烧录即可。
|  也可以不使用一键操作按钮，先点击Loading mot按钮进行加载，再点击Writing uboot烧录即可。bl2是出厂固件，一般不需要进行更新。烧录完成点击Disconnect按钮断开连接。

TF卡烧录
----------

**tf卡烧录可用于更新内核，设备树，文件系统。此方法镜像更新全面，且后期操作简单，用于生产阶段的烧录**

|  tf卡要求：保证tf卡有一个分区1,分区1内存大于所有烧录镜像的内存
|  tf卡通过读卡器接入电脑，并将如下镜像拷贝到tf卡中。镜像目录（MYZR-RZ -> 01_烧录 -> rzg2l/rzg2ul/rzfive 文件夹）

+--------+----------+----------------------------------------------------+
| 型号   | 镜像     | 镜像名称                                           |
+========+==========+====================================================+
| rzg2l  | 内核     | Image                                              |
+        +----------+----------------------------------------------------+
|        | 设备树   | myzr-rzg2l-dsi.dtb                                 |
+        +          +                                                    +
|        |          | myzr-rzg2l-rgb.dtb                                 |
+        +----------+----------------------------------------------------+
|        | 文件系统 | core-image-qt-myzr-rzg2l-Release.xxx.tar.bz2       |
+        +----------+----------------------------------------------------+
|        | ramdisk  | core-image-mini-myzr-rzg2l-mod.cpio.gz.uboot       |
+--------+----------+----------------------------------------------------+
| rzg2ul | 内核     | Image                                              |
+        +----------+----------------------------------------------------+
|        | 设备树   | myzr-rzg2ul-eth.dtb                                |
+        +          +                                                    +
|        |          | myzr-rzg2ul-lcd.dtb                                |
+        +----------+----------------------------------------------------+
|        | 文件系统 | core-image-bsp-myzr-rzg2ul-Release.xxx.tar.bz2     |
+        +----------+----------------------------------------------------+
|        | ramdisk  | core-image-mini-myzr-rzg2ul-mod.cpio.gz.uboot      |
+--------+----------+----------------------------------------------------+
| rzfive | 内核     | Image                                              |
+        +----------+----------------------------------------------------+
|        | 设备树   | myzr-rzfive-2g.dtb                                 |
+        +----------+----------------------------------------------------+
|        | 文件系统 | core-image-minimal-myzr-rzfive-Release.xxx.tar.bz2 |
+        +----------+----------------------------------------------------+
|        | ramdisk  | core-image-minimal-myzr-rzfive-mod.cpio.gz.u-boot  |
+--------+----------+----------------------------------------------------+

**其中文件系统名称需要把版本号去掉，即重命名为（core-image-qt-myzr-rzg2l.tar.bz2）**

|  将tf卡插入板子tf卡接口，启动板子进入uboot命令行模式：

.. code:: shell

   U-Boot 2021.10 (Feb 07 2023 - 11:36:41 +0800)

   CPU:   Renesas Electronics K rev 16.15
   Model: myzr-rzg2l
   DRAM:  1.9 GiB
   MMC:   sd@11c00000: 0, sd@11c10000: 1
   Loading Environment from MMC... OK
   In:    serial@1004b800
   Out:   serial@1004b800
   Err:   serial@1004b800
   Net:   
   Error: ethernet@11c20000 address not set.
   No ethernet found.

   Hit any key to stop autoboot:  0 
   =>

|  输入如下命令从tf卡中启动系统：

.. code:: shell

   => setenv startup_mode sd
   => boot

|  系统启动后输入命令进行镜像更新

.. code:: shell

   # ./sdupdate.sh

|  等待烧录完成后，显示“sdcard update succeed !!!”。重启即可完成更新。

替换镜像更新
-------------

**此方法可单独更新内核和设备树镜像，适合开发调试阶段。**

1. 开发板启动后，输入如下命令对emmc的分区一进行挂载：

.. code:: shell

   # mount /dev/mmcblk0p1 /mnt/

2. 进入挂载目录/mnt，删除原本的镜像
3. 再把新的镜像拷贝到此目录
4. 使用命令卸载并重启即可

.. code:: shell

   # umount /mnt/