.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Firmware Update
===============

Download file
~~~~~~~~~~~~~

Open the network drive and download i. The upgrade package file for MX93 is extracted.

Connect the brush cable
~~~~~~~~~~~~~~~~~~~~~~~

are Development Board Power off, with USB Wire Connection Development Board 's brush port and PC.

Dial-to-Flash Mode
~~~~~~~~~~~~~~~~~~

Move the "SW1" of Development Board to the brush mode.

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
       width: 100%;
       table-layout: auto;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;
       word-wrap: break-word;
   }
   </style>

+-------------+-------------+-------------+-------------+----------+
| BOOT\_MODE3 | BOOT\_MODE2 | BOOT\_MODE1 | BOOT\_MODE0 | Descript |
|             |             |             |             | ion      |
+=============+=============+=============+=============+==========+
| 0           | 0           | 1           | 1           | Flush    |
|             |             |             |             | Mode     |
+-------------+-------------+-------------+-------------+----------+
| 0           | 0           | 0           | 0           | Start    |
|             |             |             |             | Mode     |
+-------------+-------------+-------------+-------------+----------+

Perform brushing
~~~~~~~~~~~~~~~~

Power up Development Board

Double-click to run the "auto-myimx93ek200-2g.wic.bat" file in the upgrade package

The Windows command line window displays something like this:

.. code-block:: text

   uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.4.243-0-ged48c51
   Success 0    Failure 0
   1:32    ......

Flashing image succesfull
~~~~~~~~~~~~~~~~~~~~~~~~~

After the flush is complete, the Windows command line window displays the following information:

.. code-block:: text

   uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.4.243-0-ged48c51
   Success 1    Failure 0
   1:32    24/24 [Done                                  ] FBK: DONE
   Press any key to continue...

Start Development Board
~~~~~~~~~~~~~~~~~~~~~~~

Power off Development Board, dial "SW1" to start mode, power on Development Board, Development Board can start normally


