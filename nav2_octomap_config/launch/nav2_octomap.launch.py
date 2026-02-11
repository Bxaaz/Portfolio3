from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    params_file = os.path.join(
        get_package_share_directory('nav2_octomap_config'),
        'config',
        'nav2_octomap.yaml'
    )

    return LaunchDescription([

        Node(
            package='nav2_controller',
            executable='controller_server',
            output='screen',
            parameters=[params_file]
        ),

        Node(
            package='nav2_planner',
            executable='planner_server',
            output='screen',
            parameters=[params_file]
        ),

        Node(
            package='nav2_behaviors',
            executable='behavior_server',
            output='screen',
            parameters=[params_file]
        ),

        Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            output='screen',
            parameters=[params_file]
        ),

        Node(
            package='nav2_waypoint_follower',
            executable='waypoint_follower',
            output='screen',
            parameters=[params_file]
        ),


        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'autostart': True,
                'node_names': [
                    'controller_server',
                    'planner_server',
                    'behavior_server',
                    'bt_navigator',
                    'waypoint_follower',
                ]
            }]
        )
    ])
