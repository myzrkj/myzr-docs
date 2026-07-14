.. raw:: html

   <style>
   h1 {
       color: green;
   }
   </style>

Product Introduction
====================

Core Board Introduction
-----------------------

Hardware Resources
~~~~~~~~~~~~~~~~~~

The MYZR-RV1126B core board is developed based on the RV1126B processor, integrating DDR memory, Flash storage, power supply, clock and other basic circuits required by the main controller, and can be directly used as a complete machine main control module.

The processor integrates:

* Quad-core ARM Cortex-A53 CPU (1.5GHz) + 300MHz RISC-V MCU, balancing main computing power and low-power real-time scheduling

* Self-developed 3TOPS NPU, compatible with multi-precision quantization, Transformer optimization, supports running large models within 2B parameters

* Independent AI-ISP image processing unit, equipped with AIRemosaic, 6-DOF hardware anti-shake, multi-view panoramic stitching engine

* AOV3.0 low-power audio processing unit, integrated onboard AudioCodec audio codec

* 4-channel Sensor video input module, MIPI/RGB display output module

* DDR high-speed controller, built-in 100Mbps Ethernet PHY

* National cryptographic security engine, equipped with TrustZone, Keyladder key management system

* USB3.0 and various general on-chip peripheral resources

Core Board Specifications
-------------------------

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
       text-align: center;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
       text-align: center;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+---------------------------+-----------+------------------------------------------------------+
| Core Board Specifications                                                                    |
+===========================+===========+======================================================+
| 1                         | Model     | MYZR-RV1126B-LB221                                   |
+---------------------------+-----------+------------------------------------------------------+
| 2                         | Size      | 33.0mm × 32.0mm                                      |
+---------------------------+-----------+------------------------------------------------------+
| 3                         | PCB       | 10-layer 2-stage blind/buried via ENEPIG, LGA 221pin |
+---------------------------+-----------+------------------------------------------------------+
| 4                         | Memory    | LPDDR4X 2/4/8GByte                                   |
+---------------------------+-----------+------------------------------------------------------+
| 5                         | Storage   | eMMC 8/16/32/64GB                                    |
+---------------------------+-----------+------------------------------------------------------+
| 6                         | Boot Mode | SPI NOR, NAND, SD Card, eMMC, USB, UART multi-boot   |
+---------------------------+-----------+------------------------------------------------------+

Core Board Top/Bottom Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div style="display: flex; justify-content: space-around;">
   <div style="text-align: center; width: 45%;">

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/核心板正反图.png
   :alt: MYZR-RV1126B Core Board Top View
   :width: 100%

**MYZR-RV1126B Core Board Top View**

.. raw:: html

   </div>
   <div style="text-align: center; width: 45%;">

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/核心板背面图.jpg
   :alt: MYZR-RV1126B Core Board Bottom View
   :width: 100%

**MYZR-RV1126B Core Board Bottom View**

Core Board Dimensions
~~~~~~~~~~~~~~~~~~~~~

Core Board Mechanical Drawing [33.53mm × 32.38mm]

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/核心板尺寸图.jpg
   :alt: Core Board Dimensions
   :width: 100%

Core Board Naming Convention and Optional Configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+------------------+------------+-------------------------------+-----------------+------------+
| Core Board Model |         Naming Convention                                                 |
+==================+============+===============================+=================+============+
|                  | MYZR       | RV1126B                       | LB/EK           | 221        |
+                  +------------+-------------------------------+-----------------+------------+
|                  | MYZR       | MPU Main Controller Model     | LB [Core Board] | Pin Count  |
+                  +------------+-------------------------------+-----------------+------------+
|                  |            | RV1126B [Commercial Grade]    | EK [Dev Board]  |            |
+                  +------------+-------------------------------+-----------------+------------+
| MYZR-RV1126B     |            | RV1126BJ [Industrial Grade]   |                 |            |
+                  +------------+-------------------------------+-----------------+------------+
|                  |                        Optional Configurations                            |
+                  +------------+-------------------------------+-----------------+------------+
|                  | Memory: LPDDR4X 2/4/8GByte                                                |
+                  +------------+-------------------------------+-----------------+------------+
|                  |                        Storage: 8/16/32/64GByte eMMC                      |
+                  +------------+-------------------------------+-----------------+------------+
|                  |                        Example: MYZR-RV1126B-LB221-2G-8G                  |
+------------------+------------+-------------------------------+-----------------+------------+

Power Supply
~~~~~~~~~~~~

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+----------+----------+-----------+-----------+-----------+------+------+
| Function | Pin Label| Spec-Min  | Spec-Typ  | Spec-Max  | Unit | Note |
+==========+==========+===========+===========+===========+======+======+
| Power    | CON1     | 11.8      | 12        | 12.2      | V    | Base |
+----------+----------+-----------+-----------+-----------+------+------+

Operating Environment
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+-----------+-------+-------+-------+------+------------------+
| Parameter | Min   | Typ   | Max   | Unit | Description      |
+===========+=======+=======+=======+======+==================+
| Commercial| 0°C   | 25°C  | 70°C  | °C   | Tested 0-60°C    |
+-----------+-------+-------+-------+------+------------------+
| Industrial| 0°C   | 25°C  | 80°C  | °C   | Tested 0-70°C    |
+-----------+-------+-------+-------+------+------------------+

