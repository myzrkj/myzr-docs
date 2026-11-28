.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>

Startup Manual
================

Development Board Connection
------------------------------

Check the Power Switch
~~~~~~~~~~~~~~~~~~~~~~~~

|   Toggle the power switch "SW1" of the development board to the side with letters to ensure the power switch of the development board is in the **off** state.

Serial Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Connect one end of the Type-C cable to the "CON5" port of the development board, and the other end to the serial port of the computer.
2. Refer to the *Xshell Reference Manual* to create a new serial session and open the session.

Ethernet Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the Ethernet cable to "CON15" or "CON16", and the other end to the Ethernet port of the computer.

Download Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the Type-C cable to CON12, and the other end to the rear USB port of the computer.

Power Cable Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the power adapter to "CON3" of the development board, and the other end to a mains power (220V AC) socket.

HDMI Display Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

|   Connect one end of the HDMI display cable to CON22 of the development board, and the other end to the HDMI display. Then power on the HDMI display.
|   **Note**: It is recommended that the HDMI display uses a resolution of 1080P and is a display with a native HDMI interface (not a display converted to an HDMI interface).


Power On the Development Board
---------------------------------

Power On the Development Board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Toggle the power switch SW1 of the development board to the side with English letters to turn on the development board.

Interpretation of Development Board Startup Information
----------------------------------------------------------

|   After the development board is powered on, the startup information output by the development board can be viewed on the serial terminal software.

