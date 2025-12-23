Quick Start
=============

Instructions for Using This Document
--------------------------------------

- **All personnel involved in the project** need to understand the content in **"Part 5: Other Necessary Documents"**.
- **All personnel who need to use the development board** in the project need to understand and perform the operations in **"Part 1: Quick Start for Development Board Usage"**.
- **Software development engineers (including BSP engineers and application software engineers)** in the project need to understand and complete the content in **"Part 2: Basic Guide for Software Development"**.
- **BSP development engineers** in the project need to understand the content in **"Part 3: Advanced Guide for Software Development"**.
- **Hardware development engineers** in the project need to read **"Part 4: Guide for Hardware Development"**.

**Manual Links**

|   Testing Manual: :doc:`《Linux-5.4.1》 <./Test Manual>`
|   Development Environment Guide: :doc:`《Ubuntu14.04+Win10 (Recommended)》 </docs/COMMON/MYZR Win10 VB5212 U14045 x64 Env>`, :doc:`《Ubuntu12.04+Win10》 </docs/COMMON/MYZR Win10 VB5118 U12045 x64 Env>`, :doc:`《Ubuntu12.04+Win7》 </docs/COMMON/MYZR Win7 VB4340 U12045 x64 Env>`
|   Compilation Manual: :doc:`《Linux-5.4.1》 <./Compilation Reference Manual>`
|   Driver and Device Manual: :doc:`《Linux-5.4.1》 <./Driver and Device Manual>`

**Other Instructions**

- For opening all links in the document, it is recommended to **right-click the mouse and select "Open in New Tab"**.

Part 1: Quick Start for Development Board Usage
-------------------------------------------------

**It takes approximately half a day to read and complete the content and operations in this part for the first time.**

1. After receiving the development board, the first step is to prepare for using it, and installing terminal software is essential. Open the :doc:`《Terminal Software Reference Manual》 </docs/COMMON/Xshell.RM.参考手册>` and follow the "Software Download and Installation" section to install the terminal software.
2. After installing the terminal software, open the :doc:`《Startup Manual》 <./Startup Manual>` and follow the document to start the development board.
3. Once the development board starts successfully, perform a flashing operation by following the :doc:`《Flashing Guide Manual》 <./Programming Guide>`. The purpose is to familiarize yourself with the flashing operation and prepare for the subsequent function verification.
4. After completing the flashing of the development board, open the corresponding :doc:`《Testing Manual》 <./Test Manual>` and conduct a round of tests to verify that all functions of the development board are normal.

Part 2: Basic Guide for Software Development
----------------------------------------------

**It takes approximately half a day to read and complete the content and operations in this part for the first time.**

1. First, to carry out software development, a development environment needs to be established. Various problems may be encountered when setting up an embedded development environment. To avoid wasting unnecessary time and energy, we recommend using our virtual machine environment here. Open the 【Development Environment Guide Manual】 and follow the document to configure the virtual machine.
2. After the development environment is set up, perform a compilation by following the :doc:`《Compilation Manual》 <./Compilation Reference Manual>` and retain the target files obtained from the compilation.
3. After compiling the target files, update the target files to the device. It is recommended to conduct another test by following the :doc:`《Testing Manual》 <./Test Manual>` to verify that the compiled target files are error-free.

Part 3: Advanced Guide for Software Development
-------------------------------------------------

After completing the **Quick Start for Development Board Usage** and **Basic Guide for Software Development**, you will be familiar with the basic knowledge. Then, the next step is to learn the content required for secondary development.

**U-Boot Board-Level Files**

1. Location of U-Boot board-level files: board/myzr
2. U-Boot board-level configuration file: include/configs/myzrstm32mp1.h
3. U-Boot board-level compilation configuration file: configs/myzrstm32mp15_defconfig

**Linux Kernel Board-Level Files**

1. Kernel board-level compilation configuration file: arch/arm/configs/myzrstm32mp15_defconfig
2. Kernel board-level device tree files: arch/arm/boot/dts/myzr/*
3. Kernel Development Reference Manual: "06_Documentation Materials" directory in the network disk

Part 4: Guide for Hardware Development
-----------------------------------------

1. First, it is necessary for hardware engineers to understand the introduction and basic principles of the base board of our development board. For details, refer to the :doc:`《Base Board Hardware Introduction》 <./Backplane Hardware Manual>`.
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or conduct designs based on our schematics.
3. If changes to certain interfaces or functions are required, you can refer to the **Pin Definition & Detailed Function Description** in the :doc:`《Core Board Hardware Introduction》 <./Core Board Hardware Manual>`.
