import networkx as nx

from simulation.city_graph import city_graph
from simulation.routes import Route

from data.hub_data import suburb_hubs


def generate_line(origin_suburb, destination_suburb):

    origin_hub = suburb_hubs[origin_suburb]
    destination_hub = suburb_hubs[destination_suburb]

    try:

        path = nx.shortest_path(
            city_graph,
            origin_hub,
            destination_hub
        )

        return Route(
            path,
            "generated"
        )

    except:

        return None