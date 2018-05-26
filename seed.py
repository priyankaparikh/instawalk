"""Utility file to seed points database from tsv files in seed_data"""

from sqlalchemy import func
from models import Waypoint, Route, Route_Waypoints
from models import connect_to_db, db
from server import app
import glob
import os
import re
import string
path = "./seed_data/*.tsv"


def load_waypoints():
    """ Load waypoints from all tsv in seed_data """

    print "Waypoints"

    # Delete all rows in table to prevent duplicates
    # in case of need to re-seed
    Waypoint.query.delete()

    # Read all .tsv files in seed_data and insert data
    for fname in glob.glob(path):
        with open(fname) as f:
            content = f.readlines()[1:]
            for row in content:
                row = row.rstrip()
                row = re.split(r'\t+', row)
                if "##" in row[-1]:
                    not_useful = row[-1].find("##")
                    if not_useful >= 32:
                        row[-1] = row[-1][:not_useful]
                if "NULL" in row[-1]:
                    continue
                if "Bound" in row[-1]:
                    continue

                lat_long = row[-1].split(",")
                lat = lat_long[0]
                lng = lat_long[-1]

                if '\xe2' in lat:
                    latitude = re.sub("`", "'", lat)
                elif '\xe2' in lng:
                    longitude = re.sub("`", "'", lng)

                latitude = lat
                longitude = lng

                latitude = dms2dec(lat)
                longitude = dms2dec(lng)
                longitude = -longitude

                point = [row[0], latitude, longitude]
                waypoint = Waypoint(latitude=point[1],
                                    longitude=point[2],
                                    location=point[0],
                                    )
                # Add waypoint to db session
                db.session.add(waypoint)
    # Commit waypoints
    db.session.commit()


def dms2dec(dms_str):
    """Return decimal representation of DMS
    >>> dms2dec(utf8(4853'10.18"N))
    48.8866111111F
    >>> dms2dec(utf8(220'35.09"E))
    2.34330555556F
    >>> dms2dec(utf8(4853'10.18"S))
    -48.8866111111F
    >>> dms2dec(utf8(220'35.09"W))
    -2.34330555556F
    """
    dms_str = re.sub(r'\s', '', dms_str)
    if re.match('[swSW]', dms_str):
        sign = -1
    else:
        sign = 1

    if "." not in dms_str:
        dms_str = dms_str[:-1] + ".00" + dms_str[-1] 
    (degree, minute, second, micro_seconds, trash) = re.split('\D+', dms_str, maxsplit=4)
    return sign * (int(degree) + float(minute)
                    / 60 + float(second) / 3600 + 
                    float(micro_seconds) / 36000)


##################################################################################


def load_routes():
    """ Seed Routes and Route_Waypoints with curated Routes """
    # Themes:
    themes = {1:"foodie", 2:"coffee", 3:"beer", 4:"weed",
              5:"historical", 6:"architecture", 7:"art",
              8:"nature", 9:"oddities", 10:"music"}

    # Easy (3-4 Waypoints):
    easy = {route1:{waypoints:[], route_difficulty:"easy", route_type: }}


    # Medium (5-7 Waypoints):
    medium = {route1:{waypoints:[], route_difficulty:"medium", route_type: }}


    # Hard (8-10+ Waypoints):
    hard = {route1:{waypoints:[], route_difficulty:"hard", route_type: }}


    # Iterate through and add routes:
    routes = [easy, medium, hard]

    for route in routes:

        route = Route(waypoints=waypoints,
                      route_difficulty=route_difficulty,
                      route_type=route_type)

        db.session.add(route)
        db.session.commit()


##################################################################################    

if __name__ == "__main__":
    connect_to_db(app)

    # # In case tables haven't been created, create them
    db.create_all()

    # Import data type
    load_waypoints()
       