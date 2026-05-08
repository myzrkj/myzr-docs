Quick Start
=============

Preparations
--------------

| Development Board: 1 piece
| Type-C Data Cable: 1 piece
| TTL Serial Module: 1 piece
| Dupont Jumper Wires: Several
| Network Cable: 1 piece
| Power Adapter: 12V power adapter × 1

Serial Port Software Settings
--------------------------------

| Baud Rate: 115200
| Data Bit: 8bit
| Stop Bit: 1bit
| Parity Bit: none

DIP Switch Settings and TTL Serial Module
--------------------------------------------

DIP Switch Settings
~~~~~~~~~~~~~~~~~~~~~

.. image:: /image/MYZR-SigmaStar系列/MYZR-SSD2355-EK199/烧录手册2.png
   :alt: 烧录手册2.png
   :width: 60%

TTL Serial Module Wiring
~~~~~~~~~~~~~~~~~~~~~~~~~~

| Label: DEBUG
| Connect the computer and development board with a Type-C data cable

Serial Port Boot
------------------

.. code-block:: shell

  IPL 3e3be49
  D-7f
  CPU=1000MHz
  HEAP: [0xa0018340~0xa0018440]
  SHM: [0xa0013840~0xa0018340]
  HW Reset
  RECORD: tc at 0xa0013900
  SPI 104M
  [SPINAND] RFC use command 0x6b
  [SPINAND] dummy clock 0x8
  [SPINAND] Program with command 0x32.
  [SPINAND] Random with command 0x34.
  [FLASH] BDMA mode.
  Loading Environment from SPIFlash... 
  OK
  BGA2 NTC8G DDR4 3200
  miu pll: 432MHz
  DRAM Size: 1024MB
  ddr ott finish
  HEAP: [0x23d00000~0x23e00000]
  SHM: [0x22440000~0x23d00000 0x7dbd3840]
  IMG_LOAD@ devs:0xa img:CUST bak:0 ofs:0x0 sz:0x580 dst:0x23d00000
  IMG_LOAD@ devs:0xa img:CUST bak:0 ofs:0x0 sz:0x7c20 dst:0x22400000
  IMG_VERIFY@ type:1
  DECOMP@0 from 0x22400000 to 0x22400000
  Flashing D-Cache and Disabling MMU
  OS_JUMP@ method:1 entry_pointer:0x22400000

  IPL_CUST 3e3be49
  D-7f
  HEAP: [0x23d00000~0x23e00000]
  RECORD: moving tc from 0x224400c0 to 0x263ff000
  SPI 104M
  IMG_LOAD@ devs:0xa img:RISCVFW bak:0 ofs:0x0 sz:0x580 dst:0x23d00000
  IMG_LOAD@ devs:0xa img:RISCVFW bak:0 ofs:0x0 sz:0x62d90 dst:0x267fffc0
  IMG_VERIFY@ type:16
  DECOMP@0 from 0x26800000 to 0x26800000
  IMG_LOAD@ devs:0xa img:TFA bak:0 ofs:0x0 sz:0x580 dst:0x23d00580
  IMG_LOAD@ devs:0xa img:TFA bak:0 ofs:0x0 sz:0xe11e dst:0x263fffc0
  IMG_VERIFY@ type:2
  DECOMP@0 from 0x26400000 to 0x26400000
  IMG_LOAD@ devs:0xa img:UBOOT bak:0 ofs:0x0 sz:0x580 dst:0x23d00b00
  IMG_LOAD@ devs:0xa img:UBOOT bak:0 ofs:0x0 sz:0x68168 dst:0x22444a80
  IMG_VERIFY@ type:4
  DECOMP@2 from 0x22444ac0 to 0x23e00000
  Flashing D-Cache
  OS_JUMP@ method:2 entry_pointer:0x23e00000


  U-Boot 2021.10 (Dec 25 2025 - 10:26:46 +0000)

  SoC: SigmaStar pcupid
  Model: PCUPID
  Version: P###g#######
  DRAM:  128 MiB
  [Padmux]reset PAD51(reg 0x141a00:1a; mask0x8) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD52(reg 0x141a00:1a; mask0x10) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD56(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD58(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD60(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD54(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD55(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD57(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD59(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
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
  Fail to get pad(0x0) ip(0x0_8)  form padmux !
  MSC: 0, MSC: 1
  Loading Environment from NAND... 
  ENV: offset = 0x500000 size = 0x40000
  ENV1: offset = 0x540000 size = 0x40000
  OK
  In:    serial
  Out:   serial
  Err:   serial
  Net:   No ethernet found.
  Hit any key to stop autoboot:  0 
  mipi reset success!
  JPD_SW_decode time: 35240 us
  CACHE: Misaligned operation at range [5f600000, 5f6961e0]
  JPD_SW_decode time: 16360 us
  cost time: 839172 us
  bitwidth = 16
  ## Booting kernel from Legacy Image at 23000000 ...
     Image Name:   MVX4##P###g#######KL_LX601##[BR:
     Image Type:   AArch64 Linux Kernel Image (lzma compressed)
     Data Size:    3714700 Bytes = 3.5 MiB
     Load Address: 20200000
     Entry Point:  20200000
     Verifying Checksum ... OK
     Uncompressing Kernel Image
  [XZ] !!!reserved 0x22000000 length=0x 1000000 for xz!!
     XZ: uncompressed size=0xbd2200, ret=7
  Info: kernel address offset 0xfe0000000

  Starting kernel ...

  Booting Linux on physical CPU 0x0000000000 [0x411fd040]
  Linux version 6.1.111-rt42 (surs@myzr-u2004) (aarch64-unknown-linux-gnu-12.4.0-gcc (crosstool-NG 1.26.0) 12.4.0, GNU ld (crosstool-NG 1.26.0) 2.40) #316 SMP PREEMPT Thu Dec 25 10:27:52 UTC 2025
  early_atags_to_fdt() success
  Machine model: PCUPID
  LX_MEM addr:0x1000000000,size:0x40000000
  LXmem is 0x40000000 PHYS_OFFSET is 0x1000000000
  Add mem start 0x1000000000 size 0x40000000!!!!

  LX_MEM  = 0x1000000000, 0x40000000
  LX_MEM2 = 0x0, 0x0
  LX_MEM3 = 0x0, 0x0
  MMU_MEM = 0x0, 0x0
  EMAC_LEN= 0x0
  DRAM_LEN= 0x0
  efi: UEFI not found.
  OF: reserved mem: invalid size property in 'cma0' node.
  deal_with_reserved_mmap memblock_reserve success mmap_reserved_config[0].reserved_start=
  0x103f600000

  deal_with_reserve_mma_heap memblock_reserve success mma_config[0].reserved_start=
  0x102f600000 size:10000000

  deal_with_reserve_mma_heap memblock_reserve success mma_config[1].reserved_start=
  0x102d910000 size:1cf0000

  Zone ranges:
    DMA      [mem 0x0000001000000000-0x000000103fffffff]
    DMA32    empty
    Normal   empty
  Movable zone start for each node
  Early memory node ranges
    node   0: [mem 0x0000001000000000-0x000000102d90ffff]
    node   0: [mem 0x000000103f600000-0x000000103fffffff]
  Initmem setup node 0 [mem 0x0000001000000000-0x000000103fffffff]
  On node 0, zone DMA: 40176 pages in unavailable ranges
  cma: Reserved 4 MiB at 0x0000001001000000
  psci: probing for conduit method from DT.
  psci: PSCIv1.1 detected in firmware.
  psci: Using standard PSCI v0.2 function IDs
  psci: MIGRATE_INFO_TYPE not supported.
  psci: SMC Calling Convention v1.2
  percpu: Embedded 17 pages/cpu s32440 r8192 d29000 u69632
  Detected VIPT I-cache on CPU0
  CPU features: detected: GIC system register CPU interface
  alternatives: applying boot alternatives
  Built 1 zonelists, mobility grouping on.  Total pages: 186243
  Kernel command line: ubi.mtd=ubia,2048 root=/dev/mtdblock8 rootfstype=squashfs ro init=/linuxrc pstore_blk.blkdev=PSTORE LX_MEM=0x1000000000,0x40000000 mma_heap=mma_heap_name0,miu=0,sz=0x10000000 mma_memblock_remove=1 cma=2M mma_heap=mma_heap_fb,miu=0,sz=0x1CF0000 mmap_reserved=fb,miu=0,sz=0x800000,max_start_off=0x3f600000,max_end_off=0x3fe00000 mtdparts=nand0:1920k@1280k(BOOT),1920k(BOOT_BAK),256k(ENV),256k(ENV1),384k(DDRTRAIN),5m(KERNEL),5m(RECOVERY),512k(RISCVFW),6m(rootfs),768k(vendor_storage),1m(MISC),1m(PSTORE),105344k(ubia)
  Dentry cache hash table entries: 131072 (order: 8, 1048576 bytes, linear)
  Inode-cache hash table entries: 65536 (order: 7, 524288 bytes, linear)
  mem auto-init: stack:off, heap alloc:off, heap free:off
  Memory: 711552K/756800K available (6784K kernel code, 840K rwdata, 2668K rodata, 1664K init, 310K bss, 41152K reserved, 4096K cma-reserved)
  SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
  rcu: Preemptible hierarchical RCU implementation.
  rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
  NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
  GICv3: GIC: Using split EOI/Deactivate mode
  GICv3: 192 SPIs implemented
  GICv3: 0 Extended SPIs implemented
  Root IRQ handler: gic_handle_irq
  GICv3: GICv3 features: 16 PPIs
  GICv3: CPU0: found redistributor 0 region 0:0x0000000016080000
  sstar_main_intc_init: np->name=sstar_main_intc, parent=gic
  sstar_gpi_intc_init: np->name=sstar_gpi_intc, parent=sstar_main_intc
  sstar_pm_gpi_intc_init: np->name=sstar_pm_gpi_intc, parent=sstar_main_intc
  rcu: srcu_init: Setting srcu_struct sizes based on contention.
  [hal_clk_ipupll_init] ipupll already init, skip
  arch_timer: cp15 timer(s) running at 6.00MHz (phys).
  clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x1623fa770, max_idle_ns: 440795202238 ns
  sched_clock: 56 bits at 6MHz, resolution 166ns, wraps every 4398046511055ns
  printk: console [ttyS0] enabled
  Calibrating delay loop (skipped), value calculated using timer frequency.. 12.00 BogoMIPS (lpj=24000)
  pid_max: default: 4096 minimum: 301
  Mount-cache hash table entries: 2048 (order: 2, 16384 bytes, linear)
  Mountpoint-cache hash table entries: 2048 (order: 2, 16384 bytes, linear)
  cacheinfo: Unable to detect cache hierarchy for CPU 0
  rcu: Hierarchical SRCU implementation.
  rcu:         Max phase no-delay instances is 1000.
  printk: console [ttyS0] printing thread started
  EFI services will not be available.
  smp: Bringing up secondary CPUs ...
  Detected VIPT I-cache on CPU1
  cacheinfo: Unable to detect cache hierarchy for CPU 1
  GICv3: CPU1: found redistributor 1 region 0:0x00000000160a0000
  CPU1: Booted secondary processor 0x0000000001 [0x411fd040]
  Detected VIPT I-cache on CPU2
  cacheinfo: Unable to detect cache hierarchy for CPU 2
  GICv3: CPU2: found redistributor 2 region 0:0x00000000160c0000
  CPU2: Booted secondary processor 0x0000000002 [0x411fd040]
  Detected VIPT I-cache on CPU3
  cacheinfo: Unable to detect cache hierarchy for CPU 3
  GICv3: CPU3: found redistributor 3 region 0:0x00000000160e0000
  CPU3: Booted secondary processor 0x0000000003 [0x411fd040]
  smp: Brought up 1 node, 4 CPUs
  SMP: Total of 4 processors activated.
  CPU features: detected: 32-bit EL0 Support
  CPU features: detected: CRC32 instructions
  CPU: All CPU(s) started at EL2
  alternatives: applying system-wide alternatives
  devtmpfs: initialized
  clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
  futex hash table entries: 16 (order: -2, 1024 bytes, linear)
  pinctrl core: initialized pinctrl subsystem
  DMI not present or invalid.
  NET: Registered PF_NETLINK/PF_ROUTE protocol family
  DMA: preallocated 128 KiB GFP_KERNEL pool for atomic allocations
  DMA: preallocated 128 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
  DMA: preallocated 128 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
  rpmsg_dualos init success!
  hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
  ASID allocator initialised with 65536 entries
  platform soc: Fixed dependency cycle(s) with /soc/sstar_main_intc
  GPIO: probe end
  [Padmux]reset PAD51(reg 0x141a00:1a; mask0x8) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD52(reg 0x141a00:1a; mask0x10) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD56(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD58(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD60(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD54(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD55(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD57(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD59(reg 0x141a00:1a; mask0x20) t0 ETH1_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD96(reg 0x153400:5c; mask0x1) t0 MIPI_TX_MODE_3 (org: OUTP_CH0_IE_CLR_MODE_0)
  [Padmux]reset PAD97(reg 0x153400:5c; mask0x100) t0 MIPI_TX_MODE_3 (org: OUTN_CH0_IE_CLR_MODE_0)
  [Padmux]reset PAD98(reg 0x153400:5c; mask0x2) t0 MIPI_TX_MODE_3 (org: OUTP_CH1_IE_CLR_MODE_0)
  [Padmux]reset PAD99(reg 0x153400:5c; mask0x200) t0 MIPI_TX_MODE_3 (org: OUTN_CH1_IE_CLR_MODE_0)
  [Padmux]reset PAD100(reg 0x153400:5c; mask0x4) t0 MIPI_TX_MODE_3 (org: OUTP_CH2_IE_CLR_MODE_0)
  [Padmux]reset PAD101(reg 0x153400:5c; mask0x400) t0 MIPI_TX_MODE_3 (org: OUTN_CH2_IE_CLR_MODE_0)
  SCSI subsystem initialized
  usbcore: registered new interface driver usbfs
  usbcore: registered new interface driver hub
  usbcore: registered new device driver usb
  pps_core: LinuxPPS API ver. 1 registered
  pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
  PTP clock support registered
  icp_i2c_init 243 ret = 0

  [MIU ERR] [sstar_miu_clk_register@541] [sstar_miu_clk_register] clk_miu enable 0
  [hal_clk_mtcmos_isp_enable] clk_mtcmos_isp already enabled!
  Do qos-initialize
  Advanced Linux Sound Architecture Driver Initialized.
  clocksource: Switched to clocksource arch_sys_counter
  NET: Registered PF_INET protocol family
  IP idents hash table entries: 16384 (order: 5, 131072 bytes, linear)
  tcp_listen_portaddr_hash hash table entries: 512 (order: 2, 16384 bytes, linear)
  Table-perturb hash table entries: 65536 (order: 6, 262144 bytes, linear)
  TCP established hash table entries: 8192 (order: 4, 65536 bytes, linear)
  TCP bind hash table entries: 8192 (order: 7, 524288 bytes, linear)
  TCP: Hash tables configured (established 8192 bind 8192)
  UDP hash table entries: 512 (order: 3, 49152 bytes, linear)
  UDP-Lite hash table entries: 512 (order: 3, 49152 bytes, linear)
  NET: Registered PF_UNIX/PF_LOCAL protocol family
  RPC: Registered named UNIX socket transport module.
  RPC: Registered udp transport module.
  RPC: Registered tcp transport module.
  RPC: Registered tcp NFSv4.1 backchannel transport module.
  armv8-pmu soc:pmu: hw perfevents: no interrupt-affinity property, guessing.
  hw perfevents: enabled with armv8_cortex_a35 PMU driver, 7 counters available
  Initialise system trusted keyrings
  workingset: timestamp_bits=62 max_order=18 bucket_order=0
  squashfs: version 4.0 (2009/01/31) Phillip Lougher
  jffs2: version 2.2. © 2001-2006 Red Hat, Inc.
  fuse: init (API version 7.38)
  Key type asymmetric registered
  Asymmetric key parser 'x509' registered
  io scheduler mq-deadline registered
  io scheduler kyber registered


  Version : MVX4##P###g#######KL_LX601##[BR:g]#XVM

  cacheinfo: Unable to detect cache hierarchy for CPU 0
  usbcore: registered new interface driver cdc_acm
  cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
  mousedev: PS/2 mouse device common for all mice
  i2c_dev: i2c /dev entries driver
  IR NEC protocol handler initialized
  SMCCC: SOC_ID: ID = jep106:0000:8192 Revision = 0x00000000
  failed to get uart clk_mcu
  address of rpmsg share area:0x26876000,0x10076000,12288
  random: crng init done
  alloc buffers: va 0xffffffc009300000, pa 0x269c0000, size=0x40000
  virtio_rpmsg_bus virtio0: rpmsg host is online
  rpmsg_ns_cb, name:rpmsg_dualos, addr:0x2000030
  virtio_rpmsg_bus virtio0: creating channel rpmsg_dualos addr 0x2000030
  rpmsg_dualos_probe: add new channel(type=6,dev_id=0)
  sstar riscv driver is registered
  [Dev_EMAC_PHYHW_reset] EMAC1 PHY RESET, gpio_no = 53
  mdio_bus mdio-bus@emac0: ethernet-phy@0 has invalid PHY address
  mdio_bus mdio-bus@emac0: scan phy ethernet-phy at address 0
  mdio_bus mdio-bus@emac0: scan phy ethernet-phy at address 1
  [emac_phy_connect][3011] connected mac emac0 to PHY at mdio-bus@emac0:01 [uid=02430c54, driver=Generic PHY]
  [Dev_EMAC_PHYHW_reset] EMAC1 PHY RESET, gpio_no = 53
  mdio_bus mdio-bus@emac1: ethernet-phy@1 has invalid PHY address
  mdio_bus mdio-bus@emac1: scan phy ethernet-phy at address 0
  mdio_bus mdio-bus@emac1: scan phy ethernet-phy at address 1
  [emac_phy_connect][3011] connected mac emac1 to PHY at mdio-bus@emac1:01 [uid=02430c54, driver=Generic PHY]
  Registered IR keymap sstar-ir0-map
  rc rc0: sstar-input-ir0 as /devices/virtual/rc/rc0
  input: sstar-input-ir0 as /devices/virtual/rc/rc0/input0
  Registered IR keymap sstar-ir1-map
  rc rc1: sstar-input-ir1 as /devices/virtual/rc/rc1
  input: sstar-input-ir1 as /devices/virtual/rc/rc1/input1
  Registered IR keymap sstar-ir2-map
  rc rc2: sstar-input-ir2 as /devices/virtual/rc/rc2
  input: sstar-input-ir2 as /devices/virtual/rc/rc2/input2
  Registered IR keymap sstar-ir3-map
  rc rc3: sstar-input-ir3 as /devices/virtual/rc/rc3
  input: sstar-input-ir3 as /devices/virtual/rc/rc3/input3
  Registered IR keymap sstar-ir4-map
  rc rc4: sstar-input-ir4 as /devices/virtual/rc/rc4
  input: sstar-input-ir4 as /devices/virtual/rc/rc4/input4
  [Padmux]reset PAD70(reg 0x103e00:46; mask0x8) t0 I2C0_MODE_4 (org: GPIO_MODE)
  [Padmux]reset PAD71(reg 0x103e00:47; mask0x8) t0 I2C0_MODE_4 (org: GPIO_MODE)
  [Padmux]reset PAD66(reg 0x103e00:42; mask0x8) t0 I2C1_MODE_3 (org: GPIO_MODE)
  [Padmux]reset PAD67(reg 0x103e00:43; mask0x8) t0 I2C1_MODE_3 (org: GPIO_MODE)
  [Padmux]reset PAD18(reg 0x103e00:12; mask0x8) t0 I2C2_MODE_3 (org: GPIO_MODE)
  [Padmux]reset PAD19(reg 0x103e00:13; mask0x8) t0 I2C2_MODE_3 (org: GPIO_MODE)
  [Padmux]reset PAD64(reg 0x103e00:40; mask0x8) t0 I2C3_MODE_3 (org: GPIO_MODE)
  [Padmux]reset PAD65(reg 0x103e00:41; mask0x8) t0 I2C3_MODE_3 (org: GPIO_MODE)
  [Padmux]reset PAD123(reg 0x103e00:7b; mask0x8) t0 I2C4_MODE_1 (org: GPIO_MODE)
  [Padmux]reset PAD124(reg 0x103e00:7c; mask0x8) t0 I2C4_MODE_1 (org: GPIO_MODE)
  cryptodev: driver 1.10(a1e738a) loaded.
  ........................................
  ........................................
  / #
  / # ls
  bin       dev       lib       misc      run       tmp
  config    etc       lib64     mnt       sbin      usr
  customer  home      linuxrc   proc      sys       var

Network Cable Telnetd Login
-----------------------------

.. code-block:: shell

  # Connect the network cable and obtain IP address first
  /customer/ssh/etc # ifconfig eth1 down
  fconfig eth0 up
  udhcpc -i eth0 -s /etc/init.d/udhcpc.script
  ping baidu/customer/ssh/etc # ifconfig eth0 up
  3
  [emac_phy_link_adjust] EMAC Link Down 
  /customer/ssh/etc # udhcpc -i eth0 -s /etc/init.d/udhcpc.script
  udhcpc (v1.20.2) started
  Setting IP address 0.0.0.0 on eth0
  Sending discover...
  [emac_phy_link_adjust] EMAC Link Up 
  Sending discover...
  Sending select for 192.168.128.140...
  Lease of 192.168.128.140 obtained, lease time 300
  Setting IP address 192.168.128.140 on eth0
  Deleting routers
  route: SIOCDELRT: No such process
  Adding router 192.168.128.1
  Recreating /customer/resolv.conf
   Adding DNS server 192.168.128.1
  mount: mounting /customer/resolv.conf on /etc/resolv.conf failed: No such file or directory
  /customer/ssh/etc # ping baidu.com -c 3
  PING baidu.com (124.237.177.164): 56 data bytes
  64 bytes from 124.237.177.164: seq=0 ttl=53 time=36.546 ms
  64 bytes from 124.237.177.164: seq=1 ttl=53 time=36.160 ms
  64 bytes from 124.237.177.164: seq=2 ttl=53 time=36.075 ms

  --- baidu.com ping statistics ---
  3 packets transmitted, 3 packets received, 0% packet loss


  Connecting to 192.168.128.140:22...
  Connection established.
  To escape to local shell, press 'Ctrl+Alt+]'.
  # Username: root, no password, press Enter directly to log in as follows
  WARNING! The remote SSH server rejected X11 forwarding request.
  Could not chdir to home directory /home/root: No such file or directory
  / # 
  / # 
  / # 
  / # ls
  bin       config    customer  dev       etc       home      lib       lib64     linuxrc   misc      mnt       proc      run       sbin      sys       tmp       usr       va
