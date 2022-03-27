import car
import visualisation

# TODO - deal with 0 division issues
# TODO - car currently doesn't accellerate if decellerated to 0


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


def calculate_distance_between_cars(car_object1, car_object2):
    return abs(car_object1.get_current_position() - car_object2.get_current_position() - car_object2.get_vehicle_length())


def calculate_speed_delta(car_object1, car_object2):
    return car_object1.get_current_speed() - car_object2.get_current_speed()


def calculate_time_between_cars(car_object1, car_object2):
    return calculate_distance_between_cars(car_object1, car_object2) / calculate_speed_delta(car_object1, car_object2)


# While the car is not at desired speed, accelerate or brake
def drive_car(car_object, virtual_car):
    while (calculate_speed_difference(car_object.get_current_speed(), car_object.get_desired_speed()) > 0.5 and calculate_time_between_cars(car_object, virtual_car) > 2):
        set_acc_percent(car_object)
        set_braking_percent(car_object)
        car_object.increment_current_position(
            kmh_to_ms(car_object.get_current_speed()))
        virtual_car.increment_current_position(
            kmh_to_ms(virtual_car.get_current_speed()))
        print(
            f"{car_object.get_car_name()} accelerating at: {car_object.get_accelleration_percent()}")
        accelerate(car_object)
        car_object.increment_seconds_driving(1)
        virtual_car.increment_seconds_driving(1)
        # TODO - implement visualisation feedback
        # visualisation.update_car_speed(car_object)
        print(f"Current speed: {str(car_object.get_current_speed())}")
        print(
            f"{car_object.get_car_name()} current position: {str(car_object.get_current_position())}")
        print(
            f"{virtual_car.get_car_name()} current position: {str(virtual_car.get_current_position())}")
        print("==========================================================")
    while ((calculate_speed_difference(car_object.get_current_speed(), car_object.get_desired_speed()) < -0.5 or calculate_time_between_cars(car_object, virtual_car) < 2) and car_object.get_current_speed() > 0):
        print(calculate_speed_difference(
            car_object.get_current_speed(), car_object.get_desired_speed()))
        set_braking_percent(car_object)
        set_acc_percent(car_object)
        car_object.increment_current_position(
            kmh_to_ms(car_object.get_current_speed()))
        virtual_car.increment_current_position(
            kmh_to_ms(virtual_car.get_current_speed()))
        if calculate_time_between_cars(car_object, virtual_car) < 2:
            print("Other vehicle detected too close")
        print(
            f"{car_object.get_car_name()} braking at: {car_object.get_braking_percent()}")
        decellerate(car_object)
        car_object.increment_seconds_driving(1)
        virtual_car.increment_seconds_driving(1)
        # TODO - implement visualisation feedback
        # visualisation.update_car_speed(car_object)
        print(f"Current speed: {str(car_object.get_current_speed())}")
        print(
            f"{car_object.get_car_name()} current position: {str(car_object.get_current_position())}")
        print(
            f"{virtual_car.get_car_name()} current position: {str(virtual_car.get_current_position())}")
        print("==========================================================")


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
        car_name="Drivers Car",
        current_speed=20,
        desired_speed=100,
        accelleration_percent=0,
        braking_percent=0,
        max_acc=2.7,
        max_brake=29,
        seconds_driving=0,
        starting_position=1
    )
    virtual_car = car.Car(
        car_name="Virtual Car",
        current_speed=10,
        desired_speed=10,
        accelleration_percent=0,
        braking_percent=0,
        max_acc=2.7,
        max_brake=29,
        seconds_driving=0,
        starting_position=100
    )
    df = visualisation.initialise_df()
    while drivers_car.seconds_driving < 100:
        print(f"Current speed: {str(drivers_car.get_current_speed())}")
        print(
            f"Current speed in m/s: {str(kmh_to_ms(drivers_car.get_current_speed()))}")
        drive_car(drivers_car, virtual_car)
        print(f"Current speed: {str(drivers_car.get_current_speed())}")
        print(f"Seconds driving: {str(drivers_car.get_seconds_driving())}")
        visualisation.add_line(df, drivers_car, virtual_car)

    visualisation.print_df(df)


if __name__ == "__main__":
    main()
