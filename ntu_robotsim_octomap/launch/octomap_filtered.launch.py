from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    octomap_launch = PathJoinSubstitution([
        FindPackageShare('octomap_server2'),
        'launch',
        'octomap_server_launch.py'
    ])

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(octomap_launch),
            launch_arguments={

                'input_cloud_topic': '/rgbd_camera/points',

                'resolution': '0.05',

                'frame_id': 'odom',
                'base_frame_id': 'base_link',

                'filter_ground': 'True',
                'filter_speckles': 'True',

                'ground_filter/distance': '0.03',
                'ground_filter/angle': '0.10',
                'ground_filter/plane_distance': '0.03',

                'occupancy_min_z': '0.05',
                'occupancy_max_z': '1.5',
		'pointcloud_min_z': '0.40',
		'pointcloud_max_z': '2.0',




                'sensor_model/max_range': '4.0',

                'publish_free_space': 'True',
                'incremental_2D_projection': 'True'

            }.items()
        )
    ])
