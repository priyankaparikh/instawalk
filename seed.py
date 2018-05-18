"""Utility file to seed points database from tsv files in seed_data"""

from sqlalchemy import func
from models import Waypoint

from models import connect_to_db, db
from server import app

import glob
import os
import re
path = "./seed_data/*.tsv"


def load_waypoints():
    """Load waypoints from all tsv in seed_data"""

    print "Waypoints"

    # Delete all rows in table to prevent duplicates
    # in case of need to re-seed
    Waypoints.query.delete()

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
                point = [row[0], lat_long[0], lat_long[-1]]
                
                waypoint = Waypoints(waypoint_id=waypoint_id,
                                     latitude=point[1],
                                     longitude=point[2],
                                     location=point[0],
                                     )

                # Add waypoint to db session
                db.session.add(waypoint)
    # Commit waypoints
    db.session.commit()


def set_val_waypoint_id():
    """Set value for the next waypoint_id after seeding database"""

    # Get the Max waypoint_id in the database
    result = db.session.query(func.max(Waypoints.waypoint_id)).one()
    max_id = int(result[0])

    # Set the value for the next waypoint_id to be max_id + 1
    query = "SELECT setval('waypoints_way_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db.app()

    # In case tables haven't been created, create them
    db.create_all()

    # Import data type
    load_waypoints()
    set_val_waypoint_id()
       