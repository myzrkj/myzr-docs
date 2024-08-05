
R16 android4.4 常见问题参考手册
================================

R16 android4.4 常见问题
------------------------

1.在内核中添加spi驱动
~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   $ cd lichee/linux-3.4 
   $ make ARCH=arm menuconfig 
   $ lunch astar_parrot-tina
   $ make kernel_menuconfig

| Device Drivers ---> SPI support ---> <*> User mode SPI device driver support
| 修改

.. code:: shell

   lichee/tools/pack/chips/sun8iw5p1/configs/evb-30/sys_config.fex  
   [spi_board0]  
   modalias      = "at25df641"  
   sflash_size   = 32  
   max_speed_hz  = 50000000
   bus_num       = 0  
   chip_select   = 0  
   mode          = 0  

| 修改成

.. code:: shell 

   [spi_board0]
   modalias      = "spidev"  
   sflash_size   = 32  
   max_speed_hz  = 50000000  
   bus_num       = 0  
   chip_select   = 0  
   mode          = 0  

2.设备信息配置文件
~~~~~~~~~~~~~~~~~~~

| 设备信息配置文件：lichee/tools/pack/chips/sun8iw5p1/configs/evb-30/sys_config.fex

3.以太网不能用
~~~~~~~~~~~~~~~

| 在内核增加驱动

.. code:: shell

   $ make ARCH=arm menuconfig  
   Device Drivers --->
      [*] Network device support --->  
         USB Network Adapters --->
               <*> Multi-purpose USB Networking Frameworksuch as cable modems) 
               <*> SMSC LAN95XX based USB 2.0 10/100 ethernet devices  

4.默认勾选使用以太网
~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   1)在frameworks\base\packages\SettingsProvider\res\values\default.xml 
      <bool name="def_ethernet_on">true</bool>  改成true
      <bool name="def_ethernet_mode">true</bool> 添加以下这两句  
      <bool name="def_ethernet_conf">true</bool>
      <string name="def_ethernet_ifname" translatable="false">eth0</string> 
   
   2)在frameworks\base\packages\SettingsProvider\src\com\android\providers\settings\DatabaseHelper.java 添加
      loadBooleanSetting(stmt, Settings.Global.ETHERNET_CONF, R.bool.def_ethernet_conf) 
      loadStringSetting(stmt, Settings.Global.ETHERNET_IFNAME, R.string.def_ethernet_ifname)


::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2023/5/08  
   * Supporter: Zhong JiaYi
   --------------------------------------------------------------------------------