Boot Configuration
~~~~~~~~~~~~~~~~~~

* eMMC Boot

Fast Boot Support and Boot Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+----------+----------+------+
| Item     | Support  | Time |
+==========+==========+======+
| RV1126B  | No       |      |
+----------+----------+------+ 

Core Board Power Consumption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+------------------------------------+-----------+---------+-----------+---------+
| Type                               |    Standby Power    |    Full Load Power  |
|                                    +-----------+---------+-----------+---------+
|                                    | Current   | Power   | Current   | Power   |
+====================================+===========+=========+===========+=========+
| MYZR-RV1126B Dev Board             |   140mA   | 1.680W  | 210mA     | 2.520W  |
+------------------------------------+-----------+---------+-----------+---------+
| Note: Values are current (mA), voltage is 5.0V, full load is all cores running |
+------------------------------------+-----------+---------+-----------+---------+

Core Board Mounting/Soldering Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/核心板贴片_安装示意图.png
   :alt: Core Board Mounting/Soldering Diagram
   :width: 100%

Signal Definition
~~~~~~~~~~~~~~~~~

Core Board Pinout

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Pin NO.
     - Pin Name
     - Description
   * - A1
     - PWM0_CH1_M0
     - UART1_RX_M0/I2C5_SDA_M0/PWM0_CH1_M0/SPI2AHB_D2/GPIO00_
   * - A2
     - GPIO0_AO_Z
     - TEST_CLKO_OUT/REF_CLKO_OUT/GPIO0O_AO_Z
   * - A3
     - UART0_TX_DBG
     - JTAG_TCK_M0 /I2C1_SCL_M0 / PWM1_CH2_M0 /UART0_TX_M2 / GPI000
   * - A4
     - UART0_RX_DBG
     - JTAG_TMS_M0/I2C1_SDA_M0/ PWM1_CH3_M0 / UART0_RX_M2/ GPIO00
   * - A5
     - GND
     - 
   * - A6
     - VCC_1V8
     - 
   * - A7
     - VCC_1V8
     - 
   * - A8
     - FSPI_DO
     - SAI1_LRCK_M0/FSPI0_D0/GPIO1_B4_U
   * - A9
     - FSPI_CSN
     - SAI1_MCLK_M0 / FSPI1_CSN0_M1/ FSPI0_CSN0 / GPIO1_B0_U
   * - A10
     - FSPI_D2
     - SAI1_LRCK_M0/FSPI0_D2/GPIO1_B2_U
   * - A11
     - IRCUT_A0
     - I2C3_SCL_M2/DSMSCSN3/ETPTP REFCLKPM1/PWM0_CH6_M
   * - A12
     - SDMMC0_VOL_CTRL
     - SPI0_CS1N_M0/FSPI1_D2_M0/GPIO00_A6_U
   * - A13
     - SDMMC0_CMD
     - UART4_TX_M3/UART3_CTSN_M0/ SDMMC0_CMD/GPIO2_A5_D
   * - A14
     - SDMMC0_D2
     - TEST_CLK1_OUT/JTAG_TCK_M1/UART4RTSNM3/ART3_RX_M0/ SDMM
   * - A15
     - SDMMC0_DO
     - I2C0_SDA_M1/UART0_RX_M0/SDMMC0_D0/GPIO2_A0_D
   * - A16
     - SDMMC0_CLK
     - UART4_RX_M3/UART3_RTSN_M0/ SDMMC0_CLK/GPIO2_A4_D
   * - B1
     - ETH_LED_SPD
     - SARADC2ETHXCMM/FHYCMHYD
   * - B2
     - SARADC0_INO_KEY
     - SARADC0INO_KEY
   * - B3
     - RESET
     - RESET
   * - B4
     - SDIO_D1
     - I2C1_SDA_M1/SDMMC1_D1/GPIO3_A3_D
   * - B5
     - GND
     - 
   * - B6
     - VCC_1V8
     - 
   * - B7
     - FSPI_CLK
     - FSPI0_CLK/GPIO1_B7_D
   * - B8
     - FSPI_D1
     - SAI1_SCLK_M0/FSPI0_D1/GPIO1_B5_U
   * - B9
     - FSPI_D3
     - SAI1_SDI_M0/FSPI0_D3/GPIO1_B6_U
   * - B10
     - IRCUT_B1
     - DSMC_INT2/UART3_CTSN_M1/PWM1SHD3M1/SPI_MISO_M2/VO_LCD
   * - B11
     - IRCUT_B0
     - RCUTO
   * - B12
     - IRCUT_A1
     - DSMC_INT3/UART3 RTSNMP/GCH⊥M1/SPI1_MOSM2/
   * - B13
     - SDMMC0_PWREN
     - SPI0_MOSI_M0/FSPI1_DO_M0/GPIO0O_BO_D
   * - B14
     - SDMMC0_DET
     - PWM1_CH0_M0/SDMMC0_DET/GPIO00_A5_U
   * - B15
     - SDMMC0_D3
     - SDMMC0D3
   * - B16
     - SDMMC0_D1
     - SDMMC0D1
   * - C1
     - ETH_LED_ACT
     - SARADC2_IN6/ETHXCLKMM/WOIFCLKMUTMO6EHYLEDLINK
   * - C2
     - FEPHY_TXN
     - EPHVXN
   * - C3
     - FEPHY_RXP
     - FEPHYRXP
   * - C4
     - FEPHY_TXP
     - FEPHYTXP
   * - C5
     - SDIO_DO
     - I2C1_SCL_M1/SDMMC1_D0/GPIO3_A2_D
   * - C6
     - SDIO_D3
     - SDMMC1_D3/GPIO3_A5_D
   * - C7
     - UART2_TX_BT
     - UART2_TX_M0/GPIO3_B1_D
   * - C8
     - SDIO_D2
     - SDMMC1_D2/GPIO3_A4_D
   * - C9
     - WIFI_WAKE_HOST_3V3
     - SPI0_MISO_M0/FSPI1_D1_M0/GPIO00_B1_D
   * - C10
     - CLK_32K_OUT
     - RTC_32K_OUT/CLK_32K/GPIO00_A2_Z
   * - C11
     - SARADC0_IN1_CDS
     - SARADC0_IN1_CDS
   * - C12
     - SENSOR_INT
     - SENSORINT
   * - C13
     - LED_PWM_IR
     - UART1_CTSN_M0 /PWM0_CH3_M0 / SPI2AHB_D0 /GPIO00_C7_D
   * - C14
     - LED_PWM_WHITE
     - UART1_RTSN_M0 /PWM0_CH2_M0 /SPI2AHB_D1/GPIO00_C6_D
   * - C15
     - I2C2_SDA_SENSOR
     - I2C2_SDA_M0/PWM0_CH5_M0/GPIO00_D1_D
   * - C16
     - I2C2_SCL_SENSOR
     - I2C2_SCL_M0/PWM0_CH4_M0/GPIO00_D0_D
   * - D1
     - GMAC_TXCTL_M1
     - DSMC_D5/ETH_TXCTL_M1/ PWM3CH2_M1/V_CIF_D14_M1/VO_LCDC
   * - D2
     - GPIO3_B2_D
     - FLASH_TRIG_OUT/WMCHOM/AI2SDMO/SAI2_SDO_M0
   * - D3
     - FEPHY_RXN
     - FEPHYRXN
   * - D4
     - FEPHY_TXN
     - FEPHYTXN
   * - D5
     - SDIO_CLK
     - SDMMC1_CLK/GPIO3_AO_D
   * - D6
     - UART2_CTSN_BT
     - UART2_CTSN_M0/GPIO3_A7_D
   * - D7
     - UART2_RTSN_BT
     - UART2_RTSN_M0/GPIO3_A6_D
   * - D8
     - HOST_WAKE_BT
     - SDMMCI_DETN/I2C5_SCL_M1/SA2MGLKMO/SPI_CSN1_M1/UART1
   * - D9
     - WIFI_REG_ON_3V3
     - SPI0_CLK_M0/FSPI1_CLK_M0/GPIO00_B2_D
   * - D10
     - GPIO00_A3_U
     - PWR_CTRLO/GPIO0O_A3_U
   * - D11
     - GMAC_RXCLK_M1
     - DSMC_DO/SAI1_SDI_M2/ETHLRXCLK2M1/PM3CH_M1/V_CIF_HSY
   * - D12
     - GMAC_RXD2_M1
     - GMAC_RXD2_M1
   * - D13
     - GMAC_MDIO_M1
     - DSMC_DQS0 /UART7_RX_M0 /VI_CIF_D13_M1/VO_LCDC_D13 /GPIO5_
   * - D14
     - GMAC_RXD1_M1
     - DSMC_RESETN/DSMCI1/THMDRGRTSMO/MC
   * - D15
     - GMAC_TXD1_M1
     - DSMC_D7/ETH_TXD1_M1/PWM3_CHS_M1/VI_CIF_D12_M1/VO_LCDC
   * - D16
     - GMAC_TXDO_M1
     - DSMC_CLKP/ETH_TXDO_M1/URT_CISNMI/5M2_CH3M1/V_CIF
   * - E1
     - GPIO3_B5_D
     - FEPHY_EDSPMS/PM2CHMC/2C4SAPMO/SAI2LRCK
   * - E2
     - GPIO3_B3_D
     - PRELIGHT_TRIG_OUT/PWM2_CHIMB/SAI2_SDIO_M0/SPI1_MISO_M
   * - E3
     - GPIO3_B4_D
     - FEPT_LEDESPI1_CLK M1/UART1 RTSN_M1/GPIO3_B4I2_SCEK_M
   * - E4
     - GPIO7_A5_D
     - SAI0_SDO0_M0/DSM_AUD_LP/GPIO7_A5_D
   * - E5
     - GND
     - 
   * - E6
     - GND
     - 
   * - E7
     - UART2_RX_BT
     - UART2_RX_M0/GPIO3_BO_D
   * - E8
     - BT_WAKE_HOST
     - I2C5_SDA_M1/ SAI2_SDI1_M0 /UART1_RX_M1 /GPIO3_B7_D
   * - E9
     - GND
     - 
   * - E10
     - GND
     - 
   * - E11
     - GND
     - 
   * - E12
     - VBAT_RTC
     - 
   * - E13
     - GMAC_RXD3_M1
     - DSMC_D3/SAI1_SDO_M2/ETRXD32M1/PM3CH4_M1/V_CIF_VSYN
   * - E14
     - GEPHY_RST_3V3IO
     - 
   * - E15
     - GMAC_TXCLK_M1
     - DSMC_D1/SA1_LRCKM2/TXCL2MM3CH_M/V_IF_L
   * - E16
     - CLK_OUT_ETHERNET_M1
     - DSMC_D6/ETH_CLK 25MCUT M17/PPM3_CHLM1/V_CIF_D13M
   * - F1
     - GPIO7_A0_D
     - SAI0_SCLK_M0/PWM2_CH4_M1/GPIO7_A0_D
   * - F2
     - GPIO7_A3_D
     - SAI0_LRCK_M0/DSM_AUD_LN/PWM2_CH7_M1/ GPIO7_A3_D
   * - F3
     - I2C4_SDA_M3
     - PDM_CLK0_M0/I2C4_SDA_M3/UART2_CTSN_M1/ GPIO7_A4_D
   * - F4
     - I2C4_SCL_M3
     - PDM_CLK1_M0/I2C4_SCL_M3/ PWM2_CH5_M1/GPIO7_A1_D
   * - F5
     - GND
     - 
   * - F6
     - GND
     - 
   * - F12
     - VBAT_RTC
     - 
   * - F13
     - GMAC_RXDO_M1
     - DSMC_D8/ETH_RXDO_M1/UARTM0/L_CIF_D9_M1/VO_CDC
   * - F14
     - GMAC_RXCTL_M1
     - DSMC_D9 /ETH_RXCTL_M1/UART6TXMO/V_CIFD8_M1/VO_LCDC
   * - F15
     - GMAC_TXD3_M1
     - DSMC_CSN1/ETH_TXD3_M1/UART4_RTNM5AWM2_CH4_M /V_CIF
   * - F16
     - GMAC_MDC_M1
     - DSMC_CLKN /DSMCINT/THMDC M/UR7RTS MO/PM2_CH
   * - G1
     - GPIO7_A0_D
     - SAI0_SCLK_M0/PWM2_CH4_M1/GPIO7_A0_D
   * - G2
     - GPIO7_A6_D
     - SAI0_SDI0_M0/PDM_SDI0_M0/GPIO7_A6_D
   * - G3
     - GPIO7_A7_D
     - SAI0_SDO1_M0 / SAI0_SDI3_M0/ PDM_SDI3_M0/ UART2_RTSN_M1/ GPIO
   * - G4
     - VCC5V0_SYS
     - 
   * - G5
     - GND
     - 
   * - G12
     - VBAT_RTC
     - 
   * - G13
     - USB_DRD_ID
     - USBDRDID
   * - G14
     - USB2_DRD_DP
     - USB2DRDDP
   * - G15
     - USB2_DRD_DM
     - 
   * - G16
     - USB2_DRD_VBUSDET
     - USB2_DRD_VBUSDET
   * - H1
     - VCC5V0_SYS
     - 
   * - H2
     - VCC5V0_SYS
     - 
   * - H3
     - VCC5V0_SYS
     - 
   * - H4
     - VCC5V0_SYS
     - 
   * - H5
     - GND
     - 
   * - H12
     - GND
     - 
   * - H13
     - USB2_HOST_DM
     - USB2HOST_DM
   * - H14
     - USB_DRD_SSTXN
     - USB_DRDSSTXN
   * - H15
     - USB_DRD_SSRXP
     - USB_DRD_SSRXP
   * - H16
     - GMAC_TXD2_M1
     - GMAC_TXD2_M1
   * - J1
     - GPIO6_B7_D
     - SARADC2_IN3/THMCMMICFD15MO/PDM_CLK1_M1/
   * - J2
     - GPIO6_C1_D
     - SARADC2_IN5/ETH_CLK 25MOCHM//GPIFCLKIN_M /UART3_CTS
   * - J3
     - GPIO6_B4_D
     - ETH_MCLK_M0/V_CIF_D12_M0/ PMGL4_M1 / SPI1_CLK_M0/UART7
   * - J4
     - SARADC0_IN2_BOM_ID
     - SARADC0_IN2_BOM_ID
   * - J5
     - SARADC0_IN6
     - SARADC0N6
   * - J12
     - GND
     - 
   * - J13
     - USB2_HOST_DP
     - USB2_HOST_DP
   * - J14
     - USB_DRD_SSTXP
     - USB_DRD_SSTXP
   * - J15
     - USB_DRD_SSRXN
     - USB_DRD_SSRXN
   * - J16
     - USB2_HOST_PWREN_H
     - DSMC_D11/SA2_SDCM/SCLK/ATTSNM/PWM_CH
   * - K1
     - GPIO6_B0_D
     - SARADC2INO/ETHMASM/IFM/SA_S
   * - K2
     - GPIO6_B3_D
     - ETHRXD1_M0/V_CRFCTSMOMMS3M1/SPI1_MISO_M0/
   * - K3
     - SARADC0_IN3
     - SARADC0N3
   * - K4
     - SARADC0_IN5
     - SARADC0N5
   * - K5
     - SARADC0_IN4
     - SARADC0IN4
   * - K12
     - GND
     - 
   * - K13
     - SPK_CTRL
     - PWR_CTRL1/GPIO00_A4_D
   * - K14
     - DSM_AUD_RN
     - SAIO_SDO2_M0/SAIO_SD2/PMMPMO72C1SCL_M3/DSM_AU
   * - K15
     - MIC1_P
     - C1
   * - K16
     - MIC1_N
     - CN
   * - L1
     - GPIO6_B6_D
     - SARADC2_IN2 /VI_CIF_D14_M0 /PDM_SDI1_M1 /UART7_RTSN_M1 / GPIO6
   * - L2
     - GPIO06_B5_D
     - SARADC2_IN1/ ETH_RXCTL_M0 /VI_CIF_D13_M0 / PDM_SDIO_M1/ UART7_
   * - L3
     - GPIO6_B2_D
     - ETHRXDO_M0/VCRRSMOMMS2M/SPI1_MOSMO/
   * - L4
     - GPIO6_B1_D
     - ETH_TXCTLMO/SAIO_SDVGMO/SIDIM1/PICS
   * - L5
     - SARADC0_IN7_BOOT
     - SARADC0_IN7_BOOT
   * - L12
     - VCCIO_SD
     - 
   * - L13
     - MIPI_CSI_RX0_D2P
     - MIPI_CSIRXOD2P
   * - L14
     - DSM_AUD_RP
     - SAIO_SDO3_M0/SAIO_SDPMMSPMO7C1SDA_M3/DSM_AU
   * - L15
     - MIC0_P
     - CO
   * - L16
     - MIPI_DPHY_CSI_RX0_CLK1N
     - MIPI_DPHY_CSI_RXO_CLKIN
   * - M1
     - GPIO6_C0_D
     - SARADC2HMM/MCVSCSCM/
   * - M2
     - VCC3V3_SYS
     - 
   * - M3
     - VCC_3V3
     - 
   * - M4
     - VCC_3V3
     - 
   * - M5
     - VCC_3V3
     - 
   * - M6
     - GND
     - 
   * - M7
     - GND
     - 
   * - M8
     - GND
     - 
   * - M9
     - VCCIO_SD
     - 
   * - M10
     - VCCIO_SD
     - 
   * - M11
     - VCCIO_SD
     - 
   * - M12
     - VCCIO_SD
     - 
   * - M13
     - MIPI_CSI_RX0_D2N
     - MIPI_CSIRXOD2N
   * - M14
     - MIC0_N
     - 
   * - M15
     - MIC0_N
     - 
   * - M16
     - MIPI_DPHY_CSI_RX0_CLK1P
     - MIPI_DPHY_CSI_RXO_CLK1P
   * - N1
     - GND
     - 
   * - N2
     - GND
     - 
   * - N3
     - GND
     - 
   * - N4
     - VCC_3V3
     - 
   * - N5
     - MIPI_DSI_D0P
     - MIPI_DSI_DOP
   * - N6
     - MIPI_DSI_D0N
     - MIPI_DSI_DON
   * - N7
     - WORK_PWM_LED
     - UART0_RX_M1/PWM2_CH7_M0 / JTAG_TMS_M2/ CAN1_TXD_M0 /GPIO5
   * - N8
     - GPIO5_D4_U
     - I2C2_SCL_M1/FEPHNLL/NKM1/UART3XPM/PMO_CH_M
   * - N9
     - MIPI_RX1_PDN
     - PWM0_CH5_M1 / SPI0_CSN1_M1/ SAI1_MCLK_M1 /UART4_TX_M0 / GPIO4
   * - N10
     - MIPI_MCLK_OUT0
     - CAM_CLKO_OUT/UART5_CTSN_M0/GPIO4_B1_D
   * - N11
     - MIPI_CSI_RX0_D1P
     - MIPI_CSIRXOD1P
   * - N12
     - MIPI_CSI_RX0_D1N
     - MIPICSIXODN
   * - N13
     - MIPI_CSI_RX0_D3P
     - MIPI_CSIRXOD3P
   * - N14
     - MIPI_CSI_RX0_D3N
     - MIPI_CSIRXOD3N
   * - N15
     - MIPI_CSI_RX0_CLK0P
     - MIPI_CSIRXO_CLKOP
   * - N16
     - MIPI_CSI_RX0_CLK0N
     - MIPI_CSIRXO_CLKON
   * - P1
     - MIPI_DSI_D1P
     - MIPI_DSI_DP
   * - P2
     - MIPI_DSI_CLKN
     - MIPI_DSI_CLKN
   * - P3
     - GND
     - 
   * - P4
     - GPIO5_B3_D
     - DSMC_RDYN/ETH_MCLKM1/LARTG_CTSNGMO5WM2_CH1_M1/V_CIF
   * - P5
     - TP_INT_L
     - DSMC_D13/SA2SOM/P1MW_CH
   * - P6
     - LCD_PWREN_H
     - DSMC_D14/SAI2MCLKM1/PI0CSODM/A4AM/PWM_CH
   * - P7
     - GPIO5_D6_U
     - UART0_TX_M1/ PWM2_CH6_M0 / JTAG_TCK_M2 / CAN1_RXD_M0/ GPIO5
   * - P8
     - GPIO5_D5_U
     - I2C2_SDA_M1/FEPHYLEDSPD_M/ART3 RXM1/PWM1_CH3_M
   * - P9
     - I2C4_SDA_CAM
     - PWM0_CH6_M1/SPI_CSNO_M1/SA14DLM/I2C4_SDA_M2/UART5_T
   * - P10
     - I2C4_SCL_CAM
     - PWM0_CH7_M1/SPI0_CLK_M1/SASDAM1/2C4_SCL_M2/UART5_R
   * - P11
     - I2C3_SCL_CAM
     - SPI0_MOSI_M1/ SAI1_SCLK_M1/I2C3_SCL_M1/ GPIO4_A4_D
   * - P12
     - MIPI_RX0_PDN
     - PWM0_CH4_M1/UART4_RX_M0/GPIO4_A2_D
   * - P13
     - I2C3_SDA_CAM
     - SPI0_MISO_M1/SAI1_LRCK_M1/ I2C3_SDA_M1/ GPIO4_A5_D
   * - P14
     - MIPI_RX0_RST
     - CAM_CLK3_OUT /I2C1_SDA_M2 /UART4_RTSN_M0 /GPIO4_A0_U
   * - P15
     - MIPI_CSI_RX0_D0N
     - MIPI_CSI_RX0_DON
   * - P16
     - MIPI_CSI_RX0_D0P
     - MIPI_CSI_RX0_DOP
   * - R1
     - MIPI_DSI_D1N
     - MIPI_DSI_DN
   * - R2
     - MIPI_DSI_CLKP
     - MIPI_DSI_CLKP
   * - R3
     - MIPI_DSI_D2P
     - MIPI_DSI_D2P
   * - R4
     - MIPI_DSI_D2N
     - MIPI_DSI_D2N
   * - R5
     - LCD_BL_PWM
     - CDBLPWM
   * - R6
     - MOTOR1_D1
     - SARADC1/GMMA
   * - R7
     - MOTOR2_D2
     - SARADC1IN5/ETHTXD2MMCIFD/2C5SDAM3/ART5_CTS
   * - R8
     - MOTOR2_D3
     - SARADC1_IN6 ETH_TXD3_MOV_CI6OUART4_RTSN_M2 PWM_CH
   * - R9
     - MOTOR2_D4
     - SARADC1N/THTMMAS
   * - R10
     - MIPI_CSI_RX1_D0N
     - MIPI_CSIRX1_DON
   * - R11
     - MIPI_CSI_RX1_D0P
     - MIPI_CSIRX1DOP
   * - R12
     - MIPI_RX1_RST
     - CAM_CLK2_OUT /I2C1_SCL_M2 /UART4_CTSN_M0 / GPIO4_A1_U
   * - R13
     - MIPI_DPHY_CSI_RX1_CLK1N
     - MIPI_DPHY_CSI_RX1_CLKIN
   * - R14
     - MIPI_DPHY_CSI_RX1_CLK1P
     - MIPI_DPHY_CSI_RX1_CLK1P
   * - R15
     - MIPI_CSI_RX1_D3N
     - MIPI_CSIRX1_D3N
   * - R16
     - MIPI_CSI_RX1_D3P
     - MIPI_CSIRX1D3P
   * - T1
     - MIPI_DSI_D3P
     - MIPI_DSI_D3P
   * - T2
     - MIPI_DSI_D3N
     - MIPI_DSI_D3N
   * - T3
     - TP_RST_L
     - DSMC_D1/A2SCKMM/M/
   * - T4
     - I2C5_SDA_TP
     - I2C5SDMMCAKM/M/TCTS
   * - T5
     - I2C5_SCL_TP
     - I2C5_SCL_M2/DSMCD/AIDMATCTAM/PWM_
   * - T6
     - MOTOR2_D1
     - SARADC1IN/T/IAL/SC
   * - T7
     - MOTOR1_D3
     - SARADC1/AMA
   * - T8
     - MOTOR1_D2
     - SAISRDCM//ETHPRECLKTCANTXMMM1
   * - T9
     - MOTOR1_D4
     - SARADC1N/ETACANMHIA
   * - T10
     - MIPI_CSI_RX1_D1P
     - MIPI_CSIRX1_D1P
   * - T11
     - MIPI_CSI_RX1_D1N
     - MIPI_CSIRX1_DIN
   * - T12
     - MIPI_MCLK_OUT1
     - MIPIMCLK_OUT1
   * - T13
     - MIPI_CSI_RX1_D2N
     - MIPI_CSIRX1_D2N
   * - T14
     - MIPI_CSI_RX1_D2P
     - MIPI_CSIRX1D2P
   * - T15
     - MIPI_CSI_RX1_CLKON
     - MIPI_CSI_RX1_CLKON
   * - T16
     - MIPI_CSI_RX1_CLKOP
     - MIPI_CSI_RX1_CLKOP