.. code-block:: shell

    [146]HELLO! BOOT0 is starting!
    [149]BOOT0 commit : 5e112d72ef
    [153][pmu]: bus read error
    [156]PMU: AXP2202
    [158]combi:0x1, cpu_vol:920
    [161][pmu]: bus read error
    [165]axp_id:2, sys_vol:940
    [168]set pll start
    [170]set pll end
    [172]vaild para:1  select dram para0
    [175]board init ok
    [177]enable_jtag
    [179]card no is 2
    [181]sdcard 2 line count 8
    [183][mmc]: mmc driver ver 2024-11-12 20:45
    [190][mmc]: need set skew
    [196][mmc]: Wrong media type 0x0, but host sdc2, try mmc first
    [202][mmc]: ***Try MMC card 2***
    [226][mmc]: RMCA OK!
    [228][mmc]: need set skew
    [234][mmc]: need set skew
    [236][mmc]: need set skew
    [239][mmc]: MMC 5.1
    [241][mmc]: HSSDR52/SDR25 8 bit
    [244][mmc]: 50000000 Hz
    [246][mmc]: 14930 MB
    [248][mmc]: ***SD/MMC 2 init OK!!!***
    [254]DRAM BOOT DRIVE INFO: V0.40
    [257]VCC_DRAM set to 1100 mv
    [260]DRAM CLK =1200 MHZ
    [263]DRAM Type =8 (3:DDR3,4:DDR4,7:LPDDR3,8:LPDDR4)
    [272]DRAM SIZE =2048 MBytes, para1 = 310a, para2 = 8000000, tpr13 = 6461
    [284]DRAM simple test OK.
    [287]dram size = 2048
    [380]Loading boot-pkg Succeed(index=0).
    [384]Entry_name        = u-boot
    [395]Entry_name        = monitor
    [399]Entry_name        = scp
    [402]error: dtb not found for scp
    [406]tunning data addr:0x4a0003e8
    [409]Jump to ATF: monitor_base = 0x48000000, uboot_base = 0x4a000000, optee_base = 0x0
    NOTICE:  BL31: OP-TEE 32bit detected
    NOTICE:  BL31: U-BOOT 32bit detected
    NOTICE:  BL31: v2.5(debug):93418067d
    NOTICE:  BL31: Built : 15:24:39, Dec  4 2024
    NOTICE:  BL31: No DTB found.
    ERROR:   Error initializing runtime service opteed_fast
    [00.586]ns16550_serial serial@0x02600000L: pinctrl_select_state_full: uclass_get_device_by_phandle_id: err=-19
    
    
    U-Boot 2023.04-rc4 (Nov 24 2026 - 04:04:18 +0000) Allwinner Technology
    U-Boot bsp (Nov 24 2026 - 04:04:18 +0000) Allwinner Technology
    
    14/40 CPU:   SUNXI Family
    Model: myzr-t536-bl270
    DRAM:  2 GiB
    [00.615]Relocation Offset is: 71d92000
    [00.695]set_sunxi_flash_curdev...65:cur_sunxi_flash :mmc@0x04022000L.sunxi_flash
    [00.703][mmc]: mmc driver ver uboot2023:2024-11-15 16:03:00
    [00.709][mmc]: get sdc_type fail and use default host:tm4.
    [00.715][mmc]: SUNXI SDMMC Controller Version:0x50520
    [00.723][mmc]: 200 MHz...
    [00.725][mmc]: sample: 15 - 166(ps)
    [00.728][mmc]: ds: 15 - 166(ps)
    Working FDT set to b7d89350
    [00.736]secure enable bit: 0
    [00.740][AXP2202] comm status : 0x0 = 0x20, 0x1 = 0x90
    [00.745][AXP2202] onoff status : 0x20 = 0x4, 0x21 = 0x0
    [00.750][[AXP2202] reboot/charge status: 0xf0 = 0x0
    [00.755][[AXP2202] reboot/charge status: 0x17 = 0x1c
    [00.760]no axp start up debug function
    [00.763]no axp start up debug function
    [00.768]axp2202_dcdc1_mode = 1[now:1]
    [00.773]axp2202_dcdc2_mode = 1[now:1]
    [00.777]axp2202_dcdc3_mode = 1[now:1]
    [00.783]axp2202_aldo1_vol = 1800[now:1800], onoff=1[now:1]
    [00.791]axp2202_bldo1_vol = 1800[now:1800], onoff=0[now:0]
    [00.798]axp2202_bldo2_vol = 1800[now:1800], onoff=1[now:1]
    [00.805]axp2202_cldo4_vol = 3300[now:3300], onoff=1[now:1]
    [00.810]workmode = 0,storage type = emmc
    SUNXI SD/MMC: 0
    [00.816]sunxi_rproc e907_rproc@1a00000: version: 1.0.0
    Core:  151 devices, 30 uclasses, devicetree: separate
    WDT:   Not starting watchdog@0x02050000L
    MMC:   Loading Environment from SUNXI_FLASH... [00.840][mmc]: mmc 2 cmd timeout 100 status 100
    [00.844][mmc]: smc 2 err, cmd 8,  RTO
    [00.847][mmc]: mmc 2 close bus gating and reset
    [00.852][mmc]: mmc 2 cmd timeout 100 status 100
    [00.857][mmc]: smc 2 err, cmd 55,  RTO
    [00.860][mmc]: mmc 2 close bus gating and reset
    [00.883][mmc]: Best spd md: 4-HS400, freq: 4-150000000, Bus width: 8
    OK
    In:    serial
    Out:   serial
    Err:   serial
    gic: sec monitor mode
    [00.900]skip update boot_param
    [00.903]update bootcmd
    Net:   
    Warning: ethernet@4500000 (eth0) using random MAC address - 7a:e3:a4:85:06:05
    eth0: ethernet@4500000
    Warning: ethernet@4510000 (eth1) using random MAC address - ee:6b:8b:6c:f2:a1
    , eth1: ethernet@4510000
    [00.935]Item0 (Map) magic is bad
    [00.938]the secure storage item0 copy0 magic is bad
    [00.943]Item0 (Map) magic is bad
    [00.945]the secure storage item0 copy1 magic is bad
    [00.950]Item0 (Map) magic is bad
    List file under ULI/factory
    [00.956]root_partition is rootfs
    [00.959]set root to /dev/mmcblk0p5
    [00.962]update part info
    [00.970]Fail to get reset clk for rst_bus_de_sys
    [00.974]Fail to get de's irq!
    [00.976]sunxi_de_get_disp_sys:Get top phandle fail!
    [00.993]panel_dsi dsi0@5506000.0: failed to request regulator(power2-supply): -2
    [01.000]panel_dsi dsi0@5506000.0: failed to request enable1-gpios GPIO: -2
    [01.007]panel_dsi dsi0@5506000.0: failed to request enable2-gpios GPIO: -2
    [01.013]panel_dsi_probe: Cannot get backlight: -2
    [01.019]Using display timing dts
    dsi0@5506000:  detailed mode clock 33823 kHz, flags[5]
        H: 0480 0520 0524 0564
        V: 0854 0976 0978 0990
    bus_format: 0
    1229814 bytes read in 5 ms (234.6 MiB/s)
    [01.046]irq no:123
    [lowlevel] x:480, y:854, vt:990, vbp:12, vspw:2, ht:564, hbp:40, hspw:4
    Working FDT set to 42000000
    [01.157]change working_fdt 0xb7d89350 to 0x42000000
    ret 0
    [01.182]update dts
    delay time 0
    Hit any key to stop autoboot:  0 
    ## Booting Android Image at 0x4007f800 ...
    Android's image name: sun55i_arm64
    Kernel load addr 0x40080000 size 26901 KiB
    ## Flattened Device Tree blob at 42000000
       Booting using the fdt blob at 0x42000000
    Working FDT set to 42000000
       XIP Kernel Image
       Using Device Tree in place at 42000000, end 42042fff
    Working FDT set to 42000000
    [01.692]Starting kernel ...
    
    NOTICE:  [SCP] :wait arisc ready....
    NOTICE:  [SCP] :arisc version: []
    NOTICE:  [SCP] :arisc startup ready
    NOTICE:  [SCP] :arisc startup notify message feedback
    NOTICE:  [SCP] :sunxi-arisc driver is starting
    NOTICE:  BL3-1: Next image address = 0x40080000
    NOTICE:  BL3-1: Next image spsr = 0x3c5
    [    0.000000] Booting Linux on physical CPU 0x0000000000 [0x412fd050]
    [    0.000000] Linux version 5.10.198 (linyn@myzr-u2204) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #23 SMP PREEMPT Wed Nov 25 11:07:31 UTC 2026
    [    0.000000] Machine model: TLT536-EVM HDMI
    [    0.000000] printk: bootconsole [earlycon0] enabled
    [    0.000000] [Firmware Bug]: Kernel image misaligned at boot, please fix your bootloader!
    [    0.000000] Reserved memory: created DMA memory pool at 0x0000000042380000, size 0 MiB
    [    0.000000] OF: reserved mem: initialized node e907_rpbuf@42380000, compatible id shared-dma-pool
    [    0.000000] Reserved memory: created DMA memory pool at 0x0000000042400000, size 0 MiB
    [    0.000000] OF: reserved mem: initialized node vdev0buffer@42400000, compatible id shared-dma-pool
    [    0.000000] Reserved memory: created DMA memory pool at 0x0000000042444000, size 0 MiB
    [    0.000000] OF: reserved mem: initialized node vdev0buffer@42444000, compatible id shared-dma-pool
    [    0.000000] Zone ranges:
    [    0.000000]   DMA      [mem 0x0000000040000000-0x00000000bfffffff]
    [    0.000000]   DMA32    empty
    [    0.000000]   Normal   empty
    [    0.000000] Movable zone start for each node
    [    0.000000] Early memory node ranges
    [    0.000000]   node   0: [mem 0x0000000040000000-0x000000004237ffff]
    [    0.000000]   node   0: [mem 0x0000000042380000-0x0000000042488fff]
    [    0.000000]   node   0: [mem 0x0000000042489000-0x0000000048ffffff]
    [    0.000000]   node   0: [mem 0x0000000049000000-0x00000000499fffff]
    [    0.000000]   node   0: [mem 0x0000000049a00000-0x000000005fffffff]
    [    0.000000]   node   0: [mem 0x0000000060000000-0x00000000600fffff]
    [    0.000000]   node   0: [mem 0x0000000060100000-0x00000000bfffffff]
    [    0.000000] Initmem setup node 0 [mem 0x0000000040000000-0x00000000bfffffff]
    [    0.000000] On node 0 totalpages: 524288
    [    0.000000]   DMA zone: 8192 pages used for memmap
    [    0.000000]   DMA zone: 0 pages reserved
    [    0.000000]   DMA zone: 524288 pages, LIFO batch:63
    [    0.000000] psci: probing for conduit method from DT.
    [    0.000000] psci: PSCIv1.1 detected in firmware.
    [    0.000000] psci: Using standard PSCI v0.2 function IDs
    [    0.000000] psci: MIGRATE_INFO_TYPE not supported.
    [    0.000000] psci: SMC Calling Convention v1.2
    [    0.000000] percpu: Embedded 21 pages/cpu s48216 r8192 d29608 u86016
    [    0.000000] pcpu-alloc: s48216 r8192 d29608 u86016 alloc=21*4096
    [    0.000000] pcpu-alloc: [0] 0 [0] 1 [0] 2 [0] 3 
    [    0.000000] Detected VIPT I-cache on CPU0
    [    0.000000] CPU features: detected: GIC system register CPU interface
    [    0.000000] CPU features: kernel page table isolation forced ON by KASLR
    [    0.000000] CPU features: detected: Kernel page table isolation (KPTI)
    [    0.000000] CPU features: detected: ARM errata 1165522, 1319367, or 1530923
    [    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 516096
    [    0.000000] Kernel command line: earlyprintk=sunxi-uart,0x02600000 initcall_debug=0 console=ttyAS0,115200 loglevel=8 root=/dev/mmcblk0p5 rootwait init=/init rdinit=/rdinit partitions=boot-resource@mmcblk0p1:env@mmcblk0p2:boot@mmcblk0p3:private@mmcblk0p4:rootfs@mmcblk0p5:UDISK@mmcblk0p6 cma= snum=3c000c6d570147d1d51 mac_addr= wifi_mac= bt_mac= selinux= specialstr= coherent_pool=16K ion_carveout_list= gpt=1 androidboot.serialno=3c000c6d570147d1d51 androidboot.hardware=sun55iw6p1 boot_type=2 androidboot.boot_type=2 gpt=1 uboot_message=2023.04-rc4 mbr_offset=20971520 androidboot.dramfreq=1200 androidboot.dramsize=2048 
    [    0.000000] Dentry cache hash table entries: 262144 (order: 9, 2097152 bytes, linear)
    [    0.000000] Inode-cache hash table entries: 131072 (order: 8, 1048576 bytes, linear)
    [    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
    [    0.000000] Memory: 1996408K/2097152K available (13246K kernel code, 3028K rwdata, 5492K rodata, 5056K init, 409K bss, 100744K reserved, 0K cma-reserved)
    [    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
    [    0.000000] rcu: Preemptible hierarchical RCU implementation.
    [    0.000000] rcu:         RCU event tracing is enabled.
    [    0.000000]         Trampoline variant of Tasks RCU enabled.
    [    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
    [    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
    [    0.000000] GICv3: 256 SPIs implemented
    [    0.000000] GICv3: 0 Extended SPIs implemented
    [    0.000000] GICv3: Distributor has no Range Selector support
    [    0.000000] GICv3: 16 PPIs implemented
    [    0.000000] GICv3: CPU0: found redistributor 0 region 0:0x0000000003460000
    [    0.000000] ITS: No ITS available, not enabling LPIs
    [    0.000000] sunxi:ccu-ng:[INFO]: sun55iw6 not use npu!
    [    0.000000] AW BSP version: UNKNOWN, 2026-11-25 11:06:27
    [    0.000000] sunxi:ccu-ng:[INFO]: ccu: sunxi ccu init OK
    [    0.000000] sunxi:ccu-ng:[INFO]: sunxi ccu common driver version: 1.2.1
    [    0.000000] sunxi:ccu-ng:[INFO]: sunxi ccu driver version: 0.6.3
    [    0.000000] arch_timer: cp15 timer(s) running at 24.00MHz (virt).
    [    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x588fe9dc0, max_idle_ns: 440795202592 ns
    [    0.000005] sched_clock: 56 bits at 24MHz, resolution 41ns, wraps every 4398046511097ns
    [    0.008254] sunxi:hstimer:[INFO]: sun50i timer init:0xffffff00000002, driver version: 1.1.3
    [    0.016295] clocksource: timer: mask: 0xffffffffffffff max_cycles: 0x1623fa770, max_idle_ns: 440795202238 ns
    [    0.026818] Calibrating delay loop (skipped), value calculated using timer frequency.. 48.00 BogoMIPS (lpj=96000)
    [    0.036324] pid_max: default: 32768 minimum: 301
    [    0.041038] Mount-cache hash table entries: 4096 (order: 3, 32768 bytes, linear)
    [    0.048295] Mountpoint-cache hash table entries: 4096 (order: 3, 32768 bytes, linear)
    [    0.057867] rcu: Hierarchical SRCU implementation.
    [    0.062792] smp: Bringing up secondary CPUs ...
    [    0.066034] Detected VIPT I-cache on CPU1
    [    0.066071] GICv3: CPU1: found redistributor 100 region 0:0x0000000003480000
    [    0.066113] CPU1: Booted secondary processor 0x0000000100 [0x412fd050]
    [    0.066862] Detected VIPT I-cache on CPU2
    [    0.066894] GICv3: CPU2: found redistributor 200 region 0:0x00000000034a0000
    [    0.066931] CPU2: Booted secondary processor 0x0000000200 [0x412fd050]
    [    0.067631] Detected VIPT I-cache on CPU3
    [    0.067658] GICv3: CPU3: found redistributor 300 region 0:0x00000000034c0000
    [    0.067693] CPU3: Booted secondary processor 0x0000000300 [0x412fd050]
    [    0.067821] smp: Brought up 1 node, 4 CPUs
    [    0.121967] SMP: Total of 4 processors activated.
    [    0.126632] CPU features: detected: Privileged Access Never
    [    0.132199] CPU features: detected: LSE atomic instructions
    [    0.137726] CPU features: detected: User Access Override
    [    0.143025] CPU features: detected: 32-bit EL0 Support
    [    0.148124] CPU features: detected: Common not Private translations
    [    0.154381] CPU features: detected: RAS Extension Support
    [    0.159738] CPU features: detected: Data cache clean to the PoU not required for I/D coherence
    [    0.168313] CPU features: detected: CRC32 instructions
    [    0.173425] CPU features: detected: Speculative Store Bypassing Safe (SSBS)
    [    0.207019] CPU: All CPU(s) started at EL1
    [    0.207098] alternatives: patching kernel code
    [    0.211499] devtmpfs: initialized
    [    0.237271] KASLR disabled due to lack of seed
    [    0.237518] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
    [    0.245826] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
    [    0.252774] pinctrl core: initialized pinctrl subsystem
    [    0.258948] NET: Registered protocol family 16
    [    0.262902] DMA: preallocated 16 KiB GFP_KERNEL pool for atomic allocations
    [    0.269233] DMA: preallocated 16 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
    [    0.276842] DMA: preallocated 16 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
    [    0.285017] thermal_sys: Registered thermal governor 'fair_share'
    [    0.285023] thermal_sys: Registered thermal governor 'bang_bang'
    [    0.290698] thermal_sys: Registered thermal governor 'step_wise'
    [    0.296680] thermal_sys: Registered thermal governor 'user_space'
    [    0.302651] thermal_sys: Registered thermal governor 'power_allocator'
    [    0.309469] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
    [    0.322079] ASID allocator initialised with 32768 entries
    [    0.383572] sunxi:ccu-ng:[INFO]: sunxi rtc-ccu version: 0.0.2
    [    0.384563] sunxi:ccu-ng:[INFO]: rtc_ccu: sunxi ccu init OK
    [    0.389727] sunxi:ccu-ng:[INFO]: clock: sunxi ccu init OK
    [    0.394645] sunxi:ccu-ng:[INFO]: sunxi pll_cpu driver version: 0.0.2
    [    0.402617] sunxi:ccu-ng:[INFO]: r_ccu: sunxi ccu init OK
    [    0.406325] sunxi:ccu-ng:[INFO]: sunxi r-ccu driver version: 0.2.8
    [    0.412582] sunxi:pin:[INFO]: sunxi r-pinctrl version: 0.8.3
    [    0.420468] sunxi:pin-7096000.pinctrl:[INFO]: pinctrl withstand voltage config mode=auto_hard
    [    0.426605] sunxi:pin:[INFO]: sunxi pinctrl core driver version: 1.3.7
    [    0.495585] sunxi:pin-7096000.pinctrl:[INFO]: Auto power withstand voltage configuration detected, automatically exit!
    [    0.501236] iommu: Default domain type: Translated 
    [    0.505674] vgaarb: loaded
    [    0.508469] SCSI subsystem initialized
    [    0.512249] usbcore: registered new interface driver usbfs
    [    0.517463] usbcore: registered new interface driver hub
    [    0.522702] usbcore: registered new device driver usb
    [    0.527793] mc: Linux media interface: v0.10
    [    0.531980] videodev: Linux video capture interface: v2.00
    [    0.537863] Advanced Linux Sound Architecture Driver Initialized.
    [    0.548614] sun6i-dma 3001000.dma-controller: sunxi dma probed, driver version: 1.2.8
    [    0.557573] sun6i-dma 4000000.dma-controller: sunxi dma probed, driver version: 1.2.8
    [    0.560347] sunxi iommu: irq = 26
    [    0.566845] Bluetooth: Core ver 2.22
    [    0.566915] NET: Registered protocol family 31
    [    0.571043] Bluetooth: HCI device and connection manager initialized
    [    0.577668] Bluetooth: HCI socket layer initialized
    [    0.582264] Bluetooth: L2CAP socket layer initialized
    [    0.587305] Bluetooth: SCO socket layer initialized
    [    0.593188] sunxi-twi 7083000.twi: supply twi not found, using dummy regulator
    [    0.602494] sunxi:axp2101-7-0036:[ERR]: Unable to match OF ID
    [    0.605079] sunxi:pmu_ext_core-7-0036:[INFO]: pmu_ext_dev variant AXP1530 found
    [    0.612610] sunxi:twi-7083000.twi:[ERR]: drv-mode: Timeout when sending 9th SCL clk
    [    0.619923] sunxi:twi-7083000.twi:[ERR]: drv mode: TWI BUS error state is drv:0x1 eng:0x20
    [    0.628162] sunxi:twi-7083000.twi:[ERR]: drv-mode: xfer failed (dev addr:0x36)
    [    0.635350] axp1530-dcdc1: failed to get the current voltage: -EINVAL
    [    0.641766] sunxi:pmu_ext_regulator-pmu-ext-regulator.0:[ERR]: Failed to register dcdc1
    [    0.649737] pmu-ext-regulator: probe of pmu-ext-regulator.0 failed with error -22
    [    0.668436] sunxi:pmu_ext_core-7-0036:[INFO]: pmu_ext:AXP1530 driver loaded
    [    0.673411] sunxi:axp2101-7-0035:[INFO]: AXP20x variant AXP2202 found
    [    0.681765] axp2202-gpio: Failed to locate of_node [id: 0]
    [    0.682294] axp2202-dcdc1: supplied by regulator-dummy
    [    0.691210] axp2202-dcdc2: supplied by regulator-dummy
    [    0.695209] axp2202-dcdc3: supplied by regulator-dummy
    [    0.703363] axp2202-dcdc4: supplied by regulator-dummy
    [    0.704026] axp2202-aldo1: supplied by regulator-dummy
    [    0.708450] axp2202-aldo2: supplied by regulator-dummy
    [    0.713422] axp2202-aldo3: supplied by regulator-dummy
    [    0.722675] axp2202-aldo4: supplied by regulator-dummy
    [    0.726673] axp2202-bldo1: supplied by regulator-dummy
    [    0.734699] axp2202-bldo2: supplied by regulator-dummy
    [    0.738867] axp2202-bldo3: supplied by regulator-dummy
    [    0.739801] axp2202-bldo4: supplied by regulator-dummy
    [    0.745054] axp2202-cldo1: supplied by regulator-dummy
    [    0.749905] axp2202-cldo2: supplied by regulator-dummy
    [    0.759130] axp2202-cldo3: supplied by regulator-dummy
    [    0.763296] axp2202-cldo4: supplied by regulator-dummy
    [    0.765069] axp2202-rtcldo: supplied by regulator-dummy
    [    0.770576] axp2202-cpusldo: supplied by regulator-dummy
    [    0.776170] axp2202-vmid: supplied by regulator-dummy
    [    0.780867] axp2202-drivevbus: supplied by axp2202-vmid
    [    0.785908] axp2202-bat-power-supply: Failed to locate of_node [id: 0]
    [    0.792216] axp2202-usb-power-supply: Failed to locate of_node [id: 0]
    [    0.798710] gpio-supply: Failed to locate of_node [id: 0]
    [    0.807866] sunxi:axp2101-7-0035:[INFO]: AXP20X driver loaded
    [    0.809888] sunxi:twi-7083000.twi:[INFO]: v2.7.6 probe success
    [    0.816096] sunxi-twi 7084000.twi: supply twi not found, using dummy regulator
    [    0.823500] sunxi:twi-7084000.twi:[INFO]: v2.7.6 probe success
    [    0.829866] sunxi:pwm-2090000.pwm:[INFO]: start probe
    [    0.831374] sunxi:pwm-2090000.pwm:[INFO]: pwmchip probe success
    [    0.839601] sunxi:pwm-2091000.pwm:[INFO]: start probe
    [    0.841074] sunxi:pwm-2091000.pwm:[INFO]: pwmchip probe success
    [    0.850432] sunxi:pwm-2092000.pwm:[INFO]: start probe
    [    0.851852] sunxi:pwm-2092000.pwm:[INFO]: pwmchip probe success
    [    0.861346] sunxi:pwm-7023000.s_pwm:[INFO]: start probe
    [    0.862010] sunxi:pwm-7023000.s_pwm:[INFO]: pwmchip probe success
    [    0.873389] sunxi:lradc-208b000.lradc:[WARN]: get key_debounce failed, please check whether to enable key debounce
    [    0.882895] sunxi:lradc-208b000.lradc:[WARN]: warn: filter_cnt not set, default value is 3
    [    0.891289] input: sunxi-keyboard as /devices/platform/soc@3000000/208b000.lradc/input/input0
    [    0.899783] sunxi:lradc-208b000.lradc:[INFO]: sunxi lradc init success
    [    0.906832] clocksource: Switched to clocksource arch_sys_counter
    [    0.913584] sunxi:pin:[INFO]: sunxi pinctrl version: 0.9.0
    [    0.931636] sunxi:pin-3604000.pinctrl:[INFO]: pinctrl withstand voltage config mode=auto_hard
    [    0.935748] sunxi_usb_udc 4100000.udc-controller: sunxi:sunxi_usb_udc UDC Inner DMA Feature - wordaddr: -1, extend: disabled
    [    0.946362] NET: Registered protocol family 2
    [    0.950268] IP idents hash table entries: 32768 (order: 6, 262144 bytes, linear)
    [    0.958702] tcp_listen_portaddr_hash hash table entries: 1024 (order: 2, 16384 bytes, linear)
    [    0.966026] TCP established hash table entries: 16384 (order: 5, 131072 bytes, linear)
    [    0.973910] TCP bind hash table entries: 16384 (order: 6, 262144 bytes, linear)
    [    0.981300] TCP: Hash tables configured (established 16384 bind 16384)
    [    0.987708] UDP hash table entries: 1024 (order: 3, 32768 bytes, linear)
    [    0.994297] UDP-Lite hash table entries: 1024 (order: 3, 32768 bytes, linear)
    [    1.001519] NET: Registered protocol family 1
    [    1.006299] RPC: Registered named UNIX socket transport module.
    [    1.011612] RPC: Registered udp transport module.
    [    1.016261] RPC: Registered tcp transport module.
    [    1.020936] RPC: Registered tcp NFSv4.1 backchannel transport module.
    [    1.028165] PCI: CLS 0 bytes, default 64
    [    1.032014] sunxi-spi-ng 4026000.spi: supply spi not found, using dummy regulator
    [    1.038937] sunxi:spi-4026000.spi:[INFO]: bus num_1 mode_1 freq_100000000
    [    1.045470] sunxi:spi-4026000.spi:[INFO]: cs num_1 mode_0
    [    1.051696] sunxi:spi-4026000.spi:[INFO]: probe success (Version 2.4.12)
    [    1.184481] hw perfevents: enabled with armv8_pmuv3 PMU driver, 7 counters available
    [    1.188699] Initialise system trusted keyrings
    [    1.191315] workingset: timestamp_bits=46 max_order=19 bucket_order=0
    [    1.203067] squashfs: version 4.0 (2009/01/31) Phillip Lougher
    [    1.204844] Key type cifs.idmap registered
    [    1.207374] ntfs: driver 2.1.32 [Flags: R/O].
    [    1.211962] fuse: init (API version 7.32)
    [    1.259746] Key type asymmetric registered
    [    1.259789] Asymmetric key parser 'x509' registered
    [    1.263117] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 247)
    [    1.270598] io scheduler mq-deadline registered
    [    1.274957] io scheduler kyber registered
    [    1.280135] pwm-backlight backlight0: supply power not found, using dummy regulator
    [    1.291023] reg-virt-consumer reg-virt-consumer.0.auto: DMA mask not set
    [    1.293293] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    1.301773] reg-virt-consumer reg-virt-consumer.1.auto: DMA mask not set
    [    1.308524] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    1.316931] reg-virt-consumer reg-virt-consumer.2.auto: DMA mask not set
    [    1.323665] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    1.332096] reg-virt-consumer reg-virt-consumer.3.auto: DMA mask not set
    [    1.338840] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    1.347255] reg-virt-consumer reg-virt-consumer.4.auto: DMA mask not set
    [    1.353947] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    1.362431] reg-virt-consumer reg-virt-consumer.5.auto: DMA mask not set
    [    1.369450] reg-virt-consumer reg-virt-consumer.6.auto: DMA mask not set
    [    1.376119] reg-virt-consumer reg-virt-consumer.7.auto: DMA mask not set
    [    1.382757] reg-virt-consumer reg-virt-consumer.8.auto: DMA mask not set
    [    1.389414] reg-virt-consumer reg-virt-consumer.9.auto: DMA mask not set
    [    1.396088] reg-virt-consumer reg-virt-consumer.10.auto: DMA mask not set
    [    1.402863] reg-virt-consumer reg-virt-consumer.11.auto: DMA mask not set
    [    1.409621] reg-virt-consumer reg-virt-consumer.12.auto: DMA mask not set
    [    1.416412] reg-virt-consumer reg-virt-consumer.13.auto: DMA mask not set
    [    1.423133] reg-virt-consumer reg-virt-consumer.14.auto: DMA mask not set
    [    1.429885] reg-virt-consumer reg-virt-consumer.15.auto: DMA mask not set
    [    1.436648] reg-virt-consumer reg-virt-consumer.16.auto: DMA mask not set
    [    1.443397] reg-virt-consumer reg-virt-consumer.17.auto: DMA mask not set
    [    1.450177] reg-virt-consumer reg-virt-consumer.18.auto: DMA mask not set
    [    1.456922] reg-virt-consumer reg-virt-consumer.19.auto: DMA mask not set
    [    1.463703] reg-virt-consumer reg-virt-consumer.20.auto: DMA mask not set
    [    1.470445] reg-virt-consumer reg-virt-consumer.21.auto: DMA mask not set
    [    1.477209] reg-virt-consumer reg-virt-consumer.22.auto: DMA mask not set
    [    1.486495] cacheinfo: Unable to detect cache hierarchy for CPU 0
    [    1.491416] CAN device driver interface
    [    1.493576] usbcore: registered new interface driver asix
    [    1.498990] usbcore: registered new interface driver ax88179_178a
    [    1.505014] usbcore: registered new interface driver cdc_ether
    [    1.510809] usbcore: registered new interface driver net1080
    [    1.516438] usbcore: registered new interface driver cdc_subset
    [    1.522328] usbcore: registered new interface driver zaurus
    [    1.527903] usbcore: registered new interface driver cdc_ncm
    [    1.533491] GobiNet: Quectel_Linux&Android_GobiNet_Driver_V1.6
    [    1.539323] usbcore: registered new interface driver GobiNet
    [    1.544951] usbcore: registered new interface driver qmi_wwan
    [    1.551608] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    [    1.557155] ehci-pci: EHCI PCI platform driver
    [    1.561601] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
    [    1.567723] ohci-pci: OHCI PCI platform driver
    [    1.572965] usbcore: registered new interface driver cdc_wdm
    [    1.577997] usbcore: registered new interface driver uas
    [    1.583128] usbcore: registered new interface driver usb-storage
    [    1.589062] usbcore: registered new interface driver ums-alauda
    [    1.594952] usbcore: registered new interface driver ums-cypress
    [    1.600931] usbcore: registered new interface driver ums-datafab
    [    1.606916] usbcore: registered new interface driver ums_eneub6250
    [    1.613069] usbcore: registered new interface driver ums-freecom
    [    1.619058] usbcore: registered new interface driver ums-isd200
    [    1.624945] usbcore: registered new interface driver ums-jumpshot
    [    1.631010] usbcore: registered new interface driver ums-karma
    [    1.636825] usbcore: registered new interface driver ums-realtek
    [    1.642793] usbcore: registered new interface driver ums-sddr09
    [    1.648689] usbcore: registered new interface driver ums-sddr55
    [    1.654579] usbcore: registered new interface driver ums-usbat
    [    1.660444] usbcore: registered new interface driver option
    [    1.665924] usbserial: USB Serial support registered for GSM modem (1-port)
    [    1.673542] sunxi:twi-7084000.twi:[ERR]: drv-mode: Timeout when sending 9th SCL clk
    [    1.680463] sunxi:twi-7084000.twi:[ERR]: drv mode: TWI BUS error state is drv:0x1 eng:0x20
    [    1.688700] sunxi:twi-7084000.twi:[ERR]: drv-mode: xfer failed (dev addr:0x51)
    [    1.695935] rtc-pcf8563 8-0051: pcf8563_write_block_data: err=-22 addr=0e, data=03
    [    1.703431] rtc-pcf8563 8-0051: pcf8563_probe: write error
    [    1.711025] rtc-pcf8563: probe of 8-0051 failed with error -5
    [    1.714645] i2c /dev entries driver
    [    1.718461] usbcore: registered new interface driver uvcvideo
    [    1.723800] USB Video Class driver (1.1.1)
    [    1.728172] device-mapper: ioctl: 4.43.0-ioctl (2020-10-01) initialised: dm-devel@redhat.com
    [    1.736630] Bluetooth: HCI UART driver ver 2.3
    [    1.740710] Bluetooth: HCI UART protocol H4 registered
    [    1.747559] SMCCC: SOC_ID: ARCH_SOC_ID not implemented, skipping ....
    [    1.752378] usbcore: registered new interface driver usbhid
    [    1.757769] usbhid: USB HID core driver
    [    1.763206] sunxi:ccu_ddr:[ERR]: dram_clk:1200
    [    1.765996] sunxi:ccu_ddr:[ERR]: dram_div:0x0
    [    1.771691] uart-ng uart-ng0: supply uart not found, using dummy regulator
    [    1.777357] sunxi:uart-ng-uart-ng0:[INFO]: cannot get the TX DMA channel!
    [    1.783944] sunxi:uart-ng-uart-ng0:[INFO]: cannot get the RX DMA channel!
    [    1.790743] sunxi:uart-ng:[INFO]: sunxi uart-ng driver version: 1.1.7
    [    1.797140] uart-ng0: ttyAS0 at MMIO 0x2600000 (irq = 46, base_baud = 1500000) is a SUNXI
    [    1.805270] sunxi:uart-ng-uart-ng0:[INFO]: console setup baud 115200 parity n bits 8, flow n
    [    1.813775] printk: console [ttyAS0] enabled
    [    1.813775] printk: console [ttyAS0] enabled
    [    1.824114] printk: bootconsole [earlycon0] disabled
    [    1.824114] printk: bootconsole [earlycon0] disabled
    [    1.834910] uart-ng uart-ng1: supply uart not found, using dummy regulator
    [    1.846658] sunxi:uart-ng-uart-ng1:[INFO]: cannot get the TX DMA channel!
    [    1.854274] sunxi:uart-ng-uart-ng1:[INFO]: cannot get the RX DMA channel!
    [    1.861964] uart-ng1: ttyAS1 at MMIO 0x2601000 (irq = 47, base_baud = 1500000) is a SUNXI
    [    1.871999] uart-ng uart-ng2: supply uart not found, using dummy regulator
    [    1.879876] sunxi:uart-ng-uart-ng2:[INFO]: cannot get the TX DMA channel!
    [    1.887489] sunxi:uart-ng-uart-ng2:[INFO]: cannot get the RX DMA channel!
    [    1.895175] uart-ng2: ttyAS2 at MMIO 0x2602000 (irq = 48, base_baud = 1500000) is a SUNXI
    [    1.905213] uart-ng uart-ng3: supply uart not found, using dummy regulator
    [    1.913089] sunxi:uart-ng-uart-ng3:[INFO]: cannot get the TX DMA channel!
    [    1.920732] sunxi:uart-ng-uart-ng3:[INFO]: cannot get the RX DMA channel!
    [    1.928430] uart-ng3: ttyAS3 at MMIO 0x2603000 (irq = 49, base_baud = 1500000) is a SUNXI
    [    1.938462] uart-ng uart-ng4: supply uart not found, using dummy regulator
    [    1.946346] sunxi:uart-ng-uart-ng4:[INFO]: cannot get the TX DMA channel!
    [    1.953937] sunxi:uart-ng-uart-ng4:[INFO]: cannot get the RX DMA channel!
    [    1.961594] uart-ng4: ttyAS4 at MMIO 0x2604000 (irq = 50, base_baud = 1500000) is a SUNXI
    [    1.971669] uart-ng uart-ng5: supply uart not found, using dummy regulator
    [    1.979532] sunxi:uart-ng-uart-ng5:[INFO]: cannot get the TX DMA channel!
    [    1.987138] sunxi:uart-ng-uart-ng5:[INFO]: cannot get the RX DMA channel!
    [    1.994801] uart-ng5: ttyAS5 at MMIO 0x2605000 (irq = 51, base_baud = 1500000) is a SUNXI
    [    2.004824] uart-ng uart-ng6: supply uart not found, using dummy regulator
    [    2.012702] sunxi:uart-ng-uart-ng6:[INFO]: cannot get the TX DMA channel!
    [    2.020324] sunxi:uart-ng-uart-ng6:[INFO]: cannot get the RX DMA channel!
    [    2.028007] uart-ng6: ttyAS6 at MMIO 0x2606000 (irq = 52, base_baud = 1500000) is a SUNXI
    [    2.038035] uart-ng uart-ng7: supply uart not found, using dummy regulator
    [    2.045912] sunxi:uart-ng-uart-ng7:[INFO]: cannot get the TX DMA channel!
    [    2.053591] sunxi:uart-ng-uart-ng7:[INFO]: cannot get the RX DMA channel!
    [    2.061248] uart-ng7: ttyAS7 at MMIO 0x2607000 (irq = 53, base_baud = 1500000) is a SUNXI
    [    2.071250] uart-ng uart-ng9: supply uart not found, using dummy regulator
    [    2.079119] sunxi:uart-ng-uart-ng9:[INFO]: cannot get the TX DMA channel!
    [    2.086740] sunxi:uart-ng-uart-ng9:[INFO]: cannot get the RX DMA channel!
    [    2.094394] uart-ng9: ttyAS9 at MMIO 0x2609000 (irq = 54, base_baud = 1500000) is a SUNXI
    [    2.104379] uart-ng uart-ng11: supply uart not found, using dummy regulator
    [    2.112340] sunxi:uart-ng-uart-ng11:[INFO]: cannot get the TX DMA channel!
    [    2.120044] sunxi:uart-ng-uart-ng11:[INFO]: cannot get the RX DMA channel!
    [    2.127802] uart-ng11: ttyAS11 at MMIO 0x260b000 (irq = 55, base_baud = 1500000) is a SUNXI
    [    2.137943] uart-ng uart-ng12: supply uart not found, using dummy regulator
    [    2.145921] sunxi:uart-ng-uart-ng12:[INFO]: cannot get the TX DMA channel!
    [    2.153639] sunxi:uart-ng-uart-ng12:[INFO]: cannot get the RX DMA channel!
    [    2.161412] uart-ng12: ttyAS12 at MMIO 0x260c000 (irq = 56, base_baud = 1500000) is a SUNXI
    [    2.171534] uart-ng uart-ng15: supply uart not found, using dummy regulator
    [    2.179500] sunxi:uart-ng-uart-ng15:[INFO]: cannot get the TX DMA channel!
    [    2.187195] sunxi:uart-ng-uart-ng15:[INFO]: cannot get the RX DMA channel!
    [    2.194991] uart-ng15: ttyAS15 at MMIO 0x7080000 (irq = 57, base_baud = 1500000) is a SUNXI
    [    2.205187] uart-ng uart-ng16: supply uart not found, using dummy regulator
    [    2.213164] sunxi:uart-ng-uart-ng16:[INFO]: cannot get the TX DMA channel!
    [    2.220883] sunxi:uart-ng-uart-ng16:[INFO]: cannot get the RX DMA channel!
    [    2.228637] uart-ng16: ttyAS16 at MMIO 0x7081000 (irq = 58, base_baud = 1500000) is a SUNXI
    [    2.239689] sunxi:rtc:[INFO]:  Saving SoC boot-reason: COLD-BOOT
    [    2.246441] sunxi:rtc-7090000.rtc:[INFO]: errata__fix_alarm_day_reg_default_value(): ALARM0_DAY_REG=0, set it to 1
    [    2.258750] sunxi-rtc 7090000.rtc: registered as rtc0
    [    2.264472] sunxi-rtc 7090000.rtc: setting system clock to 1970-01-01T00:00:04 UTC (4)
    [    2.273350] sunxi:rtc-7090000.rtc:[INFO]: sunxi rtc probed
    [    2.280909] NSI_PMU 2020000.nsi-controller: Get ia_pmu_data_unit failed
    [    2.288350] NSI_PMU 2020000.nsi-controller: Get ta_pmu_data_unit failed
    [    2.295785] NSI_PMU 2020000.nsi-controller: Get cpu_pmu_data_unit failed
    [    2.303602] NSI_PMU 2020000.nsi-controller: nsi not support ecc(efuse)
    [    2.312255] sunxi-wdt 2050000.watchdog: Watchdog enabled (timeout=16 sec, nowayout=0), driver version: 1.0.4
    [    2.324572] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: SD/MMC/SDIO Host Controller Driver(v5.58 2024-11-13 15:50)
    [    2.336396] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: ctl-spec-caps 328
    [    2.344322] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: No vdmmc regulator found
    [    2.352534] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: No vd33sw regulator found
    [    2.360832] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: No vd18sw regulator found
    [    2.369143] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: No vq33sw regulator found
    [    2.377445] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: No vq18sw regulator found
    [    2.385753] sunxi:sunxi_mmc_host-4022000.sdmmc:[WARN]: Cann't get pin bias hs pinstate,check if needed
    [    2.396286] sunxi:sunxi_mmc_host-4022000.sdmmc:[ERR]: Could not get mbus clock
    [    2.404422] sunxi:sunxi_mmc_host-4022000.sdmmc:[ERR]: Could not get store clock
    [    2.413068] sunxi-mmc 4022000.sdmmc: sunxi:sunxi_mmc_host***ctl-cmdq-md*** 20
    [    2.421277] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 0Hz bm PP pm UP vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.446709] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.472737] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.486093] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: detmode:alway in(non removable)
    [    2.489110] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.496205] sunxi:sunxi_mmc_host-4020000.sdmmc:[INFO]: SD/MMC/SDIO Host Controller Driver(v5.58 2024-11-13 15:50)
    [    2.509676] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm OD pm ON vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.520189] sunxi:sunxi_mmc_host-4020000.sdmmc:[INFO]: ctl-spec-caps 428
    [    2.541283] sunxi:sunxi_mmc_host-4020000.sdmmc:[INFO]: No vqmmc regulator found
    [    2.549503] sunxi:sunxi_mmc_host-4020000.sdmmc:[INFO]: No vdmmc regulator found
    [    2.557839] sunxi:sunxi_mmc_host-4020000.sdmmc:[ERR]: Could not get mbus clock
    [    2.565985] sunxi:sunxi_mmc_host-4020000.sdmmc:[ERR]: Could not get store clock
    [    2.572198] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm OD pm ON vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.574638] sunxi-mmc 4020000.sdmmc: Got CD GPIO
    [    2.587619] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm OD pm ON vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.592793] sunxi-mmc 4020000.sdmmc: sunxi:sunxi_mmc_hostcd-set-debounce is 0x1
    [    2.609046] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm OD pm ON vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.614259] sunxi-mmc 4020000.sdmmc: sunxi:sunxi_mmc_hostexecute tuning in kernel, retune_period=3600
    [    2.638132] sunxi:sunxi_mmc_host-4020000.sdmmc:[INFO]: sdc set ios:clk 0Hz bm PP pm UP vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.651092] sunxi:sunxi_mmc_host-4020000.sdmmc:[INFO]: no vqmmc,Check if there is regulator
    [    2.655907] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.672995] sunxi:sunxi_mmc_host-4020000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 23 width 1 timing LEGACY(SDR12) dt B
    [    2.686568] sunxi:sunxi_mmc_host-4022000.sdmmc:[ERR]: avoid to switch power_off_notification to POWERED_ON(0x01)
    [    2.698595] sunxi:sunxi_mmc_host-4022000.sdmmc:[ERR]: avoid to switch power_off_notification to POWERED_ON(0x01)
    [    2.700064] sunxi:sunxi_mmc_host-4020000.sdmmc:[INFO]: detmode:gpio irq
    [    2.710001] sunxi:sunxi_mmc_host-4022000.sdmmc:[ERR]: avoid to switch power_off_notification to POWERED_ON(0x01)
    [    2.710008] sunxi:sunxi_mmc_host-4022000.sdmmc:[ERR]: avoid to switch power_off_notification to POWERED_ON(0x01)
    [    2.718255] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: SD/MMC/SDIO Host Controller Driver(v5.58 2024-11-13 15:50)
    [    2.729547] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 23 width 8 timing LEGACY(SDR12) dt B
    [    2.740582] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: ctl-spec-caps 428
    [    2.754237] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 23 width 8 timing MMC-HS200 dt B
    [    2.765262] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: No vmmc regulator found
    [    2.772738] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 52000000Hz bm PP pm ON vdd 23 width 8 timing MMC-HS200 dt B
    [    2.785634] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: No vqmmc regulator found
    [    2.794200] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 150000000Hz bm PP pm ON vdd 23 width 8 timing MMC-HS200 dt B
    [    2.806858] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: No vdmmc regulator found
    [    2.806863] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: No vd33sw regulator found
    [    2.806866] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: No vd18sw regulator found
    [    2.806874] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: No vq33sw regulator found
    [    2.815287] sunxi:sunxi_mmc_host-4022000.sdmmc:[ERR]: sdc2 :the host don't support tuning in kernel
    [    2.828331] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: No vq18sw regulator found
    [    2.828338] sunxi:sunxi_mmc_host-4021000.sdmmc:[ERR]: manual set ocr
    [    2.836574] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 150000000Hz bm PP pm ON vdd 23 width 8 timing MMC-HS(SDR20) dt B
    [    2.844848] sunxi:sunxi_mmc_host-4021000.sdmmc:[WARN]: Cann't get pin bias hs pinstate,check if needed
    [    2.853339] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 52000000Hz bm PP pm ON vdd 23 width 8 timing MMC-HS(SDR20) dt B
    [    2.861490] sunxi:sunxi_mmc_host-4021000.sdmmc:[ERR]: Could not get mbus clock
    [    2.872036] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 50000000Hz bm PP pm ON vdd 23 width 8 timing MMC-HS400 dt B
    [    2.879897] sunxi:sunxi_mmc_host-4021000.sdmmc:[ERR]: Could not get store clock
    [    2.887218] sunxi:sunxi_mmc_host-4022000.sdmmc:[INFO]: sdc set ios:clk 150000000Hz bm PP pm ON vdd 23 width 8 timing MMC-HS400 dt B
    [    2.901081] sunxi-mmc 4021000.sdmmc: sunxi:sunxi_mmc_hostexecute tuning in kernel, retune_period=3600
    [    2.902866] sunxi:sunxi_mmc_host-4020000.sdmmc:[INFO]: sdc set ios:clk 0Hz bm PP pm OFF vdd 0 width 1 timing LEGACY(SDR12) dt B
    [    2.902898] sunxi:pin-3604000.pinctrl:[INFO]: Auto power withstand voltage configuration detected, automatically exit!
    [    2.911462] mmc0: new HS400 MMC card at address 0001
    [    2.924787] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: sdc set ios:clk 0Hz bm PP pm UP vdd 21 width 1 timing LEGACY(SDR12) dt B
    [    2.933677] mmcblk0: mmc0:0001 58A43A 14.6 GiB 
    [    2.958456] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [    2.977823] mmcblk0rpmb: mmc0:0001 58A43A partition 3 4.00 MiB, chardev (245:0)
    [    3.003244] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: detmode:manually by software
    [    3.004048] sunxi:sunxi_mmc_host-4021000.sdmmc:[ERR]: smc 2 p1 err, cmd 52, RTO !!
    [    3.010858]  mmcblk0: p1 p2 p3 p4 p5 p6
    [    3.021800] sunxi:sunxi_mmc_host-4021000.sdmmc:[ERR]: smc 2 p1 err, cmd 52, RTO !!
    [    3.021938] [drm] [DSI-PANEL] panel_dsi_init start
    [    3.022434] [drm] [DSI-PANEL] dsi driver regsiter finsh
    [    3.023450] [drm] [TCON_TOP]sunxi_tcon_top_probe start
    [    3.024206] sunxi-display-engine 5000000.de: Adding to iommu group 0
    [    3.025360] [drm] de use no display sys
    [    3.025530] [drm] [SUNXI-DE] port reg not found
    [    3.025640] sunxi-display-engine 5000000.de: register iommu fault callback for sunxi-drm, master=5
    [    3.026539] [drm] [PHY] sunxi_dsi_combophy_probe start
    [    3.126843] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [    3.127245] [drm] [PHY]sunxi_dsi_combophy_probe finish
    [    3.143221] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [    3.147068] [drm] [DSI] sunxi_drm_dsi_probe start
    [    3.161058] sunxi-mmc 4021000.sdmmc: card claims to support voltages below defined range
    [    3.165256] [drm] [DSI-PANEL] panel_dsi_probe start
    [    3.175667] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: sdc set ios:clk 0Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [    3.179215] [drm:panel_dsi_probe] *ERROR* endpoint panel_node not fount
    [    3.199527] virtual-panel 5506000.dsi0.0: get child panel fail
    [    3.204628] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 1 timing LEGACY(SDR12) dt B
    [    3.206661] [drm] [DSI]sunxi_drm_dsi_host_attach start
    [    3.225202] [drm] [DSI]sunxi_drm_dsi_host_attach finish
    [    3.230975] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 4 timing LEGACY(SDR12) dt B
    [    3.231070] [drm] [DSI-PANEL] panel_dsi_probe finish
    [    3.245211] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: sdc set ios:clk 400000Hz bm PP pm ON vdd 21 width 4 timing UHS-DDR50 dt B
    [    3.250281] [drm] [DSI]sunxi_drm_dsi_probe ok
    [    3.263100] sunxi:sunxi_mmc_host-4021000.sdmmc:[INFO]: sdc set ios:clk 50000000Hz bm PP pm ON vdd 21 width 4 timing UHS-DDR50 dt B
    [    3.269842] [drm] [TCON] sunxi_tcon_probe start
    [    3.282366] mmc2: new ultra high speed DDR50 SDIO card at address 0001
    [    3.286224] [drm] [SUNXI-TCON] sunxi_tcon_of_get_id 0
    [    3.299387] [drm] [TCON] sunxi_tcon_probe ret = 0
    [    3.305147] [drm] sunxi_drm_platform_probe start
    [    3.310353] [drm] sunxi_drm_match_add start
    [    3.317713] [drm] sunxi_drm_match_add finish
    [    3.322561] [drm] sunxi_drm_bind start
    [    3.327088] [drm] [TCON_TOP]sunxi_tcon_top_bind start
    [    3.332931] sunxi-drm soc@3000000:sunxi-drm: bound 5500000.vo0 (ops sunxi_tcon_top_component_ops)
    [    3.342888] [drm] [SUNXI-DE] sunxi_de_bind start
    [    3.348137] sunxi-drm soc@3000000:sunxi-drm: Adding to iommu group 0
    [    3.355412] [drm] sunxi_de_bind crtc init for de 0 ok
    [    3.361119] sunxi-drm soc@3000000:sunxi-drm: bound 5000000.de (ops sunxi_de_component_ops)
    [    3.370413] sunxi-drm soc@3000000:sunxi-drm: bound 5507000.phy (ops sunxi_cphy_component_ops)
    [    3.379960] [drm] [DSI]sunxi_drm_dsi_bind start
    [    3.385143] [drm] [SUNXI-TCON] sunxi_tcon_of_get_id 0
    [    3.390904] sunxi-drm soc@3000000:sunxi-drm: bound 5506000.dsi0 (ops sunxi_drm_dsi_component_ops)
    [    3.400872] sunxi-drm soc@3000000:sunxi-drm: bound 5501000.tcon0 (ops sunxi_tcon_component_ops)
    [    3.413544] [drm] [SUNXI-CRTC]sunxi_crtc_atomic_enable
    [    3.419337] [drm] sunxi_de_enable index 0
    [    3.423873] [drm] sunxi_de_enable finish sw en=1
    [    3.429067] [drm] [DSI] sunxi_drm_dsi_encoder_atomic_enable start
    [    3.435941] [drm] [DSI] sunxi_tcon_dsi_mode_init start
    [    3.441919] [drm] [DSI] sunxi_lcd_pin_set_state start
    [    3.470282] platform 2091010.pwm: supply pwm not found, using dummy regulator
    [    3.478633] [drm] [DSI] sunxi_drm_dsi_encoder_atomic_enable finish
    [    3.492572] [drm] Initialized sunxi-drm 3.0.0 20230901 for soc@3000000:sunxi-drm on minor 0
    [    3.501960] [drm] sunxi_drm_bind ok
    [    3.506304] sunxi:VE:[INFO]: 2735 sunxi_cedar_init(): sunxi cedar version 1.1
    [    3.514730] sunxi-cedar 1c0e000.ve: Adding to iommu group 0
    [    3.521507] sunxi:VE:[WARN]: 2563 cedardev_init(): ve vol = 940 mv
    [    3.528496] sunxi:VE:[INFO]: 2268 deal_with_resouce(): cedar-ve the get irq is 128
    [    3.537142] sunxi:VE:[WARN]: 91 resource_iomap_init(): ve Can't map regs_ccmu registers, maybe no use
    [    3.547878] sunxi:VE:[INFO]: 372 ve_debug_register_driver(): ve_debug_proc_info:(____ptrval____), data:(____ptrval____), lock:(____ptrval____)
    [    3.565118] dwmac-sunxi 4500000.ethernet: IRQ eth_wake_irq not found
    [    3.572267] dwmac-sunxi 4500000.ethernet: IRQ eth_lpi not found
    [    3.579304] sunxi:stmmac-4500000.ethernet:[INFO]: Phy use ext osc
    [    3.586224] sunxi:stmmac-4500000.ethernet:[WARN]: Not found dwmac3v3-supply
    [    3.594050] sunxi:stmmac-4500000.ethernet:[WARN]: Not found phy3v3-supply
    [    3.601660] sunxi:stmmac-4500000.ethernet:[WARN]: Get gmac tx-delay failed, use default 0
    [    3.610841] sunxi:stmmac-4500000.ethernet:[WARN]: Get gmac rx-delay failed, use default 0
    [    3.620019] sunxi:stmmac-4500000.ethernet:[INFO]: Not found delay-maps in dts
    [    3.628030] sunxi:stmmac-4500000.ethernet:[INFO]: RGMII use internal transmit clock
    [    3.636834] dwmac-sunxi 4500000.ethernet: User ID: 0x20, Synopsys ID: 0x53
    [    3.644542] dwmac-sunxi 4500000.ethernet:         DWMAC4/5
    [    3.650016] dwmac-sunxi 4500000.ethernet: DMA HW capability register supported
    [    3.658091] dwmac-sunxi 4500000.ethernet: RX Checksum Offload Engine supported
    [    3.666204] dwmac-sunxi 4500000.ethernet: TX Checksum insertion supported
    [    3.673795] dwmac-sunxi 4500000.ethernet: Wake-Up On Lan supported
    [    3.680807] dwmac-sunxi 4500000.ethernet: Enable RX Mitigation via HW Watchdog Timer
    [    3.689505] dwmac-sunxi 4500000.ethernet: Using 32 bits DMA width
    [    3.781442] sunxi:stmmac-4500000.ethernet:[INFO]: probe success (Version 0.3.1)
    [    3.791056] dwmac-sunxi 4510000.ethernet: IRQ eth_wake_irq not found
    [    3.798205] dwmac-sunxi 4510000.ethernet: IRQ eth_lpi not found
    [    3.805149] sunxi:stmmac-4510000.ethernet:[INFO]: Phy use ext osc
    [    3.812061] sunxi:stmmac-4510000.ethernet:[WARN]: Not found dwmac3v3-supply
    [    3.819877] sunxi:stmmac-4510000.ethernet:[WARN]: Not found phy3v3-supply
    [    3.827504] sunxi:stmmac-4510000.ethernet:[WARN]: Get gmac tx-delay failed, use default 0
    [    3.836681] sunxi:stmmac-4510000.ethernet:[WARN]: Get gmac rx-delay failed, use default 0
    [    3.845845] sunxi:stmmac-4510000.ethernet:[INFO]: Not found delay-maps in dts
    [    3.853827] sunxi:stmmac-4510000.ethernet:[INFO]: RGMII use internal transmit clock
    [    3.862646] dwmac-sunxi 4510000.ethernet: User ID: 0x20, Synopsys ID: 0x53
    [    3.870331] dwmac-sunxi 4510000.ethernet:         DWMAC4/5
    [    3.875820] dwmac-sunxi 4510000.ethernet: DMA HW capability register supported
    [    3.883919] dwmac-sunxi 4510000.ethernet: RX Checksum Offload Engine supported
    [    3.892027] dwmac-sunxi 4510000.ethernet: TX Checksum insertion supported
    [    3.899621] dwmac-sunxi 4510000.ethernet: Wake-Up On Lan supported
    [    3.906633] dwmac-sunxi 4510000.ethernet: Enable RX Mitigation via HW Watchdog Timer
    [    3.915314] dwmac-sunxi 4510000.ethernet: Using 32 bits DMA width
    [    4.006558] sunxi:stmmac-4510000.ethernet:[INFO]: probe success (Version 0.3.1)
    [    4.016431] sunxi:gpadc:[INFO]: sunxi_gpadc_init(): 2075: gpadc class register success
    [    4.025758] sun55iw6-pinctrl 3604000.pinctrl: pin PA6 already requested by 3604000.pinctrl:6; cannot claim for 2087000.gpadc
    [    4.038349] sun55iw6-pinctrl 3604000.pinctrl: pin-6 (2087000.gpadc) status -22
    [    4.046471] sun55iw6-pinctrl 3604000.pinctrl: could not request pin 6 (PA6) from group PA6  on device 3604000.pinctrl
    [    4.058371] sunxi-gpadc 2087000.gpadc: Error applying setting, reverse things back
    [    4.066880] sunxi-gpadc: probe of 2087000.gpadc failed with error -22
    [    4.074165] sunxi:gpadc-2088000.gpadc:[INFO]: gpadc channel only used for gapdc
    [    4.082408] sunxi:gpadc-2088000.gpadc:[WARN]: warn: sample rate not set
    [    4.089834] sunxi:gpadc-2088000.gpadc:[WARN]: sunxi_gpadc_dts_parse: warn: keyadc not select
    [    4.099542] sunxi:sunxi_sidget_soc_ver_regs() +267: Failed to find "soc_id" in dts.
    [    4.108699] sunxi:gpadc-2088000.gpadc:[INFO]: sunxi_gpadc_dts_parse: sync_group 0
    [    4.117406] input: sunxi-gpadc1/channel0/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input1
    [    4.128640] input: sunxi-gpadc1/channel1/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input2
    [    4.139867] input: sunxi-gpadc1/channel2/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input3
    [    4.151061] input: sunxi-gpadc1/channel3/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input4
    [    4.162238] input: sunxi-gpadc1/channel4/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input5
    [    4.173432] input: sunxi-gpadc1/channel5/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input6
    [    4.184600] input: sunxi-gpadc1/channel6/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input7
    [    4.195816] input: sunxi-gpadc1/channel7/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input8
    [    4.207017] input: sunxi-gpadc1/channel8/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input9
    [    4.218208] input: sunxi-gpadc1/channel9/input0 as /devices/platform/soc@3000000/2088000.gpadc/input/input10
    [    4.229658] sunxi:gpadc-2088000.gpadc:[INFO]: sunxi_gpadc probe success
    [    4.237205] sunxi:gpadc-2089000.gpadc:[WARN]: warn: sample rate not set
    [    4.244660] sunxi:gpadc-2089000.gpadc:[ERR]: sunxi_gpadc_dts_parse:get channel0_compare_higdata err!
    [    4.254894] sunxi:gpadc-2089000.gpadc:[INFO]: sunxi_gpadc_dts_parse: sync_group 0
    [    4.263535] input: sunxi-gpadc2/channel0/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input11
    [    4.274770] input: sunxi-gpadc2/channel1/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input12
    [    4.286029] input: sunxi-gpadc2/channel2/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input13
    [    4.297331] input: sunxi-gpadc2/channel3/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input14
    [    4.308639] input: sunxi-gpadc2/channel4/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input15
    [    4.319898] input: sunxi-gpadc2/channel5/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input16
    [    4.331195] input: sunxi-gpadc2/channel6/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input17
    [    4.342485] input: sunxi-gpadc2/channel7/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input18
    [    4.353764] input: sunxi-gpadc2/channel8/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input19
    [    4.365053] input: sunxi-gpadc2/channel9/input0 as /devices/platform/soc@3000000/2089000.gpadc/input/input20
    [    4.376475] sunxi:gpadc-2089000.gpadc:[INFO]: sunxi_gpadc probe success
    [    4.384010] sunxi:gpadc-208a000.gpadc:[WARN]: sunxi_gpadc_dts_parse: warn: keyadc not select
    [    4.393515] sunxi:gpadc-208a000.gpadc:[INFO]: sunxi_gpadc_dts_parse: sync_group 0
    [    4.402161] input: sunxi-gpadc3/channel0/input0 as /devices/platform/soc@3000000/208a000.gpadc/input/input21
    [    4.413551] sunxi:gpadc-208a000.gpadc:[INFO]: sunxi_gpadc probe success
    [    4.421862] sunxi-rtp 208c000.rtp: can't request region for resource [mem 0x0208c000-0x0208c3ff]
    [    4.431723] sunxi:tpadc-208c000.rtp:[ERR]: Fail to map IO resource
    [    4.438638] sunxi:tpadc-208c000.rtp:[ERR]: sunxi rtp get resource failed
    [    4.446359] sunxi-rtp: probe of 208c000.rtp failed with error -16
    [    4.453584] RTW: module init start
    [    4.457392] RTW: rtl8821cs v5.15.9.3-1-gf1a46d7a4.20240325_COEX20230331-5d5d
    [    4.465254] RTW: build time: Nov 23 2026 09:35:23
    [    4.470527] RTW: rtl8821cs BT-Coex version = COEX20230331-5d5d
    [    4.477122] RTW: rtw_inetaddr_notifier_register
    [    4.482421] RTW: DBG_MEM_ALLOC devobj_init:2754 dbg_rtw_zmalloc(9864)
    [    4.489751] RTW: == SDIO Card Info ==
    [    4.493863] RTW:   card: (____ptrval____)
    [    4.498359] RTW:   clock: 50000000 Hz
    [    4.502464] RTW:   timing spec: sd uhs DDR50
    [    4.507237] RTW:   sd3_bus_mode: TRUE
    [    4.511321] RTW:   func num: 1
    [    4.514745] RTW:   func1: (____ptrval____) (*)
    [    4.519722] RTW:   max_byte_size: 512
    [    4.523833] RTW: ================
    [    4.527540] RTW: CHIP TYPE: RTL8821C
    [    4.531570] RTW: loadparam, Select P2P interface: iface_id:1
    [    4.537979] RTW: [HALMAC]55772M
    [    4.537979] HALMAC_MAJOR_VER = 1
    [    4.537979] HALMAC_PROTOTYPE_VER = 6
    [    4.537979] HALMAC_MINOR_VER = 7
    [    4.537979] HALMAC_PATCH_VER = 11
    [    4.559707] RTW: Chip Version Info: CHIP_8821C_U5_1T1R_RomVer(4)
    [    4.574683] RTW: SetHwReg: bMacPwrCtrlOn=1
    [    4.667708] RTW: is_valid_id_status: HALMAC_FEATURE_DUMP_LOGICAL_EFUSE
    [    4.675040] RTW: HW EFUSE
    [    4.677977] RTW: 0x000: 29 81 00 BC  09 10 28 00  AA 04 AD 75  10 8E 30 0B  
    [    4.685919] RTW: 0x010: FF FF FF FF  FF FF FF FF  FF FF FF 02  FF FF FF FF  
    [    4.693878] RTW: 0x020: FF FF 2C 2B  2B 2A 26 26  26 25 25 25  25 26 26 27  
    [    4.701855] RTW: 0x030: 02 FF FF FF  FF FF 00 FF  FF FF 2B 2B  2B 2B 2B 2B  
    [    4.709799] RTW: 0x040: 2C 2C 2C 2D  2D 12 FF FF  FF FF FF FF  FF FF FF FF  
    [    4.717766] RTW: 0x050: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.725721] RTW: 0x060: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.733673] RTW: 0x070: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.741614] RTW: 0x080: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.749572] RTW: 0x090: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.757529] RTW: 0x0A0: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.765479] RTW: 0x0B0: FF FF FF FF  FF FF FF FF  7F 6D 21 00  FF FF FF FF  
    [    4.773439] RTW: 0x0C0: FF 21 00 41  00 00 00 00  00 FF 02 FF  FF FF FF FF  
    [    4.781413] RTW: 0x0D0: 7E D1 01 23  34 FF FF FF  20 04 4C 02  21 C8 21 02  
    [    4.789364] RTW: 0x0E0: 0C 00 22 04  00 08 00 32  FF 21 02 0C  00 22 2A 01  
    [    4.797330] RTW: 0x0F0: 01 00 00 00  00 00 00 00  00 00 00 00  02 00 FF FF  
    [    4.805288] RTW: 0x100: 00 00 00 00  00 00 00 00  00 00 00 00  00 00 00 00  
    [    4.813270] RTW: 0x110: 00 EB 00 6E  01 00 00 00  00 FF 40 55  48 45 16 0A  
    [    4.821223] RTW: 0x120: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.829173] RTW: 0x130: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.837119] RTW: 0x140: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.845083] RTW: 0x150: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.853045] RTW: 0x160: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.860985] RTW: 0x170: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.868951] RTW: 0x180: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.876914] RTW: 0x190: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.884869] RTW: 0x1A0: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.892820] RTW: 0x1B0: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.900767] RTW: 0x1C0: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.908724] RTW: 0x1D0: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.916697] RTW: 0x1E0: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.924667] RTW: 0x1F0: FF FF FF FF  FF FF FF FF  FF FF FF FF  FF FF FF FF  
    [    4.932623] RTW: EEPROM ID = 0x8129
    [    4.936529] RTW: EEPROM Version = 0
    [    4.940426] RTW: EEPROM Regulatory=0x01
    [    4.944723] RTW: EEPROM Board Type=0x01
    [    4.949111] RTW: EEPROM Enable BT-coex, ant_num=1
    [    4.954401] RTW: EEPROM crystal_cap=0x6d
    [    4.958797] RTW: EEPROM ThermalMeter=0x21
    [    4.963331] RTW: EEPROM Customer ID=0x00
    [    4.967737] RTW: EEPROM SupportRemoteWakeup=1
    [    4.972638] RTW: EEPROM rfe_type=0x2
    [    4.976629] RTW: WIFI Module is iPA/iLNA
    [    4.981027] RTW: EEPROM tx_bbswing_24G =0x00
    [    4.985814] RTW: EEPROM tx_bbswing_5G =0x00
    [    4.998905] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:38 dbg_rtw_zmalloc(29184)
    [    5.008131] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:54 dbg_rtw_mfree(29184)
    [    5.020496] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:38 dbg_rtw_zmalloc(29184)
    [    5.029709] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:54 dbg_rtw_mfree(29184)
    [    5.040230] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:38 dbg_rtw_zmalloc(29184)
    [    5.049434] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:54 dbg_rtw_mfree(29184)
    [    5.059944] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:38 dbg_rtw_zmalloc(6656)
    [    5.068536] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:54 dbg_rtw_mfree(6656)
    [    5.078605] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:38 dbg_rtw_zmalloc(29184)
    [    5.087819] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:54 dbg_rtw_mfree(29184)
    [    5.099035] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:38 dbg_rtw_zmalloc(15872)
    [    5.107939] RTW: DBG_MEM_ALLOC sdio_write_data_rsvd_page:54 dbg_rtw_mfree(15872)
    [    5.127652] RTW: DBG_MEM_ALLOC _rtw_hal_set_fw_rsvd_page:12646 dbg_rtw_zmalloc(5120)
    [    5.136335] RTW: _rtw_hal_set_fw_rsvd_page((null)) Get [ NOR ] RsvdPageNUm  ==>
    [    5.144533] RTW: LocPsPoll: 4
    [    5.147866] RTW: WARN Invalid rate 0x0 in MRateToHwRate
    [    5.153721] RTW: LocNullData: 5
    [    5.157251] RTW: WARN Invalid rate 0x0 in MRateToHwRate
    [    5.163107] RTW: LocQosNull: 6
    [    5.166531] RTW: WARN Invalid rate 0x0 in MRateToHwRate
    [    5.172396] RTW: LocBTQosNull: 7
    [    5.176010] RTW: WARN Invalid rate 0x0 in MRateToHwRate
    [    5.181853] RTW: DBG_MEM_ALLOC _rtw_hal_set_fw_rsvd_page:12904 dbg_rtw_mfree(5120)
    [    5.190354] RTW: _rtw_hal_set_fw_rsvd_page((null)) Get [ NOR ] RsvdPageNUm <==
    [    5.207050] RTW: WARN [HALMAC][WARN]the H2C ver. does not match halmac
    [    5.215440] RTW: [H2C] - 4C 02 00 04  11 00 00 00  
    [    5.220948] RTW: rtl8821c_fw_dl Download Firmware from array success
    [    5.228098] RTW: NIC FW Version:24 SubVersion:13
    [    5.234383] RTW: c2h_mac_hidden_rpt_hdl: 0x55
    [    5.239292] RTW: c2h_mac_hidden_rpt_hdl: 0x3B
    [    5.244169] RTW: c2h_mac_hidden_rpt_hdl: 0xF6
    [    5.249046] RTW: c2h_mac_hidden_rpt_hdl: 0xD3
    [    5.253917] RTW: c2h_mac_hidden_rpt_hdl: 0xF6
    [    5.258795] RTW: c2h_mac_hidden_rpt_hdl: 0xFF
    [    5.263678] RTW: c2h_mac_hidden_rpt_hdl: 0x37
    [    5.268562] RTW: c2h_mac_hidden_rpt_hdl: 0xFF
    [    5.273458] RTW: uuid x:0x55 y:0x3b z:0x16 crc:0x69f
    [    5.279021] RTW: hci_type:0x6
    [    5.282335] RTW: package_type:0x7
    [    5.286063] RTW: tr_switch:0x1
    [    5.289489] RTW: wl_func:0xf
    [    5.292713] RTW: hw_stype:0xf
    [    5.296049] RTW: bw:0x7
    [    5.298784] RTW: ant_num:0x1
    [    5.302015] RTW: protocol:0x3
    [    5.305336] RTW: nic:0x3
    [    5.308170] RTW: c2h_mac_hidden_rpt_2_hdl: 0xFF
    [    5.313244] RTW: c2h_mac_hidden_rpt_2_hdl: 0xFF
    [    5.318327] RTW: c2h_mac_hidden_rpt_2_hdl: 0xF8
    [    5.323422] RTW: c2h_mac_hidden_rpt_2_hdl: 0xFC
    [    5.328495] RTW: c2h_mac_hidden_rpt_2_hdl: 0xFF
    [    5.333578] RTW: hal_read_mac_hidden_rpt OK! (1, 100ms), fwdl:1, id:0x19
    [    5.341206] RTW: is_valid_id_status: HALMAC_FEATURE_DUMP_PHYSICAL_EFUSE
    [    5.348743] RTW: is_valid_id_status: HALMAC_FEATURE_DUMP_PHYSICAL_EFUSE
    [    5.356261] RTW: is_valid_id_status: HALMAC_FEATURE_DUMP_PHYSICAL_EFUSE
    [    5.363758] RTW: is_valid_id_status: HALMAC_FEATURE_DUMP_PHYSICAL_EFUSE
    [    5.371285] RTW: is_valid_id_status: HALMAC_FEATURE_DUMP_PHYSICAL_EFUSE
    [    5.378815] RTW: is_valid_id_status: HALMAC_FEATURE_DUMP_PHYSICAL_EFUSE
    [    5.386358] RTW: is_valid_id_status: HALMAC_FEATURE_DUMP_PHYSICAL_EFUSE
    [    5.393883] RTW: SetHwReg: bMacPwrCtrlOn=0
    [    5.404507] RTW: rtw_hal_read_chip_info in 840 ms
    [    5.409809] RTW: [RF_PATH] ver_id.RF_TYPE:RF_1T1R
    [    5.415082] RTW: [RF_PATH] HALSPEC's rf_reg_trx_path_bmp:0x11, rf_reg_path_avail_num:1, max_tx_cnt:1
    [    5.425328] RTW: [RF_PATH] PG's trx_path_bmp:0x00, max_tx_cnt:0
    [    5.431960] RTW: [RF_PATH] Registry's trx_path_bmp:0x00, tx_path_lmt:0, rx_path_lmt:0
    [    5.440756] RTW: [RF_PATH] HALDATA's trx_path_bmp:0x11, max_tx_cnt:1
    [    5.447891] RTW: [RF_PATH] HALDATA's rf_type:RF_1T1R, NumTotalRFPath:1
    [    5.455204] RTW: rtw_hal_rfpath_init trx_path_bmp:0x11(RF_1T1R), NumTotalRFPath:1, max_tx_cnt:1
    [    5.464978] RTW: [TRX_Nss] HALSPEC - tx_nss:1, rx_nss:1
    [    5.470856] RTW: [TRX_Nss] Registry - tx_nss:0, rx_nss:0
    [    5.476813] RTW: [TRX_Nss] HALDATA - tx_nss:1, rx_nss:1
    [    5.482670] RTW: rtw_hal_trxnss_init tx_nss:1, rx_nss:1
    [    5.488535] RTW: txpath=0x1, rxpath=0x1
    [    5.492828] RTW: txpath_1ss:0x1, num:1
    [    5.497087] RTW: devobj_decide_init_chplan alpha2:{255,255}
    [    5.503328] RTW: devobj_decide_init_chplan chplan:0x7f
    [    5.509075] RTW: devobj_decide_init_chplan chplan_6g:0x00
    [    5.515115] RTW: devobj_decide_init_chplan disable_sw_chplan:0
    [    5.521647] RTW: rtw_rfctl_decide_init_chplan chplan:0x7F
    [    5.527817] RTW: init_mlme_default_rate_set: support CCK
    [    5.533786] RTW: init_mlme_default_rate_set: support OFDM
    [    5.539905] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.548631] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.557323] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.566041] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.574747] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.583448] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.592134] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.600811] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.609495] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.618180] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.626874] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.635558] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.644259] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.652954] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.661626] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.670330] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    5.679127] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(5632)
    [    5.687735] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(5632)
    [    5.696597] RTW: rtw_alloc_macid((null)) if1, mac_addr:ff:ff:ff:ff:ff:ff macid:1
    [    5.704893] RTW: rtw_init_pwrctrl_priv: IPS_mode=1, LPS_mode=2, LPS_level=1
    [    5.712714] RTW: rtw_init_pwrctrl_priv: WOW_IPS_mode=1, WOW_LPS_mode=2, WOW_LPS_level=1
    [    5.721711] RTW: Init_ODM_ComInfo bb_opmode set to 0
    [    5.727526] RTW: IQK FW offload:enable
    [    5.731745] RTW: init_phydm_cominfo: Fv=1 Cv=4
    [    5.736752] RTW: [A] 2G G00 CCK-1T base:45 from IC_DEF
    [    5.742489] RTW: [A] 2G G01 CCK-1T base:45 from IC_DEF
    [    5.748265] RTW: [A] 2G G02 CCK-1T base:45 from IC_DEF
    [    5.754030] RTW: [A] 2G G03 CCK-1T base:45 from IC_DEF
    [    5.759792] RTW: [A] 2G G04 CCK-1T base:45 from IC_DEF
    [    5.765557] RTW: [A] 2G G05 CCK-1T base:45 from IC_DEF
    [    5.771331] RTW: [A] 2G G00 BW40-1S base:45 from IC_DEF
    [    5.777196] RTW: [A] 2G G01 BW40-1S base:45 from IC_DEF
    [    5.783061] RTW: [A] 2G G02 BW40-1S base:45 from IC_DEF
    [    5.788938] RTW: [A] 2G G03 BW40-1S base:45 from IC_DEF
    [    5.794807] RTW: [A] 2G G04 BW40-1S base:45 from IC_DEF
    [    5.800685] RTW: rtw_regsty_chk_target_tx_power_valid return _FALSE for band:0, path:0, rs:0, t:-1
    [    5.810784] RTW: phy_ConfigBBWithPgParaFile(): No File PHY_REG_PG.txt, Load from HWImg Array!
    [    5.820390] RTW: ERROR >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    [    5.820395] RTW: ERROR >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    [    5.827211] RTW: ERROR PHY_REG_PG.txt doesn't exist, will use driver default power by rate parameter
    [    5.844272] RTW: ERROR Pls upload it into /lib/firmware/ or the path defined by fw_path in GKI kernel
    [    5.854607] RTW: ERROR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    [    5.854611] RTW: ERROR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    [    5.861485] ------------[ cut here ]------------
    [    5.873487] WARNING: CPU: 2 PID: 1 at bsp/drivers/net/wireless/rtl8821cs/hal/hal_com_phycfg.c:4348 phy_load_tx_power_by_rate+0x54/0x254
    [    5.887107] Modules linked in:
    [    5.890532] CPU: 2 PID: 1 Comm: swapper/0 Not tainted 5.10.198 #23
    [    5.897466] Hardware name: TLT536-EVM HDMI (DT)
    [    5.902523] pstate: 60c00005 (nZCv daif +PAN +UAO -TCO BTYPE=--)
    [    5.909268] pc : phy_load_tx_power_by_rate+0x54/0x254
    [    5.914915] lr : phy_load_tx_power_by_rate+0x1c0/0x254
    [    5.920646] sp : ffffffc01003ba80
    [    5.924336] x29: ffffffc01003ba80 x28: 0000000000000000 
    [    5.930283] x27: ffffffc0112e044c x26: ffffffc011341060 
    [    5.936221] x25: 0000000000000000 x24: ffffff8002da0000 
    [    5.942175] x23: ffffffc0119ed9a8 x22: 0000000000000001 
    [    5.948120] x21: ffffffc011fe5000 x20: ffffffc0128b5000 
    [    5.954082] x19: ffffffc0128b9000 x18: 0000000000000030 
    [    5.960015] x17: 0000000000000000 x16: ffffffc011884f00 
    [    5.965983] x15: ffffffffffffffff x14: ffffffc09003b797 
    [    5.971940] x13: ffffffc0117ec8c8 x12: 0000000000000912 
    [    5.977879] x11: 0000000000000306 x10: ffffffc011849158 
    [    5.983830] x9 : fffffffffffed780 x8 : ffffffc0117ec8c8 
    [    5.989767] x7 : ffffffc0118448c8 x6 : 0000000000004890 
    [    5.995706] x5 : 000000000000bff4 x4 : 40000000fffff306 
    [    6.001632] x3 : 0000000000000000 x2 : 0000000000000000 
    [    6.007586] x1 : ffffff8001cb8000 x0 : 0000000000000035 
    [    6.013528] Call trace:
    [    6.016258]  phy_load_tx_power_by_rate+0x54/0x254
    [    6.021524]  phy_load_tx_power_ext_info+0x5c/0x90
    [    6.026791]  rtw_hal_dm_init+0x54/0x70
    [    6.030995]  rtw_init_drv_sw+0x520/0x5b8
    [    6.035390]  rtw_sdio_primary_adapter_init+0x154/0x214
    [    6.041149]  rtw_drv_init+0x94/0x1dc
    [    6.045165]  sdio_bus_probe+0xe8/0x204
    [    6.049372]  really_probe+0xf0/0x530
    [    6.053371]  driver_probe_device+0xe4/0x130
    [    6.058038]  device_driver_attach+0xc0/0xd0
    [    6.062722]  __driver_attach+0xc8/0x190
    [    6.067011]  bus_for_each_dev+0x70/0xd0
    [    6.071292]  driver_attach+0x24/0x30
    [    6.075301]  bus_add_driver+0x144/0x244
    [    6.079600]  driver_register+0x78/0x130
    [    6.083888]  sdio_register_driver+0x28/0x3c
    [    6.088557]  rtw_drv_entry+0x110/0x170
    [    6.092768]  do_one_initcall+0x50/0x1c0
    [    6.097058]  kernel_init_freeable+0x230/0x294
    [    6.101928]  kernel_init+0x14/0x110
    [    6.105843]  ret_from_fork+0x10/0x38
    [    6.109852] ---[ end trace 7cc4f6fe331130e4 ]---
    [    6.115079] RTW: default power by rate loaded
    [    6.119972] RTW: phy_txpwr_by_rate_chk_for_path_dup duplicate 2.4G [A] to [B]
    [    6.127984] RTW: rtw_chset_apply_from_rtk_priv chplan:0x7F chplan_6g:0x00
    [    6.135615] RTW: band:5G ch52 is NO_IR DFS while beacon hint not allowed
    [    6.143131] RTW: band:5G ch56 is NO_IR DFS while beacon hint not allowed
    [    6.150650] RTW: band:5G ch60 is NO_IR DFS while beacon hint not allowed
    [    6.158170] RTW: band:5G ch64 is NO_IR DFS while beacon hint not allowed
    [    6.165692] RTW: band:5G ch100 is NO_IR DFS while beacon hint not allowed
    [    6.173324] RTW: band:5G ch104 is NO_IR DFS while beacon hint not allowed
    [    6.180919] RTW: band:5G ch108 is NO_IR DFS while beacon hint not allowed
    [    6.188519] RTW: band:5G ch112 is NO_IR DFS while beacon hint not allowed
    [    6.196143] RTW: band:5G ch116 is NO_IR DFS while beacon hint not allowed
    [    6.203743] RTW: band:5G ch120 is NO_IR DFS while beacon hint not allowed
    [    6.211360] RTW: band:5G ch124 is NO_IR DFS while beacon hint not allowed
    [    6.218978] RTW: band:5G ch128 is NO_IR DFS while beacon hint not allowed
    [    6.226592] RTW: band:5G ch132 is NO_IR DFS while beacon hint not allowed
    [    6.234243] RTW: band:5G ch136 is NO_IR DFS while beacon hint not allowed
    [    6.241855] RTW: band:5G ch140 is NO_IR DFS while beacon hint not allowed
    [    6.249483] RTW: band:5G ch144 is NO_IR DFS while beacon hint not allowed
    [    6.257098] RTW: rtw_rfctl_chset_apply_regulatory ch num:41
    [    6.264679] RTW: RM: rtw_init_rm
    [    6.268321] RTW: rtw_macaddr_cfg mac addr:40:55:48:45:16:0a
    [    6.274690] RTW: disable_interrupt: update SDIO HIMR=0
    [    6.280472] RTW: bDriverStopped:True, bSurpriseRemoved:False, bup:0, hw_init_completed:0
    [    6.289578] RTW: loadparam, Select P2P interface: iface_id:1
    [    6.296068] RTW: init_mlme_default_rate_set: support CCK
    [    6.302037] RTW: init_mlme_default_rate_set: support OFDM
    [    6.308159] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.316886] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.325574] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.334268] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.342983] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.351666] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.360368] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.369073] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.377761] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.386469] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.395161] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.403824] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.412525] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.421215] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.429899] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.438590] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(20992)
    [    6.447405] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(5632)
    [    6.456001] RTW: DBG_MEM_ALLOC rtw_os_xmit_resource_alloc:136 dbg_rtw_zmalloc(5632)
    [    6.464852] RTW: rtw_alloc_macid((null)) if2, mac_addr:ff:ff:ff:ff:ff:ff macid:1
    [    6.473195] RTW: RM: rtw_init_rm
    [    6.476833] RTW: rtw_drv_add_vir_if if2 mac_addr : 42:55:48:45:16:0a
    [    6.483968] RTW: rtw_cfg80211_init_wiphy_band:rf_type=0
    [    6.489880] RTW: [VHT] Declare supporting MAX MPDU len = 11454 bytes
    [    6.497013] RTW: [VHT] Declare supporting SGI 80MHz
    [    6.502491] RTW: [VHT] Declare supporting VHT variant HT Control
    [    6.509236] RTW: [VHT] Declare supporting RX A-MPDU Length Exponent = 7
    [    6.516684] RTW: rtw_wiphy_alloc(phy0)
    [    6.520912] RTW: rtw_wdev_alloc(padapter=(____ptrval____))
    [    6.527073] RTW: rtw_wdev_alloc(padapter=(____ptrval____))
    [    6.533247] RTW: rtw_wiphy_register(phy0)
    [    6.537740] RTW: Register RTW cfg80211 vendor cmd(0x67) interface
    [    6.545028] RTW: rtw_ndev_init(wlan0) if1 mac_addr=40:55:48:45:16:0a
    [    6.552563] RTW: rtw_ndev_notifier_call(wlan0) state:17
    [    6.559021] RTW: cfg80211_rtw_get_txpower(wlan0) total max: -10000 mbm
    [    6.566371] RTW: rtw_ndev_notifier_call(wlan0) state:5
    [    6.572180] RTW: rtw_ndev_init(p2p0) if2 mac_addr=42:55:48:45:16:0a
    [    6.579606] RTW: rtw_ndev_notifier_call(p2p0) state:17
    [    6.585883] RTW: cfg80211_rtw_get_txpower(p2p0) total max: -10000 mbm
    [    6.593117] RTW: rtw_ndev_notifier_call(p2p0) state:5
    [    6.598877] RTW: module init ret=0
    [    6.606185] axp2101-pek axp2101-pek.0: DMA mask not set
    [    6.616263] input: axp2202-pek as /devices/platform/soc@3000000/7083000.twi/i2c-7/7-0035/axp2101-pek.0/input/input22
    [    6.631198] core: _opp_supported_by_regulators: OPP minuV: 0 maxuV: 0, not supported by regulator
    [    6.641198] cpu cpu0: _opp_add: OPP not supported by regulators (1104000000)
    [    6.649393] core: _opp_supported_by_regulators: OPP minuV: 0 maxuV: 0, not supported by regulator
    [    6.659354] cpu cpu0: _opp_add: OPP not supported by regulators (1296000000)
    [    6.667437] core: _opp_supported_by_regulators: OPP minuV: 0 maxuV: 0, not supported by regulator
    [    6.677414] cpu cpu0: _opp_add: OPP not supported by regulators (1392000000)
    [    6.685731] core: _opp_supported_by_regulators: OPP minuV: 0 maxuV: 0, not supported by regulator
    [    6.695716] cpu cpu0: _opp_add: OPP not supported by regulators (1608000000)
    [    6.703767] core: _opp_supported_by_regulators: OPP minuV: 0 maxuV: 0, not supported by regulator
    [    6.713723] cpu cpu0: _opp_add: OPP not supported by regulators (1656000000)
    [    6.721812] core: _opp_supported_by_regulators: OPP minuV: 0 maxuV: 0, not supported by regulator
    [    6.731767] cpu cpu0: _opp_add: OPP not supported by regulators (1704000000)
    [    6.739802] core: _opp_supported_by_regulators: OPP minuV: 0 maxuV: 0, not supported by regulator
    [    6.749716] cpu cpu0: _opp_add: OPP not supported by regulators (1752000000)
    [    6.757849] cpu cpu0: EM: created perf domain
    [    6.765320] sunxi-msgbox 3003000.msgbox: sunxi:sunxi_msgboxsunxi_msgbox_probe(): sunxi msgbox start probe
    [    6.776252] sunxi-msgbox 3003000.msgbox: sunxi:sunxi_msgboxsunxi_msgbox_probe(): sunxi msgbox probe success
    [    6.787229] sunxi-msgbox 3600000.msgbox_core0: sunxi:sunxi_msgboxsunxi_msgbox_probe(): sunxi msgbox start probe
    [    6.798707] sunxi-msgbox 3600000.msgbox_core0: sunxi:sunxi_msgboxsunxi_msgbox_probe(): sunxi msgbox probe success
    [    6.810864] sunxi-rproc 1a00000.e907_rproc: sunxi rproc driver 2.4.3
    [    6.818063] sunxi-rproc 1a00000.e907_rproc: rv-cfg base: 0x01a00000, va: 0xffffffc011e3d000
    [    6.827463] sunxi-rproc 1a00000.e907_rproc: memstore num: 0
    [    6.833785] sunxi-rproc 1a00000.e907_rproc: e907 standby init end
    [    6.840904] sunxi_rproc_stdby_dev_init remoteproc0
    [    6.846324] sunxi-rproc 1a00000.e907_rproc: is_using_kernel_fw: 0
    [    6.853192] remoteproc remoteproc0: e907_rproc is available
    [    6.859494] sunxi-rproc 1a00000.e907_rproc: sunxi rproc driver probe ok
    [    6.867069] sunxi-rproc soc@3000000:a55_rproc@0: sunxi rproc driver 2.4.3
    [    6.874661] sunxi-rproc soc@3000000:a55_rproc@0: failed to get firmware-name
    [    6.882558] sunxi-rproc soc@3000000:a55_rproc@0: find rproc priv error
    [    6.889852] sunxi-rproc soc@3000000:a55_rproc@0: Failed to get resource
    [    6.897245] remoteproc remoteproc1: releasing a55_rproc
    [    6.903091] sunxi-rproc: probe of soc@3000000:a55_rproc@0 failed with error -22
    [    6.911909] sunxi-rfkill soc@3000000:rfkill: module version: v1.1.5
    [    6.918956] sunxi-rfkill soc@3000000:rfkill: pinctrl_lookup_state(default) failed! return ffffffffffffffed 
    [    6.929856] sunxi-rfkill soc@3000000:rfkill: get gpio chip_en failed
    [    6.936959] sunxi-rfkill soc@3000000:rfkill: get gpio power_en failed
    [    6.944292] sunxi-rfkill soc@3000000:rfkill: wlan_busnum (1)
    [    6.950769] sunxi-rfkill soc@3000000:rfkill: wlan power[0] (axp2202-dcdc4) voltage: 3300mV
    [    6.960137] sunxi-rfkill soc@3000000:rfkill: wlan power[1] (axp2202-bldo1) voltage: 1800mV
    [    6.969475] sunxi-rfkill soc@3000000:rfkill: wlan power[2] (axp2202-bldo2) voltage: 1800mV
    [    6.978730] sunxi-rfkill soc@3000000:rfkill: wlan clock[0] (dcxo24M-out)
    [    6.986255] sunxi-rfkill soc@3000000:rfkill: wlan clock[1] (osc32k-out)
    [    6.993669] sunxi-rfkill soc@3000000:rfkill: wlan_regon gpio=385 assert=1
    [    7.001266] sun55iw6-r-pinctrl 7096000.pinctrl: pin PM1 already requested by 7081000.uart; cannot claim for 7096000.pinctrl:385
    [    7.014094] sun55iw6-r-pinctrl 7096000.pinctrl: pin-385 (7096000.pinctrl:385) status -22
    [    7.023139] sunxi-rfkill soc@3000000:rfkill: can't request wlan_regon gpio 385
    [    7.031347] sunxi-rfkill: probe of soc@3000000:rfkill failed with error -22
    [    7.039576] [ADDR_MGT] addr_mgt_probe: module version: v1.0.12
    [    7.046778] sunxi:sunxi_sidget_soc_ver_regs() +267: Failed to find "soc_bin" in dts.
    [    7.055616] [ADDR_MGT] addr_mgt_probe: success.
    [    7.061779] -----*clock freq is 40000000*----
    [    7.067295] sunxi-can 453c800.can: PM runtime resume.
    [    7.073307] sunxi-can 453c800.can: sunxican device registered (irq=59, version=33)
    [    7.081836] sunxi-can 453c800.can: PM runtime suspend.
    [    7.088115] -----*clock freq is 40000000*----
    [    7.093603] sunxi-can 4541800.can: PM runtime resume.
    [    7.099575] sunxi-can 4541800.can: sunxican device registered (irq=62, version=33)
    [    7.108046] sunxi-can 4541800.can: PM runtime suspend.
    [    7.114268] -----*clock freq is 40000000*----
    [    7.119756] sunxi-can 4546800.can: PM runtime resume.
    [    7.125702] sunxi-can 4546800.can: sunxican device registered (irq=65, version=33)
    [    7.134174] sunxi-can 4546800.can: PM runtime suspend.
    [    7.140351] -----*clock freq is 40000000*----
    [    7.145838] sunxi-can 454b800.can: PM runtime resume.
    [    7.151778] sunxi-can 454b800.can: sunxican device registered (irq=68, version=33)
    [    7.160250] sunxi-can 454b800.can: PM runtime suspend.
    [    7.166809] IPVS: Registered protocols ()
    [    7.171372] IPVS: Connection hash table configured (size=4096, memory=32Kbytes)
    [    7.179663] IPVS: ipvs loaded.
    [    7.183457] NET: Registered protocol family 10
    [    7.189356] Segment Routing with IPv6
    [    7.193570] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
    [    7.200585] NET: Registered protocol family 17
    [    7.205574] NET: Registered protocol family 15
    [    7.210612] Bridge firewalling registered
    [    7.215127] can: controller area network core
    [    7.220085] NET: Registered protocol family 29
    [    7.225060] can: raw protocol
    [    7.228383] can: broadcast manager protocol
    [    7.233065] can: netlink gateway - max_hops=1
    [    7.238118] Bluetooth: RFCOMM TTY layer initialized
    [    7.243607] Bluetooth: RFCOMM socket layer initialized
    [    7.249374] Bluetooth: RFCOMM ver 1.11
    [    7.253796] Loading compiled-in X.509 certificates
    [    7.276525] sunxi-twi 2512000.twi: supply twi not found, using dummy regulator
    [    7.285626] sunxi:twi-2512000.twi:[INFO]: v2.7.6 probe success
    [    7.292694] sunxi-twi 2513000.twi: supply twi not found, using dummy regulator
    [    7.303874] es8328 3-0011: supply DVDD not found, using dummy regulator
    [    7.311379] es8328 3-0011: supply AVDD not found, using dummy regulator
    [    7.318849] es8328 3-0011: supply PVDD not found, using dummy regulator
    [    7.326294] es8328 3-0011: supply HPVDD not found, using dummy regulator
    [    7.333882] sunxi:twi-2513000.twi:[INFO]: v2.7.6 probe success
    [    7.340680] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    7.350478] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    7.360210] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    7.369925] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    7.379637] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    7.389362] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    7.399081] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    7.408796] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    7.418505] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    7.428214] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    7.438689] input: gpio-keys as /devices/platform/gpio-keys/input/input23
    [    7.446565] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    7.447925] sunxi:sound-common:[ERR]: 301 pacfg_level_trig_init(): pa-pin-0 (9) request failed
    [    7.456378] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    7.465739] sunxi:sound-common:[ERR]: 612 snd_sunxi_pa_pin_init(): pacfg_level_trig_init failed
    [    7.475431] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    7.485586] sunxi:sound-aa:[WARN]: 110 sunxi_aaudio_parse_dma_param(): capture-cma missing, using default value
    [    7.494678] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    7.505771] sunxi:sound-aa:[WARN]: 132 sunxi_aaudio_parse_dma_param(): rx-fifo-size miss,using default value
    [    7.505776] sunxi:sound-aa:[WARN]: 150 sunxi_aaudio_parse_dma_param(): adc-txdata miss, no aaudio platform
    [    7.506897] sunxi:sound-i2s:[WARN]: 2206 snd_sunxi_dts_params_init(): clk-en-post-delay missing
    [    7.515523] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    7.526293] sunxi:sound-i2s:[WARN]: 2214 snd_sunxi_dts_params_init(): clk-keep missing
    [    7.537248] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    7.547685] sunxi:sound-i2s:[WARN]: 2206 snd_sunxi_dts_params_init(): clk-en-post-delay missing
    [    7.556512] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    7.565168] sunxi:sound-i2s:[WARN]: 2214 snd_sunxi_dts_params_init(): clk-keep missing
    [    7.566000] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    7.574902] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    7.584777] debugfs: Directory 'soc@3000000:codec_plat' with parent 'audiocodec' already present!
    [    7.594144] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    7.603393] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    7.612430] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    7.621821] sunxi-snd-mach soc@3000000:i2s1_mach: No 'sound-dai' property
    [    7.631879] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    7.641413] debugfs: Directory '2033000.i2s1_plat' with parent 'sndi2s1' already present!
    [    7.650845] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    7.660840] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    7.667955] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    7.678804] debugfs: Directory '2034000.i2s2_plat' with parent 'sndi2s2' already present!
    [    7.686680] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    7.733762] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    7.743474] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    7.753188] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    7.803653] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    7.813447] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    7.813528] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    7.822946] sunxi:sound-mach:[ERR]: 488 simple_parse_of(): simple_dai_link_of failed
    [    7.832599] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    7.842494] sunxi-ehci 4200000.ehci1-controller: supply hci not found, using dummy regulator
    [    7.850883] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    7.860170] sunxi-ehci 4200000.ehci1-controller: supply vbusin not found, using dummy regulator
    [    7.869758] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    7.880782] sunxi-ehci 4200000.ehci1-controller: EHCI Host Controller
    [    7.889018] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    7.896028] sunxi-ehci 4200000.ehci1-controller: new USB bus registered, assigned bus number 1
    [    7.905730] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    7.915277] sunxi-ehci 4200000.ehci1-controller: irq 110, io mem 0x04200000
    [    7.925007] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    7.941940] sunxi:sound-mach:[ERR]: 488 simple_parse_of(): simple_dai_link_of failed
    [    7.946846] sunxi-ehci 4200000.ehci1-controller: USB 2.0 started, EHCI 1.00
    [    7.950695] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    7.958523] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.10
    [    7.977165] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [    7.985238] usb usb1: Product: EHCI Host Controller
    [    7.990686] usb usb1: Manufacturer: Linux 5.10.198 ehci_hcd
    [    7.996914] usb usb1: SerialNumber: sunxi-ehci
    [    8.002326] hub 1-0:1.0: USB hub found
    [    8.006557] hub 1-0:1.0: 1 port detected
    [    8.011180] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    8.020920] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    8.022531] sunxi-ohci 4200400.ohci1-controller: supply hci not found, using dummy regulator
    [    8.030688] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    8.040067] sunxi-ohci 4200400.ohci1-controller: supply vbusin not found, using dummy regulator
    [    8.049625] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    8.059549] sunxi-ohci 4200400.ohci1-controller: OHCI Host Controller
    [    8.068985] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    8.075884] sunxi-ohci 4200400.ohci1-controller: new USB bus registered, assigned bus number 2
    [    8.076008] sunxi-ohci 4200400.ohci1-controller: irq 111, io mem 0x04200400
    [    8.085331] sunxi:sound-mach:[ERR]: 488 simple_parse_of(): simple_dai_link_of failed
    [    8.111477] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    8.121190] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    8.130918] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    8.158971] usb usb2: New USB device found, idVendor=1d6b, idProduct=0001, bcdDevice= 5.10
    [    8.168213] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
    [    8.176283] usb usb2: Product: OHCI Host Controller
    [    8.181733] usb usb2: Manufacturer: Linux 5.10.198 ohci_hcd
    [    8.187956] usb usb2: SerialNumber: sunxi-ohci
    [    8.193372] hub 2-0:1.0: USB hub found
    [    8.197596] hub 2-0:1.0: 1 port detected
    [    8.202227] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    8.203881] sun55iw6-r-pinctrl 7096000.pinctrl: pin PL10 already requested by 7080000.uart; cannot claim for 7096000.pinctrl:362
    [    8.212061] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    8.224742] sun55iw6-r-pinctrl 7096000.pinctrl: pin-362 (7096000.pinctrl:362) status -22
    [    8.234579] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    8.244151] cfg80211: Loading compiled-in X.509 certificates for regulatory database
    [    8.252712] sunxi:sound-mach:[ERR]: 488 simple_parse_of(): simple_dai_link_of failed
    [    8.265727] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
    [    8.270229] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    8.277398] platform regulatory.0: Direct firmware load for regulatory.db failed with error -2
    [    8.279105] ALSA device list:
    [    8.279111]   #0: audiocodec
    [    8.279114]   #1: sndi2s1
    [    8.279117]   #2: sndi2s2
    [    8.287160] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    8.296469] cfg80211: failed to load regulatory.db
    [    8.323968] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    8.333728] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    8.343469] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    8.353322] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    8.362771] sunxi:sound-mach:[ERR]: 488 simple_parse_of(): simple_dai_link_of failed
    [    8.374847] usb 1-1: new high-speed USB device number 2 using sunxi-ehci
    [    8.375706] EXT4-fs (mmcblk0p5): INFO: recovery required on readonly filesystem
    [    8.390567] EXT4-fs (mmcblk0p5): write access will be enabled during recovery
    [    8.402028] EXT4-fs (mmcblk0p5): recovery complete
    [    8.407806] EXT4-fs (mmcblk0p5): mounted filesystem with ordered data mode. Opts: (null)
    [    8.416922] VFS: Mounted root (ext4 filesystem) readonly on device 179:5.
    [    8.426458] Freeing unused kernel memory: 5056K
    [    8.431695] Run /init as init process
    [    8.435799]   with arguments:
    [    8.439113]     /init
    [    8.441661]   with environment:
    [    8.445171]     HOME=/
    [    8.447803]     TERM=linux
    [    8.450824]     partitions=boot-resource@mmcblk0p1:env@mmcblk0p2:boot@mmcblk0p3:private@mmcblk0p4:rootfs@mmcblk0p5:UDISK@mmcblk0p6
    [    8.463941]     snum=3c000c6d570147d1d51
    [    8.468327]     mac_addr=
    [    8.471251]     wifi_mac=
    [    8.474174]     bt_mac=
    [    8.476904]     selinux=
    [    8.479732]     specialstr=
    [    8.482853]     ion_carveout_list=
    [    8.486644]     boot_type=2
    [    8.489761]     uboot_message=2023.04-rc4
    [    8.494246]     mbr_offset=20971520
    [    8.535830] EXT4-fs (mmcblk0p5): re-mounted. Opts: (null)
    [    8.543515] usb 1-1: New USB device found, idVendor=1a86, idProduct=8091, bcdDevice=13.40
    [    8.552721] usb 1-1: New USB device strings: Mfr=0, Product=2, SerialNumber=0
    [    8.560721] usb 1-1: Product: USB HUB
    [    8.565607] hub 1-1:1.0: USB hub found
    [    8.570030] hub 1-1:1.0: 4 ports detected
    [    8.576087] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    8.586039] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    8.595974] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    8.605918] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    8.615843] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    8.625972] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    8.635493] sunxi:sound-mach:[ERR]: 488 simple_parse_of(): simple_dai_link_of failed
    [    8.668905] udevd[160]: starting version 3.2.11
    [    8.678314] random: udevd: uninitialized urandom read (16 bytes read)
    [    8.686133] random: udevd: uninitialized urandom read (16 bytes read)
    [    8.693413] random: udevd: uninitialized urandom read (16 bytes read)
    [    8.703051] udevd[160]: specified group 'input' unknown
    [    8.709462] udevd[160]: specified group 'kvm' unknown
    [    8.723773] udevd[160]: specified group 'xenomai' unknown
    [    8.731910] udevd[162]: starting eudev-3.2.11
    [    8.831086] npu[a5][a5] vipcore, platform driver init
    [    8.836770] npu[a5][a5] vipcore, insmod param cpu_physical=0x0
    [    8.845180] npu[a5][a5] vipcore, insmod param cpu_physical=0x0
    [    8.854974] npu[a5][a5] vipcore, insmod param cpu_physical=0x0
    [    8.861539] npu[a5][a5] vipcore, insmod param cpu_physical=0x0
    [    8.868118] usb 1-1.1: new high-speed USB device number 3 using sunxi-ehci
    [    8.875876] npu[a5][a5] vipcore, platform device compatible=allwinner,npu
    [    8.883960] npu[a5][a5] vipcore, platform driver device=0xffffff8002cfc010
    [    8.891733] npu[a5][a5] vipcore irq number is 74.
    [    8.897018] vipdrv_drv_adjust_param 825 SUCCESS
    [    8.902137] NPU AXI CLK NULL
    [    8.905423] NPU AHB CLK NULL
    [    8.910459] npu[a5][a5] EXTRA: 0xfa5a, SID: 0x1, max_freq: 0, default_freq: 0
    [    8.926103] npu[a5][a5] current vf index: 100
    [    8.931727] npu[a5][a5] Supported vf list: 
    [    8.937563] npu[a5][a5] Don`t Set NPU regulator!
    [    8.945569] npu[a5][a5] vipcore, device_cnt=1, core_cnt=1
    [    8.952617] npu[a5][a5] core_0, request irqline=74, name=vipcore_0
    [    8.960062] npu[a5][a5] vipcore, allocate page for video memory, size: 0x400000 bytes
    [    8.969367] npu[a5][a5] vipcore, heap_cnt=0, reserved video memory cpu_phy=0x45800000, vip_phy=0x45800000, size=0x400000
    [    8.987057] npu[a5][a5] VIPLite driver version 2.0.3.1-AW-2024-11-07
    [    8.995574] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    9.006669] usb 1-1.1: New USB device found, idVendor=1a86, idProduct=8091, bcdDevice=13.40
    [    9.018654] usb 1-1.1: New USB device strings: Mfr=0, Product=2, SerialNumber=0
    [    9.029108] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    9.041050] usb 1-1.1: Product: USB HUB
    [    9.046546] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    9.057743] hub 1-1.1:1.0: USB hub found
    [    9.063694] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    9.073482] hub 1-1.1:1.0: 4 ports detected
    [    9.091355] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    9.119390] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    9.130004] sunxi:sound-mach:[ERR]: 488 simple_parse_of(): simple_dai_link_of failed
    [    9.139071] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    9.148945] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    9.158700] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    9.168594] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    9.309471] sunxi-can 453c800.can: PM runtime resume.
    [    9.315172] sunxi-can 453c800.can: PM runtime suspend.
    [    9.321187] sunxi-can 4541800.can: PM runtime resume.
    [    9.327048] sunxi-can 4541800.can: PM runtime suspend.
    [    9.333073] sunxi-can 4546800.can: PM runtime resume.
    [    9.338878] sunxi-can 4546800.can: PM runtime suspend.
    [    9.344782] sunxi-can 454b800.can: PM runtime resume.
    [    9.350502] sunxi-can 454b800.can: PM runtime suspend.
    [    9.423744] file system registered
    [    9.456671] read descriptors
    [    9.459928] read strings
    [    9.527380] FAT-fs (mmcblk0p6): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
    [    9.563717] FAT-fs (mmcblk0p6): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
    [    9.672644] Sitronix TDDI Touch Driver v43.00.250117
    [    9.678348] i2c addr: 0x55
    [    9.681429] sitronix_ts_i2c_parse_dt: Interrupt GPIO = 0. (flag=0) , request ret = 0
    [    9.690103] sitronix_ts_i2c_parse_dt: Reset GPIO = 1. (flag=1), request ret = 0
    [    9.698883] reg-virt-consumer reg-virt-consumer.3.auto: Failed to obtain supply 'aldo1': -517
    [    9.700810] sitronix_ts_probe:815 
    [    9.708891] sunxi:sound-mach:[WARN]: 372 asoc_simple_parse_ucfmt(): set data late to default
    [    9.712251] start of sitronix_ts_probe
    [    9.712261] sitronix_ts_reset_device: Hardware Reset device.
    [    9.721699] sunxi:sound-mach:[ERR]: 488 simple_parse_of(): simple_dai_link_of failed
    [    9.741007] reg-virt-consumer reg-virt-consumer.4.auto: Failed to obtain supply 'dldo1': -517
    [    9.750784] reg-virt-consumer reg-virt-consumer.0.auto: Failed to obtain supply 'dcdc1': -517
    [    9.760526] reg-virt-consumer reg-virt-consumer.1.auto: Failed to obtain supply 'dcdc2': -517
    [    9.770264] reg-virt-consumer reg-virt-consumer.2.auto: Failed to obtain supply 'dcdc3': -517
    [    9.846898] sunxi:twi-2512000.twi:[ERR]: drv-mode: Timeout when sending 9th SCL clk
    [    9.855463] sunxi:twi-2512000.twi:[ERR]: drv mode: TWI BUS error state is drv:0x1 eng:0x20
    [    9.864715] sunxi:twi-2512000.twi:[ERR]: drv-mode: xfer failed (dev addr:0x28)
    [    9.872806] sitronix_ts_i2c_awrite: I2C retry 1
    [    9.902842] sitronix_ts_i2c_awrite: I2C write over retry limit
    [    9.909417] sunxi:twi-2512000.twi:[ERR]: drv-mode: Timeout when sending 9th SCL clk
    [    9.917977] sunxi:twi-2512000.twi:[ERR]: drv mode: TWI BUS error state is drv:0x1 eng:0x20
    [    9.927234] sunxi:twi-2512000.twi:[ERR]: drv-mode: xfer failed (dev addr:0x28)
    [    9.935315] sitronix_ts_i2c_awrite: I2C retry 1
    [    9.966841] sitronix_ts_i2c_awrite: I2C write over retry limit
    [    9.973407] sunxi:twi-2512000.twi:[ERR]: drv-mode: Timeout when sending 9th SCL clk
    [    9.981967] sunxi:twi-2512000.twi:[ERR]: drv mode: TWI BUS error state is drv:0x1 eng:0x20
    [    9.991249] sunxi:twi-2512000.twi:[ERR]: drv-mode: xfer failed (dev addr:0x28)
    [    9.999330] sitronix_ts_i2c_awrite: I2C retry 1
    [   10.030841] sitronix_ts_i2c_awrite: I2C write over retry limit
    [   10.037407] sunxi:twi-2512000.twi:[ERR]: drv-mode: Timeout when sending 9th SCL clk
    [   10.045967] sunxi:twi-2512000.twi:[ERR]: drv mode: TWI BUS error state is drv:0x1 eng:0x20
    [   10.055223] sunxi:twi-2512000.twi:[ERR]: drv-mode: xfer failed (dev addr:0x28)
    [   10.063309] sitronix_ts_i2c_aread: I2C retry 1
    [   10.094841] sitronix_ts_i2c_aread: I2C read over retry limit
    [   10.101165] myzr get id = 0x0, off = 0
    [   10.105361] sitronix_ts_check_ic_sfrver: read id error (0)
    [   10.111493] sitronix_ts_probe: Failed to sitronix_ts_check_ic_sfrver
    [   10.118597] Error occurred while unregistering fb_notifier.
    [   10.124825] sitronix_mt_stop
    [   10.128060] sitronix_ts_i2c: probe of sitronix_ts_i2c.0 failed with error -22
    [   10.145673] sunxi:uart-ng-uart-ng0:[WARN]: dts not support rs485 mode or                          rs485conf.flags = 0 not support
    Trying to connect to SWUpdate...
    
    Welcome to Allwinner Longan Platform
    Longan login: 
    Welcome to Allwinner Longan Platform
    Longan login: 



U-Boot Information
~~~~~~~~~~~~~~~~~~~~~

|   The startup information line **U-Boot 2023.04-rc4 (Nov 24 2026 - 04:04:18 +0000) Allwinner Technology** contains the following details:

- [U-Boot Version]: 2023.04
- [Source Code Version]: rc4
- [U-Boot File Compilation Time]: Nov 24 2026 - 04:04:18 +0000

Kernel Information
~~~~~~~~~~~~~~~~~~~~~
|   The startup information line **Linux version 5.10.198 (linyn@myzr-u2204) (aarch64-none-linux-gnu-gcc (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 10.3.1 20210621, GNU ld (GNU Toolchain for the A-profile Architecture 10.3-2021.07 (arm-10.29)) 2.36.1.20210621) #23 SMP PREEMPT Wed Nov 25 11:07:31 UTC 2026** contains the following details:

- [Kernel Version]: Linux- 5.10.198
- [GCC Version for Kernel Compilation]: 10.3.1
- [Kernel File Compilation Time]: Wed Nov 25 11:07:31 UTC 2026

Development Board Login
~~~~~~~~~~~~~~~~~~~~~~~~~~

|   After the system starts up, when the message **Longan login:** is displayed, you can log in with the following credentials:

- [Username]: root
- [Password]: None

|   **Tip**: After logging in, you can use the "passwd" command to set or modify the password.