MYZR-LS1012A-EK200 Linux-4.4.98 Test Manual
=============================================

Test Environment
------------------

|   【Development Board Model】: MYZR-LS1012A-EK200
|   【Kernel Version】: Linux-4.4.98
|   【File System】: rootfs.tar.gz
|   【Tool Version】: CW_ARMv8_v2019.01_b190130_Win_Offline
|   Note: To ensure accurate testing, the version of the programming tool used must be no less than 2019.01

Interface Identification Diagram
----------------------------------

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/1275px-LS1012A-interface.jpg
   :alt: 1275px-LS1012A-interface.jpg

Ethernet Port Test (ETH1)
---------------------------

|   【Test Description】: The test is conducted by having the development board send ICMP packets to the PC.
|   【Interface Identification】: ETH1
|   【Interface Silkscreen】: U2
|   【System Interface】: eth0

**Test Operations**

|   Configure the PC's wired network card IP to 192.168.137.99.
|   Connect the ETH1 port of the development board to the PC using a network cable.
|   Configure the development board's Ethernet port:

.. code-block:: shell

    =====> Enter command:
    ifconfig eth1 down 
    ifconfig eth0 192.168.137.81

|   Test ETH1 (eth0):

.. code-block:: shell

    =====> Enter command:
    ping 192.168.137.99 -c 2 -w 4 

    =====> Output information:
    PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
    64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.685 ms
    64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.374 ms 
    
    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 999ms
    rtt min/avg/max/mdev = 0.374/0.529/0.685/0.157 ms

**Test Result**

|   "0% packet loss" indicates the test is passed.

---

Ethernet Port Test (ETH2)
---------------------------

|   【Test Description】: The test is conducted by having the development board send ICMP packets to the PC.
|   【Interface Identification】: ETH2
|   【Interface Silkscreen】: U1
|   【System Interface】: eth1

**Test Operations**

|   Configure the PC's wired network card IP to 192.168.137.99.
|   Connect the ETH2 port of the development board to the PC using a network cable.
|   Configure the development board's Ethernet port:

.. code-block:: shell

    =====> Enter command:
    ifconfig eth0 down
    ifconfig eth1 192.168.137.82 

|   Test ETH2 (eth1):

.. code-block:: shell

    =====> Enter command:
    ping 192.168.137.99 -c 2 -w 4 

    =====> Output information:
    PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
    64 bytes from 192.168.137.99: icmp_seq=1 ttl=64 time=0.705 ms
    64 bytes from 192.168.137.99: icmp_seq=2 ttl=64 time=0.386 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 999ms
    rtt min/avg/max/mdev = 0.386/0.545/0.705/0.161 ms

**Test Result**

|   "0% packet loss" indicates the test is passed.

vsftpd Test
-------------

|   【Test Description】: File transfer between the development board and the PC.
|   【Interface Identification】: None
|   【Interface Silkscreen】: None
|   【System Interface】: None

**Test Operations**

|   Connect the PC to Ethernet Port 1 of the development board using a network cable.
|   Configure the PC's wired network card IP to 192.168.137.99.
|   Open "My Computer" and enter: ftp://192.168.137.81

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/Ls1012a-vsftpd.png
   :alt: Ls1012a-vsftpd.png

|   A login interface will pop up. Enter "root" as the username and leave the password blank.

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/Ls1012a-vsftpd2.png
   :alt: Ls1012a-vsftpd2.png

|   After logging in, you will enter the /home/root/ directory of the development board, where you can perform file transfer operations.

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/Ls1012a-vsftpd3.png
   :alt: Ls1012a-vsftpd3.png


USB Test
----------

|   【Test Description】: The test is conducted by plugging and unplugging a USB storage device (USB flash drive).
|   【Interface Identification】: USB3.0/USB2.0
|   【Interface Silkscreen】: J10

**Test Method**

|   Insert the USB device into the USB interface of the base board.