Interface Resources
-------------------

Note: Parameters in the table are hardware design or CPU theoretical values

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+------------+-------------+-------------------+--------------------------------------------------+
|             Interface    | Max Configurable  | Description                                      |
|             Spec         | Interface Count   |                                                  |
+============+=============+===================+==================================================+
|            | Ethernet    | 1                 | 1 Ethernet controller, supports RGMII/RMII,      |
|            |             |                   | speed 10/100/1000                                |
+            +-------------+-------------------+--------------------------------------------------+
|            | USB2.0      | 2                 | 1 USB2.0 Host, 1 USB2.0 OTG, max speed 480Mbps   |
+            +-------------+-------------------+--------------------------------------------------+
|            | UART        | 9                 | 6 UART interfaces, max baud rate 4Mbps           |
+            +-------------+-------------------+--------------------------------------------------+
|            | SPI         | 3                 | 2 general SPI + 1 dedicated FSPI, master/slave   |
+            +-------------+-------------------+--------------------------------------------------+
| Comm       | I2C         | 9                 | 6 I2C interfaces, 7bit/10bit address, 1Mbps max  |
+ Interface  +-------------+-------------------+--------------------------------------------------+
|            | CAN         | 1                 | 1 CAN interface, supports standard/extended/CANFD|
+            +-------------+-------------------+--------------------------------------------------+
|            | PWM         | 13                | 12 general PWM + 1 audio dedicated PWM           |
+            +-------------+-------------------+--------------------------------------------------+
|            | ADC         | 8                 | 6 10-bit SARADC + 2 TSADC for temperature        |
+            +-------------+-------------------+--------------------------------------------------+
|            | I2S         | 3                 | 3 I2S audio interfaces, max 192KHz sample rate   |
+------------+-------------+-------------------+--------------------------------------------------+
|            | SDIO        | 1                 | 1 SDIO3.0 interface, supports SD3.0, MMC4.51     |
+            +-------------+-------------------+--------------------------------------------------+
| External   | eMMC        | 1                 | 1 eMMC4.51 interface, 1/4/8bit bus, HS200 mode   |
| Storage    +-------------+-------------------+--------------------------------------------------+
|            | FSPI        | 1                 | 1 FSPI interface, x1/x2/x4 modes, 2 chip selects |
+            +-------------+-------------------+--------------------------------------------------+
|            | NAND Flash  | 1                 | 1 async NAND Flash, 8bit bus, hardware ECC       |
+------------+-------------+-------------------+--------------------------------------------------+
|            | CSI_MIPI    | 2                 | 2 MIPI CSI input interfaces, max 4 lanes each    |
+            +-------------+-------------------+--------------------------------------------------+
| Multimedia | DSI_MIPI    | 1                 | 1 4Lane DSI_MIPI interface, max 1920×1080        |
+            +-------------+-------------------+--------------------------------------------------+
|            | LVDS        | 2                 | 2 4-channel LVDS input, shared with MIPI CSI     |
+            +-------------+-------------------+--------------------------------------------------+
|            | RGB         | 1                 | 1 24bit parallel RGB display, max 1920×1080      |
+------------+-------------+-------------------+--------------------------------------------------+
| System     | buildroot, debian12                                                                |
| Version    +-------------+-------------------+--------------------------------------------------+
|            | weston                                                                             |
+------------+-------------+-------------------+--------------------------------------------------+ 

