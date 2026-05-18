Quick Start
=============

Instructions for Using This Document
---------------------------------------

- **All personnel involved** in the project need to understand the `Other Necessary Documents`_.
- **All personnel who need to use the development board** in the project need to understand and follow the `Quick Start Guide for Development Board Usage`_.
- **Software development engineers** in the project (including BSP engineers and application software engineers) need to understand and complete the `Basic Guide for Software Development`_.
- **BSP development engineers** in the project need to understand the `Advanced Guide for Software Development`_.
- **Hardware development engineers** in the project need to read the `Hardware Development Guide`_.

Manual Links
~~~~~~~~~~~~~~~

- Startup Manual: :doc:`《Linux-5.10.110》<L510110-Startup Manual>` :doc:`《Android12》<android12-Startup Manual>`
- Test Manual: :doc:`《Linux-5.10.110》<L510110-Test Manual>` :doc:`《Android12》<android12-Test Manual>`
- Compilation Manual: :doc:`《Linux-5.10.110》<L510110-Compilation Manual>` :doc:`《Android12》<android12-Compilation Manual>`
- Flashing Manual: :doc:`《Linux-5.10.110》<L510110-Firmware Flashing Manual>` :doc:`《Android12》<android12-Firmware Flashing Manual>`

Additional Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

- For opening all links in the document, it is recommended to **right-click the mouse and select "Open in a new tab"**.

Quick Start Guide for Development Board Usage
------------------------------------------------

**Reading through and completing the content and operations in this section for the first time will take approximately half a day.**

1. After receiving the development board, the first thing to do is prepare for using it, and installing terminal software is essential. Open :doc:`《Xshell Reference Manual》</docs/COMMON/Xshell.RM Reference Manual >` and follow the instructions in the **Software Download and Installation** section to install the terminal software.
2. After installing the terminal software, open the **《Startup Manual》** and follow the document to start the development board.
3. Once the development board starts successfully, open the corresponding **【Flashing Manual】** and perform a flashing operation. The purpose is to familiarize yourself with the burning process and prepare for the next function verification.
4. After the development board flashing is completed, open the corresponding **【Test Manual】** and conduct a round of tests to verify that all functions of the development board are normal.

Basic Guide for Software Development
---------------------------------------

**Reading through and completing the content and operations in this section for the first time will take approximately half a day.**

1. First, to carry out software development, it is necessary to set up a development environment. Various problems may be encountered when building an embedded development environment. To avoid wasting unnecessary time and energy, we recommend using our virtual machine environment here. Open the **【Development Environment Guide Manual】** and follow the document to configure the virtual machine properly.
2. After setting up the development environment, you should refer to the **【Compilation Manual】** to perform a compilation and retain the target files obtained from the compilation.
3. After compiling the target files, update the target files to the device, and it is advisable to refer to the **【Test Manual】** to conduct another test to verify that the compiled target files are free of issues.

Advanced Guide for Software Development
------------------------------------------

After completing the `Quick Start Guide for Development Board Usage`_ and the `Basic Guide for Software Development`_, you will be familiar with the basic knowledge. Then, the next step is to learn the content required for secondary development.

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Location of U-Boot board-level files: u-boot/board/rockchip/myzr_rk3588/
- U-Boot board-level configuration file: u-boot/include/configs/myzr_rk3588.h
- U-Boot board-level compilation configuration file: u-boot/configs/myzr-rk3588_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Kernel board-level compilation configuration file: kernel/arch/arm64/configs/myzr_rk_defconfig 
- Kernel board-level device tree file: kernel/arch/arm64/boot/dts/rockchip/myzr-rk3588.dts
- Kernel Development Reference Manual: docs/Kernel

Hardware Development Guide
----------------------------

1. First, it is necessary for hardware engineers to understand the introduction and basic principles of the baseboard of our development board. For details, see :doc:`《Baseboard Hardware Introduction》<HM.MB314.Hardware Manual>`.
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or carry out designs based on our schematics.
3. If changes to certain interfaces or functions are required, you can refer to the **Pin Definition & Detailed Function Description** in :doc:`《Core Board Hardware Introduction》<HM.CB314.Hardware Manual>`.
4. For more detailed information, please refer to "05_Document Materials" in the network disk.

Other Necessary Documents
---------------------------

### Developer Guide
~~~~~~~~~~~~~~~~~~~~~

- Location: docs/Rockchip_Developer_Guide_Linux_Software_CN.pdf


Datasheet
~~~~~~~~~~~

- Location in the network disk: docs/RK3588/Datasheet/*
