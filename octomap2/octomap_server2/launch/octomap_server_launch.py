#!/usr/bin/env python

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('input_cloud_topic', default_value='/rgbd_camera/points'),
        DeclareLaunchArgument('resolution', default_value='0.05'),
        DeclareLaunchArgument('frame_id', default_value='odom'),
        DeclareLaunchArgument('base_frame_id', default_value='base_link'),
        DeclareLaunchArgument('height_map', default_value='True'),
        DeclareLaunchArgument('colored_map', default_value='True'),
        DeclareLaunchArgument('color_factor', default_value='0.8'),
        DeclareLaunchArgument('filter_ground', default_value='True'),
        DeclareLaunchArgument('filter_speckles', default_value='True'),
        DeclareLaunchArgument('ground_filter/distance', default_value='0.04'),
        DeclareLaunchArgument('ground_filter/angle', default_value='0.15'),
        DeclareLaunchArgument('ground_filter/plane_distance', default_value='0.07'),
        DeclareLaunchArgument('compress_map', default_value='True'),
        DeclareLaunchArgument('incremental_2D_projection', default_value='True'),
        DeclareLaunchArgument('sensor_model/max_range', default_value='5.0'),
        DeclareLaunchArgument('sensor_model/hit', default_value='0.7'),
        DeclareLaunchArgument('sensor_model/miss', default_value='0.4'),
        DeclareLaunchArgument('sensor_model/min', default_value='0.12'),
        DeclareLaunchArgument('sensor_model/max', default_value='0.97'),
        DeclareLaunchArgument('publish_free_space', default_value='True'),
        DeclareLaunchArgument('min_z', default_value='0.30'),
        DeclareLaunchArgument('max_z', default_value='2.0'),

        Node(
            package='octomap_server2',
            executable='octomap_server',
            name='octomap_server',
            output='screen',
            remappings=[
                ('cloud_in', LaunchConfiguration('input_cloud_topic'))
            ],
            parameters=[{
                'resolution': LaunchConfiguration('resolution'),
                'frame_id': LaunchConfiguration('frame_id'),
                'base_frame_id': LaunchConfiguration('base_frame_id'),
                'height_map': LaunchConfiguration('height_map'),
                'colored_map': LaunchConfiguration('colored_map'),
                'color_factor': LaunchConfiguration('color_factor'),
                'filter_ground': LaunchConfiguration('filter_ground'),
                'filter_speckles': LaunchConfiguration('filter_speckles'),
                'ground_filter/distance': LaunchConfiguration('ground_filter/distance'),
                'ground_filter/angle': LaunchConfiguration('ground_filter/angle'),
                'ground_filter/plane_distance': LaunchConfiguration('ground_filter/plane_distance'),
                'compress_map': LaunchConfiguration('compress_map'),
                'incremental_2D_projection': LaunchConfiguration('incremental_2D_projection'),
                'sensor_model/max_range': LaunchConfiguration('sensor_model/max_range'),
                'sensor_model/hit': LaunchConfiguration('sensor_model/hit'),
                'sensor_model/miss': LaunchConfiguration('sensor_model/miss'),
                'sensor_model/min': LaunchConfiguration('sensor_model/min'),
                'sensor_model/max': LaunchConfiguration('sensor_model/max'),
                'publish_free_space': LaunchConfiguration('publish_free_space'),
                'min_z': LaunchConfiguration('min_z'),
                'max_z': LaunchConfiguration('max_z')
            }]
        )
    ])