Development Board Introduction
------------------------------

Development Board Top/Bottom Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div style="display: flex; justify-content: space-around;">
   <div style="text-align: center; width: 45%;">

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/开发板.png
   :alt: Development Board Top View
   :width: 100%

**Development Board Top View**

.. raw:: html

   </div>
   <div style="text-align: center; width: 45%;">

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/开发板_02.png
   :alt: Development Board Bottom View
   :width: 100%

**Development Board Bottom View**

.. raw:: html

   </div>
   </div>

Development Board Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/开发板尺寸机械图.jpg
   :alt: Development Board Dimensions
   :width: 100%  

Development Board Interface Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../../image/MYZR-瑞芯微系列/MYZR-RV1126B-EK221/开发板接口图.jpg
   :alt: Development Board Interface Diagram
   :width: 100%  

Development Board Basic Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+-----+---------------+--------------------+
| No. |     Item      |   Specification    |
+=====+===============+====================+
| 1   | Model         | MYZR-RV1126B-EK221 |
+-----+---------------+--------------------+
| 2   | PCB Size      | 190mm × 125mm      |
+-----+---------------+--------------------+
| 3   | PCB Layers    | 4 layers           |
+-----+---------------+--------------------+
| 4   | PCB Thickness | 1.6mm              |
+-----+---------------+--------------------+
| 5   | PCB Color     | Black              |
+-----+---------------+--------------------+
| 6   | Core Board    | LGA                |
+-----+---------------+--------------------+

