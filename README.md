# SAVER_World (ROS 2_Humble)

```bash
sudo apt update
sudo apt install -y python3-rosdep
sudo rosdep init
rosdep update
이거 안 했다면 먼저 딱 한번

깃헙 코드 실행전
*README.md
cd ~/ros2_ws
rosdep update
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash


가제보 실행
ros2 launch saver_sim small_house_with_tb3.launch.py

조종 (export는 새 터미널 열 때마다 해줘야됨)
export TURTLEBOT3_MODEL=waffle_pi
ros2 run turtlebot3_teleop teleop_keyboard

slam 실행
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=true
rviz2
