MYZR-SSD20X-MB096 硬件介绍
============================

接口概览
---------

正面图
~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/963px-MYZR-SSD20X-MB096-Front.jpg
   :alt: 963px-MYZR-SSD20X-MB096-Front.jpg

背面图
~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/963px-MYZR-SSD20X-MB096-Back.jpg
   :alt: 963px-MYZR-SSD20X-MB096-Back.jpg

MYZR-SSD20X-MB096底板参数
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------+------------+------------------+--------------------+---------+
| 标号 | 接口       | 功能             | 接口形式           | 丝印    |
+======+============+==================+====================+=========+
| 1    | 5V_IN      | 电源输入         | DC-005圆口         | P1      |
+------+------------+------------------+--------------------+---------+
| 2    | Ethernet   | 1个10/100M以太网 | RJ45               | P2和P11 |
+------+------------+------------------+--------------------+---------+
| 3    | DEBUG UART | 调试串口         | PH1.25排母(4针)    | P5      |
+------+------------+------------------+--------------------+---------+
| 4    | RS232      | RS232接口        | 螺钉式接线端子     | P6      |
+------+------------+------------------+--------------------+---------+
| 5    | RS485      | RS485接口        | 螺钉式接线端子     | P7      |
+------+------------+------------------+--------------------+---------+
| 6    | 4G模块     | 4G模块接口       | MINI-PCIE          | J2      |
+------+------------+------------------+--------------------+---------+
| 7    | sim        | sim卡            | MICRO SIM 自弹式   | J1      |
+------+------------+------------------+--------------------+---------+
| 8    | TF         | TF卡             | 标准TF卡自弹式卡座 | P3      |
+------+------------+------------------+--------------------+---------+
| 9    | USB        | USB2.0           | 双层USB_A          | P12     |
+------+------------+------------------+--------------------+---------+
| 10   | MIPI-DSI   | MIPI屏接口       | FPC插座（40Pin）   | P10     |
+------+------------+------------------+--------------------+---------+
| 11   | USER LIGHT | 用户LED灯        | 贴片LED灯（2个）   | D7和D8  |
+------+------------+------------------+--------------------+---------+
| 12   | 天线       | WIFI&蓝牙        | IPX接头            | E1      |
+------+------------+------------------+--------------------+---------+
| 13   | 串口       | BOOT LOADER      | PH2.54插针         | P4      |
+------+------------+------------------+--------------------+---------+
| 14   | 复位按键   | 复位             | 轻触按键开关       | SW1     |
+------+------------+------------------+--------------------+---------+


MYZR-SSD20X-MB096底板说明
---------------------------

1. 底板电源
~~~~~~~~~~~~~

|  底板使用DC 5.5插头（P1）插座插入5V电源供电，经过C1电容稳压滤波后到自恢复保险丝(F1)、（D2）5.6V稳压二极管及Q2三极管通过电源输入反馈检测控制5VDC-DC（Q1）pin4 EN管脚高低电平输入，控制电源开启关闭以此来预防电源输入过压保护。后级输出5VIN电压经电容及磁珠滤波后依次分3.3V、1.8V降压给控制底板部分电路供电。

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-5V.png
   :alt: MYZR-SSD20X-MB096-5V.png

|  5V输入部分电路

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-3.3V.png
   :alt: MYZR-SSD20X-MB096-3.3V.png

|  3.3V部分电路

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-1.8V.png
   :alt: MYZR-SSD20X-MB096-1.8V.png

|  1.8V部分电路

|  注意事项：电源部分设计时5V/3.3V请按照最低3A电流覆铜及电源走线，1.8V请按照最低1.5A电流覆铜及电源走线，如需正反面走线需多打过孔，防止电源通电瞬间过载导致PCB烧板，保证供电正常。

2. 复位电路
~~~~~~~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-RESET.png
   :alt: MYZR-SSD20X-MB096-RESET.png

|  注意：本开发板预留了硬件输入复位，按下SW1复位开关上拉3.3V系统复位。

3. LED显示电路
~~~~~~~~~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-LED01.png
   :alt: MYZR-SSD20X-MB096-LED01.png

|  电源指示灯

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-LED02.png
   :alt: MYZR-SSD20X-MB096-LED02.png

|  系统指示灯

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-LED03.png
   :alt: MYZR-SSD20X-MB096-LED03.png

|  4G模块指示灯
|  本系统共4路LED 灯指示。

4. RTC实时时钟电路
~~~~~~~~~~~~~~~~~~~

|  本电路所用RTC芯片内置晶振匹配电容，如需更换方案则需注意晶振精度问题，可在晶振两网络上并联匹配电容到地以达到调整精度的需要。 在底板上电时，底板的3.3V电源将给RTC芯片供电并给电池BT1充电；在底板掉电时，电池BT1将放电充当RTC芯片工作的电源。

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-RTC.png
   :alt: MYZR-SSD20X-MB096-RTC.png

