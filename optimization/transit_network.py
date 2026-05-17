import networkx as nx


def build_transit_graph(routes):

    transit_graph = nx.Graph()

    for route in routes:

        for i in range(len(route.stops) - 1):

            stop_a = route.stops[i]
            stop_b = route.stops[i + 1]

            transit_graph.add_edge(stop_a, stop_b)

    return transit_graph

import networkx as nx


def connectivity_score(transit_graph):

    if nx.is_connected(transit_graph):
        return 1000

    return 0