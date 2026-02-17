def detect(assignments):

    alerts = []

    seen_pilots = set()
    seen_drones = set()

    for a in assignments:

        if a["pilot"] in seen_pilots:
            alerts.append(f"Double booking pilot {a['pilot']}")

        if a["drone"] in seen_drones:
            alerts.append(f"Double booking drone {a['drone']}")

        if a["cost"] > a["budget"]:
            alerts.append(f"Budget overrun on mission {a['mission']}")

        if a["weather_forecast"].strip().lower() == "rainy":
            alerts.append(f"Check waterproof drone for mission {a['mission']}")

        seen_pilots.add(a["pilot"])
        seen_drones.add(a["drone"])

    return alerts
