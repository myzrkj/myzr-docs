Quick Start
=============

Document Usage Instructions
------------------------------

- **All participants** in the project need to understand the `Other Necessary Documents`_.
- **All personnel in the project who need to use the development board** must understand and follow the `Development Board Quick Start Guide`_.
- **Software development engineers** in the project (including BSP engineers and application software engineers) need to understand and complete the `Basic Software Development Guide`_.
- **BSP development engineers** in the project need to understand the `Advanced Software Development Guide`_.
- **Hardware development engineers** in the project need to read the `Hardware Development Guide`_.

Manual Links
~~~~~~~~~~~~~~

- Startup Manual: :doc:`《Linux-5.10.72》<L51072-Startup Manual>`
- Test Manual: :doc:`《Linux-5.10.72》<L51072-Test Manual>`
- Compilation Manual: :doc:`《Linux-5.10.72》<L51072-Compilation Manual>`
- Flashing Manual: :doc:`《Linux-5.10.72》<L51072-Firmware Flashing Manual>`

Additional Instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~

- For opening all links in the document, it is recommended to **right-click the mouse and select "Open in a new tab"**.

Development Board Quick Start Guide
--------------------------------------

**It takes approximately half a day to read and complete the content and operations in this section for the first time.**

1. After receiving the development board, the first step is to prepare for using it, and installing terminal software is essential. Open :doc:`《Xshell Reference Manual》</docs/COMMON/Terminal software XShell reference manual>` and follow the **Software Download and Installation** section to install the terminal software.
2. After installing the terminal software, open the :doc:`《Startup Manual》<L51072-Startup Manual>` and follow the document to start the development board.
3. Once the development board starts successfully, open the corresponding **[Flashing Manual]** to perform a flashing operation. The purpose is to familiarize yourself with the flashing process and prepare for the next function verification.
4. After the development board flashing is completed, open the corresponding **[Test Manual]** and conduct a round of tests to verify that all functions of the development board are normal.

Basic Software Development Guide
----------------------------------

**It takes approximately half a day to read and complete the content and operations in this section for the first time.**

1. First, to carry out software development, a development environment needs to be established. Various problems may be encountered when setting up an embedded development environment. To avoid wasting unnecessary time and energy, we recommend using our virtual machine environment here. Open the **[Development Environment Guide Manual]** and follow the document to configure the virtual machine.
2. After the development environment is set up, follow the **[Compilation Manual]** to perform a compilation and retain the target files obtained from the compilation.
3. After compiling the target files, update the target files to the device. It is also advisable to conduct another test with reference to the **[Test Manual]** to verify that the compiled target files are error-free.

Advanced Software Development Guide
-------------------------------------

After completing the `Development Board Quick Start Guide`_ and `Basic Software Development Guide`_, you will be familiar with the basic knowledge. Next, you will learn the content required for secondary development.

U-Boot Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Location of U-Boot board-level files: board/myzr
- U-Boot board-level configuration files: include/configs/myimx*.h
- U-Boot board-level compilation configuration files: configs/*_defconfig

Linux Kernel Board-Level Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Kernel board-level compilation configuration files: arch/arm/configs/*_defconfig
- Kernel board-level device tree files: arch/arm/boot/dts/---*
- Kernel Development Reference Manual: 《*Reference Manual*.pdf》 in the network disk

Hardware Development Guide
----------------------------

1. First, hardware engineers need to understand the introduction and basic principles of the development board baseboard. For details, see :doc:`《Baseboard Hardware Introduction》<Hardware Manual for Backplane>`.
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or carry out designs based on our schematics.
3. If changes to certain interfaces or functions are required, you can refer to the **Pin Definition & Detailed Function Description** in the :doc:`《Core Board Hardware Introduction》<Core Board Hardware Manual>`.
4. For more detailed information, please refer to "1.1_NXP-Document-> i.MX8M Plus" in the network disk.

Other Necessary Documents
----------------------------

Reference Manual
~~~~~~~~~~~~~~~~~~

- Location in the network disk: "1.1_NXP-Document -> i.MX8M Plus"

**The corresponding document has up to 6,000 pages. Software and hardware engineers can read it selectively during the design and development process.**

Datasheet
~~~~~~~~~~~~

- Location in the network disk: "1.1_NXP-Document -> i.MX8M Plus"

**The corresponding document has approximately 200 pages. Software and hardware engineers can browse it and decide whether to read it in detail by themselves.**
