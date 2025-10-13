Startup Manual
================

MYZR-STM32MP15-EK152 Package List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Standard Components
"""""""""""""""""""""

|  [Base Board]: MYZR-STM32-MB152, 1 piece
|  [Core Board]: MYZR-STM32-CB152, 1 piece (pre-attached to the base board)
|  [Power Adapter]: 5V, 1 piece
|  [DEBUG Serial Connector]: 1 piece
|  [Micro USB Cable]: 1 piece

User-Prepared Components
""""""""""""""""""""""""""

|  [Ethernet Cable]: 1 piece
|  [USB-to-Serial Cable]: 1 piece, used for debugging (required if the computer does not have a DB9 serial port)

Other Optional Components
"""""""""""""""""""""""""""

|  [Display Circuit Board]
|  [LCD Display]
|  [Touch Screen]

MYZR-STM32MP15-EK152 Main Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/1425px-MYZR-STM32MP15-EK152-Front.png
   :alt: 1425px-MYZR-STM32MP15-EK152-Front.png
   
Development Board Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Power Connection
""""""""""""""""""

|  The development board has no power switch. Therefore, when connecting the power cable, ensure that the correct power adapter is used, and connect the power cable to the **DC: 5V-3A** interface.

Serial Cable Connection
"""""""""""""""""""""""""

|  Connect the Debug serial connector to the **Debug_232** interface, then use a USB-to-serial cable to connect the computer's serial port and the Debug serial connector.
|  Refer to the :doc:`《Terminal Software Reference Manual》 </docs/COMMON/Xshell.RM.参考手册>` to create a new serial session and open the session.

Ethernet Cable Connection
"""""""""""""""""""""""""""

|  Connect one end of the Ethernet cable to **ETH10/100/1000M** and the other end to the computer's network port.

USB Download Cable Connection
"""""""""""""""""""""""""""""""

|  Connect one end of the Micro USB cable to the **BootLoader** port of the development board, and the other end to the rear USB port of the computer.

Start the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check the Development Board DIP Switch
"""""""""""""""""""""""""""""""""""""""""

|  Set the **SW: BOOT** DIP switch of the development board to the normal startup mode. The DIP switch modes are as follows:
|  [eMMC Startup]: 1 (off), 2 (on), 3 (off), 4 (off)
|  [TF Card Startup]: 1 (on), 2 (off), 3 (on), 4 (off)
|  [Download Mode]: 1 (off), 2 (off), 3 (off), 4 (off)
|  Note: The "ON" position of the DIP switch is on the side with letters, and the "OFF" position is on the side with numbers.

Check the Development Board's Boot Medium DIP Switch
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

|  Select the corresponding boot medium according to your development board.
|  [eMMC Startup]: 1 (ON), 2 (ON), 3 (ON), 4 (OFF)
|  [NAND Startup]: 1 (OFF), 2 (OFF), 3 (OFF), 4 (ON)

Power On the Development Board
"""""""""""""""""""""""""""""""""

|  Directly connect the power adapter to power on the development board.

Interpretation of Development Board Startup Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  After the development board is powered on, you can view the startup information output by the development board in the serial terminal software.

.. code-block:: shell
   
   NOTICE:  CPU: STM32MP157AAC Rev.Z
   NOTICE:  Model: MYZR STM32MP15 Discovery Board
   INFO:    Reset reason (0x10):
   INFO:      Reset due to a failure of VDD_CORE
   INFO:    PMIC version = 0x10
   INFO:    Using EMMC
   INFO:      Instance 2
   INFO:    Boot used partition fsbl1
   NOTICE:  BL2: v2.2-r1.0(debug):2e4f8b4-dirty
   NOTICE:  BL2: Built : 06:17:37, Apr  7 2021
   INFO:    Using crypto library 'stm32_crypto_lib'
   INFO:    BL2: Doing platform setup
   INFO:    RAM: DDR3-DDR3L 16bits 533000Khz
   INFO:    Memory size = 0x10000000 (256 MB)
   ...
   NOTICE:  SP_MIN: Built : 06:17:46, Apr  7 2021

   ......

   U-Boot 2020.01-stm32mp-r1 (Apr 07 2021 - 19:15:56 +0800)

   CPU: STM32MP157AAC Rev.Z
   Model: MYZR STM32MP15 Discovery Board
   Board: stm32mp1 in trusted mode (myzr,myzr-stm32mp15)
   DRAM:  256 MiB
   Clocks:
   - MPU : 650 MHz
   - MCU : 208.878 MHz
   - AXI : 266.500 MHz
   - PER : 24 MHz
   - DDR : 533 MHz

   ......

   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Linux version 5.4.31 (myzr@u14045) (gcc version 9.3.0 (GCC)) #20 SMP PREEMPT Tue Apr 6 19:11:34 CST 2021
   [    0.000000] CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=10c5387d
   ......

   ST OpenSTLinux - Weston - (A Yocto Project Based Distro) 3.1-openstlinux-5.4-dunfell-mp1-20-06-24 stm32mp1 ttySTM0

   stm32mp1 login: root (automatic login)

TF-A Information
""""""""""""""""""

.. code-block:: shell

   "NOTICE: CPU: STM32MP157AAC Rev.Z": Indicates that the CPU model used is STM32MP157AAC with revision Z. For 153 and 151 CPUs, it will be "CPU: STM32MP153AAC Rev.Z" and "CPU: STM32MP151AAC Rev.Z" respectively.
   "NOTICE: Model: MYZR STM32MP15 Discovery Board": This is the software name of our development board.
   "Reset reason (0x10)": Indicates the reason for the development board's reset.
   "Using EMMC": Indicates startup using eMMC; for TF card startup, it will be "Using SDMMC".
   "INFO: RAM: DDR3-DDR3L 16bits 533000Khz" and "INFO: Memory size = 0x10000000 (256 MB)": Indicate DDR information.
   "SP_MIN: Built : 06:17:46, Apr 7 2021": Indicates the compilation time of the TF-A image. During debugging, this can be used to determine whether the update was successful.

U-Boot Information
""""""""""""""""""""

.. code-block:: shell

   "U-Boot 2020.01-stm32mp-r1 (Apr 07 2021 - 19:15:56 +0800)": This is the U-Boot version number and compilation time.
   "CPU: STM32MP157AAC Rev.Z": This is the CPU information.
   "Model: MYZR STM32MP15 Discovery Board": This is the software name of our development board.
   "DRAM: 256 MiB": Indicates that 256MB DDR is used.
   "Clocks": These are the configurations of various clocks.

Kernel Information
""""""""""""""""""""

.. code-block:: shell

   The startup information "Linux version 5.4.31 (myzr@u14045) (gcc version 9.3.0 (GCC)) #20 SMP PREEMPT Tue Apr 6 19:11:34 CST 2021" includes the following details:
   [Kernel Version]: Linux-5.4.31;
   [Host Name]: (myzr@u14045)
   [Compiler Version]: gcc version 9.3.0
   [Kernel File Compilation Time]: Tue Apr 6 19:11:34 CST 2021.

File System Information
"""""""""""""""""""""""""

.. code-block:: shell

   The two lines of startup information "ST OpenSTLinux - Weston - (A Yocto Project Based Distro) 3.1-openstlinux-5.4-dunfell-mp1-20-06-24 stm32mp1 ttySTM0" include the following details:
   [ST OpenSTLinux - Weston]: Indicates the base package of the file system;
   [20-06-24]: Indicates the compilation time of the file system;
   [ttySTM0]: Indicates the debug serial port device of the file system;
   [automatic login]: Indicates that this system enables automatic login;