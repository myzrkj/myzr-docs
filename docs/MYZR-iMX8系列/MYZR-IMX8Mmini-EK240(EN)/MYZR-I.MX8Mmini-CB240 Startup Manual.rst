MYZR-I.MX8Mmini-CB240 Startup Manual
=======================================

Development board connection
--------------------------------

**Check the power switch**

|  Press the "o" of the power switch "SWITCH" of the development board to ensure that the power switch of the development board is off.

**Serial cable connection**

|  Connect one end of the serial cable to the "DEBUG" port of the development board, and connect the other end to the serial port or USB port of the computer. 
|  Reference [Xshell.RM Reference Manual ] Create a new serial port session and open the session.

**Network cable connection**

|  Connect one end of the network cable to "ETH1" and the other end to the computer's network port.

**USB download line connection**

|  Connect one end of the double-headed USB cable to J15 and the other end to the rear USB port of the computer.

**Power cord connection**

|  Connect one end of the power adapter to the "12V_IN" of the development board, and plug the other end into the mains (220V AC) socket.

**HDMI display connection**

|  Connect one end of the HDMI display cable to the development board and the other end to the HDMI display, and power on the HDMI display. 
|  Note: It is recommended to use 1080P for the resolution of the HDMI display, and the display using the HDMI interface instead of the HDMI interface.

Start the development board
------------------------------

**Check the startup mode dial code of the development board**

|  Turn the "BOOT MODE" dial switch of the development board to the normal startup mode.
|  [Start Mode]: 1 (ON), 2 (OFF)
|  [download mode]: 1 (OFF), 2 (ON) 
|  Note: ON of the DIP switch is the letter side, and OFF is the number side.

**Power on the development board**

|  Press the "-" of the power switch "SWITCH" of the development board to turn on the power switch of the development board. At this time, you can see part of the LED lights on the development board light up.

Interpretation of the startup information of the development board
---------------------------------------------------------------------

|  After the development board is powered on, you can see the startup information output by the development board on the serial terminal software.

.. code-block:: shell

   U-Boot 2019.04-04784-g7666e4b (Dec 23 2019 - 10:15:13 +0800)

   CPU:   Freescale i.MX8MQ rev2.1 1500 MHz (running at 1000 MHz)
   CPU:   Commercial temperature grade (0C to 95C) at 26C
   Reset cause: POR
   Model: MYZR i.MX8M Evaluation Kit (300 pins)
   DRAM:  2 GiB
   MMC:   FSL_SDHC: 0, FSL_SDHC: 1
   Loading Environment from MMC... *** Warning - bad CRC, using default environment


   ......

   Starting kernel ...

   Booting Linux on physical CPU 0x0
   Linux version 4.14.98 (myzr@u14045) (gcc version 7.3.1 20180425 [linaro-7.3-2018.05 revision d29120a424ecfbc167ef90065c0eeb7f91977701] (Linaro GCC 7.3-2018.05)) #2 SMP PREEMPT Tue Jan 14 14:30:15 CST 2020
   Boot CPU: AArch64 Processor [410fd034]
   Machine model: MYZR i.MX8M Evaluation Kit (300 pins)

   ......

   [  OK  ] Reached target Multi-User System.
            Starting Update UTMP about System Runlevel Changes...
   [  OK  ] Started Session c1 of user root.
   [  OK  ] Started User Manager for UID 0.
   [  OK  ] Started Update UTMP about System Runlevel Changes.

   NXP i.MX Release Distro 4.14-sumo imx8mmek240 ttymxc0

**U-Boot Information**

|  "U-Boot 2019.04-04784-g7666e4b (Dec 23 2019-10:15:13 +0800)" in the boot information contains the following information: 
|  [U-boot version]: 2019.04; 
|  [version number of the source code]: g7666e4b; 
|  [Compiling time of u-boot file]: Dec 23 2019-10:15:13 +0800.

**Kernel Information**

|  In the boot information, "Linux version 4.14.98 (myzr@u14045) (gcc version 7.3.1 20180425 [linaro-7.3-2018.05 revision d29120a424ecfbc167ef90065c0eeb7f91977701] (Linaro GCC 7.3-2018.05)) #2 SMP PREEMPT Tue Jan 14 14:30:15 CST 2020" contains the following information: 
|  [Kernel version]: Linux-4.14.98; 
|  [GCC version of the compiled kernel]: 7.3.1; 
|  [Compilation time of the kernel file]: Tue Jan 14 14:30:15 CST 2020.

Development board login
--------------------------

|  After the system is started, "imx8mmek240 login::" is output, you can log in:
|  [Username]: root
|  [Password]: None 
|  Note: After logging in, you can set and modify the password through the "passwd" command.