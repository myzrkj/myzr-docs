MYZR-SSD20X-CB096 编译参考手册
===============================

相关文件介绍
--------------

- gcc-arm-8.2-2018.08-x86_64-arm-linux-gnueabihf.tar.xz：交叉编译工具
- kernel-release20220221.tar.bz2：内核源码
- boot-release20220221.tar.bz2：uboot源码
- project-release20220221.tar.bz2：与镜像打包，文件系统等相关的源码
- sdk.tar.bz2：sdk工具包

安装和配置交叉编译工具
----------------------

1. 创建一个目录用于存放sigmastar所有相关文件

.. code-block:: shell

   mkdir sigmastar
   cd sigmastar/

2. 解压交叉编译工具压缩包

.. code-block:: shell

   tar xvf gcc-arm-8.2-2018.08-x86_64-arm-linux-gnueabihf.tar.xz

3. 添加交叉编译工具链的环境变量

.. code-block:: shell

   export PATH=~/my-work/sigma/source/gcc-arm-8.2-2018.08-x86_64-arm-linuxgnueabihf/bin:$PATH

4. 检查交叉编译工具链

.. code-block:: shell

   arm-linux-gnueabihf-gcc -v

编译uboot
-----------

1. 解压uboot源码压缩包

.. code-block:: shell

   $ tar jxvf boot-release*.tar.bz2
   $ cd boot/

2. 配置编译环境

.. code-block:: shell

   $ declare -x ARCH="arm"
   $ declare -x CROSS_COMPILE="arm-linux-gnueabihf-"
   $ make infinity2m_spinand_defconfig

3. 编译

.. code-block:: shell

   #首次编译先清除配置
   $ make clean
   #编译
   $ make -j8

4. 将镜像复制到一个目录中

.. code-block:: shell

   #在sigmastar目录下创建一个专门用于存放镜像的目录
   $ mkdir ../release_image
   #将镜像复制到release_image目录中
   $ cp u-boot_spinand.xz.img.bin ../release_image/

编译kernel
------------

1. 解压kernel源码压缩包

.. code-block:: shell

   $ cd ../
   $ tar jxvf kernel-release*.tar.bz2
   $ cd kernel/

2. 配置编译环境

.. code-block:: shell

   $ declare -x ARCH="arm"
   $ declare -x CROSS_COMPILE="arm-linux-gnueabihf-"

3. 编译

.. code-block:: shell

   #首次编译先清除配置
   $ make clean
   #编译
   $ make -j8

4. 将镜像复制到一个目录中

.. code-block:: shell

   #将镜像复制到release_image目录中
   $ cp arch/arm/boot/uImage.xz ../release_image/

编译project
-------------

1. 解压project源码压缩包

.. code-block:: shell

   $ cd ../
   $ tar -jxvf project-release*.tar.bz2
   $ cd project/

2. 配置编译环境(第一次编译时需要配置，后面project目录无改动或重命名的话无需配置)

.. code-block:: shell

   ./setup_config.sh ./configs/nvr/i2m/8.2.1/spinand.glibc.011a.128

3. 编译

.. code-block:: shell

   #首次编译先清除配置
   $ make clean
   #编译
   $ make image
   $ tar cjvf ../release_image/image.tar.bz2 image/output/images/*