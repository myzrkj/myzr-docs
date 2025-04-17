
MYZR-A40I-CB204 烧录手册
=========================

A40I烧写
---------

|  安装 PhoenixSuit 解压 PhoenixSuit.zip，运行 PhoenixSuit_CN.msi

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-A40I-EK204/PhoenixSuit_01.png
  :alt: MY-R16-PhoenixSuit_01

|  点击下一步，下一步，提示安装 Device Driver ，点击下一步安装，直到安装完成，点击关闭。


USB 升级开发板固件
------------------

|  打开 PhoenixSuit 软件，选择一键刷机，点击浏览选择固件。

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-A40I-EK204/PhoenixSuit_02.png
  :alt: MY-R16-PhoenixSuit_02

|  刷机步骤，请严格按步骤 1~5 顺序来操作(步骤不能颠倒)：

1. 打开 usb 刷机软件 PhoenixSuit。
2. 选择“一键刷机”页面，点击“浏览”加载好固件。
3. 按住开发板 MENU 或者 BOOT 按钮不放。
4. 插入开发板电源，打开开发板电源开关。
5. 使用 otg 线连接开发板和电脑，刷机软件自动提示升级（说明：这个步骤正常了刷机软件会提示“开始刷机”，如果刷机软件没有任何反应，请检查步骤 1~4 是否正确，这个过程中刷机软件左下角会一直提示“无设备连接！！！”，请忽略）。
6. 松开 MENU 或者 BOOT 按钮。

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-A40I-EK204/PhoenixSuit_03.png
  :alt: PhoenixSuit_03.png

|  点击 “是”，选择强制格式化（没有任何程序的裸板第一次升级或者原本系统是 linux、ubuntu 等升级 android 系统需要选择强制格式化），板子开始升级，直至升级完成。升级完成，开发板自动启动系统。