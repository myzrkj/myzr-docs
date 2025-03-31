MYZR-I.MX8Mmini-CB240 烧录手册
================================

**下载文件**

|  打开网盘到 “2.1_OS_Linux-4.14.98 -> 01_ManufacturingToolkit”，下载 “UUU-MYIMX8MM-L4.14.98” 目录和 “UUU-MYIMX8MM-L4.14.98-Patch.*.rar” 压缩包。

**解压文件**

|  解压MYIMX8MM-L4.14.98-Patch.*.rar，把fsl-image-validation-myimx8mm.tar.bz2和fsl-image-validation-myimx8mm.manifest复制到image-rootfs-L4.14.98目录里面。

**连接烧录线**

|  为开发板断电，用 USB 线连接开发板的烧录口和 PC。

**拨码到下载模式**

|  并把开发板的 “Boot Mode” 拨到 “OFF ON”。

**执行烧录**

|  给开发板上电，双击运行 “myimx8mmek240-8mm.bat” 文件，这时候 Windows 命令行窗口会看到如下信息：

.. code-block:: shell

   <code>uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.2.135-0-gacaf035
   Success 0    Failure 0
   1:32    ......
   </code>

**烧录完成**

|  烧录完成后，Windows 命令行窗口信息如下：

.. code-block:: shell

   <code>uuu (Universal Update Utility) for nxp imx chips -- libuuu_1.2.135-0-gacaf035
   Success 1    Failure 0
   1:32    24/24 [Done                                  ] FBK: DONE
   请按任意键继续. . .
   </code>

**启动开发板**

|  把开发板断电，“Boot Mode” 拨到 “ON OFF”，并为开发板上电，开发板即可正常启动