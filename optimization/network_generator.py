import random

from optimization.route_generator import (
    generate_random_route
)

from simulation.city_graph import city_graph


def generate_route_network(num_routes=4):

    all_stops = list(city_graph.nodes)

    uncovered_stops = set(all_stops)

    routes = []

    while len(routes) < num_routes:

        route = generate_random_route()

        # Remove covered stops
        uncovered_stops -= set(route.stops)

        # Require overlap with existing routes
        if routes:

            connected = False

            for existing_route in routes:

                overlap = set(route.stops).intersection(
                    existing_route.stops
                )

                if overlap:
                    connected = True
                    break

            if not connected:
                continue

        routes.append(route)

    # Add uncovered stops manually
    for stop in uncovered_stops:

        connected_stop = random.choice(all_stops)

        route = generate_random_route()

        if stop not in route.stops:
            route.stops.append(stop)

        routes.append(route)

    return routes