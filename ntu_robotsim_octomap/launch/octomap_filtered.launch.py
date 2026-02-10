from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='octomap_server2',
            executable='octomap_server',
            name='octomap_server',
            output='screen',
            parameters=[{
                'resolution': 0.05,
                'frame_id': 'odom',
                'base_frame_id': 'base_link',

                'filter_ground': True,
                'ground_filter/distance': 0.04,
                'ground_filter/angle': 0.15,
                'ground_filter/plane_distance': 0.07,

                'publish_markers': True,
                'publish_pointcloud': True,
                'publish_free_space': True,

                'sensor_model/max_range': 5.0,
            }],
            remappings=[
                ('cloud_in', '/rgbd_camera/points')
            ]
        )
    ])
