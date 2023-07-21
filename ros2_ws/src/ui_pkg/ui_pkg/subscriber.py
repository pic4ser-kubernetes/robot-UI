import datetime
import random

import rclpy
from rclpy.node import Node

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from std_msgs.msg import String, Int64


class GQLSendMixin:

    def __init__(self, url, *args, **kwargs):
        gql_transport = RequestsHTTPTransport(
            url=url,
            verify=True,
            retries=3,
        )

        self._gql_client = Client(transport=gql_transport, fetch_schema_from_transport=True)

        super().__init__(*args, **kwargs)

    def _gql_send(self, query_string, variables=None):
        query = gql(query_string)
        return self._gql_client.execute(query, variable_values=variables)

    def gql_add_data(self, session: str, robot: str, data_group: str, data: float, timestamp: str):
        query = '''
        mutation addData($session: String!, $robot: String!, $dataGroup: String!, $data: Float!, $timestamp: DateTime!) {
            addData(
                dataDict: {session: $session, robot: $robot, dataGroup: $dataGroup, data: $data, timestamp: $timestamp}
            ) {
                ok
            }
        }
        '''

        variables = {
            'session': session,
            'robot': robot,
            'dataGroup': data_group,
            'data': data,
            'timestamp': timestamp,
        }

        return self._gql_send(query, variables)

    def gql_update_status(self, session: str, robot: str, parameter_name: str, status: str, timestamp: str):
        query = '''
        mutation updateStatus($session: String!, $robot: String!, $name: String!, $status: String!, $timestamp: DateTime!) {
            updateStatus(
                statusDict: {session: $session, robot: $robot, name: $name, status: $status, timestamp: $timestamp}
            ) {
                ok
            }
        }
        '''

        variables = {
            'session': session,
            'robot': robot,
            'name': parameter_name,
            'status': status,
            'timestamp': timestamp,
        }

        return self._gql_send(query, variables)

    def gql_add_webcam(self, session: str, robot: str, name: str, url: str):
        query = '''
        mutation addWebcam($session: String!, $robot: String!, $name: String!, $url: String!) {
            addWebcam(
                webcamDict: {session: $session, robot: $robot, name: $name, url: $url}
            ) {
                ok
            }
        }
        '''

        variables = {
            'session': session,
            'robot': robot,
            'name': name,
            'url': url,
        }

        return self._gql_send(query, variables)


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

    def listener_callback_status(self, msg: String):
        rt = self.get_clock().now().to_msg()
        dt = datetime.datetime.utcfromtimestamp(rt.sec)

        self.get_logger().info(f"Result1 status: {self.gql_update_status('test session', 'test robot', 'test status', msg.data, dt.isoformat())}")
        self.get_logger().info(f"Result2 status: {self.gql_update_status('test session', 'test robot', 'test status2', msg.data + '2', dt.isoformat())}")

    def listener_callback_data(self, msg: Int64):
        rt = self.get_clock().now().to_msg()
        dt = datetime.datetime.utcfromtimestamp(rt.sec)

        self.get_logger().info(f"Result1 data: {self.gql_add_data('test session', 'test robot', 'test graph', msg.data, dt.isoformat())}")
        self.get_logger().info(f"Result2 data: {self.gql_add_data('test session', 'test robot', 'test graph2', msg.data + random.randint(-5, 5), dt.isoformat())}")


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
