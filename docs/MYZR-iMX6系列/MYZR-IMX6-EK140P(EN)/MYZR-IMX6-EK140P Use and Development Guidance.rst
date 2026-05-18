MYZR-IMX6-EK140P Use and Development Guidance
===============================================

Instructions for use of this document
---------------------------------------

- All participants in the project need to know **"Other necessary documents for Part V"**
- All personnel in the project who need to use the development board need to understand and operate the **"first part of the development board use fast entry"**
- Software development engineers(including BSP engineers, application software engineers) in the project need to understand and complete the **"Part 2 Basic Guidance for Software Development"**
- In the project, BSP development engineers need to understand **"Part 3 Advanced Guidance for Software Development".**
- The hardware development engineer in the project needs to read **"Part 4 Hardware Development Guidance".**

Link to manual
~~~~~~~~~~~~~~~~~

| **Test Manual**：
  :doc:`《Linux-4.1.15》<MYZR-IMX6-EK140P Linux-4.1.15 Test Manual>`

| **Development Environment Guidance Manual**：
  :doc:`《Ubuntu14.04+Win10 (Recommended)》 </docs/COMMON/MYZR Windows-10 VirtualBox-5.2.12 Ubuntu-14.04.5 64-bit Dev Env Guide>`
  :doc:`《Ubuntu12.04+Win10》</docs/COMMON/MYZR Windows-10 VirtualBox-5.1.18 Ubuntu-12.04.5 64-bit Dev Env Guide>`
  :doc:`《Ubuntu12.04+Win7》</docs/COMMON/MYZR Windows-7 VirtualBox-4.3.40 Ubuntu-12.04.5 64-bit Dev Env Guide>`
  :doc:`《Terminal Software Reference Manual》</docs/COMMON/Xshell.RM Reference Manual >`

| **Build Manual**：
  :doc:`《Linux-4.1.15》<MYZR-IMX6 Linux-4.1.15 Build Reference Manual>`
  :doc:`《Linux-4.9.88》<MYZR-IMX Linux-4.9.88 Build Manual>`

| Description: Open all links in the document, it is recommended to use the mouse right click to open in the new tab.

The first part of the development board USES a quick start
---------------------------------------------------------------

**This part of the content and operation, the first reading and completion of about half a day**

1. After getting the development board, the first thing is to prepare for the use of the development board, installation of terminal software is necessary.Open :doc:`《Terminal Software Reference Manual》</docs/COMMON/Xshell.RM Reference Manual >` ，refer to **Software Download and Installation** to install the terminal software.
2. After the installation of terminal software, open :doc:`《Quick Start》<MYZR-IMX6-EK140P Quick Start>`, refer to the document to start the development board.
3. After the development board is started successfully, refer to :doc:`《Burning Manual》<MYZR-IMX6 MfgTool-v2.6 User Guide(EN)>` for a burn.The purpose is to familiarize yourself with the burn operation and prepare for the next functional verification.
4. After the development board is burned, open the corresponding **【Test Manual】** and conduct a test to verify that all functions of the development board are normal.

The second part is the basic guidance of software development
------------------------------------------------------------------

**The second part of the software development basic guidance of this part of the content and operation, the first reading and completion of about half a day**

1. First of all, to develop software, we need to establish a development environment. When building an embedded development environment, we will encounter various problems. To avoid wasting unnecessary time and energy, we recommend using our virtual machine environment. Turn on the **【 Development Environment Instruction Manual 】** and configure the virtual machine with reference to the document.
2. After the development environment is established, you should refer to **【Building Manual】** for a compilation, and retain the compiled target files.
3. After compiling the target file, update the target file to the device, and it is best to refer to the **【Test Manual】** for another test to verify that the compiled target file is ok.

The third part is advanced guidance of software development
-------------------------------------------------------------------

| After completing the **Development board using quickstart** and **Software development basic guidance** , the basic things we have been familiar with.Then, the next step, is secondary development needs to understand the content.

U-Boot Board level file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. u-boot Board file location: board/myzr
2. u-boot Board level configuration file: include/configs/myimx*.h
3. u-boot Polar compilation configuration file: configs/<ek_name>-<cpu_type>-<mem_size>-\*_defconfig

Linux Kernel board-level files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Kernel plate-level compilation configuration file: arch/arm/configs/myimx*_defconfig
2. Kernel board-level device tree file: arch/arm/boot/dts/<ek_name>-<cpu_type>-<mem_size>-\*
3. Kernel development reference manual: network disk《i.MX_Linux_Reference_Manual.pdf》

The fourth part hardware development guidance
-------------------------------------------------

1. First of all, it is necessary for hardware engineers to understand the introduction and basic principles of our development board floor. See :doc:`《Base Plate Introduction》<MYZR-IMX6-MB140P Hardware Introduction>` 。
2. The hardware engineer opens the network disk, downloads the hardware schematic diagram file to carry on the reference, or carries on the design based on our schematic diagram. 
3. If some interfaces and functions need to be changed, please refer to the Pin definition & detailed function description in :doc:`《 Core board introduction》<MYZR-IMX6-CB140 Hardware Introduction>` Refer to "1.1 _nxp-document-> reference-manual" in the network disk for more details.


Part V Other necessary documents
------------------------------------

**i.MX Family Comparison Table**

- Network disk location: "1.1_NXP-Document -> brochure"

    **The document has only one page and it is recommended that all participants in the project read it.**

**i.MX Applications Processors Fact Sheet**

- Location of network disk:"1.1_NXP-Document -> fact-sheet"

    **The corresponding document is only two pages long and is recommended for all people involved in the project.**

**i.MX Applications Processor Reference Manual**

- Location of network disk: "1.1_NXP-Document -> reference-manual"

    **The corresponding documents are up to 6,000 pages long, and software and hardware engineers can read them selectively during the design and development process.**

**i.MX Applications Processor Technical Data**

- Location of network disk:"1.1_NXP-Document -> technical-data"

    **The corresponding document has about 200 pages of content. Software and hardware engineers can browse and decide whether to read it in detail.**