测试手册
========


RTC
---

+ 测试说明：RTC 测试需要安装纽扣电池，电池位置在丝印 BT1。

**功能测试**

+ **RTC时间**

  1）说明：设置RTC时间，之后断电重启后再核对RTC时间

  2）操作

    a）点击时钟APP，查看当前时钟：

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-clock-1.png
      :alt: image-RK3588-android12-clock-1.png

    b）断电重启设备。

    c）重新查看时钟：

    .. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-clock-2.png
      :alt: image-RK3588-android12-clock-2.png

  3）结果：执行操作后，核对 RTC 时间基本没有问题，且操作过程中的输出符合预期即功能正常。


网口
----

  + 接口丝印：J14（ETH1），J15（ETH2）
  + 系统接口：eth0（ETH1），eth1（ETH2）

**功能测试**

+ **网口一**

  1）说明：采用开发板向PC发送ICMP报文的方式进行测试

  2）操作

    a）配置电脑有线网卡IP为 192.168.137.99。

    b）把开发板的这个网口用网线跟电脑网口连接起来。

    c）执行网口测试命令

    + 输入指令：

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4

    + 输出信息：

    .. code-block:: text

      PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
      64 bytes from 192.168.137.99: icmp_seq-1 ttl-64 time-1.35 ms
      64 bytes from 192.168.137.99: icmp_seq-2 ttl-64 time-1.35 ms

      --- 192.168.137.99 ping statistics ---
      2 packets transmitted, 2 received, 0% packet loss, time 1002ms
      rtt min/avg/max/mdev - 1.347/1.347/1.348/0.000 ms

  3）结果：“0% packet loss”表示测试通过。

+ **网口二**

  1）说明：采用开发板向PC发送ICMP报文的方式进行测试

  2）操作

    a）配置电脑有线网卡IP为 192.168.137.99。

    b）把开发板的这个网口用网线跟电脑网口连接起来。

    c）执行网口测试命令

    + 输入指令：

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4

    + 输出信息：

    .. code-block:: text

      PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
      64 bytes from 192.168.137.99: icmp_seq-1 ttl-64 time-0.595 ms
      64 bytes from 192.168.137.99: icmp_seq-2 ttl-64 time-0.843 ms

      --- 192.168.137.99 ping statistics ---
      2 packets transmitted, 2 received, 0% packet loss, time 1001ms
      rtt min/avg/max/mdev - 0.595/0.719/0.843/0.124 ms

  3）结果：“0% packet loss”表示测试通过。



U盘连接
---------

+ 接口丝印：P2、P3、J3

**功能测试**

|  1）说明：采用插拔USB存储设备（U盘）的方式进行测试

|  2）操作：

|    a）将U盘插入底板USB接口

|    b）下拉框通知信息出现U盘信息

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-USB-1.png
  :alt: image-RK3588-android12-USB-1.png    

|    c）需要拔出U盘点击弹出按钮即可。


鼠标键盘连接
--------------

+ 接口丝印：P2、P3、J3

**功能测试**

|  1）操作：

|    a）将鼠标接口插入P2或P3或J3 usb接口，键盘接口插入P2或P3或J3 usb接口

|    b）点击搜索栏，弹出键盘，测试鼠标键盘是否可用。

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-USB-2.jpg
  :alt: image-RK3568-android11-USB-2.jpg    


图片查看
--------

**功能测试**

|  1）操作：

|    a）U盘中放入图片，并接上U盘

|    b）在资源管理器 》USB 中进入U盘目录

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-picture-1.jpg
  :alt: image-RK3568-android11-picture-1.jpg 

|    c）打开图片

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-picture-2.jpg
  :alt: image-RK3568-android11-picture-2.jpg 


播放音频
--------

**功能测试**

|  1）操作：

|    a）U盘中放入音频文件，并接上U盘

|    b）在资源管理器 》USB 中进入U盘目录

|    c）打开音频文件

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-music-1.jpg
  :alt: image-RK3568-android11-music-1.jpg


播放视频
--------

**功能测试**

|  1）操作：

|    a）U盘中放入音频文件，并接上U盘

|    b）在资源管理器 》USB 中进入U盘目录

|    c）打开视频频文件

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-movies-1.jpg
  :alt: image-RK3568-android11-movies-1.jpg


