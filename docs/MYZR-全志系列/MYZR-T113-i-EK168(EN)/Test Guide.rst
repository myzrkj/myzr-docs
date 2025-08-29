Test Guide
============

LED Test
----------

|  Access the file system and enter commands. If the LED can be normally controlled to turn on and off, the LED function is normal.

.. code-block:: shell

    echo 0 > /sys/class/leds/user-led0/brightness                //Turn off LED1
    echo 1 > /sys/class/leds/user-led0/brightness                //Turn on LED1

Key Test
----------

1. After pressing the KEY0, if the evaluation board system restarts, the key function is normal.
2. Follow the steps in the flashing manual to flash the firmware via USB and start the system normally; if successful, the KEY1 function is normal.
3. Enter the commands:

.. code-block:: shell

    cat /proc/bus/input/devices
    od -x /dev/input/event0

|  If output information similar to the following is displayed, the KEY2 function is normal.

.. code-block:: shell

    0000000 6129 63e2 0930 0000 0001 0073 0001 0000
    0000020 6129 63e2 0930 0000 0000 0000 0000 0000
    0000040 6129 63e2 d9b7 0003 0001 0073 0000 0000
    0000060 6129 63e2 d9b7 0003 0000 0000 0000 0000

Ethernet Port Test
--------------------

Ethernet Port 1
~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON20
|  System Interface: eth0
|  Test Description: Test by sending ICMP packets from the development board to the PC.
|  Test Operations:

1. Configure the PC's wired network card IP to 192.168.137.1
2. Enable Ethernet Port 1, connect the development board's Ethernet port to the PC's Ethernet port using a network cable. The serial port will display the following information:

.. code-block:: shell

    ifconfig eth0 up

.. code-block:: shell

    [  413.267040] libphy: 4500000.gmac0: probed
    [  413.272096] [sound  403][MACH simple_parse_of] simple_dai_link_of failed
    [  413.274297] sunxi-gmac 4500000.gmac0 eth0: eth0: Type(8) PHY ID 0000011a at 0 IRQ poll (4500000.gmac0-0:00)
    [  443.434378] sunxi-gmac 4500000.gmac0 eth0: Link is Up - 1Gbps/Full - flow control off
    [  443.443192] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready

3. Enter the following command to automatically obtain an IP address:

.. code-block:: shell

    udhcpc -i eth0

|  Output Information:

.. code-block:: shell

    udhcpc: started, v1.33.2
    udhcpc: sending discover
    udhcpc: sending select for 192.168.137.88
    udhcpc: lease of 192.168.137.88 obtained, lease time 604800
    deleting routers
    adding dns 192.168.137.1

4. Enter the following command to verify Ethernet Port 1:

.. code-block:: shell

    ping www.baidu.com -I eth0

|  Output Information:

.. code-block:: shell

    PING www.baidu.com (183.2.172.177): 56 data bytes
    64 bytes from 183.2.172.177: seq=0 ttl=53 time=10.659 ms
    64 bytes from 183.2.172.177: seq=1 ttl=53 time=9.572 ms
    64 bytes from 183.2.172.177: seq=2 ttl=53 time=9.260 ms
    64 bytes from 183.2.172.177: seq=3 ttl=53 time=9.235 ms

    --- www.baidu.com ping statistics ---
    4 packets transmitted, 4 packets received, 0% packet loss
    round-trip min/avg/max = 9.235/9.681/10.659 ms

4. Configure a static IP:

.. code-block:: shell
    
    ifconfig eth0 192.168.137.81

|  Enter the command for verification:

.. code-block:: shell

    ping -I eth0 192.168.137.1 -c 2 -w 4

|  Output Information:

.. code-block:: shell

    PING 192.168.137.1 (192.168.137.1): 56 data bytes
    64 bytes from 192.168.137.1: seq=0 ttl=128 time=0.636 ms
    64 bytes from 192.168.137.1: seq=1 ttl=128 time=1.165 ms

    --- 192.168.137.1 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.636/0.900/1.165 ms

|  "0% packet loss" indicates the test is passed.
|  If "100% packet loss" appears, first confirm that all firewalls on the PC are disabled.

Ethernet Port 2
~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON21
|  System Interface: eth1
|  Test Description: Test by sending ICMP packets from the development board to the PC.
|  Test Operations:

1. Configure the PC's wired network card IP to 192.168.137.1
2. Enable Ethernet Port 1, connect the development board's Ethernet port to the PC's Ethernet port using a network cable:

.. code-block:: shell

    ifconfig eth1 up

3. Enter the following command to automatically obtain an IP address:

.. code-block:: shell

    udhcpc -i eth1

.. code-block:: shell

    udhcpc: started, v1.33.2
    udhcpc: sending discover
    udhcpc: sending select for 192.168.137.44
    udhcpc: lease of 192.168.137.44 obtained, lease time 604800
    deleting routers
    adding dns 192.168.137.1

4. Enter the following command to verify Ethernet Port 1:

.. code-block:: shell

    ping www.baidu.com -I eth1

.. code-block:: shell

    PING www.baidu.com (183.2.172.177): 56 data bytes
    64 bytes from 183.2.172.177: seq=0 ttl=53 time=12.714 ms
    64 bytes from 183.2.172.177: seq=1 ttl=53 time=15.923 ms
    64 bytes from 183.2.172.177: seq=2 ttl=53 time=10.738 ms
    64 bytes from 183.2.172.177: seq=3 ttl=53 time=12.096 ms

    --- www.baidu.com ping statistics ---
    5 packets transmitted, 5 packets received, 0% packet loss
    round-trip min/avg/max = 10.736/12.441/15.923 ms

5. Configure a static IP:

.. code-block:: shell

    ifconfig eth0 192.168.137.81

|  Enter the command for verification:

.. code-block:: shell

    ping -I eth0 192.168.137.1 -c 2 -w 4

|  Output Information:

.. code-block:: shell

    PING 192.168.137.1 (192.168.137.1): 56 data bytes
    64 bytes from 192.168.137.1: seq=0 ttl=128 time=0.636 ms
    64 bytes from 192.168.137.1: seq=1 ttl=128 time=1.165 ms

    --- 192.168.137.1 ping statistics ---
    2 packets transmitted, 2 packets received, 0% packet loss
    round-trip min/avg/max = 0.636/0.900/1.165 ms

|  "0% packet loss" indicates the test is passed.
|  If "100% packet loss" appears, first confirm that all firewalls on the PC are disabled.

USB Test
----------

USB0_DRD
~~~~~~~~~~

|  Interface Silkscreen: CON22
|  Test Description: Test the read/write functionality of USB0_DRD by plugging/unplugging a USB storage device (USB flash drive) and using commands.

**HOST Mode Test:**

|  Test Operations:

1. Insert the USB device into the USB port on the baseboard. The system will output information similar to the following:

.. code-block:: shell

    [ 7546.482276] sunxi_set_cur_vol_work()422 WARN: get power supply failed
    [ 7546.489555] sunxi_set_cur_vol_work()422 WARN: get power supply failed
    [ 7547.772538] 
    [ 7547.772538] rmmod_device_driver
    [ 7547.772538] 
    [ 7547.779396] rmmod_device_driver()223 WARN: get power supply failed
    [ 7547.786585] 
    [ 7547.786585] insmod_host_driver
    [ 7547.786585] 
    [ 7547.793319] [ehci0-controller]: sunxi_usb_enable_ehci
    [ 7547.799042] [sunxi-ehci0]: probe, pdev->name: 4101000.ehci0-controller, sunxi_ehci: 0xc0c92388, 0x:d1f41000, irq_no:3e
    [ 7547.811352] sunxi-ehci 4101000.ehci0-controller: 4101000.ehci0-controller supply hci not found, using dummy regulator
    [ 7547.823932] android_work: did not send uevent (0 0 00000000)
    [ 7547.830384] sunxi-ehci 4101000.ehci0-controller: EHCI Host Controller
    [ 7547.837675] sunxi-ehci 4101000.ehci0-controller: new USB bus registered, assigned bus number 3
    [ 7547.848149] sunxi-ehci 4101000.ehci0-controller: irq 62, io mem 0x04101000
    [ 7547.884737] sunxi-ehci 4101000.ehci0-controller: USB 2.0 started, EHCI 1.00
    [ 7547.893595] hub 3-0:1.0: USB hub found
    [ 7547.897942] hub 3-0:1.0: 1 port detected
    [ 7547.903099] [ohci0-controller]: sunxi_usb_enable_ohci
    [ 7547.908849] [sunxi-ohci0]: probe, pdev->name: 4101400.ohci0-controller, sunxi_ohci: 0xc0c92638
    [ 7547.918891] sunxi-ohci 4101400.ohci0-controller: 4101400.ohci0-controller supply hci not found, using dummy regulator
    [ 7547.921210] sunxi-ehci 4101000.ehci0-controller: ehci_irq: highspeed device connect
    [ 7547.931381] sunxi-ohci 4101400.ohci0-controller: OHCI Host Controller
    [ 7547.946708] sunxi-ohci 4101400.ohci0-controller: new USB bus registered, assigned bus number 4
    [ 7547.956934] [sound  403][MACH simple_parse_of] simple_dai_link_of failed
    [ 7547.964762] debugfs: Directory 'sunxi-ohci' with parent 'ohci' already present!
    [ 7547.973064] sunxi-ohci 4101400.ohci0-controller: irq 63, io mem 0x04101400
    [ 7548.049743] hub 4-0:1.0: USB hub found
    [ 7548.054035] hub 4-0:1.0: 1 port detected
    [ 7548.059941] [sound  403][MACH simple_parse_of] simple_dai_link_of failed
    [ 7548.264735] usb 3-1: new high-speed USB device number 2 using sunxi-ehci
    [ 7548.466532] usb-storage 3-1:1.0: USB Mass Storage device detected
    [ 7548.479245] scsi host0: usb-storage 3-1:1.0
    [ 7548.494584] [sound  403][MACH simple_parse_of] simple_dai_link_of failed
    [ 7549.515526] scsi 0:0:0:0: Direct-Access     General  UDisk            5.00 PQ: 0 ANSI: 2
    [ 7549.528712] sd 0:0:0:0: [sda] 1966080 512-byte logical blocks: (1.01 GB/960 MiB)
    [ 7549.539317] sd 0:0:0:0: [sda] Write Protect is off
    [ 7549.547711] sd 0:0:0:0: [sda] Mode Sense: 0b 00 00 08
    [ 7549.557376] sd 0:0:0:0: [sda] No Caching mode page found
    [ 7549.563355] sd 0:0:0:0: [sda] Assuming drive cache: write through
    [ 7549.635368]  sda:
    [ 7549.648386] sd 0:0:0:0: [sda] Attached SCSI removable disk
    create /dev/sda[ 7549.655125][sound  403][MACH simple_parse_of] simple_dai_link_of failed

    [ 7549.736630] FAT-fs (sda): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

