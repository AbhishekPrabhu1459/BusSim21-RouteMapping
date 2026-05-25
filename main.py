from optimization.network_optimizer import (
    optimize_network
)

from optimization.frequency_assigner import (
    assign_frequency
)

from optimization.network_scorer import (
    score_network
)

from optimization.travel_time_calculator import (
    calculate_route_time
)


# =====================================
# GENERATE NETWORK
# =====================================

routes = optimize_network()


# =====================================
# ASSIGN FREQUENCIES
# =====================================

for route in routes:

    assign_frequency(route)

    calculate_route_time(route)


# =====================================
# SCORE NETWORK
# =====================================

network_score = score_network(routes)


# =====================================
# PRINT NETWORK
# =====================================

print(
    "\n=== METROPOLITAN TRANSIT AUTHORITY ===\n"
)

for i, route in enumerate(routes):

    print(f"LINE {i + 1}")

    print(
        f"Service Type: {route.route_type}"
    )

    print(
        f"Frequency: every "
        f"{route.frequency} mins"
    )

    print(
        f"Stops ({len(route.stops)}):"
    )

    for stop in route.stops:

        print(f" - {stop}")

    print()


# =====================================
# NETWORK SUMMARY
# =====================================

print("=== NETWORK SUMMARY ===\n")

total_routes = len(routes)

local_count = sum(
    1 for r in routes
    if r.route_type == "local"
)

connector_count = sum(
    1 for r in routes
    if r.route_type == "connector"
)

trunk_count = sum(
    1 for r in routes
    if r.route_type == "trunk"
)

express_count = sum(
    1 for r in routes
    if r.route_type == "express"
)

all_stops = set()

for route in routes:

    all_stops.update(route.stops)

print(f"Total Routes: {total_routes}")

print(f"Local Routes: {local_count}")

print(f"Connector Routes: {connector_count}")

print(f"Trunk Routes: {trunk_count}")

print(f"Express Routes: {express_count}")

print(f"Unique Stops Covered: {len(all_stops)}")

print(f"\nNETWORK SCORE: {network_score}")