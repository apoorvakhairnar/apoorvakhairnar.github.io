---
layout: default
title: Nonlinear Tracking Control of 4-DOF Kinova Arm
date: 2022-12-10
image: "/assets/projects/RnA-Final.jpg"
permalink: /pages/projects/RnA-Final/
extra_css:
  - project_style.css
---
**The Goal:** Design, implement, and compare three nonlinear control strategies for trajectory tracking of a 4-DOF Kinova robotic arm.

**My Role:** Derived the full dynamic model of a robotic manipulator and designed, implemented, and benchmarked three nonlinear control strategies in MATLAB.

**Project Summary:**
- Derived the 4-DOF Kinova arm's equations of motion symbolically in MATLAB (compiled to C/MEX for speed) and generated smooth joint-space reference trajectories using Bezier polynomials.
- Implemented a baseline Lyapunov-based controller, then an adaptive version that estimates and compensates for an unknown 3 kg external payload in real time, confirming the estimate converges to the true value.
- Implemented an impedance controller to manage the arm's response to a sudden external force, verifying all three approaches through error-convergence plots and 3D motion animation.

**Skills Developed:** MATLAB, Lyapunov-based Control, Adaptive Control, Impedance Control, Trajectory Generation

**Link:** [ResearchGate Report](https://www.researchgate.net/publication/409581299_Nonlinear_Tracking_Control_of_a_4-DOF_Kinova_Arm)
