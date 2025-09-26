Test Manual
=============

Test Overview
---------------

+----------------------+-------------+-----------------+-------------+-------------+-------------+
| Test Item            | Test Result | Test Item       | Test Result | Test Item   | Test Result |
+----------------------+-------------+-----------------+-------------+-------------+-------------+
| Power Indicator LED  | Pass        | TF Card         | Pass        | HDMI        | Pass        |
+----------------------+-------------+-----------------+-------------+-------------+-------------+
| Power Switch         | Pass        | Ethernet Port 1 | Pass        | USB Camera  | Pass        |
+----------------------+-------------+-----------------+-------------+-------------+-------------+
| Reset Button         | Pass        | Ethernet Port 2 | Pass        | M.2 SSD     | Pass        |
+----------------------+-------------+-----------------+-------------+-------------+-------------+
| System Indicator LED | Pass        | RTC             |             | M.2 WiFi    | Pass        |
+----------------------+-------------+-----------------+-------------+-------------+-------------+
| Memory Stress Test   | Pass        | Audio           |             | M.2 5G      | Pass        |
+----------------------+-------------+-----------------+-------------+-------------+-------------+
| USB 2.0              | Pass        |                 |             | MIPI Camera | Pass        |
+----------------------+-------------+-----------------+-------------+-------------+-------------+
| USB 3.0              | Pass        |                 |             |             |             |
+----------------------+-------------+-----------------+-------------+-------------+-------------+


Power Indicator LED
----------------------

* Interface Silkscreen: LD6

**Status Description**

* On: Indicates the main power supply of the development board is connected.
* Off: Indicates the main power supply of the development board is disconnected.

### Function Test
* Refer to the `Power Switch` section in this manual for testing.


Power Switch
--------------

* Interface Silkscreen: SW3

**Function Test**

* **Description**: The power switch can control the power on/off of the development board.

- **Power Off**

  1) Operation: When the device power is connected, toggle the power switch of the development board to **OFF**.

  2) Result: It is normal if the power indicator LED of the development board turns off.

  3) Note: It takes a few seconds for the power indicator LED of the development board to turn off completely, which is a normal phenomenon. This is because the capacitors on the development board store electricity after power-on, and the indicator LED will turn off completely once the capacitors discharge.

- **Power On**

  1) Operation: After the power is turned off as above, toggle the power switch of the development board to **ON**.

  2) Result: It is normal if the power indicator LED of the development board turns on.


Reset Button
--------------

- Interface Silkscreen: SW1

**Function Test**

* Description: A short press on the reset button can reset the device power.

* Operation: When the main board power is on, press and release the reset button briefly to reset the device power.

* Result: After pressing and releasing, you can see the development board restarting through the serial port, which indicates normal operation.


System Indicator LED
-----------------------

**Interface Silkscreen**

* Heartbeat Indicator LED: LD2
* User Indicator LED: LD1

**System Interface**

* Heartbeat Indicator LED: /sys/class/leds/heartbeat
* User Indicator LED: /sys/class/leds/user

**Function Test**

- **Heartbeat Indicator LED**

  1) Description: The heartbeat indicator LED is used to check if the system is running normally.

  2) Operation: None

  3) Result: After the system starts successfully, the heartbeat indicator LED will flash, indicating that the system is running normally and this function is working properly.

- **User Indicator LED**

  1) Description: The user indicator LED can usually be controlled by the user through the system interface.

  2) Operation: Control via the system interface, with the following control commands:

.. code-block:: shell

   # Turn off the LED
   echo 0 > /sys/class/leds/user/brightness
   # Turn on the LED
   echo 1 > /sys/class/leds/user/brightness

\

  3) Result: After executing the LED-off command, the user indicator LED turns off. After executing the LED-on command, the user indicator LED turns on.


Memory Stress Test
--------------------

* Interface Silkscreen: None

**Function Test**

