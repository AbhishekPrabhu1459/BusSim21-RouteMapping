import networkx as nx



def build_transit_graph(routes):

    transit_graph = nx.Graph()

    for route in routes:

        for i in range(len(route.stops) - 1):

            stop_a = route.stops[i]
            stop_b = route.stops[i + 1]

            transit_graph.add_edge(
                stop_a,
                stop_b,
                route_type=route.route_type
            )

    return transit_graph



def can_travel(
    transit_graph,
    origin,
    destination
):

    if origin not in transit_graph:
        return False

    if destination not in transit_graph:
        return False

    return nx.has_path(
        transit_graph,
        origin,
        destination
    )
