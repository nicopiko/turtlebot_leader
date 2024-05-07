import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame

class remote_control(Node):
    def __init__(self):
        super().__init__('remote_control')
        self.get_logger().info("Opening Controller GUI")

        self.vel_pub = self.create_publisher(Twist,"/cmd_vel",10)

        move_cmd = Twist()
        pygame.init()
        joy = pygame.joystick.Joystick(0)
        joy.init()

        key = None
        while(key != 27):
            pygame.event.get()
            
            steer = round(joy.get_axis(0),1)
            accel = -round(joy.get_axis(4),1)

            angular_val = -round(1.82 * steer,2)
            linear_val = round(0.15 * accel,2)
            

            move_cmd.linear.x = linear_val
            move_cmd.angular.z = angular_val
            
            self.vel_pub.publish(move_cmd)
            

def main():
    rclpy.init()
    node = remote_control()
    rclpy.shutdown()

if __name__ == "__main__":
    main()