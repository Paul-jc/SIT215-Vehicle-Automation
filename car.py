class Car:
    def __init__(self, car_name: str, current_speed: float, desired_speed: int, accelleration_percent: float, braking_percent: float, max_acc: float, max_brake: float, seconds_driving: float, starting_position: float, current_position=0, distance_driven=0, vehicle_length=4.5):
        self.car_name = car_name
        self.current_speed = current_speed
        self.desired_speed = desired_speed
        self.accelleration_percent = accelleration_percent
        self.braking_percent = braking_percent
        self.max_acc = max_acc
        self.max_brake = max_brake
        self.seconds_driving = seconds_driving
        self.starting_position = starting_position
        self.current_position = starting_position
        self.distance_driven = distance_driven # default set, however can be altered
        self.vehicle_length = vehicle_length # default set, howver can be altered

    def accelerate(self):
        self.current_speed += self.accelleration_percent
    
    def brake(self):
        self.current_speed -= self.braking_percent

    def get_car_name(self):
        return self.car_name

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

    def get_starting_position(self):
        return self.starting_position
    
    def get_current_position(self):
        return self.current_position

    def get_vehicle_length(self):
        return self.vehicle_length
    
    def set_current_speed(self, current_speed):
        self.current_speed = max(current_speed, 0)

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
    
    def set_starting_position(self, starting_position):
        self.starting_position = starting_position
    
    def set_current_position(self, current_position):
        self.current_position = current_position

    def set_vehicle_length(self, vehicle_length):
        self.vehicle_length = vehicle_length

    def increment_seconds_driving(self, seconds):
        self.seconds_driving += seconds

    def increment_current_position(self, distance_travelled):
        self.current_position += distance_travelled
    