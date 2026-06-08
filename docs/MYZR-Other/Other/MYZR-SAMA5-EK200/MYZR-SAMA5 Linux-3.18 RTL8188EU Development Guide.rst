MYZR-SAMA5 Linux-3.18 RTL8188EU Development Guide
===================================================

Prepare source code
---------------------

Download source code package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   在网盘下载 rtl8188EUS_linux_v4.3.0.9_15178.20150907.tar.xz

Decompress source code package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Create working directory**

|   Here we create ~/my-demo/exclude_src directory，and work under the directory.

.. code-block:: shell

    $ mkdir ~/my-demo/exclude_src -p

**Copy source code package to working directory**

|   Copy source code package downloaded to ~/my-demo/exclude_src .
|   Next step should be done in your own way.

**Decompress source code package**

- Enter source code directory.

.. code-block:: shell

    $ cd ~/my-demo/exclude_src

- Decompress

.. code-block:: shell

    $ tar xf rtl8188EUS_linux_v4.3.0.9_15178.20150907.tar.xz

Compilation module
---------------------

Check configuration
~~~~~~~~~~~~~~~~~~~~~~

|   Instruction：module compilation exist with two dependent relationships，cross compilation link and kernel，which need to be in the path designated.

- Validate configured file of compilation.

.. code-block:: shell

    $ source ~/my-sama5/03_tools/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.config

.. figure:: /image/MYZR-其他/MYZR-SAMA5-EK200/Myimx6linux3.14_build_5.2.1.1.png
   :alt: Myimx6linux3.14_build_5.2.1.1.png

- Check path of source code in kernel.

.. code-block:: shell

    $ ls ~/my-sama5/02_source/linux-at91-linux4sam_4.7

|   If there is kernel source code and in correct path then content of kernel source code directory can be found.
|   If result of execution of command is anormal，need to re-compife kernel with reference to《MYZR-SAMA5 L318 compilation manual》.

Compile
~~~~~~~~~

- Enter driving code directory.

.. code-block:: shell

    $ cd rtl8188EUS_linux_v4.3.0.9_15178.20150907/

- Execute compilation command

.. code-block:: shell

    $ make

Target file
~~~~~~~~~~~~~

- Check target file information

.. code-block:: shell

    $ file *.ko

|   Execute file command to see module information compiled，example.
|   8188eu.ko: ELF 32-bit LSB relocatable, ARM, version 1 (SYSV), BuildID[sha1]=0x1a3bbb865d785effc8acfebf9e2c8faf066b3fbf, not stripped
|   8188eu.ko is the target file compiled

WIFI test
----------

refer to :doc:`《MYZR-SAMA5 Linux-3.18 test manual》<MYZR-SAMA5-EK200 Linux-3.18 Test Manual>` 