.. code-block:: shell

    =====> Enter command:
    df  

    =====> Output information: 
    Filesystem     1K-blocks    Used Available Use% Mounted on  
    /dev/root        3691872  119072   3381928   4% /  
    devtmpfs          197896       4    197892   1% /dev  
    tmpfs             206364     216    206148   1% /run  
    tmpfs             206364     136    206228   1% /var/volatile  
    /dev/sda1       30450128 5837584  24612544  20% /run/media/sda1  

|   Unplug the USB device from the base board.

.. code-block:: shell

    =====> Enter command:
    df  

    =====> Output information: 
    Filesystem     1K-blocks    Used Available Use% Mounted on  
    /dev/root        3691872  119072   3381928   4% /  
    devtmpfs          197896       4    197892   1% /dev  
    tmpfs             206364     216    206148   1% /run  
    tmpfs             206364     136    206228   1% /var/volatile  

**Test Result**

|   The sda1 device should be visible when the USB storage device is inserted.

---

SD Interface Test
--------------------

|   【Test Description】: The test is conducted by plugging and unplugging an SD card.
|   【Interface Identification】: SD_CARD
|   【Interface Silkscreen】: J9

**Test Method**

|   Insert the SD card into the SD interface.

.. code-block:: shell

    =====> Enter command:
    df  

    =====> Output information: 
    Filesystem     1K-blocks   Used Available Use% Mounted on
    /dev/root        3691872 119320   3381680   4% /
    devtmpfs          197896      4    197892   1% /dev
    tmpfs             206364    216    206148   1% /run
    tmpfs             206364    128    206236   1% /var/volatile
    /dev/mmcblk1p1    511384 258580    252804  51% /run/media/mmcblk1p1

|   Unplug the SD card from the base board.

.. code-block:: shell

    =====> Enter command:
    df  

    =====> Output information: 
    Filesystem     1K-blocks    Used Available Use% Mounted on  
    /dev/root        3691872  119072   3381928   4% /  
    devtmpfs          197896       4    197892   1% /dev  
    tmpfs             206364     216    206148   1% /run  
    tmpfs             206364     136    206228   1% /var/volatile  

**Test Result**

|   The sda1 device should be visible when the SD card is inserted.


RS232 Test (RS232_3)
----------------------

|   【Test Description】: The test is conducted using a self-transmit and self-receive method.
|   【Interface Identification】: RS232/RS485
|   【Interface Location】: J1
|   【System Device】: /dev/TtyXRUSB2

**Test Operations**

|   Short-circuit the transmit and receive pins of RS232_3 (the 5th/6th interfaces from the left in the lower row of J1).
|   (The lower row of J1 from left to right is: RS2232_TX1, RS232_RX1, RS232_TX2, RS232_RX2, RS232_TX3, RS232_RX3, empty pin, empty pin.
|   The corresponding system devices are: ttyXRUSB0, ttyXRUSB1, ttyXRUSB2 in sequence.)
|   Execute the test command:

.. code-block:: shell

    =====> Enter command:
    /my-demo/uart_test.out /dev/ttyXRUSB2 "www.myzr.com.cn"  

    =====> Output information:
    Starting send data...finish
    Starting receive data:
    ASCII: 0x77      Character: w 
    ASCII: 0x77      Character: w 
    ASCII: 0x77      Character: w 
    ASCII: 0x2e      Character: . 
    ASCII: 0x6d      Character: m 
    ASCII: 0x79      Character: y 
    ASCII: 0x7a      Character: z 
    ASCII: 0x72      Character: r 
    ASCII: 0x2e      Character: . 
    ASCII: 0x63      Character: c 
    ASCII: 0x6f      Character: o 
    ASCII: 0x6d      Character: m 
    ASCII: 0x2e      Character: . 
    ASCII: 0x63      Character: c 
    ASCII: 0x6e      Character: n 
    ASCII: 0x0       Character:   

**Test Result**

|   After executing the test command, the application is normal if it outputs information similar to the above.


RS485 Test (RS485_1)
----------------------

