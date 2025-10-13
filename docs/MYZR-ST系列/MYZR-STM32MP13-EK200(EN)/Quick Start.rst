Quick Start
=============

Instructions for Using This Document
--------------------------------------

- **All personnel involved** in the project need to understand the `Other Necessary Documents`_.
- **All personnel who need to use the development board** in the project need to understand and follow the `Quick Start Guide for Development Board Usage`_.
- **Software development engineers** in the project (including BSP engineers and application software engineers) need to understand and complete the `Basic Guide for Software Development`_.
- **BSP development engineers** in the project need to understand the `Advanced Guide for Software Development`_.
- **Hardware development engineers** in the project need to read the `Hardware Development Guide`_.

Manual Links
~~~~~~~~~~~~~~

- Startup Manual: :doc:`《Linux-5.15.67》<Startup Manual>`
- Test Manual: :doc:`《Linux-5.15.67》<Test Manual>`
- Compilation Manual: :doc:`《Linux-5.15.67》<Compilation Manual>`
- Flashing Manual: :doc:`《Linux-5.15.67》<Firmware Flashing Manual>`

Additional Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~

- For opening all links in the document, it is recommended to **right-click the mouse and select "Open in New Tab"**.

Quick Start Guide for Development Board Usage
-----------------------------------------------

**It takes approximately half a day to read and complete the content and operations in this section for the first time**

1. After receiving the development board, the first thing to do is prepare for using it, and installing terminal software is essential. Open :doc:`《Xshell Reference Manual》</docs/COMMON/Terminal software XShell reference manual>` and follow the **Software Download and Installation** section to install the terminal software.
2. After installing the terminal software, open the :doc:`《Startup Manual》<Startup Manual>` and follow the document to start the development board.
3. Once the development board starts successfully, open the corresponding **[Flashing Manual]** to perform a flashing operation. The purpose is to familiarize yourself with the flashing process and prepare for the next function verification.
4. After the development board flashing is completed, open the corresponding **[Test Manual]** and conduct a round of tests to verify that all functions of the development board are normal.

Basic Guide for Software Development
---------------------------------------

**It takes approximately half a day to read and complete the content and operations in this section for the first time**

1. First, to carry out software development, it is necessary to set up a development environment. Various problems may be encountered when building an embedded development environment. To avoid wasting unnecessary time and energy, we recommend using our virtual machine environment here. Open the **[Development Environment Guide Manual]** and follow the document to configure the virtual machine properly.
2. After the development environment is set up, you should perform a compilation according to the **[Compilation Manual]** and keep the target files obtained from the compilation.
3. After compiling the target files, update the target files to the device. It is advisable to conduct another test with reference to the **[Test Manual]** to verify that the compiled target files are error-free.

Advanced Guide for Software Development
------------------------------------------

After completing the Quick Start Guide for Development Board Usage_ and Basic Guide for Software Development_, we will be familiar with the basic knowledge. Then, the next step is to learn the content required for secondary development.

### U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Location of U-Boot board-level files: board/myzr
- U-Boot board-level configuration files: include/configs/myzrstm32mp13*.h
- U-Boot board-level compilation configuration file: configs/myzrstm32mp13_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Kernel board-level compilation configuration file: arch/arm/configs/myzr-stm32mp13_defconfig 
- Kernel board-level device tree files: arch/arm/boot/dts/myzr/---\*
- Kernel Development Reference Manual: 《\*Reference Manual\*.pdf》 in the network disk

Hardware Development Guide
----------------------------

1. First, it is necessary for hardware engineers to understand the introduction and basic principles of the baseboard of our development board. For details, see :doc:`《Baseboard Hardware Introduction》<Hardware Manual for Backplane>` .
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or conduct design based on our schematics.
3. If changes to certain interfaces or functions are required, you can refer to the **Pin Definition & Detailed Function Description** in the :doc:`《Core Board Hardware Introduction》<Hardware Manual for Core Board>` .
4. For more detailed information, please refer to "05_Document Materials" in the network disk.

Other Necessary Documents
---------------------------

Reference Manual
~~~~~~~~~~~~~~~~~~

- Location in the network disk: "05_Document Materials -> RM0475_Rev0.6b.pdf"

**The corresponding document has up to 3,000 pages. Software and hardware engineers can read it selectively during the design and development process.**

Datasheet
~~~~~~~~~~~~

- Location in the network disk: "05_Document Materials -> DS13874_STM32MP135A STM32MP135D_Rev0.5a"

**The corresponding document has approximately 200 pages. Software and hardware engineers can browse it and decide whether to read it in detail by themselves.**