* Description:

  1) A memory stress test tool is used for testing.

  2) The memory stress test takes a relatively long time. If no issues are encountered, the memory test can be skipped.

  3) The memory space is pre-allocated with 1917MB, specifically as follows:

  * Security Area - 128MB
  * Linux CMA - 256MB
  * CMA for Codec - 512MB
  * CMA for ISP - 384MB
  * OpenCVA - 125MB
  * DRP-AI - 512MB

* Operation:

  1) Enter the following commands for testing:

.. code-block:: shell

   # For development boards with 4GB memory, execute this command
   memtester 2100m 1
   # For development boards with 8GB memory, execute this command
   memtester 6100m 1
   # For development boards with 16GB memory, execute this command
   memtester 14100m 1

\

  2) The memory stress test takes a relatively long time. During the test, characters or cursors will flash, and you may see information similar to the following:

.. code-block:: shell

  memtester version 4.3.0 (64-bit)
  Copyright (C) 2001-2012 Charles Cazabon.
  Licensed under the GNU General Public License version 2 (only).
  
  pagesize is 4096
  pagesizemask is 0xfffffffffffff000
  want 6100MB (6396313600 bytes)
  got  6100MB (6396313600 bytes), trying mlock ...locked.
  Loop 1/1:
    Stuck Address       : ok
    Random Value        : ok
    Compare XOR         : ok
    Compare SUB         : ok
    Compare MUL         : ok
    Compare DIV         : ok
    Compare OR          : ok
    Compare AND         : ok
    Sequential Increment: ok
    Solid Bits          : ok
    Block Sequential    : ok
    Checkerboard        : ok
    Bit Spread          : ok
    Bit Flip            : ok
    Walking Ones        : ok
    Walking Zeroes      : ok
  
  Done.

* Result: The test command can be executed normally and the output information meets expectations, indicating normal operation.


USB 2.0
---------

* Interface Silkscreen: J7

**Function Test**

* Description: Testing is performed by plugging and unplugging a USB storage device (USB flash drive).

* Operation:

  1) Insert the USB flash drive into the USB 2.0 interface of the development board. The system will output information similar to the following:

.. code-block:: shell

  usb 1-1: new high-speed USB device number 2 using ehci-platform
  usb-storage 1-1:1.0: USB Mass Storage device detected
  scsi host0: usb-storage 1-1:1.0
  ......
   sda: sda1
  sd 0:0:0:0: [sda] Attached SCSI removable disk

\

  2) Unplug the USB flash drive from the development board. The system will output information similar to the following:

.. code-block:: shell

   usb 1-1: USB disconnect, device number 2

* Result: The system output information during the plugging and unplugging of the USB flash drive meets expectations, indicating normal operation.


USB 3.0
---------

* Interface Silkscreen: J7

**Function Test**

* Description: Testing is performed by plugging and unplugging a USB storage device (USB flash drive).

* Operation:

  1) Insert the USB 3.0 flash drive into the USB 3.0 interface of the development board. The system will output information similar to the following:

.. code-block:: shell

  usb 6-1: new SuperSpeed Gen 1 USB device number 2 using xhci-hcd
  usb-storage 6-1:1.0: USB Mass Storage device detected
  scsi host0: usb-storage 6-1:1.0
  ......
   sda: sda1
  sd 0:0:0:0: [sda] Attached SCSI removable disk

\

  2) Unplug the USB flash drive from the development board. The system will output information similar to the following:

.. code-block:: shell

   usb 6-1: USB disconnect, device number 2


* Result: The system output information during the plugging and unplugging of the USB flash drive meets expectations, indicating normal operation.


Ethernet Port 1
-----------------

  + Interface Silkscreen: CN6
  + System Interface: eth0

**Function Test**

* Description: Testing is performed by sending ICMP packets from the development board to the PC.

* Operation:

  1) Configure the IP address of the PC's wired network card to 192.168.137.99.

  2) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

  3) Configure the IP address of the development board's Ethernet port with the following specific configuration commands:

.. code-block:: shell

  ifconfig eth1 down
  ifconfig eth0 up
  ifconfig eth0 192.168.137.81

\

  4) Execute the Ethernet port test command with the following specific command:

.. code-block:: shell

   ping 192.168.137.99 -c 2 -w 4

\

  * You may see output information similar to the following:

.. code-block:: shell

  PING 192.168.137.99 (192.168.137.99): 56 data bytes
  64 bytes from 192.168.137.99: seq=0 ttl=128 time=0.833 ms
  64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.429 ms
  
  --- 192.168.137.99 ping statistics ---
  2 packets transmitted, 2 packets received, 0% packet loss
  round-trip min/avg/max = 0.429/0.631/0.833 ms

\

  5) Unplug the network cable, and you may see information similar to the following:

.. code-block:: shell

   dwc-eth-dwmac 15c30000.ethernet eth0: Link is Down


* Result: During the operation, the output information seen meets expectations, and `0% packet loss` during the `ping` test indicates that the Ethernet port is normal.


Ethernet Port 2
------------------

  + Interface Silkscreen: CN7
  + System Interface: eth1

**Function Test**

* Description: Testing is performed by sending ICMP packets from the development board to the PC.

* Operation:

  1) Configure the IP address of the PC's wired network card to 192.168.137.99.

  2) Connect this Ethernet port of the development board to the PC's Ethernet port using a network cable.

  3) Configure the IP address of the development board's Ethernet port with the following specific configuration commands:

.. code-block:: shell

  ifconfig eth0 down
  ifconfig eth1 up
  ifconfig eth1 192.168.137.90

\

  4) Execute the Ethernet port test command with the following specific command:

.. code-block:: shell

   ping 192.168.137.99 -c 2 -w 4

\

  * You may see output information similar to the following:

.. code-block:: shell

  PING 192.168.137.99 (192.168.137.99): 56 data bytes
  64 bytes from 192.168.137.99: seq=0 ttl=128 time=0.849 ms
  64 bytes from 192.168.137.99: seq=1 ttl=128 time=0.470 ms
  
  --- 192.168.137.99 ping statistics ---
  2 packets transmitted, 2 packets received, 0% packet loss
  round-trip min/avg/max = 0.470/0.659/0.849 ms

\

  5) Unplug the network cable, and you may see information similar to the following:

.. code-block:: shell

   dwc-eth-dwmac 15c40000.ethernet eth1: Link is Down


* Result: During the operation, the output information seen meets expectations, and `0% packet loss` during the `ping` test indicates that the Ethernet port is normal.


TF Card
---------

+ Interface Silkscreen: J10
+ Description: The TF card interface of the device supports hot-swapping, and the TF card slot is a self-eject type.

**Function Test**

* Description: Check whether the development board can correctly recognize and remove the TF card by plugging and unplugging the TF card.

+ Operation:

  1) Insert the TF card. At this time, the debug port of the development board should output information similar to the following:

.. code-block:: shell

   mmc1: new high speed SDHC card at address 5048
   mmcblk1: mmc1:5048 SD32G 29.7 GiB
    mmcblk1: p1 p2

\

  2) Eject the TF card. At this time, the debug port of the development board should output information similar to the following:

.. code-block:: shell

   mmc1: card 5048 removed

* Result: If the output information during card insertion and removal meets expectations, the TF card function is normal.


HDMI
------

+ Interface Silkscreen: CN5

**Function Test**

* Description: The device will recognize the HDMI display device and enable it. It is recommended to use a display with a native HDMI interface.

* Operation:

  1) Power off the development board and connect the HDMI display.

  2) Power on the development board. During the startup process, you can see the screen output from the HDMI display.

* Result: Normal display on the HDMI display indicates that the function is normal.

* Attachment: You can enter the `fbset` command in the terminal to view the framebuffer information, which is similar to the following:

.. code-block:: shell

   mode "1920x1080-0"
           # D: 0.000 MHz, H: 0.000 kHz, V: 0.000 Hz
           geometry 1920 1080 1920 1080 32
           timings 0 0 0 0 0 0 0
           accel true
           rgba 8/16,8/8,8/0,0/0
   endmode


USB Camera
------------

+ Interface Silkscreen: J7

**Function Test**

* Description: The system already supports USB cameras and hot-swapping. Common USB cameras can be used for testing.

* Operation:

  1) Connect the HDMI display and insert the USB camera, then enter the following command to view USB devices:

.. code-block:: shell

   lsusb

\

  * You may see the following information (Note: The information listed on the USB bus will vary depending on the camera model):

.. code-block:: shell

   ......
   Bus 001 Device 003: ID 2bdf:0297 DC474C08_P050301_SN0002 2K USB Camera
   ......

\

  2) Use `gst-launch` to capture camera images with the following command:


.. code-block:: shell

   gst-launch-1.0 v4l2src device=/dev/video0 ! waylandsink

\

  * You may see information similar to the following:

.. code-block:: shell

   Setting pipeline to PAUSED ...
   Pipeline is live and does not need PREROLL ...
   Setting pipeline to PLAYING ...
   New clock: GstSystemClock

\

  3) After executing the command, you can see the images captured by the camera on the HDMI display.

* Result: Normal display of the images captured by the USB camera on the display indicates normal operation.



Test Manual
=============

M.2 SSD
---------

- **Interface Description**: PCIe x 2 M.2 Key-M interface, which can be used to connect an M.2 solid-state drive (SSD).
- **Interface Silkscreen**: J14
- **System Interface**: /dev/nvme0

**Function Test**

- **Operation**

  1. Power off the development board, install the M.2 SSD onto the development board, and secure it properly.

  2. Power on the development board. After the system starts successfully and you log in, enter the `lspci` command. You can see the information of the SSD (the device ID here varies by SSD manufacturer):

.. code-block:: shell

   01:00.0 Non-Volatile memory controller: Device 1e4b:1202 (rev 01)

\

  3. Enter the following command to view kernel information:

.. code-block:: shell

   dmesg | grep -i nvme

\

  * You should see information similar to the following:

.. code-block:: shell

   nvme nvme0: pci function 0000:01:00.0
   nvme 0000:01:00.0: enabling device (0000 -> 0002)
   nvme nvme0: allocated 8 MiB host memory buffer.
   nvme nvme0: 4/0/0 default/read/poll queues
    nvme0n1: p1

- **Result**: If you can see the SSD information when viewing the kernel information, the SSD is working normally.

- **Others**:

  1. If the SSD partition is of a type supported by Linux, you can mount the SSD to the system. Refer to the following command:

.. code-block:: shell

   mount /dev/nvme0n1p1 /mnt

\

  2. If the system cannot recognize the SSD partition, back up the data first, then create and format a partition for the SSD before mounting it.


M.2 WiFi
----------

- **Interface Description**: PCIe M.2 Key-E interface, which can be used to connect an M.2 WiFi network card.

- **Interface Silkscreen**: J11

**Function Test**

- **Operation 1: Update Firmware and Configuration to the Development Board**

  1. Power off the development board and connect the Intel AC3165 network card to the WiFi interface.

  2. Power on the development board. After logging in, enter the `lspci` command to check if the 3165 module exists on the PCI bus:

.. code-block:: shell

   lspci

\

  You should be able to see the information of the Intel 3165 network card:

.. code-block:: shell

   01:00.0 Network controller: Intel Corporation Wireless 3165 (rev 79)

\

  3. Extract the firmware of the WiFi module to the root directory of the development board (the WiFi firmware is located in `1. General Materials/1.2 Firmware`):

.. code-block:: shell

   tar xf iwlwifi-7265.tar.gz -C /

\

  4. Load the WiFi driver modules using the following commands:

.. code-block:: shell

   cd /lib/modules/$(uname -r)
   depmod -a
   modprobe cfg80211
   modprobe mac80211
   modprobe iwlwifi
   modprobe iwlmvm

\

  After loading, use the `lsmod` command to check the status of the driver modules. You can see the following information:

.. code-block:: shell

   Module                  Size  Used by
   iwlmvm                299008  0
   mac80211              438272  1 iwlmvm
   iwlwifi               229376  1 iwlmvm
   cfg80211              307200  3 iwlmvm,iwlwifi,mac80211

\

  5. Check the driver binding status with the following command:

.. code-block:: shell

   lspci -nnk -d 8086:3165

\

  After executing the command, you can see the following information:

.. code-block:: shell

   01:00.0 Network controller [0280]: Intel Corporation Wireless 3165 [8086:3165] (rev 79)
           Subsystem: Intel Corporation Wireless 3165 [8086:4410]
           Kernel modules: iwlwifi

\

  6. Create a configuration using the following command:

.. code-block:: shell

   wpa_passphrase MY-WIFI wifi_passwd > /etc/wpa_supplicant.conf

\

  * **Note**: "MY-WIFI" needs to be changed to the name of the WiFi network you can connect to, and "wifi_passwd" needs to be changed to the password of the corresponding WiFi hotspot.

- **Operation 2: Test WiFi Function**

  1. Restart the development board. After the system starts successfully, enter `lsmod` to check the loading status of the WiFi driver modules. This time, you can see that the driver modules have been loaded automatically, as shown in the following information:

.. code-block:: shell

   Module                  Size  Used by
   iwlmvm                299008  0
   mac80211              438272  1 iwlmvm
   iwlwifi               229376  1 iwlmvm
   cfg80211              307200  3 iwlmvm,iwlwifi,mac80211

\

  2. Check the WiFi network card information with the following command:

.. code-block:: shell

  dmesg | grep -i iwlwifi

\

  You can see the following information:

.. code-block:: shell

   iwlwifi 0000:01:00.0: enabling device (0000 -> 0002)
   iwlwifi 0000:01:00.0: Found debug destination: EXTERNAL_DRAM
   iwlwifi 0000:01:00.0: Found debug configuration: 0
   iwlwifi 0000:01:00.0: loaded firmware version 29.4063824552.0 7265D-29.ucode op_mode iwlmvm
   iwlwifi 0000:01:00.0: Detected Intel(R) Dual Band Wireless AC 3165, REV=0x210
   iwlwifi 0000:01:00.0: Applying debug destination EXTERNAL_DRAM
   iwlwifi 0000:01:00.0: Allocated 0x00400000 bytes for firmware monitor.
   iwlwifi 0000:01:00.0: base HW address: a4:6b:b6:52:1c:0a
   iwlwifi 0000:01:00.0 wlp1s0: renamed from wlan0

\

  * **Note**: You can see that the interface registered by the WiFi module in the system is `wlp1s0`.

  3. Connect to the WiFi network using the following command:

.. code-block:: shell

   wpa_supplicant -B -i wlp1s0 -c /etc/wpa_supplicant.conf

\

  You should see the following information:

.. code-block:: shell

   Successfully initialized wpa_supplicant
   rfkill: Cannot open RFKILL control device

\

  4. Check the connection information with the following command:

.. code-block:: shell

   dmesg | grep -i -E "wlp1s0|iwlwifi"

\

  You should see the following information:

.. code-block:: shell

   iwlwifi 0000:01:00.0: Applying debug destination EXTERNAL_DRAM
   iwlwifi 0000:01:00.0: FW already configured (0) - re-configuring
   ......
   wlp1s0: authenticated
   ......
   wlp1s0: associated
   IPv6: ADDRCONF(NETDEV_CHANGE): wlp1s0: link becomes ready

\

  5. Obtain an IP address for the WiFi network card using the following command:

.. code-block:: shell

   udhcpc -i wlp1s0

