Hardware Design Guide
=======================

1. Debug Circuit
------------------

|   The default UART Debug of RV1126B is selected as UART0_RX_M2/UART0_TX_M2 in the PMUIO0 domain, with a default baud rate of 1500000bps.  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw1-1.png
   :alt: hw1-1.png
   :width: 90%

|   Precautions for using the UART interface:

- The IO level of the UART interface on the SoC side must match that of the conversion chip or peripheral chip;
- For the external USB-to-UART adapter chip, it is recommended to take power for VCCIO from the PMUIO0_VCC3V3 power domain of the motherboard to avoid voltage backflow when the SOC is powered off;
- If UART Debug needs to be used, it is recommended to reserve 2.54 pin headers or test points. The UART circuit is shown in the following figure. The series 510 ohm resistor must not be omitted, and a TVS tube should be added to enhance anti-static surge capability and prevent damage to chip pins during development.  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw1-2.png
   :alt: hw1-2.png
   :width: 90%

- Alternatively, the CH340T chip can be used to convert to USB signals.

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw1-3.png
   :alt: hw1-3.png
   :width: 90%

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw1-4.png
   :alt: hw1-4.png
   :width: 90%

2. OTG Circuit
----------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw2-1.png
   :alt: hw2-1.png
   :width: 90%

|   1. Please note to add ESD protection at the interface.
|   2. Add common-mode filtering to improve signal quality.

3. Power Input Circuit
-------------------------

12V Input
~~~~~~~~~~~

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw3-1.png
   :alt: hw3-1.png
   :width: 90%

|   1. This circuit has overvoltage protection, overcurrent protection, and reverse connection prevention.
|   2. There is an LED power indicator.

5V
~~~~

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw3-2.png
   :alt: hw3-2.png
   :width: 90%

|   1. Uses the SY8113BADC DCDC chip.
|   2. Supports a maximum output current of 3A.

3.3V
~~~~~~

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw3-3.png
   :alt: hw3-3.png
   :width: 90%

|   1. Uses the SY8113BADC DCDC chip.
|   2. Supports a maximum output current of 3A.

4. USB—HUB Circuit
--------------------

|   1. Uses the USB2514B chip, which can expand to four USB ports at once.
|   2. Adds an overcurrent protection chip.

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw4-1.png
   :alt: hw4-1.png
   :width: 90%

5. USB3.0
------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw5-1.png
   :alt: hw5-1.png
   :width: 90%

|   1. A 0.1uF capacitor must be added to the TX signal of USB3.0.
|   2. A 2.0R resistor must be connected in series with the USB2.0 signal.
|   3. Overcurrent protection is added.

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw5-2.png
   :alt: hw5-2.png
   :width: 90%

6. MIPI-CSI
--------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw6-1.png
   :alt: hw6-1.png
   :width: 90%

- The DVDD power supply of the Camera has different specifications such as 1.2V/1.5V/1.8V. Please provide the accurate power supply according to the Camera's datasheet;
- Some Cameras have a large DVDD current (high-resolution modules). If it exceeds 300mA, it is recommended to use DCDC power supply;
- The power supply of some Cameras has power-on sequence requirements. Please reserve RC for the power enable pin and adjust the power-on sequence accordingly according to the module's datasheet;
- When using a Camera with a CIF interface, ensure that the DOVDD (IO power supply) of the Camera and the power domain (VCCIO5 or VCCIO6) connected to the SOC side use the same voltage;
- When using two Cameras, the power supplies can be separated or combined according to actual application requirements;
- The decoupling capacitor of the Camera power supply must not be omitted and must be retained, placed close to the sensor image; if the Camera module is connected to the SoC through a flat cable, a uF-level capacitor should also be placed at the connector;
- The PWDN signal of the Camera must be controlled by GPIO, and the GPIO level must match the Camera IO level;
- It is recommended that the Reset/Shutdown signal of the Camera be controlled by GPIO, and the GPIO level must match the Camera IO level. The 100nF capacitor of the Reset signal must not be deleted, placed close to the connector to enhance anti-static capability;
- In dual-camera mode, if the two Cameras are of the same model, pay attention to whether the I2C address can be configured through SID. If the I2C address is fixed, they cannot be connected to the same I2C bus and need to be connected separately.
- The MCLK of the Camera can be obtained from the following clock sources:
    - VI_CIF_CLKOUT
    - REF_CLK0_OUT
    - CAM_CLK0_OUT/CAM_CLK1_OUT/CAM_CLK2_OUT/CAM_CLK3_OUT
    - Note: The level of the clock must match the Camera IO level. If not, level conversion or resistor voltage division must be performed to make the levels match;  

7. MIPI-DSI
--------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw7-1.png
   :alt: hw7-1.png
   :width: 90%

|   RV1126B has one MIPI DPHY DSI TX, supporting MIPI V1.2 version with a total of 4 Lanes. The maximum transmission rate supported by each channel is 1.5Gbps/Lane, and the maximum resolution supported is 1920x1080@60Hz.  

+-------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------+
| MIPI_DPHY_DSI_TX_D0P/N  | Direct connection; it is recommended to reserve a common-mode inductor to suppress electromagnetic radiation | MIPI DSI Data Lane 0 output |
+-------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------+
| MIPI_DPHY_DSI_TX_D1P/N  | Direct connection; it is recommended to reserve a common-mode inductor to suppress electromagnetic radiation | MIPI DSI Data Lane 1 output |
+-------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------+
| MIPI_DPHY_DSI_TX_D2P/N  | Direct connection; it is recommended to reserve a common-mode inductor to suppress electromagnetic radiation | MIPI DSI Data Lane 2 output |
+-------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------+
| MIPI_DPHY_DSI_TX_D3P/N  | Direct connection; it is recommended to reserve a common-mode inductor to suppress electromagnetic radiation | MIPI DSI Data Lane 3 output |
+-------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------+
| MIPI_DPHY_DSI_TX_CLKP/N | Direct connection; it is recommended to reserve a common-mode inductor to suppress electromagnetic radiation | MIPI DSI Clock output       |
+-------------------------+--------------------------------------------------------------------------------------------------------------+-----------------------------+
  
|   Precautions for the design of the MIPI DPHY DSI TX interface:

- Supports 1/2/4 Lane modes. 1 Lane defaults to D0, and 2 Lane mode defaults to D0/D1;
- MIPI Data Lanes do not support inter-group swapping and need to be in one-to-one correspondence; intra-group P/N swapping is also not supported;
- When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (2.2ohm, subject to meeting SI test requirements) in series and reserve TVS devices.  

8. LCD
---------

|   The RV1126B LCDC TX interface supports parallel 24bit RGB mode, 16bit BT.1120 mode, 8bit BT.656 mode, and MCU mode. Among them, the resolution support for RGB, BT.1120, and BT.656 is as follows:

- 24bit RGB mode: The maximum output resolution can reach 1920x1080@60Hz;
- 16bit BT.1120 mode: The maximum output resolution can reach 1920x1080@60Hz;
- 8bit BT.656 mode: The maximum resolution is 720x576@60Hz, supporting PAL and NTSC;

|   The signal connection of the LCDC TX interface is shown in the following figure:  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw8-1.png
   :alt: hw8-1.png
   :width: 90%