5. 外接TF卡电路
~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/480px-MYZR-SSD20X-MB096-TF.png
   :alt: 480px-MYZR-SSD20X-MB096-TF.png

6. 以太网电路接口
~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-ETH1.png
   :alt: MYZR-SSD20X-MB096-ETH1.png

|  ETH1电路

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-ETH2.png
   :alt: MYZR-SSD20X-MB096-ETH2.png

|  ETH2电路

|  注意：5VIN电源需严格预留最少1.5A通过电流设计加粗，DP/DM 信号线需走差分信号线。BR1/2是防静电保护器件，L4/5/6为共模滤波器，设计PCB时需要靠近USB接口， P12 为USB2.0插座可外接U盘或鼠标等。

7. USB电路

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/720px-MYZR-SSD20X-MB096-HUB-IC.png
   :alt: 720px-MYZR-SSD20X-MB096-HUB-IC.png

|  HUB IC 电路

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-USB.png
   :alt: MYZR-SSD20X-MB096-USB.png

|  外置2路USB输入插座电路

|  注意：5VIN电源需严格预留最少1.5A通过电流设计加粗，DP/DM 信号线需走差分信号线。BR1/2是防静电保护器件，L4/5/6为共模滤波器，设计PCB时需要靠近USB接口， P12 为USB2.0插座可外接U盘或鼠标等。

8. 4G模块电路
~~~~~~~~~~~~~~

MY-A40I-MB204_4G.png

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MY-A40I-MB204_4G.png
   :alt: MY-A40I-MB204_4G.png

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-4G2.png
   :alt: MYZR-SSD20X-MB096-4G2.png

|  注意：4G模块瞬时工作电流可达3A 左右，电路设计时3.3v电源线需严格按照电流设计，滤波电容需尽量靠近放置；D4为模块的工作状态指示灯，P27为SIM卡卡座要求靠近4G模块放置，模块到SIM卡网络要求成组走线避免走线太远长度误差太大并远离强信号干扰源和走线需就近布置。L12为共模滤波器，USB线要求差分走线。

9. MIPI电路
~~~~~~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-MIPI.png
   :alt: MYZR-SSD20X-MB096-MIPI.png

|  注意：5V/3.3V/1.8V 电源需按照1A以上电流设计，除电源线外其余信号线需严格按照等距差分信号线布线，信号线需按组分并行走线，走线尽量要短，滤波电容靠近接口放置。


10. WIFI模块电路
~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/720px-MYZR-SSD20X-MB096-WIFI.png
   :alt: 720px-MYZR-SSD20X-MB096-WIFI.png

|  注意： 3.3V 电源需按照1A以上电流设计，USB信号线电路需严格按等长走线，布线尽量走不打过孔。模块ANT 端到E1 天线端子输出信号端输出线尽量加宽， E1所在网络要求走线满足50Ω阻抗设计，走线尽量短且不可走折角C87/L8/C88等器件需尽量靠近并π型输出，天线输出两端尽量覆铜GND包裹。

11. SPI/I2C/AUD/GPIO/IRN电路
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-AUD.png
   :alt: MYZR-SSD20X-MB096-AUD.png

|  排针_AUD_GPIO_IRIN接口

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-SPI.png
   :alt: MYZR-SSD20X-MB096-SPI.png

|  排针SPI、I2C、ADC接口

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-ADC.png
   :alt: MYZR-SSD20X-MB096-ADC.png

|  ADC 接口电路

|  注意：I2C、SPI等信号线路需严格按照差分线路布线并且尽量短及走线周围包地处理，远离信号线等干扰。

12. RS232/485 电路
~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/480px-MYZR-SSD20X-MB096-RS232.png
   :alt: 480px-MYZR-SSD20X-MB096-RS232.png

|  RS232电路

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-RS485.png
   :alt: MYZR-SSD20X-MB096-RS485.png

|  RS485电路

|  注意： 3.3V 电源需按照1A以上电流设计，TX/RX信号线电路需严格按等距差分信号线布线。P5为内部调试端口为方便后期调试请用户在自行设计底板时将此调试串口引出。485信号端匹配电阻R58视负载数量及传输长度增加120欧姆电阻。器件布局时U6、U7两芯片靠近P6、P7接口摆放。

13. 调试串口及烧录接口
~~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-国产系列/SigmaStar平台/MYZR-SSD20X/MYZR-SSD20X-MB096-Serial.png
   :alt: MYZR-SSD20X-MB096-Serial.png

|  注意：设计PCB时，每路TX/RX两信号线应成组走线，避免走线太远时导致组内两网络走线长度误差太大。

**PCB 设计要求：**

|  1、整体布局走线时，应以电源及功能模块分开布局，以模块为单位，无屏蔽模块需尽量紧靠，信号走线尽量走差分走短。
|  2、有屏蔽要求模块需屏蔽处理，周围用GND 包裹，并且GND尽量加大多打过孔。
|  3、供电部分走线尽量加粗并且尽量小走分叉及打过孔，打过孔需多加过孔。电容电感需尽量靠近电源及IC 放置。