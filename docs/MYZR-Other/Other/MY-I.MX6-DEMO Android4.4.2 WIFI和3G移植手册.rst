MY-I.MX6-DEMO Android4.4.2 WIFI和3G移植手册
==============================================

移植WIFI（RTL8188EUS）
-----------------------

**步骤一:**

.. code-block:: shell

   ＃ UNITE is a virtual device support both atheros and realtek wifi(ar6103 and rtl 8723as)
   ＃BOARD_WLAN_DEVICE:            := UNITE
   ＃WPA_SUPPLICANT_VERSION:         := VER_0_8_UNITE
   ＃TARGET_KERNEL_MODULES:          := \  kernel_imx/drivers/net/wireless/rtl8723as/8723as.ko:system/lib/modules/8723as.ko \
      kernel_imx/net/wireless/cfg80211.ko:system/lib/modules/cfg80211_realtek.ko
   ＃BOARD_WPA_SUPPLICANT_DRIVER:      := NL80211
   ＃BOARD_HOSTAPD_DRIVER:           := NL80211

   ＃BOARD_HOSTAPD_PRIVATE_LIB_QCOM:           := lib_driver_cmd_qcwcn
   ＃BOARD_WPA_SUPPLICANT_PRIVATE_LIB_QCOM:      := lib_driver_cmd_qcwcn
   ＃BOARD_HOSTAPD_PRIVATE_LIB_RTL:           := lib_driver_cmd_rtl
   ＃BOARD_WPA_SUPPLICANT_PRIVATE_LIB_RTL

   ...
   ...
   BOARD_WIFI_VENDOR := realtek

   BOARD_WLAN_VENDOR := REALTEK

   ifeq ($(BOARD_WIFI_VENDOR),realtek)

   WPA_SUPPLICANT_VERSION :=VER_0_8_X

   BOARD_WPA_SUPPLICANT_DRIVER :=NL80211
   ＃CONFIG_DRIVER_WEXT :=y

   CONFIG_DRIVER_NL80211 :=true

   BOARD_WPA_SUPPLICANT_PRIVATE_LIB:= lib_driver_cmd_rtl

   BOARD_HOSTAPD_DRIVER := NL80211

   BOARD_HOSTAPD_PRIVATE_LIB :=lib_driver_cmd_rtl
   BOARD_WLAN_DEVICE := rtl8192cu

   ＃BOARD_WLAN_DEVICE := rtl8192du

   ＃BOARD_WLAN_DEVICE := rtl8192ce

   ＃BOARD_WLAN_DEVICE := rtl8192de

   ＃BOARD_WLAN_DEVICE := rtl8723as

   ＃BOARD_WLAN_DEVICE := rtl8723au

   ＃BOARD_WLAN_DEVICE := rtl8189es

   ＃BOARD_WLAN_DEVICE := rtl8723bs

   ＃BOARD_WLAN_DEVICE := rtl8723bu

   WIFI_DRIVER_MODULE_NAME :="wlan"

   WIFI_DRIVER_MODULE_PATH := "/system/lib/modules/wlan.ko"

   WIFI_DRIVER_MODULE_ARG :="ifname=wlan0 if2name=p2p0"

   WIFI_FIRMWARE_LOADER :=""

   WIFI_DRIVER_FW_PATH_STA :=""

   WIFI_DRIVER_FW_PATH_AP :=""

   WIFI_DRIVER_FW_PATH_P2P :=""

   WIFI_DRIVER_FW_PATH_PARAM :=""

   Endif

**步骤二：**

