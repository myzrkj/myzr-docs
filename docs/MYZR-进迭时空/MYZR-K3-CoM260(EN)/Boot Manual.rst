.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Boot Manual
===========

Preparing For Use
~~~~~~~~~~~~~~~~~

Power Adapter
^^^^^^^^^^^^^

The K3 CoM260 Development Kit is powered by the DCIN and requires a DC Jack power adapter with an output specification of 19 V /2.37 A or 12 V /5 A. For detailed requirements regarding the interface and adapter, please refer to the Power Input section.

Keyboard and mouse
^^^^^^^^^^^^^^^^^^

You can use any of the USB-A ports on the K3 CoM260 Development Kit to connect a wired keyboard, mouse, or USB receiver, or you can connect a keyboard and mouse via Bluetooth.

When a USB 3.0 device and a keyboard and mouse using a 2.4 GHz wireless receiver are simultaneously connected to adjacent USB 3.0 ports, the keyboard and mouse may experience input lag or delays. This is because the high-speed transmission of USB 3.0 may interfere with the 2.4 GHz wireless signal, which is a fairly common physical phenomenon.

If you encounter such a situation, it is recommended to use the USB extension cable to extend the wireless receiver away from the USB 3.0 device to reduce signal interference and improve the stability of the wireless connection.

monitor
^^^^^^^

The K3 CoM260 requires an external monitor to output the image. The product supports DP and MIPI DSI video interfaces, so it can be connected to a monitor with one or both of the corresponding interfaces.

.. code-block:: text

   Note: If you need to output the image through the MIPI DSI interface, be sure to connect the video cable between the monitor and the K3 CoM260 before powering on. The MIPI DSI interfaces of the K3 CoM260 do not support hot-plugging.

Internet connection
^^^^^^^^^^^^^^^^^^^

The K3 CoM260 supports wired RJ45 network connections, allowing you to connect directly to the network cable.

Meanwhile, the K3 CoM260 also supports Wi-Fi and Bluetooth wireless connectivity; an external antenna can be installed for enhanced signal strength.

Start to Start
~~~~~~~~~~~~~~

Please follow the steps below to complete the connections before powering on the device:

- Connect the device to the monitor using a video cable, and connect a keyboard and mouse.

- Finally, connect the power cord and turn on the power.

  - First power-on: The device turns on automatically.

  - After a software shutdown: Briefly press the power button to turn the device back on.

After the device is started:

- The red power indicator on the K3 CoM260 Development Kit will light up;

- The cooling fan of the K3 CoM260 module starts operating.

Configure your K3- CoM260 at first startup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The K3 CoM260 comes pre-installed with the Bianbu operating system from Jiedi Shikong. The Configuration Wizard will run automatically when the device is started for the first time. You will need to complete the relevant configuration using the monitor, keyboard, and mouse.

For detailed configuration instructions, please refer to `LXQt First Launch and Session <https://spacemit.com/community/document/info?lang=zh&nodepath=software/SDK/bianbu/user_guide/LXQt/initial_setup_and_sessions.md>`__.
