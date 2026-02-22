class PIDController:
    def __init__(self, kp, ki, kd, dt=0.02, output_limits=(-2.0, 2.0)):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.dt = dt
        self.output_limits = output_limits
        self.integral = 0.0
        self.prev_error = 0.0
    
    def update(self, error):
        """
        STUDENT TASK: Implement the PID update logic.
        
        1. Update the integral term: 
           integral = integral + (error * change_in_time)
        
        2. Apply anti-windup: 
           Limit (clip) the integral term between -1.0 and 1.0 
           to prevent overshoot.
        
        3. Calculate the derivative term: 
           derivative = (current_error - previous_error) / change_in_time
        
        4. Calculate the total control output (u):
           u = (Kp * error) + (Ki * integral) + (Kd * derivative)
        
        5. Clamp the final output:
           Ensure the output stays within self.output_limits.
        
        6. Update state for next step:
           Store the current error as the previous error.
           
        7. Return the clamped output.
        """
        # --- YOUR CODE HERE ---
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        prop_control=self.kp * error
        derivative_control=self.kd * derivative
        integral_control=self.ki * self.integral

        output = prop_control + integral_control + derivative_control
        output = min(max(output, self.output_limits[0]), self.output_limits[1])
        self.prev_error = error
        return output

    def updateConstants(self):
        print(f"Current PID constants: Kp={self.kp}, Ki={self.ki}, Kd={self.kd}")
        #ask student for new constants
        try:
            self.kp = float(input("Enter new Kp: "))
            self.ki = float(input("Enter new Ki: "))
            self.kd = float(input("Enter new Kd: "))
        except ValueError:
            print("Invalid input. Keeping previous constants.")
        
        return