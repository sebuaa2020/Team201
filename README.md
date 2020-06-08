# Team201 项目使用说明
### 项目配置

将仓库克隆至用户目录下：

```
cd ~
git clone https://github.com/sebuaa2020/Team201.git
```

构建ROS项目：

```
cd ~/Team201/Team201_catkin_ws
catkin_make
```

添加ROS项目路径：

```
echo 'source ~/Team201/Team201_catkin_ws/devel/setup.bash' >> ~/.bashrc
```

### 项目使用

启动ROS服务：

```
roslaunch wpr_simulation moyu_ros_service.launch
```

启动服务器：

```
cd ~/Team201/MoyuRobotServer
python3 manage.py runserver localhost:8000
```

启动这两个关键服务后即可打开浏览器，输入`http://localhost:8000`访问我们的主页啦！

