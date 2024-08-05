
MYZR-R16-EK166 Linux-3.4 Test Manual
======================================

Wifi Test
-----------

.. code:: shell

   $ wifi_connect_ap_test wifi_name password

| **参数说明：**
| "wifi_connect_ap_test" is the application name
| "wifi_name" is the name of the wifi to connect to
| "password" is the password of the wifi to connect to
| For Example:

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test1.png
   :alt: MY-R16-CB166_linux-34_test1.png

USB Test
----------

1. Insert U disk

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test2-1.png
   :alt: MY-R16-CB166_linux-34_test2-1.png

.. code:: shell
   
   $ ls /dev/sda*

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test2-2.png
   :alt: MY-R16-CB166_linux-34_test2-2.png

2. Mount the U disk

.. code:: shell
   
   $ mount /dev/sda4 /mnt

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test2-3.png
   :alt: MY-R16-CB166_linux-34_test2-3.png

3. View the contents of the USB flash drive

.. code:: shell

   $ ls /mnt


.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test2-4.png
   :alt: MY-R16-CB166_linux-34_test2-4.png

4. Uninstall the U disk

.. code:: shell
   
   $ umount /mnt

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test2-5.png
   :alt: MY-R16-CB166_linux-34_test2-5.png

SD card Test
--------------

1. Insert SD card

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test3-1.png
   :alt: MY-R16-CB166_linux-34_test3-1.png
 
.. code:: shell
   
   $ ls /dev/mmcblk1

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test3-2.png
   :alt: MY-R16-CB166_linux-34_test3-2.png

2. Mount the SD card

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test3-3.png
   :alt: MY-R16-CB166_linux-34_test3-3.png

3. View the contents of the SD card

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test3-4.png
   :alt: MY-R16-CB166_linux-34_test3-4.png

4. Uninstall the SD card

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test3-5.png
   :alt: MY-R16-CB166_linux-34_test3-5.png

Audio Test
------------

1. Copy an mp3 file to the development board with a USB flash drive.

.. code:: shell

   $ mount /dev/sda4 /mnt/
   $ cp /mnt/music.mp3 /
   $ cd /
   $ tinyplayer music.mp3

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test4-1.png
   :alt: MY-R16-CB166_linux-34_test4-1.png

2. Volume adjustment

.. code:: shell

   $ amixer controls

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test4-2.png
   :alt: MY-R16-CB166_linux-34_test4-2.png

|  Find out numid=3,iface=MIXER,name='speaker volume control'

3. Gets current volume information

.. code:: shell

   $ amixer cget numid=3,iface=MIXER,name='speaker volume control'

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test4-3.png
   :alt: MY-R16-CB166_linux-34_test4-3.png

4. Set the volume to 50

.. code:: shell

   $ amixer cset numid=3,iface=MIXER,name='speaker volume control' 50

Record Test
-------------

1. Recording

.. code:: shell

   $ arecord -d 10 -D plughw:0 demo.wav

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test5-1.png
   :alt: MY-R16-CB166_linux-34_test5-1.png

2. Play recording

.. code:: shell
   
   $ aplay -Dplug:dmix demo.wav

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test5-2.png
   :alt: MY-R16-CB166_linux-34_test5-2.png

Serial port test
------------------

- The development board has only one UART3, which shorts the pin of pin 13.14 of J20.

.. code:: shell

   $ ./etc/uart.o /dev/ttyS3 “Hello”

- Parameter Description：

 | "uart.o" serial test application name
 | "ttyS3" serial port to be tested
 | "Hello" message content to be sent

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test6-1.png
   :alt: MY-R16-CB166_linux-34_test6-1.png

Network port test
-------------------

- Set your computer's local IP to 192.168.18.18 ，and close your computer's firewall.Connect the development board to the computer with a network cable and execute the following command:

.. code:: shell

   $ ifconfig eth0 192.168.18.36
   $ ping 192.168.18.18

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test7-1.png
   :alt: MY-R16-CB166_linux-34_test7-1.png

4G Test
---------

- The test takes L506 as an example (L506 is the 4G module of total network access)
- The test card is a mobile card.
- The dialup script is in the /etc/ppp/peers/ directory.
- Dial：

.. code:: shell

   $ pppd call gprsdial &

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test8-1.png
   :alt: MY-R16-CB166_linux-34_test8-1.png

- Check the IP

.. code:: shell

   $ ifconfig ppp0

.. image:: ../../../../image/MYZR-国产系列/Allwinner平台/MYZR-R16-EK166/MY-R16-CB166_linux-34_test8-2.png
   :alt: MY-R16-CB166_linux-34_test8-2.png


::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2023/5/08  
   * Supporter: Zhong JiaYi
   --------------------------------------------------------------------------------
