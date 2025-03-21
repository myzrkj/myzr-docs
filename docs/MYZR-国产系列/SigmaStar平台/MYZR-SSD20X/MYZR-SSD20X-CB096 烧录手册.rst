MYZR-SSD20X-CB096 烧录手册
============================

使用网口网线烧录
-----------------

1. 在windows下创建一个文件夹来存放即将要烧录的镜像
2. 将release_image目录下的image.tar.bz2拷贝到windows下解压到新建文件夹下
3. 将文件夹下的kernel删除或重命名为kernel.bak，将release_image目录下的uImage.xz拷贝到文件夹下，并且改名为kernel
4. 将文件夹下的uboot_s.bin删除或改名为uboot_s.bin.bak，将release_image目录下的uboot_spinand.xz.img.bin拷贝到文件夹下，并且改名为uboot_s.bin

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-CB096_Burning_01.png
   :alt: MYZR-SSD20X-CB096_Burning_01.png

5. 使用网线连接开发板的网口P2和电脑的网口
6. 使用串口转USB连接开发板和电脑，打开终端软件串口会话，为开发板连接电源线，然后上电
7. 配置windows的有线ip例如：192.168.137.99
8. 打开tftp服务器，Current Directory选择镜像文件夹目录，选择Server interfaces：192.168.137.99

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-CB096_Burning_02.png
   :alt: MYZR-SSD20X-CB096_Burning_02.png

9. 在终端软件中的会话里的uboot启动阶段，敲击Enter回车键进入到uboot命令行
10. 配置uboot烧录环境

.. code:: shell

   # windows ip
   setenv serverip 192.168.137.99
   # uboot ip
   setenv ipaddr 192.168.137.81
   saveenv
   # 烧录镜像
   estar

|  等待，直到开启kernel，即烧录成功。