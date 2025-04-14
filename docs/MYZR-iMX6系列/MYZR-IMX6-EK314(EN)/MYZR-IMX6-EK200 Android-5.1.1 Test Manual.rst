MYZR-IMX6-EK200 Android-5.1.1 Test Manual
============================================

Applicable scope
-------------------

+-----------------------+---------------+
| sphere of application                 |
+=======================+===============+
| evaluation board type | system type   |
+-----------------------+---------------+
| MYZR-IMX6-EK200       | Android 5.1.1 |
+-----------------------+---------------+
| MYZR-IMX6-EK314       | Android 5.1.1 |
+-----------------------+---------------+

Test project
--------------

I.）uart Test
~~~~~~~~~~~~~~~

|   Before testing, you need to short the serial port's transceiver pin. The pins of different development boards are different. The corresponding relationship is as follows:

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/960px-Android_test_1.2.jpg
   :alt: 960px-Android_test_1.2.jpg

- Test method:

|   1）Select the serial port to test, set the baud rate
|   2）Click on the device button
|   3）Enter the content to send
|   4）Click the Transfer Data button
|   5）Click the Close Device button

II.）Gpio Test
~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/960px-Android_test_1.3.jpg
   :alt: 960px-Android_test_1.3.jpg

- Test method:

|   1）Input: Enter a GPIO set to input pin 
|   2）Output: Enter a GPIO set to the output pin 
|   3）Click the high/low level button to set the level
|   4）Test the output pin level with a multimeter


Iii.）Spi Test
~~~~~~~~~~~~~~~~~

|   Before the test, the pins of the SPI need to be short-connected. The pins of the short connections of different development boards are different. The corresponding relationships are as follows:

+-----------------------+------+-------+--------+
| evaluation board type | SPIx | MISO  |  MOSI  |
+=======================+======+=======+========+
| MYZR-IMX6-EK200       | SPI1 | J7:7  | J7:9   |
+                       +------+-------+--------+
|                       | SPI2 | J7:8  | J7:10  |
+-----------------------+------+-------+--------+
| MYZR-IMX6-EK314       | SPI1 | J13:7 | J13:11 |
+                       +------+-------+--------+
|                       | SPI2 | J13:6 | J13:12 |
+-----------------------+------+-------+--------+

- Test method:

|   1）Click on the device button
|   2）Enter what you want to send
|   3）Click the data transfer button
|   4）Click the Close Device button

Iv. ）I2C Test
~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/960px-Android_test_1.5.jpg
   :alt: 960px-Android_test_1.5.jpg

- Test method:

|   1）Select I2C bus to test
|   2）Click to read I2C button to read the device on the bus

V.） Can Test
~~~~~~~~~~~~~~~~

|   Before testing, it is necessary to connect CAN pins, connect CAN _ L of CAN 1 with CAN _ L of CAN 2, and connect CAN _ H of CAN 1 with CAN _ H of CAN 2.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/960px-Android_test_1.6.jpg
   :alt: 960px-Android_test_1.6.jpg

- Test method:

|   1）Click on Open Device
|   2）Enter the content to send, not more than 8
|   3）Click to transmit data
|   4）Click to close device


VI.） Usb test
~~~~~~~~~~~~~~~~~

|   Check the USB and SD cards.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/960px-Android_test_1.7.jpg
   :alt: 960px-Android_test_1.7.jpg

VII.） media Test
~~~~~~~~~~~~~~~~~~~~

|   Bring your own video before testing.

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/960px-Android_test_1.8.jpg
   :alt: 960px-Android_test_1.8.jpg

- Test methods:

|   1）Select a video
|   2）Play Video

VIII.） Wifi Test
~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-iMX6系列/MYZR-IMX6-EK314/960px-Android_test_1.9.jpg
   :alt: 960px-Android_test_1.9.jpg

- Test methods:

|   1）Click the WiFi switch to turn on WiFi and wait for WiFi search results
|   2）Click the WiFi you want to connect to
|   3）Enter password, click the connection button