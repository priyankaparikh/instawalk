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
                "227 Church St, San Francisco, CA 94114":{
                "location":"Aardvark Books","category":cats[11], 
                "description":""},
                "3130 24th St, San Francisco, CA 94110":{
                "location":"Adobe Books","category":cats[11], 
                "description":""},
                "653 Chenery St, San Francisco, CA 94131":{
                "location":"Bird and Beckett","category":cats[11], 
                "description":""},
                "1 Ferry Bldg, San Francisco, CA 94111":{
                "location":"Book Passage","category":cats[11], 
                "description":""},
                "601 Van Ness Ave, San Francisco, CA 94102":{
                "location":"Books Inc.","category":cats[11], 
                "description":""},
                "1644 Haight St, San Francisco, CA 94117":{
                "location":"The Booksmith","category":cats[11], 
                "description":""},
                "866 Valencia St, San Francisco, CA 94110":{
                "location":"Borderlands","category":cats[11], 
                "description":""},
                "261 Columbus Ave, San Francisco, CA 94133":{
                "location":"City Lights","category":cats[11], 
                "description":""},
                "900 Valencia St, San Francisco, CA 94110":{
                "location":"Dog-Eared Books","category":cats[11], 
                "description":""},
                "506 Clement St, San Francisco, CA 94118":{
                "location":"Green Apple Books","category":cats[11], 
                "description":""},
                "814 Post St, San Francisco, CA 94109":{
                "location":"Kayo Books","category":cats[11], 
                "description":""},
                "3885A Cesar Chavez St, San Francisco, CA 94131":{
                "location":"Omnivore Books","category":cats[11], 
                "description":""},
                "2162 Polk St, San Francisco, CA 94109":{
                "location":"Russian Hill Bookstore","category":cats[11], 
                "description":"Russian Hill Bookstore, established in 1993, is one of the last family-owned used and new bookstores in San Francisco."},
                "83 Marina Green Dr, San Francisco, CA 94123":{
                "location":"The Wave Organ","category":cats[8], 
                "description":"Located on a jetty in the San Francisco Bay, the Wave Organ was built in 1986. In collaboration with the Exploratorium, artist Peter Richards built an acoustic sculpture that amplifies the sounds of the waves from the Bay."},
                "1700 16th Avenue San Francisco, California, 94122":{
                "location":"Secret Tiled Staircase","category":cats[8], 
                "description":"An artsy hidden staircase leading to breathtaking views of San Francisco."},
                "Corwin Community Garden and Seward Mini-Park Seward St & Douglass St San Francisco, California, 94114":{
                "location":"Seward Street Slides","category":cats[8], 
                "description":"Bring your own cardboard to the slippery slopes of concrete hidden in a neighborhood park."},
                "Pier 39, Building O-11, San Francisco, California 94111":{
                "location":"Magowan's Infinite Mirror Maze","category":cats[8], 
                "description":"A psychedelic labyrinth on the San Francisco bay."},
                "881 Innes Avenue San Francisco, California, 94124":{
                "location":"Albion Castle","category":cats[5], 
                "description":"A 140-year-old castle with underground caves hidden in San Francisco."},
                "1616 Bush St. San Francisco, California, 94109":{
                "location":"Audium","category":cats[8], 
                "description":"Audium is the only theatre anywhere in the world that is constructed specifically for sound movement, utilizing the entire environment as a compositional tool."},
                "680 Point Lobos Ave, San Francisco, CA 94121":{
                "location":"Land's End Labyrinth","category":cats[8], 
                "description":"Burnt once, destroyed twice, and rebuilt at the edge of the continent, the labyrinth at Land’s End may be Land’s End’s most beautiful secret."},
                "1681 Haight St San Francisco, California, 94117":{
                "location":"Loved to Death","category":cats[8], 
                "description":"Storefront that specializes in Oddities, Victorian antiques, taxidermy and Jewelry. Home of The Articulated Art Gallery."},
                "Dewitt Rd San Francisco, California, 94129":{
                "location":"Yoda Fountain","category":cats[8], 
                "description":"Jedi Master Yoda, known to generations new and old as maybe the wisest Jedi in the Star Wars universe has been immortalized in bronze atop a decorative fountain outside the headquarters of Lucasfilm."},
                "1620 Polk St San Francisco, California, 94109":{
                "location":"Good Vibrations Antique Vibrator Museum","category":cats[], 
                "description":"This vibrator museum honors dildo history."},
                "Presidio Boulevard & West Pacific Avenue San Francisco, California, 94129":{
                "location":"Wood Line","category":cats[5], 
                "description":"Wood Line is a snaking sculptural installation of eucalyptus trunks and branches, covertly following Lover’s Lane, the oldest footpath in the Presidio."},
                "1096 Point Lobos Ave San Francisco, California, 94121":{
                "location":"Camera Obscura and Holograph Collection","category":cats[8], 
                "description":"This tiny museum also known as the ‘Giant Camera’ is on the grounds of the historic Cliff House and features a working camera obscura, which reflects images of the beach front outside. It also houses a small collection of holograms."},
                "San Francisco Botanical Garden Martin Luther King Jr. (at Lincoln) San Francisco, California, 94122":{
                "location":"Garden of Fragrance","category":cats[10], 
                "description":"From a wall of cascading rosemary to mint and lemon verbena, the San Francisco Botanical Garden’s Garden of Fragrance is specially designed to be a delight to the sense of smell."},
                "3466 20th St San Francisco, California, 94110":{
                "location":"Institute of Illegal Images","category":cats[8], 
                "description":"Museum befitting the city responsible for supplying the majority of the world's LSD."},
                "75 Hagiwara Tea Garden Drive San Francisco, California, 94118":{
                "location":"Japanese Tea Garden","category":cats[10], 
                "description":"Japanese Tea Garden located in Golden Gate Park, originally constructed for the 1894 Midwinter Exposition."},
                "Pier 15 The Embarcadero, San Francisco, CA 94111":{
                "location":"Exploratorium","category":cats[8], 
                "description":"The Exploratorium, a museum of science, art and human perception, is home to hundreds of exhibits that help in the understanding of electricity, centrifugal motion, sound waves, optical illusion and superstitions among other things."},
                "1090 Point Lobos San Francisco, California, 94121":{
                "location":"Ruins of the Sutro Baths","category":cats[5],
                "description":"Low stone and concrete walls and twisted, rusty steel supports are all that remain of the enormous glass-enclosed public baths at Point Lobos."},
                "Pier 45, Shed A Taylor Street, Fisherman's Wharf San Francisco, California, 94105":{
                "location":"Musée Mécanique","category":cats[8], 
                "description":"A collection of 20th-century automata, penny arcade games, and musical contraptions."},
                "501 Jones Street San Francisco, California, 94102":{
                "location":"Bourbon & Branch","category":cats[5], 
                "description":"A nondescript building that's been funtioning as a speakeasy for nearly a century and a half."},
                "Filbert St & Kearny St San Francisco, CA 94133":{
                "location":"The Parrots of Telegraph Hill","category":cats[8], 
                "description":"The parrot flock began around 1990 when one pair of escaped cherry-headed conures (a small parrot species) quickly found an ecological niche on Telegraph Hill. Joined by other escaped (or released) conures from the city of San Francisco, the flock continued to grow, and after a couple generations of offspring, the flock had grown to over 200 wild parrots by 2005. Today, the parrots of Telegraph Hill can be spotted all over the city, and have been spotted as far south as Brisbane."},
                "824 Valencia St. San Francisco, California, 94110":{
                "location":"Paxton Gate","category":cats[8], 
                "description":"Paxton Gate is an eclectic cross between a gardening store, taxidermy shop, entomological treasure trove, art book retailer, and natural history boutique."},
                "950 Mason Street San Francisco, California 94108":{
                "location":"The Tonga Room","category":cats[5], 
                "description":"In an era when most tiki bars are no more than a novelty dive, the Tonga Room serves up a bit of the exotic glamour that tiki culture once symbolized."},
                "Point Lobos Marine Exchange Lookout Station Land's End San Francisco, California, 94121":{
                "location":"Land’s End Octagon House","category":cats[6], 
                "description":"This one-time watch house for incoming ships at the Golden Gate now stands abandoned and hidden in trees."},
                "Esmeralda Ave & Winfield St San Francisco, CA 94110":{
                "location":"Winfield Street Slides","category":cats[5], 
                "description":"A pair of slides and a tree-lined stair corridor have been an urban oasis for nearly 40 years."},
                "1746 Post Street San Francisco, California, 94115":{
                "location":"Crown & Crumpet","category":cats[8], 
                "description":"Painfully cute tea room."},
                "743 Washington St, San Francisco, CA 94108":{
                "location":"Old Chinese Telephone Exchange","category":cats[5], 
                "description":"Formerly the Bank of Canton, this used to be the Chinese Telephone Exchange where Chinese women operated a switchboard where they had to know the names and numbers of every resident of Chinatown (and speak Cantonese, Mandarin and English)."},
                "2645 Gough St, San Francisco, CA 94123":{
                "location":"McElroy Octagon House","category":cats[6], 
                "description":"Located on the corner of Gough and Union Streets, Octagon House was built in 1861 by William C. McElroy, a miller and early resident of San Francisco."},
                "826 Valencia St. San Francisco, California, 94103":{
                "location":"The Pirate Shop","category":cats[8], 
                "description":"The Pirate Shop carries an extensive array of essential pirate paraphernalia: various Jolly Roger flags, glass eyes, lard, spyglasses, skeleton keys, etc. It’s also a book store associated with the 826 Valencia literacy program, McSweeney’s and The Believer literary journals."},
                "3260-3298 Van Ness Avenue San Francisco, California, 94109":{
                "location":"Aquatic Park Tombstones","category":cats[8], 
                "description":"Repurposed Gold Rush era tombstones visible at low tide."},
                "312 Sutter St #500 San Francisco, California, 94108":{
                "location":"Book Club of California","category":cats[11], 
                "description":"For over a hundred years the Book Club of California has been heralding the artistry of Western writers and printers, and their public clubhouse has become a bastion where print will never die."},
                "280 Orange Alley San Francisco, California":{
                "location":"Peephole Cinema","category":cats[8], 
                "description":"A tiny theater hidden in an alley plays a constant stream of short silent films for anyone willing to peer through the peephole."},
                "Land's End San Francisco, California, 94121":{
                "location":"Fort Miley Batteries","category":cats[5], 
                "description":"Built as part of the late 19th-century Endicott series of fortifications that included the batteries at the Marin Headlands and elsewhere in the Bay Area, Fort Miley stood as the city’s first line of defense, with guns overlooking the entrance to the bay through the end of WWII."},
                "Land's End San Francisco, California, 94121":{
                "location":"The Shipwrecks at Land's End","category":cats[5], 
                "description":"A 300 ship graveyard - 3 still visible at low tide."},
                "Lloyd Lake Golden Gate Park San Francisco, California, 94122":{
                "location":"Portals of the Past","category":cats[5], 
                "description":"Remains of the 1891 Nob Hill mansion of railroad tycoon Alban Towne on California Street memorializing the 1906 earthquake."},
                "50 Hagiwara Tea Garden Dr San Francisco, California, 94118":{
                "location":"Three Gems","category":cats[7], 
                "description":"Tucked into a grassy mound in the Osher Sculpture Garden at the de Young Museum, James Turrell’s “Three Gems” is a secret space to contemplate the sky."},
                "298 Pacific Ave San Francisco, CA 94111":{
                "location":"The Old Ship Saloon","category":cats[5], 
                "description":"In 1849, at the height of the Gold Rush, stormy seas drove the ship Arkansas aground on Alcatraz Island, and the wreckage was towed to shore along the city’s notorious Barbary Coast. In 1851, the ship started its second life as a bar."},
                "1237 John F Kennedy Dr, San Francisco, CA 94121":{
                "location":"Golden Gate Park Bison","category":cats[8], 
                "description":"Longtime pasture with a grazing herd of American bison, cared for by the San Francisco zoo."},
                "Mission Dolores 3321 16th Street San Francisco, California, 94110":{
                "location":"Mission Dolores Cemetery","category":cats[5], 
                "description":"Now one of only a small handful of cemeteries remaining in San Francisco, the tiny burial ground at mission Dolores was once part of a much larger cemetery, the final resting place of city founders, criminals and thousands of Ohlone Native Americans."},
                "221 Fourth St San Francisco, California, 94103":{
                "location":"Leroy King Carousel","category":cats[5], 
                "description":"The Leroy King Carousel is a wonderfully well preserved and restored historical ride, hearkening back to a time when everything was new and exciting, and amusement park rides such as these were as much marveled inventions as they were public entertainment."},
                "940 Sutter StreetSan Francisco, California, 94109":{
                "location":"Hotel Vertigo","category":cats[5], 
                "description":"Originally called the Empire Hotel, the renamed Hotel Vertigo made a cameo in Hitchcock's film, Vertigo. When Hitchcock was filming his 1958 suspense classic, he chose the exterior of the Empire Hotel as the location for character Judy Barton’s home."},
                "Alvord Lake Golden Gate Park San Francisco, California, 94117":{
                "location":"Alvord Lake Bridge","category":cats[6], 
                "description":"The Alvord Lake Bridge was the first reinforced concrete bridge built in the United States, and to this day remains a viable entrance into San Francisco’s Golden Gate Park as the oldest standing bridge on the grounds."},
                "Justin Herman Plaza San Francisco, California, 94111":{
                "location":"Vaillancourt Fountain","category":cats[7], 
                "description":"Designed and executed by outspoken Canadian artist Armand Vaillancourt, this (technically) eponymous fountain has inhabited many roles in its tumultuous career as public art."},
                "1709 Broderick San Francisco, California, 94115":{
                "location":"The Full House house","category":cats[8],
                "description":"This private residence was the template for one of the most beloved television homes ever."},
                "375 Rhode Island St San Francisco, California, 94103":{
                "location":"San Francisco Center for the Book","category":cats[11], 
                "description":"This shop and studio is dedicated to the art of the book, from letterpress to bookbinding."},
                "McDowell ave and Cowles ave San Francisco, California, 94129":{
                "location":"San Francisco's Pet Cemetery","category":cats[8], 
                "description":"Just south of Crissy Fields in San Francisco’s Presidio district is a tiny cemetery bound by a white picket fence and dotted with miniature gravestones. This is the final resting place of Presidio residents’ beloved pets."},
                "320 Bowling Green Dr Golden Gate Park San Francisco, California, 94122":{
                "location":"Golden Gate Park Vintage Carousel","category":cats[5], 
                "description":"The vintage carousel that currently sits in Golden Gate Park is one of only 100 of its kind still in operation. Built in 1912 in Buffalo, NY by the renowned carousel builders the Herschell-Spillman Company, it took a long, winding path through multiple west coast parks before becoming part of the Golden Gate International Exposition on Treasure Island in 1939. After the fair closed, a $14,000 donation from Herbert Fleishhacker, a local carousel enthusiast, brought it to Golden Gate Park in 1941. Originally powered by steam, it was retrofitted with an electric engine loaned to the park by PG&E."},
                "Buena Vista Park San Francisco, California, 94117":{
                "location":"Buena Vista Park Tombstones","category":cats[8], 
                "description":"If you look very closely as you explore the winding, tree-lined paths of Buena Vista Park, overlooking Haight Street, you’ll find some of the city’s earliest tombstones, in this, the city’s earliest park."},
                "540 Broadway San Francisco, California, 94133":{
                "location":"Beat Museum","category":cats[5], 
                "description":"The Beat Museum is a bookstore and museum in the North Beach neighborhood of San Francisco. The museum contains a large collection of memorabilia from the Beat era, including personal effects and manuscripts of Allen Ginsberg, Jack Kerouac, Charles Bukowski, and other prominent poets and writers of the time."},
                "1969 California St San Francisco, California, 94109":{
                "location":"Tobin House","category":cats[8], 
                "description":"Built by Michael De Young (founder of the San Francisco Chronicle) for his daughter, Constance, the Tobin house was to be the first half of a pair."},
                "9th Avenue and Lincoln Way Golden Gate Park San Francisco, California, 94122":{
                "location":"San Francisco Botanical Gardens","category":cats[5], 
                "description":"Golden Gate Park's historic botanical collection."},
                "1001 Mariposa St #307 San Francisco, California":{
                "location":"Letterform Archive","category":cats[11], 
                "description":"A collection of over 30,000 artifacts of typography, calligraphy, and graphic design, spanning from ancient times to modern day."},
                "Entrada Court San Francisco, California, 94127":{
                "location":"Urbano Sundial","category":cats[8], 
                "description":"Dedicated on October 10, 1913, this massive white sundial measures 28 feet across and, being of recent construction as sundials go, is almost entirely for looks and attention.  It resides at the site of one of early San Francisco’s most thrilling spectator sports: the Ingleside Race Track."},
                "57 Post Street San Francisco, California, 94104":{
                "location":"Mechanics' Institute Library and Chess Room","category":cats[11], 
                "description":" A library built during San Francisco's pioneer times is a student's retreat, bibliophile's sanctuary, and chess player's delight."},
                "Church St. and 20th St. San Francisco, California, 94114":{
                "location":"The Golden Fire Hydrant","category":cats[5], 
                "description":"When San Francisco burst into flames in the days following the disastrous 1906 earthquake, much of the city’s network of fire hydrants failed. Miraculously this hydrant, nicknamed “little giant,” is said to have been the only functioning hydrant and is credited with saving the historic Mission District neighborhood from a certain fiery doom."},
                "624 Taylor Street San Francisco, California, 94102":{
                "location":"Bohemian Club ","category":cats[5], 
                "description":"The Bohemian Club was founded as an official regular meeting of journalists, artists, and musicians in 1872. The building’s exterior is adorned with plaques bearing owls and the Club’s motto, “Weaving spiders come not here,” just as it had when early members Ambrose Bierce, Mark Twain, and Jack London roamed its halls. That soon changed, however, when local businessmen and entrepreneurs were granted admission."},
                "Balmy Street San Francisco, California, 94110":{
                "location":"Balmy Alley Murals","category":cats[7], 
                "description":"In the heart of the Mission District lies the most concentrated collection of murals in San Francisco. Renowned for their political import and reverential maintenance, Balmy Alley has become a destination for appreciators of street art and political culture alike."},
                "301 Upper Terrace San Francisco, California, 94117":{
                "location":"The 'Center' of San Francisco Monument","category":cats[5], 
                "description":"Adolph Sutro's little-known, geographically inaccurate, deprecated monument."},
                "Burrit Street San Francisco, California, 94108":{
                "location":"Maltese Falcon Alleyway","category":cats[11], 
                "description":"Alleyway plaque commemorating the death of a fictional character in The Maltese Falcon, not far from the author's home."},
                "1452 Haight St San Francisco, California":{
                "location":"Dangling Legs at the Piedmont Boutique","category":cats[8], 
                "description":"An unusual marketing technique, the legs serve as a siren call (sign). Selling faux fur, disco outfits, feathery dresses, wigs, and 80s bangles, the Piedmont Boutique in the Haight Ashbury neighborhood of San Francisco sprung out of the 60s hippie counterculture. But this boutique has evolved to sell a racier selection of wares over the years, today selling lingerie, fetish wear, cigarette holders, and as the store facade suggests, fishnet leggings."},
                "398 Eddy Street San Francisco, California, 94102":{
                "location":"The Tenderloin Museum","category":cats[5], 
                "description":"A walk down memory lane in the heart of one of San Francisco's most notorious neighborhoods."},
                "Strybing Arboretum Golden Gate Park San Francisco, California, 94122":{
                "location":"Spanish Monastery Stones","category":cats[5], 
                "description":"These stones originally made up the 12th century Cisterian monastery of Santa Maria de Ovila in Spain. The abandoned buildings were purchased by William Randolph Hearst in 1931, part of his elaborate Wyntoon estate building project in Northern California. It took eleven ships to bring all of the stones to the U.S."
                "301 8th St. Rm. 215 San Francisco, California, 94103":{
                "location":"Prelinger Library","category":cats[11], 
                "description":"A privately-funded public library in San Francisco, the Prelinger was founded in 2004 and is operated by Rick Prelinger and his wife, Megan Shaw Prelinger. Together, they’ve collected more than 50,000 books, periodicals, and other pieces of printed material. Working to bridge the divide between analog and digital, the Prelingers also offer about 4,000 e-books."},
                "916 Kearny St San Francisco, California":{
                "location":"Short Story Vending Machine","category":cats[11], 
                "description":"At this vending machine, with the touch of a button, you can read a randomly selected short story."},
                "1802 Hays Street San Francisco, California 94129":{
                "location":"Arion Press and M & H Type","category":cats[11], 
                "description":"The M & H Type foundry continues to make fonts the old-fashioned way, by moulding them out of red hot metal. Located in San Francisco’s beautiful Presidio, the foundry shares a roof with one of the most vintage typesetters, Arion Press, and you can get a tour of the printing process from start to finish."},
                "1500 Sutter Street San Francisco, California, 94109":{
                "location":"Hotel Majestic","category":cats[6], 
                "description":"San Francisco's oldest operating hotel, with a Victorian atmosphere and a 'haunted' fourth floor."},
                "Strawberry Hill, Stow Lake, Golden Gate Park San Francisco, California, 94118":{
                "location":"Sweeney Observatory Site","category":cats[5], 
                "description":"Barely visible foundations remain where Stow Lake’s “observatory” once welcomed visitors."},
                "505 Sansome St San Francisco, California, 94111":{
                "location":"Site of the Niantic","category":cats[5], 
                "description":"Gold Rush ship-turned-hotel buried underneath San Francisco's financial district."},
                "Hippie Hill Golden Gate Park San Francisco, California, 94122":{
                "location":"Janis Joplin Tree","category":cats[9], 
                "description":"Now the best place in the park to find impromptu drum circles and enthusiastic pot smokers, the gentle grassy slope known as “Hippie Hill” once attracted Janis Joplin to play her guitar in the shade of the tree that now bears her name."},
                "2450 Sutter St Third Floor San Francisco, California, 94115":{
                "location":"Museum of Russian Culture","category":cats[5], 
                "description":"When you think San Francisco, you probably don’t think “babushka,” but the Museum of Russian Culture in Pacific Heights showcases Russian culture and the lives of notable Americans of Russian descent. For more than sixty years, the museum has been open to the public for free."},
                "655 Beach Street San Francisco, California, 94109":{
                "location":"Museum of Vision","category":cats[5], 
                "description":"The Museum of Vision (formerly the Museum of Ophthalmology) traces the history of ophthalmology through its collection of over 10,000 artifacts, rare books, and extensive archives. The collection dates from the third century B.C. to the present, and includes the history of the Academy, personal physician papers, medical instruments, over one thousand spectacles and additional vision aids."},
                "1 Cohen Pl San Francisco, CA 94109 ":{
                "location":"Tenderloin National Forest","category":cats[8], 
                "description":"A previously drug and trash riddled alleyway in San Francisco’s Tenderloin neighborhood is now a colorful and verdant oasis, dubbed the Tenderloin National Forest."},
                "2097 Turk Street San Francisco, California, 94115":{
                "location":"Saint John Coltrane African Orthodox Church","category":cats[8], 
                "description":"Reverend Franzo Wayne King administers spiritual enlightenment through the music of the jazz legend at this renowned house of worship."},
                "300 Funston Ave San Francisco, California, 94118":{
                "location":"Internet Archive Headquarters","category":cats[5], 
                "description":"With the stated mission of providing “universal access to all knowledge,” the Internet Archive is one of history’s most ambitious cataloging projects. So far millions of books, movies, television, music, software, and video games have been collected and digitized by the project, and that’s not counting the billions of websites they’ve been archiving over the past two decades with the Wayback Machine."},
                "San Francisco Zoo San Francisco, California, 94132":{
                "location":"Fleishhacker Pool Ruins","category":cats[5], 
                "description":"Underneath the parking lot of the San Francisco Zoo lies one of the city’s great lost landmarks: a massive saltwater swimming pool - possibly the largest in the world at the time."},
                "580 California Street San Francisco, California, 94109":{
                "location":"Corporate Goddess Sculptures","category":cats[8], 
                "description":"Twelve ghostly figures watch over San Francisco’s financial district from a rooftop perch 23 stories up, spooking those who spot them as they have for more than 20 years."},
                "Hotaling Building 451 Jackson Street San Francisco, California, 94133":{
                "location":"Hotaling Whiskey Warehouse","category":cats[5], 
                "description":"The massive Earthquake that struck San Francisco in April 1906 destroyed much of the old city’s historic waterfront, including most of the dives, dance halls and brothels that led to the Barbary Coast’s notoriety – but one important building survived: the one holding all the whiskey. The former Hotaling warehouse no longer houses whiskey, and like much of the area is now home to upscale offices."},
                "1 Dr Carlton B Goodlett Place San Francisco, California, 94102":{
                "location":"The Head of The Goddess of Progress","category":cats[7], 
                "description":"The Goddess of Progress was a towering 20-foot tall statue that stood atop San Francisco’s original city hall. The proud figure jutted out from the building’s central dome looking like the kind of iconic symbol that that comes to represent a whole city. Unfortunately this famous fate was not in the cards for the golden lady. In 1906 a massive earthquake rocked the city and the historic city hall building collapsed. Miraculously however the Goddess of Progress remained standing, lording over a pile of rubble."},
                "Spreckels Temple of Music, Music Concourse, Golden Gate Park, San Francisco, California, 94118":{
                "location":"Spreckels Temple of Music","category":cats[6], 
                "description":"Erected in 1900 at the music concourse established for the 1894 California Midwinter Exposition, the classically inspired band shell was a gift to the city from sugar mogul Claus Spreckels."},
                "578-598 Market St San Francisco, California 94104":{
                "location":"Admission Day Monument Octopuses","category":cats[7], 
                "description":"A pair of mutilated bronze octopuses slump at the base of the monument honoring California's admission to the U.S. "},
                "1101 Geary Blvd, San Francisco, CA 94109":{
                "location":"Portrait of Emperor Norton","category":cats[8], 
                "description":"A mysterious painting of the self-declared Emperor of the United States watches over local hof-brau, Tommy's Joynt."},
                "121 Spear St. San Francisco, California, 94105":{
                "location":"Rincon Center Murals","category":cats[7], 
                "description":"These murals were the work of Russian-born artist Anton Refregier who won a competition to paint the works in the newly built Rincon Annex Post Office. From a period between 1941-1948, interrupted by the outbreak of World War II, Refregier created 27 murals on the walls of the post office’s main hall. He worked in a “social realist” style that endeavored to paint the lives of the working class as they were with little aggrandizement."},
                "1000 Great Highway San Francisco, California, 94121":{
                "location":"Beach Chalet WPA Murals","category":cats[7], 
                "description":"The inside of the Beach Chalet is adorned with exceptional WPA era murals depicting scenes from the everyday life of the city and Golden Gate Park."},
                "555 California St, San Francisco, CA 94104":{
                "location":"Banker's Heart","category":cats[7], 
                "description":"This sculpture’s official name is “Transcendence,” and it was sculpted by Masayuki Nagare from 200 tons of black Swedish granite. It was commissioned in 1969 for the A.P. Giannini Plaza of 555 California Street, the building that was originally the headquarters for Bank of America, and as such, a hub of San Francisco finance."},
                "300 Post St San Francisco, CA 94108":{
                "location":"Ruth Asawa’s San Francisco Fountain","category":cats[7], 
                "description":"World-renowned San Francisco sculptor Ruth Asawa produced this intricately detailed monument to San Francisco in 1972, featuring whimsical bas-relief scenes of the city. The large circular fountain is comprised of 41 individual bronze panels overflowing with San Francisco landmarks—all arranged relative to their location to Union Square—along with fantastical fictional characters."},
                "Elizabeth Street and Douglas Street San Francisco, California, 94114":{
                "location":"1908 Cistern Circles","category":cats[5], 
                "description":"175 cisterns holding between 75,000-200,000 gallons of water are distributed through the city, marked on the surface by circles of red brick and a nearby hydrant topped with a green cap. The cisterns represent a worst-case-scenario fire solution based on ancient technology."},
                "501 Taylor Street San Francisco, California, 94102":{
                "location":"Birthplace of Isadora Duncan","category":cats[5], 
                "description":"Isadora Duncan was known as a mother of modern dance, and defied the current social and dance conventions. She favored barefeet, flowing clothing, loose hair, and free form movements. Her communist leanings and unconventional - some might say scandalous– love life made her a controversial figure. She has since appeared in pop culture, including a 1968 film in which she was portrayed by Vanessa Redgrave."},
                "Murphy Windmill and Millwright Cottage Martin Luther King, Jr. Drive Golden Gate Park San Francisco, California, 94121":{
                "location":"Murphy Windmill","category":cats[6], 
                "description":"The second of two enormous windmills built in Golden Gate Park, Murphy windmill was capable of drawing an impressive 40,000 gallons of water per hour on a windy day, helping to transform the shifting ocean-side dunes into the green of parkland."},
                "1000 Great Highway San Francisco, California, 94121":{
                "location":"Golden Gate Park Diorama","category":cats[8], 
                "description":"Inside the classic Art Deco lobby of the Beach Chalet, surrounded by Lucien Labuadt WPA era frescos, sits a detailed bird’s eye view of Golden Gate Park, executed in exacting miniature."},
                "600 Montgomery St, San Francisco, CA 94111":{
                "location":"Plaque to Bummer & Lazarus","category":cats[8], 
                "description":'In a city with strict anti-stray dog policies, Bummer and Lazarus had carte blanche to do as they pleased. Their friendship was legendary and their rat-killing skills celebrated. The local newspapers chronicled their escapades and the citizens of Emperor Norton’s city loved them. The San Francisco Bulletin referred to them as “two dogs with but a single bark, two tails that wagged as one.”'},
                "2080 Washington St. San Francisco, California, 94109":{
                "location":"Spreckels Mansion","category":cats[6], 
                "description":"This French Baroque chateau was designed for Adolph and Alma de Bretteville Spreckels by George A. Applegarth, a graduate of the Ecole des Beaux Arts in Paris. In order to attain the desired views for this mansion, Spreckels had to purchase several pricey adjacent lots overlooking the San Francisco Bay and the Golden Gate Bridge. Alma insisted on saving eight of the existing Victorian-style houses across these lots, so all of them were disassembled, moved, and rebuilt elsewhere."},
                "Conservatory Dr. East Golden Gate Park San Francisco, California, 94117":{
                "location":"Golden Gate Park Horseshoe Pitch","category":cats[], 
                "description":"Built on the site of a former rock quarry, the horseshoe pitch tucked into the northeast corner of the park is easy to miss."},
                "1 Avenue of the Palms San Francisco, California, 94130":{
                "location":"Pacific Unity Sculptures","category":cats[7], 
                "description":"Twenty sculptures were commissioned by prominent sculptors for the Court of Pacifica, representing the different cultures of the Pacific nations. Most were created with cast stone and steel reinforcement, and have survived to this day - however, four of the originals, made of less permanent materials have been lost."},
                "John McLaren Memorial Rhododendron Dell. Golden Gate Park San Francisco, California, 94118":{
                "location":"John McLaren Statue","category":cats[7], 
                "description":"He fought city officials every time they wanted to place a statue in his park. When he lost the fight, he would send his men to hide the offending monument by planting trees, shrubs and vines around it, obscuring the view. Perhaps out of reverence, or perhaps as a snarky joke, on his 65th birthday McLaren was presented with a life size statue of himself."},
                "555 Pacific Ave, San Francisco, CA 94133":{
                "location":"Site of the San Francisco Hippodrome","category":cats[5], 
                "description":"This building, at 555 Pacific Street, hosted one of Terrific Street’s most beloved nightclubs, the Hippodrome. Before then, the space hosted a series of clubs. One was known as the Red Mill. It later operated as Moulin Rouge (French was classier, befitting the new surrounds)."},
                "Spreckels Lake Golden Gate Park San Francisco, California, 94121":{
                "location":"Golden Gate Park Model Yacht Club","category":cats[8], 
                "description":"The San Francisco Model Yacht Club, founded in 1898, is the oldest Model Yacht club in the Americas and has about 175 active members. Hidden out of site on most days, the club keeps a beautiful and extensive collection of model boats in its modest WPA era clubhouse."},
                "9th Avenue at Lincoln Way Golden Gate Park San Francisco, California, 94122":{
                "location":"Helen Crocker Russell Library of Horticulture","category":cats[11], 
                "description":"Home to 27,000 volumes on all aspects of plant life as well as 350 plant related periodicals and a 1,600-volume children’s botanical library, the Helen Crocker Russell Library of Horticulture is a little known gem located at the San Francisco Botanical Garden in Golden Gate Park."},
                "1100 California St San Francisco, California 94108":{
                "location":"AIDS Interfaith Memorial Chapel","category":cats[5], 
                "description":"In the north tower lobby of the impressive Grace Cathedral atop Nob Hill in San Francisco is a peaceful but provocative chapel dedicated to those who have been taken by AIDS and those who continue to fight the disease and care for its victims."},
                "1501 Van Ness Ave San Francisco, CA 94109":{
                "location":"The Last Standard Oil Company Gas Station in California","category":cats[], 
                "description":"Chevron, the West Coast and Southern descendant of Standard, has strategically maintained one Standard gas station in each of its 16 states of operation, ensuring the storied name remains a legally active trademark to this day. One of them currently stands in San Francisco, California."},
                "Speedway Meadows Golden Gate Park San Francisco, California, 94122":{
                "location":"Site of the Golden Gate Speed Road","category":cats[8], 
                "description":"Once the site of speeding horses, now home to picnickers and public concerts."},
                "1232 John F Kennedy Dr San Francisco, California, 94122":{
                "location":"Angler's Lodge and Casting Pools","category":cats[8], 
                "description":"Established in June 1933 as part of the San Francisco Fly Casting Club to create a dedicated place for local anglers to perfect their cast."},
                "3200 Washington St San Francisco, CA 94115 ":{
                "location":"Swedenborgian Church","category":cats[6], 
                "description":"The church and garden are usually open to visitors during the week (ring doorbell for sanctuary access). Church service is every Sunday at 11 a.m. and visitors are welcome. Docent-led tours can be arranged ahead of time."},
                "Rose St & Octavia St San Francisco, CA 94102 ":{
                "location":"Two O'Clock Titty","category":cats[8], 
                "description":"Thanks to a combination of the Cathedral of Saint Mary of the Assumption’s geographic location and architectural shape, a shadow in the shape of a silhouette of a woman’s breast spreads across the church for all to see each afternoon. Locals have come to call it “two o’clock titty” because the shapely melon can best be seen at this time of day thanks to the angle of the sun."},
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

