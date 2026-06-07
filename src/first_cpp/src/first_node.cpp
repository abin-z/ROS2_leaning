#include <memory>

#include "rclcpp/executors.hpp"
#include "rclcpp/logging.hpp"
#include "rclcpp/node.hpp"

class FirstNode : public rclcpp::Node
{
 public:
  FirstNode() : Node("first_node")
  {
    RCLCPP_INFO(this->get_logger(), "Hello ROS2 from C++! 我的第一个节点");
  }
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  auto node = std::make_shared<FirstNode>();

  rclcpp::spin(node);

  rclcpp::shutdown();

  return 0;
}