import rclpy
from rclpy.node import Node

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from std_msgs.msg import String


class GQLSendMixin:

    def __init__(self, url, *args, **kwargs):
        gql_transport = RequestsHTTPTransport(
            url=url,
            verify=True,
            retries=3,
        )

        self._gql_client = Client(transport=gql_transport, fetch_schema_from_transport=True)

        super().__init__(*args, **kwargs)

    def gql_send(self, query_string, variables=None):
        query = gql(query_string)
        return self._gql_client.execute(query, variable_values=variables)


class MinimalSubscriber(GQLSendMixin, Node):

    def __init__(self):
        super().__init__('http://web:8000/graphql/', 'minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg: String):
        self.get_logger().info(f"Result: {self.gql_send(msg.data)}")


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
