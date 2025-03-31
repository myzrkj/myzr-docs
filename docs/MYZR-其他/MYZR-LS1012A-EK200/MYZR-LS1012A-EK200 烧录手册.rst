MYZR-LS1012A-EK200 烧录手册
=============================

安装和配置烧录工具
------------------

**安装烧录工具**

|   打开工具目录，双击CW_ARMv8_v2019.01_b190130_Win_Offline.exe进行安装，安装路径和配置默认选择。

**复制rcw和uboot镜像到烧录工具目录**

|   复制rcw_800.bin.swapped和ls1012a-ek200-uboot.bin到目录C:\Freescale\CW4NET_v2019.01\CW_ARMv8\ARMv8\gdb\bin。

**配置烧录工具脚本文件**

1. 打开文件C:\Freescale\CW4NET_v2019.01\CW_ARMv8\ARMv8\gdb_extensions\flash\cwflash.py
2. 修改文件中的内容： 

.. code::shell

   。。。
   PROBE_CONNECTION = "cmsisdap"
   。。。
   FLASH_TYPE = "qspi"
   。。。
   SOC_NAME = "LS1012A"
   。。。
   JTAG_SPEED = 6000
   。。。

开发板烧录rcw和uboot镜像
-------------------------

**使开发板处于下载模式**

|   找到开发板上的 BOOTMODE 或 BOOT SWITCH 所指示的二位拨码开关，1拨到ON，2拨到OFF。

**连接开发板和电脑**

1. 打开电源，插上K20-JTAG模块到开发板，另外一端连接通过MINI USB线连接到电脑。
2. 双击工具目录下的mbedWinSerial_16466.exe进行驱动的安装。
3. 安装好后，打开电脑的设备管理器可看到如下图的相应的端口。

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012-com.png
   :alt: LS1012-com.png

**烧录rcw和uboot镜像到开发板**

1. 双击“C:\Freescale\CW4NET_v2019.01\CW_ARMv8\ARMv8\gdb\bin\aarch64-fsl-gdb.bat”。
2. 弹出命令窗口，输入命令：source ../../gdb_extensions/flash/cwflash.py

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012-win.jpg
   :alt: LS1012-win.jpg

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012-win2.jpg
   :alt: LS1012-win2.jpg

3. 依次输入一下命令：

.. code-block:: shell

   fl_unprotect 0x0 0x4000000
   fl_write 0x0 rcw_800.bin.swapped --erase --force
   fl_write 0x100000 u-boot.bin --erase
   quit

.. figure:: /image/MYZR-其他/MYZR-LS1012A-EK200/LS1012-win3.jpg
   :alt: LS1012-win3.jpg

4. 烧录好后，开发板关电，拔掉USB线，设置拨码为启动模式，1拨到OFF，2拨到ON。

开发板烧录ppa，uImage，dtb和文件系统
-------------------------------------

**tftpd软件下载和使用**

1. 网上下载tftpd64软件。
2. 打开软件，打击Browse选择镜像文件所在的目录

`注意：目录包含的文件：u-boot.bin，ppa.itb，rcw_800.bin.swapped`
`firmware-4.4.98.tar.bz2，kernel-4.4.98.tar.bz2，modules-4.4.98.tar.bz2，ramsys.itb，rootfs_jethro.tar.bz2，rootfs_jethro_config.tar.bz2，rootfs_jethro_update.tar.bz2和system_recovery.sh`

**烧录ppa**

1. 电脑插上网线连接开发板网口，设置电脑以太网IP：192.168.137.1。
2. 重启开发板，进入uboot命令行。
3. 输入命令：

.. code-block:: shell

   =====> Input:
   setenv ipaddr 192.168.137.81  
   setenv serverip 192.168.137.1  
   setenv ethaddr 00:00:00:00:00:03  
   ping 192.168.137.1  

   =====> Output: 
   => setenv ipaddr 192.168.137.81
   => setenv serverip 192.168.137.1
   => setenv ethaddr 00:00:00:00:00:03
   => ping 192.168.137.1 
   Speed detected 3e8
   Using pfe_eth0 device
   host 192.168.137.99 is alive

