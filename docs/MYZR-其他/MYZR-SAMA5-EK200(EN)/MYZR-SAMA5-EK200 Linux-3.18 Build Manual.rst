MYZR-SAMA5-EK200 Linux-3.18 Build Manual
===========================================

Document instruction
-----------------------

System environment instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- CUP architeture of host used for compilation：64bit
- System of compilation host：Linux
- Linux release version: Ubuntu
- Ubuntu version type: saver version
- Ubuntu version no.: 12.04.5
- Ubuntu system type: x86-64

**The development host should use ubuntu 12.04.5 x86-64（desktop and server version are available），Using other distribution of Linux and other versions of Ubuntu may encounter unnecessary problems.**

Operation instruction
~~~~~~~~~~~~~~~~~~~~~~~

|  1）The line in the document which begins with “$”,which is followed by the Linux command.
|  2）All the Linux commands in the document are recommended to be entered into the host manually for execution.（Copying ,pasting to the host directly to execute may fail）.
|  3）In all the Linux execution commands of the document，if the next character after the space is "-",（example：sudo apt-get –y install），please enter into Linux host to execute manually.（Copying ,pasting to the host directly to execute may fail )
|  4）Any line of Linux commands whichi is not finished is recommended to be entered into the host for execution. (Because copy or paste commands cannot contain special character such as "line breaks"）.
|  5）Note whether the execution result is consistent with the document image when you enter and execute the command. check the command was entered incorrectly or failed to execute. )
|  6）Please follow the document strictly to compile for the first time.Otherwise ,there may be unexpected error.

Screenshots instruction
~~~~~~~~~~~~~~~~~~~~~~~~~

|  To make the view look neat and tidy , the command prompt in the screenshot should use myzr$ uniformly.

Linux command in the image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  In the image of the document, you can see the input Linux command visually from the lines that start with “myzr$”.

Important information instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**To avoid our customers wasting time and energy when they encounter unnecessary problems in building development environment and compiling process,it is recommended to use “vb43-u12045-serv-amd64” virtual machine system released by MYZR.**

|  Details refered to《MYZR virtual machine system guidance》

Install and configure cross compilation tool chain
----------------------------------------------------

Prepare installation package of cross compilation tool chain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1）Download cross compilation tool
|  Cross compilation tool:gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.tar.xz
|  Configured file of cross compilation tool:gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config
|  2）Create tool directory in virtual machine system

.. code-block:: shell

   $ mkdir ~/my-sama5/03_tools -p

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_3.1.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_3.1.0.1.png

|  3）Copy file to virtual machine sytem
|  Copy cross compilation tool and configured file to ~/my-sama5/03_tools
|  This step should be done in your own way

Install cross compilation tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1）Enter cross compilation tool chain diretory

.. code-block:: shell

   $ cd ~/my-sama5/03_tools/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_3.2.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_3.2.0.1.png

|  2）Decompress(install) cross compilation tool

.. code-block:: shell

   $ tar xf gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.tar.xz

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_3.2.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_3.2.0.2.png

|  3）Check installation
|  Check the version information of cross compilation tool chain to verify the normality of the installation

.. code-block:: shell

   $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config
   $ ${CROSS_COMPILE}gcc -v

|  After execution of command,there will be following message：

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_3.3.0.7.png
   :alt: MY-SAMA5_Linux-3.18_build_3.3.0.7.png

|  And there will come out with information related to gcc version in the last line.

.. code-block:: shell

   gcc version 4.9.3 20141031 (prerelease) (Linaro GCC 2014.11)

AT91Bootstrap compilation
----------------------------

Prepare source code
~~~~~~~~~~~~~~~~~~~~~

|  1）Download source code
|  File name：at91bootstrap-3.7.2.tar.bz2
|  AT91Bootstrap is a two stage boot loader,which provide a set of algorithm to manage hardware initialization,such as configuration of clock and speed,setting of PIO,initialization of memory download main application to main memory and boot from specified boot media</span>
|  2）Create working directory

