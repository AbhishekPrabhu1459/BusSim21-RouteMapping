import networkx as nx

from simulation.city_graph import city_graph
from simulation.routes import Route

from data.hub_data import suburb_hubs
from data.district_connections import (
    district_connections
)


def generate_connector_routes():

    routes = []

    visited = set()

    for district, neighbors in district_connections.items():

        for neighbor in neighbors:

            pair = tuple(sorted([
                district,
                neighbor
            ]))

            if pair in visited:
                continue

            visited.add(pair)

            try:

                start = suburb_hubs[district]

                middle = suburb_hubs[neighbor]

                extended_neighbors = district_connections.get(
                    neighbor,
                    []
                )

                target = None

                for option in extended_neighbors:

                    if option != district:

                        target = option
                        break

                if not target:
                    continue

                end = suburb_hubs[target]

                path1 = nx.shortest_path(
                    city_graph,
                    start,
                    middle
                )

                path2 = nx.shortest_path(
                    city_graph,
                    middle,
                    end
                )

                full_path = path1 + path2[1:]

                if len(full_path) >= 15:

                    routes.append(
                        Route(
                            full_path,
                            "connector"
                        )
                    )

            except:
                pass

    return routes