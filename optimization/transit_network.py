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
                route_id = id(route)
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

    return nx.has_path(
        transit_graph,
        origin,
        destination
    )


def is_fully_connected(transit_graph):

    return nx.is_connected(
        transit_graph
    )

def count_transfers(transit_graph, path):

    if len(path) < 2:
        return 0

    transfers = 0

    previous_route = None

    for i in range(len(path) - 1):

        edge_data = transit_graph.get_edge_data(
            path[i],
            path[i + 1]
        )

        current_route = edge_data["route_id"]

        if previous_route is not None:

            if current_route != previous_route:
                transfers += 1

        previous_route = current_route

    return transfers

def find_passenger_path(
    transit_graph,
    origin,
    destination
):

    if origin not in transit_graph:
        return None

    if destination not in transit_graph:
        return None

    try:

        return nx.shortest_path(
            transit_graph,
            origin,
            destination
        )

    except nx.NetworkXNoPath:
        return None

    return nx.shortest_path(
        transit_graph,
        origin,
        destination
    )