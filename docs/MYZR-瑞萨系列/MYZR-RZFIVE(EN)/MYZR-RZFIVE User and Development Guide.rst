MYZR-RZ/FIVE User and Development Guide
=========================================

Instructions for Using This Document
--------------------------------------

- **All team members** in the project need to understand the content in **"Part 5: Other Necessary Documents"**.
- **All personnel in the project who need to use the development board** must understand and perform the operations outlined in **"Part 1: Quick Start for Development Board Usage"**.
- **Software development engineers** in the project (including BSP engineers and application software engineers) need to understand and complete the tasks in **"Part 2: Basic Guide for Software Development"**.
- **BSP development engineers** in the project need to understand the content in **"Part 3: Advanced Guide for Software Development"**.
- **Hardware development engineers** in the project need to read **"Part 4: Guide for Hardware Development"**.

Manual Links
~~~~~~~~~~~~~

| **Test Manual**: :doc:`《Linux-5.10.145》<MYZR-RZFIVE-EK200 Test Manual>`
| **Development Environment Guide Manuals**:
  :doc:`《Ubuntu14.04+Win10 (Recommended)》</docs/COMMON/MYZR Windows-10 VirtualBox-5.2.12 Ubuntu-14.04.5 64-bit Dev Env Guide>`
  :doc:`《Ubuntu12.04+Win10》</docs/COMMON/MYZR Windows-10 VirtualBox-5.1.18 Ubuntu-12.04.5 64-bit Dev Env Guide>`
  :doc:`《Ubuntu12.04+Win7》</docs/COMMON/MYZR Windows-7 VirtualBox-4.3.40 Ubuntu-12.04.5 64-bit Dev Env Guide>`

Additional Notes
~~~~~~~~~~~~~~~~~~

| It is recommended to open all links in this document by **right-clicking the mouse and selecting "Open in New Tab"**.

Part 1: Quick Start for Development Board Usage
-------------------------------------------------

**For first-time readers, it takes approximately half a day to read through and complete the operations in this part.**

1. After receiving the development board, the first step is to prepare for its use, and installing terminal software is essential. Open :doc:`《Terminal Software Reference Manual》</docs/COMMON/Xshell.RM Reference Manual >` and follow the "Software Download and Installation" section to install the terminal software.
2. Once the terminal software is installed, open :doc:`《Startup Manual》<MYZR-RZFIVE-EK200 Startup Manual>` and follow the instructions to start the development board.
3. After the development board starts successfully, refer to :doc:`《Flashing Guide Manual》<MYZR-RZ-EK200 Programming Manual>` to perform a flashing operation. The purpose is to familiarize yourself with the flashing process and prepare for the subsequent function verification.
4. After the development board is flashed, open the corresponding **[Test Manual]** and conduct a full test to verify that all functions of the development board are working properly.

Part 2: Basic Guide for Software Development
----------------------------------------------

**For first-time readers, it takes approximately half a day to read through and complete the operations in this part.**

1. First, to carry out software development, a development environment needs to be established. Various issues may arise when setting up an embedded development environment. To avoid wasting unnecessary time and effort, we recommend using our virtual machine environment. Open the **[Development Environment Guide Manual]** and follow the instructions to configure the virtual machine.
2. After the development environment is set up, refer to the **[Compilation Manual]** to perform a compilation and retain the target files obtained from the compilation.
3. After the target files are compiled, update them to the device. It is advisable to refer to the **[Test Manual]** and conduct another test to verify that the compiled target files are error-free.

Part 3: Advanced Guide for Software Development
-------------------------------------------------

| After completing the **Quick Start for Development Board Usage** and **Basic Guide for Software Development**, you will be familiar with the basic knowledge. Next, the following content covers what you need to know for secondary development. **

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Location of U-Boot board-level files: board/renesas/myzr-rzfive/
2. U-Boot board-level configuration file: include/configs/myzr-rzfive.h
3. U-Boot board-level compilation configuration files: configs/myzr-rzfive-1g_defconfig and configs/myzr-rzfive-2g_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Kernel board-level compilation configuration file: arch/riscv/configs/myzr-rzfive_defconfig
2. Kernel board-level device tree files: arch/riscv/boot/dts/renesas/myzr-rzfive-1g.dts, arch/riscv/boot/dts/renesas/myzr-rzfive-2g.dts
3. Kernel development reference manual: Located in the "06_Documentation and Materials" directory of the network disk

Part 4: Guide for Hardware Development
----------------------------------------

1. First, hardware engineers need to understand the introduction and basic principles of the development board's baseboard. For details, refer to :doc:`《Baseboard Hardware Introduction》<MYZR-RZFIVE-MB200 Hardware Introduction>`.
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or conduct design based on our schematics.
3. If changes to certain interfaces or functions are required, refer to the **"Pin Definition & Detailed Function Description"** section in :doc:`《Core Board Hardware Introduction》<MYZR-RZFIVE-CB200 Hardware Introduction>`.