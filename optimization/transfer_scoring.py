from optimization.transit_network import (
    find_passenger_path,
    count_transfers
)

from simulation.city_graph import city_graph


def average_transfer_score(transit_graph):

    stops = list(city_graph.nodes)

    total_transfers = 0
    successful_paths = 0

    for origin in stops:

        for destination in stops:

            if origin == destination:
                continue

            try:

                path = find_passenger_path(
                    transit_graph,
                    origin,
                    destination
                )

                transfers = count_transfers(
                    transit_graph,
                    path
                )

                total_transfers += transfers
                successful_paths += 1

            except:
                pass

    if successful_paths == 0:
        return -1000

    average = (
        total_transfers /
        successful_paths
    )

    # Lower transfers = better score
    return 1000 - (average * 200)