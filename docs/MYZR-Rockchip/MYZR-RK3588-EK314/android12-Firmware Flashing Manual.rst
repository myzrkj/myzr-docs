Firmware Flashing Manual
==========================

Downloading Files
-------------------

- Open the network disk and download the files in the "01_Flashing" directory.


Installing the DriverAssitant Driver
--------------------------------------

- Extract DriverAssitant_v5.12.zip, then enter the DriverAssitant_v5.12 folder.
- Double-click the DriverInstall.exe program to install the driver.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/driver-1.png
   :alt: image-driver-1.png



Flashing Firmware with RKDevTool
----------------------------------

- Extract RKDevTool_Release_v2.92.zip, then enter the RKDevTool_Release_v2.92 folder.
- Double-click RKDevTool.exe to launch the program.
- Click to enter the "Firmware Upgrade" interface.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-download-1.png
   :alt: image-RK3568-download-1.png

- Click the "Firmware" button, then select the corresponding update.img image file. The image files are located in the image-android11 folder downloaded earlier, and they are categorized by different display panel images.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-download-5.png
   :alt: image-RK3588-download-5.png

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-download-6.png
   :alt: image-RK3588-download-6.png

- Connect the development board to the flashing cable, press and hold the VOL+ button on the development board, then power on the development board. After approximately 3 seconds of power-on, you will see that the development board has entered download mode.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-download-7.png
   :alt: image-RK3588-download-7.png

- Click the "Upgrade" button to start firmware flashing. When the flashing is successful, a success message will be displayed on the right side.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-download-8.png
   :alt: image-RK3588-download-8.png
   
- After the flashing is completed, the development board system will restart automatically.
