from simulation.passenger_patterns import (
    estimate_stop_demand
)


def score_network(routes):

    score = 0

    all_stops = set()

    for route in routes:

        all_stops.update(route.stops)

        # =====================================
        # DEMAND COVERAGE
        # =====================================

        for stop in route.stops:

            score += (

                estimate_stop_demand(
                    stop,
                    "morning"
                ) * 10
            )

        # =====================================
        # EXPRESS BONUS
        # =====================================

        if route.route_type == "express":

            score += 500

        # =====================================
        # TRUNK BONUS
        # =====================================

        if route.route_type == "trunk":

            score += 300

        # =====================================
        # LOOP PENALTY
        # =====================================

        duplicates = (

            len(route.stops)
            - len(set(route.stops))
        )

        score -= duplicates * 100

        # =====================================
        # EXCESSIVE LENGTH PENALTY
        # =====================================

        if len(route.stops) > 20:

            score -= (

                len(route.stops) - 20
            ) * 80

    # =====================================
    # COVERAGE BONUS
    # =====================================

    score += len(all_stops) * 50

    return score