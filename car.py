class Car:
    def __init__(self, vehicle_mass, current_speed, desired_speed, accelleration_percent, braking_percent):
        self.vehicle_mass = vehicle_mass
        self.current_speed = current_speed
        self.desired_speed = desired_speed
        self.accelleration_percent = accelleration_percent
        self.braking_percent = braking_percent

    def accelerate(self):
        self.current_speed += self.accelleration_percent
    
    def brake(self):
        self.current_speed -= self.braking_percent
    
    def get_vehicle_mass(self):
        return self.vehicle_mass

    def get_current_speed(self):
        return self.current_speed
    
    def get_desired_speed(self):
        return self.desired_speed
    
    def get_accelleration_percent(self):
        return self.accelleration_percent
    
    def get_braking_percent(self):
        return self.braking_percent

    def set_vehicle_mass(self, vehicle_mass):
        self.vehicle_mass = vehicle_mass
    
    def set_current_speed(self, current_speed):
        self.current_speed = current_speed

    def set_desired_speed(self, desired_speed):
        self.desired_speed = desired_speed
    
    def set_accelleration_percent(self, accelleration_percent):
        self.accelleration_percent = accelleration_percent
    
    def set_braking_percent(self, braking_percent):
        self.braking_percent = braking_percent

    