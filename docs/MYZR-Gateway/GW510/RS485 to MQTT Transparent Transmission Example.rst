RS485 to MQTT Transparent Transmission Example
================================================

1. Objective
---------------

| Convert data from the RS485 electricity meter (dds1079) into MQTT messages via the gateway, and upload them to the MQTT server. Users can then view the meter data on an MQTT client running on a computer.
| Devices involved

  - Gateway development board (built-in RS485 and Ethernet interface, running gateway firmware)
  - RS485 electricity meter dds1079 (or equivalent device)
  - Client computer (for web configuration + MQTT client)
  - MQTT server (public broker.emqx.io or user self-built server)


2. Device Connection
----------------------

| RS485 Connection

1. Prepare an RS485 communication cable (2-core A/B or differential cable).
2. Connect the RS485 terminal to the RS485 interface of the gateway accordingly:

  - Meter A ↔ Gateway A2
  - Meter B ↔ Gateway B2
  - Meter GND ↔ Gateway GND

3. Confirm that both the meter and gateway are powered on normally:

  - Meter display/indicator is normal;
  - Gateway power indicator and RUN indicator are normal.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例1.png
   :alt: RS485与MQTT透传示例1.png


3. Ethernet Connection
------------------------

| ETH1 -- WAN: DHCP
| BR0 -- LAN: 192.168.9.1
| BR0 (ETH2, WLAN0, WLAN1)

1. First connect the host computer and the development board via an Ethernet cable. Use the static IP 192.168.137.81 to access the web homepage, find and record the MAC address.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例2.png
   :alt: RS485与MQTT透传示例2.png

 
| The MAC address here is C6:72:27:3C:73:E1

2. Open the cmd terminal on the host and run the command:
   arp -a | find /i "c6-72-27-3c-73-e1"
   to locate the device.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例3.png
   :alt: RS485与MQTT透传示例3.png


3. Access the web configuration page in the browser using the obtained address.

3. Web Configuration
----------------------

| Enter the configuration editor on the left. You can modify the configuration file on this interface.
| Device represents the physical device, UART represents the serial port, and MQTT represents the server.
| The three are linked via object/interface.

Device List Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

Parameter Description
"""""""""""""""""""""""

- **interface (Interface Name)**

  - Meaning: Unique identifier for this collection task.
  - Description: Recommended to set as the device model or installation location (e.g., dds1079) for easy identification in logs and data platforms.

- **status (Enable Status)**
  
  - Meaning: Switch for this task.
  - Description: Set to enabled to start collection immediately; set to disabled to pause the task temporarily.

- **command (Collection Command)**
  
  - Meaning: Raw command frame sent to the physical device.
  - Description: Usually in hexadecimal format (Hex). For example, the command in the figure is a Modbus or DL/T 645 protocol command for reading meter data.

- **period (Collection Period)**
  
  - Meaning: Time interval between two collection operations.
  - Description: Unit: milliseconds. For example, 1000 means sending a command to the device every 1 second.

- **action (Processing Action)**
  
  - Meaning: Processing method after receiving data returned from the device.
  - Description: Commonly forward, meaning the collected raw data is directly forwarded to the server or cloud platform.

- **object (Physical Port)**
  
  - Meaning: Hardware interface through which the command is sent.
  - Description: For example, uart2 represents the 2nd serial port on the development board (usually corresponding to the RS485 interface on the board).

- **format (Data Format)**
  
  - Meaning: Data encoding used for communication.
  - Description: hex stands for hexadecimal (most common in industrial devices); can also be configured as string or json as required.
  
**Example:**

| Use the configuration shown in the figure for this example.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例4.png
   :alt: RS485与MQTT透传示例4.png


Serial Port List Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parameter Description
"""""""""""""""""""""""

- **interface (Interface Name)**

  - Meaning: Internal identifier for this serial port configuration.
  - Description: Usually named uart1, uart2, etc., for referencing this serial port in other configurations.

- **status (Enable Status)**

  - Meaning: Whether to activate this serial port.
  - Description: enabled for on, disabled for off. Disable unused ports to save resources.

- **device (Device Path)**

  - Meaning: Physical address of the hardware serial port in the Linux system.
  - Description: For example, /dev/ttyS1. Directly corresponds to a physical terminal on the development board; usually no user modification needed.

- **baud_rate (Baud Rate)**

  - Meaning: Transmission rate for serial communication.
  - Description: Must match the connected external device. Common values: 9600, 115200, etc.

- **data_bits / stop_bits / parity (Data Bits / Stop Bits / Parity)**

  - Meaning: Basic underlying protocol parameters for serial communication.
  - Description: Industrial standard is usually 8 data bits, 1 stop bit, none parity. Must match the external device manual.

- **flow_control (Flow Control)**

  - Meaning: Flow control mode for data transmission.
  - Description: Usually set to none. Not recommended unless required by the device.

- **udelay (Microsecond Delay)**

  - Meaning: Forced wait time after serial read/write operations.
  - Description: Unit: microseconds. Used for slow old industrial devices; usually 0.

- **action / object (Processing Action / Forward Target)**

  - Meaning: Destination of data received by the serial port.
  - Description: For example, action = forward and object = server1 means all raw data from the serial port is immediately forwarded to the configured server.

- **format (Data Format)**

  - Meaning: Representation of data.
  - Description: string for text string, hex for raw hexadecimal bytes.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例5.png
   :alt: RS485与MQTT透传示例5.png


**Example**

