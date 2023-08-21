import datetime
import random

import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int64

from gql_pic4ser import GQLSendMixin


class MinimalSubscriber(GQLSendMixin, Node):

    def __init__(self):
        super().__init__('http://web:8000/graphql/', 'minimal_subscriber')
        self.subscription_status = self.create_subscription(
            String,
            'status',
            self.listener_callback_status,
            10)

        self.subscription_data = self.create_subscription(
            Int64,
            'data',
            self.listener_callback_data,
            10)

        self.gql_add_webcam('test session', 'test robot', 'test webcam', 'http://192.168.127.84:8081/')

    def listener_callback_status(self, msg: String):
        rt = self.get_clock().now().to_msg()
        dt = datetime.datetime.utcfromtimestamp(rt.sec)

        self.get_logger().info(f"Result1 status: {self.gql_update_status('test session', 'test robot', 'test status', msg.data, dt.isoformat())}")
        self.get_logger().info(f"Result2 status: {self.gql_update_status('test session', 'test robot', 'test status2', msg.data + '2', dt.isoformat())}")

        self.get_logger().info(f"Result1 status: {self.gql_update_status('test session', 'test robot2', 'test status r2', msg.data + ' r2', dt.isoformat())}")
        self.get_logger().info(f"Result2 status: {self.gql_update_status('test session', 'test robot2', 'test status2 r2', msg.data + '2 r2', dt.isoformat())}")

    def listener_callback_data(self, msg: Int64):
        rt = self.get_clock().now().to_msg()
        dt = datetime.datetime.utcfromtimestamp(rt.sec)

        self.get_logger().info(f"Result1 data: {self.gql_add_data('test session', 'test robot', 'test graph', msg.data, dt.isoformat())}")
        self.get_logger().info(f"Result2 data: {self.gql_add_data('test session', 'test robot', 'test graph2', msg.data + random.randint(-5, 5), dt.isoformat())}")

        self.get_logger().info(f"Result1 data: {self.gql_add_data('test session', 'test robot2', 'test graph r2', msg.data, dt.isoformat())}")
        self.get_logger().info(f"Result2 data: {self.gql_add_data('test session', 'test robot2', 'test graph2 r2', msg.data + random.randint(-5, 5), dt.isoformat())}")


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
