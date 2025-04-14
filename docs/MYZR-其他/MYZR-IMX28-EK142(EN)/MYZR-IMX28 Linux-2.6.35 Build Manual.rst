MYZR-IMX28 Linux-2.6.35 Build Manual
======================================

Document instruction
-----------------------

System environment instruction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- CUP architeture of host used for compilation：64bit
- CUP architeture of host used for compilation：64bit
- Linux release verson:Ubuntu
- Ubuntu version type: saver veresion
- Ubuntu version no.:12.04.5
- Ubuntu system type:x86-64

**Note: The development host should use ubuntu 12.04.5 x86-64（desktop and server version are available），Using other distribution of Linux and other versions of Ubuntu may encounter unnecessary problems**

Operation instruction
~~~~~~~~~~~~~~~~~~~~~~~

|  1）The line in the document which begins with “$”,which is followed by the Linux command.
|  2）All the Linux commands in the document are recommended to be entered into the host manually for execution.（Copying ,pasting to the host directly to execute may fail）
|  3）In all the Linux execution commands of the document，if the next character after the space is "-",（example：sudo apt-get –y install），please enter into Linux host to execute manually.（Copying ,pasting to the host directly to execute may fail )
|  4）Any line of Linux commands whichi is not finished is recommended to be entered into the host for execution. （Because copy or paste commands cannot contain special character such as "line breaks"）
|  5）Note whether the execution result is consistent with the document image when you enter and execute the command. check the command was entered incorrectly or failed to execute.
|  6）Please follow the document strictly to compile for the first time.Otherwise ,there may be unexpected error

Screenshots instruction
~~~~~~~~~~~~~~~~~~~~~~~~~

|  To make the view look neat and tidy , the command prompt in the screenshot should use myzr$ uniformly.

Linux command in the image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  In the image of the document, you can see the input Linux command visually from the lines that start with "linyn@u12045-serv:~$".>

Prepare source code and relevant files
----------------------------------------

Source code
~~~~~~~~~~~~~

|  The corresponding Linux version of the evaluation board and the corresponding source code files are shown in the table below：

+------------------------+--------------------------+-----------------------------------+------------------------+
| Evaluation board model | System version supported | u-boot source code                | linux source code      |
+------------------------+--------------------------+-----------------------------------+------------------------+
| MYZR-IMX28-EVK         | Linux-2.6.35             | u-boot-2009.08.tar.bz2            | linux-2.6.35.3.tar.bz2 |
+                        +                          +                                   +                        +
|                        |                          | imx-bootlets-src-10.12.01.tar.bz2 |                        |
+------------------------+--------------------------+-----------------------------------+------------------------+

Cross compilation tool file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Linux program cross compilation tool:gcc-4.4.4-glibc-2.11.1-multilib-1.0.tar.bz2
|  Linux cross compilation tool configuration file:gcc-4.4.4-glibc-2.11.1-multilib-env

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

|  3）Image directory

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

Install management tool of aptitude package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get -y install aptitude

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.2.1.1.png
   :alt: IMX28_2635_build_3.2.1.1.png

|  Tips: the above image is the screenshots after re-execution of installation command when intallation of aptitude was completed

Install ia32-libs with aptitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo aptitude -y install ia32-libs

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.2.2.1.png
   :alt: IMX28_2635_build_3.2.2.1.png

|  Tips: the above image is the screenshots after re-execution of installation command when intallation of aptitude and ia32-libs was completed

Install mkimage tool
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ sudo apt-get -y install uboot-mkimage

|  Tips: the following image is the screenshots after re-execution of installation command when intallation of mkimage was completed

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.3.0.1.png
   :alt: IMX28_2635_build_3.3.0.1.png

Install ncurses-dev
~~~~~~~~~~~~~~~~~~~~~

|  Make menuconfig is dependant to it

.. code-block:: shell

   $ sudo aptitude -y install ncurses-dev

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_3.4.0.1.png
   :alt: IMX28_2635_build_3.4.0.1.png