\

  You should see information similar to the following:

.. code-block:: shell

   udhcpc: started, v1.30.1
   udhcpc: sending discover
   udhcpc: sending select for 192.168.61.130
   udhcpc: lease of 192.168.61.130 obtained, lease time 86400
   /etc/udhcpc.d/50default: Adding DNS 192.168.60.1

\

- **Result**: If the WiFi network card can obtain an IP address, it is working normally.


M.2 5G
--------

+ **Interface Silkscreen**: J13

**Function Test**

- **Description**: The adapted 5G module model is Quectel RM500Q.

- **Operation**:

  1. Power off the development board and connect the Quectel RM500Q to the 5G interface.

  2. Power on the development board. After logging in, enter the `lsusb` command to check if the RM500Q module exists on the USB bus:

.. code-block:: shell

   lsusb

\

  You should see the device information of the RM500Q, similar to the following:

.. code-block:: shell

   Bus 008 Device 002: ID 2c7c:0800 Quectel Wireless Solutions Co., Ltd. RM500Q-GL

\

  3. View the loading status of the 5G module interface driver using the following specific command:

.. code-block:: shell

   dmesg | grep ttyUSB

\

  You should see that the GSM Modem device is successfully connected to the system device, as shown in the following information:

.. code-block:: shell

   usb 8-1: GSM modem (1-port) converter now attached to ttyUSB0
   usb 8-1: GSM modem (1-port) converter now attached to ttyUSB1
   usb 8-1: GSM modem (1-port) converter now attached to ttyUSB2
   usb 8-1: GSM modem (1-port) converter now attached to ttyUSB3

\

  4. Check if the network interface is loaded successfully with the following command:

.. code-block:: shell

   dmesg | grep GobiNet

\

  You should see the GobiNet driver information, registration information, and network interface information of the 5G module, as follows:

.. code-block:: shell

   GobiNet: Quectel_Linux&Android_GobiNet_Driver_V1.6
   usbcore: registered new interface driver GobiNet
   GobiNet 8-1:1.4 eth2: register 'GobiNet' at usb-15860000.usb-1, GobiNet Ethernet Device, 0e:0c:aa:23:b9:21

\

  * **Note**: The information here shows that the network interface of the 5G module is registered as eth2.

  5. Execute the network connection program of the 5G module using the following command:

.. code-block:: shell

   ./quectel-CM

\

  * **Note**: The `quectel-CM` program is located in the network disk `1. General Materials/1.2-Firmware`

  After executing the network connection program of the 5G module, you can see that the 5G module has obtained an IP address. The information is similar to the following:

.. code-block:: shell

   QConnectManager_Linux_V1.6.5
   Find /sys/bus/usb/devices/8-1 idVendor=0x2c7c idProduct=0x800, bus=0x008, dev=0x002
   Auto find qmichannel = /dev/qcqmi2
   Auto find usbnet_adapter = eth2
   netcard driver = GobiNet, driver version = 5.10.145-cip17-yocto-standard-g
   qmap_mode = 1, qmap_version = 5, qmap_size = 16384, muxid = 0x81, qmap_netcard = eth2
   Modem works in QMI mode
   Get clientWDS = 7
   Get clientDMS = 8
   Get clientNAS = 9
   Get clientUIM = 10
   requestBaseBandVersion RM500QGLABR10A02M4G
   requestGetSIMStatus SIMStatus: SIM_READY
   ctnet///0/IPV4V6
   requestRegistrationState2 MCC: 460, MNC: 11, PS: Attached, DataCap: LTE
   requestQueryDataCall IPv4ConnectionStatus: DISCONNECTED
   ip addr flush dev eth2
   ip link set dev eth2 down
   requestSetupDataCall WdsConnectionIPv4Handle: 0x551fc220
   ip link set dev eth2 up
   busybox udhcpc -f -n -q -t 5 -i eth2
  udhcpc: started, v1.30.1
  udhcpc: sending discover
  udhcpc: sending select for 10.23.45.204
  udhcpc: lease of 10.23.45.204 obtained, lease time 7200
   /etc/udhcpc.d/50default: Adding DNS 202.96.128.86
   /etc/udhcpc.d/50default: Adding DNS 202.96.134.133


