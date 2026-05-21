def overlap_ratio(route1, route2):

    set1 = set(route1.stops)
    set2 = set(route2.stops)

    overlap = len(set1 & set2)

    smaller = min(
        len(set1),
        len(set2)
    )

    if smaller == 0:
        return 0

    return overlap / smaller


def clean_routes(routes):

    cleaned = []

    for route in routes:

        if len(route.stops) < 4:
            continue

        redundant = False

        for existing in cleaned:

            if overlap_ratio(
                route,
                existing
            ) > 0.75:

                redundant = True
                break

        if not redundant:

            cleaned.append(route)

    return cleaned