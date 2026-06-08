Hardware Design Guidelines
============================

1. Power Supply
-----------------

| The power adapter inputs 12V/3A power, which is converted by a front-end buck converter to obtain the system power supply VCC5V0_SYS_S5. This system voltage is then provided to the PMIC power management chip, which outputs different voltages for the system to use.
| Power-on sequence:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导1.png
   :alt: 硬件设计指导1.png
   :width: 90%

**12V**

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导2.png
   :alt: 硬件设计指导2.png
   :width: 90%

**5V**

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导3.png
   :alt: 硬件设计指导3.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导4.png
   :alt: 硬件设计指导4.png
   :width: 90%

**3.3V**

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导5.png
   :alt: 硬件设计指导5.png
   :width: 90%

**VCC3.3_RTC**

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导6.png
   :alt: 硬件设计指导6.png
   :width: 90%

**1.8V**

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导7.png
   :alt: 硬件设计指导7.png
   :width: 90%


2. Flashing
-------------

| The USB3 OTG0 controller supports SS/HS/FS/LS. The built-in USB2.0 (HS/FS/LS) signals use the USB2.0 OTG PHY, and the signal names are shown in the red box in the figure below. RK3576 uses this interface by default for firmware download. This interface must be reserved in applications.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导8.png
   :alt: 硬件设计指导8.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导9.png
   :alt: 硬件设计指导9.png
   :width: 90%

3. USB
--------

USB3.0
~~~~~~~~

| Note the following in USB2/USB3 design:
| ⚫ USB2_OTG0_DP/USB2_OTG0_DM is the system firmware flashing port. If the product does not use this interface, it must be reserved during debugging and production; otherwise, debugging and production firmware flashing will be impossible.
| ⚫ USB2_OTG0_ID has an internal pull-up resistor of approximately 12Kohm to USB2_OTG_AVDD1V8.
| ⚫ USB20_OTG0_VBUSDET is the detection pin for OTG and Device modes. The chip has an internal 40Kohm pull-down resistor. A high level (2.7-3.3V, TYP: 3.0V) indicates Device mode. It is recommended to place a 100nF capacitor on the pin. OTG mode can be set to the following three modes:
| ⚫ OTG mode: Automatically switches between Device mode and HOST mode based on the ID pin state. A high ID indicates Device mode, and a pulled-down ID indicates HOST mode. In Device mode, it also checks if the VBUSDET pin is high (greater than 2.3V); if so, it pulls up DP to start enumeration.
| ⚫ Device mode: In this mode, the ID pin is not required. It only checks if the VBUSDET pin is high (greater than 2.3V); if so, it pulls up DP to start enumeration.
| ⚫ HOST mode: In this mode, the states of the ID and VBUSDET pins are irrelevant. (If the product only requires HOST mode, but since USB2_OTG0_DP/USB2_OTG0_DM is the system firmware flashing port and is needed during debugging and production, Device mode must be set during flashing and adb debugging. Therefore, the USB2_OTG0_VBUSDET signal must also be connected.) It defaults to Device mode before uboot starts. After entering uboot, these three modes can be configured according to actual needs.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导10.png
   :alt: 硬件设计指导10.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导11.png
   :alt: 硬件设计指导11.png
   :width: 90%

USB2.0
~~~~~~~

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导12.png
   :alt: 硬件设计指导12.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导13.png
   :alt: 硬件设计指导13.png
   :width: 90%

4. WIFI
---------

| For the wiring of the WIFI antenna, note that a π-type circuit should be used for filtering.
| The wiring of the WIFI antenna is best fully grounded.

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导14.png
   :alt: 硬件设计指导14.png
   :width: 90%

5. SD Card
------------

| RK3576 integrates 2 SDMMC controllers, both supporting the SDIO3.0 protocol and MMC V4.51 protocol. They have a 4-wire data bus width and support SDR104 mode with a maximum rate of 200MHz.

**SDMMC0 Interface**

