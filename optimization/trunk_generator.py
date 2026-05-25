from simulation.routes import Route


def generate_trunk_routes():

    routes = []

    # =====================================
    # METRO CORE EAST/WEST
    # =====================================

    routes.append(

        Route(

            [

                "Cathedral City Center 1",

                "Wilten Theatre",

                "Main Station",

                "Central Hub Station"
            ],

            "trunk"
        )
    )

    # =====================================
    # UNIVERSITY CORRIDOR
    # =====================================

    routes.append(

        Route(

            [

                "Central Hub Station",

                "Sunglare Valley",

                "Westfield",

                "Lower Sonnstein",

                "University of Technology"
            ],

            "trunk"
        )
    )

    # =====================================
    # INDUSTRIAL CORRIDOR
    # =====================================

    routes.append(

        Route(

            [

                "Main Station",

                "Fishers Ground",

                "Boos Corp Warehouses",

                "Harbour Distribution Centre",

                "Harbour Administration"
            ],

            "trunk"
        )
    )

    return routes