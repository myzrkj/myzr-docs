MYZR-IMX28 Linux-3.14.52 Build Manual
=======================================

Document instruction
----------------------

System environment instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- CUP architeture of host used for compilation：64bit
- System of compiler host：Linux
- Linux release version:
- Ubuntu version type:saver version
- Ubuntu version no.:12.04.5
- Ubuntu system type:x86-64

**Note: The development host should use ubuntu 12.04.5 x86-64（desktop and server version are available），Using other distribution of Linux and other versions of Ubuntu may encounter unnecessary problems.**

Operation instruction
~~~~~~~~~~~~~~~~~~~~~~~

|  1）The line in the document which begins with “$”,which is followed by the Linux command.
|  2）All the Linux commands in the document are recommended to be entered into the host manually for execution.（Copying ,pasting to the host directly to execute may fail.
|  3）In all the Linux execution commands of the document，if the next character after the space is "-",（example：sudo apt-get –y install），please enter into Linux host to execute manually.（Copying ,pasting to the host directly to execute may fail）.
|  4）Any line of Linux commands whichi is not finished is recommended to be entered into the host for execution. （Because copy or paste commands cannot contain special character such as "line breaks"）.
|  5）Note whether the execution result is consistent with the document image when you enter and execute the command. check the command was entered incorrectly or failed to execute.
|  6）Please follow the document strictly to compile for the first time.Otherwise ,there may be unexpected error.

Screenshots instruction
~~~~~~~~~~~~~~~~~~~~~~~~~

|  To make the view look neat and tidy , the command prompt in the screenshot should use myzr$ uniformly.

Linux command in the image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  In the image of the document, you can see the input Linux command visually from the lines that start with “myzr$” linux command.

Prepare source code and relevant files
----------------------------------------

Source code
~~~~~~~~~~~~~~

|  The corresponding Linux version of the evaluation board and the corresponding source code files are shown in the table below：

+------------------------+--------------------------+------------------------+-----------------------+
| Evaluation board model | System version supported | u-boot source code     | linux source code     |
+------------------------+--------------------------+------------------------+-----------------------+
| MYZR-IMX28-EVK         | Linux-3.14.54            | u-boot-2015.04.tar.bz2 | linux-3.14.54.tar.bz2 |
+------------------------+--------------------------+------------------------+-----------------------+


Cross compiler tool file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Linux program cross compiler tool:gcc-4.4.4-glibc-2.11.1-multilib-1.0.tar.bz2
|  Linux cross compiler tool configuration file:gcc-4.4.4-glibc-2.11.1-multilib-env

Creat working directory
~~~~~~~~~~~~~~~~~~~~~~~~~

|  1）Source code directory

.. code-block:: shell

   $ mkdir -p ~/my-imx28/02_source

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_2.3.0.1.png
   :alt: IMX28_2635_build_2.3.0.1.png

|  2）Tool directory

.. code-block:: shell

   $ mkdir -p ~/my-imx28/03_tools

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_2.3.0.2.png
   :alt: IMX28_2635_build_2.3.0.2.png

|  3）Image dirrectory

.. code-block:: shell

   $ mkdir -p ~/my-imx28/04_image

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_2.3.0.3.png
   :alt: IMX28_2635_build_2.3.0.3.png

|  4）Application directory

.. code-block:: shell

   $ mkdir -p ~/my-imx28/01_application

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_2.3.0.4.png
   :alt: IMX28_2635_build_2.3.0.4.png

Prepare development environment
---------------------------------

Update source list of host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get update

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.1.0.1.png
   :alt: IMX28_2635_build_3.1.0.1.png

|  It looks like below after the update

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.1.0.2.png
   :alt: IMX28_2635_build_3.1.0.2.png

Install management tool of aptitude package and ia32-libs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Tips: if Linux of compilation host is 32bit,then you can skip this step

**Install management tool of aptitude package**

