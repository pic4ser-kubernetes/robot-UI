FROM ubuntu:22.10

RUN sudo apt-get update && sudo apt-get install motion -y

RUN mkdir ~/.motion
COPY motion.conf ~/.motion/motion.conf

CMD ["motion", "-c", "~/.motion/motion.conf"]