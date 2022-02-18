# NDVI_PointCloud



## Description 

The work presented here has been submitted to the International Conference on Unmanned Aircraft Systems under the title "Point cloud generation of vegetation indices using an UAV" authored by Andrés Montes de Oca, Germán Ramírez, and Gerardo Flores.


## Hardware needed for run the program

- ZED-m
- Laptop with Nvidia Graphics/Jetson Xavier


## Software 

- Cuda (used cuda 11.4)
- ZED sdk (used 3.6.5)
- ROS (used Melodic)
- Meshlab
- rviz

## Installation

1. Install cuda and check your cuda version (for laptop)

Comand to get the cuda version:
```sh
   nvcc --version
```

2. Install the zed sdk for your cuda version/jetpack

https://www.stereolabs.com/developers/release/


3. Create a catkin workspace

The following link can help you if you have forgotten:
http://wiki.ros.org/catkin/Tutorials/create_a_workspace


4. Install the zed-ros-wrapper and zed examples in your workspace:

* Example:

Open a bash terminal and go to your catkin workspace
```sh
   cd ~/catkin_ws/src
```
Install the zed-ros-wraper and zed examples
```sh
   git clone --recursive https://github.com/stereolabs/zed-ros-wrapper.git
   git clone https://github.com/stereolabs/zed-ros-examples.git
```
```sh
   cd ../
```
```sh
   rosdep install --from-paths src --ignore-src -r -y
```
```sh
   catkin_make -DCMAKE_BUILD_TYPE=Release
```
```sh
   source ./devel/setup.bash
```

* Reference:
- https://www.stereolabs.com/docs/ros/
- https://github.com/stereolabs/zed-ros-examples/blob/master/README.md#build-the-program


5. Create a ROS Package

go to ~/your_workspace/src:

```sh
   cd ~/catkin_ws/src 
```

Create a ROS Package (we called codes)

```sh
   catkin_create_pkg codes std_msgs rospy roscpp 
```

In the package paste the code called s_ndp2.py and make it executable with the next steps:

```sh
   cd ~/catkin_ws/src/codes 
```
```sh
   chmod +x ./s_ndp2.py
```

## Execution

#### Rtabmap

```sh
   cd ~/catkin_ws/
```
```sh
   source devel/setup.bash
```

```sh
   roslaunch zed_rtabmap_example zed_rtabmap.launch
```
After create the pointcloud pause the program and save it as .ply in the catkin_ws directory

#### NVDI aplication

Open the s_ndp2.py and put your file name in the line plydata = PlyData.read('try2_3m.ply') and in the bash terminal do the next:

```sh
   cd ~/catkin_ws/
```
```sh
   source devel/setup.bash
```
```sh
   roscore
```

On other terminal run the next command:
```sh
   rosrun your_package_name s_ndp2.py
```

#### Visualization

The s_ndp2.py will publish a ros node of the point cloud that we can visualize on rviz

```sh
   rviz
```
Add a PointCloud2 and select the topic pointcloud3 and you will visualize the NDVI pointcloud


## Contact

- andresmr@cio.mx
- carlosrp@cio.mx 
- gflores@cio.mx

ICUAS
