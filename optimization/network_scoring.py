from optimization.scoring import (
    calculate_route_score,
    coverage_score
)
from optimization.transfer_scoring import (
    average_transfer_score
)

from optimization.transit_network import (
    build_transit_graph
)
from optimization.overlap_scoring import (
    overlap_penalty
)

import networkx as nx


def network_connectivity_score(routes):

    transit_graph = build_transit_graph(routes)

    if nx.is_connected(transit_graph):
        return 1000

    return 0


def calculate_network_score(routes):

    total = 0

    for route in routes:
        total += calculate_route_score(route)

    total += coverage_score(routes)

    total += network_connectivity_score(routes)

    transit_graph = build_transit_graph(routes)

    total += average_transfer_score(
        transit_graph
    )
    total -= overlap_penalty(routes)

    return total