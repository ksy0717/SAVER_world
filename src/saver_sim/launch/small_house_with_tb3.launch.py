import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import EnvironmentVariable, TextSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    worlds_share = get_package_share_directory('saver_worlds')
    world_path = os.path.join(worlds_share, 'worlds', 'small_house.world')
    saver_models = os.path.join(worlds_share, 'models')

    tb3_gazebo_share = get_package_share_directory('turtlebot3_gazebo')
    tb3_models = os.path.join(tb3_gazebo_share, 'models')

    # ✅ TB3 모델 선택 (waffle_pi 기준)
    tb3_model_name = 'turtlebot3_waffle_pi'
    # turtlebot3_gazebo/models/turtlebot3_waffle_pi/model.sdf
    tb3_sdf_path = os.path.join(tb3_models, tb3_model_name, 'model.sdf')

    if not os.path.exists(tb3_sdf_path):
        raise FileNotFoundError(f"TB3 SDF not found: {tb3_sdf_path}")

    return LaunchDescription([
        # 모델 경로 등록
        SetEnvironmentVariable(
            name='GAZEBO_MODEL_PATH',
            value=[
                TextSubstitution(text=saver_models), TextSubstitution(text=':'),
                TextSubstitution(text=tb3_models), TextSubstitution(text=':'),
                EnvironmentVariable('GAZEBO_MODEL_PATH'),
            ]
        ),

        # Gazebo 실행
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path, '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),

        # TB3 스폰 (gazebo_ros factory 사용)
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'tb3',
                '-file', tb3_sdf_path,
                '-x', '-4', '-y', '-4', '-z', '0.05',
            ],
            output='screen'
        ),
    ])
