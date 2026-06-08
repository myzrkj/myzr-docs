MYZR-LS1012A-EK200 Startup Manual
===================================

MYZR-LS1012A-EK200 Package List
---------------------------------

**Standard Components**

| 【Base Board】: MYZR-LS1012A-MB200, 1 piece
| 【Core Board】: MYZR-LS1012A-CB200, 1 piece
| 【Power Adapter】: 5V, 1 piece
| 【Ethernet Cable】: 1 piece
| 【Serial Cable】: 1 piece

**User-Prepared Components**

| 【Mini USB Cable】: 1 piece, used for downloading (a common Android phone data cable is acceptable)
| 【USB-to-Serial Cable】: 1 piece, used for debugging (required if the computer does not have a DB9 serial port)

MYZR-LS1012A-EK200 Main Interfaces
------------------------------------

Development Board Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Check the Power Switch**

| Press the "o" on the development board's power switch "SWITCH" to ensure the power switch is in the off state.

**Serial Cable Connection**

| Connect one end of the serial cable to the "DEBUG" port of the development board, and the other end to the computer's serial port or USB port.
| Refer to the :doc:`《Xshell.RM Reference Manual 》 </docs/COMMON/Xshell.RM Reference Manual >` to create a new serial session and open the session.

**Ethernet Cable Connection**

| Connect one end of the Ethernet cable to "ETH1" and the other end to the computer's network port.

**USB Download Cable Connection**

| Connect one end of the Mini USB cable to the K20-JTAG module, and the other end to the computer's rear USB port.

**Power Cable Connection**

| Connect one end of the power adapter to the "5V_IN" of the development board, and the other end to a mains (220V AC) socket.

**K20-JTAG Module Connection**

| Connect the K20-JTAG module to the J8 interface of the development board, and connect the other end to the mini USB cable.


Start the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Check the Boot Mode DIP Switch of the Development Board**

| Set the "BOOT MODE" DIP switch of the development board to the normal boot mode.
| 【Boot Mode】: 1 (OFF), 2 (ON)
| 【Download Mode】: 1 (ON), 2 (OFF)
| Note: The "ON" side of the DIP switch is where the letters are, and the "OFF" side is where the numbers are.

**Power On the Development Board**

| Press the "-" on the development board's power switch "SWITCH" to turn on the power switch. At this point, you can see some of the LEDs on the development board light up.


Interpretation of Development Board Boot Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| After the development board is powered on, you can see the boot information output by the development board on the serial terminal software.

.. code-block:: shell

   U-Boot 2016.092.0+ga06b20925c (Nov 01 2019 - 18:45:12 +0800)

   SoC:  LS1012A Rev1.0 (0x87040110)
   Clock Configuration:
          CPU0(A53):800  MHz  
          Bus:      250  MHz  DDR:      1000 MT/s
   Reset Configuration Word (RCW):
          00000000: 08000008 00000000 00000000 00000000
          00000010: 33050000 c000000c 40000000 00001800
          00000020: 00000000 00000000 00000000 00004570
          00000030: 00000000 00c28120 00000096 00000000
   I2C:   ready
   DRAM:  510 MiB


   ......

   Starting kernel ...

   [    0.000000] Booting Linux on physical CPU 0x0
   [    0.000000] Initializing cgroup subsys cpu
   [    0.000000] Linux version 4.1.35-rt41 (linyn@u12045) (gcc version 4.9.3 20150311 (prerelease) (Linaro GCC 4.9-2015.03) ) #1 SMP Mon Nov 4 19:59:14 CST 2019
   [    0.000000] CPU: AArch64 Processor [410fd034] revision 4

   ......

   Starting system log daemon...0
   Starting kernel log daemon...0
   Starting internet superserver: xinetd.

   QorIQ SDK (FSL Reference Distro) 2.0 ls1012a-ek200 /dev/ttyS0

**U-Boot Information**

| The boot information "U-Boot 2016.092.0+ga06b20925c (Nov 01 2019 - 18:45:12 +0800)" includes the following information:
| 【U-Boot Version】: 2016.09;
| 【Source Code Version Number】: ga06b20925c;
| 【U-Boot File Compilation Time】: Nov 01 2019 - 18:45:12 +0800.

**Kernel Information**

| The boot information "Linux version 4.1.35-rt41 (linyn@u12045) (gcc version 4.9.3 20150311 (prerelease) (Linaro GCC 4.9-2015.03) ) #1 SMP Mon Nov 4 19:59:14 CST 2019" includes the following information:
| 【Kernel Version】: Linux-4.1.35;
| 【Kernel Source Code Version Number】: rt41;
| 【GCC Version for Kernel Compilation】: 4.9.3;
| 【Kernel File Compilation Time】: Mon Nov 4 19:59:14 CST 2019.


Development Board Login
~~~~~~~~~~~~~~~~~~~~~~~~~

| After the system starts, when "ls1012a-ek200 login: " is displayed, you can log in:
| 【Username】: root
| 【Password】: None

`Note: After logging in, you can set and modify the password using the "passwd" command.`
