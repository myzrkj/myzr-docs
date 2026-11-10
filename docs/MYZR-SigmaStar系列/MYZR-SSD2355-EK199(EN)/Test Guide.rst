.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Test Guide
==========

Network Port Test
-----------------

Port 0
~~~~~~

[Test Description]: Use Development Board to send ICMP message to PC for testing

[Interface identification]: ETH1

[System equipment]: eth0

[Test Procedure]:

#. Use the network cable to connect the Development Board network port and the computer's network port, enter the following command to open the network port 0

   .. code-block:: text

      ifconfig eth0 up

   The output information is as follows

   .. code-block:: text

      [emac_phy_link_adjust] EMAC Link Up

#. Enter the following command to get the network port IP

   .. code-block:: text

      udhcpc -i eth0 -s /etc/init.d/udhcpc.script

   The output information is as follows

   .. code-block:: text

      /# udhcpc -i eth0 -s /etc/init.d/udhcpc.script
      udhcpc (v1.20.2) started
      Setting IP address 0.0.0.0 on eth0
      Sending discover...
      Sendingselectfor192.168.128.40...
      Lease of 192.168.128.40 obtained, lease time 300
      Setting IP address 192.168.128.40 on eth0
      Deleting routers
      route: SIOCDELRT: No such process
      Adding router 192.168.128.1
      Recreating /customer/resolv.conf
      Adding DNS server 192.168.128.1

#. Enter the following command for network port verification

   .. code-block:: text

      pingbaidu.com-c 4

   The output information is as follows: "0% packet loss" means that the test passed

   .. code-block:: text

      # pingbaidu.com-c 4
      PINGbaidu.com(124.237.177.164): 56 data bytes
      64 bytes from 124.237.177.164: seq=0 ttl=53 time=35.747 ms
      64 bytes from 124.237.177.164: seq=1 ttl=53 time=35.424 ms
      64 bytes from 124.237.177.164: seq=2 ttl=53 time=35.335 ms
      64 bytes from 124.237.177.164: seq=3 ttl=53 time=35.782 ms
      ---baidu.comping statistics ---
      4 packets transmitted, 4 packets received, 0% packet loss

Network port 1
~~~~~~~~~~~~~~

[Test Description]: Use Development Board to send ICMP message to PC for testing

[Interface identification]: ETH2

[System equipment]: eth1

[Test Procedure]:

#. Use the network cable to connect the Development Board network port and the computer's network port, enter the following command to open the network port 0

   .. code-block:: text

      ifconfig eth1 up

   The output information is as follows

   .. code-block:: text

      [emac_phy_link_adjust] EMAC Link Up

#. Enter the following command to get the network port IP

   .. code-block:: text

      udhcpc -i eth1 -s /etc/init.d/udhcpc.script

   The output information is as follows

   .. code-block:: text

      /# udhcpc -i eth1 -s /etc/init.d/udhcpc.script
      udhcpc (v1.20.2) started
      Setting IP address 0.0.0.0 on eth1
      Sending discover...
      Sendingselectfor192.168.128.40...
      Lease of 192.168.128.40 obtained, lease time 300
      Setting IP address 192.168.128.40 on eth1
      Deleting routers
      route: SIOCDELRT: No such process
      Adding router 192.168.128.1
      Recreating /customer/resolv.conf
      Adding DNS server 192.168.128.1
      mount: mounting /customer/resolv.conf on /etc/resolv.conf failed: No such file or directory

#. Enter the following command for network port verification

   .. code-block:: text

      pingbaidu.com-c 4

   The output information is as follows: "0% packet loss" means that the test passed

   .. code-block:: text

      # pingbaidu.com-c 4
      PINGbaidu.com(124.237.177.164): 56 data bytes
      64 bytes from 124.237.177.164: seq=0 ttl=53 time=35.747 ms
      64 bytes from 124.237.177.164: seq=1 ttl=53 time=35.424 ms
      64 bytes from 124.237.177.164: seq=2 ttl=53 time=35.335 ms
      64 bytes from 124.237.177.164: seq=3 ttl=53 time=35.782 ms
      ---baidu.comping statistics ---
      4 packets transmitted, 4 packets received, 0% packet loss

USB Test
--------

[Test Description]: Hot-swappable test

