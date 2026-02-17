from models import get_missions
from assignment import match_pilots, match_drones
from sheets import update_pilot_status, update_drone_status

print("Drone Operations AI Agent Started")

assigned = False

while True:

    query = input("\nAsk agent: ").lower()

    if "missions" in query:
        print(get_missions())

    elif "assign" in query:

        missions = get_missions()

        mission = missions.iloc[0]

        pilots = match_pilots(mission)
        drones = match_drones(mission)

        if pilots.empty or drones.empty:
            print("No valid assignment found")
            continue

        pilot = pilots.iloc[0]
        drone = drones.iloc[0]

        print("\nAssigned Pilot:", pilot["name"])
        print("Assigned Drone:", drone["drone_id"])

        # Update status in Google Sheets
        update_pilot_status(pilot["name"], "Unavailable")
        update_drone_status(drone["drone_id"], "Unavailable")

        print("\nStatus updated in Google Sheets")

        assigned = True

    elif "reassign" in query:

        if not assigned:
            print("No previous assignment to reassign")
            continue

        print("Reassigning...")
        assigned = False

    elif "exit" in query:
        break

    else:
        print("Commands: missions | assign | reassign | exit")
