GW200(EN)
===========

Product Specification
------------------------

.. figure:: /image/MYZR-其他/网关/GW200/576px-GW200_1.0.0.1.png
   :alt: 576px-GW200_1.0.0.1.png

**Description**

| The product corresponding to this document is GW200.

Product Overview
------------------

Product Introduction
~~~~~~~~~~~~~~~~~~~~~~

| GW200 is a 5G wireless communication gateway applied in industrial fields. It provides RS485/RS232/DI/DO/Gigabit Ethernet interfaces to realize external device control, data collection, data parsing, and transparent transmission. The uplink can connect to servers or the cloud via 5G, Wi-Fi STA, and Ethernet to control terminal devices and collect information. The device meets industrial-grade standards in terms of temperature rating, electrostatic protection, EMC (Electromagnetic Compatibility), and vibration resistance, making it suitable for various harsh industrial environments and enabling highly reliable data transmission.

.. figure:: /image/MYZR-其他/网关/GW200/576px-GW200_1.1.0.1.png
   :alt: 576px-GW200_1.1.0.1.png

**The product is equipped with abundant interfaces**

| 5G: Multi-network standard module, supporting GPS/BeiDou positioning system. 
| Wi-Fi: 2.4G/5G dual-band. It can connect to the Internet while providing an AP (Access Point) for devices to access the gateway wirelessly. 
| Ethernet: Supports WAN and LAN port modes. The WAN port can connect to the Internet, and the LAN port allows external devices to access the gateway. 
| RS232/RS485: Used to connect external devices, supporting data collection, transparent transmission, or parsing. 
| DI/DO: DI (Digital Input) can be used to detect signals from external devices or sensors; DO (Digital Output) can be used to control the on/off status of external devices. 
| USB/TF Card: Used to connect external storage devices for backing up device data.

Product Features
~~~~~~~~~~~~~~~~~~

**High Performance and High Throughput**

| The product adopts a Cortex-A53 core 64-bit processor with a performance of over 4000 CoreMarks. The processor's packet forwarding engine can support packets ranging from 64 bytes to 10,240 bytes, and can independently process all packets of a specified flow without the intervention of the processor. It can meet the application requirements of high-data-volume and high-performance industrial environments.

**5G Network Access**

| Supports 5G network, featuring higher network speed, low latency, high reliability, and low-power massive connections. 
| Supports network standards such as 5G NR, LTE FDD, LTE TDD, and WCDMA to achieve full coverage. 
| Supports NSA (Non-Standalone) and SA (Standalone) modes. 
| The ultra-low latency of 5G enables it to better meet the wide application needs in the field of industrial automatic control. 
| The massive connection capability of 5G makes it more suitable for application in the Internet of Things (IoT).

**Reliable Wi-Fi Function**

| Supports standard 802.11a/b/g/n/ac protocols, 2.4GHz and 5GHz dual bands, 802.11ac 2x2, and is compatible with Wave-2 and MU-MIMO (Multi-User Multiple-Input Multiple-Output). It features stronger and more stable wireless signals, higher anti-interference capability, faster transmission speed, lower latency, and better access capacity, enabling industrial WLAN (Wireless Local Area Network) access applications. 
| The AP function can create a wireless network for other devices to access the gateway. 
| The STA (Station) function allows the gateway to connect to a wireless network, making the application environment not affected by Ethernet wiring and mobile network signal quality.

**Flexible Ethernet Access**

| Supports two 10/100/1000Mbps Ethernet interfaces. The LAN and WAN can be flexibly configured: they can be set as two LAN ports, or one of them can be configured as a WAN port.

**Abundant Data Communication Interfaces**

| To meet the data access needs of various terminal interfaces in industrial environments, the product provides abundant interfaces, including: one TF card interface; one USB port; one isolated RS232 interface; two isolated RS485 interfaces; two groups of isolated DI interfaces; two groups of isolated DO interfaces.

**High Hardware Reliability**

| It has a die-cast aluminum body with high electromagnetic compatibility. It meets industrial-grade standards in terms of electrostatic surge protection, EMC, and vibration resistance. It adopts a wall-mounted installation method, which is easy to install on-site. The LAN port and RS485 interface are built with electromagnetic isolation protection to ensure transmission reliability in industrial environments.

**Local Console Debug Interface Provided**

| The device can be debugged, configured, and managed through the Console interface.