|   【Test Description】: The test is conducted using a differential method.
|   【Interface Identification】: RS232/RS485
|   【Interface Location】: J1
|   【System Device】: /dev/TtyXRUSB3

**Test Operations**

|   Log in to the development board using Telnet.
|   Connect the 485-232 adapter to the transmit and receive pins of RS485_1 on the development board (the 1st/2nd interfaces in the upper row of J1). Connect the positive terminal of the adapter to A and the negative terminal to B.
|   (The upper row of J1 from left to right is: RS485_A1, RS485_B1, RS485_A2, RS485_B2, RS485_A3, RS485_B3, empty pin, empty pin.
|   The corresponding system devices are: ttyXRUSB3, ttyXRUSB4, ttyXRUSB5 in sequence.)
|   Connect the other end of the adapter to the PC's USB-to-serial cable.
|   Set the serial terminal baud rate to 9600.
|   Execute the test command:

.. code-block:: shell

    =====> Enter command:
    echo "myzr" > /dev/ttyXRUSB3

    =====> Serial port output information:
    myzr
    =====> Enter command:
    cat /dev/ttyXRUSB3

    =====> Serial port input:
    myzr

    =====> Development board output information:
    myzr

**Test Result**

|   After executing the test command, the application is normal if it outputs information similar to the above.


GPIO Input Test
-----------------

|   【Test Description】: Using the key interrupt method.
|   【Interface Identification】: DI
|   【Interface Location】: J2
|   【System Device】: /sys/class/gpio/

**Test Operations**

|   The GPIOs corresponding to the DI interface are:
|   gpio440 ----> I2C_3_GPIO1_0_IN (J2 lower row 1, 2)
|   gpio441 ----> I2C_3_GPIO1_1_IN (J2 upper row 1, 2)
|   gpio442 ----> I2C_3_GPIO1_2_IN (J2 lower row 3, 4)
|   gpio443 ----> I2C_3_GPIO1_3_IN (J2 upper row 3, 4)
|   gpio444 ----> I2C_3_GPIO1_4_IN (J2 lower row 5, 6)
|   gpio445 ----> I2C_3_GPIO1_5_IN (J2 upper row 5, 6)
|   gpio446 ----> I2C_3_GPIO1_6_IN (J2 lower row 7, 8)
|   gpio447 ----> I2C_3_GPIO1_7_IN (J2 upper row 7, 8)

|   Use the J2 interface of the GPIO test board to connect to the upper or lower row of the DI interface on the development board.
|   Connect a 5V power supply to the test board.
|   Execute the test command:

.. code-block:: shell

    =====> Enter command:
    chmod +x /home/root/gpio-in.sh  
    /home/root/gpio-in.sh  

    =====> Output information:
    gpio440
    gpio441
    gpio442
    gpio443
    gpio444
    gpio445
    gpio446
    gpio447

|   Check the number of GPIO key interrupts:

.. code-block:: shell

    =====> Enter command:
    cat /proc/interrupts | grep gpio  

    =====> Output information:
     25:          0  mpc8xxx-gpio  22 Edge      0-0026
     29:          0   pca953x   8 Edge      gpiolib
     30:          0   pca953x   9 Edge      gpiolib
     31:          


GPIO Input Test
------------------

|   【Test Description】: Adopt key interrupt mode
|   【Interface Identification】: DI
|   【Interface Location】: J2
|   【System Device】: /sys/class/gpio/

**Test Operation**

|   The GPIOs corresponding to the DI interface are:
|   gpio440 ----> I2C_3_GPIO1_0_IN J2 Lower 1,2
|   gpio441 ----> I2C_3_GPIO1_1_IN J2 Upper 1,2
|   gpio442 ----> I2C_3_GPIO1_2_IN J2 Lower 3,4
|   gpio443 ----> I2C_3_GPIO1_3_IN J2 Upper 3,4
|   gpio444 ----> I2C_3_GPIO1_4_IN J2 Lower 5,6
|   gpio445 ----> I2C_3_GPIO1_5_IN J2 Upper 5,6
|   gpio446 ----> I2C_3_GPIO1_6_IN J2 Lower 7,8
|   gpio447 ----> I2C_3_GPIO1_7_IN J2 Upper 7,8

