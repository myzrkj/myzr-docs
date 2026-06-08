Software Development Guide
============================

.. include:: /docs/COMMON/MYZR-RK3588-EK360开发环境搭建手册.rst

Compilation Manual
--------------------

Install Cross-Compilation Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Download Network Disk File**

   Open the network disk and navigate to `3. Software Materials -> Linux-5.10.145 —> 3.3-Tools`, then download the `poky` directory.

2. **Copy File to Compilation Host**

   Copy the downloaded `poky` directory to `${HOME}/my-work/rzv-linux-5.10.145` on the compilation host. If this directory does not exist yet, enter the following command on the compilation host and press Enter to create the required directory.

   .. code-block:: shell

      # Description: Create directory path
      mkdir ~/my-work/rzv-linux-5.10.145 -p

3. **Execute Installation Command**

   Enter the following command on the compilation host and press Enter to start the installation.

   .. code-block:: shell

      # Description: Enter the poky directory
      cd ~/my-work/rzv-linux-5.10.145/poky

      # Description: Run the installation file
      ./poky-glibc-x86_64-core-image-weston-aarch64-myzr-rzv2h-ek320-toolchain-3.1.31.sh


   After executing the command, the following information will appear, indicating that the above command is executed normally.

   .. code-block:: shell

      Poky (Yocto Project Reference Distro) SDK installer version 3.1.31
         ==================================================================
      Enter target directory for SDK (default: /opt/poky/3.1.31):


4. **Enter Installation Path**

   Enter the following path on the compilation host and press Enter, which means installing the poky compilation tool to the required path.

   .. code-block:: shell

      ${HOME}/my-work/rzv-linux-5.10.145/poky


   After entering, the following prompt will appear, indicating that this step is executed normally.

   .. code-block:: shell

      You are about to install the SDK to "/home/tangbin/my-work/rzv-linux-5.10.145/poky". Proceed [Y/n]?


5. **Confirm Installation Path**

   After the above prompt appears, enter `Y` and press Enter to confirm the installation path.

   .. code-block:: shell

      Y

6.  **Wait for Installation**

   After entering in the previous step, the installation will start. The installation time varies depending on the configuration of the compilation host. During the installation process, you can see continuous output. The complete output information is as follows:

   .. code-block:: shell

      Extracting SDK............................................................................................................................done
      Setting it up...done
      SDK has been successfully set up and is ready to be used.
      Each time you wish to use the SDK in a new shell session, you need to source the environment setup script e.g.
       $ . /home/tangbin/my-work/rzv-linux-5.10.145/poky/environment-setup-aarch64-poky-linux
       $ . /home/tangbin/my-work/rzv-linux-5.10.145/poky/environment-setup-armv7vet2hf-neon-vfpv4-pokymllib32-linux-gnueabi


   So far, the installation of the poky cross-compilation tool is completed. Here is a screenshot of the process from Step 3 to Step 6:

   .. figure:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/build.poky.install.png
      :alt: build.poky.install.png


7. **Configure Tool Environment Variables**

   Enter the following command on the compilation host:

   .. code-block:: shell

      . ~/my-work/rzv-linux-5.10.145/poky/environment-setup-aarch64-poky-linux


8.  **Confirm Environment Variables Take Effect**

   Enter the following command on the compilation host:

   .. code-block:: shell

      echo $CC


   The following output information will be displayed, indicating that the environment variables are configured normally.

   .. code-block:: shell

      aarch64-poky-linux-gcc -mtune=cortex-a55 -fstack-protector-strong -D_FORTIFY_SOURCE=2 -Wformat -Wformat-security -Werror=format-security --sysroot=/home/tangbin/my-work/rzv-linux-5.10.145/poky/sysroots/aarch64-poky-linux


9. **View Tool Information**

   Enter the following command on the compilation host:

   .. code-block:: shell

      $CC -v

   The following output information will be displayed, indicating normal status.

   .. code-block:: shell

      Using built-in specs.
      COLLECT_GCC=aarch64-poky-linux-gcc
      COLLECT_LTO_WRAPPER=/home/tangbin/my-work/rzv-linux-5.10.145/poky/sysroots/x86_64-pokysdk-linux/usr/libexec/aarch64-poky-linux/gcc/aarch64-poky-linux/8.3.0/lto-wrapper
      Target: aarch64-poky-linux
      Configured with: ............
      Thread model: posix
      gcc version 8.3.0 (GCC)


Compile Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~

1.  **Prepare Source Code**

   Open the network disk and navigate to `3. Software Materials -> Linux-5.10.145 —> 3.4-Source Code`, then download the `rzv-linux-5.10.145.tar.gz` file.

   Copy the downloaded `rzv-linux-5.10.145.tar.gz` file to `${HOME}/my-work/rzv-linux-5.10.145` on the compilation host. If this directory does not exist yet, enter the following command on the compilation host and press Enter to create the required directory.

   .. code-block:: shell

      mkdir ~/my-work/rzv-linux-5.10.145 -p


   Enter the following command on the compilation host to decompress the source code. If no error is prompted during the decompression process, it means it is normal.

   .. code-block:: shell

      tar zxf rzv-linux-5.10.145.tar.gz -C ~/my-work/rzv-linux-5.10.145/


