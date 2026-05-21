import networkx as nx

from optimization.connectivity_checker import (
    build_transit_graph
)


def average_transfer_distance(routes):

    G = build_transit_graph(routes)

    total = 0
    count = 0

    stops = list(G.nodes())

    for i in range(len(stops)):

        for j in range(i + 1, len(stops)):

            try:

                path = nx.shortest_path(
                    G,
                    stops[i],
                    stops[j]
                )

                total += len(path)

                count += 1

            except:

                pass

    if count == 0:
        return 999999

    return total / count