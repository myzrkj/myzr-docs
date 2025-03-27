MYZR-SSD2351-EK112快速启动手册
================================

准备工作
~~~~~~~~~

| 开发板：1个
| TYPEC数据线：1条
| TTL串口模块：1个
| 杜板线：若干
| 网线：1根

串口软件设置
~~~~~~~~~~~~~

| 波特率：115200
| 数据位：8bit
| 停止位：1bit
| 校验位：none

拨码设置以及TTL串口模块
~~~~~~~~~~~~~~~~~~~~~~~

拨码设置
---------

| 启动拨码模式：1: on， 2: on， 3: off， 4 : off

TTL串口模块接法
----------------

| 座子：J3
| 按以下CPU的对应端和TTL模块的管脚连接起来

+---------+-------------------------+-------------+---------+
| CPU端： | J3_1:RX管脚(正方形焊盘) | J3_2:TX管脚 | J3_3:地 |
+=========+=========================+=============+=========+
| TTL端： | TX管脚                  | RX管脚      | GND     |
+---------+-------------------------+-------------+---------+


串口启动
~~~~~~~~~~

.. code:: shell

  #用TTL模块，把电脑和板子连接起来。插入TYPEC线，开机
  提示信息如下：
  IPL gf7fc380
  D-19
  CPU=800MHz
  HEAP: [0xa0018330~0xa0018430]
  SHM: [0xa0013830~0xa0018330]
  RECORD: tc at 0xa00138c0
  HW Reset
  SPI 104M
  [SPINAND] RFC use command 0x6b
  [SPINAND] dummy clock 0x8
  [SPINAND] Program with command 0x32.
  [SPINAND] Random with command 0x34.
  [FLASH] BDMA mode.
  Loading Environment from SPIFlash... 
  OK
  QFN128 NTC1G DDR3 DFS(2133, 800)
  miu pll: 300MHz
  DRAM Size: 128MB
  ddr train finish
  HEAP: [0x23d00000~0x23e00000]
  SHM: [0x22440000~0x23d00000 0x7dbd3830]
  IMG_LOAD@ devs:0xa img:CUST bak:0 ofs:0x0 sz:0x580 dst:0x23d00000
  IMG_LOAD@ devs:0xa img:CUST bak:0 ofs:0x0 sz:0x7520 dst:0x22400000
  IMG_VERIFY@ type:1
  DECOMP@0 from 0x22400000 to 0x22400000
  Flashing D-Cache and Disabling MMU
  OS_JUMP@ method:1 entry_pointer:0x22400000

  IPL_CUST gf7fc380
  D-19
  HEAP: [0x23d00000~0x23e00000]
  RECORD: moving tc from 0x22440090 to 0x263ff000
  SPI 104M
  IMG_LOAD@ devs:0xa img:TFA bak:0 ofs:0x0 sz:0x580 dst:0x23d00000
  IMG_LOAD@ devs:0xa img:TFA bak:0 ofs:0x0 sz:0xc10a dst:0x263fffc0
  IMG_VERIFY@ type:2
  DECOMP@0 from 0x26400000 to 0x26400000
  IMG_LOAD@ devs:0xa img:UBOOT bak:0 ofs:0x0 sz:0x580 dst:0x23d00580
  IMG_LOAD@ devs:0xa img:UBOOT bak:0 ofs:0x0 sz:0x55268 dst:0x22444680
  IMG_VERIFY@ type:4
  DECOMP@2 from 0x224446c0 to 0x23e00000
  Flashing D-Cache
  OS_JUMP@ method:2 entry_pointer:0x23e00000


  U-Boot 2021.10 (Mar 03 2025 - 07:57:25 +0000)

  SoC: SigmaStar pcupid
  Model: PCUPID
  Version: P###g#######
  DRAM:  128 MiB
  WDT:   Not found!
  NAND:  SPI 104M
  [SPINAND] RFC use command 0x6b
  [SPINAND] dummy clock 0x8
  [SPINAND] Program with command 0x32.
  [SPINAND] Random with command 0x34.
  [FLASH] BDMA mode.
  spi clk already initialized
  [FLASH] dev_id = 0xee
  [FLASH] mfr_id = 0xc8, dev_id= 0x91 id_len = 0x2
  128 MiB
  MMC:   Fail to get pad(0x20309) ip(0x2_8)  form padmux !
  Fail to get pad(0x20003) ip(0x0_2)  form padmux !
  MSC: 0, MSC: 1
  Loading Environment from NAND... 
  ENV: offset = 0x4c0000 size = 0x40000
  ENV1: offset = 0x500000 size = 0x40000
  OK
  In:    serial
  Out:   serial
  Err:   serial
  Net:   No ethernet found.
  Hit any key to stop autoboot:  0 
  firmwarefs_open: open PQ.bin fail(-2)
  JPD_SW_decode time: 74259 us
  JPD_SW_decode time: 13134 us
  cost time: 508815 us
  bitwidth = 16
  
  ## Booting kernel from Legacy Image at 23000000 ...
     Image Name:   MVX4##P###g#######KL_LX601##[BR:
     Image Type:   ARM Linux Kernel Image (lzma compressed)
     Data Size:    3436492 Bytes = 3.3 MiB
     Load Address: 20008000
     Entry Point:  20008000
     Verifying Checksum ... OK
     Uncompressing Kernel Image
  [XZ] !!!reserved 0x22000000 length=0x 1000000 for xz!!
     XZ: uncompressed size=0x9651ec, ret=7

  Starting kernel ...

  Booting Linux on physical CPU 0x0
  Linux version 6.1.111-rt42 (tangbin@myzr-u2004) (arm-sigmastar-linux-uclibcgnueabihf-12.4.0-gcc (crosstool-NG 1.26.0) 12.4.0, GNU ld (crosstool-NG 1.26.0) 2.40) #120 SMP PREEMPT Wed Mar  5 04:14:41 UTC 2025
  CPU: ARMv7 Processor [411fd040] revision 0 (ARMv7), cr=50c5383d
  CPU: div instructions available: patching division code
  CPU: PIPT / VIPT nonaliasing data cache, VIPT aliasing instruction cache
  early_atags_to_fdt() success

