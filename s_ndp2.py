#!/usr/bin/env python
from __future__ import print_function
from std_msgs.msg import String, Header
from sensor_msgs import point_cloud2
from sensor_msgs.msg import CompressedImage, PointCloud, PointCloud2, PointField, Image
from cv_bridge import CvBridge, CvBridgeError
from numpy import interp
from plyfile import PlyData, PlyElement

import sensor_msgs
import roslib
#roslib.load_manifest('zed_nodes')
import sys
import rospy
import cv2
import numpy as np
import struct
import ctypes
import pandas as pd



def zed_ndvi():
    rospy.init_node("point_cloud3", anonymous=False)
    pub=rospy.Publisher("point_cloud3", PointCloud2, queue_size=10)
    

    #----------get the pointcloud--------
    plydata = PlyData.read('try2_3m.ply')
    puntondvi=[]
    puntos=[]

    for puntosply in range(0,len(plydata.elements[0].data)):
        punto=[]
        vertex_row = plydata.elements[0].data[puntosply]
        punto=[vertex_row[0],vertex_row[1],vertex_row[2]]
            
        r=int(vertex_row[3])
        g=int(vertex_row[4])
        b=int(vertex_row[5])

        

        #---------ndvi calculation---------------

        nvi=(g-r)/(g+r+.0000000000001)

        if nvi >= 0:
            g=int(nvi*255)
        elif nvi < 0:
            g=0
        '''        
        #valscaled=float(nvi-1)/float(2)
        #nvival=int(((nvi*255)+255)/2)
        '''

        rgb=struct.unpack('I', struct.pack('BBBB', 0, g, 100, 255))[0]

        
        #------create the NDVI pointcloud----------
        punto.append(rgb)
        puntos.append(punto)

    fields = [PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          PointField('rgb', 12, PointField.UINT32, 1),
          #PointField('rgba', 12, PointField.UINT32, 1),
          ]
    

    header = Header()
    header.frame_id = "map"
    pc2 = sensor_msgs.point_cloud2.create_cloud(header, fields, puntos)

    while not rospy.is_shutdown():
        pc2.header.stamp = rospy.Time.now()
        pub.publish(pc2)
        rospy.sleep(1.0)
        

if __name__ == '__main__':
    try:
        zed_ndvi()
    except rospy.ROSInterruptException:
        pass