|   Precautions for the design of the LCDC TX interface:

- The power domain of these parallel signal output interfaces is powered by VCCIO5. In actual product design, the corresponding power supply must be selected according to the actual IO power supply requirements (1.8V or 3.3V) of the peripheral to ensure consistency;
- When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (between 22ohm-100ohm, subject to meeting SI test requirements) in series and reserve TVS devices.
- To improve the performance of the parallel signal output interface, the decoupling capacitor of the VCCIO5 power supply must not be deleted, and should be placed close to the pins during layout.  

9. Audio Interface
--------------------

|   RV1126B provides rich audio interface capabilities and resources, including 3 groups of SAI interfaces, 1 group of PDM interfaces, 1 group of DSM interfaces, 2 groups of Audio ADCs, and 2 groups of ASRC processing units.  
|   The block diagram of the RV1126B audio subsystem is shown below, including information about external/internal interfaces:  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-1.png
   :alt: hw9-1.png
   :width: 90%

|   The following points should be noted in audio design:

- SAI0, SAI1, and SAI2 can be maximally combined into 6TX lanes +8RX lanes;
- SAI2_SDO can be internally selected to connect to the Audio DSM interface or directly to GPIO, and only one of the two can be selected;
- SAI2_SDI0 can be internally selected to connect to the Audio ADC0 interface or directly to GPIO, and only one of the two can be selected;
- SAI2_SDI1 can be internally selected to connect to the Audio ADC1 interface or directly to GPIO, and only one of the two can be selected;
- If the Audio DSM and Audio ADC0/1 interfaces are already in use, please select SDI2 for the SAI2 interface input;
- The MCLK of SAI0, SAI1, and SAI2 not only supports output but also input. In input mode, it can provide clock sources for PDM, DSM, Audio ADC0/1, and the SAI interface itself. For example: SAI0_MCLK can provide clock sources for PDM, DSM, Audio ADC0/1, and SAI0; SAI1_MCLK can provide clock sources for SAI1; SAI2_MCLK can provide clock sources for SAI2;

- If SAI is used as SLAVE, there is no need to connect MCLK input.  

|   RV1126B provides a total of 3 groups of SAI interfaces. The full name of the SAI interface is Serial Audio Interface, which is a serial interface used for digital audio data communication. It supports a wide range of audio protocols, including standard formats such as PCM, I2S, and TDM, and can meet the requirements of mono, stereo, and multi-channel audio transmission. As the most widely used digital audio interface, SAI can be used for communication with peripherals such as audio ADCs, audio DACs, audio Codecs, and DSPs, and can also provide integrated audio input and output support for video input/output interfaces. The SAI interface of RV1126B has the following characteristics:

- Supports bit widths from 8 to 32 bits, including common ones such as 32 bits, 24 bits, and 16 bits;
- Supports up to 128 channels (slots);
- Supports mono mode;
- For TX/RX in Master mode and Slave mode, the upper limit of the SCLK design rate is 25M;

|   SAI0 supports 4TX Lanes +4RX Lanes, SAI1 supports 1TX Lanes +1RX Lanes, and SAI2 supports 1TX Lanes +3RX Lanes. Here, TX represents the output data line SDOx, and RX represents the input data line SDIx. Each TX or RX contains 2 channels. The upper limit of the sampling rate of the data line can be calculated as follows: IO rate / (slots * width), where slots is the number of channels and width is the bit width. The typical sampling rate reference calculation is as follows, and other sampling rates can be configured with reference  

+-------+----------------------------+-------------------+------------------+-------------+
| Mode  | Number of Channels (Slots) | Bit Width (Width) | LRCK Sample Rate | SCLK Rate   |
+-------+----------------------------+-------------------+------------------+-------------+
| I2S   | 2                          | 32                | 16 kHz           | 1.024 MHz   |
+-------+----------------------------+-------------------+------------------+-------------+
| I2S   | 2                          | 32                | 44.1 kHz         | 2.8224 MHz  |
+-------+----------------------------+-------------------+------------------+-------------+
| I2S   | 2                          | 32                | 48 kHz           | 3.072 MHz   |
+-------+----------------------------+-------------------+------------------+-------------+
| TDM8  | 8                          | 32                | 16 kHz           | 4.096 MHz   |
+-------+----------------------------+-------------------+------------------+-------------+
| TDM8  | 8                          | 32                | 44.1 kHz         | 11.2896 MHz |
+-------+----------------------------+-------------------+------------------+-------------+
| TDM8  | 8                          | 32                | 48 kHz           | 12.288 MHz  |
+-------+----------------------------+-------------------+------------------+-------------+
| TDM16 | 16                         | 32                | 16 kHz           | 8.192 MHz   |
+-------+----------------------------+-------------------+------------------+-------------+
| TDM16 | 16                         | 32                | 44.1 kHz         | 22.5792 MHz |
+-------+----------------------------+-------------------+------------------+-------------+
| TDM16 | 16                         | 32                | 48 kHz           | 24.576 MHz  |
+-------+----------------------------+-------------------+------------------+-------------+

|   The above are theoretical calculation values. The actual rate is also affected by factors such as IO signal quality and wiring delay. Please pay attention to the distribution of relevant clocks and signals and optimize the wiring in the design.
|   Due to differences in interface design, the operating rates of different SAI interfaces are as follows:  

+------+-------------------+
| Mode | Maximum SCLK Rate |
+------+-------------------+
| SAI0 | 13 MHz            |
+------+-------------------+
| SAI1 | 25 MHz            |
+------+-------------------+
| SAI2 | 25 MHz            |
+------+-------------------+
  
|   The SAI0 interface includes independent 4TX Lanes and 4RX Lanes. For the output data line SDOx and input data SDIx, a set of bit/frame clocks SCLK/LRCK is referenced simultaneously.
|   The SAI0 interface supports master and slave working modes, which can be configured by software. SAI0 provides a flexible compatibility configuration mode that can customize the frame format of LRCK and DATA, thereby achieving compatibility with most I2S, PCM, and TDM; at the same time, it also provides direct configuration of 3 I2S formats (standard, left-aligned, right-aligned) and early PCM format.
|   The pins of this group of SAI are multiplexed in 2 different power domains: SAI0_M0 is multiplexed in VCCIO7, and SAI0_M1 is multiplexed in VCCIO6. The two multiplexing cannot be used at the same time, and only one group can be used each time. Different data lines SDOx or SDIx can be remapped internally to reconfigure the order. For example, SDO1+SDO3 can be extracted at intervals to form 2 lanes for use.
|   In the design, it is necessary to check the IO level of the SAI peripheral to match the power supply of the corresponding IO power domain.

|   The matching design of the SAI0 interface is shown in the following table:  

