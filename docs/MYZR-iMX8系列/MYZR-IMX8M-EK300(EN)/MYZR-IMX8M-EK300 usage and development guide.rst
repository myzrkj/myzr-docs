
MYZR-IMX8M-EK300 usage and development guide
===============================================

Instructions for use of this document
----------------------------------------

- In the project **All participants** Need to know **"Part 5 Other necessary documents"**
- In the project **All people who need to use the development board** Need to know and operate **"Part 1 Quick Start to Use the Development Board"**
- In the project **Software development engineers** (including BSP engineers, application software engineers) need to understand and complete **"Part II Basic Software Development Guidelines"**
- In the project **BSP development engineer** Need to understand **"Part III Software Development Advanced Guide"**
- In the project Hardware development engineer Need to read **"Part 4 Hardware Development Guide"**

Manual link
~~~~~~~~~~~~~

| **Test Manual:** :doc:`《Linux-4.14.98》 <./MYZR-IMX8M-EK300 Linux-4.14.98 Test Manual>`
| **Development Environment Guidance Manual:**
 :doc:`《Ubuntu14.04+Win10 (Recommended)》 </docs/COMMON/MYZR Win10 VB5212 U14045 x64 Env>`,
 :doc:`《Ubuntu12.04+Win10》 </docs/COMMON/MYZR Win10 VB5118 U12045 x64 Env>`,  
 :doc:`《Ubuntu12.04+Win7》 </docs/COMMON/MYZR Win7 VB4340 U12045 x64 Env>`
| **Compilation Manual:** 
 :doc:`《Linux-4.14.98》 <./MYZR-IMX8M-EK300 Linux-4.14.98 compilation reference manual>`
| **Driver and device manual:** :doc:`《Linux-4.14.98》 <./MYZR-IMX8M-EK300 Devices and Drivers>`

other instructions
~~~~~~~~~~~~~~~~~~~

- Open all links in the document, it is recommended to right-click with the mouse **Open in a new tab**.

Part 1 Quick Start
---------------------

**This part of content and operation, it takes about half a day to read and complete the first time**

1. 1. After getting the development board, the first thing is to prepare for using the development board. It is necessary to install terminal software. Open :doc:`《Terminal software XShell reference manual》 </docs/COMMON/Terminal software XShell reference manual>` ，and refer to **Software Download and Installation** to install the terminal software.
2. After the terminal software is installed, open :doc:`《Startup Manual》 <./MYZR-IMX8M-EK300 Startup Manual>` , and start the development board with reference to the document.
3. After the development board is successfully started, refer to :doc:`《Programming Guide》 <./MYZR-IMX8M-EK300 Programming Manual>` for one programming. The purpose is to become familiar with the programming operation and prepare for the next functional verification.
4. After the development board is burned, open the corresponding **【Test Manual】** and perform a test to verify that the development board functions properly.

Part II Basic Software Development Guidelines
-------------------------------------------------

**This part of content and operation, it takes about half a day to read and complete the first time**

1. First of all, to develop software, you need to set up a development environment. You will encounter various problems when setting up an embedded development environment. In order to avoid wasting unnecessary time and energy, we recommend using our virtual machine here. surroundings. Open **【Development Environment Guide】** and configure the virtual machine by referring to the document.
2. After the development environment is set up, you should refer to **[Compilation Manual]** to compile once, and keep the compiled object files.
3. After compiling the object file, update the object file to the device, and it is best to refer to **[Test Manual]** to perform another test to verify that there is no problem in the compiled object file.

Part III Advanced Software Development Guide
-----------------------------------------------

| After completing the **Quick Start for Using the Development Board** and the **Basic Guide to Software Development**, we are already familiar with the basic things. So, the next step is what you need to know about secondary development.

**U-Boot Board Files**

1. u-boot board level file location: board / myzr / myimx8mq.c
2. u-boot board configuration file: include / configs / myimx8mq.h
3. u-boot Extreme compilation configuration file: configs / myimx8mek300-8mq_defconfig

**Linux kernel board files**

1. Kernel board-level compilation configuration file: arch / arm64 / configs / myimx8mq_defconfig
2. Kernel board level device tree file: arch / arm64 / boot / dts / myzr / myimx8mek300-8mq.dts
3. Kernel Development Reference Manual: "i.MX Reference Manual" in Network Disk

Part 4 Hardware Development Guide
------------------------------------

1. First, it is necessary for the hardware engineer to understand the introduction and basic principles of the baseboard of our development board. For details, please refer to :doc:`《Backplane Hardware Introduction》 <./MYZR-IMX8M-MB300 hardware introduction>` 。
2. The hardware engineer opens the network disk, downloads the hardware schematic file for reference, or designs based on our schematic.
3. If some interfaces and functions need to be changed, please refer to ** Pin definition & detailed function description in :doc:`《Core Board Hardware Introduction》 <./MYZR-IMX8M-CB300 Hardware Introduction>`. For more details, please refer to "1.1_NXP-Document-> IMX8MDQLQRM_Rev0.pdf"

Part 5 Other necessary documents
-----------------------------------

**i.MX Applications Processor Reference Manual**

- The location of the network disk: "1.1_NXP-Document-> IMX8MDQLQRM_Rev0.pdf" **Corresponding documents have up to 6,000 pages, and software and hardware engineers can read them selectively during the design and development process**.

 | can read them selectively during the design and development process.

**i.MX 8M Dual / 8MQuadLite / 8M Quad Data Sheet**

- The location of the network disk: "1.1_NXP-Document-> MIMX8MQ6DVAJZAA.pdf" The corresponding document has 96 pages. 

 | Software and hardware engineers can browse and decide whether to read it in detail.

::

   --------------------------------------------------------------------------------
   * Zhuhai Mingyuan Zhirui Technology Co., Ltd.
   * ZhuHai MYZR Technology CO., LTD.
   * Latest Update: 2019/02/19
   * Supporter: Tang Bin (Linux), Lin YuanNan (Android)
   --------------------------------------------------------------------------------