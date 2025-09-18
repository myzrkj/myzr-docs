MYZR-A40I User and Development Guide
======================================

Instructions for Using This Document
---------------------------------------

- All participants in the project need to understand the **"Part 5: Other Necessary Documents"**.
- All personnel in the project who need to use the development board must understand and follow the **"Part 1: Quick Start for Development Board Usage"**.
- Software development engineers in the project (including BSP engineers and application software engineers) must understand and complete the **"Part 2: Basic Guide for Software Development"**.
- BSP development engineers in the project need to understand the **"Part 3: Advanced Guide for Software Development"**.
- Hardware development engineers in the project need to read the **"Part 4: Guide for Hardware Development"**.

Manual Links
~~~~~~~~~~~~~~

| Test Manual: :doc:`《Linux-3.10.65》<MYZR-A40I-EK204 Linux-3.10.65 Test Manual>`
| Development Environment Guide Manual: :doc:`《Ubuntu14.04+Win10》</docs/COMMON/MYZR Windows-10 VirtualBox-5.2.12 Ubuntu-14.04.5 64-bit dev env Manual>`
| Compilation Manual:
  :doc:`《Linux-3.10.65》<MYZR-A40I-EK204 Linux-3.10.65 Compilation Reference Manual>`
  :doc:`《android》<MYZR-A40I-EK204 Android Compilation Reference Manual>`

Additional Notes
~~~~~~~~~~~~~~~~~~

| For opening all links in the document, it is recommended to **right-click the mouse and select "Open in New Tab"**.


Part 1: Quick Start for Development Board Usage
--------------------------------------------------

**It takes approximately half a day to read and complete the content and operations in this part for the first time.**

1. After receiving the development board, the first thing to do is prepare for using it, and installing terminal software is essential. Open the :doc:`《Terminal software XShell reference manual》</docs/COMMON/Terminal software XShell reference manual>` and follow the "Software Download and Installation" section to install the terminal software.
2. After installing the terminal software, open the :doc:`《Startup Manual》<MYZR-A40I-CB204 Startup Manual>` and follow the document to start the development board.
3. Once the development board starts successfully, perform a flashing operation by following the :doc:`《linux-3.10.65 Programming Manual》<MYZR-A40I-CB204 Programming Manual>`. The purpose is to familiarize yourself with the flashing operation and prepare for the next function verification.
4. After the development board is flashed successfully, open the corresponding **[Test Manual]** and conduct a test to verify that all functions of the development board are normal.


Part 2: Basic Guide for Software Development
-----------------------------------------------

**It takes approximately half a day to read and complete the content and operations in this part for the first time.**

1. First, to carry out software development, you need to set up a development environment. Various problems may be encountered when building an embedded development environment. To avoid wasting unnecessary time and energy, we recommend using our virtual machine environment here. Open the **[Development Environment Guide Manual]** and follow the document to configure the virtual machine.
2. After setting up the development environment, you should perform a compilation by following the **[Compilation Manual]** and keep the target files obtained from the compilation.
3. After compiling the target files, update them to the device. It is better to conduct another test by referring to the **[Test Manual]** to verify that the compiled target files are error-free.


Part 3: Advanced Guide for Software Development
--------------------------------------------------

| After completing the **Quick Start for Development Board Usage** and **Basic Guide for Software Development**, you will be familiar with the basic knowledge. Then, the next step is to learn the content required for secondary development.

**Directory of Board-Level Configuration Files:**

| device/config/chips/r40/configs/m2ultra/

Part 4: Guide for Hardware Development
-----------------------------------------

1. First, hardware engineers need to understand the introduction and basic principles of the baseboard of our development board. For details, see the :doc:`《Backplane Hardware Introduction》<MYZR-A40I-MB204 Hardware Introduction>`.
2. Hardware engineers should open the network disk, download the hardware schematic files for reference, or conduct design based on our schematics.
3. If changes to certain interfaces and functions are required, you can refer to the **"Pin Definition & Detailed Function Description"** in the :doc:`《Core Board Hardware Introduction》<MYZR-A40I-CB204 Hardware Introduction>`.