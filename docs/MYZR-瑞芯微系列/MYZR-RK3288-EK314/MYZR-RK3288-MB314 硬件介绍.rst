底板硬件手册
=============

接口概览
--------

**正面图**

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/1500px-Myrk3288_mb314_1.1.0.1.jpg
   :alt: 1500px-Myrk3288_mb314_1.1.0.1.jpg

**背面图**

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/1500px-Myrk3288_mb314_1.2.0.1.jpg
   :alt: 1500px-Myrk3288_mb314_1.2.0.1.jpg


接口功能
--------

串口
~~~~~~

+------+----------+------------------+
| 丝印 |   功能   |     接口属性     |
+======+==========+==================+
| P4   | 调试串口 | 3线标准RS232接口 |
+------+----------+------------------+
| P3   | 功能串口 | 3线标准RS232接口 |
+------+----------+------------------+


.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.1.0.1.png
   :alt: 963px-Myrk3288_mb314_2.1.0.1.png

**U20**

======  ============  ======  ============
 引脚   功能信号名称   引脚   功能信号名称
======  ============  ======  ============
U20-1   C1+           U20-2   C1+
U20-3   C1-           U20-4   V-
U20-5   C2-           U20-6   V-
U20-7   T2OUT         U20-8   R2IN
U20-9   R2OUT         U20-10  T2IN
U20-11  T1IN          U20-12  R1OUT
U20-13  R1IN          U20-14  T1OUT
U20-15  GND           U20-16  VCC
======  ============  ======  ============

GPS
~~~~~~

| 丝印: U24
| 模块型号：NEO-6M
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.2.0.1.png
   :alt: 963px-Myrk3288_mb314_2.2.0.1.png

======  ============  =========  ============
 引脚   功能信号名称    引脚     功能信号名称
======  ============  =========  ============
U24-1   Reserved1     U24-2      NC
U24-3   TIMEPULSE     U24-4      EXTINT0
U24-5   USB_DM        U24-6      USB_DP
U24-7   VDDUSB        U24-8      Reserved2
U24-9   VCC_RF        U24-10     GND1
U24-11  RF_IN         U24-12     GND2
U24-13  GND3          U24-14~19  NC
U24-20  TXD1          U24-21     RXD1
U24-22  V_BCKP        U24-23     VCC
U24-24  GND
======  ============  =========  ============

TF卡座
~~~~~~~~

| 丝印: U22
| 接口属性：标准TF卡座
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.3.0.1.png
   :alt: 963px-Myrk3288_mb314_2.3.0.1.png

======  ============  ======  ============
 引脚   功能信号名称   引脚   功能信号名称
======  ============  ======  ============
U22-1   SDMMC_D2      U22-2   SDMMC_D3
U22-3   SDMMC_CMD     U22-4   VDD
U22-5   SDMMC_CLK     U22-6   VSS
U22-7   SDMMC_D0      U22-8   SDMMC_D1
U22-9   SDMMC_DET     U22-10  GND_01
U22-11  GND_02        U22-12  GND_03
U22-13  GND_04
======  ============  ======  ============

HDMI
~~~~~~

| 丝印：J14
| 接口属性：HDMI-1.4标准接口
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.4.0.1.png
   :alt: 963px-Myrk3288_mb314_2.4.0.1.png

======  ============  ======  ============
 引脚   功能信号名称   引脚   功能信号名称
======  ============  ======  ============
J14-1   HDMI_TX2P     J14-11  CK_SHIELD
J14-2   D2_SHIELD     J14-12  HDMI_TXCN
J14-3   HDMI_TX2N     J14-13  HDMI_CEC
J14-4   HDMI_TX1P     J14-14  HEC
J14-5   D1_SHIELD     J14-15  12C_CLK
J14-6   HDMI_TX1N     J14-16  12C_DADT
J14-7   HDMI_TX0P     J14-17  GND
J14-8   D0_SHIELD     J14-18  +5V
J14-9   HDMI_TX0N     J14-19  HOT_PLUG_DET
J14-10  HDMI_TXCP     G1-G4   HDMI_CHASSIS
======  ============  ======  ============

