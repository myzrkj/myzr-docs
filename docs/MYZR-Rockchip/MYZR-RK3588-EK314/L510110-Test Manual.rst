Test Manual
=============

RTC
------

- Device Interface: /dev/rtc

- Test Description: A button battery is required for RTC testing, and the battery is located at the silk screen **BT1**.

**Functional Test**

- **RTC Time**

  1) Description: Set the RTC time, then power off and restart the device, and check the RTC time again.

  2) Operations

    a) Set the RTC time. The specific operations are as follows:

    - Enter the command to update the system time:

    .. code-block:: shell

       date -s "2023-02-06 12:34:56"

    - You can see that the current system time is updated to the set time:

    .. code-block:: text

      Mon Feb  6 12:34:56 UTC 2023

    - Enter the command to set the system time to RTC:

    .. code-block:: shell

      hwclock -w 

    b) Power off and restart the device.

    c) Check the RTC time. The specific operations are as follows:

    - Enter the command:

    .. code-block:: shell

       hwclock 

    - You can see that the time stored in RTC is basically the same as the time we set, similar to the following:

    .. code-block:: text

      2023-02-06 12:35:34.485664+00:00

  3) Result: After performing the operations, if the checked RTC time is basically correct and the output during the operation meets the expectations, the function is normal.


Ethernet Port
---------------

  - Interface Silk Screen: J14 (ETH1), J15 (ETH2)
  - System Interface: eth0 (ETH1), enP3p49s0 (ETH2)

**Functional Test**

- **Ethernet Port 1**

  1) Description: Test by sending ICMP packets from the development board to the PC.

  2) Operations

    a) Configure the IP address of the PC's wired network card to 192.168.137.99.

    b) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

    c) Configure the IP address of the development board's Ethernet port. The specific configuration commands are as follows:

    .. code-block:: shell

      ifconfig enP3p49s0 down
      ifconfig eth0 up
      ifconfig eth0 192.168.137.81

    d) Execute the Ethernet port test command

    - Enter the command:

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4

    - Output information:

    .. code-block:: text

      PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
      64 bytes from 192.168.137.99: icmp_seq-1 ttl-64 time-1.35 ms
      64 bytes from 192.168.137.99: icmp_seq-2 ttl-64 time-1.35 ms

      --- 192.168.137.99 ping statistics ---
      2 packets transmitted, 2 received, 0% packet loss, time 1002ms
      rtt min/avg/max/mdev - 1.347/1.347/1.348/0.000 ms

  3) Result: "0% packet loss" indicates that the test is passed.

- **Ethernet Port 2**

  1) Description: Test by sending ICMP packets from the development board to the PC.

  2) Operations

    a) Configure the IP address of the PC's wired network card to 192.168.137.99.

    b) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

    c) Configure the IP address of the development board's Ethernet port. The specific configuration commands are as follows:

    .. code-block:: shell

      ifconfig eth0 down
      ifconfig enP3p49s0 up
      ifconfig enP3p49s0 192.168.137.82

    d) Execute the Ethernet port test command

    - Enter the command:

    .. code-block:: shell

      ping 192.168.137.99 -c 2 -w 4

    - Output information:

    .. code-block:: text

      PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data.
      64 bytes from 192.168.137.99: icmp_seq-1 ttl-64 time-0.595 ms
      64 bytes from 192.168.137.99: icmp_seq-2 ttl-64 time-0.843 ms

      --- 192.168.137.99 ping statistics ---
      2 packets transmitted, 2 received, 0% packet loss, time 1001ms
      rtt min/avg/max/mdev - 0.595/0.719/0.843/0.124 ms

  3) Result: "0% packet loss" indicates that the test is passed.


Audio
--------

- Interface Silk Screen: P15

**Functional Test**

  1) Description: Test by playing an audio file.

  2) Operations

    a) Insert headphones or a speaker into the interface corresponding to the silk screen **P15**.

    b) Enter the command to perform the test:

    .. code-block:: shell

      aplay /mytest.wav

  3) Result: When the test command is executed, if sound can be heard from the headphones, the function is normal.


