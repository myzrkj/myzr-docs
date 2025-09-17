Compilation Manual
====================


Compilation Environment Requirements
--------------------------------------

1. The compilation host must run on the Ubuntu system, and the version must be Ubuntu 20.04 or higher. My host system is Ubuntu 20.04.

2. The host must be able to connect to the external network, as the compilation process needs to download some files.


Downloading the Source Code Package
--------------------------------------

1. In the 02_Source Code directory of the network disk, download the source code package MYZR-RK3588_Android12_20240110.tar.bz2.

2. Create a compilation directory:

.. code-block:: shell

    mkdir ~/my-work/RK3588/05_android -p

3. Place the source code in this directory and extract it:

.. code-block:: shell

    tar xvf MYZR-RK3588_Android12_20240110.tar.bz2 -C ~/my-work/RK3588/05_android/



Configuring the Compilation Environment
------------------------------------------

1. Every time a new terminal is opened, environment configuration is required.

2. Enter the 3588-android12 directory.

3. Enter the following command to configure the Java environment:

.. code-block:: shell

    source javaenv.sh

4. Enter the following command to configure the compilation environment:

.. code-block:: shell

    source build/envsetup.sh

5. Enter the following command to configure the platform environment:

.. code-block:: shell

    lunch rk3588_s-userdebug


Overall Compilation
----------------------

1. The overall compilation will build the entire Android system, including the kernel, uboot, Android, and recovery.

2. Enter the following command:

.. code-block:: shell

    ./build.sh -AUCKu

3. The compilation time is relatively long. It took 4 hours to compile on my 16-thread host (for reference only!).

4. After successful compilation, you can see the relevant images in the rockdev/Image-rk3588_s/ directory, where update.img is a collection of all images.


Compiling U-Boot Separately
------------------------------

1. You can clear the generated files before compilation.

.. code-block:: shell

    cd u-boot/
    make clean

2. Return to the SDK main directory and compile U-Boot separately.

.. code-block:: shell

    cd ../
    ./build.sh -U


Compiling Kernel Separately
------------------------------

1. You can clear the generated files before compilation.

.. code-block:: shell

    cd kernel-5.10/
    make clean

2. Return to the SDK main directory and compile the kernel separately.

.. code-block:: shell

    cd ../
    ./build.sh -CKA

3. Or use the following command:

First, you need to install the gcc compiler.

.. code-block:: shell

    sudo apt-get install gcc-aarch64-linux-gnu

Enter the following command to compile:

.. code-block:: shell

    cd kernel-5.10/
    export PATH=../prebuilts/clang/host/linux-x86/clang-r416183b/bin:$PATH
    alias msk='make CROSS_COMPILE=aarch64-linux-gnu- LLVM=1 LLVM_IAS=1'
    msk ARCH=arm64 rockchip_defconfig
    msk ARCH=arm64 BOOT_IMG=../rockdev/Image-rk3588_s/boot.img myzr-rk3588.img -j24

Manually copy the image after compilation:

.. code-block:: shell

    cp boot.img ../rockdev/Image-rk3588_s/boot.img

    
Compiling Android Separately
-------------------------------

1. In the Android12 main directory:

.. code-block:: shell

    ./build.sh -A


Packaging update.img
----------------------

1. Package the image into update.img in rockdev.

2. In the Android12 main directory:

.. code-block:: shell

    ./build.sh -u