|   Use the J2 interface of the GPIO test board to connect to the upper row or lower row of the DI on the development board.
|   Connect a 5V power supply to the test board.
|   Execute the test command:

.. code-block:: shell

    =====> Input Command:
    chmod +x /home/root/gpio-in.sh  
    /home/root/gpio-in.sh  

    =====> Output Information:
    gpio440
    gpio441
    gpio442
    gpio443
    gpio444
    gpio445
    gpio446
    gpio447

|   Check the number of GPIO key interrupts:

.. code-block:: shell

    =====> Input Command:
    cat /proc/interrupts | grep gpio  

    =====> Output Information:
     25:          0  mpc8xxx-gpio  22 Edge      0-0026
     29:          0   pca953x   8 Edge      gpiolib
     30:          0   pca953x   9 Edge      gpiolib
     31:          0   pca953x  10 Edge      gpiolib
     32:          0   pca953x  11 Edge      gpiolib
     33:          0   pca953x  12 Edge      gpiolib
     34:          0   pca953x  13 Edge      gpiolib
     35:          0   pca953x  14 Edge      gpiolib
     36:          0   pca953x  15 Edge      gpiolib

|   Press the keys corresponding to the GPIOs on the test board several times, and check the interrupt count repeatedly:

.. code-block:: shell

    =====> Input Command:
    cat /proc/interrupts | grep gpio  

    =====> Output Information:
     25:         20  mpc8xxx-gpio  22 Edge      0-0026
     29:          2   pca953x   8 Edge      gpiolib
     30:          0   pca953x   9 Edge      gpiolib
     31:          4   pca953x  10 Edge      gpiolib
     32:          0   pca953x  11 Edge      gpiolib
     33:          2   pca953x  12 Edge      gpiolib
     34:          0   pca953x  13 Edge      gpiolib
     35:          2   pca953x  14 Edge      gpiolib
     36:          0   pca953x  15 Edge      gpiolib

**Test Result**

|   After executing the test operation, if the application outputs information similar to the above, it is normal.


GPIO Output Test
-------------------

|   【Test Description】: Control GPIO output level
|   【Interface Identification】: DO
|   【Interface Location】: J3
|   【System Device】: /sys/class/gpio/

**Test Operation**

|   The GPIOs corresponding to the DO interface are:
|   gpio432 ----> I2C_3_GPIO0_0_OUT J3 Lower 1,2
|   gpio433 ----> I2C_3_GPIO0_1_OUT J3 Upper 1,2
|   gpio434 ----> I2C_3_GPIO0_2_OUT J3 Lower 3,4
|   gpio435 ----> I2C_3_GPIO0_3_OUT J3 Upper 3,4
|   gpio436 ----> I2C_3_GPIO0_4_OUT J3 Lower 5,6
|   gpio437 ----> I2C_3_GPIO0_5_OUT J3 Upper 5,6
|   gpio438 ----> I2C_3_GPIO0_6_OUT J3 Lower 7,8
|   gpio439 ----> I2C_3_GPIO0_7_OUT J3 Upper 7,8

|   Use the J3 interface of the GPIO test board to connect to the upper row or lower row of the DO on the development board.
|   Connect a 5V power supply to the test board.
|   Execute the test command:

.. code-block:: shell

    =====> Input Command:
    chmod +x /home/root/gpio-out.sh  
    /home/root/gpio-out.sh  

    =====> Output Information:
    goio432
    goio433
    goio434
    goio435
    goio436
    goio437
    goio438
    goio439
    Please add the parameter 1 or 0

|   Control output high level:

.. code-block:: shell

    =====> Input Command:
    /home/root/gpio-out.sh 1    

|   Control output low level:

.. code-block:: shell

    =====> Input Command:
    /home/root/gpio-out.sh 0

**Test Result**

