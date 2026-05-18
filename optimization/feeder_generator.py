import random

from simulation.city_graph import city_graph
from simulation.routes import Route


def generate_feeder_route():

    suburban_stops = [
        stop
        for stop, data
        in city_graph.nodes(data=True)
        if data["district_type"] == "suburban"
    ]

    route = random.sample(
        suburban_stops,
        min(5, len(suburban_stops))
    )

    return Route(route, "feeder")
