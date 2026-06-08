Startup Manual
================

Preparing Tool Software
--------------------------

* **Download and Extract Files**

  * Open the network drive and navigate to the `1. General Materials` folder, then download the `1.3- Tools` directory.
  * Extract `1.3- Tools/TeraTerm.v4.108.zip`. The extracted directory contains `ttermpro.exe`, which is the serial port tool we will use later.


Connecting the Development Board
-----------------------------------

* **Connecting Power**

  * Toggle the development board's power switch (silk-screened **SW3**) to the **OFF** position to ensure the power switch is disconnected.
  * Connect the power supply to the development board's power connector (silk-screened **P3**).
    **Note**: The development board supports a power supply voltage of **12 ~ 24V**.


* **Connecting the Debug Cable**

  * Use a `USB Type-C` data cable to connect the Type-C port (silk-screened `CON2`) on the development board to a computer. Open the computer's Device Manager, and you will see an additional `USB-SERIAL CH340 (COMx)` under `Ports (COM & LPT)`. Remember the serial port number `COMx` as it will be used later.

    * **Note**: There is no need to power on the development board; the `USB-SERIAL CH340 (COMx)` device will still appear on the computer.
    * If there is a triangular exclamation mark next to `USB-SERIAL CH340 (COMx)` after connecting the Type-C cable, you need to update the CH340 driver on the computer (the driver is located at `1.3- Tools/MYZR-RZV2H-USB Driver.zip`).
    * If no additional `USB-SERIAL CH340 (COMx)` device appears after connecting the Type-C cable, replace the Type-C cable and try connecting to another computer.

* **Connecting the Network Cable**

   * Connect one end of the network cable to the first Ethernet port (silk-screened **ETH0**) on the development board, and the other end to the Ethernet port of a computer.


* **Connecting an HDMI Display**

   * Connect the HDMI display to the HDMI interface (silk-screened ***HDMI***) on the development board, and power on the HDMI display.

    **Note**: It is recommended to use an HDMI display with a resolution of 1080P and a display with a native HDMI interface, rather than one converted to an HDMI interface.


Starting the Development Board
--------------------------------

* **Configuring the Serial Port**

  * Run `ttermpro.exe` obtained by extracting `1.3- Tools/TeraTerm.v4.108.zip`.

  * When creating a new connection, select the COM port that appeared earlier after connecting the Type-C cable.

   .. figure:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.Serial.New.png
      :alt: TeraTerm.Serial.New.png

  * Click `Setup -> Serial port...` in the Tera Term menu bar and select the appropriate parameters.

   .. figure:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.Serial.Setup.png
      :alt: TeraTerm.Serial.Setup.png

  * Click `Setup -> Save setup` in the Tera Term menu bar to save the configuration. You can use the default file name and path. This way, the configuration we just set will be loaded automatically the next time we use the tool.

* **Setting the DIP Switch to Boot Mode**

  * Toggle switch **1** of the mode DIP switch (silk-screened `SW2`) to **ON**, and switch **2** to **OFF**.


* **Powering On**

  * Toggle the power switch to **ON** to supply power to the development board. You can see the information output by the development board in the Tera Term software.


Startup Information
---------------------

* **Description**

  * After the development board is connected and the serial port is configured, when powered on, you can see the startup information output by the development board in the serial port terminal software. This includes Boot output information, kernel output information, and file system loading information.

* **Boot Information**

  * The development board first starts with Boot, and the information output by Boot is similar to the following:

  .. code-block:: shell

     NOTICE:  BL2: v2.7(release):3ff5203
     NOTICE:  BL2: Built : 08:59:25, May 26 2025
     NOTICE:  BL2: Booting BL31
     NOTICE:  BL31: v2.7(release):3ff5203
     NOTICE:  BL31: Built : 08:59:25, May 26 2025


     U-Boot 2021.10 (May 27 2025 - 07:07:53 +0000)

     CPU:   Renesas Electronics CPU rev 1.0
     Model: MYZR RZV2H LGA320 Evaluation Kit - 4GB Memory
     DRAM:  3.9 GiB
     MMC:   mmc@15c00000: 0, mmc@15c10000: 1
     Loading Environment from MMC... *** Warning - bad CRC, using default environment

     In:    serial@11c01400
     Out:   serial@11c01400
     Err:   serial@11c01400
     Net:   eth0: ethernet@15c30000
     Hit any key to stop autoboot:    


  * Among the above lines, those starting with `NOTICE` are `trusted-firmware-a` information, which mainly includes:

    **Version**: `v2.7(release):3ff5203`

    **Compilation Time**: `Built : 08:59:25, May 26 2025`

  * The content from `U-Boot 2021.10` to the last line is U-Boot information, which mainly includes:

    **Version and Compilation Time**: `U-Boot 2021.10 (May 27 2025 - 07:07:53 +0000)`

    **Development Board Information**: `MYZR RZV2H LGA320 Evaluation Kit - 4GB Memory`

* **Kernel Information**

  * The content starting with `Starting kernel` is kernel information, which is mainly as follows:

  .. code-block:: shell

      Starting kernel ...

      [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
      [    0.000000] Linux version 5.10.145-cip17-yocto-standard (oe-user@oe-host) (aarch64-poky-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #1 SMP PREEMPT Mon May 26 12:39:31 UTC 2025
      [    0.000000] Machine model: MYZR RZV2H LGA320 Evaluation Kit - 4GB Memory
      [    0.000000] earlycon: scif0 at MMIO 0x0000000011c01400 (options '115200n8')
      [    0.000000] printk: bootconsole [scif0] enabled


  * The kernel build information is: `Linux version 5.10.145-cip17-yocto-standard (oe-user@oe-host) (aarch64-poky-linux-gcc (GCC) 8.3.0, GNU ld (GNU Binutils) 2.31.1) #1 SMP PREEMPT Fri Apr 11 02:33:14 UTC 2025`

    **Kernel Version**: `5.10.145`

    **GCC Platform**: `aarch64`

    **GCC Version**: `8.3.0`

    **Compilation Time**: `May 26 12:39:31 UTC 2025`

    **Development Board Information**: `MYZR RZV2H LGA320 Evaluation Kit - 4GB Memory`

* **System Information**

  * After the development board starts up successfully, you can see the system login information as follows:

  .. code-block:: shell
  
      Poky (Yocto Project Reference Distro) 3.1.31 myzr-rzv2h-ek320 ttySC0
      
      BOARD: MYZR RZV2H LGA320 Evaluation Kit
      LSI: RZ/V2H
      AI SDK V5.00 (Source Code)
      myzr-rzv2h-ek320 login:


  **Build Tool**: `Poky 3.1.31`

  **System Source Code**: `AI SDK V5.00`

  **Development Board Information**: `MYZR RZV2H LGA320 Evaluation Kit`

Logging In to the Development Board
--------------------------------------

* When the system displays `myzr-rzv2h-ek320 login:`, you can log in:

  **Username**: root

  **Password**: None

  **Note**: After logging in, you can use the **passwd** command to set and change the password.

.. code-block:: shell

   myzr-rzv2h-ek320 login: root
   root@myzr-rzv2h-ek320:~#

