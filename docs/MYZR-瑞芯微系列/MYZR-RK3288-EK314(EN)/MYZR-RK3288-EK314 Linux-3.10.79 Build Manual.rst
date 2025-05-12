
MYZR-RK3288-EK314 Linux-3.10.79 Build Manual
=============================================


Prepare source code pacakge
----------------------------

3.10.79 version code
~~~~~~~~~~~~~~~~~~~~~~

**u-boot source code**

|   File name：rk32-myzr_uboot_2014.10_201803028.tar.bz2

**kernel source code**

|   File name：rk32-myzr_kernel_3.10_201803028.tar.bz2

**Cross compifer tool**

|   File name：gcc-arm-eabi-4.6.tar.bz2


Configuration of compifer environment
---------------------------------------

Prepare source code
~~~~~~~~~~~~~~~~~~~~~~

**Prepare source code package**

|   1）Create working directory
|   Ceate ~/my-rk3288 as working directory

.. code-block:: shell

    $ mkdir ~/my-rk3288

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.1.1.1.jpg
   :alt: My-rk32-ek314build_2.1.1.1.jpg

|   Ceate ~/my-rk3288/02_source as source code directory.

.. code-block:: shell

    $ mkdir ~/my-rk3288/02_source

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.1.1.2.jpg
   :alt: My-rk32-ek314build_2.1.1.2.jpg

|   Ceate ~/my-rk3288/03_tools as tool directory.

.. code-block:: shell
    
    $ mkdir ~/my-rk3288/03_tools

|   2）Copy source code package to the development host.
|   Do it in this step in your own way.

`Tips：this step is to copy “02_source code”from network disk to “~/my-rk3288/02_source”in development host, copy “03_tool”to “~/my-rk3288/03_tools, and copy “01_application”to “~/my-rk3288/01_application”。in development host`


**Decompress source code package**

|   1）Decompress u-boot source code and kernel source code.

.. code-block:: shell

    $ cd ~/my-rk3288/02_source
    $ tar jxf rk32-myzr_uboot_2014.10_201803028.tar.bz2
    $ tar jxf rk32-myzr_kernel_3.10_201803028.tar.bz2

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.1.2.1.jpg
   :alt: My-rk32-ek314build_2.1.2.1.jpg

|   2）Decompress cross compiler tool

.. code-block:: shell

    $ cd ~/my-rk3288/03_tools/
    $ tar jxf gcc-arm-eabi-4.6.tar.bz2

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.1.2.2.jpg
   :alt: MMy-rk32-ek314build_2.1.2.2.jpg


Development environment configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Install package needed**

|   1）List of updated source

.. code-block:: shell

    $ sudo apt-get update

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.1.jpg
   :alt: My-rk32-ek314build_2.2.1.1.jpg

|   After update,it will look like below：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.2.jpg
   :alt: My-rk32-ek314build_2.2.1.2.jpg

|   2）Install aptitude package management tool and ia32-libs

`Tips：If Linux of compiler host is 32bit，you can skip this step`

- Install aptitude package management tool

.. code-block:: shell

    $ sudo apt-get -y install aptitude

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.3.jpg
   :alt: My-rk32-ek314build_2.2.1.3.jpg

- Install ia32-libs with aptitude

.. code-block:: shell

    $ sudo aptitude -y install ia32-libs

`Tips：following is the screenshots with re-execution of installation command after installation of aptitude and ia32-libs is finished.`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.4.jpg
   :alt: My-rk32-ek314build_2.2.1.4.jpg


|   3）Install mkimage tool

.. code-block:: shell

    $ sudo apt-get -y install uboot-mkimage

`Tips：following is the screenshots with re-execution of installation command after installation of mkimage tool is finished.`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.5.jpg
   :alt: My-rk32-ek314build_2.2.1.5.jpg

|   4）Install ncurses-dev
|   Instruction：make menuconfig is dependent on it.

.. code-block:: shell

    $ sudo aptitude -y install ncurses-dev

`Tips：following is the screenshots with re-execution of installation command after installation of ncurses-dev tool is finished.`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_2.2.1.6.jpg
   :alt: My-rk32-ek314build_2.2.1.6.jpg


Compile u-boot
-----------------

Enter u-boot source code directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ cd ~/my-rk3288/02_source/rk32-myzr_uboot_2014.10/

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.1.1.jpg
   :alt: My-rk32-ek314build_3.1.1.jpg

Validate configured file
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Execute source command

.. code-block:: shell

    $ source ~/my-rk3288/03_tools/gcc-arm-eabi-4.6-env

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.2.1.jpg
   :alt: My-rk32-ek314build_3.2.1.jpg

