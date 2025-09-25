MYZR-IMX28-EK142 启动手册
===========================

串口的配置如下
---------------

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/MY_IMX283_1.png
   :alt: MY_IMX283_1.png

开机准备
----------

- 针对MYZR-I.MX28-DEMO-V3.1版本

|   1）拿到评估板之后 ，如果有7寸液晶，将液晶接到RGB液晶接口接到4.3寸液晶下面的接插件。
|   2）将4位拨码开关拨到1：OFF，2：OFF，3：ON，4：OFF(NandFlash启动)
|   3）如果是SD卡启动，1：ON，2：OFF，3：OFF，4：ON
|   4）将串口线公头插入到调试串口(DEBUG UART)位置，另一头连接电脑。将MINIUSB线一端插到电脑，一端插到DEMO板 MINI USB 口处，或者5V电源插入到电源插孔(DC-5V-IN)处，此时串口上面有系统正常启动的log信息。

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/969px-IMX28_DEMO_front.jpg
   :alt: 969px-IMX28_DEMO_front.jpg