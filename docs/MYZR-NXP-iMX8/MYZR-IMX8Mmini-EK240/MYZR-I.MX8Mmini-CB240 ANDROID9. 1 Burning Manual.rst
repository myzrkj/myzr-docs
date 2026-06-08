MYZR-I.MX8Mmini-CB240 ANDROID9. 1 Burning Manual
===================================================

surroundings
--------------

|  The host environment needs to use win10 system, use USB2.0

Download burning tool
-----------------------

- Corresponding flashing tools under Baidu Netdisk

Burning
----------

- Open Administrator command prompt window

1. Click the win icon in the lower left corner of the computer
2. Find the windows system option
3. Right-click the command prompt window
4. Click More
5. Click Run as administrator

- Enter the storage directory of the burning tool. For example, the storage path of the burning tool is G:\imx8m\imx8mm-android-image

.. code-block:: shell

   <code class="shell"># Enter G drive
   C:\Windows\system32> G:
   # Enter the programming tool directory
   G:\>cd imx8m\imx8mm-android-image
   </code>

-  Set the sw2 dial switch of the development board to the state of 01
-  Connect the USB port of the development board j3 to the computer USB port with a USB male-to-male programming cable
-  Enter uuu_imx_android_flash.bat -f imx8mq -a -e in the command prompt window to start flashing

.. code-block:: shell

   <code class="shell">G:\imx8mq\imx8mq-android-ek300-AP6398S>uuu_imx_android_flash.bat -f imx8mm -a -e
   </code>