4. ping通后，输入命令：

.. code-block:: shell

   =====> Input:
   setenv update_ppa 'tftp 0x96000000 ppa.itb;sf probe 0:0; sf erase 0x500000 +$filesize; sf write 0x96000000 0x500000 $filesize;'
   run update_ppa  

   =====> Output: 
   => setenv update_ppa 'tftp 0x96000000 ppa.itb;sf probe 0:0; sf erase 0x500000 +$filesize; sf write 0x96000000 0x500000 $filesize;'
   => run update_ppa 
   Speed detected 3e8
   Using pfe_eth0 device
   TFTP from server 192.168.137.1; our IP address is 192.168.137.81
   Filename 'ppa.itb'.
   Load address: 0x96000000
   Loading: #######
        5.7 MiB/s
   done
   Bytes transferred = 89027 (15bc3 hex)
   SF: Detected S25FS512S with page size 256 Bytes, erase size 256 KiB, total 64 MiB
   SF: 262144 bytes @ 0x500000 Erased: OK
   device 0 offset 0x500000, size 0x15bc3
   SF: 89027 bytes @ 0x500000 Written: OK

更新内核，设备树，模块和文件系统
--------------------------------

**tftp更新方法**

1. 加载ramdisk系统启动

.. code-block:: shell

   =====> Input:
   run bootcmd_tftp 

   =====> Output: 
   Speed detected 3e8
   Using pfe_eth0 device
   TFTP from server 192.168.137.1; our IP address is 192.168.137.81
   Filename 'ramsys.itb'.
   Load address: 0x96000000
   Loading: #################################################################

2. 开发板启动完毕后，输入命令：

