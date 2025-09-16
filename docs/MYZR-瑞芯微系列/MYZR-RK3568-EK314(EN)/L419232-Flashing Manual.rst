Flashing Manual
=================

Download Files
----------------

- Open the network disk and download the files in the "01_Flash" directory.


Install DriverAssitant Driver
--------------------------------

- Unzip DriverAssitant_v5.12.zip, then enter the DriverAssitant_v5.12 folder.

- Double-click the DriverInstall.exe program to install the driver.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/driver-1.png
   :alt: image-driver-1.png



Flashing with RKDevTool
--------------------------

- Unzip RKDevTool_Release_v2.92.zip, then enter the RKDevTool_Release_v2.92 folder.

- Double-click RKDevTool.exe to open the program.

- Click to enter the "Upgrade Firmware" interface.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-download-1.png
   :alt: image-RK3568-download-1.png

- Click the "Firmware" button, then select the corresponding update.img image file. The image file is in the image-buildroot file downloaded just now, which is divided into two images: hdmi and vga.

   The image in hdmi can display three types of interface displays: hdmi + MIPI-DSI + LVDS;
   The image in vga can display three types of interface displays: vga + MIPI-DSI + LVDS.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-download-2.png
   :alt: image-RK3568-download-2.png

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-download-3.png
   :alt: image-RK3568-download-3.png

- Connect the programming cable to the development board, press and hold the VOL+ button of the development board, then power on the development board. After about 3 seconds of power-on, you can see that the development board has entered the download mode.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-download-4.png
   :alt: image-RK3568-download-4.png

- Click the "Upgrade" button to perform flashing. If the flashing is successful, the success characters will be displayed on the right.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-download-5.png
   :alt: image-RK3568-download-5.png

- After the programming is completed, the development board system will restart automatically.
