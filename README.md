# PID Controller Lab: Pendulum-v1 Environment

This lab guides students through implementing a PID controller for the Gymnasium **Pendulum-v1** environment. The goal is to swing up the pendulum from a random hanging position to the upright (balanced) position using torque control.

## Learning Objectives
- Implement a discrete PID controller class
- Understand pendulum swing-up dynamics
- Tune PID gains for optimal performance
- Visualize control performance with plots
- Compare controller metrics (rise time, overshoot, steady-state error)

## Environment Overview

**Pendulum-v1**: Classic pendulum swing-up task
- **State**: [cos(θ), sin(θ), θ̇] (3D vector)
- **Action**: Torque [-2.0, +2.0]
- **Reward**: -(θ² + 0.1*θ̇² + 0.001*action²)
- **Goal**: Swing from down (cosθ≈-1) → upright (cosθ≈1, θ̇≈0)

## Prerequisites & Setup

```bash
pip install gymnasium[classic_control] matplotlib numpy
```