+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| Signal                    | Default Pull-Up/Pull-Down | Connection Method     | Description (Chip Side)                                    |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_MCLK_M0              | Pull-Down                 | Series 22ohm resistor | SAI system clock output                                    |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SCLK_M0              | Pull-Down                 | Series 22ohm resistor | SAI continuous serial clock, bit clock                     |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_LRCK_M0              | Pull-Down                 | Series 22ohm resistor | SAI frame clock, used for channel selection                |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDO0_M0              | Pull-Down                 | Direct Connection     | SAI serial output data line 0                              |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDO1_M0/SAI0_SDI3_M0 | Pull-Down                 | Direct Connection     | SAI serial output data line 1/SAI serial input data line 3 |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDO2_M0/SAI0_SDI2_M0 | Pull-Down                 | Direct Connection     | SAI serial output data line 2/SAI serial input data line 2 |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDO3_M0/SAI0_SDI1_M0 | Pull-Down                 | Direct Connection     | SAI serial output data line 3/SAI serial input data line 1 |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDI0_M0              | Pull-Down                 | Direct Connection     | SAI serial input data line 0                               |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_MCLK_M1              | Pull-Down                 | Series 22ohm resistor | SAI system clock output                                    |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SCLK_M1              | Pull-Down                 | Series 22ohm resistor | SAI continuous serial clock, bit clock                     |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_LRCK_M1              | Pull-Down                 | Series 22ohm resistor | SAI frame clock, used for channel selection                |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDO0_M1              | Pull-Down                 | Direct Connection     | SAI serial output data line 0                              |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDO1_M1/SAI0_SDI3_M1 | Pull-Down                 | Direct Connection     | SAI serial output data line 1/SAI serial input data line 3 |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDO2_M1/SAI0_SDI2_M1 | Pull-Down                 | Direct Connection     | SAI serial output data line 2/SAI serial input data line 2 |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDO3_M1/SAI0_SDI1_M1 | Pull-Down                 | Direct Connection     | SAI serial output data line 3/SAI serial input data line 1 |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+
| SAI0_SDI0_M1              | Pull-Down                 | Direct Connection     | SAI serial input data line 0                               |
+---------------------------+---------------------------+-----------------------+------------------------------------------------------------+

**PDM Digital Audio Interface**

|   RV1126B provides a total of 1 group of 8-channel PDM interfaces. The full name of the PDM interface is Pulse Density Modulation, which is usually used to connect digital microphones or record analog microphones through the analog audio ADC of the PDM interface. The sampling rate is usually 16kHz, 48kHz, or 8kHz, and some products with ultrasonic requirements need to use a 96kHz sampling rate.
|   Both groups of PDM work in master receive mode (i.e., RV1126B provides PDM clock and receives data), supporting 8-channel input capability, bit widths from 16 to 32 bits, and a maximum sampling rate of 192kHz.
|   The following figure shows the data format of the PDM interface. PDM_DATA is composed of Data(R) and Data(L). PDM is a 1-bit sampling interface that samples these two Data(L) and Data(R) on the rising edge and falling edge of the CLK respectively, that is, each PDM_SDIx data line can transmit audio data of 2 channels. Therefore, the four SDIx data lines of one group of PDM can meet the requirement of connecting up to 8 microphones (or 6 microphones + 2 loopback channels, totaling 8 channels).  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-2.png
   :alt: hw9-2.png
   :width: 90%

|   The corresponding relationship between common sampling rates and PDM_CLK is shown in the following table, which can be used as a reference during hardware debugging. The quality of the clock signal has a direct impact on the PDM recording quality. Therefore, when dividing the PLL frequency, a fractional PLL + integer division method should be used.  

+-------------------+-------------------------------------------------+
| PDM_CLK Frequency | Sampling Rate                                   |
+-------------------+-------------------------------------------------+
| 3.072MHz          | 12kHz, 24kHz, 48kHz, 96kHz, 192kHz              |
+-------------------+-------------------------------------------------+
| 2.8224MHz         | 11.025kHz, 22.05kHz, 44.1kHz, 88.2kHz, 176.4kHz |
+-------------------+-------------------------------------------------+
| 2.048MHz          | 8kHz, 16kHz, 32kHz, 64kHz, 128kHz               |
+-------------------+-------------------------------------------------+

|   The PDM pins are multiplexed in 2 different power domains: PDM_M0 is multiplexed in VCCIO7, and PDM_M1 is multiplexed in VCCIO6. The relevant multiplexing is shown in the following table. The two multiplexing cannot be used at the same time, and only one group can be used each time. It is necessary to check the IO level of the PDM peripheral to match the power supply of the corresponding IO power domain.  

+-----+-----+--------+----------------------+
| PDM | M0  | VCCIO7 | CLK0+CLK1+SDI0/1/2/3 |
+-----+-----+--------+----------------------+
| PDM | M1  | VCCIO6 | CLK0+CLK1+SDI0/1/2/3 |
+-----+-----+--------+----------------------+

|   To improve the impact of PCB wiring on the clock, two homologous and in-phase PDM clocks, PDM_CLK0 and PDM_CLK1, are provided, which can be used with PDM_SDIx data lines arbitrarily. In the actual product design, reasonable and flexible allocation should be carried out according to the peripheral connection, product structure, and PCB wiring conditions to avoid the large impact of long wiring branches and multiple loads on signal quality when a single clock is connected to multiple MIC inputs.
|   The matching design of the PDM interface is shown in the following table:  

+-------------+---------------------------+-----------------------+-------------------------+
| Signal      | Default Pull-Up/Pull-Down | Connection Method     | Description (Chip Side) |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_CLK0_M0 | Pull-Down                 | Series 22ohm resistor | PDM Clock 0             |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_CLK1_M0 | Pull-Down                 | Series 22ohm resistor | PDM Clock 1             |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_SDI0_M0 | Pull-Down                 | Direct Connection     | PDM Input Data Line 0   |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_SDI1_M0 | Pull-Down                 | Direct Connection     | PDM Input Data Line 1   |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_SDI2_M0 | Pull-Down                 | Direct Connection     | PDM Input Data Line 2   |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_SDI3_M0 | Pull-Down                 | Direct Connection     | PDM Input Data Line 3   |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_CLK0_M1 | Pull-Down                 | Series 22ohm resistor | PDM Clock 0             |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_CLK1_M1 | Pull-Up                   | Series 22ohm resistor | PDM Clock 1             |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_SDI0_M1 | Pull-Down                 | Direct Connection     | PDM Input Data Line 0   |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_SDI1_M1 | Pull-Up                   | Direct Connection     | PDM Input Data Line 1   |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_SDI2_M1 | Pull-Up                   | Direct Connection     | PDM Input Data Line 2   |
+-------------+---------------------------+-----------------------+-------------------------+
| PDM_SDI3_M1 | Pull-Up                   | Direct Connection     | PDM Input Data Line 3   |
+-------------+---------------------------+-----------------------+-------------------------+

|   Precautions for the design of the PDM interface:

- To improve the performance of the PDM interface, the decoupling capacitor of the corresponding VCCIO power domain must not be deleted, and should be placed close to the pins during layout;
- When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (between 22ohm-100ohm, subject to meeting SI test requirements) in series for clocks/controls/signals and reserve TVS devices.  

**DSM Audio Interface**

|   DSM Audio (Digital Signal Modulator) refers to a 1-bit signal stream data obtained by converting audio PCM data through Direct Stream Digital encoding. In designs requiring audio output, the digital signal output by the interface is processed by a first-order RC low-pass filter to obtain an analog audio signal output. The principle of DSM is shown in the following figure:  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-3.png
   :alt: hw9-3.png
   :width: 90%