|  Tips: the above image is the screenshots after re-execution of installation command when intallation of ncurses-dev was completed

Install and configure cross compiler tool chain
--------------------------------------------------

Install cross compilation tool chain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  1）Enter cross compilation tool chain diretory

.. code-block:: shell

   $ cd ~/my-imx28/03_tools/

|  2）Copy Linux cross compilation tool to directory
|  Copy gcc-4.4.4-glibc-2.11.1-multilib-1.0.tar.bz2 to“~/my-imx28/03_tools”,this step should be done in your own way
|  3）Decompress Linux cross compilation tool

.. code-block:: shell

   $ tar jxf gcc-4.4.4-glibc-2.11.1-multilib-1.0.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_4.1.0.1.png
   :alt: IMX28_2635_build_4.1.0.1.png

|  4）Copy congigured file of cross compilation tool
|  将gcc-4.4.4-glibc-2.11.1-multilib-env复制到“~/my-imx28/03_tools”，这一步自己采取相应的方式完成。
|  5）Check installation

.. code-block:: shell

   $ source gcc-4.4.4-glibc-2.11.1-multilib-env
   $ ${CROSS_COMPILE}gcc -v

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_4.1.0.2.png
   :alt: IMX28_2635_build_4.1.0.2.png

U-Boot compilation
--------------------

Prepare compilation
~~~~~~~~~~~~~~~~~~~~~

**Copy source code package to development host**

|  Copy“u-boot source code”downloaded to “~/my-imx28/02_source”of Linux development host
|  This step should be done in your own way

**Decompress u-boot source code**

.. code-block:: shell

   $ cd ~/my-imx28/02_source/
   $ tar jxf u-boot-2009.08.tar.bz2
   $ tar jxf imx-bootlets-src-10.12.01.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.1.2.1.png
   :alt: IMX28_2635_build_5.1.2.1.png

Compile
~~~~~~~~~

**Validate configured file of compilation**

.. code-block:: shell

   $ source ~/my-imx28/03_tools/gcc-4.4.4-glibc-2.11.1-multilib-env

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.1.1.png
   :alt: IMX28_2635_build_5.2.1.1.png

**Enter u-boot source code directory**

.. code-block:: shell

   $ cd ~/my-imx28/02_source/u-boot-2009.08

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.2.1.png
   :alt: IMX28_2635_build_5.2.2.1.png

**Remove u-boot temporary file**

.. code-block:: shell

   $ make distclean

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.3.1.png
   :alt: IMX28_2635_build_5.2.3.1.png

**Configure u-boot**

+-----------------------------+---------------------------+---------------------------------------+
| Evaluation board main model | CPU type--momery capacity | Corresponding configuration of u-boot |
+=============================+===========================+=======================================+
| MYZR-IMX28-EVK              | MX283/7, 128M             | mx28_evk_config                       |
+-----------------------------+---------------------------+---------------------------------------+

- Example for configuration of MYZR-IMX28-EVK :

.. code-block:: shell

   $ make mx28_evk_config

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.4.1.png
   :alt: IMX28_2635_build_5.2.4.1.png

**Execute compilation**

.. code-block:: shell

   $ make

|  Tips：To speed up the compilation，add "-j4" after make.The Linux host used to compile is dual-core ,4 threads .So "-j" is followed by 4, which takes 4 threads to compile. The number behind "-j" is allocated based on system resources,but It should not exceed the maximum threads the host support.

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.5.1.png
   :alt: IMX28_2635_build_5.2.5.1.png

- Compile imx28_ivt_uboot.sb

|  Tips: imx28_ivt_uboot.sb is the image programmed

.. code-block:: shell

   $ cp u-boot ../imx-bootlets-src-10.12.01
   $ cd ../imx-bootlets-src-10.12.01/
   $ sudo cp elftosb /usr/bin/
   $ ./build

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.2.5.2.png
   :alt: IMX28_2635_build_5.2.5.2.png

Target file
~~~~~~~~~~~~~~

- Compile file

|  You can get the compiled file imx28_ivt_uboot.sb with ls command after compilation.

