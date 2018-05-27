"""Utility file to seed points database with curated points of interest."""

from sqlalchemy import func
from models import Interest_Point
from models import connect_to_db, db
from server import app


def load_interest_points():
    """ Load points of interest, seed interest_points table. """
    pass


##################################################################################    

if __name__ == "__main__":
    connect_to_db(app)

    # # In case tables haven't been created, create them
    db.create_all()

    # Import data type
    load_interest_points()