[Interface identification]: HOST

[System equipment]: /dev/sda1

[Test Procedure]:

#. PM_SAR_GPIO4 needs to be pulled higher to recognize the device, enter the following command

   .. code-block:: text

      echo 147 > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio147/direction
      echo 1 > /sys/class/gpio/gpio147/value

#. Insert the USB flash drive Enter the following command to view the USB flash drive information

   .. code-block:: text

      fdisk -l

   The output information is as follows

   .. code-block:: text

      Disk /dev/sda: 247.9 GB, 247993466880 bytes
      256 heads, 63 sectors/track, 30032 cylinders
      Units = cylinders of 16128 * 512 = 8257536 bytes
      Device Boot      Start         End      Blocks  Id System
      /dev/sda1               1       30033   242181088+ 83 Linux

SD Card Test
------------

[Test Description]: Hot-swappable test

[Interface identification]: SD

[System equipment]: /dev/mmcblk0p1

[Test Procedure]:

#. Insert the sd card and enter the following command to view the sd card information

   .. code-block:: text

      fdisk -l

   The output information is as follows

   .. code-block:: text

      Disk /dev/mmcblk0: 7746 MB, 7746879488 bytes
      256 heads, 63 sectors/track, 938 cylinders
      Units = cylinders of 16128 * 512 = 8257536 bytes
      
      Device Boot      Start         End      Blocks  Id System
      /dev/mmcblk0p1   *           1         939     7564288   c Win95 FAT32 (LBA)
      Partition 1 has different physical/logical beginnings (non-Linux?):
      phys=(1023, 255, 63) logical=(0, 32, 33)
      Partition 1 has different physical/logical endings:
      phys=(1023, 255, 63) logical=(938, 40, 40)

GPIO Test
---------

[Test Description]: Test by pulling the pin high and low

[Interface identification]:

[System equipment]: /sys/class/gpio/

[Test Procedure]:

GPIOE_01 (facing the position of the pin number 4 on the left in the direction of the network port)

#. Enter the following command to raise gpioe_01

   .. code-block:: shell

      echo 10 > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio10/direction
      echo 1 > /sys/class/gpio/gpio10/value
      cat /sys/class/gpio/gpio10/value

   At this time, the pin can be seen as high 3.3v with a multimeter

#. Pull down gpioe_01 by entering the following command

   .. code-block:: text

      echo 0 > /sys/class/gpio/gpio10/value
      cat /sys/class/gpio/gpio10/value

   At this time, the pin can be seen as low level 0v with a multimeter

GPIOE_02 (the position of the opposite pin facing the pin row number 6 on the left in the direction of the network port)

#. Enter the following command to raise gpioe_02

   .. code-block:: shell

      echo 11 > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio11/direction
      echo 1 > /sys/class/gpio/gpio11/value
      cat /sys/class/gpio/gpio11/value

   At this time, the pin can be seen as high 3.3v with a multimeter

#. Pull down gpioe_02 by entering the following command

   .. code-block:: text

      echo 0 > /sys/class/gpio/gpio11/value
      cat /sys/class/gpio/gpio11/value

   At this time, the pin can be seen as low level 0v with a multimeter

GPIOE_03 (the position of the opposite pin facing the pin row number 5 on the left in the direction of the network port)

#. Enter the following command to raise gpioe_03

   .. code-block:: shell

      echo 12 > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio12/direction
      echo 1 > /sys/class/gpio/gpio12/value
      cat /sys/class/gpio/gpio12/value

   At this time, the pin can be seen as high 3.3v with a multimeter

#. Pull down gpioe_03 by entering the following command

   .. code-block:: text

      echo 0 > /sys/class/gpio/gpio12/value
      cat /sys/class/gpio/gpio12/value

   At this time, the pin can be seen as low level 0v with a multimeter

GPIOE_04 (facing the position of the number -6 on the left side of the network port)

#. Enter the following command to raise gpioe_04

   .. code-block:: shell

      echo 13 > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio13/direction
      echo 1 > /sys/class/gpio/gpio13/value
      cat /sys/class/gpio/gpio13/value

   At this time, the pin can be seen as high 3.3v with a multimeter