.. code-block:: shell

   $ mkdir ~/my-sama5/02_source -p

|  3）Copy source code to working directory
|  Copy in your own way AT91Bootstrap to “~/my-sama5/02_source”,or refer to “2.3 demo of common function”.
|  4）Decompress source code

- Enter working directory

.. code-block:: shell

   $ cd ~/my-sama5/02_source/

- Execute decompress command

.. code-block:: shell

   $ tar jxf at91bootstrap-3.7.2.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.1.0.3.png
   :alt: MY-SAMA5_Linux-3.18_build_4.1.0.3.png

Compile
~~~~~~~~~

|  1）Enter source code directory

.. code-block:: shell

   $ cd ~/my-sama5/02_source/at91bootstrap-3.7.2/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.1.png

|  2）Validate configured file of compilation

.. code-block:: shell

   $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config

|  3）Remove temporary file which may exist in the code

.. code-block:: shell

   $ make mrproper

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.3.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.3.png

|  4）Generate configuration file

.. code-block:: shell

   $ make mysama5ek200_defconfig

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.4.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.4.png

|  5）Execute compilation

.. code-block:: shell

   $ make -j4

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.5.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.5.png

|  6）Complete compilation

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.2.0.6.png
   :alt: MY-SAMA5_Linux-3.18_build_4.2.0.6.png

Target file
~~~~~~~~~~~~~

|  1）Target file
|  Target file needed by us will be generated under directory of binaries of source code after compilation is completed
|  You can see through ls command that mysama5ek200-dataflashboot-uboot-3.7.2.bin is the file what we need.

.. code-block:: shell

   $ ls binaries/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.3.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_4.3.0.1.png

|  2）Re-name target file
|  These target files will be used by us in programming,to make programming convenient,we need to change the name of these files to be as bootstrap-mysama5ek200.

.. code-block:: shell

   $ cd binaries/
   $ rename 's/mysama5ek200-dataflashboot-uboot-3.7.2/bootstrap-mysama5ek200/' *
   $ ls -1

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_4.3.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_4.3.0.2.png

|  3）Save target file
|  save bootstrap-mysama5ek200.*

u-boot compilation
--------------------

Prepare source code
~~~~~~~~~~~~~~~~~~~~~~

|  1）Download source code
|  File name：u-boot-at91-linux4sam_4.7.tar.bz2
|  U-boot is the third stage bootloader on Atmel AT91 SoC, it is engaged in configuring main interfaces and booting Linux system.
|  2）copy source code to working directory
|  copy in your own way source code of u-boot to “~/my-sama5/02_source”,or refer to “2.3 demo of common function”
|  3）Decompress source code

- Enter working directory

.. code-block:: shell

   $ cd ~/my-sama5/02_source/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.1.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_5.1.0.1.png

- Execute decompress command

.. code-block:: shell

   $ tar jxf u-boot-at91-linux4sam_4.7.tar.bz2

Compile
~~~~~~~~~

|  1）Enter directory of u-boot source code

.. code-block:: shell

   $ cd ~/my-sama5/02_source/u-boot-at91-linux4sam_4.7/

|  2）Validate configured file of compilation

.. code-block:: shell

   $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config

|  3）Remove temporary file which may exist in code

.. code-block:: shell

   $ make distclean

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.2.0.3.png
   :alt: MY-SAMA5_Linux-3.18_build_5.2.0.3.png

|  4）Generate configured file

.. code-block:: shell

   $ make mysama5ek200_defconfig

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.2.0.4.png
   :alt: MY-SAMA5_Linux-3.18_build_5.2.0.4.png

|  5）Execute compilation

.. code-block:: shell

   $ make -j4

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.2.0.5.png
   :alt: MY-SAMA5_Linux-3.18_build_5.2.0.5.png