.. code-block:: shell

   =====> Input:
   $ root
   $ ifconfig eth0 192.168.137.81
   $ tftp -gr system_recovery.sh 192.168.137.1
   $ chmod +x system_recovery.sh
   $ ./system_recovery.sh tftp   

   =====> Output: 
   ls1012a-ek200 login: root
   root@ls1012a-ek200:~# ifconfig
   lo        Link encap:Local Loopback  
             inet addr:127.0.0.1  Mask:255.0.0.0
             inet6 addr: ::1/128 Scope:Host
             UP LOOPBACK RUNNING  MTU:65536  Metric:1
             RX packets:0 errors:0 dropped:0 overruns:0 frame:0
             TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:0 
             RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

   root@ls1012a-ek200:~# ifconfig eth0 192.168.137.81
   root@ls1012a-ek200:~# tftp -gr system_recovery.sh 192.168.137.1
   system_recovery.sh   100% |*******************************************************************************************************|  2282   0:00:00 ETA
   root@ls1012a-ek200:~# chmod +x system_recovery.sh 
   root@ls1012a-ek200:~# ./system_recovery.sh tftp
   ========>> sfdisk - manipulate a disk partition table
   umount: /dev/mmcblk0: not mounted
   Checking that no-one is using this disk right now ... OK

   Disk /dev/mmcblk0: 3.7 GiB, 3909091328 bytes, 7634944 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disklabel type: dos
   Disk identifier: 0x7283ff12

   Old situation:

   Device         Boot   Start     End Sectors  Size Id Type
   /dev/mmcblk0p1         2048 1026047 1024000  500M  c W95 FAT32 (LBA)
   /dev/mmcblk0p2      1026048 7634943 6608896  3.2G 83 Linux

   >>> Created a new DOS disklabel with disk identifier 0x16b893a9.
   Created a new partition 1 of type 'W95 FAT32 (LBA)' and of size 500 MiB.
   /dev/mmcblk0p2: Created a new partition 2 of type 'Linux' and of size 3.2 GiB.
   /dev/mmcblk0p3: 
   New situation:

   Device         Boot   Start     End Sectors  Size Id Type
   /dev/mmcblk0p1         2048 1026047 1024000  500M  c W95 FAT32 (LBA)
   /dev/mmcblk0p2      1026048 7634943 6608896  3.2G 83 Linux

   The partition table has been altered.
   Calling ioctl() to re-read partition table.
   Syncing disks.
   ========>> mkfs.fat - create an MS-DOS filesystem under Linux
   umount: /dev/mmcblk0p1: not mounted
   mkfs.fat 3.0.28 (2015-05-16)
   umount: /dev/mmcblk0p2: not mounted
   ========>> mke2fs - create an ext4 filesystem
   mke2fs 1.42.9 (28-Dec-2013)
   Filesystem label=
   OS type: Linux
   Block size=4096 (log=2)
   Fragment size=4096 (log=2)
   Stride=0 blocks, Stripe width=0 blocks
   206752 inodes, 826112 blocks
   41305 blocks (5.00%) reserved for the super user
   First data block=0
   Maximum filesystem blocks=847249408
   26 block groups
   32768 blocks per group, 32768 fragments per group
   7952 inodes per group
   Superblock backups stored on blocks: 
       32768, 98304, 163840, 229376, 294912, 819200

   Allocating group tables: done                            
   Writing inode tables: done                            
   Creating journal (16384 blocks): done
   Writing superblocks and filesystem accounting information: done 

   ========>> Start system recovery
   ========>> Transfer system files
   rootfs_jethro.tar.bz 100% |*******************************************************************************************************| 32161k  0:00:00 ETA
   rootfs_jethro_update 100% |*******************************************************************************************************|  6391k  0:00:00 ETA
   rootfs_jethro_config 100% |*******************************************************************************************************|   314k  0:00:00 ETA
   kernel-4.4.98.tar.bz 100% |*******************************************************************************************************|  7673k  0:00:00 ETA
   modules-4.4.98.tar.b 100% |*******************************************************************************************************| 15029k  0:00:00 ETA
   firmware-4.4.98.tar. 100% |*******************************************************************************************************| 26012   0:00:00 ETA
   system_recovery.sh   100% |*******************************************************************************************************|  2282   0:00:00 ETA
   ramsys.itb           100% |*******************************************************************************************************| 54211k  0:00:00 ETA
   ========>> Updating... rootfs_jethro.tar.bz2
   ========>> Updating... rootfs_jethro_update.tar.bz2
   ========>> Updating... rootfs_jethro_config.tar.bz2
   ========>> System recovery complete

   The system is going down for reboot NOW!0 (ttyS0) (Tue Aug 20 04:00:39 2019):
   INIT: Sending processes the TERM signal
   INIT: SStopping system message bus: dbus.
   Stopping HOSTAP Daemon: no /usr/sbin/hostapd found; none killed
   hostapd.
   Stopping system log daemon...0
   Stopping kernel log daemon...0
   Stopping internet superserver: xinetd.
   Deconfiguring network interfaces... done.
   Sending all processes the TERM signal...
   Sending all processes the KILL signal...
   Unmounting remote filesystems...
   Deactivating swap...
   Unmounting local filesystems...
   Rebooting... Press Enter for maintenance(or press Control-D to continue): 

**U盘更新**

1. 加载ramdisk启动

.. code-block:: shell

   =====> Input:
   usb start
   run bootargs_ram; run load_itb_usb; pfe stop; bootm ${loadaddr_itb}; 

   =====> Output: 
   => usb start
   starting USB...
   USB0:   Register 200017f NbrPorts 2
   Starting the controller
   USB XHCI 1.00
   scanning bus 0 for devices... Device not responding to set address.

         USB device not accepting new address (error=80000000)
   3 USB Device(s) found
          scanning usb for storage devices... 1 Storage Device(s) found

   => run bootargs_ram; run load_itb_usb; pfe stop; bootm ${loadaddr_itb}; 
   reading ramsys.itb
   55512815 bytes read in 32071 ms (1.6 MiB/s)
   Stopping PFE... 
   ## Loading kernel from FIT Image at 96000000 ...
      Using 'config@1' configuration
      Trying 'kernel@1' kernel subimage
      Description:  ARM64 Linux kernel

