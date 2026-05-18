def overlap_penalty(routes):

    penalty = 0

    for i in range(len(routes)):

        for j in range(i + 1, len(routes)):

            route_a = routes[i]
            route_b = routes[j]

            overlap = set(
                route_a.stops
            ).intersection(
                route_b.stops
            )

            shared = len(overlap)

            # =================================
            # SMALL OVERLAP GOOD
            # =================================

            if shared <= 1:
                continue

            # =================================
            # EXPRESS + TRUNK OVERLAP ACCEPTABLE
            # =================================

            route_types = {
                route_a.route_type,
                route_b.route_type
            }

            if route_types == {
                "trunk",
                "express"
            }:

                penalty += shared * 20

            # =================================
            # FEEDER + TRUNK OVERLAP GOOD
            # =================================

            elif route_types == {
                "feeder",
                "trunk"
            }:

                penalty += shared * 10

            # =================================
            # SAME-TYPE OVERLAP BAD
            # =================================

            else:

                penalty += shared * 120

    return penalty