Product Technical Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------+-------------------------------------------------------------------------------------------------------+
|       Product Model       |                                                 GW200                                                 |
+===========================+=======================================================================================================+
| **Basic Information**     |                                                                                                       |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Processor                 | Arm® Cortex®-A53 Core 64-bit MPU                                                                      |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Memory                    | 512MByte                                                                                              |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Storage                   | 4GByte eMMC                                                                                           |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| 5G Frequency Bands        | 5G NR：n1/n2/n3/n5/n7/n8/n12/n20/n28/n41/n66/n71/n77n78/n79                                           |
+                           +-------------------------------------------------------------------------------------------------------+
|                           | LTE FDD：B1/B2/B3/B4/B5/B7/B8/B9/B12/B13/B14/B17/B18/B19 B20/B21(TBD)/B25/B26/B28/B29/B30/B32/B66/B71 |
+                           +-------------------------------------------------------------------------------------------------------+
|                           | LTE TDD：B34/B38/39/B40/B41/B42/B43/B48                                                               |
+                           +-------------------------------------------------------------------------------------------------------+
|                           | WCDMA：B1/B2/B3/B4/B5/B6/B8/B19                                                                       |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Transmission Rate         | 5G SA Sub6：DL 3.3Gbps，UL 250Mbps                                                                    |
+                           +-------------------------------------------------------------------------------------------------------+
|                           | 5G NSA Sub6：DL 3.4Gbps，UL 200Mbps                                                                   |
+                           +-------------------------------------------------------------------------------------------------------+
|                           | LTE：DL 2.0Gbps，UL 150Mbps                                                                           |
+                           +-------------------------------------------------------------------------------------------------------+
|                           | WCDMA：DL 42Mbps，UL 5.76Mbps                                                                         |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Wi-Fi Features            | IEEE Standards: IEEE 802.11a/b/g/n/ac                                                                 |
+                           +-------------------------------------------------------------------------------------------------------+
|                           | Wireless data rate up to 867Mbps                                                                      |
+                           +-------------------------------------------------------------------------------------------------------+
|                           | 802.11ac 2x2, Wave-2 compatible with MU-MIMO                                                          |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Wi-Fi Frequency Bands     | 2.4G：2.4~2.4835GHz                                                                                   |
+                           +-------------------------------------------------------------------------------------------------------+
|                           | 5G：5.150~5.850GHz                                                                                    |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| GNSS                      | GPS/BeiDou                                                                                            |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Power Supply              | 9 ~ 36V                                                                                               |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Operating Temperature     | -40°C ~ 75°C                                                                                          |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Storage Temperature       | -40°C ~ 85°C                                                                                          |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| **Physical Appearance**   |                                                                                                       |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Dimensions                | 200mm (Length) x 135mm (Width) x 35mm (Height), excluding the size of the antenna connector           |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Weight                    | 821.6g                                                                                                |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Case Craft                | Die-cast Aluminum                                                                                     |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Installation Method       | Wall-mounted Installation                                                                             |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Antenna                   | Butterfly-shaped Full-band Antenna                                                                    |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| **Software Features**     |                                                                                                       |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| MYZR Cloud Service        | Supports the device to connect to the MYZR cloud server for device management and control             |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Alibaba Cloud IoT         | Supports the device to connect to Alibaba Cloud IoT                                                   |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Tencent Cloud IoT         | Supports the device to connect to Tencent Cloud IoT                                                   |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Local Configuration       | The device can be configured through local configuration files or configuration tools                 |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| WAN                       | Supports WAN Port Configuration                                                                       |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| LAN                       | Supports LAN Port Configuration                                                                       |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Wi-Fi AP                  | Supports Wi-Fi AP Mode                                                                                |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Wi-Fi STA                 | Supports Wi-Fi STA Mode                                                                               |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Mobile Network Connection | Supports the device to connect to the mobile network                                                  |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| MQTT                      | Supports MQTT Protocol                                                                                |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Modbus                    | Supports Modbus RTU/TCP Protocol                                                                      |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| UART                      | Supports direct sending and receiving of serial port data                                             |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| DI                        | Supports obtaining DI status through SDK                                                              |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| DO                        | Supports controlling DO output through SDK                                                            |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| GNSS                      | Supports obtaining location information through SDK                                                   |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Network Communication     | Supports direct sending and receiving of data through SDK                                             |
+---------------------------+-------------------------------------------------------------------------------------------------------+
| Secondary Development     | Based on the Linux system, customers can carry out secondary development                              |
+                           +                                                                                                       +
|                           | of upper-layer applications according to project requirements                                         |
+---------------------------+-------------------------------------------------------------------------------------------------------+


