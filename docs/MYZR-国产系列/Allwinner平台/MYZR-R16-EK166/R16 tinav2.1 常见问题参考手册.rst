
R16 tinav2.1 常见问题参考手册
==============================

R16 tinav2.1常见问题
----------------------

1.分区
~~~~~~~

| 修改target/allwinner/astar-parrot/configs/sys_partition.fex
| 例如：

.. code:: shell

    [partition]
    name        = rootfs_data
    size        = 12582912
    user_type    = 0x8000

| 修改其中的size属性，单位: 扇区。
| 如要修改成1G，计算方法如下
| size = 1024 * 1024 * 1024 / 512

2.把文件打包到rootfs
~~~~~~~~~~~~~~~~~~~~~

| 将文件放到package/base-files/files目录下即可。如果文件过大，在pack时报错，修改分区表的rootfs分区的大小

3.设备信息配置文件
~~~~~~~~~~~~~~~~~~

| 设备信息配置文件：target/allwinner/astar-parrot/configs/sys_config.fex

4.增加spi
~~~~~~~~~~

| 1) 在内核中添加spi 驱动

.. code:: shell

   $ cd tinaV2.1
   $ source build/envsetup.sh
   $ lunch astar_parrot-tina
   $ make kernel_menuconfig  
   Device Drivers --->
   SPI support --->
   <*> User mode SPI device driver support  

| 2) 修改

.. code:: shell

   tinaV2.1/target/allwinner/astar-parrot/configs/sys_config.fex
   [spi_board0]
   modalias = "at25df641"
   sflash_size = 32
   max_speed_hz = 50000000
   bus_num = 0
   chip_select = 0
   mode = 0

| 修改成

.. code:: shell

   [spi_board0]
   modalias = "spidev"
   sflash_size = 32
   max_speed_hz = 50000000
   bus_num = 0
   chip_select = 0
   mode = 0

5.以太网不可用
~~~~~~~~~~~~~~~

.. code:: shell

   $ cd tinaV2.1
   $ make kernel_menuconfig
   Device Drivers --->
      [*] Network device support --->
         USB Network Adapters --->
            <*> Multi-purpose USB Networking Frameworksuch as cable modems)
            <*> SMSC LAN95XX based USB 2.0 10/100 ethernet devices