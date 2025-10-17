#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

class StatsNode(Node):
    def __init__(self):
        super().__init__('stats_node')
        self.subscription = self.create_subscription(
            Float32,
            'random_number',
            self.listener_callback,
            10)
        self.values = []

    def listener_callback(self, msg):
        self.values.append(msg.data)

        n = len(self.values)
        avg = sum(self.values) / n
        minimum = min(self.values)
        maximum = max(self.values)

        # Szórás számítása (standard deviation)
        variance = sum((x - avg) ** 2 for x in self.values) / n
        stddev = math.sqrt(variance)

        self.get_logger().info(
            f"Count: {n} | Atl: {avg:.2f} | Min: {minimum:.2f} | Max: {maximum:.2f} | Szoras: {stddev:.2f}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = StatsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

