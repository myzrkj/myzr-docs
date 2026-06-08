Quick Start
=============

Instructions for Using This Document
--------------------------------------

- All participants in the project need to understand `other necessary documents`_.
- All personnel in the project who need to use the development board must understand and operate the `Quick Start for Using the Development Board`_.
- Software development engineers in the project (including BSP engineers and application software engineers) need to understand and complete the `Basic Guidelines for Software Development`_.
- BSP development engineers in the project need to understand the `Advanced Guidelines for Software Development`_.
- Hardware development engineers in the project need to read the `Hardware Development Guidelines`_.

Manual Links
~~~~~~~~~~~~~~~

- Startup Manuals: :doc:`《Linux-4.19.232》<L419232-Startup Manual>` :doc:`《Android11》<android11-Startup Manual>`
- Test Manuals: :doc:`《Linux-4.19.232》<L419232-Test Manual>` :doc:`《Android11》<android11-Test Manual>`
- Compilation Manuals: :doc:`《Linux-4.19.232》<L419232-Compilation Manual>` :doc:`《Android11》<android11-Compilation Manual>`
- Flashing Manuals: :doc:`《Linux-4.19.232》<L419232-Flashing Manual>` :doc:`《Android11》<android11-Flashing Manual>`

Other Instructions
~~~~~~~~~~~~~~~~~~~~

- For opening all links in the document, it is recommended to right-click the mouse and select "Open in New Tab".

Quick Start for Using the Development Board
---------------------------------------------

**Reading and completing the content and operations in this section for the first time will take approximately half a day.**

1. After receiving the development board, the first thing to do is prepare for using it, and installing terminal software is necessary. Open the :doc:`《XShell reference manual》</docs/COMMON/Xshell.RM Reference Manual >` and follow the "Software Download and Installation" section to install the terminal software.
2. After installing the terminal software, open the **"Startup Manual"** and follow the document to start the development board.
3. Once the development board starts successfully, open the corresponding **"Flashing Manual"** to perform a flashing operation. The purpose is to familiarize yourself with the burning process and prepare for the next functional verification.
4. After the development board is flashed, open the corresponding **"Test Manual"** to conduct a round of tests to verify that all functions of the development board are normal.

Basic Guidelines for Software Development
-------------------------------------------

**Reading and completing the content and operations in this section for the first time will take approximately half a day.**

1. First, for software development, a development environment needs to be established. Various problems may be encountered when setting up an embedded development environment. To avoid wasting unnecessary time and energy, we recommend using our virtual machine environment. Open the **"Development Environment Guide Manual"** and follow the document to configure the virtual machine.
2. After the development environment is set up, follow the **"Compilation Manual"** to perform a compilation and retain the resulting target files.
3. After compiling the target files, update them to the device, and it is advisable to conduct another test with reference to the **"Test Manual"** to verify that the compiled target files are correct.

Advanced Guidelines for Software Development
----------------------------------------------

After completing the `Quick Start for Using the Development Board`_ and `Basic Guidelines for Software Development`_, we will be familiar with the basic aspects. Then, the next step is to learn the content required for secondary development.

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Location of U-Boot board-level files: u-boot/board/rockchip/myzr_rk3568/
- U-Boot board-level configuration file: u-boot/include/configs/myzr_rk3568.h
- U-Boot board-level compilation configuration file: u-boot/configs/myzr-rk3568_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Kernel board-level compilation configuration file: kernel/arch/arm64/configs/myzr_rk_defconfig
- Kernel board-level device tree file: kernel/arch/arm64/boot/dts/rockchip/myzr-rk3568.dts
- Kernel development reference manual: docs/Kernel

Hardware Development Guidelines
----------------------------------

1. First, hardware engineers need to understand the introduction and basic principles of our development board's baseboard. For details, see the :doc:`《Baseboard Hardware Manual》<HM.MB314.Hardware Manual>`.
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or carry out designs based on our schematics.
3. If changes to certain interfaces or functions are required, refer to the **"Pin Definitions & Detailed Function Descriptions"** in the :doc:`《Core Board Hardware Manual》<HM.CB314.Hardware Manual>`.
4. For more detailed information, please refer to "05_Documentation Materials" in the network disk.

Other Necessary Documents
---------------------------

Developer Guide
~~~~~~~~~~~~~~~~~

- Location: docs/Rockchip_Developer_Guide_Linux_Software_CN.pdf


Datasheet
~~~~~~~~~~~

- Location in the network disk: docs/RK356X/Datasheet/*
