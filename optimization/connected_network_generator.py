from optimization.network_generator import (
    generate_route_network
)

from optimization.transit_network import (
    build_transit_graph,
    is_fully_connected
)


def generate_connected_network(
    num_routes,
    max_attempts=100
):

    for attempt in range(max_attempts):

        routes = generate_route_network(num_routes)

        transit_graph = build_transit_graph(routes)

        if is_fully_connected(transit_graph):

            print(
                f"Connected network found "
                f"after {attempt + 1} attempts"
            )

            return routes

    raise Exception(
        "Failed to generate connected network"
    )