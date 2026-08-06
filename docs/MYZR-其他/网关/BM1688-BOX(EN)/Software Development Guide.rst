.. raw:: html

   <style>
   h1 {
       color: #4CAF50;
   }
   </style>


Software Development Guide
===========================

Compilation Manual
-----------------

Download and Compile
~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   0. Download virtual machine and SDK source code
   https://developer.sophgo.com/site/index/material/96/all.html
   BM1688 official SDK download link
   https://doc.sophgo.com/bm1688_sdk-docs/v2.0/docs_latest_release/docs/BM1688_CV186AH_SophonSDK_doc/
   SDK User Manual
   https://doc.sophgo.com/bm1688_sdk-docs/v2.0/docs_latest_release/docs/athena2-img/
   BSP Development Manual
   
   1. Import docker, get it from the official website. After successful download, rename to bm1688_docker.tar before proceeding to step 2
   wget https://sophon-assets.sophon.cn/sophon-prod-s3/drive/25/06/11/18/docker.zip
   
   2. Import docker image, skip this step if already imported
   unzip docker.zip
   sudo apt-get update
   sudo apt-get install -y docker.io
   sudo docker load -i bm1688_docker.tar
   
   3. vim ~/.bashrc
   Add the following at the end of the file
   function run_docker()
   {
   sudo docker run -e LOCAL_USER_ID=`id -u $USER_ID` --privileged -v /dev:/dev -itd -v $2:/project/$1 --name $1 bm1688_docker:latest /bin/bash
   }
   
   Save and exit, then execute: source ~/.bashrc
   
   Start container and mount code directory
   run_docker sophon /home/myzx/1688
   
   4. Enter container
   sudo docker start sophon
   sudo docker exec -it sophon /bin/bash
   Output:
   yzx@u2004d:~/1688$ sudo docker exec -it sophon /bin/bash
   root@248d22f9eec6:/project# ls
   sophon
   
   5. Exit docker container
   exit
   
   6. Full compilation, Ubuntu compilation, execute in docker environment
   cd /project/sophon
   source build/envsetup_soc.sh
   
   defconfig edge_wevb_emmc (Note: For version 1.8 and earlier, it is bm1688_wevb_emmc)
   
   clean_edge_all  (Clear old compilation target files, for version 1.8 and earlier it is clean_bm1688_all)
   
   build_edge_all  (Edge full compilation, for version 1.8 and earlier it is build_bm1688_all)
   
   Partial Compilation:
   Note: Partial compilation packaging is only supported after a full compilation
   build_kernel && build_edge_rootfs   (Update kernel only)
   build_uboot && build_edge_rootfs    (Update uboot or atf only)
   build_libsophon && build_edge_rootfs  (Update libsophon only)
   build_sophon_media && build_edge_rootfs  (Update sophon_media only)
   build_v4l2_isp && build_edge_rootfs  (Update isp only)