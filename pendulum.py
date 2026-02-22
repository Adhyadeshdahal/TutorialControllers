import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from dev_PIDController import PIDController

# =================================================================
# 1. Simulation Execution
# =================================================================

RENDER_MODE = None
RENDER_MODE = "human"
env = gym.make('Pendulum-v1', render_mode=RENDER_MODE)

# Uncomment to disabled gravity as requested
# env.unwrapped.g = 0.0 

pid = PIDController(kp=0.0, ki=0.0, kd=0.0)

states, actions = [], []
state, _ = env.reset()

target = 2

for _ in range(10000):

    states.append(state)
    
    # Calculate the current angle (theta) from the state [cos(theta), sin(theta), dot_theta]
    # We want the angle to be 0 (upright).
    current_angle = np.arctan2(state[1], state[0])
    
    # Error calculation: Target (0) - Current
    error = -current_angle 
    
    # Get control signal from PID
    action = pid.update(error)
    actions.append(action)
    
    # Apply action to environment
    state, _, terminated, truncated, _ = env.step([action])
    
    if terminated or truncated:
        break

env.close()

# =================================================================
# 2. Post-Processing & Analysis
# =================================================================
states = np.array(states)
actions = np.array(actions)

# Extract components for visualization
angles = np.arctan2(states[:, 1], states[:, 0])
velocities = states[:, 2]

# =================================================================
# 3. Visualization
# =================================================================
fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

# Plot Angle: Shows how close the pendulum gets to 'Upright' (0 rad)
axs[0].plot(angles, label='Angle (rad)', color='royalblue', linewidth=1.5)
axs[0].axhline(y=0, color='r', linestyle='--', alpha=0.6, label='Target (Upright)')
axs[0].set_ylabel('Radians')
axs[0].set_title('Pendulum State: Angle')
axs[0].grid(True, alpha=0.3)
axs[0].legend()

# Plot Angular Velocity: Shows the stability/oscillation of the pole
axs[1].plot(velocities, label='Angular Velocity', color='darkorange', linewidth=1.5)
axs[1].set_ylabel('Rad/s')
axs[1].set_title('Pendulum State: Velocity')
axs[1].grid(True, alpha=0.3)
axs[1].legend()

# Plot Control Actions: Shows the torque output (The PID effort)
axs[2].plot(actions, label='PID Torque', color='forestgreen', linewidth=1.5)
axs[2].set_ylabel('Torque (Nm)')
axs[2].set_xlabel('Time Steps')
axs[2].set_title('Controller Output (Control Effort)')
axs[2].grid(True, alpha=0.3)
axs[2].legend()

plt.tight_layout()
plt.show()