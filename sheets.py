import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

CREDS = ServiceAccountCredentials.from_json_keyfile_name(
    "service_account.json", SCOPE
)

client = gspread.authorize(CREDS)

PILOTS = client.open("pilot_roster").sheet1
DRONES = client.open("drone_fleet").sheet1
MISSIONS = client.open("missions").sheet1


def load_pilots():
    return pd.DataFrame(PILOTS.get_all_records())


def load_drones():
    return pd.DataFrame(DRONES.get_all_records())


def load_missions():
    return pd.DataFrame(MISSIONS.get_all_records())


def update_pilot_status(name, status):
    data = PILOTS.get_all_records()
    for i, r in enumerate(data):
        if r["name"] == name:
            PILOTS.update_cell(i+2, 7, status)


def update_drone_status(drone_id, status):
    data = DRONES.get_all_records()
    for i, r in enumerate(data):
        if r["drone_id"] == drone_id:
            DRONES.update_cell(i+2, 5, status)