2. 开发板启动完毕后，输入命令：

.. code-block:: shell

   =====> Input:
   $ root
   $ df
   $ cd /run/media/sda1/
   $ chmod +x system_recovery.sh
   $ ./system_recovery.sh usb

   =====> Output: 
   ls1012a-ek200 login: root
   root@ls1012a-ek200:~# df  
   Filesystem     1K-blocks   Used Available Use% Mounted on
   /dev/root        3186960 177372   2827984   6% /
   devtmpfs          195628      4    195624   1% /dev
   tmpfs             204204    228    203976   1% /run
   tmpfs             204204    184    204020   1% /var/volatile
   /dev/mmcblk0p1    511720 133864    377856  27% /run/media/mmcblk0p1
   /dev/sda1         519392 116496    402896  23% /run/media/sda1
   root@ls1012a-ek200:~# cd /run/media/sda1/
   root@ls1012a-ek200:/run/media/sda1# chmod +x system_recovery.sh 
   root@ls1012a-ek200:/run/media/sda1# ./system_recovery.sh usb
   ========>> sfdisk - manipulate a disk partition table
   umount: /dev/mmcblk0: not mounted
   Checking that no-one is using this disk right now ... FAILED

   This disk is currently in use - repartitioning is probably a bad idea.
   Umount all file systems, and swapoff all swap partitions on this disk.
   Use the --no-reread flag to suppress this check.

   Disk /dev/mmcblk0: 3.7 GiB, 3909091328 bytes, 7634944 sectors
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   Disklabel type: dos
   Disk identifier: 0xc59f61c0

   Old situation:

   Device         Boot   Start     End Sectors  Size Id Type
   /dev/mmcblk0p1         2048 1026047 1024000  500M  c W95 FAT32 (LBA)
   /dev/mmcblk0p2      1026048 7634943 6608896  3.2G 83 Linux

   >>> Created a new DOS disklabel with disk identifier 0x72a922c8.
   Created a new partition 1 of type 'W95 FAT32 (LBA)' and of size 500 MiB.
   /dev/mmcblk0p2: Created a new partition 2 of type 'Linux' and of size 3.2 GiB.
   /dev/mmcblk0p3: 
   New situation:

   Device         Boot   Start     End Sectors  Size Id Type
   /dev/mmcblk0p1         2048 1026047 1024000  500M  c W95 FAT32 (LBA)
   /dev/mmcblk0p2      1026048 7634943 6608896  3.2G 83 Linux

   The partition table has been altered.
   Calling ioctl() to re-read partition table.
   Re-reading the partition table failed.: Device or resource busy
   The kernel still uses the old table. The new table will be used at the next reboot or after you run partprobe(8) or kpartx(8).
   Syncing disks.
   ========>> mkfs.fat - create an MS-DOS filesystem under Linux
   umount: /dev/mmcblk0p1: not mounted
   mkfs.fat 3.0.28 (2015-05-16)
   ========>> mke2fs - create an ext4 filesystem
   mke2fs 1.42.9 (28-Dec-2013)
   /dev/mmcblk0p2 is mounted; will not make a filesystem here!
   mount: /dev/mmcblk0p2 is already mounted or /run/media/mmcblk0p2 busy
          /dev/mmcblk0p2 is already mounted on /
   ========>> Start system recovery
   ========>> Transfer system files
   ========>> Updating... rootfs_jethro.tar.bz2
   ========>> Updating... rootfs_jethro_update.tar.bz2
   ========>> Updating... rootfs_jethro_config.tar.bz2
   ========>> System recovery complete

   INIT: Sending processes the TERM signal
   INIT: SStopping system message bus: dbus.
   Stopping advanced IEEE 802.11 management: hostapd.
   Stopping system log daemon...0
   Stopping kernel log daemon...0
   Stopping internet superserver: xinetd.
   Deconfiguring network interfaces... done.
   chown: changing ownership of '/etc/vsftpd.conf': Read-only file system
   * stopping FTP Server: vsftpd... stopped /usr/sbin/vsftpd (pid 2240)
   done.
   Sending all processes the TERM signal...
   Sending all processes the KILL signal...
   /etc/rc6.d/S25save-rtc.sh: line 13: /etc/timestamp: Read-only file system
   urandom stop: failed.
   Unmounting remote filesystems...
   Deactivating swap...
   Unmounting local filesystems...
   Rebooting... Press Enter for maintenance(or press Control-D to continue): 

