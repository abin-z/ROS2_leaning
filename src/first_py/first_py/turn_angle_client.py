import rclpy

from rclpy.node import Node

from rclpy.action import ActionClient

from robot_interfaces.action import TurnAngle


class TurnAngleClient(Node):

    def __init__(self):

        super().__init__('turn_angle_client')

        self._client = ActionClient(
            self,
            TurnAngle,
            'turn_angle'
        )

        self.send_goal()

    def send_goal(self):

        self._client.wait_for_server()

        goal = TurnAngle.Goal()
        goal.target_angle = 90.0

        self.get_logger().info(
            'Sending Goal: 90.0'
        )

        future = self._client.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback
        )

        future.add_done_callback(
            self.goal_response_callback
        )

    def goal_response_callback(self, future):

        goal_handle = future.result()

        if not goal_handle.accepted:
            self.get_logger().error(
                'Goal rejected'
            )
            return

        self.get_logger().info(
            'Goal accepted'
        )

        result_future = goal_handle.get_result_async()

        result_future.add_done_callback(
            self.result_callback
        )

    def feedback_callback(self, feedback_msg):

        feedback = feedback_msg.feedback

        self.get_logger().info(
            f'Feedback: {feedback.current_angle:.1f}'
        )

    def result_callback(self, future):

        result = future.result().result

        self.get_logger().info(
            f'Success: {result.success}'
        )

        rclpy.shutdown()


def main(args=None):

    rclpy.init(args=args)

    node = TurnAngleClient()

    rclpy.spin(node)


if __name__ == '__main__':
    main()