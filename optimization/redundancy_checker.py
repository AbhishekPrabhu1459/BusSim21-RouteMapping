def redundancy_score(routes):

    overlap_penalty = 0

    edges_seen = {}

    for route in routes:

        stops = route.stops

        for i in range(len(stops) - 1):

            edge = tuple(sorted([
                stops[i],
                stops[i + 1]
            ]))

            edges_seen[edge] = (
                edges_seen.get(edge, 0) + 1
            )

    for edge, count in edges_seen.items():

        if count > 1:

            overlap_penalty += (count - 1) * 10

    return overlap_penalty