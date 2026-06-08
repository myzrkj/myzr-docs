Compilation Manual
====================

Compilation Environment Requirements
--------------------------------------

1. The compilation host must run on the Ubuntu system, and the version must be Ubuntu 18.04 or higher. My host system is Ubuntu 18.04.

2. The host must be able to connect to the external network because the compilation process needs to download some files.


Downloading the Source Code Package
-------------------------------------

1. In the 02_Source Code directory of the network disk, download the source code package MYZR-RK3568_Android11_20240109.tar.bz2.

2. Create a compilation directory:

.. code-block:: shell

    mkdir ~/my-work/rk3568/05_android -p

3. Place the source code in this directory and extract it:

.. code-block:: shell

    tar xvf MYZR-RK3568_Android11_20240109.tar.bz2 -C ~/my-work/rk3568/05_android/


Configuring the Compilation Environment
-----------------------------------------

1. Every time a new terminal is opened, environment configuration is required.

2. Enter the RK356X_Android11 directory.

3. Enter the following command to configure the Java environment:

.. code-block:: shell

    source javaenv.sh

4. Enter the following command to configure the compilation environment:

.. code-block:: shell

    source build/envsetup.sh

5. Enter the following command to configure the platform environment:

.. code-block:: shell

    lunch rk3568_r-userdebug


Overall Compilation
----------------------

1. The overall compilation will build the entire Android system, including the kernel, uboot, Android, and recovery.

2. Enter the following command:

.. code-block:: shell

    ./build.sh -AUCKu

3. The compilation time is relatively long. It took 4 hours to compile on my 16-thread host (for reference only!).

4. After successful compilation, you can see the relevant images in the rockdev/Image-rk3568_r/ directory, where update.img is a collection of all images.


Compiling Uboot Separately
-----------------------------

1. You can clear the generated files before compilation.

.. code-block:: shell

    cd u-boot/
    make clean

2. Return to the SDK main directory and compile uboot separately.

.. code-block:: shell

    cd ../
    ./build.sh -U


Compiling Kernel Separately
------------------------------

1. You can clear the generated files before compilation.

.. code-block:: shell

    cd kernel/
    make clean

2. Return to the SDK main directory and compile the kernel separately.

.. code-block:: shell

    cd ../
    ./build.sh -CKA

3. Or use the kernel script for compilation.

.. code-block:: shell

    cd kernel/
    ./make.sh
    cp boot.img ../rockdev/Image-rk3568_r/boot.img


Compiling Android Separately
------------------------------

1. In the SDK main directory:

.. code-block:: shell

    ./build.sh -A


Packaging update.img
----------------------

1. Package the images into update.img in rockdev.

2. In the SDK main directory:

.. code-block:: shell

    ./build.sh -u
