.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Boot Manual
===========

Connection of serial port cable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Connect one end of the serial cable to the "P2" port of the Development Board, and the other end to the serial port of the computer or the USB port.

#. Refer to the Xshell Reference Manual to create a new serial session and open a session.

Connection of network cables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect one end of the network cable to "U17" or "U19" and the other end to the network port of the computer.

Connection of download lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect one end of the type-c data cable to "U9", and the other end to the computer's rear USB port.

Start Development Board
-----------------------

Check the startup mode dialing of Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Turn the "SW1" dial switch of the Development Board to the startup mode.

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

+------+------+------+------+----------+
| 1    | 2    | 3    | 4    | Descript |
|      |      |      |      | ion      |
+======+======+======+======+==========+
| 0    | 0    | 0    | 0    | Start    |
|      |      |      |      | Mode     |
+------+------+------+------+----------+
| 0    | 0    | 1    | 1    | Flush    |
|      |      |      |      | Mode     |
+------+------+------+------+----------+

Note: The ON (1) of the dial switch is the letter side, and the OFF (0) is the number side.

Power up Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect one end of the power adapter to the "J1" of the Development Board and the other end to a mains (220V AC) outlet.

Development Board Login
-----------------------

After booting the system and outputting imx93evk login:, you can log in:

[Username]: root

[Password]: None

Tip: After logging in, you can set and change your password with the "passwd" command.