.. code:: shell

  OF: fdt: Machine model: PCUPID
  LXmem is 0x8000000 PHYS_OFFSET is 0x20000000
  Add mem start 0x20000000 size 0x8000000!!!!

  LX_MEM  = 0x20000000, 0x8000000
  LX_MEM2 = 0x0, 0x0
  LX_MEM3 = 0x0, 0x0
  MMU_MEM = 0x0, 0x0
  EMAC_LEN= 0x0
  DRAM_LEN= 0x0
  Memory policy: Data cache writealloc
  OF: reserved mem: invalid size property in 'cma0' node.
  deal_with_reserved_mmap memblock_reserve success mmap_reserved_config[0].reserved_start=
  0x26800000

  deal_with_reserve_mma_heap memblock_reserve success mma_config[0].reserved_start=
  0x27600000 size:a00000

  deal_with_reserve_mma_heap memblock_reserve success mma_config[1].reserved_start=
  0x25cf7000 size:708000

  cma: Reserved 16 MiB at 0x24c00000
  Zone ranges:
    Normal   [mem 0x0000000020000000-0x00000000275fffff]
    HighMem  empty
  Movable zone start for each node
  Early memory node ranges
    node   0: [mem 0x0000000020000000-0x0000000025cf6fff]
    node   0: [mem 0x00000000263ff000-0x00000000275fffff]
  Initmem setup node 0 [mem 0x0000000020000000-0x00000000275fffff]
  On node 0, zone Normal: 776 pages in unavailable ranges
  psci: probing for conduit method from DT.
  psci: PSCIv1.1 detected in firmware.
  psci: Using standard PSCI v0.2 function IDs
  psci: MIGRATE_INFO_TYPE not supported.
  psci: SMC Calling Convention v1.2
  percpu: Embedded 11 pages/cpu s15584 r8192 d21280 u45056
  Built 1 zonelists, mobility grouping on.  Total pages: 28172
  Kernel command line: ubi.mtd=ubia,2048 root=/dev/mtdblock7 rootfstype=squashfs ro init=/linuxrc LX_MEM=0x8000000 mma_heap=mma_heap_name0,miu=0,sz=0xA00000 mma_memblock_remove=1 cma=16M mma_heap=mma_heap_fb,miu=0,sz=0x708000 mmap_reserved=fb,miu=0,sz=0x800000,max_start_off=0x6800000,max_end_off=0x7000000 mtdparts=nand0:1792k@1280k(BOOT),1792k(BOOT_BAK),256k(ENV),256k(ENV1),384k(DDRTRAIN),5m(KERNEL),5m(RECOVERY),6m(rootfs),768k(vendor_storage),1m(MISC),107136k(ubia)
  Dentry cache hash table entries: 16384 (order: 4, 65536 bytes, linear)
  Inode-cache hash table entries: 8192 (order: 3, 32768 bytes, linear)
  mem auto-init: stack:all(zero), heap alloc:off, heap free:off
  Memory: 77488K/113632K available (4096K kernel code, 436K rwdata, 2192K rodata, 1024K init, 157K bss, 19760K reserved, 16384K cma-reserved, 0K highmem)
  SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
  rcu: Preemptible hierarchical RCU implementation.
  rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
  NR_IRQS: 16, nr_irqs: 16, preallocated irqs: 16
  GICv3: 192 SPIs implemented
  GICv3: 0 Extended SPIs implemented
  GICv3: GICv3 features: 16 PPIs
  GICv3: CPU0: found redistributor 0 region 0:0x16080000
  sstar_main_intc_init: np->name=sstar_main_intc, parent=gic
  sstar_pm_main_intc_init: np->name=sstar_pm_main_intc, parent=sstar_main_intc
  sstar_gpi_intc_init: np->name=sstar_gpi_intc, parent=sstar_main_intc
  sstar_pm_gpi_intc_init: np->name=sstar_pm_gpi_intc, parent=sstar_main_intc
  rcu: srcu_init: Setting srcu_struct sizes based on contention.
  [hal_clk_ipupll_init] ipupll already init, skip
  arch_timer: cp15 timer(s) running at 6.00MHz (virt).
  clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x1623fa770, max_idle_ns: 440795202238 ns
  sched_clock: 56 bits at 6MHz, resolution 166ns, wraps every 4398046511055ns
  Switching to timer-based delay loop, resolution 166ns
  printk: console [ttyS0] enabled
  Calibrating delay loop (skipped), value calculated using timer frequency.. 12.00 BogoMIPS (lpj=60000)
  CPU: Testing write buffer coherency: ok
  pid_max: default: 4096 minimum: 301
  Mount-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
  Mountpoint-cache hash table entries: 1024 (order: 0, 4096 bytes, linear)
  CPU0: thread -1, cpu 0, socket 0, mpidr 80000000
  Setting up static identity map for 0x20100000 - 0x20100054
  rcu: Hierarchical SRCU implementation.
  rcu: 	Max phase no-delay instances is 1000.
  printk: console [ttyS0] printing thread started
  smp: Bringing up secondary CPUs ...
  GICv3: CPU1: found redistributor 1 region 0:0x160a0000
  CPU1: thread -1, cpu 1, socket 0, mpidr 80000001
  GICv3: CPU2: found redistributor 2 region 0:0x160c0000
  CPU2: thread -1, cpu 2, socket 0, mpidr 80000002
  GICv3: CPU3: found redistributor 3 region 0:0x160e0000
  CPU3: thread -1, cpu 3, socket 0, mpidr 80000003
  smp: Brought up 1 node, 4 CPUs
  SMP: Total of 4 processors activated (48.00 BogoMIPS).
  CPU: All CPU(s) started in SVC mode.
  devtmpfs: initialized
  VFP support v0.3: implementor 41 architecture 3 part 40 variant 4 rev 3
  clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
  futex hash table entries: 16 (order: -2, 1024 bytes, linear)
  NET: Registered PF_NETLINK/PF_ROUTE protocol family
  DMA: preallocated 256 KiB pool for atomic coherent allocations


  Version : MVX4##P###g#######KL_LX601##[BR:g]#XVM

  platform soc: Fixed dependency cycle(s) with /soc/sstar_main_intc
  GPIO: probe end
  [Padmux]reset PAD9(reg 0x103c00:49; mask0x8000) t0 SDIO_MODE_2 (org: SD_BOOT_MODE_1)
  [Padmux]reset PAD79(reg 0x153f00:70; mask0x1) t0 FUART1_MODE_3 (org: OUTP_RX0_CH0_IE_CLR_MODE_0)
  [Padmux]reset PAD80(reg 0x153f00:70; mask0x2) t0 FUART1_MODE_3 (org: OUTN_RX0_CH0_IE_CLR_MODE_0)
  [Padmux]reset PAD81(reg 0x153f00:70; mask0x4) t0 FUART1_MODE_3 (org: OUTP_RX0_CH1_IE_CLR_MODE_0)
  [Padmux]reset PAD82(reg 0x153f00:70; mask0x8) t0 FUART1_MODE_3 (org: OUTN_RX0_CH1_IE_CLR_MODE_0)
  [Padmux]reset PAD83(reg 0x153f00:70; mask0x10) t0 FUART2_MODE_3 (org: OUTP_RX0_CH2_IE_CLR_MODE_0)
  [Padmux]reset PAD84(reg 0x153f00:70; mask0x20) t0 FUART2_MODE_3 (org: OUTN_RX0_CH2_IE_CLR_MODE_0)
  [Padmux]reset PAD85(reg 0x153f00:70; mask0x40) t0 FUART2_MODE_3 (org: OUTP_RX0_CH3_IE_CLR_MODE_0)
  [Padmux]reset PAD86(reg 0x153f00:70; mask0x80) t0 FUART2_MODE_3 (org: OUTN_RX0_CH3_IE_CLR_MODE_0)
  [Padmux]reset PAD96(reg 0x103c00:64; mask0x7) t0 FUART3_2W_MODE_2 (org: MIPI_TX_MODE_1)
  [Padmux]reset PAD96(reg 0x153400:5c; mask0x1) t0 FUART3_2W_MODE_2 (org: OUTP_CH0_IE_CLR_MODE_0)
  [Padmux]reset PAD97(reg 0x153400:5c; mask0x100) t0 FUART3_2W_MODE_2 (org: OUTN_CH0_IE_CLR_MODE_0)
  [Padmux]reset PAD16(reg 0x103e00:10; mask0x8) t0 UART5_MODE_3 (org: GPIO_MODE)
  hw-breakpoint: found 5 (+1 reserved) breakpoint and 4 watchpoint registers.
  hw-breakpoint: maximum watchpoint size is 8 bytes.
  SCSI subsystem initialized
  pps_core: LinuxPPS API ver. 1 registered
  pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
  PTP clock support registered

  [MIU ERR] [sstar_miu_clk_register@532] [sstar_miu_clk_register] clk_miu enable 0
  [hal_clk_mtcmos_isp_enable] clk_mtcmos_isp already enabled!
  Do qos-initialize
  Advanced Linux Sound Architecture Driver Initialized.
  Bluetooth: Core ver 2.22
  NET: Registered PF_BLUETOOTH protocol family
  Bluetooth: HCI device and connection manager initialized
  Bluetooth: HCI socket layer initialized
  Bluetooth: L2CAP socket layer initialized
  Bluetooth: SCO socket layer initialized
  clocksource: Switched to clocksource arch_sys_counter
  NET: Registered PF_INET protocol family
  IP idents hash table entries: 2048 (order: 2, 16384 bytes, linear)
  tcp_listen_portaddr_hash hash table entries: 256 (order: 0, 5120 bytes, linear)
  Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
  TCP established hash table entries: 1024 (order: 0, 4096 bytes, linear)
  TCP bind hash table entries: 1024 (order: 3, 40960 bytes, linear)
  TCP: Hash tables configured (established 1024 bind 1024)
  UDP hash table entries: 128 (order: 0, 6144 bytes, linear)
  UDP-Lite hash table entries: 128 (order: 0, 6144 bytes, linear)
  NET: Registered PF_UNIX/PF_LOCAL protocol family
  RPC: Registered named UNIX socket transport module.
  RPC: Registered udp transport module.
  RPC: Registered tcp transport module.
  RPC: Registered tcp NFSv4.1 backchannel transport module.
  Initialise system trusted keyrings
  workingset: timestamp_bits=30 max_order=15 bucket_order=0
  squashfs: version 4.0 (2009/01/31) Phillip Lougher
  jffs2: version 2.2. © 2001-2006 Red Hat, Inc.
  fuse: init (API version 7.38)
  Key type asymmetric registered
  Asymmetric key parser 'x509' registered
  io scheduler mq-deadline registered
  io scheduler kyber registered
  mousedev: PS/2 mouse device common for all mice
  i2c_dev: i2c /dev entries driver
  Bluetooth: HCI UART driver ver 2.3
  Bluetooth: HCI UART protocol H4 registered
  Bluetooth: HCI UART protocol Three-wire (H5) registered
  SMCCC: SOC_ID: ID = jep106:0000:8192 Revision = 0x00000000
  no urdma irq resource defined
  no urdma irq resource defined
  no urdma irq resource defined
  no urdma irq resource defined
  no urdma irq resource defined
  no urdma irq resource defined
  no urdma irq resource defined
  no urdma irq resource defined
  no urdma irq resource defined
  mdio_bus mdio-bus@emac0: ethernet-phy@0 has invalid PHY address
  mdio_bus mdio-bus@emac0: scan phy ethernet-phy at address 0
  mdio_bus mdio-bus@emac0: scan phy ethernet-phy at address 1
  [emac_phy_connect][2999] connected mac emac0 to PHY at mdio-bus@emac0:01 [uid=02430c54, driver=Generic PHY]
  sstar,rtcpwc 1f006800.rtcpwc: registered as rtc0
  sstar,rtcpwc 1f006800.rtcpwc: setting system clock to 1970-01-01T00:28:46 UTC (1726)
  input: rtcpwc as /devices/soc0/soc/1f006800.rtcpwc/input/input0
  [Padmux]reset PAD18(reg 0x103e00:12; mask0x8) t0 I2C2_MODE_3 (org: GPIO_MODE)
  [Padmux]reset PAD19(reg 0x103e00:13; mask0x8) t0 I2C2_MODE_3 (org: GPIO_MODE)
  [Padmux]reset PAD126(reg 0x103e00:7e; mask0x8) t0 I2C3_MODE_2 (org: GPIO_MODE)
  [Padmux]reset PAD125(reg 0x103e00:7d; mask0x8) t0 I2C3_MODE_2 (org: GPIO_MODE)
  [sstar_cpufreq_init] Current clk=800000000
  request for verification of policy (0 - 2147483647 kHz) for cpu 0
  verification lead to (200000 - 1450000 kHz) for cpu 0
  sstar_pwm_probe: fail to config dead time
  sstar_pwm_probe: fail to config dead time
  sstar_pwm_probe: fail to config dead time
  sstar_pwm_probe: fail to config dead time
  sstar_pwm_probe: fail to config dead time
  sstar_pwm_probe: fail to config dead time
  spi 1f222000.spi: chipselect 0 already in use
  spi_master spi0: spi_device register error /soc/spi@1f222000/spidev@0
  spi_master spi0: Failed to create SPI device for /soc/spi@1f222000/spidev@0
  SPI 104M
  [SPINAND] RFC use command 0x6b
  [SPINAND] dummy clock 0x8
  [SPINAND] Program with command 0x32.
  [SPINAND] Random with command 0x34.
  [FLASH] BDMA mode.
  [FLASH] dev_id = 0xee
  [FLASH] mfr_id = 0xc8, dev_id= 0x91 id_len = 0x2
  nand: device found, Manufacturer ID: 0xc8, Chip ID: 0x91
  nand: Unknown nand0
  nand: 128 MiB, MLC, erase size: 128 KiB, page size: 2048, OOB size: 64
  nand: WARNING: nand0: the ECC used on your system (4b/512B) is too weak compared to the one required by the NAND chip (512b/4B)
  11 cmdlinepart partitions found on MTD device nand0
  Creating 11 MTD partitions on "nand0":
  0x000000140000-0x000000300000 : "BOOT"
  0x000000300000-0x0000004c0000 : "BOOT_BAK"
  0x0000004c0000-0x000000500000 : "ENV"
  0x000000500000-0x000000540000 : "ENV1"
  0x000000540000-0x0000005a0000 : "DDRTRAIN"
  0x0000005a0000-0x000000aa0000 : "KERNEL"
  0x000000aa0000-0x000000fa0000 : "RECOVERY"
  0x000000fa0000-0x0000015a0000 : "rootfs"
  0x0000015a0000-0x000001660000 : "vendor_storage"
  0x000001660000-0x000001760000 : "MISC"
  0x000001760000-0x000008000000 : "ubia"
  Err: Could not get dts [wakeup] option!
  wakeup: probe of soc:wakeup failed with error 1
  sstar-asoc-card soc:asoc_sound: i = 0, codec_name = sstar-dummy-codec1
  sstar-bach 1f2a0400.bach1: pcmC0 dma buffer size 0x40000
  sstar-bach 1f2a0400.bach1: physical dma address 0x24c50000
  sstar-bach 1f2a0400.bach1: miu address 0x04c50000
  sstar-bach 1f2a0400.bach1: virtual dma address (ptrval)
  sstar-bach 1f2a0400.bach1: pcmP0 dma buffer size 0x100000
  sstar-bach 1f2a0400.bach1: physical dma address 0x24c90000
  sstar-bach 1f2a0400.bach1: miu address 0x04c90000
  sstar-bach 1f2a0400.bach1: virtual dma address (ptrval)
  sstar-asoc-card soc:asoc2_sound: i = 0, codec_name = sstar-dummy-codec2
  sstar-bach 1f2a0400.bach2: pcmC1 dma buffer size 0x40000
  sstar-bach 1f2a0400.bach2: physical dma address 0x24d90000
  sstar-bach 1f2a0400.bach2: miu address 0x04d90000
  sstar-bach 1f2a0400.bach2: virtual dma address (ptrval)
  sstar-bach 1f2a0400.bach2: pcmP1 dma buffer size 0x40000
  sstar-bach 1f2a0400.bach2: physical dma address 0x24dd0000
  sstar-bach 1f2a0400.bach2: miu address 0x04dd0000
  sstar-bach 1f2a0400.bach2: virtual dma address (ptrval)
  sstar-asoc-card soc:asoc2_sound: ASoC: driver name too long 'sstar-asoc2-card' -> 'sstar-asoc2-car'
  sstar-asoc-card soc:asoc3_sound: i = 0, codec_name = sstar-dummy-codec3
  sstar-bach 1f2a0400.bach3: pcmC0 dma buffer size 0x40000
  sstar-bach 1f2a0400.bach3: physical dma address 0x24c50000
  sstar-bach 1f2a0400.bach3: miu address 0x04c50000
  sstar-bach 1f2a0400.bach3: virtual dma address (ptrval)
  sstar-bach 1f2a0400.bach3: pcmP2 dma buffer size 0x40000
  sstar-bach 1f2a0400.bach3: physical dma address 0x24e10000
  sstar-bach 1f2a0400.bach3: miu address 0x04e10000
  sstar-bach 1f2a0400.bach3: virtual dma address (ptrval)
  sstar-asoc-card soc:asoc3_sound: ASoC: driver name too long 'sstar-asoc3-card' -> 'sstar-asoc3-car'
  NET: Registered PF_PACKET protocol family
  sstar_pm_init init ...
  Registering SWP/SWPB emulation handler
  Loading compiled-in X.509 certificates
  Key type .fscrypt registered
  Key type fscrypt-provisioning registered
  Key type encrypted registered
  ubi0: attaching mtd10
  ubi0: scanning is finished
  ubi0 warning: ubi_eba_init: cannot reserve enough PEBs for bad PEB handling, reserved 9, need 20
  ubi0: attached mtd10 (name "ubia", size 104 MiB)
  ubi0: PEB size: 131072 bytes (128 KiB), LEB size: 126976 bytes
  ubi0: min./max. I/O unit sizes: 2048/2048, sub-page size 2048
  ubi0: VID header offset: 2048 (aligned 2048), data offset: 4096
  ubi0: good PEBs: 837, bad PEBs: 0, corrupted PEBs: 0
  ubi0: user volume: 2, internal volumes: 1, max. volumes count: 128
  ubi0: max/mean erase counter: 1/0, WL threshold: 4096, image sequence number: 886906549
  ubi0: available PEBs: 0, total reserved PEBs: 837, PEBs reserved for bad PEB handling: 9
  ubi0: background thread "ubi_bgt0d" started, PID 473
  OF: fdt: not creating '/sys/firmware/fdt': CRC check failed
  clk: Disabling unused clocks
  ALSA device list:
    #0: sstar-asoc-card
    #1: sstar-asoc2-card
    #2: sstar-asoc3-card
  mtdblock: MTD device 'rootfs' is NAND, please consider using UBI block devices instead.
  VFS: Mounted root (squashfs filesystem) readonly on device 31:7.
  devtmpfs: mounted
  Freeing unused kernel image (initmem) memory: 1024K
  Run /linuxrc as init process
  random: crng init done
  net.core.rmem_default = 163840
  net.core.rmem_max = 163840
  net.core.wmem_default = 524288
  net.core.wmem_max = 1048576
  net.ipv4.tcp_mem = 924  1232  1848
  net.ipv4.tcp_rmem = 4096  87380  325120
  net.ipv4.tcp_wmem = 4096  131072  393216
  /etc/init.d/rcS: line 16: resize2fs: not found
  /etc/init.d/rcS: line 17: UBIFS (ubi0:0): Mounting in unauthenticated mode
  UBIFS (ubi0:0): background thread "ubifs_bgt0_0" started, PID 489
  resize2fs: not found
  UBIFS (ubi0:0): recovery needed
  UBIFS (ubi0:0): recovery completed
  UBIFS (ubi0:0): UBIFS: mounted UBI device 0, volume 0, name "miservice"
  UBIFS (ubi0:0): LEB size: 126976 bytes (124 KiB), min./max. I/O unit sizes: 2048 bytes/2048 bytes
  UBIFS (ubi0:0): FS size: 19427328 bytes (18 MiB, 153 LEBs), max 163 LEBs, journal size 2920448 bytes (2 MiB, 23 LEBs)
  UBIFS (ubi0:0): reserved for root: 0 bytes (0 KiB)
  UBIFS (ubi0:0): media format: w4/r0 (latest is w5/r0), UUID 3C18967F-076F-4B9A-8442-6E3EA08CE71D, small LPT model
  UBIFS (ubi0:1): Mounting in unauthenticated mode
  UBIFS (ubi0:1): background thread "ubifs_bgt0_1" started, PID 492
  UBIFS (ubi0:1): recovery needed
  UBIFS (ubi0:1): recovery completed
  UBIFS (ubi0:1): UBIFS: mounted UBI device 0, volume 1, name "customer"
  /etc/init.d/rcS: line 22: fwfs: not found
  insmod: can't read '/config/modules/6.1/nfs_ssc.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/libarc4.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/scsi_mod.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/md4.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/seqiv.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/libdes.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/grace.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/sunrpc.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/lockd.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/nfs.ko': No such file or directory
  Fail to get pad(0x0) ip(0x0_8)  form padmux !
  SDMMC0 >> [Hal_CARD_SetBustiming] DEFS mode. <<
  insmod: can't read '/config/modules/6.1/sd_mod.ko': No such file or directory
  err: i2c-3 write start err!
  err: i2c-3 stop signal err!
  err:i2c-3 xfer error: -7
  Goodix-TS 3-005d: Error reading 1 bytes from 0x8140: -1
  err: i2c-3 write start err!
  err: i2c-3 stop signal err!
  err:i2c-3 xfer error: -7
  Goodix-TS 3-005d: Error reading 1 bytes from 0x8140: -1
  Goodix-TS 3-005d: I2C communication failure: -1
  insmod: can't read '/config/modules/6.1/pstore.ko': No such file or directory
  insmod: can't read '/config/modules/6.1/pstore_zone.ko': No such file or directory
  insmod:err: i2c-2 err dma write transform len:0 != para_len:2
  err:i2c-2 xfer error: -7
  rtc-hym8563 2-0051: could not init device, -1
   can't read '/config/modules/6.1/pstore_blk.ko': No such file or directory
  module [sys] init 2024-12-16_10-24-26



  mma_heap_name0,miu=0,sz=a00000,reserved_start=27600000
  mi_sys_mma_allocator_create success, heap_base_addr=27600000 length=a00000 
  mma_heap_fb,miu=0,sz=708000,reserved_start=25cf7000
  mi_sys_mma_allocator_create success, heap_base_addr=25cf7000 length=708000 
  mi_sys_mma_allocator_create success, heap_base_addr=20000000 length=43800 
  protect_panic_on: 0
  snr_sr0_par_mode = 2
  snr_sr0_par_rst_mode: no value!!
  snr_sr0_par_pdn_mode: no value!!
  snr_sr0_par_mclk_mode = 2
  snr_sr0_bt656_mode = 1
  snr_sr0_bt656_rst_mode: no value!!
  snr_sr0_bt656_pdn_mode: no value!!
  snr_sr0_bt656_mclk_mode = 2
  snr_sr0_mipi_mode = 5
  snr_sr0_mipi_rst_mode: no value!!
  snr_sr0_mipi_pdn_mode: no value!!
  snr_sr0_mipi_mclk_mode = 1
  snr_sr2_mipi_mode = 5
  snr_sr2_mipi_rst_mode: no value!!
  snr_sr2_mipi_pdn_mode: no value!!
  snr_sr2_mipi_mclk_mode = 1
  snr_sr0_rst_gpio = 69
  snr_sr2_rst_gpio = 65
  snr_sr0_pdn_gpio = 65
  snr0_paral_i2c = 0
  snr0_mipi_i2c = 1
  snr2_mipi_i2c = 0
  module [sensor] init
  module [rgn] init
  [RGN] osd blending : disable
  module [gfx] init
  module [disp] init
  [FB] keep bootlogo: false
  module [fb] init
  module [dummy] init
  module [vif] init
  [VIF] vif0ch int irq 82
  [VIF] vif0dma int irq 83
  [VIF] clk 0
  [VIF] clk 1
  mhal module [isp] init
  [ISP Driver init]
  [DRV_ISP_WORK_EarlyInit] ==================== >>>>>>>>>>
  [DRV_ISP_CLK_Register] clk_isp enable 0
  [DRV_ISP_CLK_Register] clk_isp enable 1
  [DRV_ISP_CLK_Register] clk_isp enable 2
  [DRV_ISP_CLK_Init] Use Preset Idx [0]
  [DRV_ISP_Open][0] oooooooooooooooooooo >>>>>>>>>>
  [DRV_ISP_Open] Dev ID = 0 Hal=0xc0e7ce00
  [DRV_ISP_PROXY_Isp0Probe] Dev=0, pHnd=0xbfc37348
  [ISP] Request IRQ Num: 84
  [LIBCAMERA_IspMidEarlyInit] ==================== >>>>>>>>>>
  module [isp] init
  module [scl] init
  module [pspi] init
  module [vdisp] init
  module [ipu] init
  CmdqProcInit 1178
  mi sys debug init success
  MI_SYS_Dump_Common_Info_Init is success
  mi sensor debug init success
  mi vif debug init success
  mi RGN debug init success
  mi disp debug init success
  mi wbc debug init success
  mi pspi debug init success
  mi GFX debug init success
  mi scl debug init success
  mi isp debug init success
  mi FB debug init success
  mi vdisp debug init success
  mi ipu debug init success
  module [debug] init
  pad 0 register
  pad 2 register
  Gadget configfs UDC:1f284200.msb250x-udc-p0
  /customer/ssh/sbin/sshd: can't load library 'libfts.so.0'
  / # 


