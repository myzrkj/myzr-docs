MYZR-RZG2L User Guide and Development Manual
===============================================

Instructions for Using This Document
---------------------------------------

- **All team members** involved in the project need to understand the content in **"Part 5: Other Necessary Documents"**.
- **All personnel who need to use the development board** in the project must understand and follow the instructions in **"Part 1: Quick Start for Development Board Usage"**.
- **Software development engineers** in the project (including BSP engineers and application software engineers) need to understand and complete the tasks in **"Part 2: Basic Software Development Guide"**.
- **BSP development engineers** in the project must understand the content in **"Part 3: Advanced Software Development Guide"**.
- **Hardware development engineers** in the project should read **"Part 4: Hardware Development Guide"**.

Manual Links
~~~~~~~~~~~~~~

| **Test Manual**: :doc:`《Linux-5.10.131》<RZG Test Manual>`
| **Development Environment Guide Manual**:
  :doc:`《Ubuntu14.04+Win10 (Recommended)》</docs/COMMON/MYZR Windows-10 VirtualBox-5.2.12 Ubuntu-14.04.5 64-bit Dev Env Guide>`
  :doc:`《Ubuntu12.04+Win10》</docs/COMMON/MYZR Windows-10 VirtualBox-5.1.18 Ubuntu-12.04.5 64-bit Dev Env Guide>`
  :doc:`《Ubuntu12.04+Win7》</docs/COMMON/MYZR Windows-7 VirtualBox-4.3.40 Ubuntu-12.04.5 64-bit Dev Env Guide>`
| **Compilation Manual**: :doc:`《Linux-5.10.131》<MYZR-RZG-EK200 Compilation Reference Manual>`

Additional Notes
~~~~~~~~~~~~~~~~~~

| It is recommended to right-click on all links in the document and select "Open in New Tab" to access them.

Part 1: Quick Start for Development Board Usage
-------------------------------------------------

**It takes approximately half a day to read through and complete the content and operations in this part for the first time.**

1. After receiving the development board, the first step is to prepare for its use, and installing terminal software is essential. Open :doc:`《Terminal Software Reference Manual》</docs/COMMON/Xshell.RM Reference Manual >` and follow the "Software Download and Installation" section to install the terminal software.
2. Once the terminal software is installed, open :doc:`《Startup Manual》<MYZR-RZG-EK200 Startup Manual>` and follow the instructions to start the development board.
3. After the development board starts successfully, perform a flashing operation by following the guidelines in :doc:`《Flashing Guide Manual》<MYZR-RZ-EK200 Programming Manual>`. The purpose is to familiarize yourself with the flashing process and prepare for the subsequent function verification.
4. After the development board flashing is completed, open the corresponding **[Test Manual]** and conduct a full test to verify that all functions of the development board are working properly.

Part 2: Basic Software Development Guide
-------------------------------------------

**It takes approximately half a day to read through and complete the content and operations in this part for the first time.**

1. First, to carry out software development, a development environment needs to be established. Various issues may arise when setting up an embedded development environment. To avoid wasting unnecessary time and effort, we recommend using our virtual machine environment. Open the **[Development Environment Guide Manual]** and follow the instructions to configure the virtual machine.
2. After the development environment is set up, perform a compilation by following the **[Compilation Manual]** and retain the target files obtained from the compilation.
3. Once the target files are compiled, update them to the device. It is advisable to conduct another test by referring to the **[Test Manual]** to verify that the compiled target files are error-free.

Part 3: Advanced Software Development Guide
---------------------------------------------

| After completing **Quick Start for Development Board Usage** and **Basic Software Development Guide**, you will have become familiar with the fundamental knowledge. Next, the following content covers what you need to know for secondary development. **

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Location of U-Boot board-level files: board/renesas/rzg2l-myzr/
2. U-Boot board-level configuration file: include/configs/myzr-rzg2l.h
3. U-Boot board-level compilation configuration file: configs/myzr-rzg2l_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Kernel board-level compilation configuration file: arch/arm64/configs/myzr-rz_defconfig
2. Kernel board-level device tree files: arch/arm64/boot/dts/renesas/myzr-rzg2l-rgb.dts, arch/arm64/boot/dts/renesas/myzr-rzg2l-dsi.dts
3. Kernel development reference manual: Located in the "06_Documentation and Materials" directory of the network disk

Part 4: Hardware Development Guide
------------------------------------

1. First, it is necessary for hardware engineers to understand the introduction and basic principles of the development board's baseboard. For details, refer to :doc:`《Baseboard Hardware Introduction》<MYZR-RZG2L Hardware Introduction>`.
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or conduct design based on our schematics.
3. If changes to certain interfaces or functions are required, refer to the **Pin Definition & Detailed Function Description** in :doc:`《Core Board Hardware Introduction》<MYZR-RZG2L-CB200>`.