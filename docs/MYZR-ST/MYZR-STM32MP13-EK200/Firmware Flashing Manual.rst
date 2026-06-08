Firmware Flashing Manual
==========================

Download Files
----------------

|  Open the network drive and download `jdk-8u241-windows-x64.exe` and `SetupSTM32CubeProgrammer_win64.exe` from the "06_Others" directory.


Install JDK
-------------

- Double-click `jdk-8u241-windows-x64.exe`, then click "Next" as shown in the figure.

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/jdk-1.png
   :alt: image-jdk-1

- Keep the default installation directory and click "Next".

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/jdk-2.png
   :alt: image-jdk-2

- Click "Next" again to start the installation.
- Once the installation is complete, click "Close".

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/jdk-3.png
   :alt: image-jdk-3


Install SetupSTM32CubeProgrammer
-----------------------------------

- Double-click `SetupSTM32CubeProgrammer_win64.exe` and click "Next".

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/stm32cubeprog-1.png
   :alt: image-stm32cubeprog-1

- Click "Next" repeatedly until reaching the installation directory page. Keep the default installation directory (**note: the path must not contain Chinese characters**).

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/stm32cubeprog-2.png
   :alt: image-stm32cubeprog-2

- Keep the default configuration options.

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/stm32cubeprog-3.png
   :alt: image-stm32cubeprog-3

- Another window will pop up. Click "Next" to continue the installation, then click "Finish". Return to the STM32CubeProgrammer window and click "Next".

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/stm32cubeprog-4.png
   :alt: image-stm32cubeprog-4

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/stm32cubeprog-5.png
   :alt: image-stm32cubeprog-5

- Click "Done" to complete the installation.

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/stm32cubeprog-6.png
   :alt: image-stm32cubeprog-6


Set DIP Switches to Flashing Mode
------------------------------------

|  Set the "SW1" DIP switches on the development board to *Flashing Mode*.

+------------+------------+------------+------------+---------------+
| BOOT_MODE3 | BOOT_MODE2 | BOOT_MODE1 | BOOT_MODE0 | Description   |
+============+============+============+============+===============+
| 0          | 0          | 0          | 0          | Flashing Mode |
+------------+------------+------------+------------+---------------+
| 0          | 0          | 1          | 0          | Boot Mode     |
+------------+------------+------------+------------+---------------+

|  Note: For the DIP switches, ON (1) is on the side with letters, and OFF (0) is on the side with numbers.


Execute Firmware Flashing
---------------------------

- Open the installed programming tool "STM32CubeProgrammer".
- Connect the programming cable to the development board and set the DIP switches to Flashing Mode.
- Connect the power supply to power on the development board.
- Configure as shown in the figure below: First, select the USB interface, then click "Refresh" (if the USB Port does not appear after refreshing, press the reset button on the development board once), and finally click "Connect".

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/download-1.png
   :alt: image-download-1

- After a successful connection, click "Open file" to select the FlashLayout file (located in "01_Programming -> flashlayout_st-image-weston"), and choose the appropriate file based on the board type and requirements.

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/download-2.png
   :alt: image-download-2

- Click "Browse" to select the root directory where the firmware image is located.

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/download-3.png
   :alt: image-download-3

- Click the "Download" button to start programming.

.. figure:: /image/MYZR-ST系列/MYZR-STM32MP13-EK200/download-4.png
   :alt: image-download-4


Start the Development Board
-----------------------------

|  Power off the development board, set "SW1" to *Boot Mode*, then power on the development board again. The development board will start normally.