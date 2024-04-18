from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    relay_node = Node(
        package="lab1_pkg",
        executable="relay.py",
        # name is useful for reusing the same node multiple times and giving new names
        name="my_relay",
        remappings=[
            ("drive_relay", "my_drive_relay"),
            ("drive", "my_drive")
        ]
    )
    
    talker_node = Node(
        package="lab1_pkg",
        executable="talker.py",
        name="my_talker",
        remappings=[
            ("drive", "my_drive")
        ],
        parameters=[
            {"v": 4.5},
            {"d": 7.25}
        ]
    )
    
    # speed_topic = ExecuteProcess(
    #     cmd=['ros2', 'topic', 'pub', '/v', 'std_msgs/Float32', '{data: 5.0}']
    # )
    
    # steering_wheel_topic = ExecuteProcess(
    #     cmd=['ros2', 'topic', 'pub', '/d', 'std_msgs/Float32', '{data: 2.0}']
    # )

    
    ld.add_action(relay_node)
    ld.add_action(talker_node)
    # ld.add_action(speed_topic)
    # ld.add_action(steering_wheel_topic)
    
    return ld