from simulation.routes import Route

from data.hub_data import suburb_hubs


def generate_express_route():

    hubs = list(suburb_hubs.values())

    # Select only highest-priority hubs
    express_stops = []

    if "Old Town Central" in hubs:
        express_stops.append(
            "Old Town Central"
        )

    if "Airport Terminal" in hubs:
        express_stops.append(
            "Airport Terminal"
        )

    # Add industrial only if needed
    if (
        "Industrial Hub" in hubs
        and len(express_stops) < 3
    ):

        express_stops.append(
            "Industrial Hub"
        )

    return Route(
        express_stops,
        "express"
    )