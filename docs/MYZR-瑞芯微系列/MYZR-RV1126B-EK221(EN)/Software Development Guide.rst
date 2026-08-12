.. raw:: html

   <style>
   h1 {
       color: green;
   }
   </style>

Software Development Guide
=========================

Compilation Guide
-----------------

Compilation Environment Requirements:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compilation must be performed on an Ubuntu system. The author's host system is Ubuntu 22.04. It is recommended to use the same version of Ubuntu to avoid compatibility issues with some tools.

Install Libraries and Toolset:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   sudo apt-get update && sudo apt-get install git ssh make gcc libssl-dev \
   liblz4-tool expect expect-dev g++ patchelf chrpath gawk texinfo chrpath \
   diffstat binfmt-support qemu-user-static live-build bison flex fakeroot \
   cmake gcc-multilib g++-multilib unzip device-tree-compiler ncurses-dev \
   libgucharmap-2-90-dev bzip2 expat gpgv2 cpp-aarch64-linux-gnu libgmp-dev \
   libmpc-dev bc python-is-python3 python2 gettext libc6-dev libncurses-dev rsync

* (Python version requirement: Python 3.6 or higher)

* (Make version requirement: Make 4.0 or higher)

* (lz4 version requirement: lz4 1.7.3 or higher)

Download Source Code Package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the RV1126B source code package.

2. Create a compilation directory:

.. code-block:: shell

   mkdir  -p ~/my-work/RV1126b/

3. Place the source code in the newly created directory, merge the split compressed source files, then extract:

.. code-block:: shell

   cat myzr-rv1126b.tar.gz.part-* > myzr-rv1126b.tar.gz
   tar xvf myzr-rv1126b.tgz -C ~/my-work/RV1126b/

Linux System Image Compilation and Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* View compilation commands:

.. code-block:: shell

   ./build.sh help or ./build.sh -h

   ################################################
   
   ./build.sh -h
   
   ############### Rockchip Linux SDK ###############
   
   Manifest: rv1126b_linux6.1_release_v1.0.0_20250620.xml
   
   Log colors: message notice warning error fatal
   
   Usage: build.sh [OPTIONS]
   Available options:
   chip[:<chip>[:<config>]]                choose chip
   defconfig[:<config>]                    choose defconfig
    *_defconfig                            switch to specified defconfig
       available defconfigs:
       myzr_rv1126b_evb1_defconfig
       rockchip_defconfig
       rockchip_rv1126b_evb1_v10_defconfig
       rockchip_rv1126b_evb4_v10_defconfig
       rockchip_rv1126b_ipc_32_evb1_v10_defconfig
       rockchip_rv1126b_ipc_64_evb1_v10_defconfig
       rockchip_rv1126b_robot_defconfig
       rockchip_rv1126bp_evb1_v10_defconfig
       rockchip_rv1126bp_ipc_32_evb1_v10_defconfig
       rockchip_rv1126bp_ipc_64_evb1_v10_defconfig
       rockchip_rv1126bp_robot_defconfig
    olddefconfig                           resolve any unresolved symbols in .config
    savedefconfig                          save current config to defconfig
    menuconfig                             interactive curses-based configurator
   config                                  modify SDK defconfig
   print-parts                             print partitions
   list-parts                              alias of print-parts
   edit-parts                              edit raw partitions
   misc                                    pack misc image
   kernel-6.1[:dry-run]                    build kernel 6.1
   kernel[:dry-run]                        build kernel
   recovery-kernel[:dry-run]               build kernel for recovery
   kernel-modules[:<dst dir>:dry-run]      build kernel modules
   modules[:<dst dir>:dry-run]             alias of kernel-modules
   linux-headers[:<arch>:dry-run]          build linux-headers
   kernel-config[:dry-run]                 modify kernel defconfig
   kconfig[:dry-run]                       alias of kernel-config
   kernel-make[:<arg1>:<arg2>]             run kernel make
   kmake[:<arg1>:<arg2>]                   alias of kernel-make
   wifibt[:<dst dir>[:<chip>]]             build Wifi/BT
   amp                                     build and pack amp system
   buildroot-config[:<config>]             modify buildroot defconfig
   bconfig[:<config>]                      alias of buildroot-config
   buildroot-make[:<arg1>:<arg2>]          run buildroot make
   bmake[:<arg1>:<arg2>]                   alias of buildroot-make
   buildroot-sdk                           build the buildroot SDK tarball
   bsdk                                    alias of buildroot-sdk
   rootfs[:<rootfs type>]                  build default rootfs
   buildroot                               build buildroot rootfs
   yocto                                   build yocto rootfs
   debian                                  build debian rootfs
   recovery                                build recovery
   security-createkeys                     create keys for security
   security-misc                           build misc with system encryption key
   security-ramboot[:system_image]         build security ramboot
   security-system[:system_image]          build security system
   security-remote-sign                    build remote signed image
   loader[:dry-run]                        build loader (u-boot)
   uboot[:dry-run]                         build u-boot
   u-boot[:dry-run]                        alias of uboot
   extra-parts                             pack extra partition images
   firmware                                pack and check firmwares
   edit-package-file                       edit package-file
   edit-ota-package-file                   edit package-file for OTA
   updateimg                               build update image
   ota-updateimg                           build update image for OTA
   all                                     build images
   release[:<subdir>[:<name>]]             release images and build info
   all-release[:<subdir>[:<name>]]         build and release images
   shell                                   setup a shell for developing
   buildroot-shell                         setup a shell for buildroot developing
   bshell                                  alias of buildroot-shell
   yocto-shell                             setup a shell for yocto developing
   yshell                                  alias of yocto-shell
   cleanall                                cleanup all
   clean-config                            cleanup config
   clean-recovery                          cleanup recovery
   clean-rootfs                            cleanup rootfs
   clean-security                          cleanup security
   clean-misc                              cleanup misc
   clean-extra-parts                       cleanup extra-parts
   clean-kernel                            cleanup kernel
   clean-updateimg                         cleanup updateimg
   clean-firmware                          cleanup firmware
   clean-loader                            cleanup loader
   clean-amp                               cleanup amp
   post-rootfs <rootfs dir>                trigger post-rootfs hook scripts
   help                                    display this information
   
   Default option is 'all'.