CIF
~~~~~~

| 丝印：J17
| 接口属性：CIF摄像头接口
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.5.0.1.png
   :alt: 963px-Myrk3288_mb314_2.5.0.1.png

======  ============  ======  ============
 引脚   功能信号名称   引脚   功能信号名称
======  ============  ======  ============
J17-1   NC            J17-13  CIF_CLKOUT
J17-2   GND           J17-14  CIF_D6
J17-3   CIF_SDA       J17-15  GND
J17-4   VCC28_DVP     J17-16  CIF_D5
J17-5   CIF_SCL       J17-17  CIF_CLKIN
J17-6   CIF_RST       J17-18  CIF_D4
J17-7   CIF_VSYNC     J17-19  CIF_D0
J17-8   CIF_PDN0      J17-20  CIF_D3
J17-9   CIF_HRER      J17-21  CIF_D1
J17-10  C_DVDD        J17-22  CIF_D2
J17-11  VCC18_DVP     J17-23  NC
J17-12  CIF_D7        J17-24  NC
======  ============  ======  ============

MIPI-CSI
~~~~~~~~~~

| 丝印：J19
| 接口属性：MIPI-CSI摄像头接口
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.6.0.1.png
   :alt: 963px-Myrk3288_mb314_2.6.0.1.png

======  ============  ======  ============
 引脚   功能信号名称   引脚   功能信号名称
======  ============  ======  ============
J19-1   NC            J19-16  MIPI_RX_D3P
J19-2   VCC_2V8       J19-17  GND
J19-4   VCC18_DVP     J19-19  MIPI_RX_D2P
J19-5   NC            J19-20  MIPI_RX_D2N
J19-6   GND           J19-21  GND
J19-7   VCC28_DVP     J19-22  MIPI_RX_D1P
J19-8   GND           J19-23  MIPI_RX_D1N
J19-9   CSI2-SDA      J19-24  GND
J19-10  CSI2-SCL      J19-25  MIPI_CLKP
J19-11  MIPI_RST_1V8  J19-26  MIPI_CLKN
J19-12  PWDN1         J19-27  GND
J19-13  GND           J19-28  MIPI_RX_D0P
J19-14  MIPI_CLKIN    J19-29  MIPI_RX_D0N
J19-15  GND           J19-30  GND
======  ============  ======  ============

SINGEL LVDS
~~~~~~~~~~~~~~

| 丝印：J8
| 接口属性：单路LVDS接口，用于连接MYZR-LCD_LVDS液晶板
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/Myrk3288_mb314_2.7.0.1.png
   :alt: Myrk3288_mb314_2.7.0.1.png

=====  ============  ========  ============
引脚   功能信号名称    引脚    功能信号名称
=====  ============  ========  ============
J8-1   LVDS_D1N      J8-14     LVDS_CLK0P
J8-2   LVDS_D1P      J8-15     GND
J8-3   GND           J8-16     GPIO_B5
J8-4   LVDS_D0P      J8-17     GPIO_B6
J8-5   LVDS_D0N      J8-18     GND
J8-6   GND           J8-19     LCDC_BL
J8-7   LVDS_D3N      J8-20     GND
J8-8   LVDS_D3P      J8-21     TOUCH_SCL
J8-9   GND           J8-22     TOUCH_SDA
J8-10  LVDS_D2P      J8-23~25  GND
J8-11  LVDS_D2N      J8-26~30  5V_IN
J8-12  GND           8-31~40   NC
J8-13  LVDS_CLK0N
=====  ============  ========  ============

EDP
~~~~~

| 丝印：J7
| 接口属性：EDP屏接口，用于连接15.6寸EDP显示屏
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/Myrk3288_mb314_2.8.0.1.png
   :alt: Myrk3288_mb314_2.8.0.1.png

