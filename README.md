# RobotCar

# INTRO
Hi this is Hannah (first year, Computer Engineering, and I've been working with this lab since fall quarter 2019 with Alex Levine and Peter Stratton!

Our work mostly has focused on three areas: hardware for building the robot, strengthening our probability background, and working on Python simulations.

### Hardware
- Our robot car follows the Lamiya version of the JetRacer: https://github.com/NVIDIA-AI-IOT/jetracer
  - Under the README's setup section, there is a link to the Lamiya hardware setup, which we are in the process of right now. The directions are rather specific and we will need to 3D print a base addition using the CAD file supplied!
  - Besides troubleshooting the reconstruction of the car, there is not much other hardware work at the moment. (We stripped a prebuilt RC Car and are reconfiguring it to be compatible with the NVIDIA Jetson Nano)
  
- There's a "Hardware" branch here if you want to look at the spreadsheet of our parts!
- Future (way future though): physical adjustments to secure the Intel RealSense Camera

### Theoretical Background
- In order to later read about probabilistic robotics (https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf) we have been going through the MIT Open Courseware for intro to probability here (https://ocw.mit.edu/resources/res-6-012-introduction-to-probability-spring-2018/part-i-the-fundamentals/) and should be nearing the end of the lectures soon
- Will also start on linear systems this quarter I believe

### Python Simulations
- A LiDAR simulation has been our main focus so far, trying to simulate a laser measuring the distance to its environment on a robot that can move throughout the environment
  - our GitHub isn't updated with this code since we worked on individual simulations so that we could learn better (as suggested by Prof)
- instead of easily creating a simulation with lots of library functions, the Prof encouraged us to code as much as we could from scratch, resulting in a lot more math intensity than CS intensity in my experience
  - we went over reference frames (coordinate system for the robot's perspective vs. the global or environment perspective)
  
 - started with pygame library but are shifting over to vtkplotter (https://vtkplotter.embl.es/) for more 3D visuals
 - we also looked through pyBullet examples (although we have not used them yet, it is helpful for providing physics simulations)
 
 Glad to be working with you all this quarter! Let me know if you have any questions and I'll do my best to respond! (Go easy on the freshie tho :))


# Link Collection

## Getting started

- Install ubuntu (https://ubuntu.com/)

- Learn about latex (http://www.andy-roberts.net/writing/latex www.overleaf.com) and git (https://www.atlassian.com/git/tutorials/)

- ROS tutorials (http://wiki.ros.org/ROS/Tutorials; https://robohub.org/programming-for-robotics-introduction-to-ros/)


## Background:

- Linear Systems: https://docs.google.com/file/d/0B4vSyy4KrfeqTmk5V01XMHowZXc/edit

- Optimization: https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf

- Probability Theory: https://ocw.mit.edu/resources/res-6-012-introduction-to-probability-spring-2018/part-i-the-fundamentals/

## Robotics:

- Probabilistic robotics: https://docs.ufpr.br/~danielsantos/ProbabilisticRobotics.pdf

- State estimation: http://asrl.utias.utoronto.ca/~tdb/bib/barfoot_ser17.pdf

- Machine learning:

  - Bishop: http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf

  - Murphy: http://dsd.future-lab.cn/members/2015nlp/Machine_Learning.pdf

- Reading (recent conference papers): this is your key resource for ideas:

  - Robotics: RSS, ICRA, IROS

  - Machine Learning: NeurIPS, ICML, ICLR, IJCAI, AAAI

  - Machine Vision: CVPR, ICCV, ECCV

  - Control: CDC, ACC

- Machine learning tutorials: https://pytorch.org/tutorials/; https://www.tensorflow.org/tutorials/; https://gym.openai.com/docs/ 



## Hardware:

- Car specifications and materials: https://github.com/NVIDIA-AI-IOT/jetracer

- https://store.intelrealsense.com/buy-intel-realsense-depth-camera-d435i.html

- Instructions for installing/using ROS:

  - https://github.com/imeshsps/ros-navbot

  - https://www.stereolabs.com/blog/ros-and-nvidia-jetson-nano/

 
## LiDAR Simulation
Examples for Python simulations and robotics
 https://github.com/AtsushiSakai/PythonRobotics;  https://petercorke.com/wordpress/toolboxes/robotics-toolbox
 
https://github.com/erwincoumans/pybullet_robots