* Select the corresponding board configuration, choose option 2 -- myzr_rv1126b_evb1_defconfig:

.. code-block:: shell

   ./build.sh lunch

   ################################################
   
   ./build.sh lunch
   
   ############### Rockchip Linux SDK ###############
   
   Manifest: rv1126b_linux6.1_release_v1.0.0_20250620.xml
   
   Log colors: message notice warning error fatal
   
   Log saved at /home/wanglk/my-work/rockchip/RV1126B_Linux6.1_SDK/rv1126b_linux6.1_release_v1.0.0_20250620_sync20250825/output/sessions/2025-10-22_05-44-49
   Pick a defconfig:
   
   1. rockchip_defconfig
   2. myzr_rv1126b_evb1_defconfig
   3. rockchip_rv1126b_evb1_v10_defconfig
   4. rockchip_rv1126b_evb4_v10_defconfig
   5. rockchip_rv1126b_ipc_32_evb1_v10_defconfig
   6. rockchip_rv1126b_ipc_64_evb1_v10_defconfig
   7. rockchip_rv1126b_robot_defconfig
   8. rockchip_rv1126bp_evb1_v10_defconfig
   9. rockchip_rv1126bp_ipc_32_evb1_v10_defconfig
   10. rockchip_rv1126bp_ipc_64_evb1_v10_defconfig
   11. rockchip_rv1126bp_robot_defconfig
   

* Perform global compilation and package firmware:

.. code-block:: shell

   ./build.sh 

* Only perform global compilation without firmware packaging

.. code-block:: shell

   ./build.sh all 

* Only perform firmware packaging

.. code-block:: shell 

   ./build.sh firmware

* Clean up SDK directory:

.. code-block:: shell

   ./build.sh cleanall

Compile Individual Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Compile U-Boot separately:

.. code-block:: shell 

   ./build.sh uboot

* Compile Kernel separately:

.. code-block:: shell

   ./build.sh kernel

* Compile recovery separately:

.. code-block:: shell

   ./build.sh recovery

* Compile buildroot separately:

.. code-block:: shell

   ./build.sh rootfs

After compiling individual modules, the firmware will be packaged automatically, no need to perform firmware packaging again.

Open kernel/buildroot Configuration Menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell
   
   ## Open kernel configuration menu, execute in SDK root directory:
   ./build.sh kernel-config
   
   ## Open buildroot configuration menu, execute in SDK root directory:
   ./build.sh buildroot-config