#. Pull down gpioe_04 by entering the following command

   .. code-block:: text

      echo 0 > /sys/class/gpio/gpio13/value
      cat /sys/class/gpio/gpio13/value

   At this time, the pin can be seen as low level 0v with a multimeter

GPIOE_05 (opposite position of the row pin number -5 on the left in the direction of the network port)

#. Enter the following command to raise gpioe_05

   .. code-block:: shell

      echo 14 > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio14/direction
      echo 1 > /sys/class/gpio/gpio14/value
      cat /sys/class/gpio/gpio14/value

   At this time, the pin can be seen as high 3.3v with a multimeter

#. Pull down gpioe_05 by entering the following command

   .. code-block:: text

      echo 0 > /sys/class/gpio/gpio14/value
      cat /sys/class/gpio/gpio14/value

   At this time, the pin can be seen as low level 0v with a multimeter

LED Test
--------

[Test Description]: Test by pulling the pin high and low

[Interface identification]: led2, led3, led4

System equipment

[Test Procedure]:

LED2
~~~~

#. Enter the following command, led2 is on

   .. code-block:: text

      JavaScript
      echo 75 > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio75/direction
      echo 1 > /sys/class/gpio/gpio75/value

#. Enter the following command, led2 extinguished

   .. code-block:: text

      echo 0 > /sys/class/gpio/gpio75/value

LED3
~~~~

#. Enter the following command, led3 is lit

   .. code-block:: text

      JavaScript
      echo 74 > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio74/direction
      echo 1 > /sys/class/gpio/gpio74/value

#. Enter the following command to extinguish led3

   .. code-block:: text

      echo 0 > /sys/class/gpio/gpio74/value

LED4
~~~~

#. Enter the following command, led4 light

   .. code-block:: text

      JavaScript
      echo 69 > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio69/direction
      echo 1 > /sys/class/gpio/gpio69/value

#. Enter the following command to extinguish led4

   .. code-block:: text

      echo 0  > /sys/class/gpio/gpio69/value

I2C Test
--------

[Test Description]: Test by reading the address of the i2c device

[System equipment]: ttyS2, ttyS3, ttyS4

[Test Procedure]:

I2C2
~~~~

#. Enter the test catalog and enter the following command

   .. code-block:: text

      cd /customer

#. Connect the two pins scl, sda of the i2c device to the scl, sda of i2c0, gnd to the gnd of Development Board, the address of the i2c device for testing is 0x3c, enter the following command to read the i2c device

   .. code-block:: text

      ./i2cdump -f -y 2 0x3c

   The output information is as follows

   .. code-block:: text

      /customer# ./i2cdump -f -y 2 0x3c
      No size specified (using byte-data access)     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
      00: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      10: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      20: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      30: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      40: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      50: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      60: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      70: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      80: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      90: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      a0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      b0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      c0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      d0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      e0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      f0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB

I2C3
~~~~

#. Enter the test catalog and enter the following command

   .. code-block:: text

      cd /customer

#. Connect the two pins scl, sda of the i2c device to the scl, sda of i2c0, gnd to the gnd of Development Board, the address of the i2c device for testing is 0x3c, enter the following command to read the i2c device

   .. code-block:: text

      ./i2cdump -f -y 3 0x3c

   The output information is as follows

   .. code-block:: text

      /customer# ./i2cdump -f -y 3 0x3c
      No size specified (using byte-data access)     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
      00: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      10: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      20: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      30: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      40: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      50: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      60: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      70: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      80: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      90: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      a0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      b0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      c0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      d0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      e0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      f0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB

I2C4
~~~~

#. Enter the test catalog and enter the following command

   .. code-block:: text

      cd /customer

#. Connect the two pins scl, sda of the i2c device to the scl, sda of i2c0, gnd to the gnd of Development Board, the address of the i2c device for testing is 0x3c, enter the following command to read the i2c device

   .. code-block:: text

      ./i2cdump -f -y 4 0x3c

   The output information is as follows

   .. code-block:: text

      /customer# ./i2cdump -f -y 4 0x3c
      No size specified (using byte-data access)     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f    0123456789abcdef
      00: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      10: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      20: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      30: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      40: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      50: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      60: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      70: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      80: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      90: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      a0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      b0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      c0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      d0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      e0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB
      f0: 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42 42    BBBBBBBBBBBBBBBB

Verified WiFi
-------------

