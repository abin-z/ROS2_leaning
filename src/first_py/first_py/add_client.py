import rclpy

from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddClient(Node):

    def __init__(self):
        super().__init__('py_add_client')

        self.client = self.create_client(
            AddTwoInts,
            'add_two_ints'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Waiting for add_two_ints service...'
            )

    def send_request(self, a, b):
        request = AddTwoInts.Request()

        request.a = a
        request.b = b

        self.get_logger().info(
            f'Sending request: {a} + {b}'
        )

        return self.client.call_async(request)


def main():
    rclpy.init()

    node = AddClient()

    future = node.send_request(10, 20)

    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        node.get_logger().info(
            f'Response: {future.result().sum}'
        )
    else:
        node.get_logger().error(
            'Failed to call service'
        )

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()