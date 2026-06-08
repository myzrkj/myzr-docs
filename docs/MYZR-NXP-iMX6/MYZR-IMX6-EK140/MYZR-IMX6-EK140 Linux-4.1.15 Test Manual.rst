
MYZR-IMX6-EK140 Linux-4.1.15 Test Manual
===========================================

Test Environment
-------------------

- Development board model：MYZR-IMX6-EK140-6Y
- Kernel version：Linux-4.1.15
- File system：L4115-core-image-base-myimx6a7.tar.bz2

Preparation before test
-------------------------

|  1）Please connect following the path of :doc:`《Linux fast boot manual》<MYZR-IMX6-EK140 Quick Start>` ->“Linux fast boot” -> “device connection”.
|  2）Please boot following the path of :doc:`《Linux fast boot manual》<MYZR-IMX6-EK140 Quick Start>` ->“Linux fast boot” -> “device booting”.

Test item
-----------

Network inferface test
~~~~~~~~~~~~~~~~~~~~~~~~~

|  MYZR-IMX6-EK140 support one 100 Mbps ethernet interfaces.

**Interface property**

|  ENET Interface position：P2

**Test method**

|  1）Configure computer IP
|  Set wired network card IP of computer as 192.168.18.18
|  2）ENET connect test
|  Connect lan line: connect “eth0”on evaluation board with corresponding wired network card interface on computer with lan line.

- Set evaluation board IP：

.. code-block:: shell

   # ifconfig eth0 192.168.18.100

|  Execute test command：

.. code-block:: shell

   # ping 192.168.18.18 -c 4

- Observe test result：system will output message like following:

.. code-block:: shell

   PING 192.168.18.18 (192.168.18.18): 56 data bytes
   64 bytes from 192.168.18.18: seq=0 ttl=64 time=2.848 ms
   64 bytes from 192.168.18.18: seq=1 ttl=64 time=0.496 ms
   64 bytes from 192.168.18.18: seq=2 ttl=64 time=0.478 ms
   64 bytes from 192.168.18.18: seq=3 ttl=64 time=0.518 ms

   --- 192.168.18.18 ping statistics ---
   4 packets transmitted, 4 packets received, 0% packet loss
   round-trip min/avg/max = 0.478/1.085/2.848 ms

- Test result：“0% packet loss”represent test passing.

USB Test
---------

**Interface attributes**

|  Interface location: P3

**Test Method**

|  1）Start test
|  Insert USB device into USB port on base board，system will output message like following：

.. code-block:: shell

   usb 1-1: new high-speed USB device number 2 using ci_hdrc
   usb-storage 1-1:1.0: USB Mass Storage device detected
   scsi host0: usb-storage 1-1:1.0
   scsi 0:0:0:0: Direct-Access     SMI      USB DISK         1100 PQ: 0 ANSI: 0 CCS
   sd 0:0:0:0: Attached scsi generic sg0 type 0
   sd 0:0:0:0: [sda] 15730688 512-byte logical blocks: (8.05 GB/7.50 GiB)
   sd 0:0:0:0: [sda] Write Protect is off
   sd 0:0:0:0: [sda] No Caching mode page found
   sd 0:0:0:0: [sda] Assuming drive cache: write through
    sda:
   sd 0:0:0:0: [sda] Attached SCSI removable disk

|  2）Test over Take out USB device from base board，system will output message like following：

.. code-block:: shell

   usb 1-1: USB disconnect, device number 2

- Test results: as above "(8.05 GB/7.50 GiB)" can identify the size of U disk, indicating that the test passed.

TF Card Test
--------------

**Interface properties**

|  Interface location: P5
|  Interface type ：MicroSD

**Test method**

|  1）Start test
|  When the power is off, insert the TF card into the interface of the TF card on the back of the baseplate before starting the system Enter the following command:

.. code-block:: shell

   # dmesg | grep mmc0

|  The system output is similar to the following information, which means the TF interface is normal:

.. code-block:: shell

   mmc0: SDHCI controller on 2190000.usdhc [2190000.usdhc] using ADMA
   mmc0: host does not support reading read-only switch, assuming write-enable
   mmc0: new high speed SDHC card at address 1234
   mmcblk0: mmc0:1234 SA32G 28.9 GiB

|  2）View the system's TF card equipment Enter the following command:

.. code-block:: shell

   # ls /dev/mmcblk0*   

|  The system will output the following information:

.. code-block:: shell

   /dev/mmcblk0    /dev/mmcblk0p1

RGB Screen Test
----------------

|  Test instructions;Show that the connection of module can not be connected with wrong, avoid burning board;

- Refer to the attached picture in the screen module connection in :doc:`《Quick Start》<MYZR-IMX6-EK140 Quick Start>` for the specific connection
- After starting up the development board and entering the system, the following lines of text are displayed on the screen:

.. code-block:: shell

   Freescale i.MX Release Distro 4.1.15-2.1.0 myimxlek140/dev/tty1
   imx6ek140 login:

|  The above display on the screen indicates that the screen is normal.