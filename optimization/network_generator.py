from optimization.feeder_generator import (
    generate_feeder_route
)

from optimization.trunk_generator import (
    generate_trunk_route
)

from optimization.express_generator import (
    generate_express_route
)


def generate_route_network():

    routes = []

    # =====================================
    # FEEDER ROUTES
    # =====================================

    feeder_1 = generate_feeder_route()

    routes.append(feeder_1)

    # =====================================
    # TRUNK ROUTES
    # =====================================

    trunk_1 = generate_trunk_route()

    routes.append(trunk_1)

    # =====================================
    # EXPRESS ROUTES
    # =====================================

    express_1 = generate_express_route()

    routes.append(express_1)

    return routes