.. code-block:: shell

   $ ls

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_5.3.0.1.png
   :alt: IMX28_2635_build_5.3.0.1.png

- Target file

|  The corresponding name of target file for u-boot configuration of MYZR-IMX28 series evaluation board is shown in the table below：

+----------------------+--------------------+
| u-boot configuration | Target file        |
+----------------------+--------------------+
| mx28_evk_config      | imx28_ivt_uboot.sb |
+----------------------+--------------------+


Compile kernel
----------------

Prepare compilation
~~~~~~~~~~~~~~~~~~~~~~

**Copy source code package to the development host**

|  Copy“linux source code” to “~/my-imx28/02_source”of Linux development host
|  This step should be done in your own way

**Decompress Linux source code package**

.. code-block:: shell

   $ cd ~/my-imx28/02_source/
   $ tar jxf linux-2.6.35.3.tar.bz2

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.1.2.1.png
   :alt: IMX28_2635_build_6.1.2.1.png

Configuration of kernel compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Validate configured file of compilation**

.. code-block:: shell

   $ source ~/my-imx28/03_tools/gcc-4.4.4-glibc-2.11.1-multilib-env

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.2.1.1.png
   :alt: IMX28_2635_build_6.2.1.1.png

**Remove kernel temporary file**

- Enter Linux source code directory

.. code-block:: shell

   $ cd ~/my-imx28/02_source/linux-2.6.35.3

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.2.2.1.png
   :alt: IMX28_2635_build_6.2.2.1.png

- Remove temporary file

.. code-block:: shell

   $ make distclean

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.2.2.2.png
   :alt: IMX28_2635_build_6.2.2.2.png

- Kernel configuration

.. code-block:: shell

   $ cp .mx28_config .config

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.2.3.1.png
   :alt: IMX28_2635_build_6.2.3.1.png

Compile kernel
~~~~~~~~~~~~~~~~

- Execute compilation

.. code-block:: shell

   $ make zImage -j4

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.3.0.1.png
   :alt: IMX28_2635_build_6.3.0.1.png

- Complete compilation

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.3.0.2.png
   :alt: IMX28_2635_build_6.3.0.2.png

- Target file

|  arch/arm/boot/uImage is the kernel file compiled，you can check the file information with ls command.

.. code-block:: shell

   $ ls arch/arm/boot/uImage -la

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.3.0.3.png
   :alt: IMX28_2635_build_6.3.0.3.png

Compile module
~~~~~~~~~~~~~~~~

- Command of module compilation

.. code-block:: shell

   $ make modules

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.4.0.1.png
   :alt: IMX28_2635_build_6.4.0.1.png

|  Install module to specified directory

.. code-block:: shell

   $ make modules_install INSTALL_MOD_PATH=./modules

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.4.0.2.png
   :alt: IMX28_2635_build_6.4.0.2.png

- Package module file

.. code-block:: shell

   $ cd modules
   $ tar cjf ../modules.tar.bz2 *

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_6.4.0.3.png
   :alt: IMX28_2635_build_6.4.0.3.png

Compile application
---------------------

Compilation of Linux application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Write application**

- Enter working directory

.. code-block:: shell

   $ cd ~/my-imx28/01_application/

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.1.1.png
   :alt: IMX28_2635_build_7.1.1.1.png

- Write source code

.. code-block:: shell

   $ vim hello.c

|  write and save the following code

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

**Compile application**

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

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_7.1.2.3.png
   :alt: IMX28_2635_build_7.1.2.3.png

|  You can see the property of target file hello.out

File system
-------------

File system rootfs.tar.bz2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Add your own application in following ways:（ copy MY-IMX28_Born_Tool\Profiles\MX28 Linux Update\OS Firmware\files\image-linux-2635/rootfs.tar.bz2 to the directory of “~/my-imx28/04_image/”）

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_8.1.0.1.png
   :alt: IMX28_2635_build_8.1.0.1.png