.. code-block:: shell

   vim device/fsl/sabresd_6dq/init.rc

   ＃service p2p_supplicant /system/bin/wpa_supplicant \
   ＃ -ip2p0 -Dnl80211 -c/data/misc/wifi/p2p_supplicant.conf \
   ＃ -I/system/etc/wifi/p2p_supplicant_overlay.conf -N \
   ＃ -iwlan0 -Dnl80211 -c/data/misc/wifi/wpa_supplicant.conf \
   ＃ -I/system/etc/wifi/wpa_supplicant_overlay.conf \
   ＃ -O/data/misc/wifi/sockets -puse_p2p_group_interface=1 \
   ＃ -e/data/misc/wifi/entropy.bin -g@android:wpa_wlan0
   ＃ class late_start
   ＃ socket wpa_wlan0 dgram 660 wifi wifi
   ＃ disabled
   ＃ oneshot

   ＃service rtw_suppl_con /system/bin/rtl_wpa_supplicant \
   ＃ -ip2p0 -Dnl80211 -c/data/misc/wifi/p2p_supplicant.conf \
   ＃ -I/system/etc/wifi/p2p_supplicant_overlay.conf -N \
   ＃ -iwlan0 -Dnl80211 -c/data/misc/wifi/wpa_supplicant.conf \
   ＃ -I/system/etc/wifi/wpa_supplicant_overlay.conf \
   ＃ -O/data/misc/wifi/sockets -puse_p2p_group_interface=1 \
   ＃ -e/data/misc/wifi/entropy.bin -g@android:wpa_wlan0
   ＃ class late_start
   ＃ socket wpa_wlan0 dgram 660 wifi wifi
   ＃ disabled
   ＃ oneshot

   service rtw_suppl_con /system/bin/wpa_supplicant \

     -ip2p0 -Dnl80211 -c/data/misc/wifi/p2p_supplicant.conf \
     -e/data/misc/wifi/entropy.bin -N \
     -iwlan0 -Dnl80211 -c/data/misc/wifi/wpa_supplicant.conf \
     -O/data/misc/wifi/sockets \
     -g@android:wpa_wlan0
     class main
     socket wpa_wlan0 dgram 660 wifi wifi
     disabled
     oneshot

   service rtw_suppl /system/bin/wpa_supplicant \

     -iwlan0 -Dnl80211 -c/data/misc/wifi/wpa_supplicant.conf \
     -O/data/misc/wifi/sockets \
     -e/data/misc/wifi/entropy.bin
     -g@android:wpa_wlan0
     class main
     socket wpa_wlan0 dgram 660 wifi wifi
     disabled
     oneshot

**步骤三：**

|  ”realtek_wifi_SDK_for_android_KK_4.4_20140117.tar.gz” 解压，然后将里面的ANDROID_SDK/hardware/realtek覆盖到android源码hardwar/realtek目录下中。

**步骤四：**

.. code-block:: shell

   vim hardware/libhardware_legacy/wifi/Android.mk

   ＃ifeq ($(BOARD_WLAN_DEVICE),UNITE)
   ＃ LOCAL_C_INCLUDES += $(LOCAL_PATH)/../../external/wpa_supplicant_ath/wpa_supplicant/src/common
   ＃ LOCAL_SRC_FILES += wifi/wifi_unite.c
   ＃else ifeq ($(BOARD_WLAN_VENDOR), INTEL)
   ＃ LOCAL_SRC_FILES += wifi/wifi_intel.c
   ＃ LOCAL_C_INCLUDES += $(LOCAL_PATH)/../../external/wpa_supplicant_8/src/common
   ＃else
   ＃ LOCAL_SRC_FILES += wifi/wifi.c
   ＃ LOCAL_C_INCLUDES += $(LOCAL_PATH)/../../external/wpa_supplicant_8/src/common
   ＃endif

   ifeq ($(BOARD_WIFI_VENDOR),realtek)
   LOCAL_SRC_FILES +=../realtek/wlan/libhardware_legacy/wifi/wifi_realtek.c
   else
   LOCAL_SRC_FILES += wifi/wifi.c
   endif

**步骤五：**

|  将android源码的external/下wpa_supplicant_8备份一下，然后将驱动包里的wpa_supplicant_8_kk_4.4_rtw_r10450.20140220.tar.gz解压并重命名为wpa_supplicant_8并替换到我们android的external/目录下。

**步骤六：**