Audio Recording
------------------

- Interface Silk Screen: P15

**Functional Test**

  1) Description: Test by recording and playing the recorded audio file.

  2) Operations

    a) Insert headphones or a speaker into the interface corresponding to the silk screen **P15**.

    b) Enter the commands to perform the test:

    .. code-block:: shell

      arecord -d 5 -f S16_LE record.wav
      aplay record.wav

  3) Result: When the test commands are executed, if the recorded sound can be heard from the headphones, the function is normal.


USB 2.0
----------

- Interface Silk Screen: P2, P3

**Functional Test**

  1) Description: Test by plugging and unplugging a USB storage device (USB flash drive).

  2) Operations:

    a) Insert the USB device into the USB interface of the baseboard. The system will output information similar to the following:

    .. code-block:: text

      [   27.275918] usb 1-1.3: new high-speed USB device number 4 using ehci-platform
      [   27.378130] usb 1-1.3: New USB device found, idVendor=3535, idProduct=5678, bcdDevice= 2.00
      [   27.378205] usb 1-1.3: New USB device strings: Mfr=1, Product=2, SerialNumber=3
      [   27.378229] usb 1-1.3: Product: U330
      [   27.378250] usb 1-1.3: Manufacturer: aigo
      [   27.378271] usb 1-1.3: SerialNumber: FC003F045D904
      [   27.379869] usb-storage 1-1.3:1.0: USB Mass Storage device detected
      [   27.380603] scsi host1: usb-storage 1-1.3:1.0
      [   28.308636] GobiNet::QMIWDASetDataFormat qmap settings qmap_version=9, rx_size=31744, tx_size=4096
      [   28.308713] GobiNet::QMIWDASetDataFormat qmap settings ul_data_aggregation_max_size=4096, ul_data_aggregation_max_datagrams=11
      [   28.394213] scsi 1:0:0:0: Direct-Access     aigo     U330             2.00 PQ: 0 ANSI: 4
      [   28.397070] sd 1:0:0:0: [sda] 61440000 512-byte logical blocks: (31.5 GB/29.3 GiB)
      [   28.397742] sd 1:0:0:0: [sda] Write Protect is off
      [   28.398481] sd 1:0:0:0: [sda] No Caching mode page found
      [   28.398494] sd 1:0:0:0: [sda] Assuming drive cache: write through
      [   28.429520]  sda: sda1
      [   28.435849] sd 1:0:0:0: [sda] Attached SCSI removable disk
      [   28.608386] FAT-fs (sda1): utf8 is not a recommended IO charset for FAT filesystems, filesystem will be case sensitive!
      [   28.612929] FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

    b) Unplug the USB device from the baseboard. The system will output information similar to the following:

    .. code-block:: text

      [   76.699501] usb 1-1.3: USB disconnect, device number 4


USB 3.0
----------

- Interface Silk Screen: J3

**Functional Test**

  1) Description: Test by plugging and unplugging a USB storage device (USB flash drive).

  2) Operations:

    a) Insert the USB device into the USB interface of the baseboard. The system will output information similar to the following:

    .. code-block:: text

      [  105.772698] usb 8-1: new SuperSpeed Gen 1 USB device number 2 using xhci-hcd
      [  105.793382] usb 8-1: LPM exit latency is zeroed, disabling LPM.
      [  105.794348] usb 8-1: New USB device found, idVendor=3535, idProduct=5678, bcdDevice= 2.00
      [  105.794383] usb 8-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3
      [  105.794447] usb 8-1: Product: U330
      [  105.794469] usb 8-1: Manufacturer: aigo
      [  105.794491] usb 8-1: SerialNumber: FC003F045D904
      [  105.796915] usb-storage 8-1:1.0: USB Mass Storage device detected
      [  105.797741] scsi host1: usb-storage 8-1:1.0
      [  106.820335] scsi 1:0:0:0: Direct-Access     aigo     U330             2.00 PQ: 0 ANSI: 4
      [  106.822236] sd 1:0:0:0: [sda] 61440000 512-byte logical blocks: (31.5 GB/29.3 GiB)
      [  106.822937] sd 1:0:0:0: [sda] Write Protect is off
      [  106.823212] sd 1:0:0:0: [sda] No Caching mode page found
      [  106.823234] sd 1:0:0:0: [sda] Assuming drive cache: write through
      [  106.859545]  sda: sda1
      [  106.862227] sd 1:0:0:0: [sda] Attached SCSI removable disk
      [  106.973622] FAT-fs (sda1): utf8 is not a recommended IO charset for FAT filesystems, filesystem will be case sensitive!
      [  106.977205] FAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

    b) Unplug the USB device from the baseboard. The system will output information similar to the following:

    .. code-block:: text

      [  110.135778] usb 8-1: USB disconnect, device number 2


