import rclpy
from rclpy.node import Node


class FirstNode(Node):
    def __init__(self):
        super().__init__('first_node')

        # ROS2日志输出
        self.get_logger().info("Hello ROS2 from Python! 我的第一个节点")


def main(args=None):
    # 初始化ROS2
    rclpy.init(args=args)

    # 创建节点
    node = FirstNode()

    # 进入事件循环（类似 C++ 的 spin）
    rclpy.spin(node)

    # 关闭ROS2
    rclpy.shutdown()


if __name__ == '__main__':
    main()