|  6）Complete compilation

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.2.0.6.png
   :alt: MY-SAMA5_Linux-3.18_build_5.2.0.6.png

Target file
~~~~~~~~~~~~~

|  Target file needed by us will be generated under directory of source code after compilation is completed
|  You can see through ls command that u-boot.bin is the file what we need.

.. code-block:: shell

   $ ls u-boot* -1

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.3.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_5.3.0.1.png

|  2）Re-name target file
|  These target files will be used by us in programming,to make programming convenient,we need to change the name of these files to be as uboot-mysama5ek200.bin.

.. code-block:: shell

   $ mv u-boot.bin uboot-mysama5ek200.bin
   $ ls uboot-mysama5ek200.bin

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_5.3.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_5.3.0.2.png

|  3）Save target file
|  Save uboot-mysama5ek200.bin

Compile kernel
----------------

Prepare source code
~~~~~~~~~~~~~~~~~~~~~

|  1）Download source code
|  File name：linux-at91-linux4sam_4.7.tar.bz2
|  2）Copy source code to the working directory
|  Copy in your own way source code of kernel to “~/my-sama5/02_source”,or refer to “2.3 demo of common function”.
|  3）Decompress source code

- Enter working directory

.. code-block:: shell

   $ cd ~/my-sama5/02_source/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.1.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_6.1.0.1.png

- Execute decompress command

.. code-block:: shell

   $ tar jxf linux-at91-linux4sam_4.7.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.1.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_6.1.0.2.png

Compile
~~~~~~~~~

|  1）Enter directory of kernel source code

.. code-block:: shell

   $ cd ~/my-sama5/02_source/linux-at91-linux4sam_4.7/

|  2）Validate configured file of compilation

.. code-block:: shell

   $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config

|  3）Remove temporary file which may exist in the code

.. code-block:: shell

   $ make distclean

**Compile kernel file**

|  1）Generate kernel configuration file

.. code-block:: shell

   $ make ARCH=arm mysama5ek200_defconfig

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.1.1.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.1.1.png

|  2）Execute compilation command of kernel file

.. code-block:: shell

   $ make -j4 ARCH=arm zImage

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.1.2.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.1.2.png

|  3）Complete compilation of kernel file

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.1.3.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.1.3.png

|  4）Kernel target file

.. code-block:: shell

   $ ls arch/arm/boot/zImage

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.1.4.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.1.4.png

**Compile file of device tree**

|  1）Execute compilation command for device tree file

.. code-block:: shell

   $ make ARCH=arm mysama5ek200-d36.dtb

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.2.1.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.2.1.png

|  2）Target file of device tree

.. code-block:: shell

   $ ls arch/arm/boot/dts/mysama5ek200-d36.dtb

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.2.2.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.2.2.png

**Compile kernel module**

|  1）Execute compilation command for kernel module

.. code-block:: shell

   $ make ARCH=arm modules

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.1.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.1.png

|  2）Complete compilation of kernel module

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.2.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.2.png

|  3）Install kernel module to specified directory

.. code-block:: shell

   $ make ARCH=arm modules_install INSTALL_MOD_PATH=./modules

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.3.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.3.png

|  4）Package nernel module