[Test Description]: Connect the 2.4G antenna to the Development Board WIFI (CON23) interface, and Development Board sends a ICMP message to the external network to verify that the connection is normal.

[Interface identification]: u23

[System equipment]: wlan0

[Test Procedure]

Wifi password change

.. code-block:: text

   JavaScript
   1. Edit the profile (your steps are correct, make sure the ssid and psk match the hotspot)
   vi /customer/wifi/wpa_supplicant.conf
   # Profile contents (without modification, make sure ssid = "iQOO", psk = "1234567890") ctrl_interface = /tmp/wifi/run/wpa_supplicant
   update_config=1network={ssid="iQOO"//WiFi name
   psk="1234567890"//WiFi password
   }

#. Enter the following command to set the path

   .. code-block:: text

      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/customer/wifi/

#. Enable WiFi by entering the following command

   .. code-block:: text

      ifconfig wlan0 up

   The output information is as follows, press enter

   .. code-block:: text

      RTW: ==> rtl8723du_hal_deinit
      RTW: CardDisableRTL8723du(wlan0): bMacPwrCtrlOn=1
      RTW: SetHwReg: bMacPwrCtrlOn=0
      RTW: <=== rtw_ips_pwr_down.....................in40ms
      Press Enter

#. Create an interface by entering the following command

   .. code-block:: text

      mkdir -p /tmp/wifi/run

#. Start the wifi by entering the following command

   .. code-block:: text

      /customer/wifi/wpa_supplicant -Dnl80211 -i wlan0 -c /customer/wifi/wpa_supplicant.conf -d &

   The output information is as follows, press enter

   .. code-block:: text

      RTW: WARN Invalid hw_rate 0xffinhw_rate_to_m_rate
      RTW: WARN Invalid hw_rate 0xffinhw_rate_to_m_rate
      EAPOL: startWhen --> 0
      EAPOL: disable timer tick
      RTW: rtw_set_ps_mode(wlan0) Enter 802.11 power save - WIFI-TRAFFIC_IDLE
      RTW: rtl8723d_set_FwPwrMode_cmd(): FW LPS mode = 2, SmartPS=2
      Press Enter

#. Start getting the WiFi IP by entering the following command

   .. code-block:: text

      udhcpc -q -i wlan0 -s /etc/init.d/udhcpc.script &

   The output information is as follows, press enter

   .. code-block:: text

      Lease of 192.168.112.202 obtained, lease time 3599
      Setting IP address 192.168.112.202 on wlan0
      Deleting routers
      route: SIOCDELRT: No such process
      Adding router 192.168.112.210
      Recreating /customer/resolv.conf
      Adding DNS server 192.168.112.210
      RTW: rtw_set_ps_mode(wlan0) Enter 802.11 power save - WIFI-TRAFFIC_IDLE
      RTW: rtl8723d_set_FwPwrMode_cmd(): FW LPS mode = 2, SmartPS=2
      RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 SeqNum = 5
      Press Enter

#. Verify your wifi by entering the following command

   .. code-block:: text

      ping www.baidu.com -c 3

   The output information is as follows, 0% packe means normal, press enter

   .. code-block:: text

      Python
      /# ping www.baidu.com -c 3
      PING www.baidu.com (183.2.172.177): 56 data bRTW: rtw_set_ps_mode(wlan0) Leave 802.11 power save - WIFI-LPS_CTRL_LEAVE
      RTW: rtl8723d_set_FwPwrMode_cmd(): FW LPS mode = 0, SmartPS=2
      ytes
      64 bytes from 183.2.172.177: seq=0 ttl=52 time=56.453 ms
      64 bytes from 183.2.172.177: seq=1 ttl=52 time=34.263 ms
      64 bytes from 183.2.172.177: seq=2 ttl=52 time=35.835 ms
      --- www.baidu.com ping statistics ---
      3 packets transmitted, 3 packets received, 0% packet loss
      round-trip min/avg/max = 34.263/42.183/56.453 ms
      /# RTW: rtw_set_ps_mode(wlan0) Enter 802.11 power save - WIFI-TRAFFIC_IDLE
      RTW: rtl8723d_set_FwPwrMode_cmd(): FW LPS mode = 2, SmartPS=2
      RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 SeqNum = 11
      RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0806) rate=0x0 Se

