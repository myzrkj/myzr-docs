MYZR-SSD2351-EK112 Compilation Manual
=======================================

Installing Software Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Ubuntu version: ubuntu20.04
| Software package installation:

.. code-block:: shell

   $ sudo apt-get install libc6-dev-i386 lib32z1  libuuid1 cmake libncurses5-dev libncursesw5-dev bc xz-utils automake libtool libevdev-dev pkg-config mtd-utils  bison flex libssl-dev libmpc-dev squashfs-tools gawk make gcc git python rename

| Other configurations:
| a. Default shell configuration

| The compilation script uses bash by default, requiring the system's default shell to be bash. You can confirm this with the command ls -la /bin/sh. Taking the commonly used Ubuntu as an example, newer versions of Ubuntu use dash as the default shell. To modify this:

.. code-block:: shell

   $ ls -la /bin/sh
   lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> dash

   $ sudo dpkg-reconfigure dash
   #Select <NO> in the pop-up interface

   $ ls -la /bin/sh
   lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> bash

| b. Set default python version to python2.x (No configuration needed for ubuntu20.04 as it defaults to python2.x)
| There are semantic differences between python2 and python3. The SDK compilation script uses python2 semantics, so you need to set the system's default python version to python2.x. For modification methods, refer to relevant documents online, such as using the update-alternatives tool for configuration.

Extracting Source Code and Cross-Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| boot-Pcupid_DLD00V2.3.3*.tar.gz: Uboot source code
| kernel-Pcupid_DLD00V2.3.3*.gz: kernel source code
| project-Pcupid_DLD00V2.3.3*.tar.gz: Part for compiling and creating images, including non-open source lib/ko, and reference for external API headers (squashfs compiles into a read-only system, ubifs compiles into a read-write system; ubifs version is recommended)
| sdk-Pcupid_DLD00V2.3.3*.tar.gz: Test Demo/application packaging framework part
| aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu.tar.xz: Cross-compilation tool

.. code-block:: shell

   $ mkdir ~/ssd2351/source -p
   $ tar zxvf boot-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source 
   $ tar zxvf kernel-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source
   $ tar zxvf project-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source 
   $ tar zxvf sdk-Pcupid_DLD00V2.3.3*.tar.gz -C ~/ssd2351/source
   $ mkdir ~/ssd2351/tool/toolchain -p
   $ tar -xvf ./aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu.tar.xz -C ~/ssd2351/tool/toolchain

Setting Up Cross-Compilation Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   $ export PATH=~/ssd2351/tool/toolchain/aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu/bin:$PATH
   $ export CROSS_COMPILE=aarch64-unknown-linux-gnu-12.4.0-
   $ export ARCH=arm64
   $ ${CROSS_COMPILE}gcc -v

Global Compilation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   #Global compilation, will compile boot, kernel, project, and sdk when run
   $ cd ~/ssd2351/source/project/
   $ make myzr-ssd2351-ek112_128m_defconfig    (ddr; 128M)
   or
   $ make myzr-ssd2351-ek112_256m_defconfig    (ddr; 256M)
   $ make clean;make image -j8

   #Generated images after compilation are in project/image/output/images
   #Note:
   #For the first compilation, be sure to execute make clean;make image -j8 in the project directory for a complete compilation (including full compilation of boot/kernel)
   #To improve debugging efficiency, after the first compilation, subsequent debugging can directly compile the modified modules in the project directory and then repackage quickly, for example:

   #Compile only kernel:
   $ cd ~/ssd2351/source/project/
   $ make linux-kernel_clean;make linux-kernel -j8

   #Compile only boot:
   $ cd ~/ssd2351/source/project/
   $ make boot_clean;make boot -j8

   #Quickly package only sdk image:
   $ cd ~/ssd2351/source/project/
   $ make image-fast-nocheck -j8


Separate Compilation of boot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   #The SDK compilation in the project has added boot compilation options, so it is recommended that after modifying boot, directly compile boot using make boot in the project directory. After compilation, there's no need to manually release it to the project directory; just repackage the project. Besides compiling in the project, you can also compile in the boot directory as follows:
   $ cd ~/ssd2351/source/boot
   $ make pcupid_ssm001c_s01a_spinand_arm64_defconfig
   $ make clean;make -j8;
   #Note: When compiling separately in the boot directory, you need to manually release the generated image to the corresponding project directory before packaging
   $ cp ~/ssd2351/source/boot/u-boot_spinand.xz.img.bin ~/ssd2351/source/project/board/uboot/u-boot.xz.img.bin


Separate Compilation of kernel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   #The SDK compilation in the project has added kernel compilation options, so it is recommended that after modifying the kernel, directly compile the kernel using make linux-kernel in the project directory. After compilation, there's no need to manually release it to the project directory; just repackage the project. Besides compiling in the project, you can also compile in the kernel directory as follows:
   $ cd ~/ssd2351/source/kernel
   $ make pcupid_ssm001c_s01a_spinand_voip_defconfig
   $ make clean;make image -j8;
   #Note: The packaging in the project directly uses a soft link to the kernel directory, so there's no need to manually release the kernel; just perform the project packaging
   #If new kernel modules are added to the kernel, the corresponding modules need to be added to kernel_mod_list/kernel_mod_list_late (ko files in kernel_mod_list_late will be loaded after mi modules)

   #Modification path: project/kbuild/customize/6.1/pcupid/dispcam/kernel_mod_list 

Generating USB Burning Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   #Compile the entire sdk package according to the normal process to generate the image upgrade file.
   #After successful compilation of the entire sdk package, execute the ./image/makefiletools/script/make_usb_factory_sigmastar.sh script
   #You can choose full upgrade or partial partition upgrade: (y for full update, n for partial update)
   $ cd ~/ssd2351/source/project/
   $ ./image/makefiletools/script/make_usb_factory_sigmastar.sh
   Prompt:
   Full or Optional Upgrade ? (Y/N)y
   using alone TF-A:u-bl31.bin
   USB Facotry Image Generating.....
   success, usb factory image have generated:
         path:./image/output/images/SstarUsbImage_202502280425.bin
         size:48439296 byte
         md5sum:057c1f55ecbe0a4ecaaa916a8612bfe2

uboot Configuration, Device Tree, and Kernel Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   #uboot configuration:
   Configuration: pcupid_ssm001c_s01a_spinand_arm64_defconfig
   Device tree: pcupid-ssm001c-s01a.dts
   #kernel configuration
   Configuration: pcupid_ssm001c_s01a_spinand_voip_defconfig
   Device tree: pcupid-ssm001c-s01a-voip.dts