Product Appearance and Interfaces
-----------------------------------

Product Appearance
~~~~~~~~~~~~~~~~~~~~

**Front View of the Product**

.. figure:: /image/MYZR-其他/网关/GW200/576px-GW200_2.1.1.1.png
   :alt: 576px-GW200_2.1.1.1.png

**Rear View of the Product**

.. figure:: /image/MYZR-其他/网关/GW200/576px-GW200_2.1.2.1.png
   :alt: 576px-GW200_2.1.2.1.png

Product Dimensions
~~~~~~~~~~~~~~~~~~~~

.. figure:: /image/MYZR-其他/网关/GW200/576px-GW200_2.2.0.1.png
   :alt: 576px-GW200_2.2.0.1.png

Product Interfaces
~~~~~~~~~~~~~~~~~~~~

**Front Interfaces of the Product**

.. figure:: /image/MYZR-其他/网关/GW200/576px-GW200_2.3.1.1_1.png
   :alt: 576px-GW200_2.3.1.1_1.png

+--------------------+-------------------------------------------------------------------------------------------+
| Hardware Interface |                                   Interface Description                                   |
+====================+===========================================================================================+
| Power Interface    | DC 5.5mm*2.1mm interface, powered by 9V ~ 36V                                             |
+--------------------+-------------------------------------------------------------------------------------------+
| ETH1               | RJ45 interface, supports 10/100/1000M, default LAN mode                                   |
+--------------------+-------------------------------------------------------------------------------------------+
| ETH0               | RJ45 interface, supports 10/100/1000M, default WAN mode                                   |
+--------------------+-------------------------------------------------------------------------------------------+
| Console Port       | Used for local debugging                                                                  |
+--------------------+-------------------------------------------------------------------------------------------+
| USB Port           | USB Type-A female port, can connect external USB storage devices                          |
+--------------------+-------------------------------------------------------------------------------------------+
| RS232              | 3.81mm pitch Phoenix terminal, can connect external RS232 devices                         |
+--------------------+-------------------------------------------------------------------------------------------+
| RS485              | 3.81mm pitch Phoenix terminal, can connect external RS485 devices, 2 groups of interfaces |
+--------------------+-------------------------------------------------------------------------------------------+
| DO                 | 3.81mm pitch Phoenix terminal, output control, 2 groups of interfaces                     |
+--------------------+-------------------------------------------------------------------------------------------+
| DI                 | 3.81mm pitch Phoenix terminal, input detection, 2 groups of interfaces                    |
+--------------------+-------------------------------------------------------------------------------------------+
| PWR_LED            | Power indicator light, red color                                                          |
+--------------------+-------------------------------------------------------------------------------------------+
| SYS_LED            | System indicator light, green color                                                       |
+--------------------+-------------------------------------------------------------------------------------------+
| 5G_LED             | 5G indicator light, green color                                                           |
+--------------------+-------------------------------------------------------------------------------------------+
| RST_KEY            | Button, system recovery function                                                          |
+--------------------+-------------------------------------------------------------------------------------------+

**Phoenix Terminal Signal Definition**

.. figure:: /image/MYZR-其他/网关/GW200/576px-GW200_2.3.2.1.png
   :alt: 576px-GW200_2.3.2.1.png

**Rear Interfaces of the Product**

.. figure:: /image/MYZR-其他/网关/GW200/576px-GW200_2.3.3.1.png
   :alt: 576px-GW200_2.3.3.1.png

**Packing List**

.. figure:: /image/MYZR-其他/网关/GW200/576px-GW200_2.4.0.1.png
   :alt: 576px-GW200_2.4.0.1.png

**Copyright Statement**

| All Rights Reserved © Zhuhai Mingyuan Zhirui Technology Co., Ltd. Zhuhai Mingyuan Zhirui Technology Co., Ltd. reserves all rights. Without the written permission of Zhuhai Mingyuan Zhirui Technology Co., Ltd., no unit or individual may arbitrarily extract or copy part or all of the content of this document, nor may it spread the content in any form.

| Zhuhai Mingyuan Zhirui Technology Co., Ltd. provides customers with comprehensive technical support. You can contact us through the following methods:
| Tel: 0756-3628023/3628021
| Email: service@myzr.com.cn
| Website: http://www.myzr.com.cn

- The product pictures and technical data in this document are for reference only. Updates will not be notified separately. The right to interpret the specific content belongs to Mingyuan Zhirui.
