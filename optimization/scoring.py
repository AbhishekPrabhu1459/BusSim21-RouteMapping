from data.demand_data import demand_data

def calculate_route_score(route):
    score = 0

    for i in range(len(route.stops) - 1):

        pair = (
            route.stops[i],
            route.stops[i + 1]
        )

        score += demand_data.get(pair, 0)

    return score