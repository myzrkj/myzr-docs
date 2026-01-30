Compilation Manual
====================

Compilation Environment Requirements:
----------------------------------------

|   The compilation host must be running the Ubuntu system. The author's host system is Ubuntu 22.04. It is recommended to use the same version of Ubuntu as the author to avoid compatibility issues with some tools due to different versions.

Installing Libraries and Toolkits:
-------------------------------------

.. code-block:: shell

    sudo apt-get update && sudo apt-get install git ssh make gcc libssl-dev \
    liblz4-tool expect expect-dev g++ patchelf chrpath gawk texinfo chrpath \
    diffstat binfmt-support qemu-user-static live-build bison flex fakeroot \
    cmake gcc-multilib g++-multilib unzip device-tree-compiler ncurses-dev \
    libgucharmap-2-90-dev bzip2 expat gpgv2 cpp-aarch64-linux-gnu libgmp-dev \
    libmpc-dev bc python-is-python3 python2 gettext libc6-dev libncurses-dev rsync

- (Python version requirement: Python 3.6 or higher)
- (Make version requirement: Make 4.0 or higher)
- (lz4 version requirement: lz4 1.7.3 or higher)

Downloading the Source Package
---------------------------------

1. Download the RV1126b source package.
2. Create a compilation directory:

.. code-block:: shell

    mkdir -p ~/my-work/RV1126b/

3. Place the source code into the newly created directory, merge the split compressed source code files, and then extract them:

.. code-block:: shell

    cat myzr-rv1126b.tar.gz.part-* > myzr-rv1126b.tar.gz

    tar xvf myzr-rv1126b.tgz -C ~/my-work/RV1126b/

Linux System Image Compilation and Generation
------------------------------------------------

.. code-block:: shell

    ## View specific compilation commands
    ./build.sh 

.. code-block:: shell

    ## Select the corresponding board-level configuration
    ./build.sh lunch

.. code-block:: shell

    ## Global compilation and image packaging
    ./build.sh 

.. code-block:: shell

    ## Perform only global compilation without firmware packaging
    ./build.sh all

.. code-block:: shell

    ## Perform only firmware packaging
    ./build.sh firmware

.. code-block:: shell

    ## Compile U-Boot separately
    ./build.sh uboot

.. code-block:: shell

    ## Compile Kernel separately
    ./build.sh kernel

.. code-block:: shell

    ## Compile buildroot separately
    ./build.sh rootfs

.. code-block:: shell

    ## Compile recovery separately
    ./build.sh recovery