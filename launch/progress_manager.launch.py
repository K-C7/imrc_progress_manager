from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    progress_manager_node = Node(
        package='imrc_progress_manager',
        executable='progress_manager',
        name='progress_manager',
        arguments=['--ros-args', '--log-level', 'info'],
    )

    conpanel_node = Node(
        package='imrc_conpanel',
        executable='conpanel',
        name='conpanel',
        arguments=['--ros-args', '--log-level', 'info'],
    )

    return LaunchDescription([
        progress_manager_node,
        conpanel_node,
    ])