.. code-block:: shell

   $ tar cjf modules_mysama5ek200.tar.bz2 modules/*

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.4.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.4.png

|  5）Module package

.. code-block:: shell

   $ ls modules_mysama5ek200.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_6.2.3.5.png
   :alt: MY-SAMA5_Linux-3.18_build_6.2.3.5.png

Compile file system
----------------------

Note and instruction
~~~~~~~~~~~~~~~~~~~~~~

|  a) The download of the original compilation exceed 4G。（tips：you can use files we have downloaded in order to reduce downloads and save time,which is going to be mentioned in 7.4）
|  b) The network of the compilation host is good to access to www.fackbook.com .Otherwise It may be subject to the condition of the domestic firewall and It is unable to download the software for compilation.
|  c) The initial compilation may take 2 hours to unlimited time.It depends on the network state and the configuration of the host.（After a rough statistics, It took about 100 minutes to compile QT5 system on the 16-core CPU 16 G memory host except download time.
|  Customer may decide whether to compile the file system or use the file system We provide based on the actual situation. If the file system we provide meets the requirements, you had better not to compile by yourself. Since It may be a lot of errors during compilation.

Preparation before compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Prepare compliation environment for Yocto**

|  Instruction: Yocto compilation depends on some software packages, so they need to be installed on development host.

.. code-block:: shell

   $ sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.1.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.1.1.png

.. code-block:: shell

   $ sudo apt-get install libsdl1.2-dev xterm sed cvs subversion coreutils texi2html docbook-utils python-pysqlite2 help2man make gcc g++ desktop-file-utils libgl1-mesa-dev libglu1-mesa-dev mercurial autoconf automake groff curl lzop asciidoc

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.1.2.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.1.2.png

.. code-block:: shell

    sudo apt-get install uboot-mkimage

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.1.3.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.1.3.png

**Prepare source code**

|  1）Download source code
|  Source package file name: atmel_fido.tar.bz2
|  2）Create working directory of yocto

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.2.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.2.1.png

|  3）Copy source code to devleopment host
|  Copy in your own way source code to yocto directory(e.g /home/myzr/yocto),or refer to “2.3 demo fo common functions".
|  4）Decompress source code package

- Enter main directory of user

.. code-block:: shell

   $ cd ~/yocto

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.2.2.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.2.2.png

- Execute decompress command

.. code-block:: shell

   $ tar jxf atmel_fido.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.2.3.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.2.3.png

**Prepare software package**

|  1）Create directory of “/opt/yocto”for saving software package

.. code-block:: shell

   $ sudo mkdir /opt/yocto

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.3.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.3.1.png

.. code-block:: shell

   $ sudo chmod 777 /opt/yocto

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.2.3.2.png
   :alt: MY-SAMA5_Linux-3.18_build_7.2.3.2.png

|  2）Download software package
|  Download yocto software package from network disk
|  relative path of software package:yocto/downloads，download downloads to Windows.
|  3）Copy software package to devleopment host.
|  Copy directory of “downloads”downloaded to “/opt/yocto”of development host.

Compile file system
~~~~~~~~~~~~~~~~~~~~~

**Configuration before compilation**

|  1）Prepare configuration file of compilation
|  File directory:conf。download directory of conf to Windows.
|  2）Enter directory of poky

.. code-block:: shell

   $ cd ~/yocto/atmel_fido/poky/

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.3.1.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.3.1.1.png

.. code-block:: shell

   $ source oe-init-build-env build-atmel

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.3.1.2.png
   :alt: MY-SAMA5_Linux-3.18_build_7.3.1.2.png

|  3）Initiate directory of compilatio

.. code-block:: shell

   $ source oe-init-build-env build-atmel

|  4）Copy confirured file of compilation to drectory of compilation
|  Copy conf directory to /home/myzr/yocto/poky/build-atmel.

**Compile file system of QT5**

.. code-block:: shell

   $ bitbake atmel-qt5-demo-image

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.3.2.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.3.2.1.png

|  Tips: the whole compilation process will take about one hour to compile on the 16-core CPU and 16G memory host except download time.

- Target file

|  You can find the target file we compiled in the directory of ./tmp/deploy/images/sama5d3xek/

**Compile the cross-compiler tool for QT5**

.. code-block:: shell

   $ bitbake meta-toolchain-qt5

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/MY-SAMA5_Linux-3.18_build_7.3.3.1.png
   :alt: MY-SAMA5_Linux-3.18_build_7.3.3.1.png

- Target file

|  You can find the target file we compiled in the directory of ./tmp/deploy/images/sama5d3xek