from optimization.local_route_generator import (
    generate_local_routes
)

from optimization.connector_generator import (
    generate_connector_routes
)

from optimization.trunk_generator import (
    generate_trunk_routes
)

from optimization.express_generator import (
    generate_express_routes
)

from optimization.route_cleaner import (
    clean_routes
)

from optimization.orbital_generator import (
    generate_orbital_routes
)


def optimize_network():

    routes = []

    routes.extend(
        generate_local_routes()
    )

    routes.extend(
        generate_connector_routes()
    )

    routes.extend(
        generate_trunk_routes()
    )

    routes.extend(
        generate_express_routes()
    )

    routes.extend(
    generate_orbital_routes()
    )

    routes = clean_routes(routes)

    return routes