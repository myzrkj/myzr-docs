Firmware Flashing Manual
==========================

Download Files
----------------

Open the network disk and download the files in the "01_Flashing" directory.


Install the DriverAssitant Driver
-----------------------------------

- Extract DriverAssitant_v5.12.zip, then enter the DriverAssitant_v5.12 folder.
- Double-click the DriverInstall.exe program to install the driver.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/driver-1.png
   :alt: image-driver-1.png



Flash Firmware Using RKDevTool
--------------------------------

- Extract RKDevTool_Release_v2.92.zip, then enter the RKDevTool_Release_v2.92 folder.
- Double-click RKDevTool.exe to launch the program.
- Click to enter the "Upgrade Firmware" interface.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3568-EK314/RK3568-download-1.png
   :alt: image-RK3568-download-1.png

- Click the "Firmware" button, then select the corresponding img image file. The image files are located in the image-buildroot folder downloaded earlier, which is divided into three subfolders: DP-TYPEC, MIPI0-DSI, and MIPI1-DSI.
  - The images in the DP-TYPEC folder support display on interfaces: HDMI0 + HDMI1 + MIPI0-DSI + TYPEC.
  - The images in the MIPI0-DSI folder support display on interfaces: HDMI0 + HDMI1 + MIPI0-DSI + VGA.
  - The images in the MIPI1-DSI folder support display on interfaces: HDMI0 + HDMI1 + MIPI1-DSI + VGA.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-download-1.png
   :alt: image-RK3588-download-1.png

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-download-2.png
   :alt: image-RK3588-download-2.png

- Connect the flashing cable to the development board, press and hold the SW2 button on the development board, then power on the board. After approximately 3 seconds of power-on, the development board will enter download mode.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-download-3.png
   :alt: image-RK3588-download-3.png

- Click the "Upgrade" button to start firmware flashing. If the flashing is successful, a success message will be displayed on the right side.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3588-EK314/RK3588-download-4.png
   :alt: image-RK3588-download-4.png
   
- After the flashing is completed, the development board system will restart automatically.