File system rootfs.ubifs
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Copy mkfs.ubifs，ubinize to“/usr/bin”directory of computer（copy is not needed if the computer has these two applications）；copy build_rootfs和ubinize.cfg to“~/my-imx28/04_image/”directory

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_8.2.0.1.png
   :alt: IMX28_2635_build_8.2.0.1.png

Burning way
-------------

|  So far，we get a set of programming files except file system from“~/my-imx28/02_source/”,including“imx28_ivt_uboot.sb”、“uImage”、“rootfs.tar.bz2”

Program with MFGTOOL
~~~~~~~~~~~~~~~~~~~~~~

|  Copy “imx28_ivt_uboot.sb”、“uImage”、“rootfs.tar.bz2 to the directory of “MY-IMX28_Born_Tool\Profiles\MX28 Linux Update\OS Firmware\files\image-linux-2635”。hold REC key,plug in MINI USB line and power line,then open MfgTool.exe,click"scan device",release REC key when HID device is detected,as below:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_9.1.0.1.png
   :alt: IMX28_2635_build_9.1.0.1.png

|  Click"Options" in the menu,select “MY-IMX28-2.6.35 NAND with uboot”in the option “Profiles”,then click"Enter",finally click"start"

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_9.1.0.2.png
   :alt: IMX28_2635_build_9.1.0.2.png

|  When programming is succeeded,click"stop",to finish.

``Note: if the file system you are using is rootfs-qt.tar.bz2,please choose “QT-MY-IMX28-2.6.35 NAND with uboot”as programming image.``


Program via network
~~~~~~~~~~~~~~~~~~~~~

**Establish TFTP (ubuntu system)**

|  (1) Setup tftp server files （download and isntall tftp）

.. code-block:: shell

   $ sudo apt-get install tftpd tftp openbsd-inetd

|  (2) make a tftp directory (establish tftp diretory and change its property)
|  Here we make /home/myzr/tftpt be a tftp directory.

.. code-block:: shell

   $ mkdir /home/myzr/tftp
   $ chmod 777 /home/myzr/tftp

|  (3) Open /etc/inetd.conf and edit it (modify tftp directory of congigured file)

.. code-block:: shell

   $ sudo gedit /etc/inetd.conf

|  Coment this line :
|  tftp dgram udp wait nobody /usr/sbin/tcpd /usr/sbin/in.tftpd /srv/tftp
|  Add new line:
|  tftp dgram udp wait nobody /usr/sbin/tcpd /usr/sbin/in.tftpd /home/myzr/tftp
|  (4)Restarting tftp service （重启tftp）

.. code-block:: shell

   $ sudo /etc/init.d/openbsd-inetd restart

**Establish NFS (nfs is not needed for network programming)**

|  (1) Install NFS server package (download and isntall nfs)

.. code-block:: shell

   $ sudo apt-get install nfs-kernel-server

|  (2) Create NFS directory:/home/myzr/nfsroot (establish nfs directory)

.. code-block:: shell

   $ mkdir /home/myzr/nfsroot

|  (3) Configure mounted directory and authority (modify nfs directory of configured file)

.. code-block:: shell

   $ sudo gedit /etc/exports

|  Add the following line at the end of the file:
|  /home/myzr/nfsroot \*(rw,sync,no_root_squash)

|  (4) Restart the NFS service (reboot nfs)

.. code-block:: shell

   $ sudo /etc/init.d/portmap restart
   $ sudo /etc/init.d/nfs-kernel-server restart

**Download of tftp**

|  (1) Copy“uImage” and “rootfs.ubifs”to“/home/myzr/tftp”directory
|  (2) Set environment variables(directly connect the board and computer)

.. code-block:: shell

   $ setenv ipaddr 192.168.3.104 （板子IP）
   $ setenv serverip 192.168.3.110 （电脑IP）

|  (3) Programme

.. code-block:: shell

   $ run upkernel (烧写uImage)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_9.2.3.1.png
   :alt: IMX28_2635_build_9.2.3.1.png