.. code-block:: shell

   $ sudo apt-get -y install aptitude

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.2.1.1.png
   :alt: IMX28_2635_build_3.2.1.1.png

|  Tips: the above image is the screenshots after re-execution of installation command when intallation of aptitude was completed.

**Install ia32-libs with aptitude**

.. code-block:: shell

   $ sudo aptitude -y install ia32-libs

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.2.2.1.png
   :alt: IMX28_2635_build_3.2.2.1.png

|  Tips: the above image is the screenshots after re-execution of installation command when intallation of aptitude and ia32-libs was completed.

Install mkimage tool
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get -y install uboot-mkimage

|  Tips: the following image is the screenshots after re-execution of installation command when intallation of mkimage was completed.

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.3.0.1.png
   :alt: IMX28_2635_build_3.3.0.1.png

Install ncurses-dev
~~~~~~~~~~~~~~~~~~~~~~

|  make menuconfig is dependant to it

.. code-block:: shell

   $ sudo aptitude -y install ncurses-dev

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.4.0.1.png
   :alt: IMX28_2635_build_3.4.0.1.png

|  Tips: the above image is the screenshots after re-execution of installation command when intallation of aptitude and ia32-libs was completed.

Install and configure cross compiler tool chain
--------------------------------------------------

Install Linux cross compilation tool chain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1）Enter cross compilation tool chain diretory

.. code-block:: shell

   $ cd ~/my-imx28/03_tools/

|  2）Copy Linux cross compilation tool to directory
|  Copy gcc-4.4.4-glibc-2.11.1-multilib-1.0.tar.bz2 to “~/my-imx28/03_tools”，this step need to be done in your own way.
|  3）Decompress Linux cross compilation tool

.. code-block:: shell

   $ tar jxf gcc-4.4.4-glibc-2.11.1-multilib-1.0.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_4.1.0.1.png
   :alt: IMX28_2635_build_4.1.0.1.png

|  4）Copy cross compilation tool configuration file
|  将gcc-4.4.4-glibc-2.11.1-multilib-env复制到“~/my-imx28/03_tools”，这一步自己采取相应的方式完成。
|  5）Check installation

.. code-block:: shell

   $ source gcc-4.4.4-glibc-2.11.1-multilib-env
   $ ${CROSS_COMPILE}gcc -v

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_4.1.0.2.png
   :alt: IMX28_2635_build_4.1.0.2.png

U-Boot compilation
---------------------

Prepare compilation
~~~~~~~~~~~~~~~~~~~~~~

**Copy source code package to development host**

|  Copy“u-boot source code”downloaded to “~/my-imx6/02_source”of Linux development host
|  This step need to be done in your own way

**Decompress u-boot source code package**

.. code-block:: shell

   $ cd ~/my-imx28/02_source/
   $ tar jxf u-boot-2015.04.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_5.1.2.1.png
   :alt: IMX28_31454_build_5.1.2.1.png

**Update library libssl-dev**

.. code-block:: shell

   $ sudo apt-get install libssl-dev

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_5.1.3.1.png
   :alt: IMX28_31454_build_5.1.3.1.png

Compile
~~~~~~~~

**Validate compilation configuration file**

.. code-block:: shell

   $ source ~/my-imx28/03_tools/gcc-4.4.4-glibc-2.11.1-multilib-env

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.1.1.png
   :alt: IMX28_2635_build_5.2.1.1.png

**Go to the u-boot source directory**

.. code-block:: shell

   $ cd ~/my-imx28/02_source/u-boot-2015.04

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_5.2.2.1.png
   :alt: IMX28_31454_build_5.2.2.1.png

**Remove u-boot temporary files**

.. code-block:: shell

   $ make distclean

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_5.2.3.1.png
   :alt: IMX28_31454_build_5.2.3.1.png

**Configure u-boot**

