AI Demo Manual
================

Running the AI Demo
----------------------

Downloading Demo Files
~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the network drive to `1. General Materials -> 1.4-Demo`, and download the `1.4-Demo` directory to a USB flash drive (Note: This directory is about 2GB, so it's recommended to use a USB 3.0 flash drive).
2. After the download is complete, insert the USB flash drive into the development board.
3. Mount the USB flash drive to the file system.

.. code-block:: shell

   mount /dev/sda1 /mnt

4. Copy `1.4-Demo` to the development board using the following reference command:

.. code-block:: shell

   cp /mnt/1.4-Demo ~

Extracting Demo Files
~~~~~~~~~~~~~~~~~~~~~~~

1. Copy `libtvm_runtime.so` from `1.4-Demo` to the development board using the following reference command:

.. code-block:: shell

   cp ~/1.4-Demo/libtvm_runtime.so /usr/lib64/

   **Note**: `libtvm_runtime.so` needs to be placed in the `/usr/lib64/` directory.

2. Extract `rzv_ai_apps_v520_bin.tar.gz` from `1.4-Demo` to the development board using the following reference command:

.. code-block:: shell

   tar zxf ~/1.4-Demo/rzv_ai_apps_v520_bin.tar.gz -C ~

3. Extract `rzv_ai_apps_v520_lib.tar.gz` from `1.4-Demo` using the following reference command:

.. code-block:: shell

   tar zxf ~/1.4-Demo/rzv_ai_apps_v520_lib.tar.gz -C ~

Running the Demo Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Run the Demo script

.. code-block:: shell

   ~/1.4-Demo/rzv_ai_apps_v520.sh

|  Here, you will be prompted to enter the number of the Demo you want to run, similar to the following:

.. code-block:: shell

   1) 01_Head_count
   2) 02_Line_crossing_object_counting
   3) 03_Elderly_fall_detection
   4) 04_Safety_helmet_vest_detection
   5) 05_Age_gender_detection
   6) 07_Animal_detection
   7) 09_Human_gaze_detection
   8) 10_Driver_monitoring_system
   9) 11_Head_count_topview
   10) 12_Hand_gesture_recognition_v2
   11) 13_Car_ahead_departure_detection
   12) 14_Multi_camera_vehicle_detection
   13) 15_Road_lane_segmentation
   Please enter the number of the demo to run:

2. At this point, enter the number of the Demo you want to run and press `Enter`. The program's running log will then be displayed, as shown in the following example:

.. code-block:: shell

   请输入要运行的编号：1
   运行程序：head_count_app USB
   Starting Head Count Application
   [10:56:52] /drp-ai_tvm/tutorials/now/01_Head_count/src/MeraDrpRuntimeWrapper.cpp:73: Loading json data...
   [10:56:52] /drp-ai_tvm/tutorials/now/01_Head_count/src/MeraDrpRuntimeWrapper.cpp:91: Loading runtime module...
   [10:56:54] /drp-ai_tvm/tutorials/now/01_Head_count/src/MeraDrpRuntimeWrapper.cpp:96: Loading parameters...
   [INFO] loaded runtime model :head_count_yolov3
   
   [INFO] USB CAMERA
   Key Hit Thread Starting
   ************************************************
   * Press ENTER key to quit. *
   ************************************************
   Main Loop Starts
   [10:56:56] /drp-ai_tvm/tutorials/now/01_Head_count/src/MeraDrpRuntimeWrapper.cpp:112: Loading input...
   [10:56:56] /drp-ai_tvm/tutorials/now/01_Head_count/src/MeraDrpRuntimeWrapper.cpp:112: Loading input...

Demo Description
-------------------

01_Head_count
~~~~~~~~~~~~~~~

|  This Demo program can count the number of human heads in the camera image. The AI model used is YOLOV3.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/01_Head_count.png
   :alt: 01_Head_count

02_Line_crossing_object_counting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it will count objects when they cross the virtual line drawn by the program. The AI model used is YOLOV3.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/02_Line_crossing_object_counting.png
   :alt: 02_Line_crossing_object_counting

|  This Demo program cannot be run through the script for the time being and needs to be run manually with parameters. Here's an example:

.. code-block:: shell

   cd rzv_ai_apps-5.20/02_Line_crossing_object_counting/exe_v2h/
   ./line_crossing_app USB person 150 0 950 1050 1

03_Elderly_fall_detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can detect fall events in the input video from the camera. The AI models used are TINYYOLOV2 and HRNet.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/03_Elderly_fall_detection.png
   :alt: 03_Elderly_fall_detection

04_Safety_helmet_vest_detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can detect the presence of safety helmets and vests in the image. The AI model used is YOLOV3.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/04_Safety_helmet_vest_detection.png
   :alt: 04_Safety_helmet_vest_detection

05_Age_gender_detection
~~~~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can predict an individual's age range and detect their gender. The AI models used are TINYYOLOV2 and FairFace.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/05_Age_gender_detection.png
   :alt: 05_Age_gender_detection

07_Animal_detection
~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can detect specific animal classifications in the camera input. The AI model used is YOLOV3.

+----------+-----------+----------+--------+
| Category |  Animal   | Category | Animal |
+==========+===========+==========+========+
| 1        | Wild Boar | 7        | Fox    |
+----------+-----------+----------+--------+
| 2        | Deer      | 8        | Weasel |
+----------+-----------+----------+--------+
| 3        | Crow      | 9        | Skunk  |
+----------+-----------+----------+--------+
| 4        | Monkey    | 10       | Dog    |
+----------+-----------+----------+--------+
| 5        | Bear      | 11       | Cat    |
+----------+-----------+----------+--------+
| 6        | Raccoon   |          |        |
+----------+-----------+----------+--------+

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/07_Animal_detection.png
   :alt: 07_Animal_detection

09_Human_gaze_detection
~~~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can detect an individual's line of sight. The AI models used are TINYYOLOV2 and ResNet18.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/09_Human_gaze_detection.png
   :alt: 09_Human_gaze_detection

10_Driver_monitoring_system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can recognize the driver's attention. This includes driver's head pose detection (left, right, and middle head poses), blink detection, and yawn detection. The AI models used are YOLOV3 and DeepPose.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/10_Driver_monitoring_system.png
   :alt: 10_Driver_monitoring_system

11_Head_count_topview
~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can count the number of human heads present in the video from the camera input. The AI model used is YOLOV3.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/11_Head_count_topview.png
   :alt: 11_Head_count_topview

12_Hand_gesture_recognition_v2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can detect different hand gestures. It detects a total of 8 gestures, including 1, 2, 3, 4, 5, thumbs up, thumbs down, and shaking in the hand. The AI model used is YOLOV3.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/12_Hand_gesture_recognition_1.jpg
   :alt: 12_Hand_gesture_recognition_1

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/12_Hand_gesture_recognition.png
   :alt: 12_Hand_gesture_recognition

13_Car_ahead_departure_detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can detect vehicles and track objects. The AI model used is TINY YOLOV3.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/13_Car_ahead_departure_detection.png
   :alt: 13_Car_ahead_departure_detection

15_Road_lane_segmentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|  When this Demo program is running, it can segment road lanes in the video from the camera input and generate a mask overlay on the lanes. The AI model used is Unet.

.. image:: /image/MYZR-瑞萨系列/MYZR-RZV2H-EK320/15_Road_lane_segmentation.png
   :alt: 15_Road_lane_segmentation