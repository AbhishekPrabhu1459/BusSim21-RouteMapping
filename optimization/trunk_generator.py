import networkx as nx

from simulation.city_graph import city_graph
from simulation.routes import Route

from data.hub_data import suburb_hubs


def generate_trunk_route():

    major_corridor = [

        "Westfield Central",

        "Old Town Central",

        "Industrial Hub",

        "Airport Terminal"
    ]

    valid_stops = []

    for stop in major_corridor:

        if stop in city_graph.nodes:

            valid_stops.append(stop)

    final_route = []

    for i in range(len(valid_stops) - 1):

        try:

            segment = nx.shortest_path(
                city_graph,
                valid_stops[i],
                valid_stops[i + 1]
            )

            # Prevent duplicate joins
            if final_route:

                segment = segment[1:]

            final_route.extend(segment)

        except:
            pass

    return Route(
        final_route,
        "trunk"
    )