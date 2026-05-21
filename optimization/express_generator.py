import networkx as nx

from simulation.city_graph import city_graph
from simulation.routes import Route


express_hubs = [

    "Cathedral City Center 1",

    "Central Hub Station",

    "University of Technology",

    "Harbour Distribution Centre",

    "Media Centre Astra"
]


def generate_express_routes():

    routes = []

    for i in range(len(express_hubs)):

        for j in range(i + 1, len(express_hubs)):

            try:

                path = nx.shortest_path(
                    city_graph,
                    express_hubs[i],
                    express_hubs[j]
                )

                filtered = path[::2]

                if path[-1] not in filtered:
                    filtered.append(path[-1])

                routes.append(
                    Route(filtered, "express")
                )

            except:
                pass

    return routes