.. code-block:: shell

   $ run upsystem (programme file system)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_9.2.3.2.png
   :alt: IMX28_2635_build_9.2.3.2.png

Login way
-----------

Login via serial port
~~~~~~~~~~~~~~~~~~~~~~~

|  Plug in USB to serial port line and power supply,in about 12 seconds after machine starting,click Enter key to enter system.

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_10.1.0.1.png
   :alt: IMX28_2635_build_10.1.0.1.png

Login via ssh
~~~~~~~~~~~~~~~

**Login via ethernet**

|  (1)Plug in lan line and power supply, in about 10 seconds after machine starting,login via software SecureCRT,defaulted IP of ethernet by board is 192.168.3.104,you can set IP of computer as 192.168.3.110,then configure SecureCRT,enter root as user name and myzr as password, as blow:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_10.2.1.1.png
   :alt: IMX28_2635_build_10.2.1.1.png

|  (2)After entering, click"OK" to complete login

**Login via USB(USB can be identified as network port)**

|  (1)Plug in MINI USB line,in about 10 seconds after machine starting,login through software SecureCRT
|  (2)Add driving and set IP, as below:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_10.2.2.1.png
   :alt: IMX28_2635_build_10.2.2.1.png

|  (3)IP of USB of the board is 192.168.4.104，you can set IP of computer as 192.168.4.110，then configure SecureCRT，enter root as user name and myzr as password。as below：
|  After entering, click"OK" to complete login

Test
------

USB test
~~~~~~~~~~

|  Directly insert U disk,you can see the content of U disk after mounting,(if it is not QT system,mounting will be automatic)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.1.0.1.png
   :alt: IMX28_2635_build_11.1.0.1.png

SD card test
~~~~~~~~~~~~~~

|  Directly insert SD card,you can see the content of U SD card after mounting,(if it is not QT system,mounting will be automatic)

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.2.0.1.png
   :alt: IMX28_2635_build_11.2.0.1.png

Ethernet test
~~~~~~~~~~~~~~~

|  Insert lan line, test eth0 and eth1 with ping command directory,defaulted IP of eth0 is 192.168.3.104，let's set IP of eth1 as 192.168.3.105,as below:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.3.0.1.png
   :alt: IMX28_2635_build_11.3.0.1.png

Test of uart serial port
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Device of serial port uat0 is ttySP0, device of serial port uat3 is ttySP3,please short connect pins in the test

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.4.0.1.png
   :alt: IMX28_2635_build_11.4.0.1.png

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.4.0.2.png
   :alt: IMX28_2635_build_11.4.0.2.png

gpio Test
~~~~~~~~~~~

|  GPIO_2_26 is already configured as GPIO function in driving,below is taking GPIO_2_26 as an example to figure out the pin no. of GPIO_2_26 is 2*32+26=90,test as below:

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.5.0.1.png
   :alt: IMX28_2635_build_11.5.0.1.png

spi Test
~~~~~~~~~~

|  SPI interface is half duplex mode,here you only test sending,you can view the wave shape through oscilloscope,one way is to send 0x55 and 0x75,another way is to send charater string ”myzr“.

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.6.0.1.png
   :alt: IMX28_2635_build_11.6.0.1.png

watdog Test
~~~~~~~~~~~~~

|  "watchdog",the full name is Watchdog timer,is a hardware timer which can reset system of computer when there is an error in software.ususally in a normal time interval during a guading process of a user space,booting of Watchdog will be noticed to kernel through sepcial device file of /dev/watchdog,then everything in the user space is normal.
|  Open device file of /dev/watchdog in the test programme,start Watchdog,feed dog once a second,system won't reboot.

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.7.0.1.png
   :alt: IMX28_2635_build_11.7.0.1.png

|  Open device file of /dev/watchdog in the test programme,programme come into the cyccling condition,since there is not dog feeding,system will be resetted after 30 seconds.

.. figure:: /image/MYZR-其他/MYZR-IMX28-EK142/IMX28_2635_build_11.7.0.2.png
   :alt: IMX28_2635_build_11.7.0.2.png