2. **Configure Compilation Tool Environment Variables**

   .. code-block:: shell

      . ~/my-work/rzv-linux-5.10.145/poky/environment-setup-aarch64-poky-linux


3. **Generate Compilation Configuration File**

   Enter the following command to enter the source code directory:

   .. code-block:: shell

      cd ~/my-work/rzv-linux-5.10.145/linux


   Enter the following command to generate the configuration file:

   .. code-block:: shell

      make defconfig


   The output information of the command execution is as follows:

   .. code-block:: shell

      HOSTCC  scripts/basic/fixdep
      HOSTCC  scripts/kconfig/conf.o
      HOSTCC  scripts/kconfig/confdata.o
      HOSTCC  scripts/kconfig/expr.o
      LEX     scripts/kconfig/lexer.lex.c
      YACC    scripts/kconfig/parser.tab.[ch]
      HOSTCC  scripts/kconfig/lexer.lex.o
      HOSTCC  scripts/kconfig/parser.tab.o
      HOSTCC  scripts/kconfig/preprocess.o
      HOSTCC  scripts/kconfig/symbol.o
      HOSTCC  scripts/kconfig/util.o
      HOSTLD  scripts/kconfig/conf
      *** Default configuration is based on 'defconfig'
      #
      # configuration written to .config
      #

4. **Linux Image Compilation**

   Enter the following command to start compilation:

   .. code-block:: shell

      make Image -j$(nproc)


   The output information of the command execution is as follows:

   .. code-block:: shell

      UPD     include/generated/uapi/linux/version.h
      WRAP    arch/arm64/include/generated/uapi/asm/errno.h
      WRAP    arch/arm64/include/generated/uapi/asm/kvm_para.h
      ............
      GEN     .version
      CHK     include/generated/compile.h
      LD      vmlinux.o
      MODPOST vmlinux.symvers
      MODINFO modules.builtin.modinfo
      GEN     modules.builtin
      LD      .tmp_vmlinux.kallsyms1
      KSYMS   .tmp_vmlinux.kallsyms1.S
      AS      .tmp_vmlinux.kallsyms1.S
      LD      .tmp_vmlinux.kallsyms2
      KSYMS   .tmp_vmlinux.kallsyms2.S
      AS      .tmp_vmlinux.kallsyms2.S
      LD      vmlinux
      SORTTAB vmlinux
      SYSMAP  System.map
      OBJCOPY arch/arm64/boot/Image

5. **Linux Device Tree Compilation**

   Enter the following command to start compilation:

   .. code-block:: shell

      make myzr/myzr-rzv2h-ek320.dtb myzr/myzr-rzv2h-ek320-4g.dtb \
      myzr/myzr-rzv2h-ek320-8g.dtb myzr/myzr-rzv2h-ek320-16g.dtb


   When the device tree is compiled successfully for the first time, the output information is similar to the following:

   .. code-block:: shell

      DTC     arch/arm64/boot/dts/myzr/myzr-rzv2h-ek320.dtb
      DTC     arch/arm64/boot/dts/myzr/myzr-rzv2h-ek320-4g.dtb
      DTC     arch/arm64/boot/dts/myzr/myzr-rzv2h-ek320-8g.dtb
      DTC     arch/arm64/boot/dts/myzr/myzr-rzv2h-ek320-16g.dtb


6. **Linux Module Compilation**

   Enter the following command to start compilation:

   .. code-block:: shell

      make modules -j$(nproc)


   The output information when the module compilation is successful is similar to the following:

   .. code-block:: shell

      CALL    scripts/atomic/check-atomics.sh
      CALL    scripts/checksyscalls.sh
      LDS     scripts/module.lds
      CC [M]  drivers/xen/gntdev.o
      ......
      LD [M]  drivers/usb/gadget/function/usb_f_serial.ko
      LD [M]  drivers/usb/gadget/legacy/g_ether.ko
      LD [M]  drivers/usb/gadget/legacy/g_mass_storage.ko


   Install kernel modules to the specified directory

   .. code-block:: shell

      # =====> Input:
      if [ -d modules ]; then rm -rf modules; fi; mkdir modules
      make modules_install INSTALL_MOD_PATH=./modules


   The output information of module installation is similar to the following:

   .. code-block:: shell

      ......
      INSTALL drivers/usb/gadget/legacy/g_ether.ko
      INSTALL drivers/usb/gadget/legacy/g_mass_storage.ko
      INSTALL drivers/usb/gadget/legacy/g_serial.ko
      DEPMOD  5.10.145-cip17-yocto-standard-gacfb9c790b2d


   Package kernel module files

   .. code-block:: shell

      # =====> Input:
      tar czf modules-myzr-rzv2h-ek320.tgz -C modules lib


7. **Target Files**

   `Image, myzr-rzv2h-ek320.dtb, myzr-rzv2h-ek320-4g.dtb, myzr-rzv2h-ek320-8g.dtb, modules-myzr-rzv2h-ek320.tgz` are the target files. You can use these compiled target files to replace the files with the same names in the firmware directory.
