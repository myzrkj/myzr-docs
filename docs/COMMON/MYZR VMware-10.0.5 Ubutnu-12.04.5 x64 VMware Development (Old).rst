MYZR VMware-10.0.5 Ubutnu-12.04.5 x64 VMware Development (Old)
=================================================================

Install and configure the development environment
----------------------------------------------------

Install and run the virtual machine system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- It is recommended to use our virtual machine as development host,guidance in this section is offered to our virtual machine.
- For users who need to build development environment himself,please do all the operations as per the manual before buiding your own development environment,in order not to waste unneccessory time and engergy.

**Prepare system and software of virtual machine**

|   1）Download system of virtual machine

- Name of file: vm10-u12045-serv-amd64.rar
- This is the working environment of Ubuntu 12.04.5 Server version which was installed and configured

|   2）Download software of virtual machine

- Name of file:VMware-workstation-full-10.0.5-2443746.exe
- This is the virtual machine software: VMware workstation.

**Install virtual machine**

|   1）Decompress system of virtual machine

- Decompress vm10-u12045-serv-amd64.rar to the current folder in Windows.
- Install software of virtual machine
- Refer to “00.vmware10 installation ”in the directory of vm10-u12045-serv-amd64 to install VMware-workstation-full-10.0.5-2443746.exe.

**Run virtual machine system**

|   1）Start up VMware Workstation software
|   2）Load virtual machine system

- Operate in order on VMware Workstation menu:file -> open -> find vm10-u12045-serv-amd64 directory，select“vm10-u12045-serv-amd64.vmx” -> open

|   3）Start up virtual machine system

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.1.3.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.1.3.1.png

- Click"start this virtual machine"

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.1.3.2.png
   :alt: MY-SAMA5_Linux-3.18_build_2.1.3.2.png

- Select"I have copied this virtual machine".

|   4）Login virtual machine system

- User Name:myzr
- Password:myzr123

Configure development environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Update source list of virtual machine system**

.. code-block:: shell

    $ sudo apt-get update

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.2.0.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.0.1.png

|   Like what the following figures showed after update

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.2.0.2.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.0.2.png

**Update virtual machine system**

.. code-block:: shell

    $ sudo apt-get -y dist-upgrade

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.2.2.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.2.1.png

|   The above figures are the screenshots when update command is executed again after the update of virtual machine system

**Install management tool of aptitude package and ia32-libs**

|   1）Install management tool of aptitude package

.. code-block:: shell

    $ sudo apt-get -y install aptitude

|   Tips: the above figures are the screenshots when installation command is executed again after aptitude was installed.

|   2）Install ia32-libs with aptitude

.. code-block:: shell

    $ sudo aptitude -y install ia32-libs

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.2.3.2.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.3.2.png

|   Tips: the above figures are the screenshots when installation command is executed again after aptitude and ia32-libs were installed

**Install mkimage tool**

.. code-block:: shell

    $ sudo apt-get -y install uboot-mkimage

|   Tips: the following figures are the screenshots when installation command is executed again after mkimage tool was installed

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.2.4.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.4.1.png

**Install ncurses-dev**

|   "make menuconfig" is dependent to it in nature

.. code-block:: shell

    $ sudo aptitude -y install ncurses-dev

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.2.5.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.2.5.1.png

|   Tips: the above figures are the screenshots when installation command is executed again after ncurses-dev tool was installed.

Demonstration of command functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   Functions such as samba service、tftp service、nfs service、GUI desktop and ect are configured in our virtual machine system,please refer to 03.* ~ 05.* in vm10-u12045-serv-amd64 direcotry for the details.

**Copy files between Windows and virtual machine system**

|   Since it is needed to share files between Windows and virtual machine system in the process of development,so here are demonstrations and isntructions for this kind of operations.
|   1）Open the shared content of virtual machine system in Windows.

- Instruction:“/home/myzr”is configured as shared content which is authorizable and accessable by network in the virtual machine system,the access path is “name of virtual host/myzr.d”or“IP of virtual host/myzr.d”.
- Open "computer or my computer" in Windows,enter “\u12045\myzr.d”in the address column(note:path is \ in Windows system).

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.3.1.1.png
   :alt: MY-SAMA5_Linux-3.18_build_2.3.1.1.png

|   2）Enter user name and password of virtual machine system（myzr : myzr123）.

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.3.1.2.png
   :alt: MY-SAMA5_Linux-3.18_build_2.3.1.2.png

|   3）Click shared content to visit after entering correct user name and password.

- To copy files between Windows and virtual machine system

.. image:: /image/env/MY-SAMA5_Linux-3.18_build_2.3.1.3.png
   :alt: MY-SAMA5_Linux-3.18_build_2.3.1.3.png