TF卡
-------

+ 接口丝印：J5

**功能测试**

|  1）说明：插入 TF 卡，观察设备能否正确识别到卡。

|  2）操作：

|    a）用一张 TF 卡，插入到设备的 TF 卡接口。

|    b）下拉框通知信息出现TF卡信息

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-TFcard-1.png
  :alt: image-RK3588-android12-TFcard-1.png  

|    c）需要拔出TF卡点击弹出按钮即可。


红外
------

+ 接口丝印：IR1

**功能测试**

  1）说明：通过接收红外信息，打印出相应数据。

  2）操作

    a）准备一个红外遥控器，或手机的红外遥控app。

    b）开发板打开相关打印开关：

    .. code-block:: text

      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/code_print
      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/dbg_level

    c）使用遥控器对准红外接口按下任意按钮

    d）开发板看到返回相关按钮信息即为成功接收到。


M2硬盘
-----------

+ 接口丝印：J21

**功能测试**

  1）接上M2硬盘

  2）启动开发板。
  
  3）输入如下命令查看pci总线设备：

  .. code-block:: shell

    lspci

  输出

  .. code-block:: shell

    01:00.0 Class 0108: 126f:2263
    00:00.0 Class 0604: 1d87:3588


  4）系统会自动挂载硬盘

  5）查看挂载情况

  .. code-block:: shell

    df -h

  6）可看到如下类似信息

  .. code-block:: shell

    /dev/block/vold/public:259,1 119G 108M  119G   1% /mnt/media_rw/BC98ABC698AB7E10
    /dev/fuse                    119G 108M  119G   1% /mnt/user/0/BC98ABC698AB7E10

  7）界面查看：在资源管理中可看到 USB 文件夹，此文件夹即为硬盘挂载目录。其操作与U盘类似


sata硬盘
-----------

+ 接口丝印：J18、J2

**功能测试**

  1）接上sata硬盘

  2）启动开发板。
  
  3）系统会自动挂载硬盘

  4）查看挂载情况

  .. code-block:: shell

    df -h

  5）可看到如下

  .. code-block:: shell

    /dev/block/vold/public:8,1 932G  15G  916G   2% /mnt/media_rw/863AAAA43AAA912B
    /dev/fuse                  932G  15G  916G   2% /mnt/user/0/863AAAA43AAA912B

  6）界面查看：在资源管理中可看到 USB 文件夹，此文件夹即为硬盘挂载目录。其操作与U盘类似


WIFI
-------

+ 接口丝印：U27

**功能测试**

|  1）操作：

|    a）把WIFI天线连接到“ANT2/ANT1”接口上

|    b）桌面中点击“设置” 》“网络与互联网” 》“互联网”

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-wifi-1.png
  :alt: image-RK3588-android12-wifi-1.png

|    c）选择wifi，输入密码进行连接

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-wifi-2.png
  :alt: image-RK3588-android12-wifi-2.png

|    d）连成功后可进行网站浏览测试

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-wifi-3.png
  :alt: image-RK3588-android12-wifi-3.png


蓝牙
-------

+ 接口丝印：U27

**功能测试**

|  1）操作：

|    a）把WIFI天线连接到“ANT2/ANT3”接口上

|    b）下拉框长按蓝牙，进入蓝牙设置界面

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-BL-1.png
  :alt: image-RK3588-android12-BL-1.png

|    c）点击“与新设置匹配”

|    d）选择手机或其它蓝牙设备进行匹配

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-BL-2.png
  :alt: image-RK3588-android12-BL-2.png

|    e）与蓝牙耳机成功匹配后，会显示使用中

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-BL-3.png
  :alt: image-RK3588-android12-BL-3.png


5G
-------

+ 接口丝印：J19

**功能测试**

|  1）接上5G模块RM500Q，接上5G天线和SIM卡

|  2）启动开发板。

|  3）可看到右上角有5G图片出现

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-android11-5g-1.jpg
  :alt: image-RK3568-android11-5g-1.jpg

  4）可进行网站浏览测试

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-android12-5g-2.png
  :alt: image-RK3588-android12-5g-2.png



















--------------------------------------------------------------------------------

::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2023/4/26
   * Supporter: Kuangwh
   --------------------------------------------------------------------------------

