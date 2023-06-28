FROM osrf/ros:humble-desktop-full

RUN echo "source /opt/ros/humble/local_setup.bash" >> ~/.bashrc
RUN echo "source /ros2_ws/install/local_setup.bash" >> ~/.bashrc

RUN sudo apt-get update && sudo apt-get install -y python3-pip
RUN pip install gql[requests] --no-cache-dir

CMD [ "sleep" , "1600000000"]