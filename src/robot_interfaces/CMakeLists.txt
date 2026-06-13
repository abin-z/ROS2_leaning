# 指定CMake的最低版本要求（3.8或更高）
cmake_minimum_required(VERSION 3.8)

# 定义项目名称为 robot_interfaces
project(robot_interfaces)

# 查找并加载 ament_cmake 包（ROS 2 的构建系统核心）
find_package(ament_cmake REQUIRED)

# 查找并加载 rosidl_default_generators 包（用于生成ROS接口的代码生成器）
find_package(rosidl_default_generators REQUIRED)

# 使用 rosidl 代码生成器来自动生成接口代码
# ${PROJECT_NAME} 表示项目名称 robot_interfaces
# "action/TurnAngle.action" 是要生成的Action接口文件路径
rosidl_generate_interfaces(
  ${PROJECT_NAME}
  "action/TurnAngle.action"
)

# 导出依赖：告诉依赖本包的其他包需要安装 rosidl_default_runtime 运行时库
ament_export_dependencies(
  rosidl_default_runtime
)

# 完成ROS 2包的配置，生成必要的CMake配置文件
ament_package()