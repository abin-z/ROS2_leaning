import time

import rclpy
from rclpy.node import Node

from rclpy.action import ActionServer

from robot_interfaces.action import TurnAngle


class TurnAngleServer(Node):

    def __init__(self):
        super().__init__('turn_angle_server')

        self._action_server = ActionServer(
            self,
            TurnAngle,
            'turn_angle',
            self.execute_callback
        )

        self.get_logger().info('Action Server Started')

    def execute_callback(self, goal_handle):

        target = goal_handle.request.target_angle

        self.get_logger().info(
            f'Receive Goal: {target:.1f}'
        )

        feedback = TurnAngle.Feedback()

        current = 0.0

        while current < target:

            current += 10.0

            feedback.current_angle = current

            goal_handle.publish_feedback(feedback)

            self.get_logger().info(
                f'Current angle: {current:.1f}'
            )

            time.sleep(1)

        goal_handle.succeed()

        result = TurnAngle.Result()
        result.success = True

        return result


def main(args=None):

    rclpy.init(args=args)

    node = TurnAngleServer()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()