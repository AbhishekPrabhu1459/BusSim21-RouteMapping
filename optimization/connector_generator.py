from simulation.routes import Route


def generate_connector_routes():

    routes = []

    # =====================================
    # WESTFIELD TO CORE
    # =====================================

    routes.append(

        Route(

            [

                "Westfield",

                "Westfield Corn Towers",

                "High Road",

                "Main Station"
            ],

            "connector"
        )
    )

    # =====================================
    # ASTRA TO INDUSTRIAL
    # =====================================

    routes.append(

        Route(

            [

                "Media Centre Astra",

                "Siegwalden Lido",

                "Fishers Ground"
            ],

            "connector"
        )
    )

    # =====================================
    # OAKVILLE CONNECTOR
    # =====================================

    routes.append(

        Route(

            [

                "Oakville Central",

                "Siegwalden",

                "Radovanovic Bridge",

                "Cathedral City Center 1"
            ],

            "connector"
        )
    )

    # =====================================
    # AGRICULTURE CONNECTOR
    # =====================================

    routes.append(

        Route(

            [

                "Corn Street Agriculture Centre",

                "Fishers Ground",

                "Main Station"
            ],

            "connector"
        )
    )

    return routes