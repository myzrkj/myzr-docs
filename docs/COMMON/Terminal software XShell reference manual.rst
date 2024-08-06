Terminal software XShell reference manual
===========================================

Software Download and Installation
------------------------------------

| 　The reason why XShell is selected is because XShell has "Free License" and the work can be used.
| 　Software official download address: `https://www.netsarang.com/download/free_license.html <https://www.netsarang.com/download/free_license.html>`_

| 　1. Click "Downroad" for "Xshell 6". 
| 　2. Fill in "Evolution user/Home & amp; After School user "with" * "table entry, click" Submit ". 
| 　3. Will receive a link from the software official containing the download address in the completed mailbox.
| 　4. Copy the link address in the message to open in the browser, that is, automatically download the software.
| 　5. he installation of the software has nothing to pay special attention to. It is written here in the manual.  

New serial session example
---------------------------

| 　1. Select "New" from the "File" menu. the New Session Properties dialog box appears.
| 　2. Select "SERIAL" from the "Protocol" list.
| 　3. Enter a session name in the Name.

.. figure:: /image/Xshell/Xshell6_New_Session_Properties_Serial01.png
   :alt: Xshell6_New_Session_Properties_Serial01.png
 
| 　4. Select "SERIAL" from the category.
| 　5. Select the serial port number to connect to the PC from port. 
| 　6. Select the speed of communication in the "baud rate". 
| 　7. Select the number of data units to transfer in the Data Bit.  
| 　8. In stop bits, select the number of digits that indicate the end of the data unit.
| 　9. The "parity check" is used to verify errors in transmitted data. 
| 　10. "Flow control" is used to control data communication.
| 　11. Click OK to create a new session. 
| 　12. Create a connection according to the description in "Connect to Session" using the session you created.

.. figure:: /image/Xshell/Xshell6_New_Session_Properties_Serial02.png
   :alt: Xshell6_New_Session_Properties_Serial02.png
 

New SSH Session Example
-------------------------

| 　1. Select "New" from the "File" menu. The New Session Properties dialog box appears.
| 　2. Select "SSH" from the "Protocol" list.
| 　3. Enter the session name in name.
| 　4. Enter the host IP of the target SSH service from the host. 
| 　5. Enter the port number "22" for the SSH service from "port number".
| 　6. Click "ok" to create a new session.
| 　7. Create a connection according to the description in "Connect to Session" using the session you created.

.. figure:: /image/Xshell/Xshell6_New_Session_Properties_SSH.png
   :alt: Xshell6_New_Session_Properties_SSH.png

Connect to Session
--------------------

| 　1. Select Open from the File menu. The Session dialog box appears.
| 　2. Select the session that you want to connect to.
| 　3. Click "Connect".
  
.. figure:: /image/Xshell/Xshell6_Sessions_Dialog_Box.png
   :alt: Xshell6_New_Session_Properties_SSH.png

| 　4. If no new target session has been created, click "New serial session" or "New SSH session" in the directory on the right side of this page to create a new session. 

**Examples of serial port session connections** 

　There is no special operation for serial port session connections. Usually, after the session is selected, click "Connect".

**SSH Sample session connection**  

| 　1. Select the target SSH session in the session dialogue box and click on the connection.
| 　2. Possible pop-up query "accept this host key? ", select" Accept and save ".

.. figure:: /image/Xshell/Xshell6_Dialog_SSH_MD5.png
   :alt: Xshell6_Dialog_SSH_MD5.png

| 　3. Enter the user name of the target host as required in the popup dialog.

.. figure:: /image/Xshell/Xshell6_Dialog_SSH_User.png
   :alt: Xshell6_Dialog_SSH_User.png
  
| 　4. If the target host needs a password, a dialogue box will pop up and enter the user password of the target host.

File Transfer
---------------

**Send files from Windows PC to the development board using ZMODE**  

| 　1. Select the file that you want to transfer to the development board from Windows File Explorer.
| 　2. Drag the file and place it on the corresponding development board terminal window in the Xshell.
| 　3. File transfer is automatically executed.

.. figure:: /image/Xshell/Xshell6_ZMODEL_Recv.png
   :alt: Xshell6_ZMODEL_Recv.png
  
**Use ZMODE to send files from the development board to Windows PC**

| 　1. Execution on the development board sz <FileName>。
| 　2. Select the saving location of the file in the dialog box where the Windows PC pops up.
| 　3. Waiting for file transfer to be completed.

.. figure:: /image/Xshell/Xshell6_ZMODEL_Send.png
   :alt: Xshell6_ZMODEL_Send.png

**Other Notes**  

| 　The ZMODEM transmission speed under the SSH terminal can reach 2MB/s.
| 　The ZMODEM transmission speed under the serial port terminal is about 20KB / second. 

--------------------------------------------------------------------------------

::

   --------------------------------------------------------------------------------
   * 珠海明远智睿科技有限公司  
   * ZhuHai MYZR Technology CO.,LTD.
   * Latest Update: 2023/5/08  
   * Supporter: Zhong JiaYi
   --------------------------------------------------------------------------------

