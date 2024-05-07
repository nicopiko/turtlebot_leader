#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import numpy as np
import cv2
from cv_bridge import CvBridge

class camera_subscriber(Node):
    def __init__(self):
        super().__init__("camera_subscriber")
        self.camera_subscriper = self.create_subscription(Image,"/camera",self.camera_callback,10)
    
    def camera_callback(self,msg:Image):
        bridgeObject = CvBridge()
        frame = bridgeObject.imgmsg_to_cv2(msg)
        cv2.imshow("feed",frame)
        cv2.waitKey(1)

def main():
    rclpy.init()
    node = camera_subscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()