Development Board Standard Accessories and Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+----------------------+-------------------------------------+--------------------------+
| Model                |   Development Board Standard Accessories                       |
+======================+=====================================+==========================+
|                      | Development Board ×1 [w/Core Board] | Network Cable ×1         |
+                      +-------------------------------------+--------------------------+
|                      | 12V Power Adapter ×1                | USB Programming Cable ×1 |
+                      +-------------------------------------+--------------------------+
| MYZR-RV1126B-EK221   | TTL Serial Module ×1 [Gift]         |                          |
+                      +-------------------------------------+--------------------------+
|                      | Optional Accessories                                           |
+                      +-------------------------------------+--------------------------+
|                      | OV5695 Camera, 5-inch MIPI Display                             |
+----------------------+-------------------------------------+--------------------------+

The development board is used with MYZR-RV1126B core board, integrating all common interfaces required for development and debugging, facilitating system development and function verification.

Development Board Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+-----+--------------------------+--------------------------+--------------------------------+-------------+
| No. |        Interface         |         Function         |         Interface Type         | Silk Screen |
+=====+==========================+==========================+================================+=============+
| 1   | Power                    | 12V IN                   | 3P DC-005 Power Jack           | CON1        |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 2   | Industrial Serial Bus    | CAN/RS232/RS485          | 3P 3.5mm Pluggable Terminal    | J3、J4、J5  |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 3   | IR LED, IR CUT2, IR CUT1 | Camera Peripheral Driver | 12P 0.5mm FPC Socket           | CON7        |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 4   | TF                       | SD                       | 9P TF Card Socket (TF-01A)     | U30         |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 5   | Ethernet                 | 10/100M                  | Right-angle RJ45 with LED      | J2          |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 6   | Ethernet                 | 10/100/1000M             | Straight Gigabit RJ45 with LED | U20         |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 7   | OTG, DEBUG               | Programming, Debug Port  | Type-C Female 16PIN 2MD        | U5、U6      |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 8   | WIFI&BT                  | WiFi, Bluetooth          |                                | U18、U25    |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 9   | USB3.0                   | USB3.0                   | USB3.0 AF Horizontal Mount     | USB1        |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 10  | USB2.0                   | USB2.0                   | Dual-layer USB-A Female        | J1          |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 11  | MIC                      | Microphone               | 1.25mm 2P Vertical Header      | CON8、CON9  |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 12  | Audio                    | Speaker                  | XH2.54 2P Straight Header      | P1          |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 13  | MIPI_CSI                 | D-PHY0_RX, D-PHY0_TX     | 2mm 2×10P IDC Header           | U13、U14    |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 14  | Motor                    | Motor                    | 1.25mm 5P Vertical Header      | CON4、CON5  |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 15  | MIPI_DSI                 | MIPI DSI Display         | 0.5mm 30P FPC Socket           | CON6        |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 16  | GPIO 40Pin               | Multiplexed Pins         | 2.54mm 2×20P Header            | J6          |
+-----+--------------------------+--------------------------+--------------------------------+-------------+
| 17  | RTC                      | Power-off Timekeeping    | CR1220 Battery Holder          | U2          |
+-----+--------------------------+--------------------------+--------------------------------+-------------+

