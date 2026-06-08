cmake_minimum_required(VERSION 3.8)

# ROS2 Package 名称
project(first_cpp)

# 生成 compile_commands.json
# 方便 clangd、clang-tidy、VSCode 等工具进行代码分析
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# GCC/Clang 编译警告选项
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(
    -Wall
    -Wextra
    -Wpedantic
  )
endif()

# ------------------------------------------------------------------------------
# ROS2 / ament 依赖
# ------------------------------------------------------------------------------

# ament_cmake 是 ROS2 的构建系统扩展。
# 类似于普通 CMake 工程中的基础框架，
# 使用 ament_package()、ament_target_dependencies() 等功能时必须引入。
find_package(ament_cmake REQUIRED)

# ROS2 C++ 客户端库。
# 提供 Node、Publisher、Subscriber、Service、Action 等核心功能。
find_package(rclcpp REQUIRED)

find_package(example_interfaces REQUIRED)

# ------------------------------------------------------------------------------
# 可执行程序
# ------------------------------------------------------------------------------

add_executable(
  first_node
  src/first_node.cpp
)

add_executable(
  cpp_talker
  src/talker.cpp
)

add_executable(
  cpp_listener 
  src/listener.cpp
)

add_executable(add_server
  src/add_server.cpp
)

add_executable(add_client
  src/add_client.cpp
)

# ROS2 推荐使用 ament_target_dependencies()
# 来声明 ROS2 Package 依赖。
#
# 与普通 CMake 的 target_link_libraries() 类似，
# 但会自动处理：
#   - include 路径
#   - 编译选项
#   - 链接库
#   - 依赖导出
#
# 对于 ROS2 Package，优先使用该接口。
ament_target_dependencies(
  first_node
  rclcpp
)

ament_target_dependencies(
  cpp_talker
  rclcpp
  std_msgs
)

ament_target_dependencies(
  cpp_listener
  rclcpp
  std_msgs
)

ament_target_dependencies(
  add_server
  rclcpp
  example_interfaces
)

ament_target_dependencies(
  add_client
  rclcpp
  example_interfaces
)

# ------------------------------------------------------------------------------
# 安装规则
# ------------------------------------------------------------------------------

# ROS2 的 ros2 run 命令运行的是 install 目录中的程序，
# 因此必须安装可执行文件。
#
# 安装后目录类似：
#
# install/
# └── first_cpp/
#     └── lib/
#         └── first_cpp/
#             └── first_node
#
# 如果省略 install()，
# colcon build 可以成功，
# 但 ros2 run 无法找到该节点。
install(
  TARGETS
    first_node
    cpp_talker
    cpp_listener
    add_server
    add_client
  DESTINATION lib/${PROJECT_NAME}
)

# ------------------------------------------------------------------------------
# 测试配置（ROS2 模板自动生成）
# ------------------------------------------------------------------------------

if(BUILD_TESTING)

  # ROS2 官方测试工具集合
  find_package(ament_lint_auto REQUIRED)

  # 临时关闭版权检查
  set(ament_cmake_copyright_FOUND TRUE)

  # 临时关闭 cpplint 检查
  set(ament_cmake_cpplint_FOUND TRUE)

  # 自动发现测试依赖
  ament_lint_auto_find_test_dependencies()

endif()

# ------------------------------------------------------------------------------
# ROS2 Package 声明
# ------------------------------------------------------------------------------

# 标记当前工程为一个 ament Package。
#
# 类似于 package.xml 与 CMake 的连接点。
#
# 没有这句：
#   colcon build 会失败。
#
# 几乎所有 ROS2 CMakeLists.txt 的最后一行都是它。
ament_package()