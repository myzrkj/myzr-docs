Software Development Guide
=============================

Compilation Manual
--------------------

1. Download the source code: Open the network disk and go to 3.Software Materials -> linux-5.4 (ubuntu), then download the 3.4-Source Code directory.
2. After extracting the downloaded SDK compressed package MYZR-H618-EK120_20250812.tar.gz, enter the directory myzr-h618-ek120

.. code-block:: shell

    cd myzr-h618-ek120

|   In the myzr-h618-ek120 directory, run the compilation script

.. code-block:: shell

    ./build.sh

|   You can see the following options

.. figure:: /image/MYZR-全志系列/MYZR-H618-EK120/编译固件1.png
   :alt: 编译固件1.png

|   For the first compilation, it is recommended to select "Build all step", press Enter, then select the development board model and the type of system to be built, and press Enter. The compilation script will automatically complete the entire process of compilation and packaging. You can also build step by step, from step1 to step4.

|   After the compilation is completed, you can find the generated image in the following path, for example:

.. code-block:: shell

    myzr-h618-ek120/out/images/myzr-h618-ek120-*/myzr-h618-ek120-*.img