=====  ============  =====  ============
引脚   功能信号名称  引脚   功能信号名称
=====  ============  =====  ============
J7-1   NC            J7-16  GND
J7-2   GND           J7-17  EDP_HPD
J7-3   EDP_TX1N      J7-18  GND
J7-4   EDP_TX1P      J7-19  GND
J7-5   GND           J7-20  GND
J7-6   EDP_TX0N      J7-21  GND
J7-7   EDP_TX0P      J7-22  BL_EN
J7-8   GND           J7-23  EDP_BL
J7-9   EDPAUXP       J7-24  NC
J7-10  EDPAUXN       J7-25  NC
J7-11  GND           J7-26  BL_12V
J7-12  GEN_3V3       J7-27  BL_12V
J7-13  GEN_3V3       J7-28  BL_12V
J7-14  NC            J7-29  BL_12V
J7-15  GND           J7-30  GND
=====  ============  =====  ============


BL
~~~~

| 丝印：J5
| 接口属性：背光12V输出，用于给设备外接屏供给12V背光电压
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/Myrk3288_mb314_2.9.0.1.png
   :alt: Myrk3288_mb314_2.9.0.1.png

====  ============  ====  ============
引脚  功能信号名称  引脚  功能信号名称
====  ============  ====  ============
J5-1  GND           J5-4  BL_EN
J5-2  GND           J5-5  BL_12V
J5-3  EDP_BL        J5-6  BL_12V
====  ============  ====  ============

DUAL LVDS
~~~~~~~~~~~

| 丝印：J9
| 接口属性：双路LVDS接口
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.10.0.1.png
   :alt: 963px-Myrk3288_mb314_2.10.0.1.png

+-------+--------------+-------+--------------+
| 引脚  | 功能信号名称 | 引脚  | 功能信号名称 |
+=======+==============+=======+==============+
| J9-1  | 5V IN        | J9-2  | 5V IN        |
+-------+--------------+-------+--------------+
| J9-3  | 5V IN        | J9-4  | GND          |
+-------+--------------+-------+--------------+
| J9-5  | GND          | J9-6  | GND          |
+-------+--------------+-------+--------------+
| J9-7  | LVDS_D0N     | J9-8  | LVDS_D0P     |
+-------+--------------+-------+--------------+
| J9-9  | LVDS_D1N     | J9-10 | LVDS_D1P     |
+-------+--------------+-------+--------------+
| J9-11 | LVDS_D2N     | J9-12 | LVDS_D2P     |
+-------+--------------+-------+--------------+
| J9-13 | GND          | J9-14 | GND          |
+-------+--------------+-------+--------------+
| J9-15 | LVDS_CLK0N   | J9-16 | LVDS_CLK0P   |
+-------+--------------+-------+--------------+
| J9-17 | LVDS_D3N     | J9-18 | LVDS_D3P     |
+-------+--------------+-------+--------------+
| J9-19 | LVDS_D5N     | J9-20 | LVDS_D5P     |
+-------+--------------+-------+--------------+
| J9-21 | LVDS_D6N     | J9-22 | LVDS_D6P     |
+-------+--------------+-------+--------------+
| J9-23 | LVDS_D7N     | J9-24 | LVDS_D7P     |
+-------+--------------+-------+--------------+
| J9-25 | GND          | J9-26 | GND          |
+-------+--------------+-------+--------------+
| J9-27 | LVDS_CLK1N   | J9-28 | LVDS_CLK1P   |
+-------+--------------+-------+--------------+
| J9-29 | LVDS_D8N     | J9-30 | LVDS_D8P     |
+-------+--------------+-------+--------------+


HP JACK
~~~~~~~~~

| 丝印：P15
| 接口属性：音频接口，用于耳机音频输出以及MIC输入
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.11.0.1.png
   :alt: 963px-Myrk3288_mb314_2.11.0.1.png

U32

=====  ============  ======  ===============
引脚   功能信号名称   引脚    功能信号名称
=====  ============  ======  ===============
U32-1  12S0_CLK      U32-6   12S0_SDO0
U32-2  AUD_3V3       U32-7   12S0_LRCK_RX/TX
U32-3  AUD_3V3       U32-8   12S0_SDI
U32-4  AAGND         U32-27  CODEC_12C_DAT
U32-5  12S0_SCLK     U32-28  CODEC_12C_CLK
=====  ============  ======  ===============


