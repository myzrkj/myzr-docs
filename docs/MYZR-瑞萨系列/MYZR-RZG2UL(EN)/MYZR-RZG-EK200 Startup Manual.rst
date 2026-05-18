MYZR-RZG-EK200 Startup Manual
===============================

MYZR-RZG-EK200 Package List
-----------------------------

**Standard Components**

|  [Backplane]: MYZR-RZG2L-MB200 / MYZR-RZG2UL-MB200-LCD / MYZR-RZG2UL-MB200-ETH, 1 piece
|  [Core Board]: MYZR-G2L-CB200 / MYZR-G2UL-CB200, 1 piece
|  [Power Adapter]: 5V, 1 piece
|  [DEBUG Serial Connector]: 1 piece
|  [Ethernet Cable]: 1 piece

**User-Prepared Components**

|  [TF Card/USB Flash Drive]
|  [USB-to-Serial Cable]: 1 piece, used for debugging

**Other Optional Components**

|  [Display Circuit Board]
|  [LCD Display Screen]
|  [Touch Screen]

MYZR-STM32-EK152 Main Interfaces
----------------------------------

**MYZR-RZG2L-MB200**

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/1425px-Myzr_rzg2l_zheng.jpg
   :alt: 1425px-Myzr_rzg2l_zheng.jpg

**MYZR-RZG2UL-MB200-ETH**

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/1425px-Myzr_rzg2ul-eth_zheng.jpg
   :alt: 1425px-Myzr_rzg2ul-eth_zheng.jpg

**MYZR-RZG2UL-MB200-LCD**

.. figure:: /image/MYZR-瑞萨系列/MYZR-RZG2UL/1425px-Myzr_rzg2ul-lcd_zheng.jpg
   :alt: 1425px-Myzr_rzg2ul-lcd_zheng.jpg

Development Board Connection
------------------------------

**Power Connection**

|  Connect the power cable to the DC: 5V-3A interface.

**Serial Cable Connection**

|  Connect the Debug serial connector to the Debug_232 interface, then use a USB-to-serial cable to connect the computer's serial port and the Debug serial connector.
|  Refer to :doc:`《Xshell.RM Reference Manual 》 </docs/COMMON/Xshell.RM.参考手册>` to create a new serial session and open the session.

**Ethernet Cable Connection**

|  Connect one end of the Ethernet cable to ETH10/100/1000M, and the other end to the computer's network port.

Powering On the Development Board
-----------------------------------

**Check the Development Board DIP Switch**

|  Set the DIP switch SW: BOOT of the development board to the normal startup mode. The DIP switch modes are as follows:
|  [EMMC Startup]: 1 (off), 2 (off), 3 (on), 4 (off)
|  [Programming Mode]: 1 (on), 2 (off), 3 (on), 4 (off) 　　Note: The ON side of the DIP switch is where the letters are located, and the OFF side is where the numbers are located.

**Power On the Development Board**

|  Directly connect the power adapter to power on the development board, then turn on the power switch.


Interpretation of Development Board Startup Information
---------------------------------------------------------

|  After the development board is powered on, the startup information output by the development board can be viewed on the serial terminal software.

.. code-block:: shell

   U-Boot 2021.10 (Feb 07 2023 - 11:36:41 +0800)

   CPU:   Renesas Electronics K rev 16.15
   Model: myzr-rzg2l
   DRAM:  1.9 GiB
   MMC:   sd@11c00000: 0, sd@11c10000: 1
   Loading Environment from MMC... OK
   In:    serial@1004b800
   Out:   serial@1004b800
   Err:   serial@1004b800
   Net:   
   Error: ethernet@11c20000 address not set.
   No ethernet found.

   Hit any key to stop autoboot:  0 
   20951552 bytes read in 666 ms (30 MiB/s)
   38404 bytes read in 3 ms (12.2 MiB/s)
   Moving Image from 0x48080000 to 0x48200000, end=49670000
   ## Flattened Device Tree blob at 48000000
      Booting using the fdt blob at 0x48000000
      Loading Device Tree to 0000000057ff3000, end 0000000057fff603 ... OK

   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
   [    0.000000] Linux version 5.10.131-cip13-yocto-standard (kuangwh@myzr-7a9b) (aarch64-poky-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #1 SMP PREEMPT Tue Feb 7 11:45:39 CST 2023
   [    0.000000] Machine model: Renesas MYZR EK200 based on r9a07g044l2
   ......

   Welcome to Poky (Yocto Project Reference Distro) 3.1.17 (dunfell)!

   [    4.514423] systemd[1]: Set hostname to <myzr-rzg2l>.
   。。。
   Poky (Yocto Project Reference Distro) 3.1.17 myzr-rzg2l ttySC0

   BSP: RZG2L/MYZR-RZG2L-EK200/3.0.1
   LSI: RZG2L
   Version: 3.0.1
   myzr-rzg2l login: 

**U-Boot Information**

|  "U-Boot 2021.10 (Feb 07 2023 - 11:36:41 +0800)": UBOOT version number and compilation time
|  "CPU: STM32MP157AAC Rev.Z": CPU information
|  "Model: myzr-rzg2l": Software name of our development board
|  "DRAM: 1.9 GiB": Indicates that 1.9 G DDR is used
|  "Hit any key to stop autoboot: 0": U-Boot countdown time; pressing the Enter key within the countdown period allows entering U-Boot command line mode

**Kernel Information**

|  The startup information "Linux version 5.10.131-cip13-yocto-standard (kuangwh@myzr-7a9b) (aarch64-poky-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #1 SMP PREEMPT Tue Feb 7 11:45:39 CST 2023" includes the following information:
|  [Kernel Version]: 5.10.131;
|  [Host Name]: (kuangwh@myzr-7a9b)
|  [Compiler Version]: gcc version 8.3.0
|  [Kernel File Compilation Time]: Tue Feb 7 11:45:39 CST 2023.

**File System Information**

|  "Welcome to Poky (Yocto Project Reference Distro) 3.1.17 (dunfell)!": Indicates that the system enters the file system from this point
|  [ttySC0]: Represents the debug serial port device of the file system;
|  [myzr-rzg2l login:]: Login prompt; enter "root" to log in successfully.