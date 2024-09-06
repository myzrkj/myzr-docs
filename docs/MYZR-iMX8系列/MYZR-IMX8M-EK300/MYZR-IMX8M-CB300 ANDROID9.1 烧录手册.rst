MYZR-IMX8M-CB300 ANDROID9.1 烧录手册
======================================

下载烧写工具
-------------

|  在百度网盘下相应的烧写工具

烧写
------

**打开管理员命令提示符窗口**

1. 点击电脑左下角的win图标
2. 找到windows系统选项
3. 右击命令提示符窗口
4. 点击更多
5. 点击以管理员身份运行

**进入烧写工具的存放目录**

|  例如烧写工具的存放路径为G:\imx8m\imx8mq-android-ek300-AP6398S

.. code-block:: shell

   # 进入G盘
   C:\Windows\system32> G:
   # 进入烧写工具目录
   G:\>cd imx8mq\imx8mq-android-ek300-AP6398S

**将开发板的sw1拨码开关拨到01的状态**

**用USB公对公烧写线将开发板j15USB接口与电脑usb接口相连接**

**在命令提示符窗口输入uuu_imx_android_flash.bat -f imx8mq -a -e开始烧写**

.. code-block:: shell

   G:\imx8mq\imx8mq-android-ek300-AP6398S>uuu_imx_android_flash.bat -f imx8mq -a -e