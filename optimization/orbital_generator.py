from simulation.routes import Route


def generate_orbital_routes():

    routes = []

    # =====================================
    # INNER ORBITAL
    # =====================================

    routes.append(

        Route(

            [

                "Westfield",

                "Steineck East",

                "Lower Sonnstein",

                "University of Technology",

                "Harbour Distribution Centre"
            ],

            "orbital"
        )
    )

    # =====================================
    # OUTER ORBITAL
    # =====================================

    routes.append(

        Route(

            [

                "Media Centre Astra",

                "Fishers Ground",

                "Harbour Distribution Centre",

                "University of Technology"
            ],

            "orbital"
        )
    )

    return routes