Headset Test
------------

[Test Description]: Test the headset with an audio file

[Interface identification]: J3

System equipment

[Test Procedure]:

#. Plug in the headset and enter the following command

   .. code-block:: text

      cd customer
      ./prog_audio_ai_ao_demo playback -i dac -f ./sample-9s.wav -a 0 -d 0 -c 2 -t 20 -v 60

#. At this point, the headphones can be heard in both channels

SPEAKER * 2 test
----------------

[Test Description]: Test SPEAKER with an audio file

[Interface identification]: P1, P2

[System Equipment]:

[Test Procedure]:

#. Insert the speaker and enter the following command

   .. code-block:: text

      cd customer
      ./prog_audio_ai_ao_demo playback -i dac -f ./sample-9s.wav -a 0 -d 0 -c 2 -t 20 -v 60

#. At this point, both spk1 and spk2 can be heard.

Recording Test
--------------

[Test Description]: Generate recording file and play test

[Interface identification]: J3 (headset MIC1), MIC0, MIC2

[Test Procedure]:

#. Insert the headset and enter the following command

   .. code-block:: text

      cd /customer
      ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic1.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60

#. Can speak to headphones until end of recording

#. After recording, enter the following command to play the audio you just recorded

   .. code-block:: text

      ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic1.wav -a 0 -d 0 -c 2 -t 20 -v 80

#. At this time, insert the speaker into spk1 or insert the headset, the speaker will have a sound, and the right channel of the headset will have a sound

#. Insert the recording device into the MIC0 and enter the following command

   .. code-block:: text

      cd /customer
      ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic0.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60

#. Speak to the recording device until the end of the recording

#. After recording, enter the following command to play the audio you just recorded

   .. code-block:: text

      ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic0.wav -a 0 -d 0 -c 2 -t 20 -v 80

#. At this time, insert the speaker into spk2 or insert the headset, the speaker will have a sound, and the left channel of the headset will have a sound

#. Insert the recording device into the MIC2 and enter the following command

   .. code-block:: text

      cd /customer
      ./prog_audio_ai_ao_demo capture -i adc_b -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60

#. Speak to the recording device until the end of the recording

#. After recording, enter the following command to play the audio you just recorded

   .. code-block:: text

      ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic2.wav -a 0 -d 0 -c 2 -t 20 -v 80

#. At this time, insert the speaker to spk1, spk2 or insert the headset, the speaker will have a sound, the left and right channels of the headset will have a sound

   .. code-block:: shell

      #MIC0
      Recording Test
      ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic0.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60#MIC1
      Recording Test
      ./prog_audio_ai_ao_demo capture -i adc_a -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60#MIC2
      Recording Test
      ./prog_audio_ai_ao_demo capture -i adc_b -F test_amic2.wav -A 0 -D 0 -R 8000 -C 2 -T 10 -V 60
      Playing a recording
      ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic0.wav -a 0 -d 0 -c 2 -t 20 -v 80
      ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic1.wav -a 0 -d 0 -c 2 -t 20 -v 80
      ./prog_audio_ai_ao_demo playback -i dac -f ./test_amic2.wav -a 0 -d 0 -c 2 -t 20 -v 80

PWM Test
--------

[Test Description]: Use an oscilloscope to check the waveform of the pwm pin

[System equipment]: sys /class/sstar/pwm/

[Test Procedure]:

Normal PWM Test
~~~~~~~~~~~~~~~

#. Enter the following command to configure pwm3

   .. code-block:: shell

      cd sys/class/sstar/pwm/group0
      /sys/devices/virtual/sstar/pwm/group2# cd pwm3
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 1000000  > period
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 500000   > duty
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo normal   > polarity
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 1        > enable

   At this time, the network port direction is facing you, and the waveform can be seen by using the oscilloscope test on the right number of the third pin under this row of pins above.

#. Enter the following command to configure pwm6

   .. code-block:: shell

      cd sys/class/sstar/pwm/group1
      /sys/devices/virtual/sstar/pwm/group2# cd pwm6
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 1000000  > period
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 500000   > duty
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo normal   > polarity
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 1        > enable

   At this time, the network port direction is facing you, and the right number of the second pin below the above row of pins can be seen using the oscilloscope test.