| ⚫ The SDMMC0 interface is multiplexed in the VCCIO1 power domain.
| ⚫ SDMMC0 supports System Boot and is assigned to the SD card function by default. It supports firmware upgrade via the SD card when EMMC/UFS is empty, and also supports upgrading EMMC/UFS via the SD card after EMMC/UFS booting.
| ⚫ SDMMC0 is multiplexed with functions such as JTAG. Function selection is determined by the SDMMC_DETN state by default. For details, refer to section 2.1.6.
| ⚫ VCCIO1 power supply requires an external 3.3V or 1.8V power supply.
| ⚫ When connecting an SDIO device: Supply 1.8V or 3.3V according to the peripheral and actual operating mode. When implementing board-to-board connection via a connector, it is recommended to connect a resistor with a certain value (between 22ohm-100ohm, subject to meeting SI test requirements) in series and reserve TVS devices.
| ⚫ When using an SD card, note the following:

1. The VDD pin of the SD card is supplied with 3.3V. Decoupling capacitors must not be omitted and should be placed close to the card holder during layout.
2. SDMMC_D[3:0], SDMMC_CMD, and SDMMC_CLK need a 22ohm series resistor, and SDMMC_DETN needs a 100ohm series resistor.
3. ESD devices must be placed at the SD card position for SDMMC_D[3:0], SDMMC_CMD, SDMMC_CLK, and SDMMC_DETN signals. For SD3.0 mode support, the junction capacitance of the ESD device must be less than 1pF; for SD2.0 mode only, it can be relaxed to 9pF.
4. When using the SDMMC0 detection BOOT gear, GPIO0_B6 where SDMMC0_PWREN is located will output a high level. SDMMC0_PWREN is directly used to control the enable of the SD card power supply Load switch, without needing inversion via a triode. Note that if the pull-up process of SDMMC0_PWREN detected by SDMMC0 affects the peripheral state, this IO should not be used to control sensitive peripherals. For example, when SARADC_IN0_BOOT is configured to Config8, the system will still detect the SD card after UFS booting, and SDMMC0_PWREN will be pulled high briefly. If there is no SD card in the hardware, do not use this IO to control sensitive peripherals. It is recommended to configure SARADC_IN0_BOOT to Config7 instead of Config8 when no SD card is needed.
5. When SDMMC is connected to an SD card, pay attention to the design of the SD card power supply to ensure that the power supply of the SD card powers down quickly, avoiding logical confusion caused by incomplete power-down and re-power-up during quick insertion/removal.
6. For low-power scenarios, note that if an SD card is inserted, SDMMC0_DETN will be pulled low continuously, resulting in relatively large current. For power-sensitive customers, it is recommended that the software configure the internal SDMMC0_DETN pin of the SoC to high-impedance state, and change the external pull-up resistor to 100k.
7. Recommended pull-up/down and matching designs for the SDMMC0 interface are as shown in the table:

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导15.png
   :alt: 硬件设计指导15.png
   :width: 90%

.. figure:: /image/MYZR-瑞芯微系列/MYZR-RK3576-EK288/硬件设计指导16.png
   :alt: 硬件设计指导16.png
   :width: 90%

**SDMMC1 Interface**

| ⚫ The SDMMC1 interface is multiplexed in two positions: one in the VCCIO3 power domain and one in the VCCIO4 power domain. Only one can be used; either all in the VCCIO3 power domain or all in the VCCIO4 power domain. Mixing is not supported.
| ⚫ System Boot is not supported.
| ⚫ VCCIO3 and VCCIO4 power supplies are 1.8V or 3.3V, selected according to peripheral requirements. Note the recommended pull-up/down and matching designs for the SDMMC1 interface with the peripheral as shown in the table. When implementing board-to-board connection via a connector, it is recommended to connect a resistor with a certain value (between 22ohm-100ohm, subject to meeting SI test requirements) in series and reserve TVS devices.
| ⚫ Notes when SDMMC is connected to Wi-Fi:

1. Ensure the IO level of the module matches that of the CPU; otherwise, level matching is required.
2. Select the crystal load capacitor according to the CL capacitance value of the actual crystal used, and control the frequency tolerance within 10ppm at room temperature.
3. Reserve a π-type circuit for the antenna for antenna matching adjustment.
4. Confirm the connection direction of the PCM and UART interfaces, such as IN and OUT, TXD and RXD.
5. For modules requiring a 32.768k clock input, the RTC chip output needs a pull-up resistor, and the pull-up voltage or voltage division must meet the parameters of the Wi-Fi module.

6. MIPI-CSI
-------------

