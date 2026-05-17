import random

from simulation.city_graph import city_graph
from simulation.routes import Route
from data.hub_data import hub_stops


def generate_random_route(length=5):

    valid_stops = [
        stop
        for stop in city_graph.nodes
        if len(list(city_graph.neighbors(stop))) > 0
    ]

    if random.random() < 0.5:
        start_stop = random.choice(hub_stops)
    else:
        start_stop = random.choice(valid_stops)

    route = [start_stop]

    attempts = 0
    max_attempts = 50

    while len(route) < length and attempts < max_attempts:

        current = route[-1]

        neighbors = list(city_graph.neighbors(current))

        # Only allow unvisited neighbors
        unvisited_neighbors = [
            neighbor
            for neighbor in neighbors
            if neighbor not in route
        ]

        if not unvisited_neighbors:
            break

        next_stop = random.choice(unvisited_neighbors)

        route.append(next_stop)

        attempts += 1

    return Route(route)