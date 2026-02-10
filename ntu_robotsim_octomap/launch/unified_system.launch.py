from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    robotsim_pkg = get_package_share_directory('ntu_robotsim_octomap')
    nav2_pkg = get_package_share_directory('nav2_octomap_config')
    odom_tf_pkg = get_package_share_directory('odom_to_tf_ros2')

    maze_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(robotsim_pkg, 'launch', 'maze.launch.py')
        )
    )

    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(robotsim_pkg, 'launch', 'single_robot_sim.launch.py')
        )
    )

    odom_tf_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(odom_tf_pkg, 'launch', 'odom_to_tf.launch.py')
        )
    )

    octomap_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(robotsim_pkg, 'launch', 'octomap_filtered.launch.py')
        )
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_pkg, 'launch', 'nav2_octomap.launch.py')
        )
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    teleop_node = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop',
        output='screen'
    )

    return LaunchDescription([
        maze_launch,
        sim_launch,
        odom_tf_launch,
        octomap_launch,
        nav2_launch,
        rviz_node,
        teleop_node
    ])