2. Enter the following command to check the mount path:

.. code-block:: shell

    df -h

.. code-block:: shell

    /dev/sda                959.7M     48.0K    959.7M   0% /mnt/usb/sda

3. Enter the following command to check the current mode of USB_DRD:

.. code-block:: shell

    cat /sys/bus/platform/drivers/otg\ manager/soc\@3000000\:usbc0\@0/otg_role

4. Enter the following command to test the write speed of the USB0_DRD interface:

.. code-block:: shell

    echo 3 > /proc/sys/vm/drop_caches
    time dd if=/dev/zero of=/dev/sda bs=1024K count=10

.. code-block:: shell

    10+0 records in
    10+0 records out

    real        0m0.080s
    user        0m0.000s
    sys        0m0.069s

|  Here, a total of 10 MByte of test data is written to the solid-state drive via the USB_DRD interface.

5. Enter the following command to test the read speed of the USB0_DRD interface:

.. code-block:: shell

    echo 3 > /proc/sys/vm/drop_caches
    time dd if=/dev/sda of=/dev/null bs=1024K count=10

.. code-block:: shell

    10+0 records in
    10+0 records out

    real        0m1.412s
    user        0m0.000s
    sys        0m0.056s

|  Here, a total of 10 MByte of test data is read from the solid-state drive via the USB_DRD interface.

6. Unplug the USB device from the baseboard. The system will output information similar to the following:

.. code-block:: shell

    [ 8667.889791] sunxi-ehci 4101000.ehci0-controller: ehci_irq: highspeed device disconnect
    [ 8668.898778] 
    [ 8668.898778] rmmod_host_driver
    [ 8668.898778] 
    [ 8668.905441] [ehci0-controller]: sunxi_usb_disable_ehci
    [ 8668.911201] [sunxi-ehci0]: remove, pdev->name: 4101000.ehci0-controller, sunxi_ehci: 0xc0c92388
    [ 8668.921004] sunxi-ehci 4101000.ehci0-controller: remove, state 1
    [ 8668.927773] usb usb3: USB disconnect, device number 1
    remove /dev/sda
    [ 8668.968046] FAT-fs (sda): unable to read boot sector to mark fs as dirty
    [ 8669.039104] sunxi-ehci 4101000.ehci0-controller: USB bus 3 deregistered
    [ 8669.047150] [ohci0-controller]: sunxi_usb_disable_ohci
    [ 8669.052958] [sunxi-ohci0]: remove, pdev->name: 4101400.ohci0-controller, sunxi_ohci: 0xc0c92638
    [ 8669.062813] sunxi-ohci 4101400.ohci0-controller: remove, state 4
    [ 8669.069636] usb usb4: USB disconnect, device number 1
    [ 8669.077208] sunxi-ohci 4101400.ohci0-controller: USB bus 4 deregistered
    [ 8669.085233] 
    [ 8669.085233] insmod_device_driver

