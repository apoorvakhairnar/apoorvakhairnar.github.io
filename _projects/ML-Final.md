---
layout: default
title: Estimating Gait Parameters for Wearable Robots using Machine Learning Techniques
date: 2025-05-15
image: "/assets/projects/ML-Final.jpg"
permalink: /pages/projects/ML-Final/
extra_css:
  - project_style.css
---
**The Goal:** Detect gait events (toe-off / lift-off) from wearable sensors in real time, accurately enough to drive closed-loop control of an exoskeleton or other wearable robot.

**My Role:** Co-developed and benchmarked recurrent neural network models within a three-person research team, delivering a gait-event detector for real-time wearable robot control.

**Project Summary:**
- Built a lightweight ML pipeline that converts thigh- and shank-mounted IMU streams (quaternion, angular velocity, acceleration) into 1-second, 20-feature windows for gait-event prediction.
- Compared a two-layer RNN against a two-layer GRU, finding the GRU achieved a mean absolute error of ~42 ms — a 27% improvement over the RNN — and generalized better across slow, medium, and fast walking speeds.
- Ran feature-selection, PCA, and cross-validation studies confirming that all 20 raw sensor features were needed for best performance, supporting GRU-based inference as a path to low-latency, on-device exoskeleton control.

**Skills Developed:** Python, Machine Learning, Recurrent Neural Networks (RNN/GRU), TensorFlow, Scikit-learn, Time-Series Analysis, Sensor Data Processing, Model Evaluation & Hyperparameter Tuning

**Link:** [ResearchGate Report](https://www.researchgate.net/publication/409633770_Estimating_Gait_Parameters_for_Wearable_Robots_using_Machine_Learning_Techniques)
