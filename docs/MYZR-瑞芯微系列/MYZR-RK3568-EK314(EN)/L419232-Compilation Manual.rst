Compilation Manual
=====================

Compilation Environment Requirements
---------------------------------------

1. The compilation host must run on an Ubuntu system with version 18.04 or higher. My host system is Ubuntu 18.04.

2. The host must have access to the internet, as the compilation process requires downloading certain files.


Downloading the Source Code Package
-------------------------------------

1. From the 02_Source Code directory in the network drive, download the source code package MYZR-RK3568_Linux-4.19_20240108.tar.bz2.

2. Create a compilation directory:

.. code-block:: shell

    mkdir ~/my-work/rk3568/02_sources -p

3. Place the source code in this directory and extract it:

.. code-block:: shell

    tar xvf MYZR-RK3568_Linux-4.19_20240108.tar.bz2 -C ~/my-work/rk3568/02_sources/


Dependency Installation
-------------------------

1. First-time compilation may require installing certain dependencies. Below are some dependencies that may need to be installed on the host:

.. code-block:: shell
    
    sudo apt-get install repo git ssh make gcc libssl-dev liblz4-tool \
    expect g++ patchelf chrpath gawk texinfo chrpath diffstat binfmt-support \
    qemu-user-static live-build bison flex fakeroot cmake gcc-multilib g++-multilib \
    unzip \
    device-tree-compiler ncurses-dev \


SDK Configuration Loading
---------------------------

1. First-time compilation requires loading the SDK configuration file.

2. Enter the RK356X_Linux directory.

3. Enter the following command to load the configuration file:

.. code-block:: shell

    ./build.sh BoardConfig-rk3568-myzr.mk


Full Compilation
------------------

1. Full compilation compiles the entire SDK in one go, including the kernel, uboot, rootfs, and recovery.

2. Enter the following command:

.. code-block:: shell

    ./build.sh

3. The compilation time is relatively long. It took 3 hours to compile on my 24-thread host (for reference only!).

4. After successful compilation, relevant images can be found in the rockdev/ directory, where update.img is a collection of all images.


Compiling U-Boot Separately
-----------------------------

1. You can clear generated files before compilation:

.. code-block:: shell

    cd u-boot/
    make clean

2. Return to the SDK main directory and compile U-Boot separately:

.. code-block:: shell

    cd ../
    ./build.sh uboot


Compiling Kernel Separately
-----------------------------

1. You can clear generated files before compilation:

.. code-block:: shell

    cd kernel/
    make clean

2. Return to the SDK main directory and compile the kernel separately:

.. code-block:: shell

    cd ../
    ./build.sh kernel


Compiling Recovery Separately
-------------------------------

1. In the SDK main directory:

.. code-block:: shell

    ./build.sh recovery

    
Compiling Buildroot Separately
---------------------------------

1. In the SDK main directory:

.. code-block:: shell

    ./build.sh rootfs


Packaging Firmware
---------------------

1. Package the firmware. Link related images to the rockdev directory.

2. In the SDK main directory:

.. code-block:: shell

    ./mkfirmware.sh


Packaging update.img
----------------------

1. Package images into update.img in rockdev.

2. In the SDK main directory:

.. code-block:: shell

    ./build.sh updateimg