+-----------------------------+--------------------------+---------------------------------------+
| Evaluation board main model | CPU type-memory capacity | Corresponaind configuration of u-boot |
+-----------------------------+--------------------------+---------------------------------------+
| MYZR-IMX28-EVK              | MX283/7, 128M            | mx28_evk_config                       |
+-----------------------------+--------------------------+---------------------------------------+

- Example for MYZR-IMX28-EVK configuration:

.. code-block:: shell

   $ make mx28evk_nand_defconfig

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_5.2.4.1.png
   :alt: IMX28_31454_build_5.2.4.1.png

**Execute compilation**

.. code-block:: shell

   $ make u-boot.sb

|  Tips：To speed up the compilation，add "-j4" after make.The Linux host used to compile is dual-core ,4 threads .So "-j" is followed by 4, which takes 4 threads to compile. The number behind "-j" is allocated based on system resources,but It should not exceed the maximum threads the host support

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_5.2.5.1.png
   :alt: IMX28_31454_build_5.2.5.1.png

- Complete compilation

|  Tips: u-boot compiling process may take one or two minutes

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_5.2.5.2.png
   :alt: IMX28_31454_build_5.2.5.2.png

Target file
~~~~~~~~~~~~~

- Compile file

|  You can get the compiled file u-boot .sb with ls command after compilation

.. code-block:: shell

   $ ls

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_5.3.0.1.png
   :alt: IMX28_31454_build_5.3.0.1.png

- Target file

|  The corresponding target file name for u-boot configuration of MY-IMX28 series evaluation board is shown in the table below.

+----------------------+--------------------+
| u-boot configuration | Target file        |
+----------------------+--------------------+
| mx28_evk_config      | imx28_ivt_uboot.sb |
+----------------------+--------------------+


Compile kernel
---------------

Prepare compilation
~~~~~~~~~~~~~~~~~~~~~~

**Copy source code package to development host**

|  Copy“linux source code”downloaded to “~/my-imx28/02_source”of Linux development host
|  This step should be done in your own way

**Decompress linux source code package**

.. code-block:: shell

   $ cd ~/my-imx28/02_source/
   $ tar jxf linux-3.14.54.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.1.2.1.png
   :alt: IMX28_31454_build_6.1.2.1.png

Configuration of kernel compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Validate configuration file of compilation**

.. code-block:: shell

   $ source ~/my-imx28/03_tools/gcc-4.4.4-glibc-2.11.1-multilib-env

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.2.1.1.png
   :alt: IMX28_2635_build_6.2.1.1.png

**Remove kernel temporary file**

- Enter linux source code directory

.. code-block:: shell

   $ cd ~/my-imx28/02_source/linux-3.14.54

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.2.2.1.png
   :alt: IMX28_31454_build_6.2.2.1.png

- Remove temporary file

.. code-block:: shell

   $ make distclean

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.2.2.2.png
   :alt: IMX28_31454_build_6.2.2.2.png

**Kernel configuration**

.. code-block:: shell

   $ cp .mx28_config .config

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.2.3.1.png
   :alt: IMX28_31454_build_6.2.3.1.png

Compile kernel
~~~~~~~~~~~~~~~~

- Execute compilation

.. code-block:: shell

   $ make zImage -j4

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.3.0.1.png
   :alt: IMX28_31454_build_6.3.0.1.png

- Complete compilation

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.3.0.2.png
   :alt: IMX28_31454_build_6.3.0.2.png

- Target file

|  arch/arm/boot/uImage即为编译得到的内核文件，使用ls命令可查看文件信息。

.. code-block:: shell

   $ ls arch/arm/boot/uImage -la

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.3.0.3.png
   :alt: IMX28_2635_build_6.3.0.3.png

Compife device tree
~~~~~~~~~~~~~~~~~~~~~

|  The correspondence between the type of evaluation board and device tree is shown below：

