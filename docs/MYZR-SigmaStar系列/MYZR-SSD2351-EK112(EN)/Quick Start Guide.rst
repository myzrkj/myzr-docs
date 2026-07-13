
.. raw:: html

   <style>
   h1 {
       color: #4CAF50;  /* Level 1 heading font color */
   }
   </style>


Quick Start Guide
=================
Note: The following applies to the UBIFS version system.

Connecting the Development Board
--------------------------------
**Preparation**

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;  /* Center header text */
   }
     td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;  /* Center first row content */
   }

   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width */
   }
   td {
       word-wrap: break-word;  /* Auto wrap long content */
   }
   </style>

+-------------------------------------+--------+
| Check Development Board Accessories |        |
+=====================================+========+
| Development Board                   | 1 unit |
+-------------------------------------+--------+
| TYPE-C Cable                        | 1 pc   |
+-------------------------------------+--------+
| TTL Serial Module                   | 1 unit |
+-------------------------------------+--------+
**Screen Connection Notes**

- Please follow the screen connection method strictly as shown. The connector is not keyed.
- Reversing the connection will damage the screen and board.

.. image:: ../../../image/MYZR-SigmaStar系列/MYZR-SSD2351/接线方向.jpg
   :alt: Connection Direction
   :width: 100%

**Check Power Switch**

Press the "o" position of the power switch "SW1" on the development board to ensure it is in the off position.

**Serial Port Settings**

+----------+----------+----------+----------+
| Baud Rate| Data Bits| Stop Bits| Parity   |
+==========+==========+==========+==========+
| 115200   | 8bit     | 1bit     | none     |
+----------+----------+----------+----------+

**DIP Switch Settings and TTL Serial Module**

Boot DIP switch setting: 1: on, 2: on, 3: off, 4: off

**TTL Serial Module Connection**

Use a TTL serial module. The debug serial port is J3. Connect the corresponding CPU pins to the TTL module pins as follows:

+-------------+----------------------------+----------------------------+----------------------------+
| **CPU Side**| J3_1: RX Pin (Square pad)  | J3_2: TX Pin               | J3_3: GND                  |
+-------------+----------------------------+----------------------------+----------------------------+
| **TTL Side**| TX Pin                     | RX Pin                     | GND                        |
+-------------+----------------------------+----------------------------+----------------------------+

**Download Cable Connection**

Use a TYPE-C cable. Connect one end to the board's Type-C port and the other end to the computer's USB port.

**Power Cable Connection**

Option 1: Use a 5V/2A DC power supply. Option 2: Power via USB through the Type-C cable from the PC.

Powering On the Development Board
---------------------------------
**Power Up the Board**

DIP Switch Settings:

Boot DIP switch setting: 1: on, 2: on, 3: off, 4: off

Understanding Boot Information
------------------------------
**U-Boot Information**

After power-on, the serial port prints SPINAND flash initialization, DDR memory detection, and environment variable loading information. It outputs U-Boot 2021.10 version, SigmaStar pcupid SoC, 128MiB DRAM capacity, SPI NAND parameters, and MTD partition address list. By default, it automatically counts down to boot the kernel. Press any key during the countdown to stop auto-boot and enter the U-Boot command line.

**Kernel Information**

U-Boot loads and decompresses the Linux image, printing Linux version 6.1.111-rt42, quad-core ARMv7 processor information, memory partition configuration, and device tree matching information. It then outputs multi-core initialization, driver loading logs for peripherals (I2C/SPI/Ethernet/Audio/NAND/UBIFS), and NAND flash partition information. Finally, it mounts the squashfs root filesystem and UBIFS data partition, entering the user initialization script.

Logging Into the Development Board
----------------------------------
**Serial Login**

.. code-block:: shell

   #Connect the board to the computer using the TTL module. Insert the TYPE-C cable and power on.
   # Username is root, no password, press Enter to login
   U-Boot 2021.10 (Aug 04 2025 - 14:14:26 +0000)
   
   SoC: SigmaStar pcupid
   Model: PCUPID
   Version: P###g#######
   DRAM:  128 MiB
   WDT:   Not found!
   NAND:  SPI 104M
   [SPINAND] RFC use command 0x6b
   [SPINAND] dummy clock 0x8
   [SPINAND] Program with command 0x32.
   [SPINAND] Random with command 0x34.
   [FLASH] BDMA mode.
   spi clk already initialized
   [FLASH] dev_id = 0xee
   [FLASH] mfr_id = 0xc8, dev_id= 0x91 id_len = 0x2
   128 MiB
   MMC:   Fail to get pad(0x20309) ip(0x2_8)  form padmux !
   ......
   mi wbc debug init success
   mi pspi debug init success
   mi GFX debug init success
   mi scl debug init success
   mi isp debug init success
   mi FB debug init success
   mi vdisp debug init success
   mi ipu debug init success
   module [debug] init
   pad 0 register
   pad 2 register
   [emac_phy_link_adjust] EMAC Link Down 
   Starting system message bus: Gadget configfs UDC:1f284200.msb250x-udc-p0
   done
   Starting iptables: CMDQ - IRQ Request 0 
   OK
   Starting bluetoothd: OK
   Starting network: OK
   Starting crond: OK
   Starting sshd: OK
   
   Welcome to MYZR-SSD2351-EK112
   myzr login: 
   Welcome to MYZR-SSD2351-EK112
   myzr login: 

**ADB Connection Login**

.. code-block:: shell

   #Power via TYPE-C cable. Open CMD terminal on Windows 10. Enter adb shell and ls as follows:
   adb shell
   * daemon not running. starting it now on port 5037 *
   * daemon started successfully *
   root@myzr:~#
   Files are visible, indicating successful login.

**SSH Login via Ethernet**

.. code-block:: shell

   #Connect Ethernet cable and configure IP address (My PC IP: 192.168.137.99)
   #Default board IP: 192.168.137.81
   #Can login via serial software:
   #Click File->New in serial software
   #Set Protocol to SSH
   #Set host to 192.168.137.81
   #Click Connect. Username is root, no password, press Enter to login:
   Connecting to 192.168.137.81:22...
   Connection established.
   To escape to local shell, press 'Ctrl+Alt+]'.
   
   WARNING! The remote SSH server rejected X11 forwarding request.
   root@myzr:~# 
   root@myzr:~# 
   root@myzr:~#