|   DSM audio is a low-cost audio output solution. For scenarios with sound quality requirements, it is recommended to use an external audio Codec or DAC to achieve audio output. The following table shows the audio indicators of the DSM audio differential output under a 200Kohm load:  

+-----------------+---------------------+-------------------------+---------+----------+------------+----------+
| Test Item       | Test Conditions     | Output Signal Amplitude | FS=8KHz | FS=16KHz | FS=44.1KHz | FS=48KHz |
+-----------------+---------------------+-------------------------+---------+----------+------------+----------+
| RMS Level(Vrms) | N/A                 | 0dBFS                   | 2.037   | 2.037    | 2.037      | 2.037    |
+-----------------+---------------------+-------------------------+---------+----------+------------+----------+
| THD+N(dB)       | LPF=20KHz, HPF=20Hz | -3dBFS                  | -72.505 | -72.888  | -75.047    | -75.241  |
+-----------------+---------------------+-------------------------+---------+----------+------------+----------+
| SNR(dB)         | 0dBFS/Noise         | 94.825                  | 95.035  | 97.508   | 97.115     |          |
+-----------------+---------------------+-------------------------+---------+----------+------------+----------+
| DR(dB)          | 0dBFS/-60dBFS       | 77.637                  | 77.732  | 82.259   | 84.261     |          |
+-----------------+---------------------+-------------------------+---------+----------+------------+----------+
| Noise(uVrms)    | N/A                 | 67.12                   | 64.95   | 62.37    | 62.79      |          |
+-----------------+---------------------+-------------------------+---------+----------+------------+----------+

|   This group of interfaces provides two pairs of differential outputs to meet stereo requirements. For detailed introduction of the interface and calculation of RC low-pass filter parameters, refer to the document "DSM AUDIO Interface Circuit Design".

- The DSM output RC filter circuit cannot be deleted;
- The quality of the audio clock signal has a direct impact on the DSM output quality. Therefore, when dividing the PLL frequency, a fractional PLL + integer division method should be used;
- PCB wiring and ground handling have a direct impact on the DSM output quality. Please route according to the PCB design recommendations;
- The differential audio output cannot be split into 2 single-ended audio outputs for use, and single-ended mode is not recommended due to poor audio quality;
- SAI2_SDO is internally connected to the DSM module. Therefore, when the DSM module is in use, the external SAI2 SDO cannot be used;

|   The matching design of the DSM interface is shown in the following table:

+-------------------------+---------------------------+---------------------------+-------------------------------------+
| Signal and Multiplexing | Default Pull-Up/Pull-Down | Connection Method         | Description (Chip Side)             |
+-------------------------+---------------------------+---------------------------+-------------------------------------+
| DSM_AUD_LP              | Pull-Down                 | Series RC low-pass filter | DSM Output Left Channel P Terminal  |
+-------------------------+---------------------------+---------------------------+-------------------------------------+
| DSM_AUD_LN              | Pull-Down                 | Series RC low-pass filter | DSM Output Left Channel N Terminal  |
+-------------------------+---------------------------+---------------------------+-------------------------------------+
| DSM_AUD_RP              | Pull-Down                 | Series RC low-pass filter | DSM Output Right Channel P Terminal |
+-------------------------+---------------------------+---------------------------+-------------------------------------+
| DSM_AUD_RN              | Pull-Down                 | Series RC low-pass filter | DSM Output Right Channel N Terminal |
+-------------------------+---------------------------+---------------------------+-------------------------------------+

|   Precautions for the design of the DSM audio interface:

- To improve interface performance, the decoupling capacitor of the corresponding VCCIO power domain must not be deleted, and should be placed close to the pins during layout;
- When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (between 22ohm-100ohm, subject to meeting SI test requirements) in series for clocks/controls/signals and reserve TVS devices.

**AUDIO ADC Audio Interface**

|   RV1126B has 2 built-in AUDIO ADCs, both supporting differential MIC input. The following points should be noted when using:
|   The reference circuit for differential MIC input is shown in the following figure:  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-4.png
   :alt: hw9-4.png
   :width: 90%

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-5.png
   :alt: hw9-5.png
   :width: 90%

|   Precautions for the design of the Audio ADC interface:

- The differential input of the MIC cannot be split into two single-ended inputs for use;
- AUDIO_ADC_VCM is the common-mode voltage pin of the Audio ADC PHY, with a voltage of 0.8V. An external 2.2uF capacitor to ground must be connected, and the capacitor value cannot be changed. It should be placed close to the SOC chip pins during layout;
- AUDIO_ADC_VREF is the reference voltage pin of the Audio ADC PHY, with a voltage of 1.6V. An external 2.2uF capacitor to ground must be connected, and the capacitor value cannot be changed. It should be placed close to the SOC chip pins during layout;
- AUDIO_ADC_AVDD_1V8 supplies power to the AUDIO ADC0/1 modules, and the decoupling capacitor should be placed close to the SOC chip pins.
- The input interfaces of ADDIO_ADC_MIC can be used as input channels for LINEIN or MIC_IN. If the input device is a passive MIC, a 1.8V bias voltage needs to be provided. If the input device is an active input, it is not needed.
- The recommended value of the coupling capacitor for MIC input is 1uF or more, and it should be placed close to the SOC chip pins during layout;
- For the bias voltage of the MIC input, reserve RC to improve power supply noise, with a resistance value of 100ohm and a capacitance value of 4.7uF; 
 
**ASRC Asynchronous Sample Rate Converter Module**

 | ASRC (Asynchronous Sample Rate Converter) does not have a specific hardware IO interface form, but it has a great impact on the design, compatibility, synchronization, and real-time functions of audio solutions in actual products, so it is introduced in this section.
 | In audio systems, ASRC is usually used to convert audio data from one sampling rate to another, or to convert "asynchronous same sampling rate" data based on different clocks. Therefore, the ASRC module can be regarded as an intermediate component of audio interfaces such as SAI and PDM. By using ASRC, devices or interfaces with different sampling rates and asynchronous clocks can maintain the continuity and stability of audio communication.
 | RV1126B provides 2 ASRC modules, covering external and internal audio modules. The supported sampling rate range is from 8kHz to 384kHz, and the typical ones are shown in the following table. It provides a conversion range from 1:8 (down conversion) to 8:1 (up conversion).  

+-----------------------------------------------------------+
| Typical Input/Output Sampling Rates of ASRC Modules       |
+-----------------------------------------------------------+
| 8KHz, 16KHz, 32KHz, 64KHz, 128KHz                         |
+-----------------------------------------------------------+
| 12KHz, 24KHz, 48KHz, 96KHz, 192KHz, 384KHz                |
+-----------------------------------------------------------+
| 11.025KHz, 22.05KHz, 44.1KHz, 88.2KHz, 176.4KHz, 352.8KHz |
+-----------------------------------------------------------+

**Design Reference for Audio Peripherals**

|   This section provides connection suggestions for common audio peripheral scenarios, which users can refer to.  
|   RV1126B can connect to an audio DAC or CODEC (such as RK730) through SAI signals to achieve analog output, and then achieve power amplification through an audio power amplifier to drive speakers, as shown in the following figure:  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-6.png
   :alt: hw9-6.png
   :width: 90%