**DEVICE Mode Test**

|  Test Operations:

1. Use a USB-to-Type-C data cable to connect the development board's usb0_drd to the PC's host interface. The system will output information similar to the following:

.. code-block:: shell

    [ 8694.440072] sunxi_set_cur_vol_work()422 WARN: get power supply failed
    [ 8694.526975] android_work: sent uevent USB_STATE=CONNECTED
    [ 8694.562395] configfs-gadget gadget: high-speed config #1: c
    [ 8694.569522] android_work: sent uevent USB_STATE=CONFIGURED

2. Enter the following command to check the current mode of USB_DRD:

.. code-block:: shell

    cat /sys/bus/platform/drivers/otg\ manager/soc\@3000000\:usbc0\@0/otg_role

3. Copy the otg.sh script file to the opt directory of the evaluation board's file system. Enter the following command to virtualize a 10 MByte DDR memory space of the evaluation board as a USB flash drive:

.. code-block:: shell

    ./opt/otg.sh

.. code-block:: shell

    10+0 records in
    10+0 records ou[  372.235549] android_work: sent uevent USB_STATE=DISCONNECTED
    t
    Cleaning up old configurations...
    [  372.243721] android_work: did not send uevent (0 0 00000000)
    Creating new configurations...

    USB Mass Storage Gadget activated
    # [  373.443261] sunxi_set_cur_vol_work()422 WARN: get power supply failed
    [  373.529838] android_work: sent uevent USB_STATE=CONNECTED
    [  374.663250] configfs-gadget gadget: high-speed config #1: c
    [  374.669936] android_work: sent uevent USB_STATE=CONFIGURED
    
4. Disconnect the USB-to-Type-C data cable from the PC host and the development board interface. The system will output information similar to the following:

.. code-block:: shell

    [ 8713.914725] sunxi_vbus_det_work()3439 WARN: get power supply failed
    [ 8713.922030] android_work: sent uevent USB_STATE=DISCONNECTED
    
USB1_HOST
~~~~~~~~~~~

|  Interface Silkscreen: CON22
|  Test Description: Test the read/write functionality of USB1_HOST by plugging/unplugging a USB storage device (USB flash drive) and using commands.
|  Test Operations:

1. Insert the USB device into the USB port on the baseboard. The system will output information similar to the following:

.. code-block:: shell

    [ 8286.514156] usb 1-1.1: new high-speed USB device number 5 using sunxi-ehci
    [ 8286.666092] usb-storage 1-1.1:1.0: USB Mass Storage device detected
    [ 8286.678608] scsi host0: usb-storage 1-1.1:1.0
    [ 8286.685232] [sound  403][MACH simple_parse_of] simple_dai_link_of failed
    [ 8287.755033] scsi 0:0:0:0: Direct-Access     General  UDisk            5.00 PQ: 0 ANSI: 2
    [ 8287.768294] sd 0:0:0:0: [sda] 1966080 512-byte logical blocks: (1.01 GB/960 MiB)
    [ 8287.782858] sd 0:0:0:0: [sda] Write Protect is off
    [ 8287.788529] sd 0:0:0:0: [sda] Mode Sense: 0b 00 00 08
    [ 8287.795011] sd 0:0:0:0: [sda] No Caching mode page found
    [ 8287.800995] sd 0:0:0:0: [sda] Assuming drive cache: write through
    [ 8287.845122]  sda:
    [ 8287.861123] sd 0:0:0:0: [sda] Attached SCSI removable disk
    create /dev/sda
    [ 8287.868032] [sound  403][MACH simple_parse_of] simple_dai_link_of failed
    [ 8287.978121] FAT-fs (sda): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.

2. Enter the following command to check the mount path:

.. code-block:: shell

    df -h

.. code-block:: shell

    /dev/sda                959.7M     48.0K    959.7M   0% /mnt/usb/sda

3. Enter the following command to test the write speed of the USB1_HOST interface:

.. code-block:: shell

    echo 3 > /proc/sys/vm/drop_caches
    time dd if=/dev/zero of=/dev/sda bs=1024K count=10

.. code-block:: shell

    10+0 records in
    10+0 records out

    real        0m0.082s
    user        0m0.000s
    sys        0m0.071s

|  Here, a total of 10 MByte of test data is written to the solid-state drive via the USB_HOST interface.