| RK3576 has two MIPI DPHY CSI RX interfaces, both supporting MIPI V1.2. Each channel has a maximum transmission rate of 2.5Gbps. Supported modes for MIPI DPHY CSI1/2 RX interfaces:
| ⚫ 4Lane mode: MIPI_DPHY_CSI1_RX_D[3:0] data is referenced to MIPI_DPHY_CSI1_RX_CLK.
| ⚫ 2Lane+2Lane mode:
| ◼ MIPI DPHY CSI1_RX_D[1:0] data is referenced to MIPI_DPHY_CSI1_RX_CLK.
| ◼ MIPI DPHY CSI2_RX_D[1:0] data is referenced to MIPI_DPHY_CSI2_RX_CLK.
| Supported modes for MIPI DPHY CSI3/4 RX interfaces:
| ⚫ 4Lane mode: MIPI_DPHY_CSI3_RX_D[3:0] data is referenced to MIPI_DPHY_CSI3_RX_CLK.
| ⚫ 2Lane+2Lane mode:
| ◼ MIPI DPHY CSI3_RX_D[1:0] data is referenced to MIPI_DPHY_CSI3_RX_CLK.
| ◼ MIPI DPHY CSI4_RX_D[1:0] data is referenced to MIPI_DPHY_CSI4_RX_CLK.
| RK3576 has one MIPI DCPHY CSI RX Combo PHY; DPHY supports V2.0, and CPHY supports V1.1. DPHY mode has 4Lanes with a maximum transmission rate of 4.5Gbps/Lane; CPHY mode has 3Trios with a maximum transmission rate of 5.7Gbps/Trio. Supported configurations for DPHY and CPHY:
| ⚫ The TX and RX of the MIPI DCPHY Combo PHY can only be configured simultaneously as DPHY TX and DPHY RX, or simultaneously as CPHY TX and CPHY RX. Configuring one as DPHY TX and the other as CPHY RX, or vice versa, is not supported. Supported modes when MIPI DCPHY works in DPHY mode:
| ⚫ Supports 4Lane/2Lane/1Lane modes. MIPI_DPHY_CSI0_RX[3:0] data is referenced to MIPI_DPHY_CSI0_RX_CLK. Splitting into 2Lane+2Lane is not supported.
| Supported modes when MIPI DCPHY works in CPHY mode:
| ⚫ Supports 0/1/2 Trios. Each Trio has 3 lines: Trio_A/Trio_B/Trio_C. MIPI_CPHY_CSI_RX_TRIO[2:0]_A, MIPI_CPHY_CSI_RX_TRIO[2:0]_B, MIPI_CPHY_CSI_RX_TRIO[2:0]_C.
| Notes for MIPI DCPHY CSI RX Combo PHY design:
| ⚫ To improve the performance of the MIPI DCPHY CSI RX Combo PHY, decoupling capacitors for each power supply of the PHY must not be removed and should be placed close to the pins during layout (note that the power supplies of MIPI DCPHY CSI RX and MIPI DCPHY DSI TX are merged into one).
| ⚫ Selection of MIPI_DCPHY_AVDD voltage: When the MIPI rate is higher than DPHY 2.5Gbps or CPHY 1.5Gsps, configure MIPI_DCPHY_AVDD to 0.85V; when lower, configure to 0.75V. The 1uF capacitor for MIPI_DCPHY_VREG must not be removed and must be placed close to the corresponding pin during layout. The DVDD power supply for the camera can be 1.2V/1.5V/1.8V, etc. Provide the accurate power supply according to the camera's datasheet; the reference circuit defaults to 1.2V.
| ⚫ For cameras with large DVDD current (exceeding 100mA), it is recommended to use DCDC power supply. The power supplies of the camera have power-on sequence requirements; adjust the power-on sequence according to the camera's datasheet. The default power-on sequence in the reference diagram is: 1.8V-->1.2V-->2.8V.
| ⚫ When using a camera with a CIF interface, ensure the DOVDD (IO power) of the camera and the VCCIO6 power supply use the same voltage.
| ⚫ When using two cameras, their power supplies can be separated or merged according to actual needs; the reference diagram defaults to separation.
| ⚫ If the camera has AF function, VCC2V8_AF needs a separate power supply; or it can share with AVCC2V8_DVP, but must be isolated with a bead.
| ⚫ Decoupling capacitors for all power supplies of the camera must not be removed and must be placed close to the socket.
| ⚫ The PWDN signal of the camera must be controlled by a GPIO, and the GPIO level must match the camera's IO level.
| ⚫ The Reset signal of the camera is recommended to be controlled