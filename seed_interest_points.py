"""Utility file to seed points database with curated points of interest."""

from sqlalchemy import func
from models import Interest_Point
from models import connect_to_db, db
from server import app
from geopy import Nominatim

def load_interest_points():
    """ Load points of interest, seed interest_points table. """
    geolocator = Nominatim()

    cats = {1:"foodie", 2:"coffee", 3:"beer", 4:"weed",
            5:"history", 6:"architecture", 7:"art",
            8:"oddities", 9:"music", 10:"design", 11:"literary"}

    addresses = {"1376 Haight St San Francisco, CA 94117":{
                "location":"Pipe Dreams","category":cats[4],
                "description":"Excellent head shop in the Haight"},
                "1467 Haight St San Francisco, CA 94117":{
                "location":"Puff Puff Pass","category":cats[4],
                "description":"Excellent head shop in the Haight"},
                "2196 Mission St San Francisco, CA 94110":{
                "location":"City Smoke Shop","category":cats[4],
                "description":"Excellent head shop in the Mission"},
                "1312 Haight St San Francisco, CA 94117":{
                "location":"Sunshine Coast","category":cats[4],
                "description":"Excellent head shop in the Haight"},
                "1038 Taraval St San Francisco, CA 94116":{
                "location":"King Kush","category":cats[4],
                "description":"Excellent head shop in Parkside"},
                "435 Stockton St San Francisco, CA 94108":{
                "location":"Vapor Smoke Shop","category":cats[4],
                "description":"Great head shop near Union Square"},
                "1077 Post St San Francisco, CA 94109":{
                "location":"Grass Roots","category":cats[4],
                "description":"Cannabis dispensary in Lower Nob Hill"},
                "952 Mission St San Francisco, CA 94103":{
                "location":"Barbary Coast Collective","category":cats[4], 
                "description":""},
                "4218 Mission St San Francisco, CA 94112":{
                "location":"The Green Cross","category":cats[4], 
                "description":""},
                "2029 Market St San Francisco, CA 94114":{
                "location":"The Apothecarium - Castro","category":cats[4], 
                "description":""},
                "2414 Lombard St San Francisco, CA 94123":{
                "location":"The Apothecarium - Marina","category":cats[4], 
                "description":""},
                "33 29th St San Francisco, CA 94110":{
                "location":"Harvest off Mission","category":cats[4], 
                "description":""},
                "471 Jessie St San Francisco, CA 94103 ":{
                "location":"Bloom Room","category":cats[4], 
                "description":""},
                "2261 Market St San Francisco, CA 94114":{
                "location":"Potbox","category":cats[4], 
                "description":""},
                "3139 Mission St San Francisco, CA 94110":{
                "location":"Cookieco415","category":cats[4], 
                "description":""},
                "473 Haight St San Francisco, CA 94117":{
                "location":"Sparc","category":cats[4], 
                "description":""},
                "2544 3rd St San Francisco, CA 94107":{
                "location":"Dutchmans Flat","category":cats[4], 
                "description":""},
                "211 12th St San Francisco, CA 94103":{
                "location":"SFFOG","category":cats[4], 
                "description":""},
                "847 Howard St San Francisco, CA 94103":{
                "location":"Lounge 847","category":cats[4], 
                "description":""},
                "70 2nd St San Francisco, CA 94105":{
                "location":"Flower Power Dispensary","category":cats[4], 
                "description":""},
                "3655 Lawton St San Francisco, CA 94122":{
                "location":"Andytown Coffee Roaster","category":cats[2], 
                "description":""},
                "805 Columbus Ave San Francisco, CA 94133":{
                "location":"Beacon Coffee and Pantry","category":cats[2], 
                "description":""},
                "115 Sansome St, San Francisco CA, 94104":{
                "location":"Blue Bottle Coffee","category":cats[2], 
                "description":""},
                "670 Commercial St San Francisco, CA 94111":{
                "location":"Chapel Hill Coffee Co.","category":cats[2], 
                "description":""},
                "1890 Bryant St San Francisco, CA 94110":{
                "location":"Coffee Bar","category":cats[2], 
                "description":""},
                "1301 Mission St San Francisco, CA 94103":{
                "location":"Coffee Cultures","category":cats[2], 
                "description":""},
                "986 Market St San Francisco, CA 94102":{
                "location":"Equator Coffees & Teas","category":cats[2], 
                "description":""},
                "1315 18th St San Francisco, CA 94107":{
                "location":"Farley's","category":cats[2], 
                "description":""},
                "3157 Geary Blvd San Francisco, CA 94118":{
                "location":"fifty/fifty","category":cats[2], 
                "description":""},
                "672 Stanyan St San Francisco, CA 94117":{
                "location":"Flywheel Coffee","category":cats[2], 
                "description":""},
                "3117 Clement St San Francisco, CA 94121":{
                "location":"Garden House Cafe","category":cats[2], 
                "description":""},
                "277 Golden Gate Ave San Francisco, CA 94102":{
                "location":"George and Lennie","category":cats[2], 
                "description":""},
                "3985 17th St San Francisco, CA 94114":{
                "location":"Hearth Coffee Roasters","category":cats[2], 
                "description":""},
                "50 Fremont St San Francisco, CA 94105":{
                "location":"La Capra Coffee","category":cats[2], 
                "description":""},
                "Steiner St Hayes St, San Francisco, CA 94115":{
                "location":"Lady Falcon Coffee Club","category":cats[2], 
                "description":""},
                "3417 18th St San Francisco, CA 94110":{
                "location":"Linea Caffe","category":cats[2], 
                "description":""},
                "720 Market St San Francisco, CA 94102":{
                "location":"Mazarine Coffee","category":cats[2], 
                "description":""},
                "1415 18th St San Francisco, CA 94107":{
                "location":"Provender","category":cats[2], 
                "description":""},
                "1300 Haight St San Francisco, CA 94117":{
                "location":"Ritual Roasters Coffee","category":cats[2], 
                "description":""},
                "610 Long Bridge St San Francisco, CA 94158":{
                "location":"Réveille Coffee Co.","category":cats[2], 
                "description":""},
                "2340 Polk St San Francisco, CA 94109":{
                "location":"Saint Frank","category":cats[2], 
                "description":""},
                "1415 Folsom St San Francisco, CA 94103":{
                "location":"Sextant Coffee Roasters","category":cats[2], 
                "description":""},
                "270 7th St San Francisco, CA 94103":{
                "location":"Sightglass Coffee","category":cats[2], 
                "description":""},
                "1352A 9th Ave San Francisco, CA 94122":{
                "location":"Snowbird Coffee","category":cats[2], 
                "description":""},
                "736 Divisadero St San Francisco, CA 94117":{
                "location":"The Mill","category":cats[2], 
                "description":""},
                "4033 Judah St San Francisco, CA 94122":{
                "location":"Trouble Coffee","category":cats[2], 
                "description":""},
                "2271 Union St San Francisco, CA 94123":{
                "location":"Wrecking Ball Coffee Roasters","category":cats[2], 
                "description":""},
                "563 2nd St San Francisco, CA 94107":{
                "location":"21st Amendment Brewery & Restaurant","category":cats[3], 
                "description":""},
                "2704 24th St San Francisco, CA 94110":{
                "location":"Almanac Tap Room","category":cats[3], 
                "description":""},
                "495 De Haro St San Francisco, CA 94107":{
                "location":"Anchor Public Taps","category":cats[3], 
                "description":""},
                "1525 Cortland Ave San Francisco, CA":{
                "location":"Barebottle Brewing Company","category":cats[3], 
                "description":""},
                "1785 Fulton St San Francisco, CA 94117":{
                "location":"Barrel Head Brewhouse","category":cats[3], 
                "description":""},
                "544 Bryant St San Francisco, CA 94107":{
                "location":"Black Hammer Brewing","category":cats[3], 
                "description":""},
                "701 Haight St San Francisco, CA 94117":{
                "location":"Black Sands Brewery","category":cats[3], 
                "description":""},
                "1150 Howard St San Francisco, CA 94103":{
                "location":"Cellarmaker Brewing Company","category":cats[3], 
                "description":""},
                "2636 San Bruno Ave San Francisco, CA 94134":{
                "location":"Ferment.Drink.Repeat","category":cats[3], 
                "description":""},
                "1 Sausalito San Francisco, CA 94111":{
                "location":"Fort Point Beer Company","category":cats[3], 
                "description":""},
                "1050 26th St San Francisco, CA 94107":{
                "location":"Harmonic Brewing","category":cats[3], 
                "description":""},
                "1439 Egbert Ave Unit A San Francisco, CA 94124":{
                "location":"Laughing Monk Brewing","category":cats[3], 
                "description":""},
                "69 Bluxome St San Francisco, CA 94107":{
                "location":"Local Brewing Co.","category":cats[3], 
                "description":""},
                "665 22nd St San Francisco, CA 94107":{
                "location":"Magnolia Brewing Company","category":cats[3], 
                "description":""},
                "3193 Mission St San Francisco, CA 94110":{
                "location":"Old Bus Tavern","category":cats[3], 
                "description":""},
                "1439 Egbert Ave Unit c San Francisco, CA 94124":{
                "location":"Seven Stills Brewery & Distillery","category":cats[3], 
                "description":""},
                "1195 Evans Ave San Francisco, CA 94124":{
                "location":"Speakeasy Ales & Lagers","category":cats[3], 
                "description":""},
                "1735 Noriega St San Francisco, CA 94122":{
                "location":"Sunset Reservoir Brewing Company","category":cats[3], 
                "description":""},
                "661 Howard St San Francisco, CA 94105":{
                "location":"ThirstyBear Brewing Company","category":cats[3], 
                "description":""},
                "2245 3rd St San Francisco, CA 94107":{
                "location":"Triple Voodoo Brewery & Tap Room","category":cats[3], 
                "description":""},
                "3801 18th St San Francisco, CA 94114":{
                "location":"Woods Cerveceria","category":cats[3], 
                "description":""},
                "1150 Howard St, San Francisco, CA 94103":{
                "location":"Cellarmaker Brewing Company","category":cats[3], 
                "description":""},
                "":{
                "location":"Aardvark Books","category":cats[], 
                "description":""},
                "":{
                "location":"Adobe Books","category":cats[], 
                "description":""},
                "":{
                "location":"Bird and Beckett","category":cats[], 
                "description":""},
                "":{
                "location":"Book Passage","category":cats[], 
                "description":""},
                "":{
                "location":"Books Inc.","category":cats[], 
                "description":""},
                "":{
                "location":"The Booksmith","category":cats[], 
                "description":""},
                "":{
                "location":"Borderlands","category":cats[], 
                "description":""},
                "":{
                "location":"City Lights","category":cats[], 
                "description":""},
                "":{
                "location":"Dog-Eared Books","category":cats[], 
                "description":""},
                "":{
                "location":"Green Apple Books","category":cats[], 
                "description":""},
                "":{
                "location":"Kayo Books","category":cats[], 
                "description":""},
                "":{
                "location":"Omnivore Books","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                "":{
                "location":"","category":cats[], 
                "description":""},
                # "":{
                # "location":"","category":cats[], 
                # "description":""}
                }

    for address in addresses:
        location = address
        point = geolocator.geocode(location)
        latitude = location.latitude
        longitude = location.longitude
        category = location["category"]


                route = Route(latitude=latitude,
                              longitude=longitude,
                              location=location,
                              category=category,
                              description=description)

                db.session.add(route)
        db.session.commit()


##################################################################################    

if __name__ == "__main__":
    connect_to_db(app)

    # # In case tables haven't been created, create them
    db.create_all()

    # Import data type
    load_interest_points()