- **Result**: The 5G module is working normally if the `quectel-CM` program can successfully obtain a network IP address (shown as `lease of x.x.x.x obtained`).


Mipi CSI
----------

+ Interface silk screen: CN1(CSI0), CN2(CSI1), CN3(CSI2), CN4(CSI3)

**Function Test**

* Description: The adapted camera model is Sony STARVIS IMX462.

* Operation:

  1) Power off the development board and connect the Sony STARVIS IMX462 camera to the MIPI-CSI interface.

  2) Power on the development board, log in to the development board, and enter the `lsmod` command to check if `ecam_imx462` is Used:

.. code-block:: shell

   lsmod

\

  * The information you can see is similar to the following:

.. code-block:: shell

   Module                  Size  Used by
   ......
   ecam_imx462          2125824  1

\

  3) Enter the command to call the preset script to configure the camera (note that the CSI interface corresponds to the configuration script, see the subsequent table):

.. code-block:: shell

   ./gstreamer_cam_test_CAM0_CN7.sh 1920x1080

\

  * The following is the table of camera configuration scripts corresponding to CSI interfaces:

+---------------+---------------------------------+
| CSI Interface |      Configuration Script       |
+===============+=================================+
| CSI0          | gstreamer_cam_test_CAM0_CN7.sh  |
+---------------+---------------------------------+
| CSI1          | gstreamer_cam_test_CAM1_CN8.sh  |
+---------------+---------------------------------+
| CSI2          | gstreamer_cam_test_CAM2_CN9.sh  |
+---------------+---------------------------------+
| CSI3          | gstreamer_cam_test_CAM3_CN10.sh |
+---------------+---------------------------------+

  * The information you can see when calling the preset script for configuration is similar to the following:

.. code-block:: shell

   1920x1080
   imx462 0-001f: Stream ON - 1080p @60fps
   Link CRU/CSI2 to imx462 0-001f with format UYVY8_2X8 and resolution 1920x1080
   Available Resolutions :  1920x1080 , 1280x720 , 640x480
    Usage Example: #sh gstreamer_cam_test.sh 1920x1080

\

  * Tip: An `ISP Write Error` reported before `Stream ON` does not affect the function. It is sufficient that `Reconfiguring ISP...` appears later and `Stream ON` is successful.

  4) Use `gst-launch` to capture and display images with the following command:

.. code-block:: shell

   gst-launch-1.0 v4l2src device=/dev/video0 ! waylandsink

\

  * The information you can see is similar to the following:

.. code-block:: shell

   Setting pipeline to PAUSED ...
   Pipeline is live and does not need PREROLL ...
   Setting pipeline to PLAYING ...
   New clock: GstSystemClock
   imx462 0-001f: imx462_get_fmt code=0x2006, w/h=(1920,1080), colorspace=7, field=1
   Gain doesn't work in Auto Exposure mode, change to manual exposure mode
   In Auto mode, change to manual exposure mode
   imx462 0-001f: Stream ON - 1080p @60fps

\

* Result: After step 4 is executed, it is normal if you can see the画面 captured by the camera on the display screen.

**Exception Handling**

* If you encounter problems with the Sony STARVIS IMX462 camera, you can provide the output information of the following commands, and we will help you analyze it:

.. code-block:: shell

   # Command 1
   lsmod
   # Command 2
   dmesg | grep csi
   # Command 3
   dmesg | grep imx462
   # Command 4
   media-ctl -d /dev/media3 -p

\

* Tip: The parameter `/dev/media3` in the last command above is passed according to the serial number of the corresponding CSI interface. For example, for CSI0, pass /dev/media0.