TF Card
---------

- Interface Silk Screen: J5

**Functional Test**

  .. note:: The TF card interface of the device supports hot-swapping, and the TF card holder is a self-ejecting type.

- TF Card Insertion Test

  1) Description: Insert the TF card and check whether the device can recognize the card correctly.

  2) Operations

    a) Take a TF card and insert it into the TF card interface of the device.

    b) The output information is similar to the following:

    .. code-block:: text

      ...
      mmc1: new ultra high speed SDR104 SDHC card at address 0001
      mmcblk1: mmc1:0001 SD16G 14.9 GiB
      ...

  3) Result: If the output information after the operation meets the correct expectations, it indicates that the TF card is recognized correctly.

- TF Card Ejection Test

  1) Eject the TF card and check whether the device can respond correctly.

  2) Operations

    a) Press the TF card inward in the direction of insertion (release it when a "click" sound is heard, and the TF card will eject).

    b) The output information is similar to the following:

    .. code-block:: text

      ...
      mmc1: card 0001 removed
      ...

  3) Result: If the phenomenon during the operation meets the correct expectations, it indicates that the TF card hot-swapping function is normal.


Infrared (IR)
---------------

- Interface Silk Screen: IR1

**Functional Test**

1) Description: Receive infrared information and print the corresponding data.

  2) Operations

    a) Prepare an infrared remote control or an infrared remote control app on a mobile phone.

    b) Enable the relevant print switch on the development board:

    .. code-block:: text

      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/code_print
      echo 1 > /sys/module/rockchip_pwm_remotectl/parameters/dbg_level

    c) Point the remote control at the infrared interface and press any button.

    d) If the development board displays the corresponding button information in return, it indicates that the infrared signal is received successfully.


WiFi
------

- Interface Silk Screen: U27

**Functional Test**

  1) Description: After the WiFi is connected to the AP, the development board sends ICMP packets to the external network to verify that the connection is normal.

  2) Operations:

    a) Connect the WiFi antenna to the "ANT2/ANT1" interface.
    b) Generate the WPA PSK file for the SSID. Enter:

    .. code-block:: shell

      wpa_passphrase MYZR-WIFI myzr2012 > /etc/wpa_supplicant.conf

    c) Connect to WiFi:

    .. code-block:: shell

      wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf 

    d) Obtain an IP address:

    .. code-block:: shell

      udhcpc -i wlan0

    e) Test the connection:

    .. code-block:: shell

      ping -I wlan0 www.baidu.com


Bluetooth
-----------

+ Interface Silkscreen: U27

