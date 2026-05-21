import networkx as nx

from simulation.city_graph import city_graph
from simulation.routes import Route


major_hubs = [

    "Cathedral City Center 1",

    "Central Hub Station",

    "Main Station",

    "Fishers Ground",

    "University of Technology",

    "Harbour Distribution Centre",

    "Harbour Administration"
]


def generate_trunk_routes():

    routes = []

    for i in range(len(major_hubs)):

        for j in range(i + 1, len(major_hubs)):

            try:

                path = nx.shortest_path(
                    city_graph,
                    major_hubs[i],
                    major_hubs[j]
                )

                if len(path) < 4:
                    continue

                routes.append(
                    Route(path, "trunk")
                )

            except:
                pass

    return routes