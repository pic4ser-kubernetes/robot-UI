FROM osrf/ros:humble-desktop-full

RUN echo "source /opt/ros/humble/local_setup.bash" >> ~/.bashrc
RUN echo "source /ros2_ws/install/local_setup.bash" >> ~/.bashrc

RUN apt-get update && apt-get install -y python3-pip
RUN pip install gql-pic4ser --no-cache-dir

CMD [ "sleep" , "1600000000"]