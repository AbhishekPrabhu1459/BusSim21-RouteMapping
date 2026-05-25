from data.stop_business_data import (
    business_profiles
)


peak_periods = {

    "morning": {

        "commuter_multiplier": 2.0,

        "education_multiplier": 1.8,

        "tourism_multiplier": 0.8
    },

    "midday": {

        "commuter_multiplier": 1.0,

        "education_multiplier": 1.0,

        "tourism_multiplier": 1.3
    },

    "evening": {

        "commuter_multiplier": 2.2,

        "education_multiplier": 0.5,

        "tourism_multiplier": 1.5
    }
}


def estimate_stop_demand(stop_name, period):

    profile = business_profiles[stop_name]

    peak = peak_periods[period]

    demand = 0

    demand += (

        profile["commuter"]
        * peak["commuter_multiplier"]
    )

    demand += (

        profile["education"]
        * peak["education_multiplier"]
    )

    demand += (

        profile["tourism"]
        * peak["tourism_multiplier"]
    )

    demand += profile["industrial"]

    return demand