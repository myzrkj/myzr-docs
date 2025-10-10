MYZR-RZG2L User and Development Guide
=======================================

Instructions for Using This Document
--------------------------------------

- **All team members** involved in the project need to understand the content in **"Part 5: Other Necessary Documents"**.
- **All personnel in the project who need to use the development board** must understand and perform the operations outlined in **"Part 1: Quick Start for Development Board Usage"**.
- **Software development engineers** in the project (including BSP engineers and application software engineers) are required to understand and complete the tasks in **"Part 2: Basic Guide for Software Development"**.
- **BSP development engineers** in the project need to understand the content in **"Part 3: Advanced Guide for Software Development"**.
- **Hardware development engineers** in the project should read **"Part 4: Guide for Hardware Development"**.

Manual Links
~~~~~~~~~~~~~~

| **Test Manual**: :doc:`《Linux-5.10.131》<RZG Test Manual>`
| **Development Environment Guide Manual**:
  :doc:`《Ubuntu14.04+Win10 (Recommended)》</docs/COMMON/MYZR Win10 VB5212 U14045 x64 Env>`
  :doc:`《Ubuntu12.04+Win10》</docs/COMMON/MYZR Win10 VB5118 U12045 x64 Env>`
  :doc:`《Ubuntu12.04+Win7》</docs/COMMON/MYZR Win7 VB4340 U12045 x64 Env>`
| **Compilation Manual**: :doc:`《Linux-5.10.131》<MYZR-RZG-EK200 Compilation Reference Manual>`

Additional Notes
~~~~~~~~~~~~~~~~~~~

| It is recommended to open all links in this document by right-clicking the mouse and selecting "Open in New Tab".

Part 1: Quick Start for Development Board Usage
--------------------------------------------------

**It takes approximately half a day to read through and complete the content and operations in this part for the first time.**

1. After receiving the development board, the first step is to prepare for its use, and installing terminal software is essential. Open :doc:`《Terminal Software Reference Manual》</docs/COMMON/Xshell.RM.参考手册>` and follow the "Software Download and Installation" section to install the terminal software.
2. Once the terminal software is installed, open :doc:`《Startup Manual》<MYZR-RZG-EK200 Startup Manual>` and follow the instructions in the document to start the development board.
3. After the development board starts successfully, perform a programming operation by following the guidelines in :doc:`《Programming Guide Manual》<MYZR-RZ-EK200 Programming Manual>`. The purpose is to familiarize yourself with the programming operation and prepare for the subsequent function verification.
4. After completing the programming of the development board, open the corresponding **[Test Manual]** and conduct a full test to verify that all functions of the development board are working properly.

Part 2: Basic Guide for Software Development
-----------------------------------------------

**It takes approximately half a day to read through and complete the content and operations in this part for the first time.**

1. First, to carry out software development, a development environment needs to be established. Various issues may arise when setting up an embedded development environment. To avoid wasting unnecessary time and effort, we recommend using our virtual machine environment. Open the **[Development Environment Guide Manual]** and follow the document to configure the virtual machine.
2. After the development environment is set up, perform a compilation by following the instructions in the **[Compilation Manual]** and retain the target files obtained from the compilation.
3. Once the target files are compiled, update them to the device. It is advisable to conduct another test by referring to the **[Test Manual]** to verify that the compiled target files are error-free.

Part 3: Advanced Guide for Software Development
-------------------------------------------------

| After completing the **Quick Start for Development Board Usage** and **Basic Guide for Software Development**, you will have become familiar with the fundamental aspects. Next, the following content covers what you need to know for secondary development. **

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Location of U-Boot board-level files: board/renesas/rzg2l-myzr/
2. U-Boot board-level configuration file: include/configs/myzr-rzg2l.h
3. U-Boot board-level compilation configuration file: configs/myzr-rzg2l_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Kernel board-level compilation configuration file: arch/arm64/configs/myzr-rz_defconfig
2. Kernel board-level device tree files: arch/arm64/boot/dts/renesas/myzr-rzg2l-rgb.dts, arch/arm64/boot/dts/renesas/myzr-rzg2l-dsi.dts
3. Kernel development reference manual: "06_Documentation and Materials" directory in the network disk

Part 4: Guide for Hardware Development
------------------------------------------

1. First, it is necessary for hardware engineers to understand the introduction and basic principles of the development board's baseboard. For details, refer to :doc:`《Baseboard Hardware Introduction》<MYZR-RZG2UL Hardware Introduction>`.
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or conduct design based on our schematics.
3. If changes to certain interfaces or functions are required, refer to the **Pin Definition & Detailed Function Description** in :doc:`《Core Board Hardware Introduction》<MYZR-RZG2UL-CB200>`.