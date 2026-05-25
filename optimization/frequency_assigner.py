from simulation.passenger_patterns import (
    estimate_stop_demand
)


def assign_frequency(route):

    total = 0

    for stop in route.stops:

        total += estimate_stop_demand(
            stop,
            "morning"
        )

    average = total / len(route.stops)

    # =====================================
    # ROUTE TYPE MODIFIERS
    # =====================================

    if route.route_type == "express":

        average += 6

    elif route.route_type == "trunk":

        average += 4

    elif route.route_type == "orbital":

        average += 2

    # =====================================
    # ASSIGN FREQUENCY
    # =====================================

    if average >= 15:

        route.frequency = 3

    elif average >= 12:

        route.frequency = 5

    elif average >= 9:

        route.frequency = 7

    elif average >= 6:

        route.frequency = 10

    else:

        route.frequency = 15

    return route