
MYZR-RK3399-EK314 Linux-4.4 Build Manual
==========================================

Configure the compilation environment
---------------------------------------

Build a compilation environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Compile ubuntu firmware

.. code:: shell
    
    $sudo apt-get install git-core gitk git-gui gcc-arm-linux-gnueabihf u-boot-tools device-tree-compiler \
    gcc-aarch64-linux-gnu mtools parted libudev-dev libusb-1.0-0-dev python-linaro-image-tools \
    linaro-image-tools gcc-4.8-multilib-arm-linux-gnueabihf gcc-arm-linux-gnueabihf libssl-dev \
    gcc-aarch64-linux-gnu g+conf autotools-dev libsigsegv2 m4 intltool libdrm-dev curl sed make \
    binutils build-essential gcc g++ bash patch gzip bzip2 perl tar cpio python unzip rsync file bc wget \
    libncurses5 libqt4-dev libglib2.0-dev libgtk2.0-dev libglade2-dev cvs git mercurial rsync openssh-client \
    subversion asciidoc w3m dblatex graphviz python-matplotlib libc6:i386 libssl-dev texinfo \
    liblz4-tool genext2fs lib32stdc++6

- Compile buildroot firmware

.. code:: shell

    $sudo apt-get install git-core gitk git-gui gcc-arm-linux-gnueabihf u-boot-tools device-tree-compiler \
    gcc-aarch64-linux-gnu mtools parted libudev-dev libusb-1.0-0-dev python-linaro-image-tools \
    linaro-image-tools autoconf autotools-dev libsigsegv2 m4 intltool libdrm-dev curl sed make \
    binutils build-essential gcc g++ bash patch gzip bzip2 perl tar cpio python unzip rsync file bc wget \
    libncurses5 libqt4-dev libglib2.0-dev libgtk2.0-dev libglade2-dev cvs git mercurial rsync openssh-client \
    subversion asciidoc w3m dblatex graphviz python-matplotlib libc6:i386 libssl-dev texinfo \
    liblz4-tool genext2fs lib32stdc++6 realpath

Download the source code and extract it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell
    
    cat myrk3399_linux.tar.bz2.a* >> myrk3399_linux.tar.bz2
    tar -xjvf myrk3399_linux.tar.bz2
    sudo chown myzr:myzr linux -R

Configuration file introduction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   The configuration file is in the device/rockchip/rk3399
|   myzr-rk3399.mk compile ubuntu image
|   myzr-rk3399-buildroot.mk compile buildroot image

|   The configuration file has several important attributes:

- Compile u-boot configuration file

|   export RK_UBOOT_DEFCONFIG=myzr-rk3399

- Compile the kernel configuration file

|   export RK_KERNEL_DEFCONFIG=myzr_linux_defconfig

- Compile kernel device tree

|   export RK_KERNEL_DTS=rk3399-myzr-hdmi

- Partition information

|   export RK_PARAMETER=parameter-ubuntu.txt

- Root file system mirror path

|   export RK_ROOTFS_IMG=system/system.img

Compile ubuntu image
~~~~~~~~~~~~~~~~~~~~~

- Set up a profile

|   $./build.sh myzr-rk3399.mk
|   You can check the device / rockchip / .BoardConfig.mk file to confirm that the configuration file is set correctly

- Compile kernel

|   $./build.sh kernel
|   Another way
|   $cd kernel
|   $make ARCH=arm64 rk3399-myzr-hdmi.img -j8

- Compile u-boot

|   $./build.sh uboot
|   Another way
|   $cd u-boot
|   $./make.sh myzr-rk3399

- Organize mirror files

|   $./mkfirmware.sh
|   You can view it in the rockdev directory

- Package unified firmware

|   $./build.sh updateimg
|   You can view the update.img file in the rockdev directory

Compile buildroot image
~~~~~~~~~~~~~~~~~~~~~~~~~

- Set up a profile

|   $./build.sh myzr-rk3399-buildroot.mk

- Compile the kernel

|   $./build.sh kernel
|   Another way
|   $cd kernel
|   $make ARCH=arm64 rk3399-myzr-hdmi.img -j8

- Compile u-boot

|   $./build.sh uboot
|   Another way
|   $cd u-boot
|   $./make.sh myzr-rk3399

- Compile buildroot

|   $./build.sh rootfs

- Organize mirror files

|   $./build.sh recovery
|   $./mkfirmware.sh
|   You can view it in the rockdev directory

- Package unified firmware

|   $./build.sh updateimg
|   You can view the update.img file in the rockdev directory