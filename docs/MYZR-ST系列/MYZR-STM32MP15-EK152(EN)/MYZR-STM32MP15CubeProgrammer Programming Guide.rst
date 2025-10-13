MYZR-STM32MP15CubeProgrammer Programming Guide
================================================

STM32CubeProgrammer Programming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  STM32CubeProgrammer is an official programming tool provided by STMicroelectronics (ST), which can be downloaded from the network disk we provided. The network disk directory is "01_Programming"; please download the entire folder.

Download and Installation
"""""""""""""""""""""""""""

1. After downloading, in the directory "01_Programming -> stm32Cubeprog", there is a compressed package and a JDK file. Extract the compressed package to obtain a folder, an exe file, and a Linux file.

2. First, install jdk-8u241-windows-x64.exe
   - Double-click jdk-8u241-windows-x64.exe, then click "Next" as shown in the figure.

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_1.png
   :alt: STM32CubeProgrammer_1.png

   - Keep the default installation directory and click "Next".

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_2.png
   :alt: STM32CubeProgrammer_2.png

   - Click "Next" again to start the installation.
   - Once the installation is complete, click "Close".

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_3.png
   :alt: STM32CubeProgrammer_3.png

3. Install SetupSTM32CubeProgrammer-2.4.0.exe
   - Double-click SetupSTM32CubeProgrammer-2.4.0.exe and click "Next".

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_4.png
   :alt: STM32CubeProgrammer_4.png

   - Click "Next" -> "Next" -> "I accept...." -> "Next" repeatedly until reaching the installation directory settings. Keep the default installation directory (**Note: The path must not contain Chinese characters**).

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_5.png
   :alt: STM32CubeProgrammer_5.png

   - Keep the default configuration options.

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_6.png
   :alt: STM32CubeProgrammer_6.png

   - Another window will pop up; click "Next" to continue the installation. After the installation finishes, click "Complete", then return to the STM32CubeProgrammer window and click "Next".

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_7.png
   :alt: STM32CubeProgrammer_7.png

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_8.png
   :alt: STM32CubeProgrammer_8.png

   - Click "Done" to complete the installation.

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_9.png
   :alt: STM32CubeProgrammer_9.png

Programming
"""""""""""""

1. Navigate to the directory "01_Programming -> myzr-stm32mp1" and extract the compressed package "openstlinux-Release.xxx.rar" (where "xxx" represents the version date).
2. Double-click the STM32CubeProgrammer shortcut on the desktop to launch the program.
3. Connect the programming cable to the development board and set the DIP switches to programming mode.
4. Connect the power supply to power on the development board.
5. Configure the settings as shown in the figure below: First, select the USB interface, then click "Refresh" (if the USB Port is not detected after refreshing, press the reset button on the development board), and finally click "Connect".

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_10.png
   :alt: STM32CubeProgrammer_10.png

6. After a successful connection, click "Open file" to select the FlashLayout file (The FlashLayout file is located in the programming directory -> myzr-stm32mp1 -> flashlayout_st-image-weston -> trusted).

 |  There are four FlashLayout files:
 |  **FlashLayout_emmc_myzr-stm32mp15-256m-trusted.tsv**
 |  **FlashLayout_emmc_myzr-stm32mp15-512m-trusted.tsv**
 |  **FlashLayout_sdcard_myzr-stm32mp15-256m-trusted.tsv**
 |  **FlashLayout_sdcard_myzr-stm32mp15-512m-trusted.tsv**
 |  Select the appropriate one based on your development board model.

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_11.png
   :alt: STM32CubeProgrammer_11.png

7. Click "Browse" to select the root directory where the image files are stored. For example, my directory is **D:\stm32\Programming\myzr-stm32mp1**.

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_14.png
   :alt: STM32CubeProgrammer_14.png

8. Click the "Download" button to start programming.

.. image:: /image/MYZR-ST系列/MYZR-STM32MP15-EK152/STM32CubeProgrammer_15.png
   :alt: STM32CubeProgrammer_15.png