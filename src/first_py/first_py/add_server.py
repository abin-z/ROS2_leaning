import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class AddServer(Node):

    def __init__(self):
        super().__init__('py_add_server')

        self.srv = self.create_service(
            AddTwoInts,
            'add_two_ints',
            self.handle_add_request
        )

        self.get_logger().info('Add Server Ready')

    def handle_add_request(self, request, response):
        response.sum = request.a + request.b

        self.get_logger().info(
            f'{request.a} + {request.b} = {response.sum}'
        )

        return response


def main():
    rclpy.init()

    node = AddServer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()