|   When outputting high level, the corresponding four LED lights turn on;
|   When outputting low level, the corresponding four LED lights turn off.


WIFI Module RTL8723du Test
----------------------------

|   【Test Description】: After the WIFI is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal.
|   【Interface Identification】: WIFI&BT, WIFI_ANT
|   【Interface Silkscreen】: U24, E1
|   【System Device】: wlan0

**Test Operation**

1. Confirm that the WIFI module is attached at the "WIFI" mark; otherwise, no test is required.
2. Connect the WIFI antenna to the interface marked "WIFI_ANT".
3. Generate the WPA PSK file for the SSID

|   Command Format: wpa_passphrase <ssid> [passphrase]

.. code-block:: shell

    =====> Input Command:
    wpa_passphrase MY-TEST-AP myzr2012 > /etc/wpa_supplicant.conf
    pkill wpa_supplicant

4. Connect

.. code-block:: shell

    =====> Input Command:
    wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

    =====> Output Information:
    Successfully initialized wpa_supplicant
    rfkill: Cannot open RFKILL control device
    ioctl[SIOCSIWAP]: Operation not permitted

5. Obtain IP

.. code-block:: shell

    =====> Input Command:
    udhcpc -i wlan0

    =====> Output Information:
    udhcpc (v1.23.2) started
    Sending discover...
    Sending select for 192.168.43.99...
    Lease of 192.168.43.99 obtained, lease time 3600
    /etc/udhcpc.d/50default: Adding DNS 192.168.43.1

6. Test Connection

.. code-block:: shell

    =====> Input Command:
    ping -I wlan0 www.baidu.com -c 2 -w 4

    =====> Output Information:
    PING www.baidu.com (14.215.177.38): 56 data bytes
    64 bytes from 14.215.177.38: seq=0 ttl=49 time=15.753 ms
    64 bytes from 14.215.177.38: seq=1 ttl=49 time=11.835 ms

    --- www.baidu.com ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 11.835/13.794/15.753 ms

**Test Result**

|   "0% packet loss" indicates that the WIFI connection is normal.


Bluetooth Test
----------------

|   【Test Description】: After Bluetooth connection, the development board sends information to the mobile phone to verify that the connection is normal.
|   【Interface Identification】: WIFI, WIFI_ANT
|   【Interface Silkscreen】: U24, E1
|   【System Device】: hci0

**Test Operation**

1. Confirm that the WIFI module is attached at the "WIFI" mark; otherwise, no test is required.
2. Connect the WIFI antenna to the interface marked "WIFI_ANT".
3. Check hci0

.. code-block:: shell

    =====> Input Command:
    hciconfig -a

    =====> Output Information:
    hci0:   Type: BR/EDR  Bus: USB
        BD Address: 74:EE:2A:46:E8:83  ACL MTU: 1021:8  SCO MTU: 255:12
        DOWN 
        RX bytes:590 acl:0 sco:0 events:31 errors:0
        TX bytes:372 acl:0 sco:0 commands:31 errors:0
        Features: 0xff 0xff 0xff 0xfe 0xdb 0xfd 0x7b 0x87
        Packet type: DM1 DM3 DM5 DH1 DH3 DH5 HV1 HV2 HV3 
        Link policy: RSWITCH HOLD SNIFF PARK 
        Link mode: SLAVE ACCEPT 

4. Start hci0

.. code-block:: shell

    =====> Input Command:
    hciconfig hci0 up

    =====> Output Information:
    [  283.065459] rtk_btusb: btusb_open hdev->promisc ==0

5. Scan Bluetooth

.. code-block:: shell

    =====> Input Command:
    hcitool scan

    =====> Output Information:
    Scanning ...
        A4:50:46:9E:11:86   Xiaomi Mobile Phone

6. Test Connection

.. code-block:: shell

    =====> Input Command:
    l2ping A4:50:46:9E:11:86

    =====> Output Information:
    Ping: A4:50:46:9E:11:86 from 74:EE:2A:46:E8:83 (data size 44) ...
    44 bytes from A4:50:46:9E:11:86 id 0 time 5022.50ms
    44 bytes from A4:50:46:9E:11:86 id 1 time 57.15ms
    44 bytes from A4:50:46:9E:11:86 id 2 time 26.12ms

