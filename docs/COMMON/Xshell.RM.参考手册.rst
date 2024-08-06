终端软件XShell参考手册
======================

软件下载及安装
--------------

| 　之所以选择 XShell，是因为XShell有 “Free License” ，并且功能够使用。  
| 　软件可以从官方下载： `https://www.xshell.com <https://www.xshell.com>`_
| 　1. 点击 “Xshell” ，点击 “Download” 。  
| 　2. 填写好 “Evaluation user / Home & School user” 带 “*” 的表项后，点击 “Submit” 。  
| 　3. 会在所填写的邮箱中收到来自软件官方包含下载地址的链接。  
| 　4. 复制邮件中的链接地址到浏览器中打开，即自动下载软件。  
| 　5. 软件的安装没有特别需要注意的地方，这里不就写在手册里了。  

新建串口会话示例
----------------

| 　1. 从 “文件” 菜单中选择 “新建” 。将显示 “新建会话属性” 对话框。  
| 　2. 从 “协议” 列表中选择 “SERIAL” 。  
| 　3. 在 “名称” 中输入会话名称。 

.. figure:: /image/Xshell/Xshell6_New_Session_Properties_Serial01.png
   :alt: Xshell6_New_Session_Properties_Serial01.png
 
| 　4. 从 “类别” 中选择 “SERIAL” 。  
| 　5. 从 “端口” 中选择与PC连接的串口号。  
| 　6. 在 “波特率” 中选择通信速度。  
| 　7. 在 “数据位” 中选择传输的数据单位位数。  
| 　8. 在 “停止位” 中选择指示数据单元结束的位数。  
| 　9.  “奇偶校验” 用于验证传输数据中的错误。  
| 　10.  “流量控制” 用于控制数据通信。  
| 　11. 单击 “确定” 创建新会话。  
| 　12. 使用创建的会话按照 “与会话连接” 中的描述建立连接。  

.. figure:: /image/Xshell/Xshell6_New_Session_Properties_Serial02.png
   :alt: Xshell6_New_Session_Properties_Serial02.png
 

新建SSH会话示例
---------------

| 　1. 从 “文件” 菜单中选择” 新建” 。将显示” 新建会话属性” 对话框。  
| 　2. 从 “协议” 列表中选择” SSH” 。  
| 　3. 在 “名称” 中输入会话名称。  
| 　4. 从 “主机” 中输入目标SSH服务的主机IP。  
| 　5. 从 “端口号” 中输入SSH服务的端口号” 22” 。  
| 　6. 单击 “确定” 创建新会话。  
| 　7. 使用创建的会话按照 “与会话连接” 中的描述建立连接。  

.. figure:: /image/Xshell/Xshell6_New_Session_Properties_SSH.png
   :alt: Xshell6_New_Session_Properties_SSH.png

与会话连接
----------

| 　1. 从 “文件” 菜单中选择 “打开” 。将显示 “会话” 对话框。  
| 　2. 选择要连接的会话。  
| 　3. 单击 “连接” 。
  
.. figure:: /image/Xshell/Xshell6_Sessions_Dialog_Box.png
   :alt: Xshell6_New_Session_Properties_SSH.png

| 　4. 如果没有新建过目标会话，则点击本页面右侧目录中的 “新建串口会话” 或 “新建SSH会话” 来新建会话。

**串口会话连接示例** 

| 　串口会话连接无特别操作，通常选中会话后点击 “连接” 即可。  

**SSH 会话连接示例**  

| 　1. 在会话对话框选择目标SSH会话并单击连接。  
| 　2. 可能弹出询问 “接受此主机密钥吗？” 的对话框，选择 “接受并保存” 。 

.. figure:: /image/Xshell/Xshell6_Dialog_SSH_MD5.png
   :alt: Xshell6_Dialog_SSH_MD5.png

| 　3. 在弹出的对话框中按要求输入目标主机的用户名。

.. figure:: /image/Xshell/Xshell6_Dialog_SSH_User.png
   :alt: Xshell6_Dialog_SSH_User.png
  
| 　4. 如果目标主机需要密码，则会弹出对话框，输入目标主机的用户密码。  

文件传输
--------

**使用 ZMODE 由 Windows PC 向开发板发送文件**  

| 　1. 从Windows文件资源管理器中选择要传输到开发板的文件。  
| 　2. 拖动文件并将其放在Xshell中对应的开发板终端窗口上。  
| 　3. 文件传输自动执行。  

.. figure:: /image/Xshell/Xshell6_ZMODEL_Recv.png
   :alt: Xshell6_ZMODEL_Recv.png
  
**使用 ZMODE 由开发板向 Windows PC 向发送文件**

| 　1. 开发板上执行 sz <FileName>。  
| 　2. 在 Windows PC 弹出的对话框中选择文件的保存位置。  
| 　3. 等待文件传输完成。  

.. figure:: /image/Xshell/Xshell6_ZMODEL_Send.png
   :alt: Xshell6_ZMODEL_Send.png

**其它说明**  

| 　SSH 终端下的 ZMODEM 的传输速度可以达到2MB/秒。
| 　串口终端下的 ZMODEM 的传输速度在20KB/秒左右。  

--------------------------------------------------------------------------------

::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2023/5/08  
   * Supporter: Zhong JiaYi
   --------------------------------------------------------------------------------

