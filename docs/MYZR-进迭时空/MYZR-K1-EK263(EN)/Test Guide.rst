Test Guide
============

Ethernet Port Test
--------------------

Ethernet Port 1
~~~~~~~~~~~~~~~~~


|  Silkscreen Label: ETH0
|  System Interface: eth0
|  Test Description: Test by sending ICMP packets from the development board to PC
|  Test Procedure

1. Set the IPv4 address of PC wired network adapter to 192.168.137.99
2. Connect the Ethernet port of the development board to the PC with an Ethernet cable. Serial port output example:

.. code-block:: shell

    [ 1069.788888] rk_gmac-dwmac 2a220000.ethernet eth0: Link is Up - 100Mbps/Full - flow control rx/tx

3. IP is obtained by DHCP by default. Configure static IP for testing with the following commands:

.. code-block:: shell

    ifconfig eth1 down
    ifconfig eth0 up
    ifconfig eth0 192.168.137.81

4. Run the following command to verify Ethernet Port 1:

.. code-block:: shell

    ping -I eth0 192.168.137.99 -c 2 -w 4
    PING 192.168.137.99 (192.168.137.99) from 192.168.137.17 eth0: 56(84) bytes of data.
    64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=1.28 ms
    64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.378 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1002ms
    rtt min/avg/max/mdev = 0.378/0.829/1.280/0.451 ms

|  "0% packet loss" means the test passed
|  If "100% packet loss" occurs, confirm that all PC firewalls are disabled

Ethernet Port 2
~~~~~~~~~~~~~~~~~~


|  Silkscreen Label: ETH1
|  System Interface: eth1
|  Test Description: Test by sending ICMP packets from the development board to PC
|  Test Procedure

1. Set the IPv4 address of PC wired network adapter to 192.168.137.99
2. Connect the Ethernet port of the development board to the PC with an Ethernet cable. Serial port output example:

.. code-block:: shell

    [ 113.734632] k1x_emac cac80000.ethernet eth0: Link is Up - 1Gbps/Full - flow control rx/tx

3. IP is obtained by DHCP by default. Configure static IP for testing with the following commands:

.. code-block:: shell

    ifconfig eth0 down
    ifconfig eth1 up
    ifconfig eth1 192.168.137.81

4. Run the following command to verify Ethernet Port 2:

.. code-block:: shell

    ping -I eth1 192.168.137.99 -c 2 -w 4
    PING 192.168.137.99 (192.168.137.99) from 192.168.137.185 eth1: 56(84) bytes of data.
    64 bytes from 192.168.137.99: icmp_seq=1 ttl=128 time=1.42 ms
    64 bytes from 192.168.137.99: icmp_seq=2 ttl=128 time=0.489 ms

    --- 192.168.137.99 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1002ms
    rtt min/avg/max/mdev = 0.489/0.955/1.421/0.466 ms

|  "0% packet loss" means the test passed
|  If "100% packet loss" occurs, confirm that all PC firewalls are disabled

USB Test
----------

|  Silkscreen Label:
|  USB 2.0/3.0 : J4
|  Test Description: Test by hot-plugging USB storage devices (USB flash drive)
|  Test Procedure

1. Insert the USB device into the onboard USB interface. The system will output logs as below:

.. code-block:: shell

    [ 56.017601] usb 3-1: new SuperSpeed USB device number 2 using xhci-hcd
    [ 56.047097] usb-storage 3-1:1.0: USB Mass Storage device detected
    [ 56.054981] scsi host0: usb-storage 3-1:1.0
    [ 57.063522] scsi 0:0:0:0: Direct-Access aigo U330 PMAP PQ: 0 ANSI: 6
    [ 59.137255] sd 0:0:0:0: [sda] 122880000 512-byte logical blocks: (62.9 GB/58.6 GiB)
    [ 59.145513] sd 0:0:0:0: [sda] Write Protect is off
    [ 59.150350] sd 0:0:0:0: [sda] Mode Sense: 2b 00 00 08
    [ 59.155652] sd 0:0:0:0: [sda] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
    [ 59.168788] sda: sda1[ 59.171550] sd 0:0:0:0: [sda] Attached SCSI removable disk
    [ 59.223333] exFAT-fs (sda): invalid fs_name
    [ 59.227645] exFAT-fs (sda): failed to read boot sector
    [ 59.232849] exFAT-fs (sda): failed to recognize exfat type
    [ 59.244624] ntfs3: sda: Primary boot signature is not NTFS.
    [ 59.250272] ntfs3: sda: try to read out of volume at offset 0xea5fffe00
    [ 59.547291] exFAT-fs (sda1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

2. Unplug the USB device from the baseboard. The system will output logs as below:

.. code-block:: shell

    [ 79.939940] usb 3-1: USB disconnect, device number 2

SD Interface Test
-------------------

|  Silkscreen Label: TF
|  Test Description: Test by hot-plugging TF card
|  Test Procedure

1. Insert the TF card into the SD interface. The system outputs the following logs:

.. code-block:: shell

    [ 98.656408] mmc0: new high speed SDHC card at address 1234
    [ 98.663781] mmcblk0: mmc0:1234 SA08G 7.21 GiB
    [ 98.670550] mmcblk0: p1

|  Result: Normal output indicates the TF card is recognized correctly.

2. Remove the TF card. The system outputs the following logs:

.. code-block:: shell

    [ 142.185791] mmc0: card 1234 removed

|  Result: Normal behavior indicates TF card hot-plug function works properly.

Audio Playback Test (Pending New Version)
--------------------------------------------

|  Silkscreen Label: P1
|  Test Description: Verify audio playback function by playing audio files
|  Test Procedure

1. Connect headphones to the corresponding silkscreen interface
2. Run the following commands for testing:

|  Check rockchipes8388 sound card and device number

.. code-block:: shell

    aplay -l

|  Specify playback device: hw:card number,device number

.. code-block:: shell

    aplay -D hw:0,0 test_app/music_test.wav

|  System output:

.. code-block:: shell

    Playing WAVE 'test_app/music_test.wav' : Signed 16 bit Little Endian, Rate 44100 Hz, Stereo

|  Audible sound from headphones means the audio playback test passed.

Recording Test (Pending New Version)
--------------------------------------

|  Silkscreen Label: JP1
|  Test Description: Test by recording and playing audio files
|  Test Procedure

1. Connect a headset with microphone to the corresponding silkscreen interface
2. Run the following command to record audio for 10 seconds:

.. code-block:: shell

    arecord -d 10 -f cd -r 44100 -c 2 -t wav record.wav

3. Connect headphones or speaker to interface J16, then play the recorded file:

.. code-block:: shell

    aplay -D hw:0,0 record.wav

|  Audible recorded sound from output device means the recording test passed.

Speaker Test (Pending New Version)
------------------------------------

|  Silkscreen Label: J15, J16
| Test Description:
| Test Procedure

1. Run the following command:

.. code-block:: shell

    aplay test_app/music_test.wav

| Sound output from the speaker indicates the test passed.

Wi-Fi Test
-----------

|  Silkscreen Label: U22
|  Test Description: Verify network connectivity by sending ICMP packets to external network after connecting to AP
|  Test Procedure

1. Connect the Wi-Fi antenna to interface U40
2. Generate WPA PSK configuration file for target SSID

|  Run the following command:

.. code-block:: shell

    cat > /etc/wpa_supplicant.conf << 'EOF'
    ctrl_interface=/var/run/wpa_supplicant
    update_config=1
    network={
        ssid="zhi"
        psk="123456789"
        key_mgmt=WPA-PSK
    }
    EOF

3. Establish Wi-Fi connection:

.. code-block:: shell

    wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf

|  Output log:

.. code-block:: shell

    Successfully initialized wpa_supplicant

4. Obtain IP address via DHCP:

.. code-block:: shell

    udhcpc -i wlan0

|  Output log:

.. code-block:: shell

    udhcpc: started, v1.36.1
    udhcpc: broadcasting discover
    udhcpc: broadcasting select for 192.168.39.200, server 192.168.39.83
    udhcpc: lease of 192.168.39.200 obtained from 192.168.39.83, lease time 3600
    deleting routers
    adding dns 192.168.39.83

5. Test network connectivity:

.. code-block:: shell

    ping -4 -I wlan0 www.baidu.com -c 3 -w 4

|  Output log:

.. code-block:: shell

    PING (183.2.172.177) from 192.168.39.200 wlan0: 56(84) bytes of data.
    64 bytes from 183.2.172.177 (183.2.172.177): icmp_seq=1 ttl=52 time=281 ms
    64 bytes from 183.2.172.177 (183.2.172.177): icmp_seq=2 ttl=52 time=332 ms
    64 bytes from 183.2.172.177 (183.2.172.177): icmp_seq=3 ttl=52 time=252 ms

    --- ping statistics ---3 packets transmitted, 3 received, 0% packet loss, time 2002ms
    rtt min/avg/max/mdev = 252.230/288.472/332.418/33.186 ms

|  Result: "0% packet loss" indicates normal Wi-Fi connection.

Bluetooth Test
----------------

|  Silkscreen Label: U22
|  Test Description: Send L2CAP echo request and receive response after scanning Bluetooth devices
|  Test Procedure

1. Connect the antenna to interface U40
2. Enable Bluetooth controller:

.. code-block:: shell

    hciconfig hci0 up

3. Scan nearby Bluetooth devices:

.. code-block:: shell

    hcitool scan

|  Output log:

.. code-block:: shell

    Scanning ...
    40:45:A0:49:3B:1A chensz

|  Capture target Bluetooth MAC address for subsequent testing.

4. Test L2CAP communication:

.. code-block:: shell

    l2ping 40:45:A0:49:3B:1A

|  Output log:

.. code-block:: shell

    Ping: 40:45:A0:49:3B:1A from E8:5C:5F:B5:7A:11 (data size 44) ...
    44 bytes from 40:45:A0:49:3B:1A id 0 time 32.41ms
    44 bytes from 40:45:A0:49:3B:1A id 1 time 77.03ms
    44 bytes from 40:45:A0:49:3B:1A id 2 time 90.89ms
    44 bytes from 40:45:A0:49:3B:1A id 3 time 59.38ms
    44 bytes from 40:45:A0:49:3B:1A id 4 time 93.44ms
    ^C5 sent, 5 received, 0% loss

|  Result: "0% packet loss" indicates normal Bluetooth communication.

M.2 Interface Test
--------------------

|  Silkscreen Label: J2
|  Test Description: Check disk mounting status after M.2 hard drive connection
|  Test Procedure

1. Power off the board, connect M.2 SSD, then power on the development board
2. Create mount point and mount NVMe disk:

.. code-block:: shell
    mkdir -p /mnt/nvme
    mount /dev/nvme0n1p1 /mnt/nvme

3. Verify mounting status:

.. code-block:: shell

    df -h

|  Successful mounting will display similar output: /dev/nvme0n1p1 499M 10M 490M 2% /mnt/nvme

4. Unmount the hard drive:

.. code-block:: shell

    umount /mnt/nvme

M.2 Wi-Fi
-----------

|   Interface Description: PCIe M.2 Key-E interface for M.2 Wi-Fi adapter
|   Silkscreen Label: WIFI

**Function Test**

- Operation 1: Upgrade firmware and configure system

1. Power off the board and install Intel AC3165 M.2 Wi-Fi card.
2. Power on and log in, run lspci to detect PCIe device:

.. code-block:: shell

    lspci

|  Expected device information:

.. code-block:: shell

    01:00.0 Class 0280: 8086:3165

3. Extract Wi-Fi firmware to system root directory:

.. code-block:: shell

    tar xf iwlwifi-7265.tar.gz -C /

4. Load Wi-Fi driver modules:

.. code-block:: shell

    cd /lib/firmware
    ln -sf iwlwifi-7265D-29.ucode iwlwifi-7265D-22.ucode
    ls -l iwlwifi-7265D-*.ucode
    cd /lib/modules/$(uname -r)
    depmod -a
    modprobe cfg80211
    modprobe mac80211
    modprobe iwlwifi
    modprobe iwlmvm

5. Generate Wi-Fi connection configuration:

.. code-block:: shell

    cat > /etc/wpa_supplicant.conf << 'EOF'
    ctrl_interface=/var/run/wpa_supplicant
    update_config=1
    network={
        ssid="zhi"
        psk="123456789"
        key_mgmt=WPA-PSK
    }
    EOF

- Operation 2: Wi-Fi function verification

3. Connect to Wi-Fi network:

.. code-block:: shell

    wpa_supplicant -B -i wlP2p1s0 -c /etc/wpa_supplicant.conf

|  Expected output:

.. code-block:: shell

    Successfully initialized wpa_supplicant
    rfkill: Cannot open RFKILL control device

5. Obtain IP address for M.2 Wi-Fi adapter:

.. code-block:: shell

    udhcpc -i wlP2p1s0

|  Expected connection logs:

.. code-block:: shell

    udhcpc: started, v1.36.1
    udhcpc: broadcasting discover
    udhcpc: broadcasting discover
    udhcpc: broadcasting discover
    [  648.886876] wlP2p1s0: authenticate with 3e:0f:fe:a1:9c:c1
    [  648.892438] wlP2p1s0: 80 MHz not supported, disabling VHT
    [  648.902205] wlP2p1s0: send auth to 3e:0f:fe:a1:9c:c1 (try 1/3)
    [  648.921023] wlP2p1s0: authenticated
    [  648.926976] wlP2p1s0: associate with 3e:0f:fe:a1:9c:c1 (try 1/3)
    [  648.966319] wlP2p1s0: RX AssocResp from 3e:0f:fe:a1:9c:c1 (capab=0x1431 status=0 aid=1)
    [  648.988409] wlP2p1s0: associated
    [  649.103599] wlP2p1s0: Limiting TX power to 20 (20 - 0) dBm as advertised by 3e:0f:fe:a1:9c:c1

.. code-block:: shell

    ping -I wlP2p1s0 www.baidu.com

.. code-block:: shell

    PING www.baidu.com(240e:ff:e020:99b:0:ff:b099:cff1 (240e:ff:e020:99b:0:ff:b099:cff1)) from 240e:47e:32e1:75ff:a3bf:def1:4d68:7cbe wlP2p1s0: 56 data bytes
    64 bytes from 240e:ff:e020:99b:0:ff:b099:cff1 (240e:ff:e020:99b:0:ff:b099:cff1): icmp_seq=1 ttl=54 time=57.8 ms
    64 bytes from 240e:ff:e020:99b:0:ff:b099:cff1 (240e:ff:e020:99b:0:ff:b099:cff1): icmp_seq=2 ttl=54 time=44.0 ms

- Result: Successful IP acquisition indicates M.2 Wi-Fi card works normally.

CAN Test
----------

|  Silkscreen Label: J13
|  Test Description: Transmit & receive test with another CAN-enabled development board (MYZR-T536-EK270 for reference)
|  Test Procedure

1. Connect CAN interfaces of two boards (H to H, L to L), then power on both devices
2. Configure CAN controller on both boards:

|  MYZR-K1-LB-REVA:

.. code-block:: shell

    ip link set can0 up type can bitrate 1000000 dbitrate 5000000 fd on
    candump can0

|  MYZR-T536-EK270:

.. code-block:: shell

    ip link set can1 up type can bitrate 1000000 dbitrate 5000000 fd on
    candump can1

3. Send test data from MYZR-K1-LB-REVA:

.. code-block:: shell

    cansend can0 1F334455#1122334455667788

|  MYZR-T536-EK270 will receive: `can1  1F334455   [8]  11 22 33 44 55 66 77 88`, press Ctrl+C to exit.

4. Switch transmission direction:

|  MYZR-K1-LB-REVA:

.. code-block:: shell

    candump can0

|  MYZR-T536-EK270:

.. code-block:: shell

    cansend can1 1F334455#1122334455667788

|  MYZR-K1-LB-REVA will receive corresponding data. Normal data interaction means CAN function is valid.

RS232 Test
------------

|  Silkscreen Label: J8
|  Test Description: Transmit & receive test with PC via RS232-to-USB adapter
|  Test Procedure

1. Connect development board and PC with RS232-to-USB adapter; cross connect TX/RX pins
2. Open serial port via Xshell: Baud rate 115200, Data bit 8, Stop bit 1
3. Run test commands:

.. code-block:: shell

    stty -F /dev/ttyS2 115200
    echo "123456789" > /dev/ttyS2
    cat /dev/ttyS2

|  The terminal will print `123456789` and enter receiving mode.

4. Input `123` in serial terminal, the board will output:

.. code-block:: shell

    123

|  Press Ctrl+C to exit. Consistent interaction indicates RS232 works normally.

RS485 Test
------------

|  Silkscreen Label: J9
|  Test Description: Transmit & receive test with PC via RS485-to-USB adapter
|  Test Procedure

1. Connect development board and PC with RS485-to-USB adapter (A to A, B to B)
2. Open serial port via Xshell: Baud rate 115200, Data bit 8, Stop bit 1
3. Run test commands:

.. code-block:: shell

    stty -F /dev/ttyS5 115200
    echo "123456789" > /dev/ttyS5
    cat /dev/ttyS5

|  The terminal will print `123456789` and enter receiving mode.

4. Input `123` in serial terminal, the board will output:

.. code-block:: shell

    123

|  Press Ctrl+C to exit. Consistent interaction indicates RS485 works normally.

RTC Test
----------

|  Silkscreen Label: RTC
|  Test Description: Read/set RTC time and verify time retention after power cycle
|  Test Procedure

1. Power off the board, confirm coin battery installation. Measure battery voltage with multimeter (normal: ~3.3V)
2. Power on and check system time:

.. code-block:: shell

    date

|  Default output:

.. code-block:: shell

    Sat Jan  1 00:01:02 UTC 2000

3. Check hardware RTC time:

.. code-block:: shell

    hwclock -f /dev/rtc0

|  Default output:

.. code-block:: shell

    Sat Jan  1 00:01:04 UTC 2000

4. Set system time and sync to RTC:

.. code-block:: shell

    date -s "2025-01-24 14:00:00" && hwclock -w -f /dev/rtc0

5. Verify RTC write result:

.. code-block:: shell

    hwclock -f /dev/rtc0

|  Output example:

.. code-block:: shell

    Fri Jan 24 14:00:17 2025  0.000000 seconds

|  Time consistency indicates successful RTC synchronization.

5. Power cycle the device and check RTC time again:

.. code-block:: shell

    hwclock -f /dev/rtc0

|  RTC time continues counting normally after power loss, which means the RTC test passed.

ADC Test
----------

|  Silkscreen Label: J12
|  Test Description: ADC pins default to low level
|  Test Procedure

1. Run the following commands to read raw ADC value:

.. code-block:: shell

    cd /sys/bus/iio/devices/iio:device0
    cat in_voltage2_raw

|  Default output:

.. code-block:: shell

    0

2. Connect 1.8V to pin 1 of J12, then read another ADC channel:

.. code-block:: shell

    cat in_voltage3_raw

|  Output example:

.. code-block:: shell

    2412

HDMI_TX Test
--------------

|  Silkscreen Label: J5
|  Test Description:
|  Test Procedure:
|  Connect HDMI display to J5 interface, system desktop will be displayed normally.

Camera Test
-------------

|  Silkscreen Label: CSI1, CSI2
|  Test Description:
|  Test Procedure:

1. Power off the board, install camera module with correct orientation, then power on.
2. Detect camera sensor on MIPI CSI interface (CSI1 as example):

.. code-block:: shell

    cam-test  /usr/share/camera_json/csi1_camera_detect.json

3. Successful detection log:

.. code-block:: shell

    ...
    I: cam_sensors_module.c(240): "detect ov5695_spm sensors in csi1: success, set 2592x1944 to 1920x1080"
    I: auto_detect_camera(1430): "auto detect sensor ===================== finish "
    I: update_json_file(732): "save json to /usr/share/camera_json/csi1_camera_auto.json success"

4. Launch camera preview:

.. code-block:: shell

    WAYLAND_DISPLAY=wayland-1 XDG_RUNTIME_DIR=/root/ \
    gst-launch-1.0 -v \
    spacemitsrc location=/usr/share/camera_json/csi1_camera_auto.json ! \
    queue ! \
    waylandsink sync=0 render-rectangle="<0,0,1280,720>"

|  Real-time camera preview indicates the camera function works normally.

MIPI_DSI Test (5-inch Display Verification Pending)
-----------------------------------------------------

|  Silkscreen Label: CON2
|  Test Description:
|  Test Procedure:

1. Power off the board, connect MIPI display, then power on.
2. System boot logs and desktop interface will be displayed normally.

GPIO Test
-----------

+------------+----------+----------+----------+----------+-----+----------+
| Silkscreen | 1        | 3        | 5        | 7        | 11  | 16       |
+------------+----------+----------+----------+----------+-----+----------+
| GPIO       | GPIO1_B4 | GPIO1_B5 | GPIO1_B6 | GPIO1_B7 | GND | GPIO1_C7 |
+------------+----------+----------+----------+----------+-----+----------+
| High Level | 1.8V     | 1.8V     | 1.8V     | 1.8V     | -   | 1.8V     |
+------------+----------+----------+----------+----------+-----+----------+

|  Test Command Format: `./gpio_test <gpio_num> [0/1/irq]`
|  Test Procedure

1. Set GPIO1_B4 to high level:

.. code-block:: shell

    ./test_app/gpio_test.out GPIO1_B4 1

|  Output:

.. code-block:: shell

    Set GPIO44 HIGH

|  Measure pin voltage with multimeter, 3.3V means test passed.

2. Set GPIO1_B4 to low level:

.. code-block:: shell

    ./test_app/gpio_test.out GPIO1_B4 0

|  Output:

.. code-block:: shell

    Set GPIO44 LOW

|  Measure pin voltage with multimeter, 0V means test passed.

3. Interrupt test (falling edge trigger). Short pin 1 and 2 of J23 with Dupont line, enable interrupt monitoring:

.. code-block:: shell

    ./test_app/gpio_test.out GPIO1_B4 irq &

|  Trigger falling edge by toggling GPIO level:

.. code-block:: shell

    ./test_app/gpio_test.out GPIO1_B5 1
    ./test_app/gpio_test.out GPIO1_B5 0

|  Interrupt trigger log:

.. code-block:: shell

    GPIO44 interrupt detected! Value: 0

|  Normal interrupt response indicates GPIO interrupt function is valid.

4G Module Test
----------------

|  Silkscreen Label: U20
|  Test Description:
|  Test Procedure:
|  Connect 4G antenna to U21
|  Run control commands:

.. code-block:: shell

    export OUT_IO_OUT_NUM=23
    echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
    echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction
    echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
    export OUT_IO_OUT_NUM=48
    echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
    echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction
    echo 0 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value
    export OUT_IO_OUT_NUM=24
    echo ${OUT_IO_OUT_NUM} > /sys/class/gpio/export
    echo "out" > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/direction
    echo 1 > /sys/class/gpio/gpio${OUT_IO_OUT_NUM}/value

|  Module enumeration logs:

.. code-block:: shell

    [   34.053593] usb 1-1.4: new high-speed USB device number 4 using mv-ehci
    [   34.169682] cdc_ether 1-1.4:1.0 eth2: register 'cdc_ether' at usb-mv-ehci1-1.4, CDC Ethernet Device, 22:89:84:6a:96:ab
    [   34.193272] usbcore: registered new interface driver usbserial_generic
    [   34.200001] usbserial: USB Serial support registered for generic
    [   34.213736] usbcore: registered new interface driver option
    [   34.219453] usbserial: USB Serial support registered for GSM modem (1-port)
    [   34.226740] option 1-1.4:1.2: GSM modem (1-port) converter detected
    [   34.233444] usb 1-1.4: GSM modem (1-port) converter now attached to ttyUSB0
    [   34.240608] option 1-1.4:1.3: GSM modem (1-port) converter detected
    [   34.247249] usb 1-1.4: GSM modem (1-port) converter now attached to ttyUSB1
    [   34.254438] option 1-1.4:1.4: GSM modem (1-port) converter detected
    [   34.261082] usb 1-1.4: GSM modem (1-port) converter now attached to ttyUSB2

|  Send AT commands to query module status:

.. code-block:: shell

    echo -e "AT+QNETDEVCTL?\r\n" > /dev/ttyUSB1
    echo -e "AT+QGMR\r\n" > /dev/ttyUSB1
    echo -e "AT+CPIN?\r\n" > /dev/ttyUSB1
    echo -e "AT+CEREG?\r\n" > /dev/ttyUSB1
    echo -e "AT+QNETDEVCTL=3,1,1\r\n" > /dev/ttyUSB1

|  Test cellular network connectivity:

.. code-block:: shell

    ping -I eth2 www.baidu.com -4 -c 3

|  Network test output:

.. code-block:: shell

    PING www.a.shifen.com (183.240.99.224) from 192.168.43.100 eth2: 56(84) bytes of data.
    64 bytes from 183.240.99.224 (183.240.99.224): icmp_seq=1 ttl=51 time=119 ms
    64 bytes from 183.240.99.224 (183.240.99.224): icmp_seq=2 ttl=51 time=106 ms
    64 bytes from 183.240.99.224 (183.240.99.224): icmp_seq=3 ttl=51 time=117 ms

    --- www.a.shifen.com ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2002ms
    rtt min/avg/max/mdev = 106.129/114.143/119.065/5.716 ms

|  Normal network access indicates the 4G module test passed.