#. Enter the following command to configure pwm7

   .. code-block:: shell

      cd sys/class/sstar/pwm/group1
      /sys/devices/virtual/sstar/pwm/group2# cd pwm7
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 1000000  > period
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 500000   > duty
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo normal   > polarity
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 1        > enable

   At this time, the network port direction is facing you, and the 4th pin on the lower right of the above row of pins can be seen using the oscilloscope test.

#. Enter the following command to configure pwm8

   .. code-block:: shell

      cd sys/class/sstar/pwm/group2
      /sys/devices/virtual/sstar/pwm/group2# cd pwm8
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 1000000  > period
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 500000   > duty
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo normal   > polarity
      /sys/devices/virtual/sstar/pwm/group2/pwm8# echo 1        > enable

   At this time, the network port direction is facing you, and the 6th pin on the lower right of the above row of pins can be seen using the oscilloscope test.

RS232 Test
----------

[Test Description]: Short-circuit 232_TX1,232_RX1 232_TX2,232_RX2 for self-transmit test

[Interface ID]: 232_TX1,232_RX1 232_TX2,232_RX2

[System equipment]: /dev/ttyS4, ttyS5

[Test Procedure]:

RS232-1
~~~~~~~

#. Short Connect with DuPont 232_TX1,232_RX1

#. Enter the test catalog and enter the following command:

   .. code-block:: text

      cd customer/

#. Run the test program and enter the following command:

   .. code-block:: text

      ./serial_test.out /dev/ttyS3 12345

   The output information is as follows:

   .. code-block:: text

      Starting send data...finish
      Starting receive data:
      ASCII: 0x31          Character: 1
      ASCII: 0x32          Character: 2
      ASCII: 0x33          Character: 3
      ASCII: 0x34          Character: 4
      ASCII: 0x35          Character: 5

RS232-2
~~~~~~~

#. Short Connect with DuPont 232_TX2,232_RX2

#. Enter the test catalog and enter the following command:

   .. code-block:: text

      cd customer/

#. Run the test program and enter the following command:

   .. code-block:: text

      ./serial_test.out /dev/ttyS2 12345

   The output information is as follows:

   .. code-block:: text

      Starting send data...finish
      Starting receive data:
      ASCII: 0x31          Character: 1
      ASCII: 0x32          Character: 2
      ASCII: 0x33          Character: 3
      ASCII: 0x34          Character: 4
      ASCII: 0x35          Character: 5

RS485 Test
----------

[Test Description]: Transceiving test through 485- USB converter and computer interconnection

[Interface ID]: 485_A1,485_B1,485_A2,485_B2

[System equipment]: /dev/ttyS1, ttyS8

[Test Procedure]:

RS485-1
~~~~~~~

#. Use the 485-USB adapter to connect the Development Board to the computer (A to A, B to B)

#. Use Xshell to open the corresponding serial port, set Portland to 115200, the data is 8 bits, and the stop bit is 1 bit

#. Enter the test directory and enter the following command:

   .. code-block:: text

      cd customer/

#. Run the test and enter the following command:

   .. code-block:: text

      ./serial_test.out /dev/ttyS1 12345

   As a result, you can see the 485 serial port terminal output

   .. code-block:: text

      Connecting to COM5...
      Connected.
      
      12345

#. At 485 serial terminal input 6 (no display), 6 can be seen at the board terminal

   .. code-block:: text

      Starting send data...finish
      Starting receive data:
      ASCII: 0x36          Character: 6

RS485-2
~~~~~~~

#. Use the 485-USB adapter to connect the Development Board to the computer (A to A, B to B)

#. Use Xshell to open the corresponding serial port, set Portland to 115200, the data is 8 bits, and the stop bit is 1 bit

#. Enter the test directory and enter the following command:

   .. code-block:: text

      cd /customer/

#. Run the test and enter the following command:

   .. code-block:: text

      ./serial_test.out /dev/ttyS8 12345

   As a result, you can see the 485 serial port terminal output

   .. code-block:: text

      Connecting to COM5...
      Connected.
      
      12345

#. At 485 serial terminal input 6 (no display), 6 can be seen at the board terminal

   .. code-block:: text

      Starting send data...finish
      Starting receive data:
      ASCII: 0x36          Character: 6