- View compiler configuration

.. code-block:: shell

    $ echo $ARCH
    $ echo $CROSS_COMPILE

`Tips：you can see that ARCH和CROSS_COMPILE is configured`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.2.2.jpg
   :alt: My-rk32-ek314build_3.2.2.jpg

- Verify cross compiler tool configuration

.. code-block:: shell

    $ ${CROSS_COMPILE}gcc –v

`Tips：you can see version information of cross compiler tool shown on terminal after execution of command.as below：`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.2.3.jpg
   :alt: My-rk32-ek314build_3.2.3.jpg


Remove u-boot configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ make distclean

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.3.1.jpg
   :alt: My-rk32-ek314build_3.3.1.jpg


u-boot configuration
~~~~~~~~~~~~~~~~~~~~~~

- Evaluation board and its corresponding u-boot compiler configuration：

+-----------------------------+--------------------------+------------------------------------+
| Evaluation board main model | CPU type-memory capacity | Corresponding u-boot configuration |
+=============================+==========================+====================================+
| MYZR-RK3288-EK314           | RK3288（quad. core）- 2G | rk3288_defconfig                   |
+-----------------------------+--------------------------+------------------------------------+

- MY-RK3288-EK314-2G configuration example：

.. code-block:: shell

    $ make rk3288_defconfig


.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.4.1.jpg
   :alt: My-rk32-ek314build_3.4.1.jpg


Compilation
~~~~~~~~~~~~~

- Execute compilation

.. code-block:: shell

    $ make

`Tips：To speed up the compilation，add "-j4" after make.The Linux host used to compile is dual-core ,4 threads .So "-j" is followed by 4, which takes 4 threads to compile. The number behind "-j" is allocated based on system resources,but It should not exceed the maximum threads the host support.`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.5.1.jpg
   :alt: My-rk32-ek314build_3.5.1.jpg

- Complete compilation

`Tips：u-boot compilation process will take a few minustes or so`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.5.2.jpg
   :alt: My-rk32-ek314build_3.5.2.jpg

Target file
~~~~~~~~~~~~~

|   You can get the compiled file u-boot.bin with ls command after compilation.

.. code-block:: shell

    $ ls

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_3.6.1.jpg
   :alt: My-rk32-ek314build_3.6.1.jpg

Compile kernel
----------------

Enter kernel source directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ cd ~/my-rk3288/02_source/rk32-myzr_kernel_3.10/

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.1.1.jpg
   :alt: My-rk32-ek314build_4.1.1.jpg


Validate configured file
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Execute source command

.. code-block:: shell

    $ source ~/my-rk3288/03_tools/gcc-arm-eabi-4.6-env

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.2.1.jpg
   :alt: My-rk32-ek314build_4.2.1.jpg

- View compiler configuration

.. code-block:: shell

    $ echo $ARCH
    $ echo $CROSS_COMPILE

`Tips：you can see that ARCH和CROSS_COMPILE is configured`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.2.2.jpg
   :alt: My-rk32-ek314build_4.2.2.jpg

- Verify cross compiler tool configuration

.. code-block:: shell

    $ ${CROSS_COMPILE}gcc -v

`Tips：you can see version information of cross compiler tool shown on terminal after execution of command.as below：`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.2.3.jpg
   :alt: My-rk32-ek314build_4.2.3.jpg


Prepare for kernel configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Remove kernel configuration

.. code-block:: shell

    $ make distclean

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.3.1.jpg
   :alt: My-rk32-ek314build_4.3.1.jpg

- Generated.config file

`Instructions：configuration files used for MY-RK3288-EK314 seires of evaluation board is rk3288-myzr-linux_defconfig.`

.. code-block:: shell

    $ make rk3288-myzr-linux_defconfig


.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.3.2.jpg
   :alt: My-rk32-ek314build_4.3.2.jpg


Compile kernel zImage and device tree dtb
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------+-----------------+-----------------------------------------+
| Evaluation board main model |    LCD type     | Corresponding device tree configuration |
+=============================+=================+=========================================+
| MYZR-RK3288-EK314           | LVDS(1024X600)  | rk3288-myzr_rh568_lvds_linux.img        |
+                             +-----------------+-----------------------------------------+
|                             | HDMI(1920X1080) | rk3288-myzr_rh568_hdmi_linux.img        |
+                             +-----------------+-----------------------------------------+
|                             | EDP(1920X1080)  | rk3288-myzr_rh568_edp_linux.img         |
+-----------------------------+-----------------+-----------------------------------------+

- Compile (for example：lvds lcd)

