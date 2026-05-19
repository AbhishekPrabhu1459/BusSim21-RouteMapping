import networkx as nx

from simulation.city_graph import city_graph
from simulation.routes import Route


def generate_trunk_route():

    major_corridor = [

        "Oakville Central",

        "Siegwalden Secondary School",

        "Siegwalden",

        "Siegwalden Lido",

        "Media Centre Astra",

        "Boos Corp Warehouses",

        "Harbour Distribution Centre",

        "Wachowski Industries",

        "University of Technology",

        "Winfield West",

        "Lower Sonnstein",

        "Steinegger Grange",

        "Gullstrom Grammar School",

        "Westfield",

        "Sonnstein Main Square",

        "Steineck East",

        "Corn Street Agriculture Centre",

        "Harbour Administration"
    ]

    final_route = []

    for i in range(len(major_corridor) - 1):

        try:

            segment = nx.shortest_path(
                city_graph,
                major_corridor[i],
                major_corridor[i + 1]
            )

            if final_route:

                segment = segment[1:]

            final_route.extend(segment)

        except:
            pass

    return Route(
        final_route,
        "trunk"
    )