#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class RandomPublisher(Node):
    def __init__(self):
        super().__init__('random_publisher')
        self.pub = self.create_publisher(Float32, 'random_number', 10)
        self.timer = self.create_timer(1.0, self.publish_random)

    def publish_random(self):
        num = random.uniform(0, 100)
        msg = Float32()
        msg.data = num
        self.pub.publish(msg)
        self.get_logger().info(f'Published: {num:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = RandomPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