Development Board Power Consumption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <style>
   table {
       border-collapse: collapse;
       background-color: #f5f5f5;
   }
   th {
       background-color: #4CAF50;
       color: white;
   }
   td {
       border: 1px solid #ddd;
       padding: 8px;
   }
   </style>

.. raw:: html

   <style>
   table {
       width: 100%;  /* Uniform width */
       border-collapse: collapse;
       table-layout: auto;  /* Auto column width distribution */
   }
   td {
       word-wrap: break-word;  /* Auto word-wrap for long content */
   }
   </style>

+------------------------------------+-----------+---------+-----------+---------+
| Type                               |    Standby Power    |  Full Load Power    |
|                                    +-----------+---------+-----------+---------+
|                                    | Current   | Power   | Current   | Power   |
+====================================+===========+=========+===========+=========+
| MYZR-RV1126B Dev Board             | 140mA     | 1.680W  | 210mA     | 2.520W  |
+------------------------------------+-----------+---------+-----------+---------+
| Note: Values are current (mA), voltage is 5.0V, full load is all cores running |
+------------------------------------+-----------+---------+-----------+---------+

Development Board Circuit Design Description
--------------------------------------------

1. Power Circuit
~~~~~~~~~~~~~~~~

* Input: 12V/2A DC input, with reverse polarity protection, overcurrent/overvoltage protection and power indicator;

