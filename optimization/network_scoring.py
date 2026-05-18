from optimization.overlap_scoring import (
    overlap_penalty
)



def calculate_network_score(routes):

    total = 0

    # Reward hubs
    for route in routes:

        for stop in route.stops:

            total += 20

    # Penalize excessive overlap
    total -= overlap_penalty(routes)

    return total
