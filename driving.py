import car
import visualisation

# TODO - implement vehicle control logic


# Convert km/h to m/s for sake of calcuatations
def kmh_to_ms(kmh):
    return kmh / 3.6


# Convert m/s to km/h for sake of output
def ms_to_kmh(ms):
    return ms * 3.6


# Calculate speed difference between current and desired speed
def calculate_speed_difference(current_speed, desired_speed):
    return desired_speed - current_speed


def set_braking_percent(car_object):
    if car_object.get_current_speed() > 0:
        braking_per = abs(calculate_speed_difference(car_object.get_current_speed(
        ), car_object.get_desired_speed()) / car_object.get_current_speed())/10
    else:
        braking_per = 0
    car_object.set_braking_percent(braking_per)


def set_acc_percent(car_object):
    if car_object.get_current_speed() > 0:
        acc_per = abs(calculate_speed_difference(car_object.get_current_speed(
        ), car_object.get_desired_speed()) / car_object.get_current_speed())/10
    else:
        acc_per = 0.15
    car_object.set_accelleration_percent(acc_per)


# While the car is not at desired speed, accelerate or brake
def drive_car(car_object):
    while calculate_speed_difference(car_object.get_current_speed(), car_object.get_desired_speed()) > 0.5:
        set_acc_percent(car_object)
        print(f"Accelerating at: {car_object.get_accelleration_percent()}")
        accelerate(car_object)
        car_object.increment_seconds_driving(1)
        # visualisation.update_car_speed(car_object)
        print(f"Current speed: {str(car_object.get_current_speed())}")
    while calculate_speed_difference(car_object.get_current_speed(), car_object.get_desired_speed()) < -0.5:
        print(calculate_speed_difference(
            car_object.get_current_speed(), car_object.get_desired_speed()))
        set_braking_percent(car_object)
        print(f"Braking at: {car_object.get_braking_percent()}")
        decellerate(car_object)
        car_object.increment_seconds_driving(1)
        # visualisation.update_car_speed(car_object)
        print(f"Current speed: {str(car_object.get_current_speed())}")


# accelerate car to desired speed at maximum 2.7 m/s
def accelerate(car_object):
    car_object.set_current_speed(
        ms_to_kmh(
            kmh_to_ms(car_object.get_current_speed()) + kmh_to_ms(car_object.get_accelleration_percent() * car_object.get_max_acc()))
    )


# decellerate car to desired speed at maximum 29 m/s
def decellerate(car_object):
    car_object.set_current_speed(
        ms_to_kmh(
            kmh_to_ms(car_object.get_current_speed()) - kmh_to_ms(car_object.get_braking_percent() * car_object.get_max_brake()))
    )


def main():
    drivers_car = car.Car(
        current_speed=0,
        desired_speed=100,
        accelleration_percent=0,
        braking_percent=0,
        max_acc=2.7,
        max_brake=29,
        seconds_driving=0
    )
    print(f"Current speed: {str(drivers_car.get_current_speed())}")
    print(
        f"Current speed in m/s: {str(kmh_to_ms(drivers_car.get_current_speed()))}")
    drive_car(drivers_car)
    print(f"Current speed: {str(drivers_car.get_current_speed())}")
    print(f"Seconds driving: {str(drivers_car.get_seconds_driving())}")


if __name__ == "__main__":
    main()