|  修改文件kernel_imx/arch/arm/configs/imx6_android_defconfig，（或者修改.config）将下列项目配置成Y.

.. code-block:: shell

   CONFIG_CFG80211=y

   CONFIG_MAC80211_MESH=y

   CONFIG_MAC80211=y

   CONFIG_HOSTAP=y

   CONFIG_USB_USBNET=y

**步骤七：**

.. code-block:: shell

   vim device/fsl/imx6/etc/init.rc

    setprop wifi.interface wlan0
    setprop wlan.driver.status "ok"

**步骤八：**

|  out/target/product/sabresd_6dq下的system文件夹以及out/target/product/sabresd_6d/obj/EXECUTABLES下wpa_supplicant_intermediates文件夹删除，重新编译system.img和boot.img。

**步骤九：**

|  编译wlan.ko复制system/lib/modules/目录下

.. code-block:: shell

   vim Makefile
   CONFIG_PLATFORM_I386_PC = n
   
   CONFIG_PLATFORM_NEW = y
   
   ifeq ($(CONFIG_PLATFORM_NEW), y)
   EXTRA_CFLAGS += -DCONFIG_LITTLE_ENDIAN
   ARCH := arm
   CROSS_COMPILE :=/home/linyn/android/android-myzr/prebuilts/gcc/linux-x86/arm/arm-eabi-4.6/bin/arm-eabi- KSRC := /home/linyn/android/android-myzr/kernel_imx
   MODULE_NAME := wlan
   endif
   
   vim include/autoconf.h
   
   ＃define CONFIG_IOCTL_CFG80211
   ＃ifdef CONFIG_IOCTL_CFG80211
   ＃define RTW_USE_CFG80211_STA_EVENT
   
   //＃defineCONFIG_CFG80211_FORCE_COMPATIBLE_2_6_37_UNDER
   
   //＃define CONFIG_DEBUG_CFG80211 1
   ＃endif
   ...
   ...
   ＃define CONFIG_CONCURRENT_MODE
   
   ＃define CONFIG_P2P_IPS

|  最后编译成wlan.ko复制到system/lib/modules/目录下


移植3G（MU609）
-----------------

**步骤一：**

.. code-block:: shell

   vim kernel_imx/drivers/usb/serial/option.c

   ＃define HUAWEI_PRODUCT_E353:     0x1506

|  改为

.. code-block:: shell

   ＃define HUAWEI_PRODUCT_E353:     0x1573

**步骤二：**

.. code-block:: shell

   vim hardware/ril/rild/rild.c

   ＃define REFERENCE_RIL_DEF_PATH "/system/lib/libreference-ril.so"

|  改为

.. code-block:: shell

   ＃define REFERENCE_RIL_DEF_PATH "/system/lib/libhuawei-ril.so"

   ...
   // switchUser();

**步骤三：**

.. code-block:: shell

   Vim hardware/ril/runtime-ril-port/runtime_port.c

|  在数组里增加新的结构：

.. code-block:: shell

   static struct modem_3g_device modem_3g_device_table[] = {
   ：{

     .name:  = "Huawei-MU609",
     .idVendor = "12d1",
     .idProduct = "1573",
     .deviceport = "/dev/ttyUSB2",
     .dataport = "/dev/ttyUSB0",
     .type:  = HUAWEI_MODEM,
   ：},

**步骤四：**

|  复制 ip-up,ip-down 到 /system/etc/ppp目录下,复制 libhuawei-ril.so 到 /system/lib目录下。

**步骤五：**

.. code-block:: shell

  vim device/fsl/imx6/etc/init.rc

|  按照以下修改：

.. code-block:: shell

   chmod 777 /dev/ttyUSB0
   chmod 777 /dev/ttyUSB2
   chmod 777 /etc/ppp/ip-up
   chmod 777 /etc/ppp/ip-down
   ＃service ril-daemon /system/bin/rild
   service ril-daemon /system/bin/rild -l /system/lib/libhuawei-ril.so

**步骤六：**

|  重新编译system.img和boot.img。