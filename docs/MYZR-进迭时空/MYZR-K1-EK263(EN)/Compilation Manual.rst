Compilation Manual
====================

Development Environment
-------------------------

Operating System
~~~~~~~~~~~~~~~~~~~

|  Recommended OS: Ubuntu 20.04

Dependency Installation
~~~~~~~~~~~~~~~~~~~~~~~~~

|  Ubuntu 20.04 or higher:

.. code-block:: shell

    sudo apt-get install git build-essential cpio unzip rsync file bc wget python3 python-is-python3 libncurses5-dev libssl-dev dosfstools mtools u-boot-tools flex bison python3-pip
    sudo pip3 install pyyaml

Configuration
~~~~~~~~~~~~~~~

**buildroot**

|  Configuration:

.. code-block:: shell

    make menuconfig

|  Save configuration, default path: buildroot-ext/configs/spacemit_k1_v2_defconfig:

.. code-block:: shell

    make savedefconfig

**linux**

|  Configuration:

.. code-block:: shell

    make linux-menuconfig

|  Save configuration, default path: bsp-src/linux-6.6/arch/riscv/configs/k1_defconfig

.. code-block:: shell

    make linux-update-defconfig

**u-boot**

|  Configuration:

.. code-block:: shell

    make uboot-menuconfig

|  Save configuration, default path: bsp-src/uboot-2022.10/configs/k1_defconfig

.. code-block:: shell

    make uboot-update-defconfig

Full Compilation
-------------------

.. code-block:: shell

    make envconfig

|  Output file: bianbu-linux-2.2/output/k1_v2/images/bianbu-linux-k1_v2.zip.

Separate Compilation
----------------------

Compile Specified Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Compile Linux Kernel:**

.. code-block:: shell

    make linux-rebuild

**Compile U-Boot:**

.. code-block:: shell

    make uboot-rebuild

|  After compiling the specified package, run the following command to package files into bianbu-linux-2.2/output/k1_v2/images/bianbu-linux-k1_v2.zip.

.. code-block:: shell

    make

**Compile k1x-cam**

.. code-block:: shell

    make k1x-cam-rebuild

|  Buildroot supports compiling designated packages. Run make help for more instructions.

Independent GCC Compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Environment Setup**

|  Cross toolchain download: http://archive.spacemit.com/toolchain/, extract and use directly.
|  Example: spacemit-toolchain-linux-glibc-x86_64-v1.0.0.tar.xz

.. code-block:: shell

    sudo tar -Jxf /path/to/spacemit-toolchain-linux-glibc-x86_64-v1.0.0.tar.xz -C /opt

|  Set environment variables:

.. code-block:: shell

    export PATH=/opt/spacemit-toolchain-linux-glibc-x86_64-v0.3.3/bin:$PATH
    export CROSS_COMPILE=riscv64-unknown-linux-gnu-
    export ARCH=riscv

**Compile OpenSBI**

.. code-block:: shell

    cd bsp-src/opensbi
    make -j$(nproc) PLATFORM_DEFCONFIG=k1_defconfig PLATFORM=generic

|  Output file: platform/generic/firmware/fw_dynamic.itb.

**Compile U-Boot**

.. code-block:: shell

    cd bsp-src/uboot-2022.10
    make k1_defconfig
    make -j$(nproc)

|  Generates u-boot-env-default.bin according to board/spacemit/k1-x/k1-x.env (env partition image), as well as FSBL.bin and u-boot.itb.

**Compile Linux**

.. code-block:: shell

    cd bsp-src/linux-6.6
    make k1_defconfig
    LOCALVERSION="" make -j$(nproc)

|  Output files: Image and k1-x_deb1.dtb.