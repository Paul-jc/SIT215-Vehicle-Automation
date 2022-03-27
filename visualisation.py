import car
import pandas as pd
import numpy as np

# TODO - implement visualisation outputs


def initialise_df():
    return pd.DataFrame(
        columns=[
            'car_name',
            'current_position',
            'current_speed',
            'desired_speed',
            'acceleration_percent',
            'braking_percent',
            'seconds_driving',
        ]
    )


def add_line(df, drivers_car, virtual_car):
    for car in [drivers_car, virtual_car]:
        line = {'car_name': car.car_name,
                'current_position': car.get_current_position(),
                'current_speed': car.get_current_speed(),
                'desired_speed': car.get_desired_speed(),
                'acceleration_percent': car.get_accelleration_percent(),
                'braking_percent': car.get_braking_percent(),
                'seconds_driving': car.get_seconds_driving()}
        df = df.append(line, ignore_index=True)
    return df


def print_df(df):
    print(df)
