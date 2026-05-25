from simulation.routes import Route


def generate_express_routes():

    routes = []

    # =====================================
    # CBD ↔ HARBOUR
    # =====================================

    routes.append(

        Route(

            [

                "Cathedral City Center 1",

                "Main Station",

                "Fishers Ground",

                "Harbour Distribution Centre"
            ],

            "express",

            express=True
        )
    )

    # =====================================
    # CBD ↔ UNIVERSITY
    # =====================================

    routes.append(

        Route(

            [

                "Cathedral City Center 1",

                "Central Hub Station",

                "University of Technology"
            ],

            "express",

            express=True
        )
    )

    # =====================================
    # CBD ↔ ASTRA
    # =====================================

    routes.append(

        Route(

            [

                "Cathedral City Center 1",

                "Main Station",

                "Fishers Ground",

                "Media Centre Astra"
            ],

            "express",

            express=True
        )
    )

    return routes