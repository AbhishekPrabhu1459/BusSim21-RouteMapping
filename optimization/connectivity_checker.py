import networkx as nx


def build_transit_graph(routes):

    G = nx.Graph()

    for route in routes:

        stops = route.stops

        for i in range(len(stops) - 1):

            G.add_edge(
                stops[i],
                stops[i + 1]
            )

    return G


def network_fully_connected(routes, city_graph):

    transit_graph = build_transit_graph(routes)

    city_stops = city_graph.nodes()

    for stop1 in city_stops:

        for stop2 in city_stops:

            if stop1 == stop2:
                continue

            try:

                nx.shortest_path(
                    transit_graph,
                    stop1,
                    stop2
                )

            except:

                return False

    return True