**Test Result**

|   "0% packet loss" indicates that the Bluetooth connection is normal.


4G Module EC20 Test
---------------------

|   【Test Description】: After the 4G connection is successful, the development board sends ICMP packets to the external network to verify that the connection is normal.
|   【Interface Identification】: 3G/4G
|   【Interface Silkscreen】: J5
|   【System Device】: eth2

**Test Operation**

1. Power off the development board, connect the 4G module, connect the antenna and insert the SIM card, then start the evaluation board.
2. Use the command to establish a network connection:

.. code-block:: shell

    =====> Input Command:
    /my-demo/quectel-CM &

    =====> Output Information:
    [1] 607
    [09-21_13:36:14:352] WCDMA&LTE_QConnectManager_Linux&Android_V1.1.34
    [09-21_13:36:14:353] /my-demo/gcc-linaro-5.3-arm/quectel-CM.out profile[1] = (null)/(null)/(null)/0, pincode = (null)
    [09-21_13:36:14:356] Find /sys/bus/usb/devices/1-1.2 idVendor=2c7c idProduct=0125
    [09-21_13:36:14:356] Find /sys/bus/usb/devices/1-1.2:1.4/net/eth2
    [09-21_13:36:14:356] Find usbnet_adapter = eth2
    [09-21_13:36:14:356] Find /sys/bus/usb/devices/1-1.2:1.4/GobiQMI/qcqmi2
    [09-21_13:36:14:357] Find qmichannel = /dev/qcqmi2
    [09-21_13:36:14:403] Get clientWDS = 7
    [09-21_13:36:14:435] Get clientDMS = 8
    [09-21_13:36:14:467] Get clientNAS = 9
    [09-21_13:36:14:499] Get clientUIM = 10
    [09-21_13:36:14:532] Get clientWDA = 11
    [09-21_13:36:14:563] requestBaseBandVersion EC20CEFAR02A10M4G
    [09-21_13:36:14:659] requestGetSIMStatus SIMStatus: SIM_READY
    [09-21_13:36:14:692] requestGetProfile[1] cmnet///0
    [09-21_13:36:14:724] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
    [09-21_13:36:14:755] requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
    [09-21_13:36:14:819] requestRegistrationState2 MCC: 460, MNC: 0, PS: Attached, DataCap: LTE
    [09-21_13:36:16:036] requestSetupDataCall WdsConnectionIPv4Handle: 0x87756f40
    [09-21_13:36:16:132] requestQueryDataCall IPv4ConnectionStatus: CONNECTED
    [09-21_13:36:16:163] ifconfig eth2 up
    [09-21_13:36:16:193] busybox udhcpc -f -n -q -t 5 -i eth2
    [09-21_13:36:16:211] udhcpc (v1.24.1) started
    [09-21_13:36:16:318] Sending discover...
    [09-21_13:36:16:378] Sending select for 10.151.159.101...
    [09-21_13:36:16:438] Lease of 10.151.159.101 obtained, lease time 7200
    [09-21_13:36:16:522] /etc/udhcpc.d/50default: Adding DNS 221.179.38.7
    [09-21_13:36:16:522] /etc/udhcpc.d/50default: Adding DNS 120.196.165.7


3. Test Connection

.. code-block:: shell

    =====> Input Command:
    ifconfig eth0 down
    ping -I eth2 www.baidu.com -c 2 -w 4

    =====> Output Information:
    PING www.baidu.com (14.215.177.38): 56 data bytes
    64 bytes from 14.215.177.38: seq=0 ttl=49 time=15.753 ms
    64 bytes from 14.215.177.38: seq=1 ttl=49 time=11.835 ms

    --- www.baidu.com ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 11.835/13.794/15.753 ms

**Test Result**

|   "0% packet loss" indicates a normal connection.