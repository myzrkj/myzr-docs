Firmware Flashing Manual
==========================

Prepare Files
---------------

- **Download Firmware**

  - Open the network drive, navigate to the `1. General Materials` folder, and download the `1.2 - Firmware` directory.
  - Open the network drive, navigate to the `1. General Materials` folder, and download the `1.3 - Tools` directory.

- **Copy Files**

  - Copy all files in the `1.2 - Firmware/Linux - 5.10.145` directory to a USB drive.

- **Prepare Tools**

  - Extract `1.3 - Tools/TeraTerm.v4.108.zip` to a location on Windows.


Connect the Development Board
--------------------------------

- **Turn off the power switch**: Toggle the power switch (silk - screened `SW3`) to the **OFF** position.
- **Set the DIP switch to flashing mode**: Toggle switch **1** of the mode DIP switch (silk - screened `SW2`) to **OFF** and switch **2** to **ON**.
- **Connect the firmware USB drive**: Insert the previously prepared USB drive into the USB port (silk - screened `USB`) of the development board.

  - Note: To avoid unnecessary issues, it is recommended to use a USB 2.0 USB drive and connect it to the USB 2.0 interface on the USB socket of the development board.

- **Connect the debug cable**: Use a `USB Type - C` data cable to connect the Type - C socket (silk - screened `CON2`) of the development board to a computer. Open the Device Manager on the computer, and you will see an additional `USB - SERIAL CH340 (COMx)` under `Ports (COM & LPT)`. Remember the serial port number `COMx` as it will be used later.

  - Note: There is no need to power on the development board here, and the `USB - SERIAL CH340 (COMx)` device will still appear on the computer.
  - If there is a triangular exclamation mark on `USB - SERIAL CH340 (COMx)` after connecting the Type - C cable, you need to update the CH340 driver on the computer (the driver is located in `1.3 - Tools/MYZR - RZV2H - USB Driver.zip`).
  - If no additional `USB - SERIAL CH340 (COMx)` device appears after connecting the Type - C cable, replace the Type - C cable and try connecting to another computer.

- **Connect the power supply**: Connect a 12~24V power supply to the power interface (silk - screened `P3`) of the development board.


Flash the BOOT
----------------

- Configure the serial port

  - Run `ttermpro.exe` obtained by extracting `1.3 - Tools/TeraTerm.v4.108.zip`.
  - When creating a new connection, select the COM port that appeared after connecting the Type - C cable earlier.

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.Serial.New.png
    :alt: TeraTerm.Serial.New

- Click `Setup -> Serial port...` in the Tera Term menu bar and select the appropriate parameters.

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.Serial.Setup.png
    :alt: TeraTerm.Serial.Setup

- Click `Setup -> Save setup` in the Tera Term software menu bar to save the configuration. You can use the default file name and path. This way, the configuration we just set will be loaded automatically the next time you use it.

- Turn on the power supply

  - Toggle the power switch to ***ON*** to power on the development board. You will see the following content in the Tera Term software:

  .. code-block:: text
     
     SCI Download mode (Normal SCI boot)
     -- Load Program to SRAM ---------------

- Load the tool

  - Load the Flash tool: Drag the `Flash_Writer_SCIF_MYZR_RZV2H_INTERNAL_MEMORY.mot` file from the `1.2 - Firmware/Linux - 5.10.145/boot - files - <date>` directory directly into the Tera Term software window.

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.SendFile.FlashWriter.png
    :alt: TeraTerm.SendFile.FlashWriter

  - Wait for the Flash tool transmission to complete. You can see the transmission progress during the transmission process.

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.Transmit.FlashWriter.png
    :alt: TeraTerm.Transmit.FlashWriter

- Switch the transmission rate

  - After the Flash tool transmission in the previous step is completed, enter `sup` in Tera Term.

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.FW.SUP.png
    :alt: TeraTerm.FW.SUP

  - Modify the serial port rate (to speed up subsequent file transmission): Click `Setup -> Serial port...` in the Trea Term menu bar and change the serial port baud rate to `921600`.

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.Serial.912600.png
    :alt: TeraTerm.Serial.912600

