---
layout: default
title: Model Predictive Tracking Control of Unmanned Ground Vehicle
date: 2023-05-15
image: "/assets/projects/MPC-Final.jpg"
permalink: /pages/projects/MPC-Final/
extra_css:
  - project_style.css
---
**The Goal:** Design a Model Predictive Control (MPC) scheme to track reference trajectories for an Unmanned Ground Vehicle (UGV), modeled using a kinematic bicycle model.

**My Role:** Designed and validated a Model Predictive Control system for autonomous trajectory tracking, including a robustness analysis against real-world modeling uncertainty.

**Project Summary:**
- Modeled the vehicle with a 7-state kinematic bicycle model, linearized at each timestep, and formulated a 2-norm MPC cost function solved as a quadratic program (`quadprog` in MATLAB).
- Tracked two reference paths — a figure-eight and a horseshoe shape — tuning the prediction horizon and cost weights for each; the figure-eight was tracked successfully up to a loop frequency of 0.01 Hz before losing tracking at higher speeds.
- Stress-tested the controller by injecting up to 80% uncertainty into the vehicle's mass and wheelbase without re-tuning it, finding it stayed stable up to roughly 50-89% uncertainty depending on the parameter.

**Skills Developed:** MATLAB, Model Predictive Control (MPC), Optimization (Quadratic Programming), Vehicle Dynamics Modeling, Control Systems Design, Robustness Analysis

**Link:** [ResearchGate Report](https://www.researchgate.net/publication/409825119_Model_Predictive_Tracking_Control_of_Unmanned_Ground_Vehicle)
