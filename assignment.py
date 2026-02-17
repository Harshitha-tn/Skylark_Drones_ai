from models import get_pilots, get_drones

def match_pilots(mission):

    pilots = get_pilots()

    matches = pilots[
        (pilots["status"].str.strip().str.lower() == "available") &
        (pilots["skills"].str.contains(mission["required_skills"], case=False, na=False))
    ]

    return matches


def match_drones(mission):

    drones = get_drones()

    available = drones[drones["status"].str.strip().str.lower() == "available"]

    weather = mission["weather_forecast"].strip().lower()

    if weather == "rainy":
        available = available[
            available["weather_resistance"].str.contains("IP|Yes|Water", case=False, na=False)
        ]

    return available
