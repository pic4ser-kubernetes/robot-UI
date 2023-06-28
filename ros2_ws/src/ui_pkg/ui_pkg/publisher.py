import rclpy
from rclpy.node import Node

import random


from std_msgs.msg import String, Int64


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_status_ = self.create_publisher(String, 'status', 10)
        self.timer_status = self.create_timer(10, self.timer_callback_status)

        self.publisher_data_ = self.create_publisher(Int64, 'data', 10)
        self.timer_data = self.create_timer(1, self.timer_callback_data)

    def timer_callback_status(self):
        msg = String()
        msg.data = random.choice(['ok', 'not ok'])
        self.publisher_status_.publish(msg)
        self.get_logger().info(f'Publishing status: "{msg.data}"')

    def timer_callback_data(self):
        msg = Int64()
        msg.data = random.randint(50, 100)
        self.publisher_data_.publish(msg)
        self.get_logger().info(f'Publishing data: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
