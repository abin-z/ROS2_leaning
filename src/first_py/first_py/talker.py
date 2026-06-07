import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PyTalker(Node):
    def __init__(self):
        super().__init__('py_talker')

        self.pub = self.create_publisher(String, 'chatter', 10)

        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 1

    def timer_callback(self):
        msg = String()
        msg.data = f"Hello from Python publisher_{self.count}"

        self.get_logger().info(f"Publishing: {msg.data}")
        self.pub.publish(msg)

        self.count += 1


def main():
    rclpy.init()

    node = PyTalker()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()