|   For the speaker playback requirement of low-cost solutions, the DSM filtered output of RV1126B can be used, and then power amplification can be achieved through an audio power amplifier to drive speakers, as shown in the following figure:  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-7.png
   :alt: hw9-7.png
   :width: 90%

|   For recording requirements, there are the following implementation methods:  

|   1. Use the built-in differential ADC of ACODEC to achieve analog signal input;  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-8.png
   :alt: hw9-8.png
   :width: 90%

|   2. Connect a PDM microphone through the PDM interface, or use an ADC with SAI/I2S/PDM interface to connect an external analog MIC; 

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-9.png
   :alt: hw9-9.png
   :width: 90%

|   3. Use a Codec (such as RK730) to achieve related functions, as shown in the following figure;  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw9-10.png
   :alt: hw9-10.png
   :width: 90%

10. RGMII/RMII Interface
--------------------------

|   GMAC is multiplexed in two different power domains: GMAC_M0 is multiplexed in the VCCIO6 power domain, and GMAC_M1 is multiplexed in the VCCIO5 power domain.  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw10-1.png
   :alt: hw10-1.png
   :width: 90%

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw10-2.png
   :alt: hw10-2.png
   :width: 90%

|   1. Both Ethernet channels adopt 3.3V level.
|   To improve the performance of the RGMII/RMII interface, the decoupling capacitor of the VCCIOx_VCC power supply in the corresponding power domain must not be deleted, and should be placed close to the pins during layout.

- For ETH_CLK_25M_OUT_Mx, a 0 ohm resistor should be reserved in series at the RV1126B end, and the resistance value should be adjusted according to the actual test results to improve signal quality.
- For TXD0~TXD3, TXCLK, and TXCTL, a 0 ohm resistor should be reserved in series at the RV1126B end, and the resistance value should be adjusted according to the actual test results to improve signal quality.
- For RXD0~RXD3, RXCLK, and RXCTL, a 22 ohm resistor should be connected in series at the PHY end to improve signal quality.

|   The matching design of the RGMII/RMII interface is shown in the following table:  

+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| Signal             | IO Type (SOC Side) | Connection Method                                                 | RGMII Interface      | Signal Description                                                                | RMII Interface                      | Signal Description                                        |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_TXD[3:0]_Mx    | Output             | Reserve series 0ohm resistor, close to the SOC side               | RGMII_TXD[3:0]       | Data Transmission                                                                 | RMII_TXD[1:0]                       | Data Transmission                                         |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_TXCLK_Mx       | Output             | Reserve series 0ohm resistor, close to the SOC side               | RGMII_TXCLK          | Data Transmission Reference Clock                                                 | --                                  | --                                                        |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_TXCTL_Mx       | Output             | Reserve series 0ohm resistor, close to the SOC side               | RGMII_TXCTL          | Data Transmission Enable (Rising Edge) and Data Transmission Error (Falling Edge) | RMII_TXEN                           | Data Transmission Enable Signal                           |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_RXD[3:0] _Mx   | Input              | Series 22ohm resistor, close to the PHY side                      | RGMII_RXD[3:0]       | Data Reception                                                                    | RMII_RXD[1:0]                       | Data Reception                                            |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_RXCLK_Mx       | Input              | Series 22ohm resistor, close to the PHY side                      | RGMII_RXCLK          | Data Reception Reference Clock                                                    | --                                  | --                                                        |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_RXCTL_Mx       | Input              | Series 22ohm resistor, close to the PHY side                      | RGMII_RXCTL          | Data Reception Valid (Rising Edge) and Reception Error (Falling Edge)             | RMII_RXCTL                          | Data Reception Valid and Carrier Sense                    |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_MCLK_Mx        | Input/Output       | Output Mode: Reserve series 0ohm resistor, close to the SOC side; | RGMII_MCLKIN 125M    | PHY sends 125MHz to MAC, optional                                                 | RMII_MCLKIN 50M or RMII_MCLKOUT 50M | RMII Data Transmission and Data Reception Reference Clock |
+                    +                    +                                                                   +                      +                                                                                   +                                     +                                                           +
|                    |                    |                                                                   |                      |                                                                                   |                                     |                                                           |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_CLK_25M_OUT_Mx | Output             | Reserve series 0ohm resistor, close to the SOC side               | ETH_CLKx_25M_O UT_Mx | RV1126B provides 25MHz clock instead of PHY crystal                               | ETH_CLK_25M_OU T_Mx                 | RV1126B provides 25MHz clock instead of PHY crystal       |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_MDC_Mx         | Output             | Reserve series 0ohm resistor, close to the SOC side               | RGMII_MDC            | Management Data Clock                                                             | RMII_MDC                            | Management Data Clock                                     |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+
| ETH_MDIO_Mx        | Input/Output       | External pull-up 1.5K-1.8Kohm resistor                            | RGMII_MDIO           | Management Data Output/Input                                                      | RMII_MDIO                           | Management Data Output/Input                              |
+--------------------+--------------------+-------------------------------------------------------------------+----------------------+-----------------------------------------------------------------------------------+-------------------------------------+-----------------------------------------------------------+


- When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (between 22ohm-100ohm, subject to meeting SI test requirements) in series and reserve TVS devices.
- Schematic Diagram of RGMII/RMII Interface Connection  

|   The working clock of RGMII GEPHY uses an external 25MHz crystal  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw10-3.png
   :alt: hw10-3.png
   :width: 90%

|   The working clock of RGMII GEPHY uses the 25MHz provided by RV1126B  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw10-4.png
   :alt: hw10-4.png
   :width: 90%

|   The working clock of RMII FEPHY uses a 25MHz crystal, ETH_MCLK_Mx adopts output mode as the reference clock of the RMII interface, and the TXCLK of FEPHY needs to be configured as input mode  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw10-5.png
   :alt: hw10-5.png
   :width: 90%

|   RMII uses the 25MHz provided by the SOC instead of the FEPHY crystal, ETH_MCLK_Mx adopts output mode as the reference clock of the RMII interface, and the TXCLK of FEPHY needs to be configured as input mode  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw10-6.png
   :alt: hw10-6.png
   :width: 90%

|   The working clock of FEPHY uses an external 25MHz crystal, ETHx_MCLK_Mx adopts input mode, the reference clock of the RMII interface is provided by FEPHY, and the TXCLK of FEPHY needs to be configured as output mode  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw10-7.png
   :alt: hw10-7.png
   :width: 90%

|   RMII uses the 25MHz provided by the SOC instead of the FEPHY crystal, ETH_MCLK_Mx adopts input mode, the reference clock of the RMII interface is provided by FEPHY, and the TXCLK of FEPHY needs to be configured as output mode  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw10-8.png
   :alt: hw10-8.png
   :width: 90%

|   Precautions for the design of the RGMII/RMII interface: 