OTG
~~~~~

| 丝印： J1
| 接口属性：USB OTG接口
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.12.0.1.png
   :alt: 963px-Myrk3288_mb314_2.12.0.1.png

====  ============  ====  ============
引脚  功能信号名称  引脚  功能信号名称
====  ============  ====  ============
J1-1  OTG_DET       J1-6  GND
J1-2  OTG_DM        J1-7  GND
J1-3  OTG_DP        J1-8  GND
J1-4  OTG_ID        J1-9  GND
J1-5  GND
====  ============  ====  ============


USB HOST
~~~~~~~~~~

| 丝印：J10
| 接口属性：双层USB接口，通过LAN9514扩展出来的host接口
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.13.0.1.png
   :alt: 963px-Myrk3288_mb314_2.13.0.1.png


=====  ============  ======  ============
引脚   功能信号名称   引脚   功能信号名称
=====  ============  ======  ============
J10-1  PWR1          J10-7   USBSN_DP2_B
J10-2  USBSN_DM1_B   J10-8   GND
J10-3  USBSN_DP1_B   J10-9   GND
J10-4  GND           J10-10  GND
J10-5  PWR2          J10-11  GND
J10-6  USBSN_DM2_B   J10-12  GND
=====  ============  ======  ============


10M/100M Ethernet
~~~~~~~~~~~~~~~~~~~

| 丝印：P1
| 接口属性：标准百兆网接口，通过LAB9514扩展出来的以太网接口，10M/100M自适应
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.14.0.1.png
   :alt: 963px-Myrk3288_mb314_2.14.0.1.png

====  ============  =====  ===============
引脚  功能信号名称  引脚    功能信号名称
====  ============  =====  ===============
P1-1  TXP0          P1-7   NC
P1-2  TXN0          P1-8   GND
P1-3  RXP0          P1-9   GEN_3V3
P1-4  GND           P1-10  nSPD_LED_GPIO2
P1-5  GEN_3V3       P1-11  nLNKA_LED_GPIO2
P1-6  RXN0          P1-12  GEN_3V3
====  ============  =====  ===============


USB to WIFI
~~~~~~~~~~~~~~

| 丝印：U26
| 模块型号：UM12BS
| 模块描述：USB转WIFI
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.15.0.1.png
   :alt: 963px-Myrk3288_mb314_2.15.0.1.png

=====  ============  =====  ============
引脚   功能信号名称  引脚   功能信号名称
=====  ============  =====  ============
U26-1  GND           U26-4  USBDN_DM3_B
U26-2  ANTENNA_1     U26-5  USBDN_DP3_B
U26-3  GEN_3V3       U26-6  GND
=====  ============  =====  ============

1000M Ethernet
~~~~~~~~~~~~~~~~~

| 丝印：U13
| 接口属性：千兆以太网接口，10M/100M/1000M自适应
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.16.0.1.png
   :alt: 963px-Myrk3288_mb314_2.16.0.1.png

=====  ============  ======  ============
引脚   功能信号名称   引脚   功能信号名称
=====  ============  ======  ============
U13-1  TEST_POINT    U13-8   NRGMI_D_P
U13-2  RGMI_A_P      U13-9   RGMI_D_N
U13-3  RGMI_A_N      U13-10  GND
U13-4  RGMI_B_P      U13-11  RGMI_3V3_A
U13-5  RGMI_C_P      U13-12  RGMI_LED2
U13-6  RGMI_C_N      U13-13  RGMI_LED1
U13-7  RGMI_B_N      U13-14  RGMI_3V3_A
=====  ============  ======  ============

3G/4G
~~~~~~~~

| 丝印：J13
| 接口属性：标准mini-PCIE接口
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.17.0.1.png
   :alt: 963px-Myrk3288_mb314_2.17.0.1.png

=======  ============  ======  =============
 引脚    功能信号名称   引脚   功能信号名称
