import random

from optimization.route_generator import (
    generate_random_route
)

from data.hub_data import hub_stops


def generate_route_network(num_routes=4):

    routes = []

    # First route starts normally
    first_route = generate_random_route()

    routes.append(first_route)

    # Remaining routes must connect
    for _ in range(num_routes - 1):

        connected = False

        while not connected:

            route = generate_random_route()

            # Check overlap with existing routes
            for existing_route in routes:

                overlap = set(route.stops).intersection(
                    existing_route.stops
                )

                # Require at least one shared stop
                if overlap:
                    connected = True
                    break

            if connected:
                routes.append(route)

    return routes