from simulation.city_graph import city_graph


# =====================================
# CALCULATE ROUTE TRAVEL TIME
# =====================================

def calculate_route_time(route):

    total = 0

    for i in range(len(route.stops) - 1):

        current = route.stops[i]

        nxt = route.stops[i + 1]

        # =====================================
        # CHECK ROAD EXISTS
        # =====================================

        if city_graph.has_edge(
            current,
            nxt
        ):

            edge = city_graph[
                current
            ][
                nxt
            ]

            # =====================================
            # GET DISTANCE
            # =====================================

            distance = edge["distance"]

            # =====================================
            # BASE SPEED
            # =====================================

            speed = 40

            # =====================================
            # ROAD TYPE MODIFIERS
            # =====================================

            road_type = edge.get(
                "road_type",
                "urban"
            )

            if road_type == "CBD":

                speed = 25

            elif road_type == "urban_core":

                speed = 30

            elif road_type == "urban":

                speed = 35

            elif road_type == "connector":

                speed = 50

            elif road_type == "regional":

                speed = 65

            # =====================================
            # TRAFFIC MODIFIER
            # =====================================

            traffic = edge.get(
                "traffic",
                0.2
            )

            speed *= (1 - (traffic * 0.5))

            # =====================================
            # PREVENT INVALID SPEED
            # =====================================

            speed = max(speed, 10)

            # =====================================
            # CALCULATE MINUTES
            # =====================================

            minutes = (
                distance / speed
            ) * 60

            # =====================================
            # STOP DWELL TIME
            # =====================================

            minutes += 1.2

            total += minutes

    # =====================================
    # FINALIZE
    # =====================================

    route.travel_time = round(total)

    return route