4. Enter the following command to test the read speed of the USB1_HOST interface:

.. code-block:: shell

    echo 3 > /proc/sys/vm/drop_caches
    time dd if=/dev/sda of=/dev/null bs=1024K count=10

.. code-block:: shell

    10+0 records in
    10+0 records out

    real        0m1.412s
    user        0m0.000s
    sys        0m0.054s

|  Here, a total of 10 MByte of test data is read from the solid-state drive via the USB_HOST interface.

5. Unplug the USB device from the baseboard. The system will output information similar to the following:

.. code-block:: shell

    [ 9655.558077] usb 1-1.1: USB disconnect, device number 7
    remove /dev/sda
    [ 9655.629385] FAT-fs (sda): unable to read boot sector to mark fs as dirty

Serial Port Test
------------------

RS232 UART2 Serial Port
~~~~~~~~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON9
|  Test Description: Use an RS232 cross serial female-to-female cable and a USB-to-RS232 male serial cable to connect to the PC for transmit and receive tests.
|  Test Operations:

1. Use an RS232 cross serial female-to-female cable and a USB-to-RS232 male serial cable to connect the development board to the PC.
2. Use Xshell to open the corresponding serial port, set the baud rate to 115200, data bits to 8, and stop bits to 1.
3. Enter the following commands to send a message to the RS232 serial port:

.. code-block:: shell

    stty -F /dev/ttyS2 ispeed 115200 ospeed 115200 cs8
    echo Myzr > /dev/ttyS2                                //Send data to the upper computer

|  You can see "Myzr" output on the RS232 serial port terminal.

4. Enter the following command to receive messages from the RS232 serial port:

.. code-block:: shell

    cat /dev/ttyS2

|  On the RS232 serial port terminal, enter "123" directly. The board outputs the result:

.. code-block:: shell

    123

|  Press Ctrl + C to terminate the test command.

TTL UART4, TTL UART5 Serial Ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON10, CON11
|  Test Description: Connect the PC to the development board interface via a USB-to-TTL module and Dupont wires for transmit and receive tests.
|  Test Operations:

1. Connect the PC interface to the development board interface using a USB-to-TTL module and Dupont wires.
2. Use Xshell to open the corresponding serial port, set the baud rate to 115200, data bits to 8, and stop bits to 1.
3. Enter the following commands to send a message to the TTL UART4 serial port:

.. code-block:: shell

    stty -F /dev/ttyS4 ispeed 115200 ospeed 115200 cs8
    echo Myzr > /dev/ttyS4                                //Send data to the upper computer

|  You can see "Myzr" output on the TTL UART4 serial port terminal.

4. Enter the following command to receive messages from the TTL UART4 serial port:

.. code-block:: shell

    cat /dev/ttyS4

|  On the TTL UART4 serial port terminal, enter "123" directly. The board outputs the result:

.. code-block:: shell

    123

|  Press Ctrl + C to terminate the test command.

5. To test TTL UART5, replace "ttyS4" with "ttyS5".

RS485 UART1, RS485 UART5 Serial Ports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: J3
|  Test Description: Connect the PC to the development board interface via a USB-to-RS485 module for transmit and receive tests.
|  Test Operations:

1. Connect the PC interface to the development board interface using a USB-to-RS485 module and Dupont wires.
2. Use Xshell to open the corresponding serial port, set the baud rate to 115200, data bits to 8, and stop bits to 1.
3. Enter the following commands to send a message to the RS485 UART1 serial port:

.. code-block:: shell

    stty -F /dev/ttyS1 ispeed 115200 ospeed 115200 cs8
    echo Myzr > /dev/ttyS1                                //Send data to the upper computer

|  You can see "Myzr" output on the RS485 UART1 serial port terminal.

4. Enter the following command to receive messages from the RS485 UART1 serial port:

.. code-block:: shell

    cat /dev/ttyS1

|  On the RS485 UART1 serial port terminal, enter "123" directly. The board outputs the result:

.. code-block:: shell

    123

|  Press Ctrl + C to terminate the test command.

5. To test RS485 UART3, replace "ttyS1" with "ttyS3".


CAN
-----

|  Interface Silkscreen: J3
|  Test Description: Use Dupont wires to connect two sets of CAN buses and test by sending and receiving data mutually.
|  Test Operations:

1. Use Dupont wires to connect the CAN0 interface and CAN1 interface to each other.
2. Enter the following commands in the terminal to configure CAN0 and CAN1:

.. code-block:: shell

    ip link set awlink0 down
    ip link set awlink0 type can bitrate 1000000
    ip link set awlink0 up

    ip link set awlink1 down
    ip link set awlink1 type can bitrate 1000000
    ip link set awlink1 up

|  If information similar to the following is displayed in the terminal, the activation is successful:

.. code-block:: shell

    link becomes ready

3. Enter the following commands in the terminal to enable CAN0 and CAN1 to receive data in the background:

.. code-block:: shell

    candump awlink0 &
    candump awlink1 &

4. Enter the following command in the serial port terminal to make CAN0 (or CAN1) send test data:

|  Enter the command:

.. code-block:: shell

    cansend awlink0 123#1122334455667788

|  Received messages:

.. code-block:: shell

  awlink0  123   [8]  11 22 33 44 55 66 77 88
  awlink1  123   [8]  11 22 33 44 55 66 77 88


TF Card
----------

TF Card Insertion Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON7
|  Test Description: Insert a TF card and check if the device can recognize the card correctly.
|  Test Operations:

1. Prepare a TF card and insert it into the Micro SD interface of the development board. The following similar information will be output:

.. code-block:: shell

    [  107.514984] sunxi-mmc 4020000.sdmmc: sdc set ios:clk 0Hz bm PP pm UP vdd 21 width 1 timing LEGACY(SDR12) dt B
    [  107.526272] sunxi-mmc 4020000.sdmmc: no vqmmc,Check if there is regulator
    [  107.546435] sunxi-mmc 4020000.sdmmc: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [  107.570689] sunxi-mmc 4020000.sdmmc: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [  107.585329] sunxi-mmc 4020000.sdmmc: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [  107.599254] sunxi-mmc 4020000.sdmmc: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [  107.613896] sunxi-mmc 4020000.sdmmc: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [  107.819966] mmc1: host does not support reading read-only switch, assuming write-enable
    [  107.832034] sunxi-mmc 4020000.sdmmc: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing SD-HS(SDR25) dt B
    [  107.843671] sunxi-mmc 4020000.sdmmc: sdc set ios:clk 50000000Hz bm PP pm ON vdd 21 width 1 timing SD-HS(SDR25) dt B
    [  107.855525] sunxi-mmc 4020000.sdmmc: sdc set ios:clk 50000000Hz bm PP pm ON vdd 21 width 4 timing SD-HS(SDR25) dt B
    [  107.867332] mmc1: new high speed SDHC card at address aaaa
    [  107.874744] mmcblk1: mmc1:aaaa SD32G 29.7 GiB 
    [  107.884002]  mmcblk1: p1 p2 p3 p4 p5 p6 p7 p8

2. Enter the command to view TF card information:

.. code-block:: shell

    fdisk -l

TF Card Read/Write Test
~~~~~~~~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON7
|  Test Description: Insert a TF card and use commands to test the read/write functionality of the Micro SD interface.
|  Test Operations:

1. Enter the command to format the unused space of the TF card:

.. code-block:: shell

    mkfs.ext4 /dev/mmcblk1p8

|  The following similar information is output, indicating successful formatting:

.. code-block:: shell

    mke2fs 1.44.5 (15-Dec-2018)
    Creating filesystem with 7506559 4k blocks and 1876800 inodes
    Filesystem UUID: 9c080811-bd02-47a3-8f31-01ea7ad2268c
    Superblock backups stored on blocks: 
            32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
            4096000

    Allocating group tables: done                            
    Writing inode tables: done                            
    Creating journal (32768 blocks): done
    Writing superblocks and filesystem accounting information: remove /dev/mmcblk1p8
    done

2. Enter the commands to create a directory and mount the partition:

.. code-block:: shell

    mkdir -p /run/media/mmcblk1p8
    mount /dev/mmcblk1p8 /run/media/mmcblk1p8

|  Output Information:

.. code-block:: shell

    [ 1023.996843] EXT4-fs (mmcblk1p8): mounted filesystem with ordered data mode. Opts: (null)

3. Enter the command to test the write speed of the Micro SD interface:

.. code-block:: shell

    echo 3 > /proc/sys/vm/drop_caches
    time dd if=/dev/zero of=/run/media/mmcblk1p8/test bs=1024K count=10 conv=fsync

|  Output Information:

.. code-block:: shell

    10+0 records in
    10+0 records out

    real        0m0.731s
    user        0m0.001s
    sys        0m0.116s

4. Enter the command to test the read speed of the Micro SD interface:

.. code-block:: shell

    echo 3 > /proc/sys/vm/drop_caches
    time dd if=/run/media/mmcblk1p8/test of=/dev/null bs=1024K

|  Output Information:

.. code-block:: shell

    10+0 records in
    10+0 records out

    real        0m0.463s
    user        0m0.000s
    sys        0m0.036s

5. After completing the test, execute the following commands to unmount the mounted partition:

.. code-block:: shell

    umount /run/media/mmcblk1p8/
    rm -r /run/media/mmcblk1p8


HDMI OUT Test
---------------

|  Interface Silkscreen: CON17
|  Test Operations: Connect the development board to a display using an HDMI cable and check if the display shows an image. If an image is displayed, the function is normal.

WIFI Test
-----------

|  Interface Silkscreen: CON24
|  Test Description: Connect a 2.4G antenna to the WIFI (CON24) interface of the development board. Verify the normal connection by sending ICMP packets from the development board to the external network.
|  Test Operations:

1. Execute the following commands to disable other networks:

.. code-block:: shell

    ifconfig eth0 down
    ifconfig eth1 down

|  Enter the command to enable WIFI:

.. code-block:: shell

    ifconfig wlan0 up

2. Add the wifi_setup.sh file to the file system and execute the following command:

.. code-block:: shell

    ./wifi_setup.sh -i MY-WIFI -p My202412

|  Where "-i" specifies the WIFI name and "-p" specifies the WIFI password. Modify them according to the actual situation.

|  Output information similar to the following:

.. code-block:: shell

    udhcpc: sending discover
    [  169.754845] RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0800) rate=0x0 SeqNum = 6
    udhcpc: sending select for 192.168.61.215
    [  170.834775] RTW: rtl8723d_fill_default_txdesc(wlan0): SP Packet(0x0800) rate=0x0 SeqNum = 9
    udhcpc: lease of 192.168.61.215 obtained, lease time 86400
    deleting routers
    adding dns 192.168.60.1
    wifi setup successfully!

3. Connection Test

|  Execute the following command to test if the network function is normal:

.. code-block:: shell

    ping -I wlan0 www.baidu.com

|  Output Information:

.. code-block:: shell

    64 bytes from 183.2.172.17: seq=0 ttl=54 time=27.760 ms
    64 bytes from 183.2.172.17: seq=1 ttl=54 time=17.046 ms
    64 bytes from 183.2.172.17: seq=2 ttl=54 time=15.300 ms
    64 bytes from 183.2.172.17: seq=3 ttl=54 time=34.486 ms

Bluetooth Test
----------------

|  Interface Silkscreen: CON24
|  Test Description: After scanning for Bluetooth devices, send an L2CAP response request and receive the reply.
|  Test Operations:

1. Add the rtl8723du_config file and rtl8723du_fw file to the /lib/firmware path in the file system.
2. Enter the following commands to start Bluetooth and check if it starts successfully:

.. code-block:: shell

    hciconfig hci0 up
    hciconfig

3. Enter the following command to scan for external Bluetooth devices:

.. code-block:: shell

    hcitool scan

|  Output information similar to the following:

.. code-block:: shell

    Scanning ...
    [  771.975134] rtk_btcoex: hci (periodic)inq start
    [  782.224170] rtk_btcoex: inquiry complete
            E8:5C:5F:B5:7A:11        BlueZ 5.77
            40:45:A0:49:3B:1A        chensz

4. Send an L2CAP packet for testing:

|  Enter the command:

.. code-block:: shell

    l2ping 40:45:A0:49:3B:1A

|  Output information similar to the following:

.. code-block:: shell

    Ping: 40:45:A0:49:3B:1A from FC:23:CD:29:9B:99 (data size 44) ...
    44 bytes from 40:45:A0:49:3B:1A id 0 time 8.75ms
    44 bytes from 40:45:A0:49:3B:1A id 1 time 54.76ms
    44 bytes from 40:45:A0:49:3B:1A id 2 time 173.62ms
    ^C3 sent, 3 received, 0% loss

|  "0% packet loss" indicates the Bluetooth connection is normal.

RTC
-----

|  Interface Silkscreen: CON6
|  Test Description: First read the RTC time, then set the RTC time, and check the RTC time again after powering off and restarting.
|  Test Operations:

1. Enter the command to view the external RTC device node:

.. code-block:: shell

    ls /dev/rtc*

|  Output Information:

.. code-block:: shell

    /dev/rtc   /dev/rtc0

2. Enter the command to read the current RTC time:

.. code-block:: shell

    hwclock -f /dev/rtc

3. Enter the command to set the RTC time:

.. code-block:: shell

    date -s "2023-02-06 12:34:56"

|  Output Information:

.. code-block:: shell

    Mon Feb  6 12:34:56 UTC 2023

