.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Programming Guide
=================

After each compilation, the SD card image sdcard.tgz will be generated in /project/sophon/1688_v2.0_source/install/soc_edge_wevb_emmc/package_edge. Extract the files from this archive to the SD card (75 files will be extracted). Then insert the SD card into the board's slot (U11), connect the serial cable (U6), and power on. You will see the burning log indicating the upgrade process. When the upgrade is complete, it will prompt to reboot. Simply power off and restart.

.. code-block:: shell

   MMC write: dev # 0, block # 25628032, count 21232 ... 21232 blocks written: OK in 134 ms (77.4 MiB/s)
   
   fs reading: //boot_emmc-misc.scr
   790 bytes read in 12 ms (63.5 KiB/s)
   ## Executing script at 120000000
   fs reading: //misc.1-of-1.gz
   10220 bytes read in 9 ms (1.1 MiB/s)
   
   Uncompressed size: 10485760 = 0xA00000
   
   
   MMC write: dev # 0, block # 532480, count 20480 ... 20480 blocks written: OK in 129 ms (77.5 MiB/s)
   
   emmc update done
   bm savelog 813 bytes written in 3 ms (264.6 KiB/s)
   all done
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot
   Please remove the installation medium, then reboot