Platform Introduction
=======================

Product Overview
------------------

- **Chip Architecture**: Adopts a multi-core heterogeneous design with three Cortex-A7 cores (up to 1.5GHz) + one Cortex-M0 core, combining high performance and real-time capabilities to meet the needs of different tasks.
- **Process Technology**: Utilizes an advanced 22nm process. Under full-load operation (CPU overclocked to 1.6GHz, DDR at 800MHz), the SoC power consumption is less than 650mW, and the temperature rise at room temperature is less than 17℃. Its excellent low-power characteristics provide long-lasting battery life for handheld devices, edge nodes, and other applications.
- **Industrial-Grade Features**: Supports wide-temperature operation from -40℃ to 85℃, and has passed rigorous tests such as electromagnetic compatibility (EMC) and high-temperature/high-humidity aging tests. It possesses industrial-grade reliability and can adapt to complex and harsh industrial environments.
- **Rich Interfaces**:
  - **Network Interfaces**: Integrates two 100Mbps Ethernet ports and supports the IEEE1588 protocol, suitable for industrial network communication.
  - **Storage Interfaces**: Supports various storage devices, such as SPI Flash and eMMC.
  - **Audio Interfaces**: Includes 5×SAI, 1×ADC, 2×DSM, etc., supporting multiple audio functions.
  - **Other Interfaces**: Features 2×USB2.0 OTG, 6×UART, 2×CAN FD, 3×SPI, 3×I2C, etc., to meet the connection requirements of different devices.
- **Low-Latency Response**: Supports the AMP multi-core heterogeneous architecture and adopts the standard RPMSG inter-core communication mechanism, enabling the system to achieve microsecond-level interrupt response latency (<5us). Under the stress test with stress-ng, the real-time latency of system scheduling can reach 60+us; for systems based on the EtherCAT IgH and CODESYS protocols, the jitter latency is approximately 90us when the control cycle is 1ms, supporting 8-axis bus control.
- **Display and Graphics Processing**: Built-in 2D hardware engine and display output engine, supporting display interfaces such as MIPI-DSI and RGB. The maximum output resolution is 1280×1280@60fps, which can meet the needs of image display and simple graphics processing.
- **System Support**: Natively supports Linux Kernel 6.1 and is compatible with distributions such as Buildroot, Debian, and Ubuntu. It realizes the RTOS SMP mode on the Rockchip platform for the first time and supports flexible scheduling of the AMP multi-core heterogeneous system.
- **Boot Speed**: The SDK natively supports the LVGL lightweight UI framework. Combined with the 2D hardware acceleration inside the chip, the LVGL runs more smoothly. After full-link boot optimization, the device can start up in less than 2.5 seconds.

Target Applications
---------------------

- **Smart Home Appliances**: The ultra-low power consumption of this processor can meet the long-term operation needs of smart home appliances, and the integrated voice algorithm can enhance the voice interaction experience. For example, the display and control modules of smart home appliances such as smart refrigerators, air conditioners, and washing machines can realize functions such as voice control, status display, and intelligent networking, providing users with a more convenient and intelligent experience.
- **Industrial Control**: In the field of industrial control, the RK3506 can be used in devices such as industrial gateways, PLCs (Programmable Logic Controllers), and HMIs (Human-Machine Interfaces). It supports two 100Mbps Ethernet ports and a variety of industrial protocols, helping industrial devices achieve interconnection and intercommunication; its multi-core heterogeneous architecture and low-latency response characteristics can meet the needs of real-time tasks such as PLC control and EtherCAT, accurately controlling devices like servo motors to achieve efficient and stable industrial automation control.
- **Handheld Terminals**: For handheld POS devices, handheld industrial terminals, etc., the RK3506 has an operating power consumption of only 200mW, providing excellent portability. Its long battery life can meet the needs of scenarios such as mobile payments, on-site data collection, and logistics distribution. At the same time, its full-process security hardening solution can also ensure data security and transaction reliability.
- **Building Intercom**: Can be applied to indoor units and door stations of building intercom systems, providing efficient graphics rendering capabilities and a smooth UI interface. It supports functions such as video calls, access control, and visitor management, providing support for building safety management and residents' convenient lives.
- **Video and Audio Players**: Supports 720P video software decoding and integrated audio algorithms, suitable for small devices with certain requirements for audio and video playback, such as portable media players and digital signs, and can provide clear video images and high-quality audio effects.