=======  ============  ======  =============
J13-1    NC            J13-2   GEN_3V3
J13-3    NC            J13-4   GND
J13-5    NC            J13-6   NC
J13-7    NC            J13-8   PCLE_UIM_PWR
J13-9    GND           J13-10  PCLE_UIM_DATA
J13-11   NC            J13-12  PCLE_UIM_CLK
J13-13   NC            J13-14  PCLE_UIM_RST
JJ13-15  GND           J13-16  PCLE_UIM_VPP
J13-17   NC            J13-18  GND
J13-19   NC            J13-20  NC
J13-21   GND           J13-22  NC
J13-23   NC            J13-24  NC
J13-25   NC            J13-26  GND
J13-27   GND           J13-28  NC
J13-29   GND           J13-30  NC
J13-31   NC            J13-32  NC
J13-33   NC            J13-34  GND
J13-35   GND           J13-36  USB_D-
J13-37   GND           J13-38  USB_D+
J13-39   GEN_3V3       J13-40  GND
J13-41   GEN_3V3       J13-42  LED_WWAN_B
J13-43   GND           J13-44  NC
J13-45   NC            J13-46  NC
J13-47   NC            J13-48  NC
J13-49   NC            J13-50  GND
J13-51   NC            J13-52  GEN_3V3
=======  ============  ======  =============

电压跳线选择
~~~~~~~~~~~~

| 丝印：J15
| 接口属性：5V/3.3V跳线

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.18.0.1.png
   :alt: 963px-Myrk3288_mb314_2.18.0.1.png

USB to UART
~~~~~~~~~~~~

| 丝印：J16
| 接口属性：USB扩展UART接口
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.19.0.1.png
   :alt: 963px-Myrk3288_mb314_2.19.0.1.png

======  ============  ======  ============
 引脚   功能信号名称   引脚   功能信号名称
======  ============  ======  ============
J16-1   GEN_3V3       J16-2   GEN_3V3
J16-3   USB_TXD       J16-4   USB_RXD
J16-5   USB_nRTS      J16-6   USB_nCTS
J16-7   USB_nDTR      J16-8   USB_nDSR
J16-11  NC            J16-12  NC
J16-13  USB_CBUS0     J16-14  USB_CBUS1
J16-15  USB_CBUS2     J16-16  USB_CBUS3
J16-17  USB_CBUS4     J16-18  NC
J16-19  GND           J16-20  GND
======  ============  ======  ============

WIFI
~~~~~~

| 丝印: E1
| 接口属性：标准WIFI天线座

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.20.0.1.png
   :alt: 963px-Myrk3288_mb314_2.20.0.1.png

DC IN
~~~~~~~

| 丝印: J3
| 接口属性：外部5V主电源输入，2.5A

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/Myrk3288_mb314_2.21.0.1.png
   :alt: Myrk3288_mb314_2.21.0.1.png

电源开关
~~~~~~~~~

| 丝印: J2
| 接口属性：主电源开关
| 状态属性：—，闭合，O，断开

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/Myrk3288_mb314_2.22.0.1.png
   :alt: Myrk3288_mb314_2.22.0.1.png

12V IN
~~~~~~~~

| 丝印：J4
| 接口属性：外部12V输入
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.23.0.1.png
   :alt: 963px-Myrk3288_mb314_2.23.0.1.png

====  ============  ====  ============
引脚  功能信号名称  引脚  功能信号名称
====  ============  ====  ============
J4-1  BL_12V        J4-3  GND
J4-2  BL_12V        J4-4  GND
====  ============  ====  ============

RESET
~~~~~~~

| 丝印: SW4
| 按键属性：复位按键

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.24.0.1.png
   :alt: 963px-Myrk3288_mb314_2.24.0.1.png

SLEEP WAKE
~~~~~~~~~~~~

| 丝印: SW3
| 按键属性：系统开关机按键，长按1秒开机，长按3秒关机

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.25.0.1.png
   :alt: 963px-Myrk3288_mb314_2.25.0.1.png

VOL +
~~~~~~~

