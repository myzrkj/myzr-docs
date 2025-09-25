MYZR-SAMA5 Linux-3.18 RTL8188EU 开发指导
==========================================

准备源码
---------

下载源码包
~~~~~~~~~~~

|   在网盘下载 rtl8188EUS_linux_v4.3.0.9_15178.20150907.tar.xz

解压源码包
~~~~~~~~~~~

**创建工作目录**

|   这里我们创建 ~/my-demo/exclude_src 目录，并在该目录下工作。

.. code-block:: shell

    $ mkdir ~/my-demo/exclude_src -p

**复制源码包到工作目录**

|   将下载的源码包复制到 ~/my-demo/exclude_src 。
|   这一步自己采取相应方式完成。

**解压源码**

- 进入源码目录

.. code-block:: shell

    $ cd ~/my-demo/exclude_src

- 解压

.. code-block:: shell

    $ tar xf rtl8188EUS_linux_v4.3.0.9_15178.20150907.tar.xz

编译模块
----------

检查配置
~~~~~~~~~

|   说明：模块编译存在两个依赖关系，交叉编译编译链和内核，并且需要在指定路径。

- 使编译配置文件生效

.. code-block:: shell

    $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/Myimx6linux3.14_build_5.2.1.1.png
   :alt: Myimx6linux3.14_build_5.2.1.1.png

- 检查内核源码路径

.. code-block:: shell

    $ ls ~/my-sama5/02_source/linux-at91-linux4sam_4.7

|   如果内核源码存在并且路径正确会看到内核源码目录的内容。
|   如果命令的执行结果异常，需要按照《MYZR-SAMA5 L318 编译手册》重新编译一次内核。

编译
~~~~~~

- 进入驱动代码目录

.. code-block:: shell

    $ cd rtl8188EUS_linux_v4.3.0.9_15178.20150907/

- 执行编译命令

.. code-block:: shell

    $ make

目标文件
~~~~~~~~~

- 查看目标文件信息

.. code-block:: shell

    $ file *.ko

|   执行 file 命令可以看到编译出来的模块的信息，类似如下：
|   8188eu.ko: ELF 32-bit LSB relocatable, ARM, version 1 (SYSV), BuildID[sha1]=0x1a3bbb865d785effc8acfebf9e2c8faf066b3fbf, not stripped
|   8188eu.ko 即编译得到的目标文件

WIFI测试
----------

见 :doc:`《MYZR-SAMA5 Linux-3.18 测试手册》<MYZR-SAMA5 Linux-3.18 测试手册>` 