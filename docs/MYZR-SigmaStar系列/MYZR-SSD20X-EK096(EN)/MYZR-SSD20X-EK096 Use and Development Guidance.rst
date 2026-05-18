MYZR-SSD20X-EK096 Use and Development Guidance
================================================

Instructions for use of this document
----------------------------------------

- All participants in the project need to know **"Other necessary documents for Part V"**
- All personnel in the project who need to use the development board need to understand and operate the **"first part of the development board use fast entry"**
- Software development engineers(including BSP engineers, application software engineers) in the project need to understand and complete the **"Part 2 Basic Guidance for Software Development"**
- In the project, BSP development engineers need to understand **"Part 3 Advanced Guidance for Software Development"**.
- The hardware development engineer in the project needs to read **"Part 4 Hardware Development Guidance"**.

**Link to manual**

|   Test Manual： :doc:`《Linux-4.9.84》<MYZR-SSD20X-MB096 Linux-4.9.84 Test Manual>`
|   Development Environment Guidance Manual： :doc:`《Ubuntu14.04+Win10》</docs/COMMON/MYZR Windows-10 VirtualBox-5.2.12 Ubuntu-14.04.5 64-bit Dev Env Guide>`
|   Build Manual： :doc:`《Linux-4.9.84》<MYZR-SSD20X-CB096 Hardware Introduction>`

**Description:**

|  Open all links in the document, it is recommended to use the mouse right click to open in the new tab.

The first part of the development board USES a quick start
-------------------------------------------------------------

**This part of the content and operation, the first reading and completion of about half a day**

1. 1. After getting the development board, the first thing is to prepare for the use of the development board, installation of terminal software is necessary.Open :doc:`《Terminal Software Reference Manual》</docs/COMMON/Xshell.RM Reference Manual >`，refer to Software Download and Installation to install the terminal software.
2. After the installation of terminal software, open :doc:`《Quick Start》<MYZR-SSD20X-CB096 Quick Start>` ，refer to the document to start the development board.
3. After the development board is started successfully, refer to :doc:`《Burning Manual》<MYZR-SSD20X-CB096 Burning Manual>` for a burn.The purpose is to familiarize yourself with the burn operation and prepare for the next functional verification.
4. After the development board is burned, open the corresponding **【Test Manual】** and conduct a test to verify that all functions of the development board are normal.

The second part is the basic guidance of software development
---------------------------------------------------------------

**The second part of the software development basic guidance of this part of the content and operation, the first reading and completion of about half a day**

1. First of all, to develop software, we need to establish a development environment. When building an embedded development environment, we will encounter various problems. To avoid wasting unnecessary time and energy, we recommend using our virtual machine environment. Turn on the **【 Development Environment Instruction Manual 】** and configure the virtual machine with reference to the document.
2. After the development environment is established, you should refer to **【Building Manual】** for a compilation, and retain the compiled target files.
3. After compiling the target file, update the target file to the device, and it is best to refer to the **【Test Manual】** for another test to verify that the compiled target file is ok.

The third part is advanced guidance of software development
--------------------------------------------------------------

|   After completing the Development board using quickstart and Software development basic guidance , the basic things we have been familiar with.Then, the next step, is secondary development needs to understand the content.

|   Board configuration file directory:

 | Arch/arm/boot/dtsinfinity2m-spinand-ssc011a-s01a-display.dts

The fourth part hardware development guidance
------------------------------------------------

1. 1. First of all, it is necessary for hardware engineers to understand the introduction and basic principles of our development board floor. See :doc:`《Base Plate Introduction》<MYZR-SSD20X-MB096 Hardware Introduction>` for details.
2. The hardware engineer opens the network disk, downloads the hardware schematic diagram file to carry on the reference, or carries on the design based on our schematic diagram. 
3. If some interfaces and functions need to be changed, please refer to the Pin definition & detailed function description in :doc:`《Core board introduction》<MYZR-SSD20X-CB096 Hardware Introduction>` .Refer to "1.1 _nxp-document-> reference-manual" in the network disk for more details.
