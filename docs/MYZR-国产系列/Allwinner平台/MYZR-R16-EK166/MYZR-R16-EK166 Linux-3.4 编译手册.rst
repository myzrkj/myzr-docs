
MYZR-R16-EK166 linux-3.4 编译手册
==================================


环境搭建
----------

|  在这里建议用户使用64bit的ubuntu12.04的操作系统，已经真机编译验证过。
|  ubuntu14.04下编译会报错。

下载源码包
----------

|  下载文件tina.tar.bz2

解压源码包
-----------

.. code-block:: shell
   
   $ tar -jxvf tina.tar.bz2

|  解压完成后会有一个名为tinaV2.1的目录。

编译
------

设置平台信息
~~~~~~~~~~~~~

.. code-block:: shell
   
   $ cd ~/tinaV2.1
   $ source build/envsetup.sh
   $ lunch astar_parrot-tina
   $ make kernel_menuconfig
   ### make kernel_menuconfig打开后退出即可，会自动生成.config文件。

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_d&d4-1.png
   :alt: MY-R16-CB166_linux-34_d&d4-1.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_d&d4-2.png
   :alt: MY-R16-CB166_linux-34_d&d4-2.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_d&d4-3.png
   :alt: MY-R16-CB166_linux-34_d&d4-3.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_d&d4-4.png
   :alt: MY-R16-CB166_linux-34_d&d4-4.png


编译Uboot
~~~~~~~~~~~

.. code-block:: shell

   $ cd lichee/brandy/u-boot-2011.09
   $ make distclean
   $ make sun8iw5p1_config
   $ make

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_d&d4-5.png
   :alt: MY-R16-CB166_linux-34_d&d4-5.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_d&d4-6.png
   :alt: MY-R16-CB166_linux-34_d&d4-6.png

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_d&d4-7.png
   :alt: MY-R16-CB166_linux-34_d&d4-7.png


编译系统跟内核
~~~~~~~~~~~~~~~

.. code-block:: shell

   $ cd ~/tinaV2.1/
   $ make

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_d&d4-8.png
   :alt: MY-R16-CB166_linux-34_d&d4-8.png

打包
~~~~~~

.. code-block:: shell

   $ cd ~/tinaV2.1
   $ pack

.. image:: /image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_d&d5-1.png
   :alt: MY-R16-CB166_linux-34_d&d5-1.png

| 打包生成的最终文件在 ``~/tinaV2.1/out/astar-parrot/`` 目录下的 ``tina_astar-parrot_uart0.img``
| 将该文件复制到电脑上就可以烧写到开发板上。烧写请参考 :doc:`./MYZR-R16-EK166 烧录指导手册`


::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2023/5/08  
   * Supporter: Zhong JiaYi
   --------------------------------------------------------------------------------