- In RGMII mode, the internal TX/RX clock path of the RV1126B chip integrates a delayline, which supports adjustment; the default configuration of the reference figure is: the timing between TXCLK and data is controlled by the MAC, and the timing between RXCLK and data is controlled by the PHY (such as using \*\*8211F/FI, the RXCLK enables 2ns delay by default, and other PHYs should pay attention to this configuration)  
- The Reset signal of the Ethernet PHY needs to be controlled by GPIO, and the GPIO level must match the PHY IO level. A 100nF capacitor must be added close to the PHY pins to enhance anti-static capability. Note: The reset pin of \*\*8211F/FI only supports 3.3V level.
- The INTB/PMEB of \*\*8211F/FI is an open-drain output, and an external pull-up resistor must be added.
- When the PHY uses an external crystal, the crystal capacitor should be selected according to the load capacitance value of the actually used crystal, and the frequency deviation should be controlled within +/-20ppm.
- The external resistor for the RSET pin of \*\*8211F/FI is 2.49K ohm with an accuracy of 1%, which cannot be modified arbitrarily.
- The hardware configuration for PHY initialization must match the actual requirements.
- MDIO must be externally pulled up with a resistor, recommended 1.5-1.8Kohm, and the pull-up power supply must be consistent with the IO power supply.
- The connection of the transformer center tap must refer to the reference design of each Ethernet PHY manufacturer, as different PHY manufacturers will have different connection methods.
- The 1000pF isolation capacitor is recommended to use a high-voltage safety capacitor with a sufficient electrical gap to ensure lightning strike safety.
- The 75 ohm resistor on the high-voltage side of the network transformer is recommended to use a package of 0805 or larger.
- To achieve a lightning protection level of 4KV or above, a lightning protection tube needs to be added. An ordinary isolation transformer can only meet the 2KV level requirement.
- If there is a lightning strike differential test requirement, a TVS tube needs to be added between the MDI differential pairs.
- It is necessary to confirm whether the RJ45 package is consistent with the schematic diagram. RJ45 is divided into Tab down and Tab up, and the signal order is exactly opposite. If using \*\*8211F/FI, it is recommended to use Tab down, and the MDI order is correct.  

**FEPHY Interface**

|   The built-in FEPHY of RV1126B can realize 100M Ethernet function, and only one of GMAC_M0/GMAC_M1 can be selected for use at the same time.
|   The signal connection of the FEPHY interface is shown in the following figure:

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw10-9.png
   :alt: hw10-9.png
   :width: 90%

|   Precautions for the design of the FEPHY interface:

- To improve performance, the decoupling capacitors of each power supply of FEPHY must not be deleted, and should be placed close to the pins during layout;
- The FEPHY output supports TX/RX swapping and intra-group P/N swapping, which can be appropriately adjusted according to the PCB wiring conditions;  
- A 110ohm termination resistor should be connected in parallel between the differential signals FEPHY_TXP/N and between the differential signals FEPHY_RXP/N, placed close to the SoC end, and cannot be deleted;
- A 5.1ohm resistor should be connected in series with FEPHY_TXP/N and FEPHY_RXP/N, placed close to the transformer end, which can improve surge resistance;
- The 1nF capacitance value of the transformer center tap cannot be modified, placed close to the transformer;  

|   The matching design of the FEPHY interface is shown in the following table  

+-------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| Signal      | Connection Method                                                                                   | Description (Chip Side)                    |
+-------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| FEPHY_TXP/N | A 110ohm resistor is connected in parallel between the differential pairs, close to the SoC end;    | Data Transmission Differential Pair Signal |
+             +                                                                                                     +                                            +
|             | a 5.1ohm resistor is connected in series with the single-ended signal, close to the transformer end |                                            |
+-------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| FEPHY_RXP/N | A 110ohm resistor is connected in parallel between the differential pairs, close to the SoC end;    | Data Reception Differential Pair Signal    |
+             +                                                                                                     +                                            +
|             | a 5.1ohm resistor is connected in series with the single-ended signal, close to the transformer end |                                            |
+-------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+
| FEPHY_EXTR  | A 6.49Kohm 1% precision resistor is connected in series to ground, placed close to the pin          | Reference Resistor                         |
+-------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------+


11. UART Interface
--------------------

|   The RV1126B chip has 8 UART controllers, supporting the following functions:

- Supports full-duplex and half-duplex communication modes;
- Each includes two 64-byte FIFOs for data reception and transmission;
- The maximum transmission rate is 4Mbps;
- Supports programmable baud rate and non-integer clock divider;
- Supports interrupt-based or DMA-based mode;
- Supports 5-8 bit width transmission;
- UART1~7 support RS485 automatic transceiving function.
- UART0 is the default programming and printing serial port

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw11-1.png
   :alt: hw11-1.png

|   Considering the flexibility of different product applications, the 8 UARTs are respectively multiplexed in several different power domains, distinguished by suffixes M0/M1/M2/M3 for different multiplexing positions. M0/M1/M2/M3 cannot be used at the same time. Only one group can be selected during allocation. It is not allowed to select M0 for some signals, M1 for others, and M2 for others. This function is not supported. Among the 8 UARTs, only UART0 does not have flow control function, and the rest UART1~7 all have flow control function.
|   The distribution of the RV1126B UART interface is as follows:

+----------------------------+---------------------+------------------------------------------------+
| UART Number                | Multiplexing Status | Multiplexing Power Domain                      |
+----------------------------+---------------------+------------------------------------------------+
| UART0 (Default Debug Uart) | M0, M1, M2          | M0: VCCIO2; M1: VCCIO5; M2: PMUIO0             |
+----------------------------+---------------------+------------------------------------------------+
| UART1                      | M0, M1              | M0: PMUIO1; M1: VCCIO3                         |
+----------------------------+---------------------+------------------------------------------------+
| UART2                      | M0, M1              | M0: VCCIO3; M1: VCCIO7                         |
+----------------------------+---------------------+------------------------------------------------+
| UART3                      | M0, M1, M2          | M0: VCCIO2; M1: VCCIO5; M2: VCCIO6             |
+----------------------------+---------------------+------------------------------------------------+
| UART4                      | M0, M1, M2, M3      | M0: VCCIO4; M1: VCCIO5; M2: VCCIO6; M3: VCCIO2 |
+----------------------------+---------------------+------------------------------------------------+
| UART5                      | M0, M1, M2          | M0: VCCIO4; M1: VCCIO5; M2: VCCIO6             |
+----------------------------+---------------------+------------------------------------------------+
| UART6                      | M0, M1              | M0: VCCIO5; M1: VCCIO6                         |
+----------------------------+---------------------+------------------------------------------------+
| UART7                      | M0, M1              | M0: VCCIO5; M1: VCCIO6                         |
+----------------------------+---------------------+------------------------------------------------+

|   Precautions for the design of the UART interface:

- Adjust the power supply of the corresponding power domain according to the IO level of the UART peripheral to ensure consistency;
- Pay attention to the direction of TX/RX when connecting the SoC to the UART device;
- When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (between 22ohm-100ohm, subject to meeting SI test requirements) in series and reserve TVS devices.  

12. RS232
------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw12-1.png
   :alt: hw12-1.png
   :width: 90%

|   1. Please note to add ESD protection at the interface.
|   2. Note that the level of the serial port is 3.3V.

13. RS485
------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw13-1.png
   :alt: hw13-1.png
   :width: 90%

|   1. Please note to add ESD protection at the interface.
|   2. Note that the level of the serial port is 3.3V.