| 丝印: SW2
| 按键属性：控制音量（音量加）

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.26.0.1.png
   :alt: 963px-Myrk3288_mb314_2.26.0.1.png

VOL –
~~~~~~~~

丝印: SW1
按键属性：控制音量（音量减）

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.27.0.1.png
   :alt: 963px-Myrk3288_mb314_2.27.0.1.png

RECOVER
~~~~~~~~

| 丝印: SW5
| 按键属性：烧写按键，与开机键(SW3)同时按下，进入烧写模式

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.28.0.1.png
   :alt: 963px-Myrk3288_mb314_2.28.0.1.png


扩展接口
~~~~~~~~~

| 丝印：J11
| 接口属性：空闲管脚，用于扩展应用
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.29.0.1.png
   :alt: 963px-Myrk3288_mb314_2.29.0.1.png

======  =============  ======  ============
 引脚   功能信号名称    引脚   功能信号名称
======  =============  ======  ============
J11-1   5V_IN          J11-2   GEN_3V3
J11-3   5V_IN          J11-4   GEN_3V3
J11-5   NC             J11-6   HSIC_DATA
J11-7   LIGHT_INT      J11-8   HSIC_STROBE
J11-9   GSEN_INT       J11-10  CABC_EN
J11-11  TOUCH_INT      J11-12  FLASH_EN
J11-13  LCD_RST        J11-14  SPK_CTL
J11-15  LCD_EN         J11-16  PMUGPIO0_B5
J11-17  TOUCH_RST      J11-18  OTG_VBUS_DRV
J11-19  FLASH_TRIGOUT  J11-20  PMUGPIO0_B5
J11-21  GPIO7_B1       J11-22  EFUSE_PWR
J11-23  NC             J11-24  GND
J11-25  5V_DRV         J11-26  ADC_1N1
J11-27  GPIO5_C2       J11-28  GND
J11-29  UART1_RST      J11-30  ADC_1N0
J11-31  SPI0_CSn1      J11-32  GND
J11-33  SPI0_RXD       J11-34  SPI2_MOS1
J11-35  SPI0_TXD       J11-36  SPI2_nCS0
J11-37  SPI0_CSn0      J11-38  SPI2_MISO
J11-39  GND            J11-40  GND
J11-41  SPI0_CLK       J11-42  SPI2_CLK
J11-43  GND            J11-44  GND
J11-45  UART1_CTS      J11-46  FLASH0_RDY
J11-47  GND            J11-48  FLASH0_CLE
J11-49  SPDIF_TX       J11-50  FLASH0_ALE
J11-51  GND            J11-52  FLASH0_CS0
J11-53  GND            J11-54  GND
J11-55  GND            J11-56  GND
======  =============  ======  ============


JTAG
~~~~~~

| 丝印：U19
| 接口属性：JTAG接口
| 引脚及信号定义：

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.30.0.1.png
   :alt: 963px-Myrk3288_mb314_2.30.0.1.png

=====  ========  ============  ======  ====  ========
引脚     信号        描述       引脚   信号    描述
=====  ========  ============  ======  ====  ========
U19-1  JTAG_TCK  测试时钟输入  U19-2   GND   数字地
U19-3  JTAG_TDO  测试数据输出  U19-4   VCC   3.3V输入
U19-5  JTAG_TMS  测试模式选择  U19-6   nRST  复位
U19-7  NC        未连接        U19-8   NC    未连接
U19-9  JTAG_TDI  测试数据输入  U19-10  GND   数字地
=====  ========  ============  ======  ====  ========


RTC电池座
~~~~~~~~~~~

| 丝印:BT1
| 接口属性：RTC纽扣电池接口

.. image:: /image/MYZR-瑞芯微系列/MYZR-RK3288-EK314/963px-Myrk3288_mb314_2.31.0.1.png
   :alt: 963px-Myrk3288_mb314_2.31.0.1.png


MXM314
~~~~~~~~

|  丝印:U14
|  接口属性：核心板接口，用于连接MYZR-RK3288_CB314核心板
|  管脚功能定义详见 :doc:`./MYZR-RK3288-CB314 硬件介绍`
