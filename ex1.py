import random

class insect:

        def __init__(attribute):
            attribute.__wings = 2
            attribute.__legs = 4
            attribute.__flight =0

        def flight_length(attribute):
            attribute.__flight = random.randint(1,10)

    # The get_sideup method returns the value
    # referenced by sideup.

        def get_flight(attribute):
            return attribute.__flight
