MYZR-SSD20X-CB096 Linux-4.9.84 Build Reference Manual
========================================================

Introduction to related documents
------------------------------------

- gcc-arm-8.2-2018.08-x86_64-arm-linux-gnueabihf.tar.xz：cross-compilation tool
- kernel-release20220221.tar.bz2：kernel source code
- boot-release20220221.tar.bz2：uboot source code
- project-release20220221.tar.bz2：source code related to image packaging, file systems, etc
- sdk.tar.bz2：sdk.tar.bz2:sdk toolkit

Install and configure the cross-compilation tool
---------------------------------------------------

1. Create a directory for all sigmastar related files

.. code-block:: shell

   mkdir sigmastar
   cd sigmastar/

2. Unzip the cross-compilation tool package

.. code-block:: shell

   tar xvf gcc-arm-8.2-2018.08-x86_64-arm-linux-gnueabihf.tar.xz

3. Add environment variables for the cross-compilation toolchain

.. code-block:: shell

   export PATH=~/my-work/sigma/source/gcc-arm-8.2-2018.08-x86_64-arm-linuxgnueabihf/bin:$PATH

4. Check the cross-compilation toolchain

.. code-block:: shell

   arm-linux-gnueabihf-gcc -v

Compile uboot
---------------

1. Unzip the uboot source code package

.. code-block:: shell

   $ tar jxvf boot-release*.tar.bz2
   $ cd boot/

2. Configure the compilation environment

.. code-block:: shell

   $ declare -x ARCH="arm"
   $ declare -x CROSS_COMPILE="arm-linux-gnueabihf-"
   $ make infinity2m_spinand_defconfig

3. Compile

.. code-block:: shell

   #Clear the configuration for the first compilation
   $ make clean
   #Compile
   $ make -j8

4. Copy the image to a directory

.. code-block:: shell

   #Create a directory dedicated to storing images in the sigmastar directory
   $ mkdir ../release_image
   #Copy the image to the release_image directory
   $ cp u-boot_spinand.xz.img.bin ../release_image/

Compile the kernel
--------------------

1. Unzip the kernel source code package

.. code-block:: shell

   $ cd ../
   $ tar jxvf kernel-release*.tar.bz2
   $ cd kernel/

2. Configure the compilation environment

.. code-block:: shell

   $ declare -x ARCH="arm"
   $ declare -x CROSS_COMPILE="arm-linux-gnueabihf-"

3. Compile

.. code-block:: shell

   #首次编译先清除配置
   $ make clean
   #编译
   $ make -j8

4. Copy the image to a directory

.. code-block:: shell

   #将镜像复制到release_image目录中
   $ cp arch/arm/boot/uImage.xz ../release_image/

Compile the project
---------------------

1. Unzip the project source code package

.. code-block:: shell

   $ cd ../
   $ tar -jxvf project-release*.tar.bz2
   $ cd project/

2. Configure the compilation environment (you need to configure it when you compile it for the first time, and you don't need to configure it if there is no change or renaming of the project directory later)

.. code-block:: shell

   ./setup_config.sh ./configs/nvr/i2m/8.2.1/spinand.glibc.011a.128

3. Compile

.. code-block:: shell

   #Clear the configuration for the first compilation
   $ make clean
   #Compile
   $ make image
   $ tar cjvf ../release_image/image.tar.bz2 image/output/images/*