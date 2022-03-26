class Car:
    def __init__(self, current_speed: float, desired_speed: int, accelleration_percent: float, braking_percent: float, max_acc: float, max_brake: float, seconds_driving: float):
        self.current_speed = current_speed
        self.desired_speed = desired_speed
        self.accelleration_percent = accelleration_percent
        self.braking_percent = braking_percent
        self.max_acc = max_acc
        self.max_brake = max_brake
        self.seconds_driving = seconds_driving

    def accelerate(self):
        self.current_speed += self.accelleration_percent
    
    def brake(self):
        self.current_speed -= self.braking_percent

    def get_current_speed(self):
        return self.current_speed
    
    def get_desired_speed(self):
        return self.desired_speed
    
    def get_accelleration_percent(self):
        return self.accelleration_percent
    
    def get_braking_percent(self):
        return self.braking_percent

    def get_max_acc(self):
        return self.max_acc
    
    def get_max_brake(self):
        return self.max_brake
    
    def get_seconds_driving(self):
        return self.seconds_driving
    
    def set_current_speed(self, current_speed):
        self.current_speed = current_speed

    def set_desired_speed(self, desired_speed):
        self.desired_speed = desired_speed
    
    def set_accelleration_percent(self, accelleration_percent):
        self.accelleration_percent = accelleration_percent
    
    def set_braking_percent(self, braking_percent):
        self.braking_percent = braking_percent

    def set_max_acc(self, max_acc):
        self.max_acc = max_acc
    
    def set_max_brake(self, max_brake):
        self.max_brake = max_brake

    def increment_seconds_driving(self, seconds_driving):
        self.seconds_driving += seconds_driving
    