+------------------------+--------------------------+--------------------------------+
|        Function        |   Source code position   |    Linux device and folder     |
+========================+==========================+================================+
| Development main model | CPU type-memory capacity | Corresponding device tree file |
+------------------------+--------------------------+--------------------------------+
| MYZR-IMX28-EVK         | MX283/7, 128M            | imx28-evk.dtb                  |
+------------------------+--------------------------+--------------------------------+

- Take MY-IMX28-EVK as an example:

.. code-block:: shell

   $ make imx28-evk.dtb

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.4.0.1.png
   :alt: IMX28_31454_build_6.4.0.1.png

- Target file

|  You can browse the target device tree file information from compilation with ls command：

.. code-block:: shell

   $ ls arch/arm/boot/dts/*.dtb

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.4.0.2.png
   :alt: IMX28_31454_build_6.4.0.2.png


Compile module
~~~~~~~~~~~~~~~~

- Command for compiling module

.. code-block:: shell

   $ make modules

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.5.0.1.png
   :alt: IMX28_31454_build_6.5.0.1.png

- Install module to the specified directory

.. code-block:: shell

   $ make modules_install INSTALL_MOD_PATH=./modules

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.5.0.2.png
   :alt: IMX28_31454_build_6.5.0.2.png

- Package the module file

.. code-block:: shell

   $ cd modules
   $ tar cjf ../modules.tar.bz2 *

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_6.5.0.3.png
   :alt: IMX28_31454_build_6.5.0.3.png

Application compilation
-------------------------

Linux application compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Write an application**

- Enter working directory

.. code-block:: shell

   $ cd ~/my-imx28/01_application/

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_7.1.1.1.png
   :alt: IMX28_31454_build_7.1.1.1.png

- Write souce code

.. code-block:: shell

   $ vim hello.c

|  Write following code and save

.. code:: c

   include <stdio.h>
   int main(int argc, char **argv)
   {
      printf("Hello, MYZR!\n");
      return;
   }

- View code

.. code-block:: shell

   $ cat hello.c

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.1.2.png
   :alt: IMX28_2635_build_7.1.1.2.png

**Compife application**

- Configure environment variables

.. code-block:: shell

   $ source ~/my-imx28/03_tools/gcc-4.4.4-glibc-2.11.1-multilib-env

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.2.1.png
   :alt: IMX28_2635_build_7.1.2.1.png

- Compile

.. code-block:: shell

   $ ${CROSS_COMPILE}gcc hello.c -o hello.out

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.2.2.png
   :alt: IMX28_2635_build_7.1.2.2.png

|  Note:The above command contains “$”,which is “${CROSS_COMPILE}gcc”. It is the environment variable generated when referring to our source.

- Target file

.. code-block:: shell

   $ file hello.out

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.2.2.png
   :alt: IMX28_2635_build_7.1.2.2.png

File system
-------------

File system rootfs.tar.bz2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Add your own application by the following means: (copy MY-IMX28_Born_Tool\Profiles\MX28 Linux Update\OS Firmware\files\image-linux-31454/rootfs.tar.bz2 to directory of“~/my-imx28/04_image/”)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_8.1.0.1.png
   :alt: IMX28_2635_build_8.1.0.1.png

File system filesystem.ubifs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Copy mkfs.ubifs，ubinize to directory of“/usr/bin”of computer（if computer has both these two applications,the copy is not needed）；copy build_rootfs和ubinize.cfg to directory of “~/my-imx28/04_image/”

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_8.2.0.1.png
   :alt: IMX28_31454_build_8.2.0.1.png

Programing mode
-----------------

|  So far,we get a set of programing file under directory of “~/my-imx28/02_source besides file system ,including “u-boot.sb”、“imx28-evk.dtb”、“zImage”、“rootfs.tar.bz2”

Program with MFGTOOL
~~~~~~~~~~~~~~~~~~~~~

|  Copy “u-boot.sb”、“imx28-evk.dtb”、“zImage”、“rootfs.tar.bz2 to the directory of “MY-IMX28_Born_Tool\Profiles\MX28 Linux Update\OS Firmware\files\image-linux-31454”.hold REC key,plug in MINI USB line and power cable,then open MfgTool.exe,click"scan device",detect HID device,release REC key,like below:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_9.1.0.1.png
   :alt: IMX28_2635_build_9.1.0.1.png

|  Click“Options”on menu，then select“MY-IMX28-3.14.54 NAND with uboot”on option of “Profiles”，then click“Enter”，finally click“start”

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_9.1.0.2.png
   :alt: IMX28_31454_build_9.1.0.2.png

|  When programing is successful,click"stop",to be completed

``Note: if file system in use is rootfs-qt.tar.bz2, please choose “QT-MY-IMX28-3.14.54 NAND with uboot”as programing image.``

Program with network
~~~~~~~~~~~~~~~~~~~~~~

**Build up TFTP (ubuntu system)**

|  (1) Setup tftp server files （下载并安装tftp）

.. code-block:: shell

   $ sudo apt-get install tftpd tftp openbsd-inetd

|  (2) make a tftp directory (buid tftp directory and change its property)
|  Here we make /home/myzr/tftpt be a tftp directory.

.. code-block:: shell

   $ mkdir /home/myzr/tftp
   $ chmod 777 /home/myzr/tftp

|  (3) Open /etc/inetd.conf and edit it (change tftp directory of configured file)

.. code-block:: shell

   $ sudo gedit /etc/inetd.conf

|  Coment this line :
|  tftp dgram udp wait nobody /usr/sbin/tcpd /usr/sbin/in.tftpd /srv/tftp
|  Add new line:
|  tftp dgram udp wait nobody /usr/sbin/tcpd /usr/sbin/in.tftpd /home/myzr/tftp

|  (4)Restarting tftp service (reboot tftp)

.. code-block:: shell

   $ sudo /etc/init.d/openbsd-inetd restart

**Build NFS (network programing does't need nfs)**

|  (1)  Install NFS server package (Download and install nfs)

.. code-block:: shell

   $ sudo apt-get install nfs-kernel-server

|  (2) Create NFS directory:/home/myzr/nfsroot (newly build nfs directory)

.. code-block:: shell

   $ mkdir /home/myzr/nfsroot

|  (3) Configure mounted directory and authority (change nfs directory of configuration file)

.. code-block:: shell

   $ sudo gedit /etc/exports

|  Add the following line at the end of the file:
|  /home/myzr/nfsroot \*(rw,sync,no_root_squash)

|  (4) Restart the NFS service (reboot nfs)

.. code-block:: shell

   $ sudo /etc/init.d/portmap restart
   $ sudo /etc/init.d/nfs-kernel-server restart

**tftp Download**

|  (1) Copy “u-boot.sb”、“imx28-evk.dtb”、“zImage”、“filesystem.ubifs”to the directory of “/home/myzr/tftp”
|  (2) Set environment variables(directly connect board with computer lan line)

.. code-block:: shell

   $ setenv ipaddr 192.168.3.104 （The board IP）
   $ setenv serverip 192.168.3.110 （Computer IP）

|  (3) Program

.. code-block:: shell

   $ run update_nand_kernel (program zImage)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_9.2.3.1.png
   :alt: IMX28_31454_build_9.2.3.1.png

.. code-block:: shell

   $ run update_nand_fdt (program fdt)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_9.2.3.2.png
   :alt: IMX28_31454_build_9.2.3.2.png

.. code-block:: shell

   $ run update_nand_filesystem (program file system)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_9.2.3.3.png
   :alt: IMX28_31454_build_9.2.3.3.png

Login way
-----------

Serial port login
~~~~~~~~~~~~~~~~~~~

|  Plug in USB to serial port line and power supply,enter key Enter to enter system in about 10 minutes after starting the device

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_10.1.0.1.png
   :alt: IMX28_31454_build_10.1.0.1.png

ssh Login
~~~~~~~~~~~

**Ethernet login**

|  Plug in lan line and power supply,you can login via software SecureCRT in about 10 minutes after starting the device,the board default ehternet IP as 192.168.3.104,you can set computer IP as 192.168.3.110,then configure SecureCRT,enter root as user name and myzr as password,like below:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_10.2.1.1.png
   :alt: IMX28_31454_build_10.2.1.1.png

|  After entering is over,click "ok",the login is completed

**USB login(USB can be identified as network port)**

|  Plug in lan line and power supply,you can login via software SecureCRT in about 10 minutes after starting the device,the board default ehternet IP as 192.168.3.104,you can set computer IP as 192.168.3.110,then configure SecureCRT,enter root as user name and myzr as password,like below:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_10.2.2.1.png
   :alt: IMX28_31454_build_10.2.2.1.png

|  After entering is over,click "ok",the login is completed

Test
------

USB test
~~~~~~~~~

|  Directly insert U disk,you can see the content of U disk after mounting(if it is not QT system,there will be an automatic mounting)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_11.1.0.1.png
   :alt: IMX28_31454_build_11.1.0.1.png

SD card test
~~~~~~~~~~~~~~

|  Directly SD card,you can see the content of SD card after mounting(if it is not QT system,there will be an automatic mounting)

IMX28_31454_build_11.2.0.1.png

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_11.2.0.1.png
   :alt: IMX28_31454_build_11.2.0.1.png

Ethernet test
~~~~~~~~~~~~~~

|  Plug in lan line,test eth0 and eth1 network port directly with ping command. defaulted IP of eth0 is 192.168.3.104,let's set eth1 as 192.168.3.105,as below:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_11.3.0.1.png
   :alt: IMX28_31454_build_11.3.0.1.png

Uart serial port test
~~~~~~~~~~~~~~~~~~~~~~~

|  Device ttyAPP0 of serial port uat0,device ttyAPP3 of serial port uat3,please short connect transceiver pin in test.

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_11.4.0.1.png
   :alt: IMX28_31454_build_11.4.0.1.png

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_11.4.0.2.png
   :alt: IMX28_31454_build_11.4.0.2.png

gpio Test
~~~~~~~~~~

|  GPIO_2_26,GPIO_2_25 and GPIO_2_27 were set as function of GPIO in driver configuration，take pin of GPIO_2_26 as an example to figure out the no.of pin of GPIO_2_26 is 2*32+26=90,the test as below:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_11.5.0.1.png
   :alt: IMX28_31454_build_11.5.0.1.png

SPI Test
~~~~~~~~~~

|  SPI interface is semiduplex mode,here you only test the sending, you can see wave shape through oscilloscope .way number 1 is to only send 0x55 and 0x75,way number2 is to send charater string"myzr"

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_11.6.0.1.png
   :alt: IMX28_31454_build_11.6.0.1.png

watchdog test
~~~~~~~~~~~~~~~

|  "watch dog",the full name is wathcdog timer,which is hardware timer to reset computer sytem when there is an error in software. usually a user space protect procedure will notice watchdog driver in kernel through special device /dev/watchdog in normal time interval that everything in user space is normal. if there is an error in user space(such as RAM error,kernel BUG and ect),the notice will be stopped,then hardware Watchdog will reset system after timeout.
|  /dev/watchdog device file will be opened in test program,and start Watchdog,feeding dog will happen once each second,system won't reboot.

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_11.7.0.1.png
   :alt: IMX28_31454_build_11.7.0.1.png

|  /dev/watchdog device file will be opened in test program,and start Watchdog,program come into cycling state,since there is not dog feeding, and system will reset in 30 seconds

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_31454_build_11.7.0.2.png
   :alt: IMX28_31454_build_11.7.0.2.png