
MYZR-STM32MP15CubeProgrammer 烧录手册
======================================

STM32CubeProgrammer烧写
~~~~~~~~~~~~~~~~~~~~~~~~~

|  STM32CubeProgrammer是ST官网自带的烧录工具，可以在我们提供的网盘上进行下载 。网盘目录在01_烧录，将整个文件夹进行下载。

下载和安装
""""""""""""

1. 下载好后，在01_烧录->stm32Cubeprog目录下有一个压缩包和jdk，将压缩包解压，可以得到一个文件夹，一个exe文件和一个linux文件。

2. 先安装jdk-8u241-windows-x64.exe

- 双击jdk-8u241-windows-x64.exe，如图，点击下一步

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_1.png
   :alt: STM32CubeProgrammer_1.png

- 安装目录默认，点击下一步

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_2.png
   :alt: STM32CubeProgrammer_2.png

- 再点击下一步进行安装
- 安装完成，点击关闭

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_3.png
   :alt: STM32CubeProgrammer_3.png

3. 安装SetupSTM32CubeProgrammer-2.4.0.exe

- 双击SetupSTM32CubeProgrammer-2.4.0.exe，点击next

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_4.png
   :alt: STM32CubeProgrammer_4.png

- 点击next->next->I accept....->next直到安装目录，安装目录默认（注意不能带有中文路径）。

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_5.png
   :alt: STM32CubeProgrammer_5.png

- 默认配置项

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_6.png
   :alt: STM32CubeProgrammer_6.png

- 弹出另一个窗口，点击下一步继续安装，点击完成，再回到stm32CubeProgrammer窗口点击next。

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_7.png
   :alt: STM32CubeProgrammer_7.png

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_8.png
   :alt: STM32CubeProgrammer_8.png

- 点击Done完成安装

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_9.png
   :alt: STM32CubeProgrammer_9.png

烧录
""""""

1. 进入01_烧录->myzr-stm32mp1目录，将openstlinux-Release.xxx.rar压缩包进行解压（xxx为版本日期）。
2. 双击桌面STM32CubeProgrammer程序
3. 开发板连接烧录线，将拨码开关拨到烧录模式
4. 接上电源开发板上电
5. 按下图所示进行配置：先选择USB接口，再点击刷新（如果刷新不出USB Port按一下开发板复位按键），最后点击连接Connect。

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_10.png
   :alt: STM32CubeProgrammer_10.png

6. 连接成功后，点击Open file选择FlashLayout文件 （FlashLayout文件在烧录目录->myzr-stm32mp1->flashlayout_st-image-weston->trusted）。

 |  有四个FlashLayout **（FlashLayout_emmc_myzr-stm32mp15-256m-trusted.tsv**
 |  **FlashLayout_emmc_myzr-stm32mp15-512m-trusted.tsv**
 |  **FlashLayout_sdcard_myzr-stm32mp15-256m-trusted.tsv**
 |  **FlashLayout_sdcard_myzr-stm32mp15-512m-trusted.tsv）**
 |  根据自己的开发板选择。

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_11.png
   :alt: STM32CubeProgrammer_11.png

7. 点击Browse选择镜像所在根目录，如我的是在 **D:\stm32\烧录\myzr-stm32mp1**

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_14.png
   :alt: STM32CubeProgrammer_14.png

8. 点击Download按键进行烧录

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_15.png
   :alt: STM32CubeProgrammer_15.png