Key Features
---------------

- **Multi-Core Heterogeneous Architecture**: Adopts a multi-core heterogeneous design with three Cortex-A7 cores (up to 1.5GHz) + one Cortex-M0 core, combining high performance and real-time capabilities. Among them, the A7 cores handle complex tasks, while the M0 core handles tasks with high real-time requirements, such as sensor data collection and real-time control.
- **Industrial-Grade Reliability**: Supports wide-temperature operation from -40℃ to 85℃, and has passed rigorous tests such as electromagnetic compatibility (EMC) and high-temperature/high-humidity aging tests, enabling it to adapt to complex industrial environments.
- **Ultra-Low Latency Response**: The AMP multi-core heterogeneous design achieves microsecond-level response for A cores and nanosecond-level response for the M0 core, meeting the needs of real-time tasks such as PLC control and EtherCAT. Under the stress test with stress-ng, the real-time latency of system scheduling can reach 60+us; for systems based on the EtherCAT IgH and CODESYS protocols, the jitter latency is approximately 90us when the control cycle is 1ms.
- **Low Power Consumption**: Uses an advanced 22nm process, with full-load power consumption of less than 0.7W and a temperature rise of less than 17℃ at room temperature, providing long-lasting battery life for handheld devices and edge nodes.
- **SparkLink Technology Support**: Supports SparkLink technology, which combines the advantages of low-power Bluetooth and high-throughput Wi-Fi, providing a low-latency, high-reliability, and strong anti-interference wireless connection solution for the industrial Internet of Things (IIoT).
- **Full-Link Fast Boot**: Through the optimization of the LVGL lightweight UI framework and full-link boot acceleration, the device can start up in less than 3 seconds, improving the response efficiency of industrial devices.
- **Multi-System Support and Developer-Friendliness**: Natively supports Linux Kernel 6.1 and is compatible with distributions such as Buildroot, Debian, and Ubuntu. It realizes the RTOS SMP mode on the Rockchip platform for the first time and supports flexible scheduling of the AMP multi-core heterogeneous system.
- **Rich Interfaces**: Integrates industrial-grade interfaces such as two 100Mbps Ethernet ports, 2-channel CAN FD, 6-channel UART (some interfaces are multiplexed), and USB 2.0 OTG. It also has a built-in 2D hardware acceleration engine and supports display output with a resolution of 1280×1280, meeting the needs of HMI human-computer interaction and multi-device collaboration.

Processor Block Diagram
-------------------------

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3506-EK134/处理器框图.png
   :alt: 处理器框图.png


Processor Characteristics
---------------------------

**Detailed Parameters**

+----------------------+------------------------------------------------------+
| Component            | Specifications                                       |
+----------------------+------------------------------------------------------+
| CPU                  | Triple Cortex-A7, maximum frequency up to 1.5GHz     |
+----------------------+------------------------------------------------------+
| MCU                  | Single-core Cortex-M0, 200MHz                        |
+----------------------+------------------------------------------------------+
| GPU                  | 2D Graphic Engine                                    |
+----------------------+------------------------------------------------------+
| DDR                  | DDR2/DDR3/DDR3L 16bit (Embedded 128MB DDR)           |
+----------------------+------------------------------------------------------+
| Display              | MIPI/RGB24/QSPI                                      |
+----------------------+------------------------------------------------------+
| Audio Interfaces     | 1×ADC, 2×DSM, 3×SAI, 5×SAI, 5×PDM                    |
+----------------------+------------------------------------------------------+
| USB                  | 2×USB OTG                                            |
+----------------------+------------------------------------------------------+
| MAC                  | 2×100M MAC                                           |
+----------------------+------------------------------------------------------+
| Expansion Interfaces | UART 6, SPI 3, CAN 2, PWM 12, I2C 3, SARADC 4, SDMMC |
+----------------------+------------------------------------------------------+
| Camera               | DVP (Flexbus)                                        |
+----------------------+------------------------------------------------------+
| Localbus             | DSMC                                                 |
+----------------------+------------------------------------------------------+