.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Software Development Guide
==========================

Building the Manual
-------------------

Compile environment
~~~~~~~~~~~~~~~~~~~

#. Ubuntu version: ubuntu20.04

#. Packages installation

   .. code-block:: text

      sudo apt-get install libc6-dev-i386 lib32z1  libuuid1 cmake libncurses5-dev libncursesw5-dev bc xz-utils automake libtool libevdev-dev pkg-config mtd-utils  bison flex libssl-dev libmpc-dev squashfs-tools gawk make gcc git python rename

#. The compilation script uses bash by default. The default shell of the system is required to be bash, which can be confirmed by using the ``ls -la /bin/sh`` command. Take the most commonly used Ubuntu as an example. The default shell of higher version of Ubuntu is dash. The modification method is as follows:

   .. code-block:: shell

      $ ls -la /bin/sh
      lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> dash
      $ sudo dpkg-reconfigure dash
      #In the pop-up interface, select<NO>
      $ ls -la /bin/sh
      lrwxrwxrwx 1 root root 4 Jun 15 08:49 /bin/sh -> bash

Set the default python version to python2.x (ubuntu20.04 does not need to be configured, the default is python2.x)

The semantics of python2 and python3 are different. The SDK compilation script uses the semantics of python2, so you need to set the system default python version to python2.x. Please refer to the relevant documents on the network for modification, such as using the update-alternatives tool to configure.

Source code and cross-compilation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Set up cross-compilation tools

   .. code-block:: shell

      export PATH=/home/surs/my-work/ssd2355/tool/toolchain/aarch64-unknown-linux-gcc-12.4.0-glibc-2.37-gnu/bin:$PATH
      export CROSS_COMPILE=aarch64-unknown-linux-gnu-12.4.0-
      export ARCH=arm64
      ${CROSS_COMPILE}gcc -v

Global compilation
~~~~~~~~~~~~~~~~~~

#. kernel Device Tree file

#. menuconfig configuration