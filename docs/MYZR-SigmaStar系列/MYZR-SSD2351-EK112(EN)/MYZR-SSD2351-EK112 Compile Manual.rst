MYZR-SSD2351-EK112 Compile Manual
===================================

Install Package
~~~~~~~~~~~~~~~~~

|  Ubuntu Version: ubuntu20.04
|  Package Installation:

.. code-block:: shell

   $ sudo apt-get install libc6-dev-i386 lib32z1  libuuid1 cmake libncurses5-dev libncursesw5-dev bc xz-utils automake libtool libevdev-dev pkg-config mtd-utils  bison flex libssl-dev libmpc-dev squashfs-tools gawk make gcc git python rename

|  Other Configurations:
|  a. Default shell configuration
|  The compilation script uses bash by default, requiring the system's default shell to be bash, which can be confirmed via the `ls -la /bin/sh` command. Taking the most commonly used Ubuntu as an example, the default shell for higher versions of Ubuntu is dash, and the modification method is as follows: 

.. code-block:: shell

   $ ls -la /bin/sh
   lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> dash

   $ sudo dpkg-reconfigure dash
   #Select on the pop-up interface<NO>

   $ ls -la /bin/sh
   lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> bash

|  b. Set the default Python version to Python 2.x (Ubuntu 20.04 does not require configuration as it defaults to Python 2.x)
|  There are semantic differences between Python 2 and Python 3, and the SDK compilation script uses Python 2 semantics. Therefore, it is necessary to set the system's default Python version to Python 2.x. For the modification method, please refer to relevant documents on the internet, such as using the update-alternatives tool for configuration.

Unzip the source code and cross-compile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  boot-Pcupid_DLD00V2.2.9.tar.gz: Uboot Source Code
|  kernel-Pcupid_DLD00V2.2.9.tar.gz: kernel source
|  project-Pcupid_DLD00V2.2.9.tar.gz: The part for compiling and creating the image, including lib/ko of non-open-source parts and reference to external API Header Files
|  sdk-Pcupid_DLD00V2.2.9.tar.gz: Test Demo/Application Packaging Framework Section
|  arm-sigmastar-linux-gcc-12.4.0-uclibc-1.0.46-gnueabihf.tar.xz: Cross-compilation tool

.. code-block:: shell

   $ mkdir ~/ssd2351/source -p
   $ tar zxvf boot-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source 
   $ tar zxvf kernel-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source
   $ tar zxvf project-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source 
   $ tar zxvf sdk-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source
   $ mkdir ~/ssd2351/tool/toolchain -p
   $ tar -xvf ./aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu.tar.xz -C ~/ssd2351/tool/toolchain

Set up cross-compilation tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ export PATH=~/ssd2351/tool/toolchain/aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu/bin:$PATH
   $ export CROSS_COMPILE=aarch64-unknown-linux-gnu-12.4.0-
   $ export ARCH=arm64
   $ ${CROSS_COMPILE}gcc -v

Global Compile
~~~~~~~~~~~~~~~~~


|  Global compilation, as long as it runs, it will compile boot, kernel, project, and SDK

.. code-block:: shell

   $ cd ~/ssd2351/source/project/
   $ make myzr-ssd2351-ek112_128m_defconfig    (ddr；128M)
   or
   $ make myzr-ssd2351-ek112_256m_defconfig    (ddr；256M)
   $ make clean;make image -j8

|  The generated images after compilation are displayed in project/image/output/images
|  Note：
|  For the first compilation, be sure to run make clean under project; make image -j8 command fully compiled (including the whole boot/kernel)
|  In order to increase the efficiency of debugging, in addition to the first compilation, subsequent debugs can be directly compiled under the project and then quickly packaged, such as:

|  Compile only the kernel:

.. code-block:: shell

   $ cd ~/ssd2351/source/project/
   $ make linux-kernel_clean;make linux-kernel -j8

|  Compile boot only:

.. code-block:: shell

   $ cd ~/ssd2351/source/project/
   $ make boot_clean;make boot -j8

|  Quickly package the SDK image only:

.. code-block:: shell

   $ cd ~/ssd2351/source/project/
   $ make image-fast-nocheck -j8


Separate compilation of boot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The boot compilation option has been added to the SDK compilation under project, so it is recommended that after the boot is modified, directly compile under the project using make boot to compile boot. In addition to compiling in project, you can also compile in the boot directory as follows:

.. code-block:: shell

   $ cd ~/ssd2351/source/boot
   $ make pcupid_ssm001c_s01a_spinand_arm64_defconfig
   $ make clean;make -j8;

|  Note: To compile separately in the boot directory, you need to manually release the generated image to the corresponding directory of the project before packaging
   
.. code-block:: shell

   $ cp ~/ssd2351/source/boot/u-boot_spinand.xz.img.bin ~/ssd2351/source/project/board/uboot/u-boot.xz.img.bin


Separate compilation kernels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  The kernel compilation option has been added to the SDK compilation under the project, so it is recommended that after the kernel is modified, directly compile under the project and use make linux-kernel to compile the kernel. In addition to compiling in Project, you can also compile in the kernel directory as follows:

.. code-block:: shell

   $ cd ~/ssd2351/source/kernel
   $ make pcupid_ssm001c_s01a_spinand_voip_defconfig
   $ make clean;make image -j8;
 
|  Note: The package in the project is the kernel directory pointed directly to by the soft link, so the kernel does not need to be manually released, just do the project packaging action
|  If there are new kernel modules in the kernel, you need to add the corresponding module to the kernel_mod_list/kernel_mod_list_late (the ko in the kernel_mod_list_late will be loaded after the mi module)

|  Modify the path: project/kbuild/customize/6.1/pcupid/dispcam/kernel_mod_list

Generate USB burning mirroring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Compile the entire SDK package according to the normal process to generate the mirroring upgrade file.
|  After the entire package SDK is successfully compiled, execute the script./image/makefiletools/script/make_usb_factory_sigmastar.sh
|  You can choose between full upgrade and partial partition upgrade: (y for full update, n for partial update)

.. code-block:: shell

   $ cd ~/ssd2351/source/project/
   $ ./image/makefiletools/script/make_usb_factory_sigmastar.sh

|  Tip：

.. code-block:: shell

   Full or Optional Upgrade ? (Y/N)y
   using alone TF-A:u-bl31.bin
   USB Facotry Image Generating.....
   success, usb factory image have generated:
         path:./image/output/images/SstarUsbImage_202502280425.bin
         size:48439296 byte
         md5sum:057c1f55ecbe0a4ecaaa916a8612bfe2