adb连接登陆
~~~~~~~~~~~~~

.. code:: shell

  #需要TYPEC线供电
  #打开win10电脑的cmd输入终端
  #输入adb shell和ls,如下：
  adb shell
  / # ls
  bin
  busybox-1.20.2-arm-buildroot-linux-uclibcgnueabihf-uclibc-12.4.0-dynamic.tar.gz
  config
  customer
  dev
  etc
  home
  lib
  linuxrc
  misc
  mnt
  proc
  run
  sbin
  sys
  tmp
  usr
  var
  / #
  #可以看到文件，说明已经登录完成

网线telnetd登录
~~~~~~~~~~~~~~~~~

.. code:: shell

  #需要插上网线和配置IP地址，以及telnetd(我的电脑IP地址为192.168.137.99)
  $ ifconfig eth0 192.168.137.81
  $ telnetd

  #可以串口软件登陆，如
  #点击串口file->New
  #设置Protocol选择TELNET
  #host设置为192.168.137.81
  #点击Connect连接
  #用户名是root，没有密码，直接敲回车登陆，如下
  login: can\'t chdir to home directory '/home/root'
  / # ls
  bin
  busybox-1.20.2-arm-buildroot-linux-uclibcgnueabihf-uclibc-12.4.0-dynamic.tar.gz
  config
  customer
  dev
  etc
  home
  lib
  linuxrc
  misc
  mnt
  proc
  run
  sbin
  sys
  tmp
  usr
  var
  / #