.. code-block:: shell

    $ make -j8 rk3288-myzr_rh568_lvds_linux.img

`Instruction：8 threads compilation is used in the screenshots.`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.4.1.jpg
   :alt: My-rk32-ek314build_4.4.1.jpg

- Complete compilation

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.4.2.jpg
   :alt: My-rk32-ek314build_4.4.2.jpg

- Target file

|   arch/arm/boot/zImage is the target file through compilation，you can view the file information with ls command.

.. code-block:: shell

    $ ls arch/arm/boot/zImage -la

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.4.3.jpg
   :alt: My-rk32-ek314build_4.4.3.jpg


Compile module
~~~~~~~~~~~~~~~~

- Compile

.. code-block:: shell

    $ make modules

`Instruction：4 threads compilation is used in the screenshots.`

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.5.1.jpg
   :alt: My-rk32-ek314build_4.5.1.jpg

- Complete compilation

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.5.2.jpg
   :alt: My-rk32-ek314build_4.5.2.jpg

- Target file

|   After the translation is completed, the .ko file of each module is located in the directory where the code is located. The find command can be used to find out the compiled module. The reference commands are as follows:

.. code-block:: shell

    $ find -name *.ko

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_4.5.3.jpg
   :alt: My-rk32-ek314build_4.5.3.jpg


Pack linux-boot.img
----------------------

Compile rockchip-mkbootimg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   1) Create application directory

.. code-block:: shell

    $ mkdir ~/my-rk3288/01_application
    $ cd ~/my-rk3288/01_application

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.1.1.jpg
   :alt: My-rk32-ek314build_5.1.1.jpg

|   2) Unpack and compile rockchip-mkbootimg

.. code-block:: shell

    $ tar jxf rockchip-mkbootimg.tar.bz2
    $ cd rockchip-mkbootimg/
    $ make && sudo make install

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.1.2.jpg
   :alt: My-rk32-ek314build_5.1.2.jpg


Pack initrd.img
~~~~~~~~~~~~~~~~~

|   1) Compresse to img format

.. code-block:: shell

    $ cd ~/my-rk3288/01_application/
    $ tar jxf initrd.tar.bz2
    $ make -C initrd/

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.2.1.jpg
   :alt: My-rk32-ek314build_5.2.1.jpg

|   2) Show results

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.2.2.jpg
   :alt: My-rk32-ek314build_5.2.2.jpg

Pack linux-boot.img
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ mkbootimg --kernel ../02_source/rk32-myzr_kernel_3.10/arch/arm/boot/zImage --ramdisk initrd.img \ 
    --second ../02_source/rk32-myzr_kernel_3.10/resource.img -o linux-boot.img

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_5.3.1.jpg
   :alt: My-rk32-ek314build_5.3.1.jpg


File system
~~~~~~~~~~~~~

|   File system package is located in image file folder in the network disk。as to type of file system supported and way of download please refer to《MYZR-RK3288-EK314 buring guide》


Package batch file relase_update.img
--------------------------------------

Compile packaging tools
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ cd ~/my-rk3288/01_application
    $ tar jxf rk2918_tools.tar.bz2
    $ cd rk2918_tools/
    $ make -j4
    $ sudo cp afptool img_unpack img_maker mkkrnlimg /usr/local/bin/

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_7.1.1.jpg
   :alt: My-rk32-ek314build_7.1.1.jpg


New folder and copy image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   The file of "test/Image/" corresponds to the file of "Image\linux", rk3288box-3.10-uboot-ubuntu.parameter.txt is renamed to parameter, RESERVED is the empty file, RK3288UbootLoader_V2.30.10.bin corresponds to RKLoader.bin, update-script and The recover-script is copied by the burning tool. The contents of the package-file are renamed according to the corresponding file, as follows:

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_7.2.1.jpg
   :alt: My-rk32-ek314build_7.2.1.jpg

.. code-block:: shell

    $ mkdir ~/my-rk3288/04_rootfs/
    $ cd ~/my-rk3288/04_rootfs/
    $ mkdir -p ubuntu/Image
    $ cp test/Image/* ubuntu/Image/
    $ cp ubuntu/Image/RKLoader.bin ubuntu/
    $ cd ubuntu/

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_7.2.2.jpg
   :alt: My-rk32-ek314build_7.2.2.jpg

Pack relase_update.img
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ cd Image/
    $ afptool -pack . ../update.img
    $ cd ..
    $ img_maker -rk32 RKLoader.bin update.img relase_update.img

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/My-rk32-ek314build_7.3.1.jpg
   :alt: My-rk32-ek314build_7.3.1.jpg