14. CAN
----------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw14-1.png
   :alt: hw14-1.png
   :width: 90%

|   The RV1126B chip has 2 CAN controllers, supporting the following functions:

- Supports traditional CAN and optimized CAN FD, with transmission rates of 1, 2, and 5 Mbps (can support a maximum rate of 8Mbps under certain conditions, but the 8M rate has high requirements on signal quality and loop delay, which needs to be guaranteed by the customer);
- Supports sending or receiving standard frames;
- Supports sending or receiving extended frames

|   Considering the flexibility of different product applications, the 2 CANs are respectively multiplexed in several different power domains, distinguished by suffixes M0/M1 for different multiplexing positions. IOMUX_M0/M1 cannot be used at the same time. Only one group can be selected during allocation. For example: if CAN_M0 is selected, CAN_M1 cannot be selected again.
|   The signal connection of the CAN interface is shown in the following figure:  
  
.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw14-2.png
   :alt: hw14-2.png
   :width: 90%

|   Precautions for the design of the CAN interface:

- Adjust the power supply of the corresponding power domain according to the IO level of the CAN peripheral to ensure consistency.
- When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (between 22ohm-100ohm, subject to meeting SI test requirements) in series and reserve TVS devices.  

15. I2C
---------

|   The RV1126B chip has 6 I2C controllers, supporting the following functions:

- Supports I2C bus master mode, not slave mode;
- The maximum software programmable clock frequency and transmission rate can reach 1M bit/s;
- Supports 7-bit and 10-bit addressing modes.

|   Considering the flexibility of different product applications, the 6 I2Cs are respectively multiplexed in several different power domains, distinguished by suffixes M0/M1/M2/M3 for different multiplexing positions. IOMUX_M0/M1/M2/M3 cannot be used at the same time. Only one group can be selected during allocation. For example: I2C1_M0 cannot be selected together with I2C1_M1, I2C1_M2, or I2C1_M3.
|   The signal connection of the I2C interface is shown in the following figure:  

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw15-1.png
   :alt: hw15-1.png
   :width: 90%

|   The distribution of the I2C interface is as follows:  

+------------+---------------------+------------------------------------------------+
| I2C Number | Multiplexing Status | Multiplexing Power Domain                      |
+------------+---------------------+------------------------------------------------+
| I2C0       | M0, M1              | M0: PMUIO1; M1: VCCIO2                         |
+------------+---------------------+------------------------------------------------+
| I2C1       | M0, M1, M2, M3      | M0: PMUIO0; M1: VCCIO3; M2: VCCIO4; M3: VCCIO7 |
+------------+---------------------+------------------------------------------------+
| I2C2       | M0, M1, M2          | M0: PMUIO1; M1: VCCIO5; M2: VCCIO6             |
+------------+---------------------+------------------------------------------------+
| I2C3       | M0, M1, M2, M3      | M0: PMUIO1; M1: VCCIO4; M2: VCCIO5; M3: VCCIO6 |
+------------+---------------------+------------------------------------------------+
| I2C4       | M0, M1, M2, M3      | M0: VCCIO3; M1: VCCIO6; M2: VCCIO4; M3: VCCIO7 |
+------------+---------------------+------------------------------------------------+
| I2C5       | M0, M1, M2, M3      | M0: PMUIO1; M1: VCCIO3; M2: VCCIO5; M3: VCCIO6 |
+------------+---------------------+------------------------------------------------+

|   The matching design of the I2C interface is shown in the following table:  

+----------+-------------------+-------------------------+
| Signal   | Connection Method | Description (Chip Side) |
+----------+-------------------+-------------------------+
| I2Cx_SCL | Direct Connection | I2C Clock               |
+----------+-------------------+-------------------------+
| I2Cx_SDA | Direct Connection | I2C Data Output/Input   |
+----------+-------------------+-------------------------+

|   Precautions for the design of the I2C interface:

- Adjust the power supply of the corresponding power domain according to the IO level of the I2C peripheral to ensure level consistency;
- The I2C signals SCL and SDA need to be externally pulled up with resistors. Different resistance values should be selected according to different bus loads. It is recommended to connect 2.2-4.7kohm pull-up resistors.
- The addresses of each device on the I2C bus should not conflict, and the pull-up power supply must be consistent with the GPIO power domain power supply.
- When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (between 22ohm-100ohm, subject to meeting SI test requirements) in series and reserve TVS devices.  

16. SPI
----------

+------------+---------------------+------------------------------------+
| SPI Number | Multiplexing Status | Multiplexing Power Domain          |
+------------+---------------------+------------------------------------+
| SPI0       | M0, M1, M2          | M0: PMUIO0; M1: VCCIO4; M2: VCCIO5 |
+------------+---------------------+------------------------------------+
| SPI1       | M0, M1, M2          | M0: VCCIO6; M1: VCCIO3; M2: VCCIO5 |
+------------+---------------------+------------------------------------+

|   Adjust the power supply of the corresponding power domain according to the IO level of the SPI peripheral to ensure consistency. The matching design of the SPI interface is shown in the following table:  

+-----------+-------------------+--------------------------+
| Signal    | Connection Method | Description (Chip Side)  |
+-----------+-------------------+--------------------------+
| SPIx_CLK  | Direct Connection | SPI Clock                |
+-----------+-------------------+--------------------------+
| SPIx_MOSI | Direct Connection | SPI Data Output (Master) |
+-----------+-------------------+--------------------------+
| SPIx_MISO | Direct Connection | SPI Data Input (Master)  |
+-----------+-------------------+--------------------------+
| SPIx_CS0  | Direct Connection | SPI Chip Select 0        |
+-----------+-------------------+--------------------------+
| SPIx_CS1  | Direct Connection | SPI Chip Select 1        |
+-----------+-------------------+--------------------------+
  
|   Precautions for the design of the SPI interface:

- When realizing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (between 22ohm-100ohm, subject to meeting SI test requirements) in series and reserve TVS devices.

|   Due to differences in interface design, the operating rates of different SPI interfaces are as follows:  

+----------------------------------+------------------+
| Interface                        | Maximum CLK Rate |
+----------------------------------+------------------+
| SPI1_M1                          | 50MHz            |
+----------------------------------+------------------+
| SPI0_M0                          | 24MHz            |
+----------------------------------+------------------+
| SPI0_M1/SPI0_M2, SPI1_M0/SPI1_M2 | 20MHz            |
+----------------------------------+------------------+

17. PWM
----------

|   The RV1126B chip integrates 4 independent PWM controllers, supporting up to 28 PWM channels. The PWM0 controller has 8 channels (PWM0_CH0~PWM0_CH7), the PWM1 controller has 4 channels (PWM1_CH0~PWM1_CH3), the PWM2 controller has 8 channels (PWM2_CH0~PWM2_CH7), and the PWM3 controller has 8 channels (PWM3_CH0~PWM3_CH7). All PWM controllers support the following functions:

- Supports capture mode;  
- Supports continuous mode or one-shot mode;
- Each channel has two optional clock inputs: one is a fixed frequency input from the crystal oscillator, and the other is a configurable frequency divided from the PLL bus;

|   The functional differences between different PWM controllers are as follows:

- The waveform generator can implement the breathing light function through hardware without consuming CPU;
- IR input can realize infrared input;
- Two-phase counters are often used for multi-motor control, such as sweeping robots;

+-------------------------------------------+------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| Function                                  | PWM0_8CH                                                         | PWM1_4CH                                  | PWM2_8CH                                                                      | PWM3_8CH                                                         |
+-------------------------------------------+------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| Waveform Generator                        | NO                                                               | NO                                        | All 8 channels are supported, sharing a lookup table (depth 768).             | NO                                                               |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
|                                           |                                                                  |                                           | Examples: 1 channel with 768 granularity; 3 channels with 256 granularity;    |                                                                  |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
|                                           |                                                                  |                                           | 6 channels with 128 granularity. All 8 channels are supported,                |                                                                  |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
|                                           |                                                                  |                                           | sharing a lookup table (depth 768). Examples: 1 channel with 768 granularity; |                                                                  |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
|                                           |                                                                  |                                           | 3 channels with 256 granularity; 6 channels with 128 granularity.             |                                                                  |
+-------------------------------------------+------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| IR Input                                  | NO                                                               | Only 1 channel is supported, which can be | NO                                                                            | NO                                                               |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
|                                           |                                                                  | arbitrarily configured among PWM1_CH0~3   |                                                                               |                                                                  |
+-------------------------------------------+------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| IR Output                                 | NO                                                               | NO                                        | NO                                                                            | NO                                                               |
+-------------------------------------------+------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| Two-Phase Counter                         | Supports 4 two-phase counters (can be used as frequency counters | NO                                        | Supports 4 two-phase counters (can be used as frequency counters              | Supports 4 two-phase counters (can be used as frequency counters |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
|                                           | with single phase, supporting 20M frequency). CH0+CH4 form one   |                                           | with single phase, supporting 20M frequency). CH0+CH4 form one                | with single phase, supporting 20M frequency). CH0+CH4 form one   |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
|                                           | two-phase counter; CH1+CH5 form one two-phase counter; CH2+CH6   |                                           | two-phase counter; CH1+CH5 form one two-phase counter; CH2+CH6                | two-phase counter; CH1+CH5 form one two-phase counter; CH2+CH6   |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
|                                           | form one two-phase counter; CH3+CH7 form one two-phase counter   |                                           | form one two-phase counter; CH3+CH7 form one two-phase counter                | form one two-phase counter; CH3+CH7 form one two-phase counter   |
+-------------------------------------------+------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| Global Control Mode (Supports synchronous | YES                                                              | YES                                       | YES                                                                           | YES                                                              |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
| update of multi-channel configuration)    |                                                                  |                                           |                                                                               |                                                                  |
+-------------------------------------------+------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| Output Offset Mode (PWM output            | YES                                                              | YES                                       | YES                                                                           | YES                                                              |
+                                           +                                                                  +                                           +                                                                               +                                                                  +
| waveform offset by specified time)        |                                                                  |                                           |                                                                               |                                                                  |
+-------------------------------------------+------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------+

|   Considering the flexibility of different product applications, the 28 PWM channels are respectively multiplexed in several different power domains, with suffixes M0/M1/M2 distinguishing different multiplexing positions. IOMUX_M0/M1/M2 cannot be used simultaneously; only one group can be selected during allocation. For example: if PWM_CH0_M0 is selected, PWM_CH0_M1 or other PWM_CH0_M* cannot be selected again.  
|   The distribution of RV1126B PWM interfaces is shown in the following table:

+------------+---------------------+------------------------------------+
| PWM Number | Multiplexing Status | Multiplexing Power Domain          |
+------------+---------------------+------------------------------------+
| PWM0_CH0~3 | M0, M1, M2          | M0: PMUIO1; M1: VCCIO5; M2: VCCIO6 |
+------------+---------------------+------------------------------------+
| PWM0_CH4~7 | M0, M1, M2          | M0: PMUIO1; M1: VCCIO4; M2: VCCIO5 |
+------------+---------------------+------------------------------------+
| PWM1_CH0~3 | M0, M1, M2          | M0: PMUIO0; M1: VCCIO5; M2: VCCIO6 |
+------------+---------------------+------------------------------------+
| PWM2_CH0~3 | M0, M1, M2          | M0: VCCIO3; M1: VCCIO5; M2: VCCIO6 |
+------------+---------------------+------------------------------------+
| PWM2_CH4~7 | M0, M1              | M0: VCCIO5; M1: VCCIO7             |
+------------+---------------------+------------------------------------+
| PWM3_CH0~7 | M0, M1              | M0: VCCIO1; M1: VCCIO5             |
+------------+---------------------+------------------------------------+
    
|   Precautions for PWM interface design:

- Adjust the power supply of the corresponding power domain according to the IO level of the PWM peripheral to ensure consistent levels.
- When implementing board-to-board connection through a connector, it is recommended to connect a resistor of a certain resistance value (between 22ohm-100ohm, subject to meeting SI test requirements) in series and reserve TVS devices.
- When inputting signals from an infrared receiver, the following points should be noted:

  - In standby mode, to support wake-up by the infrared receiver and consider low power consumption (i.e., LOGIC_DVDD power-off scheme), only PWM1_CH0~3 can be selected as the infrared receiver input;
  - The power supply of the infrared receiver needs to use the supply voltage of the PMUIO1_VCC pin;
  - The power supply of the infrared receiver requires RC filtering with a 22-100ohm resistor and a capacitor of 10uF or more;
  - The infrared receiver defaults to 38KHz; if replaced with another frequency, the software needs to be adjusted accordingly;
  - The output level of the infrared receiver must match the RV1126B IO level;
  - It is recommended to connect a 22ohm resistor in series and a 1nF capacitor in parallel to the output pin of the infrared receiver before connecting to RV1126B to enhance anti-static surge capability.

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw17-1.png
   :alt: hw17-1.png
   :width: 90%

- When laying out the infrared receiver, it should be far away from wireless module antennas (such as Wi-Fi antennas) to avoid interference with infrared signal reception during wireless data transmission.
- The layout of the infrared receiver should avoid direct exposure to on-board LED light sources to prevent the LED blinking frequency from affecting infrared reception.
- It is recommended to use full ground shielding for IR signals; if ground shielding is not feasible, the spacing between IR signals and other signals should be ≥2 times the line width.

18. WIFI&BT
--------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw18-1.png
   :alt: hw18-1.png
   :width: 90%

|   1. Uses the BL-8723DU module.
|   2. Supports 2.4G WIFI and Bluetooth 5.0.

19. Buttons
--------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw19-1.png
   :alt: hw19-1.png
   :width: 90%

|   1. The development board uses SARADC_IN0 (ESC/RECOVERY, MENU, LEFT, RIGHT) as button detection ports, supporting 13-bit resolution. The functions of the 4 ADC KEY buttons can be configured independently through software.  
|   Press and hold the button during power-on to enter RECOVERY mode.

20. Pin Header
----------------

.. image:: /image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/hw20-1.png
   :alt: hw20-1.png
   :width: 90%

|   1. 40Pin pin header.
|   2. Includes GPIO, I2C, and ADC interfaces.