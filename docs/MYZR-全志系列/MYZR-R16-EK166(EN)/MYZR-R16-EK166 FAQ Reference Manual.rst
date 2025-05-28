
MYZR-R16-EK166 FAQ Reference Manual
=====================================

About R16 increase spi
------------------------

Linux system
~~~~~~~~~~~~~~

1. Add spi drivers to the kernel

.. code-block:: shell

   $ cd tinaV2.1 
   $ source build/envsetup.sh
   $ lunch astar_parrot-tina
   $ make kernel_menuconfig
   Device Drivers --->
   SPI support --->
   <*> User mode SPI device driver support



2. Modification

.. code-block:: shell

   tinaV2.1/target/allwinner/astar-parrot/configs/sys_config.fex  
   [spi_board0]  
   modalias      = "at25df641"  
   sflash_size   = 32  
   max_speed_hz  = 50000000
   bus_num       = 0  
   chip_select   = 0  
   mode          = 0

| changed to

.. code-block:: shell

   [spi_board0]
   modalias      = "spidev"  
   sflash_size   = 32  
   max_speed_hz  = 50000000  
   bus_num       = 0  
   chip_select   = 0  
   mode          = 0  

Android system
~~~~~~~~~~~~~~~~

1. Add spi drivers to the kernel

.. code-block:: shell

   $ cd lichee/linux-3.4
   $ make ARCH=arm menuconfig
   Device Drivers --->
   SPI support --->
   <*> User mode SPI device driver support

2. Modification

.. code-block:: shell

   lichee/tools/pack/chips/sun8iw5p1/configs/evb-30/sys_config.fex    
   [spi_board0]  
   modalias      = "at25df641"    
   sflash_size   = 32    
   max_speed_hz  = 50000000  
   bus_num       = 0    
   chip_select   = 0   
   mode          = 0   

| changed to

.. code-block:: shell

   [spi_board0]  
   modalias      = "spidev"    
   sflash_size   = 32    
   max_speed_hz  = 50000000    
   bus_num       = 0   
   chip_select   = 0   
   mode          = 0


::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2023/5/08  
   * Supporter: Zhong JiaYi
   --------------------------------------------------------------------------------