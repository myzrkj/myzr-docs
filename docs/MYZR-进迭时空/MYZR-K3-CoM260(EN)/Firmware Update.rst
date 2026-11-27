.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Firmware Flashing
=================

Enter Flash Mode
----------------

Before entering flash mode, prepare two buttons to short-circuit FC_REC and GND, and SYS_RST and GND, respectively.

1. When the device is powered off

- Press and hold the FC_REC button.

- Connect the power adapter to power on the device.

- Release the FC_REC button.

- Use a Type-C cable to connect the Development Board Type-C port to the host computer.

- Use the JDT Spacetime Flashing Tool Titan or execute the fastboot command to flash.

2. When the device is powered on and in the on state

- Press and hold the FC_REC button.

- Briefly press the RST button.

- Release the FC_REC button.

- Use a Type-C cable to connect the Development Board Type-C port to the host computer.

- Use the JDT Spacetime Flashing Tool Titan or execute the fastboot command to flash.

.. image:: ../../../image/MYZR-进迭时空/MYZR-K3-CoM260/按键输入.jpeg
   :alt: 按键输入.jpeg
   :width: 100%

For the flashing process, please refer to the `Flashing Tool User Manual <https://www.spacemit.com/community/document/info?lang=zh&nodepath=tools/user_guide/flasher_user_guide.md>`__.

Firmware Download and Installation
----------------------------------

Bianbu is an operating system deeply optimized for RISC‑V architecture processors from Spacemit.

Click `K3 Bianbu <https://spacemit.com/community/resources‑download/Images%20Collects/K3/Bianbu>`__ to get the installation package.
