Linux-4.4 编译手册
====================

**配置编译环境**

|   ubuntu14.04(64bit),已经真机编译验证过

搭建编译环境
~~~~~~~~~~~~~

- 下载安装ubuntu固件所需要的库

.. code-block:: shell
    
    $sudo apt-get install git-core gitk git-gui gcc-arm-linux-gnueabihf u-boot-tools device-tree-compiler \
    gcc-aarch64-linux-gnu mtools parted libudev-dev libusb-1.0-0-dev python-linaro-image-tools \
    linaro-image-tools gcc-4.8-multilib-arm-linux-gnueabihf gcc-arm-linux-gnueabihf libssl-dev \
    gcc-aarch64-linux-gnu g+conf autotools-dev libsigsegv2 m4 intltool libdrm-dev curl sed make \
    binutils build-essential gcc g++ bash patch gzip bzip2 perl tar cpio python unzip rsync file bc wget \
    libncurses5 libqt4-dev libglib2.0-dev libgtk2.0-dev libglade2-dev cvs git mercurial rsync openssh-client \
    subversion asciidoc w3m dblatex graphviz python-matplotlib libc6:i386 libssl-dev texinfo \
    liblz4-tool genext2fs lib32stdc++6

- 下载安装buildroot固件所需要的库

.. code-block:: shell

    $sudo apt-get install git-core gitk git-gui gcc-arm-linux-gnueabihf u-boot-tools device-tree-compiler \
    gcc-aarch64-linux-gnu mtools parted libudev-dev libusb-1.0-0-dev python-linaro-image-tools \
    linaro-image-tools autoconf autotools-dev libsigsegv2 m4 intltool libdrm-dev curl sed make \
    binutils build-essential gcc g++ bash patch gzip bzip2 perl tar cpio python unzip rsync file bc wget \
    libncurses5 libqt4-dev libglib2.0-dev libgtk2.0-dev libglade2-dev cvs git mercurial rsync openssh-client \
    subversion asciidoc w3m dblatex graphviz python-matplotlib libc6:i386 libssl-dev texinfo \
    liblz4-tool genext2fs lib32stdc++6 realpath

下载源码并解压
~~~~~~~~~~~~~~

.. code-block:: shell
    
    cat myrk3399_linux.tar.bz2.a* >> myrk3399_linux.tar.bz2
    sudo tar -xjvf myrk3399_linux.tar.bz2
    sudo chown myzr:myzr linux -R       (myzr是我的用户名，按实际修改)

配置文件介绍
~~~~~~~~~~~~~

|   配置文件在device/rockchip/rk3399目录下
|   myzr-rk3399.mk编译ubuntu镜像
|   myzr-rk3399-buildroot.mk编译buildroot镜像

|   配置文件有几个重要属性：

- 编译u-boot的配置文件

|   export RK_UBOOT_DEFCONFIG=myzr-rk3399

- 编译kernel配置文件

|   export RK_KERNEL_DEFCONFIG=myzr_linux_defconfig

- 编译kernel的设备树

|   export RK_KERNEL_DTS=rk3399-myzr-hdmi

- 分区信息

|   export RK_PARAMETER=parameter-ubuntu.txt

- 根文件系统镜像路径

|   export RK_ROOTFS_IMG=system/system.img

编译ubuntu镜像
~~~~~~~~~~~~~~~

- 设置配置文件

|   $./build.sh myzr-rk3399.mk
|   可以能过查看device/rockchip/.BoardConfig.mk文件确认是否正确设置配置文件

- 编译kernel

|   $./build.sh kernel
|   或者
|   $cd kernel
|   $make ARCH=arm64 rk3399-myzr-hdmi.img -j8

- 编译u-boot

|   $./build.sh uboot
|   或者
|   $cd u-boot
|   $./make.sh myzr-rk3399

- 整理镜像文件

|   $./mkfirmware.sh
|   可以在rockdev目录下查看

- 打包统一固件

|   $./build.sh updateimg
|   可以在rockdev目录下查看update.img文件

编译buildroot镜像
~~~~~~~~~~~~~~~~~~

- 设置配置文件

|   $./build.sh myzr-rk3399-buildroot.mk

- 编译内核

|   $./build.sh kernel
|   或者
|   $cd kernel
|   $make ARCH=arm64 rk3399-myzr-hdmi.img -j8

- 编译u-boot

|   $./build.sh uboot
|   或者
|   $cd u-boot
|   $./make.sh myzr-rk3399

- 编译buildroot

|   $./build.sh rootfs

- 整理镜像文件

|   $./build.sh recovery
|   $./mkfirmware.sh
|   可以在rockdev目录下查看

- 打包统一固件

|   $./build.sh updateimg
|   可以在rockdev目录下查看update.img文件