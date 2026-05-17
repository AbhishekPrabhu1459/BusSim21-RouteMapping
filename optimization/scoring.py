from data.hub_data import hub_stops
from data.demand_data import demand_data
from data.stops_data import stops

def hub_score(route):

    score = 0

    for stop in route.stops:

        if stop in hub_stops:
            score += 50

    return score


def calculate_route_score(route):

    score = 0

    for i in range(len(route.stops) - 1):

        pair = (
            route.stops[i],
            route.stops[i + 1]
        )

        score += demand_data.get(pair, 0)

    score += hub_score(route)

    return score


def hub_score(route):

    score = 0

    for stop in route.stops:

        if stop in hub_stops:
            score += 50

    return score


def coverage_score(routes):

    served_stops = set()

    for route in routes:

        served_stops.update(route.stops)

    total_stops = len(stops)

    covered = len(served_stops)

    return (covered / total_stops) * 500