MYZR-SSD20X-CB096 启动手册
============================

串口线的连接
-------------

|  把串口线的一端连接到开发板的P5口，另一端连接到电脑的串口或USB口。(使用我们提供的串口 转接线)
|  参考《终端软件参考手册》新建串口会话并打开会话。

电源线的连接
-------------

|  把电源适配器的一端连接到开发板的“5V_IN”，另一端插入到市电（220V的交流电）插座。
|  开发板的启动信息

.. code:: shell

   IPL g5da0ceb
   D-1e
   HW Reset
   miupll_233MHz
   MIU0 zq=0x003b
   miu_bw_set
   utmi_1_init done
   utmi_2_init done
   utmi_3_init done
   usbpll init done......
   cpupll init done
   SPI 54M
   clk_init done
   P1 USB_rterm trim=0x0000
   P1 USB_HS_TX_CURRENT trim=0x000d
   P2 USB_rterm trim=0x0000
   P2 USB_HS_TX_CURRENT trim=0x0002
   P3 USB_rterm trim=0x0000
   P3 USB_HS_TX_CURRENT trim=0x0002
   PM_vol_bgap trim=0x0001
   GCR_SAR_DATA trim=0x018f
   ETH 10T output swing trim=0x0011
   ETH 100T output swing trim=0x0011
   ETH RX input impedance trim=0x0000
   ETH TX output impedance trim=0x0000
   MIPI_HS_RTERM trim=0x0001
   MIPI_LP_RTERM trim=0x0000
   128MB
   BIST0_0001-OK
   Enable MMU and CACHE
   Load IPL_CUST from SPINAND
   Checksum OK
   IPL_CUST g5da0ceb
   runUBOOT()
   runUBOOT()
   [SPINAND]
   SPI 54M
   Load UBOOT from SPINAND
   -Verify UBOOT CRC32 passed!
   -Decompress UBOOT XZ
   decomp_size=0x000a1038
   Disable MMU and D-cache before jump to UBOOT
   U-Boot 2015.01 (Apr 02 2022 - 18:22:14)
   Version: I2g#######
   Watchdog enabled
   I2C: ready
   DRAM:
   WARNING: Caches not enabled
   SPINAND: _MDrv_SPINAND_GET_INFO: Found SPINAND INFO
   (0xEF) (0xAA) (0x21)
   SPINAND: board_nand_init: CIS contains part info
   128 MiB
   MMC: MStar SD/MMC: 0
   In: serial
   Out: serial
   Err: serial
   Net: MAC Address 00:30:1B:BA:02:DB
   Auto-Negotiation...
   AN failLink Status Speed:10 Full-duplex:0
   Status Error!
   sstar_emac
   bootcheck start
   fore uup u8KeyPad_KeyVal [0xffff]
   BootMode 0
   NAND read: device 0 offset 0x4c0000, size 0x60000
   Time:73204 us, speed:5371 KB/s
   393216 bytes read: OK
   gpio debug MHal_GPIO_Pad_Set: pin=4
   gpio[4] is 1
   gpio debug MHal_GPIO_Pad_Set: pin=8
   gpio[8] is 0
   NAND read: device 0 offset 0x520000, size 0x500000
   Time:975860 us, speed:5372 KB/s
   5242880 bytes read: OK
   gpio debug MHal_GPIO_Pad_Set: pin=8
   gpio[8] is 1
   ## Booting kernel from Legacy Image at 22000000 ...
   Image Name: MVX4##I2M#g#######KL_LX409##[BR:
   Image Type: ARM Linux Kernel Image (lzma compressed)
   Data Size: 3193760 Bytes = 3 MiB
   Load Address: 20008000
   Entry Point: 20008000
   Verifying Checksum ... OK
   -usb_stop(USB_PORT0)
   -usb_stop(USB_PORT1)
   -usb_stop(USB_PORT2)
   Uncompressing Kernel Image ...
   [XZ] !!!reserved 0x21000000 length=0x 1000000 for xz!!
   XZ: uncompressed size=0x6ac000, ret=7
   OK
   atags:0x20000000
   Starting kernel ...
   Booting Linux on physical CPU 0x0
   Linux version 4.9.84 (linyn@u1804) (gcc version 8.2.1 20180802 (GNU Toolchain
   for the A-profile Architecture 8.2-2018-08 (arm-rel-8.23)) ) #3 SMP PREEMPT Sat
   Apr 2 15:22:50 CST 2022
   CPU: ARMv7 Processor [410fc075] revision 5 (ARMv7), cr=50c5387d
   CPU: div instructions available: patching division code
   CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
   early_atags_to_fdt() success
   OF: fdt:Machine model: INFINITY2M SSC011A-S01A-S
   LXmem is 0x7f00000 PHYS_OFFSET is 0x20000000
   Add mem start 0x20000000 size 0x7f00000!!!!
   LX_MEM = 0x20000000, 0x7f00000
   LX_MEM2 = 0x0, 0x0
   LX_MEM3 = 0x0, 0x0
   EMAC_LEN= 0x0
   DRAM_LEN= 0x0
   deal_with_reserved_mmap memblock_reserve success
   mmap_reserved_config[0].reserved_start=
   0x27c00000
   deal_with_reserve_mma_heap memblock_reserve success
   mma_config[0].reserved_start=
   0x27a00000
   cma: Reserved 2 MiB at 0x27800000
   Memory policy: Data cache writealloc
   percpu: Embedded 14 pages/cpu @c76bc000 s25368 r8192 d23784 u57344
   Built 1 zonelists in Zone order, mobility grouping on. Total pages: 31746
   Kernel command line: console=ttyS0,115200 ubi.mtd=UBI,2048 root=ubi:rootfs ro
   rootfstype=ubifs init=/linuxrc rootwait=1 LX_MEM=0x7f00000
   mma_heap=mma_heap_name0,miu=0,sz=0x200000 mma_memblock_remove=1 highres=off
   mmap_reserved=fb,miu=0,sz=0x300000,max_start_off=0x7C00000,max_end_off=0x7F00000
   mtdparts=nand0:384k@1280k(IPL0),384k(IPL1),384k(IPL_CUST0),384k(IPL_CUST1),768k(
   UBOOT0),768k(UBOOT1),384k(ENV0),0x20000(KEY_CUST),0x60000(LOGO),0x500000(KERNEL)
   ,0x500000(RECOVERY),-(UBI)
   PID hash table entries: 512 (order: -1, 2048 bytes)
   Dentry cache hash table entries: 16384 (order: 4, 65536 bytes)
   Inode-cache hash table entries: 8192 (order: 3, 32768 bytes)
   Memory: 114444K/128000K available (4109K kernel code, 362K rwdata, 1956K rodata,
   192K init, 216K bss, 11508K reserved, 2048K cma-reserved)
   Virtual kernel memory layout:
   vector : 0xffff0000 - 0xffff1000 ( 4 kB)
   fixmap : 0xffc00000 - 0xfff00000 (3072 kB)
   vmalloc : 0xc8000000 - 0xff800000 ( 888 MB)
   lowmem : 0xc0000000 - 0xc7f00000 ( 127 MB)
   modules : 0xbf800000 - 0xc0000000 ( 8 MB)
   .text : 0xc0008000 - 0xc040b8b0 (4111 kB)
   .init : 0xc0628000 - 0xc0658000 ( 192 kB)
   .data : 0xc0658000 - 0xc06b2858 ( 363 kB)
   .bss : 0xc06b4000 - 0xc06ea0a8 ( 217 kB)
   SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=2, Nodes=1
   Preemptible hierarchical RCU implementation.
   Build-time adjustment of leaf fanout to 32.
   RCU restricting CPUs from NR_CPUS=4 to nr_cpu_ids=2.
   RCU: Adjusting geometry for rcu_fanout_leaf=32, nr_cpu_ids=2
   NR_IRQS:16 nr_irqs:16 16
   ms_init_main_intc: np->name=ms_main_intc, parent=gic
   ms_init_pm_intc: np->name=ms_pm_intc, parent=ms_main_intc
   ss_init_gpi_intc: np->name=ms_gpi_intc, parent=ms_main_intc
   Find CLK_cpupll_clk, hook ms_cpuclk_ops
   arm_arch_timer: Architected cp15 timer(s) running at 6.00MHz (virt).
   clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x1623fa770,
   max_idle_ns: 440795202238 ns
   sched_clock: 56 bits at 6MHz, resolution 166ns, wraps every 4398046511055ns
   Switching to timer-based delay loop, resolution 166ns
   Console: colour dummy device 80x30
   console [ttyS0] enabled
   Calibrating delay loop (skipped), value calculated using timer frequency.. 12.00
   BogoMIPS (lpj=60000)
   pid_max: default: 4096 minimum: 301
   Mount-cache hash table entries: 1024 (order: 0, 4096 bytes)
   Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes)
   CPU: Testing write buffer coherency: ok
   CPU0: update cpu_capacity 1024
   CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
   Setting up static identity map for 0x20008240 - 0x20008270
   CPU1: update cpu_capacity 1024
   CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
   Brought up 2 CPUs
   SMP: Total of 2 processors activated (24.00 BogoMIPS).
   CPU: All CPU(s) started in SVC mode.
   devtmpfs: initialized
   VFP support v0.3: implementor 41 architecture 2 part 30 variant 7 rev 5
   clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns:
   19112604462750000 ns
   futex hash table entries: 16 (order: -2, 1024 bytes)
   NET: Registered protocol family 16
   DMA: preallocated 256 KiB pool for atomic coherent allocations
   Version : MVX4##I2M#g#######KL_LX409##[BR:g]#XVM
   GPIO: probe end[ss_gpi_intc_domain_alloc] hw:42 -> v:45
   [MS_PM_INTC] hw:20 -> v:53
   [Padmux]reset Pad_44(reg 0x101e0d; mask0xf00) to GPIO(org: TTL_MODE_1)
   hw-breakpoint: found 5 (+1 reserved) breakpoint and 4 watchpoint registers.
   hw-breakpoint: maximum watchpoint size is 8 bytes.
   SCSI subsystem initialized
   usbcore: registered new interface driver usbfs
   usbcore: registered new interface driver hub
   usbcore: registered new device driver usb
   Linux video capture interface: v2.00
   Bluetooth: Core ver 2.22
   NET: Registered protocol family 31
   Bluetooth: HCI device and connection manager initialized
   Bluetooth: HCI socket layer initialized
   Bluetooth: L2CAP socket layer initialized
   Bluetooth: SCO socket layer initialized
   clocksource: Switched to clocksource arch_sys_counter
   NET: Registered protocol family 2
   TCP established hash table entries: 1024 (order: 0, 4096 bytes)
   TCP bind hash table entries: 1024 (order: 2, 20480 bytes)
   TCP: Hash tables configured (established 1024 bind 1024)
   UDP hash table entries: 128 (order: 0, 6144 bytes)
   UDP-Lite hash table entries: 128 (order: 0, 6144 bytes)
   NET: Registered protocol family 1
   hw perfevents: enabled with armv7_cortex_a7 PMU driver, 5 counters available
   workingset: timestamp_bits=30 max_order=15 bucket_order=0
   squashfs: version 4.0 (2009/01/31) Phillip Lougher
   jffs2: version 2.2. © 2001-2006 Red Hat, Inc.
   fuse init (API version 7.26)
   io scheduler noop registered
   io scheduler deadline registered (default)
   libphy: Fixed MDIO Bus: probed
   tun: Universal TUN/TAP device driver, 1.6
   tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
   RTW: module init start
   RTW: rtl8723du v5.6.5_31829.20190103_COEX20181130-2e2e
   RTW: build time: Apr 2 2022 14:56:21
   RTW: rtl8723du BT-Coex version = COEX20181130-2e2e
   RTW: rtw_inetaddr_notifier_register
   usbcore: registered new interface driver rtl8723du
   RTW: module init ret=0
   usbcore: registered new interface driver asix
   usbcore: registered new interface driver ax88179_178a
   usbcore: registered new interface driver cdc_ether
   usbcore: registered new interface driver net1080
   usbcore: registered new interface driver rndis_host
   usbcore: registered new interface driver cdc_subset
   usbcore: registered new interface driver zaurus
   usbcore: registered new interface driver cdc_ncm
   usbcore: registered new interface driver usbserial
   usbcore: registered new interface driver usbserial_generic
   usbserial: USB Serial support registered for generic
   usbcore: registered new interface driver option
   usbserial: USB Serial support registered for GSM modem (1-port)
   mousedev: PS/2 mouse device common for all mice
   <<-GTP-INFO->> GTP driver installing...
   [ss_gpi_intc_domain_alloc] hw:50 -> v:60
   <<-GTP-INFO->> GTP Driver Version: V2.4<2014/11/28>
   <<-GTP-INFO->> GTP Driver Built@14:55:38, Apr 2 2022
   <<-GTP-INFO->> GTP I2C Address: 0x5d
   <<-GTP-DEBUG->> [2368]GTP power on.
   [Padmux]reset Pad_85(reg 0x101e0a; mask0x1) to GPIO(org: IDAC_MODE)
   <<-GTP-INFO->> Guitar reset
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -110! Process reset.
   <<-GTP-INFO->> Guitar reset
   <<-GTP-ERROR->> GTP i2c test failed time 1.
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -110! Process reset.
   <<-GTP-INFO->> Guitar reset
   <<-GTP-ERROR->> GTP i2c test failed time 2.
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -110! Process reset.
   <<-GTP-INFO->> Guitar reset
   <<-GTP-ERROR->> GTP i2c test failed time 3.
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -110! Process reset.
   <<-GTP-INFO->> Guitar reset
   <<-GTP-ERROR->> GTP i2c test failed time 4.
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x80 0x47
   <<-GTP-ERROR->> I2C Read: 0x8047, 1 bytes failed, errcode: -110! Process reset.
   <<-GTP-INFO->> Guitar reset
   <<-GTP-ERROR->> GTP i2c test failed time 5.
   <<-GTP-ERROR->> I2C communication ERROR!
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x81 0x40
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x81 0x40
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x81 0x40
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x81 0x40
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x81 0x40
   <<-GTP-ERROR->> I2C Read: 0x8140, 6 bytes failed, errcode: -110! Process reset.
   <<-GTP-INFO->> Guitar reset
   <<-GTP-ERROR->> GTP read version failed
   <<-GTP-ERROR->> Read version failed.
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   <<-GTP-ERROR->> I2C Read: 0x41E4, 1 bytes failed, errcode: -110! Process reset.
   <<-GTP-INFO->> Guitar reset
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   <<-GTP-ERROR->> I2C Read: 0x41E4, 1 bytes failed, errcode: -110! Process reset.
   <<-GTP-INFO->> Guitar reset
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   <<-GTP-ERROR->> I2C Read: 0x41E4, 1 bytes failed, errcode: -110! Process reset.
   <<-GTP-INFO->> Guitar reset
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   ERROR: Bus[0] in ms_i2c_xfer_write: Slave dev NAK, Addr: 0xba, Data: 0x41 0xe4
   <<-GTPWelcome to MYZR-GW-FS
   myzr login:
   Welcome to MYZR-GW-FS
   myzr login: root
   login[1007]: root login on 'console'
   client [1051] connected, module:sys
   DISP width: 800,client [1051] connected, module:disp
   height: 1280
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 4, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 2, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 8, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 9, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 10, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 6, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 7, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 11, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 13, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 12, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 14, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 5, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 3, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 38, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 50, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 40, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 43, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 41, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 44, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 42, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 46, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 50, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 45, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 50, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 22, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 23, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 30, hdmiTx = 1 Not Fund!!!
   [MI_SYSCFG_GetPanelInfo 50] eTiming = 32, hdmiTx = 1 Not Fund!!!
   client [1051] connected, module:panel
   [MI_PANEL_Init][332]LCD environment is Invalid
   main 162 687
   Error: cannot open framebuffer device: No suchclient [1051] disconnected,
   module:panel
   client [1051] disconnected, module:disp
   file or directory
   client [1051] disconnected, module:sys
   root@myzr:/opt1

开发板登录
-----------

|  启动系统完后输出“myzr login:”时，可以登录：
|  【用户名】：root
|  【密码】：无
|  注：登录后可以通过“passwd”命令来设置和修改密码。