**单独更新Image,dtb和模块**

1. 网络测试

.. code-block:: shell

   =====> Input: ifconfig eth0 192.168.137.81 ping 192.168.137.1 -c 2 -w 4 

   =====> Output: PING 192.168.137.99 (192.168.137.99) 56(84) bytes of data. PING 192.168.137.1 (192.168.137.1) 56(84) bytes of data. 64 bytes from 192.168.137.1: icmp_seq=1 ttl=128 time=0.713 ms 64 bytes from 192.168.137.1: icmp_seq=2 ttl=128 time=0.416 ms

   --- 192.168.137.1 ping statistics --- 2 packets transmitted, 2 received, 0% packet loss, time 1000ms rtt min/avg/max/mdev = 0.416/0.564/0.713/0.150 ms 

|  “0% packet loss”表示连接正常。

2. 传输文件

.. code-block:: shell

   =====> 输入指令:
   tftp -g 192.168.137.1 -r Image
   tftp -g 192.168.137.1 -r ls1012a.dtb
   tftp -g 192.168.137.1 -r modules-4.4.98.tar.bz2

3. 查看系统是否自动挂载分区

.. code-block:: shell

   =====> 输入指令:
   ls /run/media/mmcblk0p1/
   =====> 输出信息：
   Image            ramsys.itb
   firmware-4.4.98.tar.bz2  rootfs_jethro.tar.bz2
   kernel-4.4.98.tar.bz2    rootfs_jethro_config.tar.bz2
   ls1012a.dtb      rootfs_jethro_update.tar.bz2
   modules-4.4.98.tar.bz2   system_recovery.sh

**系统自动挂载分区**

1. 复制相应的文件到/run/media/mmcblk0p1/目录，将原文件替换。

.. code-block:: shell

   =====> 输入指令:
   cp Image /run/media/mmcblk0p1/
   cp ls1012a.dtb /run/media/mmcblk0p1/

2. 解压更新内核模块

.. code-block:: shell

   =====> 输入指令:
   tar xjvf modules-4.4.98.tar.bz2 -C /

3. 保存并重启

.. code-block:: shell

   =====> 输入指令:
   reboot

**若系统没有自动挂载分区**

1. 查看fat分区地址

.. code-block:: shell

   =====> 输入指令:
   fdisk -l
   =====> 输出信息：
   ......
   Device         Boot   Start     End Sectors  Size Id Type
   /dev/mmcblk0p1         2048 1026047 1024000  500M  c W95 FAT32 (LBA
   /dev/mmcblk0p2      1026048 7634943 6608896  3.2G 83 Linux
   ......

2. 手动挂载

.. code-block:: shell

   =====> 输入指令:
   mount /dev/mmcblk0p1 /mnt

3. 复制相应的文件到/mnt目录，将原文件替换。

.. code-block:: shell

   =====> 输入指令:
   cp Image /mnt
   cp ls1012a.dtb /mnt

4. 解压更新内核模块

.. code-block:: shell

   =====> 输入指令:
   tar xjvf modules-4.4.98.tar.bz2 -C /

5. 保存并重启

.. code-block:: shell

   =====> 输入指令:
   reboot