* Uses SY8113B ADC buck chip, outputs 5V (max 3A), 3.3V (max 3A), each power rail has decoupling capacitors nearby.

2. Debug UART
~~~~~~~~~~~~~

* Default debug port UART0, baud rate 1.5M, can be direct header or converted to USB via CH340;

* Signal lines have 510Ω resistor + TVS for ESD protection, IO level matches power domain.

3. Image Capture MIPI-CSI (2 channels)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Supports dual MIPI cameras, Sensor power 1.2V/1.8V/2.8V as needed, high-power Sensors use DCDC;

* PWDN, RESET controlled by GPIO, same-address I2C cameras on different buses, ESD protection added.

4. Display MIPI-DSI/RGB
~~~~~~~~~~~~~~~~~~~~~~~

* MIPI DSI: 4Lane, 1080P@60Hz, common mode chokes on differential lines;

* RGB24bit: VCCIO5 domain, 22~100Ω current-limiting resistors + TVS on interface.

5. Ethernet
~~~~~~~~~~~

* Built-in 100Mbps FE-PHY, plus Gigabit GMAC;

* FE differential pairs with 5.1Ω series, 110Ω parallel termination; MDIO with 1.5K~1.8K pull-up, RJ45 with surge protection and isolation capacitors.

6. Audio Module
~~~~~~~~~~~~~~~

* Built-in dual ADC for differential mic input, PDM interface for digital mic;

* DSM differential audio output requires RC low-pass filter, SAI for I2S external Codec.

7. RS232/RS485/CAN
~~~~~~~~~~~~~~~~~~

* 232/485 use level conversion chips, ESD protection, 3.3V level;

* Dual CANFD channels, termination resistors on differential bus, ESD protection on connectors.

8. USB Circuit
~~~~~~~~~~~~~~

* USB3.0 differential pairs with 0.1μF DC-blocking capacitors, USB2.0 with 2Ω series resistors;

* Integrated USB-HUB chip, overcurrent protection on each port.

9. WIFI&BT
~~~~~~~~~~

Equipped with BL-M8723DU module, 2.4G WiFi+BLE5.0, matching capacitors reserved at antenna.

10. Button Circuit
~~~~~~~~~~~~~~~~~~

ADC voltage-divider buttons (ESC/MENU/LEFT/RIGHT), long press during power-on enters Recovery mode.