- Flash the bl2 firmware:

  - Enter the following content in the Tera Term software:

  .. code-block:: text
     
     em_w
     1
     1
     8101e00

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.FW.BL2.CMD.png
    :alt: TeraTerm.FW.BL2.CMD

  - Transmit the bl2 firmware: Drag the `bl2_bp_emmc - myzr - rzv2h - bb320 - revb - 8g.srec` file from the `1.2 - Firmware/Linux - 5.10.145/boot - files - <date>` directory directly into the Tera Term software window and wait for the transmission to complete.

  **Note**: The file selected in this step must correspond to the memory capacity of the development board, such as revb - 4g or revb - 16g.

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.Transmit.BL2.png
    :alt: TeraTerm.Transmit.BL2

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.FW.BL2.Done.png
    :alt: TeraTerm.FW.BL2.Done

- Flash the fip firmware:

  - Enter the following content in the Tera Term software:

  .. code-block:: text
     
     em_w
     1
     300
     44000000

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.FW.FIP.CMD.png
    :alt: TeraTerm.FW.FIP.CMD

  - Transmit the fip firmware: Drag the `fip - myzr - rzv2h - bb320 - revb - 8g.srec` file from the `1.2 - Firmware/Linux - 5.10.145/boot - files - <date>` directory directly into the Tera Term software window and wait for the transmission to complete.

  **Note**: The file selected in this step must correspond to the memory capacity of the development board, such as revb - 4g or revb - 16g.

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.Transmit.FIP.png
    :alt: TeraTerm.Transmit.FIP.Loading

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/TeraTerm.FW.FIP.Done.png
    :alt: TeraTerm.FW.FIP.Done

- Completion of Boot flashing

  - So far, the Boot flashing is completed. Toggle the power switch to **OFF**, close the Tera Term software, and proceed to the next step.


Flash the System
------------------

Start the BOOT
~~~~~~~~~~~~~~~~

- **Insert the USB drive**: Insert the previously prepared USB drive into the USB port (silk - screened `USB`) of the development board.
- **Set the DIP switch to boot mode**: Toggle switch **1** of the mode DIP switch (silk - screened `SW2`) to **ON** and switch **2** to **ON**.
- **Open the terminal software**: Run `ttermpro.exe` obtained by extracting `TeraTerm.v4.108.zip`. If you saved the configuration in the previous steps, you don't need to configure it again when opening it this time. If you didn't save the configuration in the previous steps, configure the serial port as before.
- **Turn on the power supply**: Toggle the power switch to **ON** to power on the development board. When you see the countdown appear in the Tera Term software, press the `Enter` key on the computer.

  .. code-block:: shell
     
     NOTICE:  BL2: v2.7(release):3ff5203
     NOTICE:  BL2: Built : 12:10:31, May 24 2025
     NOTICE:  BL2: Booting BL31
     NOTICE:  BL31: v2.7(release):3ff5203
     NOTICE:  BL31: Built : 12:10:31, May 24 2025
     
     
     U-Boot 2021.10 (May 26 2025 - 08:03:39 +0000)
     
     CPU:   Renesas Electronics CPU rev 1.0
     Model: MYZR RZV2H LGA320 Evaluation Kit - 8GB Memory
     DRAM:  7.9 GiB
     MMC:   mmc@15c00000: 0, mmc@15c10000: 1
     Loading Environment from MMC... *** Warning - bad CRC, using default environment
     
     In:    serial@11c01400
     Out:   serial@11c01400
     Err:   serial@11c01400
     Net:   eth0: ethernet@15c30000
     Hit any key to stop autoboot:  0
     =>

Flash the System
~~~~~~~~~~~~~~~~~~~

- **Clear old environment variables**: To avoid unnecessary errors, clear the old environment variables here using the following command:

  .. code-block:: text
     
     env default -a; saveenv

  After executing the command, restart the development board and proceed to the next step.

- **Start the flashing system**: Enter the following command to start the flashing system from the USB drive.

  .. code-block:: text
     
     run bootcmd_usb

- **Wait for the flashing to complete**.


Access the System
--------------------

- After the flashing is completed, the system will restart automatically and start up. After the system starts successfully, you will see the following information:

  .. code-block:: text
     
     Poky (Yocto Project Reference Distro) 3.1.31 myzr-rzv2h-ek320 ttySC0
     
     BOARD: MYZR RZV2H LGA320 Evaluation Kit
     LSI: RZ/V2H
     AI SDK V5.00 (Source Code)
     myzr-rzv2h-ek320 login:

- At this point, enter `root` to log in.

  .. code-block:: text
     
     root

- Attached image

  .. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/Update.Done.Login.png
    :alt: Update.Done.Login