|  The system time is successfully updated to the set time.

4. Enter the commands to synchronize the system clock to the RTC clock and check:

.. code-block:: shell
    
    hwclock --systohc -u
    hwclock -u

5. Enter the command to synchronize the RTC clock as the system clock:

.. code-block:: shell

    hwclock --hctosys -u

6. Power off and restart the device.
7. Enter the command to check the RTC time:

.. code-block:: shell

    hwclock -f /dev/rtc

Audio
-------

HP OUT/MIC IN Interface Test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON19
|  Test Description: Use a 3.5mm headphone with a microphone to connect to the HP OUT/MIC IN interface on the development board for playback and recording tests.
|  Test Operations:

1. Insert the headphone into the interface corresponding to the silkscreen CON19.
2. Add the mic_in_test.sh file to the system files.
3. Enter the command to perform the recording test:

.. code-block:: shell

    ./mic_in_test.sh

4. Enter the command to perform the playback test:

.. code-block:: shell

    aplay -Dhw:audiocodec -vv test.wav

|  If sound can be heard from the headphones, the function is normal.

LINE IN Interface Test
~~~~~~~~~~~~~~~~~~~~~~~~

|  Interface Silkscreen: CON18
|  Test Description: Use a 3.5mm audio cable with male connectors on both ends to connect the development board to an audio player. Insert headphones into the HP OUT/MIC IN interface for playback testing.
|  Test Operations:

1. Prepare a 3.5mm audio cable with male connectors on both ends. Connect one end to the LINE IN interface of the evaluation board and the other end to an audio player (mobile phone or PC) that is playing audio. Connect headphones to the HP OUT/MIC IN interface.
2. Add the line_in_test.sh file to the system files.
3. Enter the command to perform the playback test:

.. code-block:: shell

    ./line_in_test.sh

|  If audio plays normally through the headphones, the function is normal.

4G Module
------------

|  Interface Silkscreen: CON25
|  Test Description: After the 4G connection is successful, verify the normal connection by sending ICMP packets from the development board to the external network.
|  Test Operations:

1. Prepare a 4G module, insert it into the 4G module interface of the development board, and enter the command to find usb0:

.. code-block:: shell

    ifconfig -a

2. Add the quectel-CM file to the file system and enter the commands to obtain an IP address and enable usb0:

.. code-block:: shell

    ./quectel-CM &
    ifconfig usb0 up

3. Enter the command to test the network connection:

.. code-block:: shell

    ping -I usb0 www.baidu.com

|  Output Information:

.. code-block:: shell

    PING www.baidu.com (183.240.99.58): 56 data bytes
    64 bytes from 183.240.99.58: seq=0 ttl=52 time=119.380 ms
    64 bytes from 183.240.99.58: seq=1 ttl=53 time=49.178 ms
    64 bytes from 183.240.99.58: seq=2 ttl=53 time=40.013 ms
    64 bytes from 183.240.99.58: seq=3 ttl=53 time=48.857 ms
    64 bytes from 183.240.99.58: seq=4 ttl=53 time=51.461 ms
    64 bytes from 183.240.99.58: seq=5 ttl=53 time=49.446 ms
    64 bytes from 183.240.99.58: seq=6 ttl=53 time=49.273 ms
    64 bytes from 183.240.99.58: seq=7 ttl=53 time=39.126 ms
    64 bytes from 183.240.99.58: seq=8 ttl=53 time=48.990 ms
    ^C
    --- www.baidu.com ping statistics ---
    9 packets transmitted, 9 packets received, 0% packet loss

|  "0% packet loss" indicates the 4G connection is normal.

GPIO
------

|  Interface Silkscreen: CON26
|  Test Description: Control the GPIO to output high and low levels through commands.
|  Test Operations:

1. First obtain the pin name and calculate the GPIO number. TX and RX use PC0 and PC1 respectively, with GPIO numbers 64 and 65.
2. Enter the command to mount debugfs:

.. code-block:: shell

    mount -t debugfs none /sys/kernel/debug

3. Enter the commands to export the GPIO pin and set it to output mode:

.. code-block:: shell

    echo 64 > /sys/class/gpio/export
    echo out > /sys/class/gpio/gpio64/direction

4. Enter the command to control the GPIO pin to output high level:

.. code-block:: shell

    echo 1 > /sys/class/gpio/gpio64/value

5. Enter the command to control the GPIO pin to output low level:

.. code-block:: shell

    echo 0 > /sys/class/gpio/gpio64/value

|  During the test operation, if the read level matches the expected correct level, the function is normal.