UART Test
---------

[Test Description]: Self-receiving test for short-circuit related pins

[System equipment]: /dev/ttyS4, ttyS5, ttyS7

[Test Procedure]:

UART4
~~~~~

#. Short-circuit RX4_3, TX4_3 pins for self-test

#. Enter the test directory and enter the following command:

   .. code-block:: text

      cd /customer/

#. Run the test and enter the following command:

   .. code-block:: text

      ./serial_test.out /dev/ttyS4 12345

   The output information is as follows:

   .. code-block:: text

      Starting send data...finish
      Starting receive data:
      ASCII: 0x31          Character: 1
      ASCII: 0x32          Character: 2
      ASCII: 0x33          Character: 3
      ASCII: 0x34          Character: 4
      ASCII: 0x35          Character: 5

UART5
~~~~~

#. Short-circuit TX5_1, RX5_1 (-10 up and down) pins for self-transmit test

#. Enter the test directory and enter the following command:

   .. code-block:: text

      cd customer/

#. Run the test and enter the following command:

   .. code-block:: text

      ./serial_test.out /dev/ttyS5 12345

   The output information is as follows:

   .. code-block:: text

      Starting send data...finish
      Starting receive data:
      ASCII: 0x31          Character: 1
      ASCII: 0x32          Character: 2
      ASCII: 0x33          Character: 3
      ASCII: 0x34          Character: 4
      ASCII: 0x35          Character: 5

UART7
~~~~~

#. Short-circuit RX7_3 TX7_3 pin for self-test

#. Enter the test directory and enter the following command:

   .. code-block:: text

      cd /customer/

#. Run the test and enter the following command:

   .. code-block:: text

      ./serial_test.out /dev/ttyS7 12345

   The output information is as follows:

   .. code-block:: text

      Starting send data...finish
      Starting receive data:
      ASCII: 0x31          Character: 1
      ASCII: 0x32          Character: 2
      ASCII: 0x33          Character: 3
      ASCII: 0x34          Character: 4
      ASCII: 0x35          Character: 5

4G testing
----------

[Test Description]: Connect the 2.4G antenna to the EC204g module interface, and Development Board sends a ICMP message to the external network to verify that the connection is normal.

[Interface identification]: CON6

[System equipment]: usb0

[Test Procedure]

#. Enter the test application path and enter the following command

   .. code-block:: text

      cd customer/

#. Enter the following command to start 4g

   .. code-block:: text

      ./4g

   The output information is as follows

   .. code-block:: text

      /customer# ./4g
      Starting 4G network...
      udhcpc (v1.20.2) started
      Sending discover...
      Sendingselectfor192.168.225.59...
      Lease of 192.168.225.59 obtained, lease time 43200
      4G network started successfully!
      Current usb0 interface information:
      usb0      Link encap:Ethernet  HWaddr 3A:87:28:7B:48:CE
      inet addr:192.168.225.59  Bcast:192.168.225.255  Mask:255.255.255.0
      UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
      RX packets:2 errors:0 dropped:0 overruns:0 frame:0
      TX packets:2 errors:0 dropped:0 overruns:0 carrier:0
      collisions:0 txqueuelen:1000
      RX bytes:674 (674.0 B)  TX bytes:656 (656.0 B)
      Start parsing the IP of www.baidu.com (up to 3 retries)...
      1st attempt (ping) parsing www.baidu.com...
      2nd try (ping) parsing www.baidu.com...
      3rd try (ping) parsing www.baidu.com...
      ping parsing failed, attempting to parse with nslookup...
      Parsing successful (nslookup): www.baidu.com IP is 183.2.172.177
      routing information

   At this time, if the above information can be known that the IP of www.baidu.com is 183.2.172.177, enter the following command to ping Baidu

   .. code-block:: text

      ping 183.2.172.177

   The output information is as follows, 0% packet loss means normal

   .. code-block:: text

      /customer# ping 183.2.172.177
      PING 183.2.172.177 (183.2.172.177): 56 data bytes
      64 bytes from 183.2.172.177: seq=0 ttl=52 time=37.138 ms
      64 bytes from 183.2.172.177: seq=1 ttl=52 time=71.735 ms
      64 bytes from 183.2.172.177: seq=2 ttl=52 time=76.311 ms
      64 bytes from 183.2.172.177: seq=3 ttl=52 time=69.584 ms
      64 bytes from 183.2.172.177: seq=4 ttl=52 time=65.987 ms
      64 bytes from 183.2.172.177: seq=5 ttl=52 time=61.267 ms
      ^C
      --- 183.2.172.177 ping statistics ---
      6 packets transmitted, 6 packets received, 0% packet loss