| This example uses the uart2 interface with device path ttyS6 as shown in the figure.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例6.png
   :alt: RS485与MQTT透传示例6.png


MQTT List Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Parameter Description
"""""""""""""""""""""""

- **interface (Interface Name)**

  - Meaning: Unique identifier for this MQTT connection.
  - Description: Used to distinguish different cloud platform connections (e.g., mqtt1, mqtt2).

- **status (Enable Status)**

  - Meaning: Whether to enable this MQTT connection.
  - Description: When set to enabled, the development board attempts to connect to the cloud server.

- **serverURL (Server Address)**

  - Meaning: Domain name or IP address of the MQTT server (Broker).
  - Description: For example, broker.emqx.io. This is the destination for data upload.

- **clientId (Client ID)**

  - Meaning: Unique ID of the development board on the cloud.
  - Description: Must be unique on the same server; used by the cloud to identify the gateway.

- **username / password (Username / Password)**

  - Meaning: Authentication credentials for connecting to the cloud platform.
  - Description: Fill in the correct credentials if the server enables security authentication.

- **topic_sub (Subscribe Topic)**

  - Meaning: Topic the development board listens to.
  - Description: Used to receive remote control commands from the cloud.

- **topic_pub (Publish Topic)**

  - Meaning: Topic the development board publishes to.
  - Description: All collected data is published to the cloud via this topic.

- **payload (Test Payload)**

  - Meaning: Default sent content.
  - Description: Usually for heartbeat or connection testing.

- **qos (Quality of Service)**

  - Meaning: Reliability level of message delivery.
  - Description: 0 (at most once), 1 (at least once), 2 (exactly once). Recommended 1 for industrial scenarios.

- **timeout (Timeout)**

  - Meaning: Network response waiting time.
  - Description: Unit: milliseconds. Increase in poor network conditions.

- **action / object / format (Processing Action / Forward Target / Data Format)**

  - Meaning: Destination of cloud commands after delivery.
  - Description: For example, action = forward, object = uart2, format = hex.
    This means cloud MQTT messages are automatically converted to hex and sent to field devices via the RS485 serial port.

**Example**

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例7.png
   :alt: RS485与MQTT透传示例7.png


**Web configuration is completed after modifying these three lists. Next, configure the serial port debugging tool.**

4. Computer Setup
-------------------

| Open the serial port debugging tool.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例8.png
   :alt: RS485与MQTT透传示例8.png


| Default interface as shown:

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例9.png
   :alt: RS485与MQTT透传示例9.png


| Click the top-left icon → Tools → Auto-Response Control.
| Open the right toolbar and click Auto-Response on the right.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例10.png
   :alt: RS485与MQTT透传示例10.png


| Right-click the blank area on the right → Import.
| Import the meter configuration .cfg file into auto-response.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例11.png
   :alt: RS485与MQTT透传示例11.png


| After import:

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例12.png
   :alt: RS485与MQTT透传示例12.png


| Then start auto-response.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例13.png
   :alt: RS485与MQTT透传示例13.png

| Serial Port Settings
   Use the configuration shown on the left in the figure for this example.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例14.png
   :alt: RS485与MQTT透传示例14.png


.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例15.png
   :alt: RS485与MQTT透传示例15.png

| After setup, click Start.
| Set both Receive and Send formats to hex.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例16.png
   :alt: RS485与MQTT透传示例16.png

| Finish configuration and open the serial port.
| Data output in the log means startup is successful:

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例17.png
   :alt: RS485与MQTT透传示例17.png


| Serial port debugging assistant configuration completed.
  
**MQTT Client Configuration**

| Install an MQTT client on the computer (MQTTX or mosquitto_sub recommended).
| Click Add Connection in the top-left corner.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例18.png
   :alt: RS485与MQTT透传示例18.png

  
| Use the same MQTT server information as in the gateway configuration:

  - Server address: e.g., broker.emqx.io or user self-built IP
  - Port: 1883 (default if not specified)
  - username/password: default admin and public
  - Client ID: **must not match** the one in the gateway config, otherwise the gateway will be disconnected.

| Click Connect in the top-right corner.
| You may refer to the MQTT list in the configuration editor.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例19.png
   :alt: RS485与MQTT透传示例19.png


.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例20.png
   :alt: RS485与MQTT透传示例20.png


| After connecting, click Add Subscription.
| Edit the topic referring to the configuration file.

| This example:

| To view data uploaded by the gateway (meter readings):
| Enter in MQTTX Topic: emqx/my_gw/shsadl_645_ack

| To view commands received by the gateway:
| Enter in MQTTX Topic: emqx/my_gw/shsadl_645_req

| Use the configuration from the completed MQTT list.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例21.png
   :alt: RS485与MQTT透传示例21.png


| Recommended wildcard (simplest):
| To view both types of data at the same time: emqx/my_gw/#

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例22.png
   :alt: RS485与MQTT透传示例22.png


.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例23.png
   :alt: RS485与MQTT透传示例23.png

  
| After subscription, the MQTT subscriber is configured.
| Meter data will appear as shown.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例24.png
   :alt: RS485与MQTT透传示例24.png


| Note: The miot program runs automatically after the development board starts.

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例25.png
   :alt: RS485与MQTT透传示例25.png


| To terminate:
| Log in as root and run: /etc/init.d/S99miot stop

.. figure:: /image/MYZR-其他/网关/GW510/RS485与MQTT透传示例26.png
   :alt: RS485与MQTT透传示例26.png