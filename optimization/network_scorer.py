from optimization.redundancy_checker import (
    redundancy_score
)

from optimization.transfer_optimizer import (
    average_transfer_distance
)

from optimization.connectivity_checker import (
    network_fully_connected
)


def score_network(routes, city_graph):

    score = 0

    # =====================================
    # CONNECTIVITY
    # =====================================

    if network_fully_connected(
        routes,
        city_graph
    ):

        score += 5000

    else:

        score -= 5000

    # =====================================
    # TRANSFER EFFICIENCY
    # =====================================

    avg_distance = average_transfer_distance(
        routes
    )

    score += max(0, 3000 - avg_distance * 30)

    # =====================================
    # ROUTE COUNT BONUS
    # =====================================

    score += len(routes) * 50

    # =====================================
    # REDUNDANCY
    # =====================================

    redundancy = redundancy_score(routes)

    score -= redundancy * 2

    return score