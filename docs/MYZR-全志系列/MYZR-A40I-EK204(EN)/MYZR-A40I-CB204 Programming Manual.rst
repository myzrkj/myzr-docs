MYZR-A40I-CB204 Programming Manual
====================================

A40I Programming
------------------

| Install PhoenixSuit: Unzip PhoenixSuit.zip and run PhoenixSuit_CN.msi

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/PhoenixSuit_01.png
  :alt: MY-R16-PhoenixSuit_01

| Click "Next", then "Next" again. When prompted to install the Device Driver, click "Next" to proceed with the installation. Once the installation is complete, click "Close".


USB Firmware Upgrade for Development Board
---------------------------------------------

| Open the PhoenixSuit software, select "One-Click Flashing", and click "Browse" to choose the firmware.

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/PhoenixSuit_02.png
  :alt: MY-R16-PhoenixSuit_02

| Flashing steps: Please strictly follow the order of steps 1~5 (do not reverse the steps):

1. Open the USB flashing software PhoenixSuit.
2. Select the "One-Click Flashing" page and click "Browse" to load the firmware properly.
3. Press and hold the MENU or BOOT button on the development board.
4. Connect the power supply to the development board and turn on the development board's power switch.
5. Use an OTG cable to connect the development board to the computer. The flashing software will automatically prompt for an upgrade (Note: If this step proceeds normally, the flashing software will display "Start Flashing". If the flashing software shows no response, please check whether steps 1~4 are performed correctly. During this process, the bottom-left corner of the flashing software will keep displaying "No device connected!!!", which can be ignored).
6. Release the MENU or BOOT button.

.. image:: /image/MYZR-全志系列/MYZR-A40I-EK204/PhoenixSuit_03.png
  :alt: PhoenixSuit_03.png

| Click "Yes" and select "Force Format" (Force Format is required for the first upgrade of a bare board without any programs, or when upgrading the system from Linux, Ubuntu, etc. to Android). The board will start the upgrade process until it is completed. After the upgrade is finished, the development board will start the system automatically.