Bluetooth Test
--------------

[Test Description]: Connect the 2.4G antenna to the U23 Bluetooth WiFi module interface, and Development Board sends a ICMP message to the external network to verify that the connection is normal.

[Interface identification]: U23

[System equipment]: hci0

[Test Procedure]

#. Turn on Bluetooth by entering the following command

   .. code-block:: text

      hciconfig hci0 up

   The output information is as follows

   .. code-block:: text

      rtk_btusb: btusb_open hdev->promisc ==0

#. Enter the following command to scan your Bluetooth device to turn on Bluetooth on your phone

   .. code-block:: text

      hcitool scan

   The output information is as follows

   .. code-block:: text

      Scanning ...
      DC:0D:30:5C:4C:93        n/a
      A8:13:06:20:06:54        iQOO Neo5
      A8:E5:44:99:28:F8        n/a

#. My phone Bluetooth is A 8:13:06: 20:06:54 iQOO Neo5, so enter the following command to connect to Bluetooth

   .. code-block:: text

      Python
      l2ping A8:13:06:20:06:54
      The output information is as follows, 0% loss means passing
      /# l2ping A8:13:06:20:06:54
      Ping: A8:13:06:20:06:54 from 94:BA:06:78:1C:E7 (data size 44) ...
      44 bytes from A8:13:06:20:06:54 id 0 time 5.01ms
      44 bytes from A8:13:06:20:06:54 id 1 time 88.41ms
      ^C2 sent, 2 received, 0% loss

MIPI Test
---------

Connect the adapter board and cable, the power display logo is normal

Camera Test
-----------

[Test Description]: Connect the mipi screen and the camera module to verify that the camera is normal.

[Interface identification]: U19

[Test Procedure]:

#. Turn on the camera by entering the following command

   .. code-block:: shell

      cd customer
      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/customer/3rd_party_libs/ffmpeg/lib
      ./prog_disp_sensor2Panel_demo -c 1 -n 0 -p 1 -t 0 -r 90 -d 1 -m model/yolov8n_800x480_P3P_fixed.sim_sgsimg.img -f font/default.ttf

#. the mipi screen shows that the camera screen is normal

Touch Test
----------

[Test Description]: Touch the mipi screen to verify that the touch function is normal.

[Interface identification]: CON5 DSI

[System equipment]: dev /input/event5

[Test Procedure]:

#. Connect the mipi screen to the Development Board and run the following command to open the touch event

   .. code-block:: text

      cd /customer
      ./my-evtest5

#. Touching the screen after running will display the coordinate information as follows

   .. code-block:: text

      /customer# ./my-evtest5=== My EVTest - Touch Screen Debug Tool ===
      Input device ID: bus 0x0018 vendor 0x0000 product 0x0000 version 0x0000
      Input device name: "sitronix_ts_i2c"
      Selected device: /dev/input/event5
      Testing ... (interrupt to exit)
      Event: time 49.628822, type 3 (EV_ABS), code 57 (ABS_MT_TRACKING_ID), value 0
      Event: time 49.629267, type 3 (EV_ABS), code 53 (ABS_MT_POSITION_X), value 132 (X=132)
      Event: time 49.629292, type 3 (EV_ABS), code 54 (ABS_MT_POSITION_Y), value 451 (Y=451)
      Event: time 49.629315, type 3 (EV_ABS), code 48 (UNKNOWN), value 1
      Event: time 49.629336, type 3 (EV_ABS), code 58 (UNKNOWN), value 255
      Event: time 49.629363, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 1 (PRESS)
      Event: time 49.629386, type 0 (EV_SYN), code 0 (UNKNOWN), value 0
      Event: time 49.687312, type 3 (EV_ABS), code 53 (ABS_MT_POSITION_X), value 134 (X=134)
      Event: time 49.687353, type 0 (EV_SYN), code 0 (UNKNOWN), value 0