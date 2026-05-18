MYZR-LS1012A-EK200 User and Development Guide
===============================================

Instructions for Using This Document
---------------------------------------

- **All personnel involved in the project** need to understand the content in **"Part 5: Other Necessary Documents"**.
- **All personnel who need to use the development board** in the project need to understand and follow the instructions in **"Part 1: Quick Start for Development Board Usage"**.
- **Software development engineers** in the project (including BSP engineers and application software engineers) need to understand and complete the tasks in **"Part 2: Basic Guide for Software Development"**.
- **BSP development engineers** in the project need to understand the content in **"Part 3: Advanced Guide for Software Development"**.
- **Hardware development engineers** in the project need to read **"Part 4: Guide for Hardware Development"**.

**Manual Links**

|  **Test Manual:** :doc:`《Linux-4.4.98》 <./MYZR-LS1012A-EK200 Linux-4.4.98 Test Manual>`
|  **Development Environment Guide Manuals:**
 :doc:`《Ubuntu14.04+Win10 (Recommended)》 </docs/COMMON/MYZR Windows-10 VirtualBox-5.2.12 Ubuntu-14.04.5 64-bit Dev Env Guide>`,
 :doc:`《Ubuntu12.04+Win10》 </docs/COMMON/MYZR Windows-10 VirtualBox-5.1.18 Ubuntu-12.04.5 64-bit Dev Env Guide>`,  
 :doc:`《Ubuntu12.04+Win7》 </docs/COMMON/MYZR Windows-7 VirtualBox-4.3.40 Ubuntu-12.04.5 64-bit Dev Env Guide>`
|  **Compilation Manual:** :doc:`《Linux-4.4.98》 <./MYZR-LS1012A-EK200 Linux-4.4.98 Compilation Reference Manual>`
|  **Driver and Device Manual:** :doc:`《Linux-4.4.98》 <./MYZR-LS1012A-EK200 L4498 Driver and Device>`

**Other Instructions**

- For opening all links in the document, it is recommended to **right-click the mouse and select "Open in a new tab"**.
- The kernel version used by **MYZR-LS1012A-EK200** is **Linux-4.4.98**.


Part 1: Quick Start for Development Board Usage
-------------------------------------------------

|  **It takes approximately half a day to read and complete the content and operations in this part for the first time.**

1. After receiving the development board, the first step is to prepare for its use, and installing terminal software is essential. Open the :doc:`《Terminal Software Reference Manual》 </docs/COMMON/Xshell.RM Reference Manual >` and follow the **Software Download and Installation** section to install the terminal software.
2. After installing the terminal software, open the :doc:`《Startup Manual》 <./MYZR-LS1012A-EK200 Startup Manual>` and follow the document to start the development board.
3. Once the development board starts successfully, perform a flashing operation by following the instructions in the :doc:`《Flashing Manual》 <./MYZR-LS1012A-EK200 Programming Guide>`. The purpose is to familiarize yourself with the flashing operation and prepare for the next function verification.
4. After completing the flashing of the development board, open the corresponding **[Test Manual]** and conduct a test to verify that all functions of the development board are normal.


Part 2: Basic Guide for Software Development
----------------------------------------------

|  **It takes approximately half a day to read and complete the content and operations in this part for the first time.**

1. First, to carry out software development, a development environment needs to be established. Various problems may be encountered when setting up an embedded development environment. To avoid wasting unnecessary time and energy, we recommend using our virtual machine environment here. Open the **[Development Environment Guide Manual]** and follow the document to configure the virtual machine.
2. After establishing the development environment, perform a compilation by following the instructions in the **[Compilation Manual]** and retain the target files obtained from the compilation.
3. After compiling the target files, update them to the device. It is also advisable to conduct another test by following the **[Test Manual]** to verify that the compiled target files are error-free.


Part 3: Advanced Guide for Software Development
-------------------------------------------------

|  After completing the **Quick Start for Development Board Usage** and **Basic Guide for Software Development**, you will be familiar with the basic knowledge. Then, the next step is to learn the content required for secondary development.

**U-Boot Board-Level Files**

1. Path of U-Boot board-level file: board/myzr/ls1012a/ls1012a.c
2. U-Boot board-level configuration file: include/configs/myzr-ls1012a.h
3. U-Boot board-level compilation configuration file: configs/myzr_ls1012a_qspi_defconfig

**Linux Kernel Board-Level Files**

1. Kernel board-level compilation configuration file: configs/myzr_ls1012a_qspi_defconfig
2. Kernel board-level device tree file: arch/arm64/boot/dts/freescale/myzr-ls1012a.dts


Part 4: Guide for Hardware Development
----------------------------------------

1. First, hardware engineers need to understand the introduction and basic principles of the development board's baseboard. For details, refer to the :doc:`《Baseboard Hardware Introduction》 <./MYZR-LS1012A-MB200 Hardware Introduction>`.
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or carry out designs based on our schematics.
3. If changes to certain interfaces or functions are required, refer to the **Pin Definition & Detailed Function Description** in the :doc:`《Core Board Hardware Introduction》 <./MYZR-LS1012A-CB200 Hardware Introduction>`. For more detailed information, please refer to "1.1_NXP-Document -> reference-manual" in the network disk.


Part 5: Other Necessary Documents
-----------------------------------

**LS1012A Data Sheet**

- Location in the network disk: "01_Manuals -> LS1012A.pdf"

 | **This document has 120 pages, and it is recommended that all personnel involved in the project read it.**

**LS1012A Product Brief**

- Location in the network disk: "01_Manuals -> LS1012APB.pdf"

 | **The corresponding document has 16 pages, and it is recommended that all personnel involved in the project read it.**

**LS1012A Security (SEC) Reference Manual**

- Location in the network disk: "01_Manuals -> LS1012ASECRM.pdf"

 | **The corresponding document has up to 1,000 pages. Software and hardware engineers can read it selectively during the design and development process.**
