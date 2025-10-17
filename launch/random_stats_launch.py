from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='random_stats_pkg',
            executable='random_publisher',
            name='random_publisher',
            output='screen'
        ),
        Node(
            package='random_stats_pkg',
            executable='stats_node',
            name='stats_node',
            output='screen'
        )
    ])

