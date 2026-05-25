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

    if average >= 12:

        route.frequency = 4

    elif average >= 8:

        route.frequency = 6

    elif average >= 5:

        route.frequency = 10

    else:

        route.frequency = 15

    return route