**Function Test**

  1) Description: After scanning for Bluetooth devices, send an L2CAP response request and receive the reply.

  2) Operations:
  
    a) Connect the antenna to the "ANT2/ANT3" interface
    b) Initialize and start Bluetooth:

    .. code-block:: shell
      
      hciconfig hci0 up

    c) Scan for external Bluetooth devices:

    .. code-block:: shell

       hcitool scan 

    Bluetooth address of my phone found:

    .. code-block:: shell

       88:46:04:4C:11:A7   Redmi K40

    d) Send an L2CAP packet for testing:

    .. code-block:: shell

      l2ping 88:46:04:4C:11:A7

    Successful connection display:

    .. code-block:: shell

      Ping: 88:46:04:4C:11:A7 from B0:F1:EC:A7:E8:03 (data size 44) ...
      44 bytes from 88:46:04:4C:11:A7 id 0 time 44.84ms
      44 bytes from 88:46:04:4C:11:A7 id 1 time 28.58ms
      44 bytes from 88:46:04:4C:11:A7 id 2 time 46.05ms
      44 bytes from 88:46:04:4C:11:A7 id 3 time 44.86ms
      44 bytes from 88:46:04:4C:11:A7 id 4 time 44.67ms
      44 bytes from 88:46:04:4C:11:A7 id 5 time 52.32ms
      44 bytes from 88:46:04:4C:11:A7 id 6 time 24.86ms
      44 bytes from 88:46:04:4C:11:A7 id 7 time 59.71ms
      ^C8 sent, 8 received, 0% loss


5G Module RM500Q
-------------------

+ Interface Silkscreen: J19

**Function Test**

  1) Connect the 5G module RM500Q, 5G antenna, and SIM card.

  2) Start the development board.
  
  3) Enter the following command to dial:

  .. code-block:: shell

    /quectel-CM &

  4) Test the connection status

  .. code-block:: shell

    ping -I rmnet_mhi0.1 www.baidu.com


M2 Hard Drive
----------------

+ Interface Silkscreen: J21

**Function Test**

  1) Connect the M2 hard drive.

  2) Start the development board.
  
  3) Enter the following command to view PCI bus devices:

  .. code-block:: shell

    lspci

    Output

  .. code-block:: shell

    21:00.0 Class 0108: 126f:2263
    20:00.0 Class 0604: 1d87:3588


  4) Mount the hard drive

  .. code-block:: shell

    mkdir /nvme
    mount /dev/nvme0n1p1 /nvme/

  5) Check the mounting status

  .. code-block:: shell

    df -h

  6) The following information should be displayed:

  .. code-block:: shell

    /dev/nvme0n1p1  120G  108M  120G   1% /nvme


SATA Hard Drive
------------------

+ Interface Silkscreen: J18, J2

**Function Test**

  1) Connect the SATA hard drive.

  2) Start the development board.
  
  3) Mount the hard drive

  .. code-block:: shell

    mkdir /sata
    mount /dev/sda1 /sata/

  5) Check the mounting status

  .. code-block:: shell

    df -h

  6) The following information should be displayed:

  .. code-block:: shell

    /dev/sda1       932G   16G  917G   2% /sata



Video Playback
----------------

**Function Test**

  1) Connect a display and start the development board.

  2) Click `test_gst_multivideo.sh` on the GUI desktop to view multiple videos playing simultaneously.

  3) Use the gst command to play a single video:

  .. code-block:: shell

    gst-launch-1.0 playbin uri=file:///oem/SampleVideo_1280x720_5mb.mp4 video-sink="waylandsink"



Full-Function TYPE-C
-----------------------

+ Interface Silkscreen: J4

**Function Test**

  1) TYPE-C interface as USB-Host: Connect a TYPE-C to USB-A adapter, then connect a USB 3.0 U disk. The U disk should be recognized and mounted automatically.

  2) TYPE-C interface as USB-Device: Connect the computer and J4 interface with a TYPE-C cable. After starting the development board, the ADB service should be activated.

  3) TYPE-C interface for DP display: Flash the DP-TYPE-C image, connect a display with a TYPE-C interface using a TYPE-C cable, and normal display should be achieved after startup.



Camera Module
----------------

+ Interface Silkscreen: P10

**Function Test**

  1) Connect the display and camera module, then start the development board.

  2) Click `camera_rkisp_test.sh` on the GUI desktop to view the real-time image captured by the camera.

  3) Use the gst command to view the real-time image captured by the camera:

.. code-block:: shell
  
  gst-launch-1.0 v4l2src device=/dev/video-camera0 ! video/x-raw,format=NV12,width=640,height=480,framerate=30/1 ! waylandsink


