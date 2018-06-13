from jinja2 import StrictUndefined
from flask import Flask, render_template, session, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2
# from OpenSSL import SSL
# import bcrypt

# context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file('/home/vagrant/src/instawalk/server.key')
# context.use_certificate_file('/home/vagrant/src/instawalk/certificate.cert')

app = Flask(__name__)
app.secret_key = 'ABCD'
# app.jinja_env.undefined = StrictUndefined
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://oyzmmmwpdkpfot:1e82487434f19e7bfd96c8730dc775e96a1fb89f907ffaf6130c9d5fdf257c9d@ec2-107-20-133-82.compute-1.amazonaws.com:5432/d1kispj4vq49gj'
UPLOAD_FOLDER = 'static/uploaded_images/'
# db = SQLAlchemy(app)

from models import connect_to_db, db
from models import (User, Comp_Routes, User_Routes, Route, Waypoint, Step, Path,
                    Direction)
from sqlalchemy import func
import queries

@app.route('/')
def landing_page():
    """Render landing page."""

    # check if user is already logged in and if they are render the index page
    if session.get('user_id'):
        return render_template('index.html')

    # if not render login page
    else:
        return render_template('login.html')


@app.route('/register', methods=['POST'])
def register_user():
    """Add a user to the database."""

    user_name = request.form.get('usrname')
    password = request.form.get('psw')
    terms = request.form.get('terms')
    tokens = 10
    terms_agreement = True

    # check if user already exists in database. if the do redirect to login
    if User.query.filter(User.user_name == user_name).all():
        return redirect('/')

    # if not in the database add them and redirect to home page
    else:
        user = User(user_name=user_name,
                    password=password,
                    tokens=tokens,
                    terms_agreement=terms_agreement)

        db.session.add(user)
        db.session.commit()

        user = User.query.filter(User.user_name == user_name).first()
        session['user_id'] = user.user_id

        return redirect('/')


@app.route('/login', methods=['POST'])
def login_user():
    """Login an already registered user."""

    user_name = request.form.get('usrname')
    password = request.form.get('psw')

    user = db.session.query(User).filter(User.user_name == user_name).first()

    # check password
    if user.password == password:
        session['user_id'] = user.user_id
        return redirect('/profile')

    else:
        return redirect('/')


@app.route('/profile', methods=['GET'])
def user_profile():
    """User profile displaying routes to unlock/walk and credits"""
    # user_name
    if session.get('user_id'):
        user_id = session.get('user_id')
        user = User.query.filter(User.user_id == user_id).first()
        user_name = user.user_name
        # tokens
        tokens = user.tokens
    else:
        return redirect('/')

    # completed routes
    completed_routes = []
    comp_routes = Comp_Routes.query.filter(Comp_Routes.user_id == user_id).all()
    for route in comp_routes:
        current_route = {}
        current_route["route_id"] = comp_routes.route_id
        completed_routes.append(current_route)

    # user routes
    user_routes = []
    user_routes = User_Routes.query.filter(User_Routes.user_id == user_id).all()
    for route in user_routes:
        current_route = {}
        current_route["route_id"] = user_routes.route_id
        user_routes.append(current_route)

    from models import Route

    # all routes
    routes = Route.query.all()
    all_routes = []

    for route in routes:
        current_route = {}
        current_route["route_id"] = route.route_id
        current_route["waypoints"] = route.waypoints
        current_route["route_difficulty"] = route.route_difficulty
        current_route["route_type"] = route.route_type
        current_route["description"] = route.description
        current_route["image_url"] = route.image_url
        all_routes.append(current_route)

    return render_template("profile.html",
                            user_name=user_name,
                            tokens=tokens,
                            completed_routes=completed_routes,
                            user_routes=user_routes,
                            all_routes=all_routes)


@app.route('/navigation', methods=['POST'])
def navigate_user():
    """ display a map with basic pins of each route """
    route_id = request.form.get('route_details')

    route = Route.query.filter(Route.route_id == route_id).first()
    route_waypoints = route.waypoints

    start_point = route_waypoints[0]
    end_point = route_waypoints[-1]


    path = Path(start_point=start_point,
                end_point=end_point,
                )
    db.session.add(path)
    db.session.commit()

    path_id_tup = db.session.query(func.max(Path.path_id)).first()
    path_id = path_id_tup[0]

    step_start = start_point
    # step_end = route_waypoints[1]
    step = Step(path_id=path_id,
                start_point=step_start,
                # end_point=step_end,
                )
    db.session.add(step)
    db.session.commit()

    return render_template('navigation.html', route_id=route_id,
                                              path_id=path_id)


# @app.route('/add_directions.json', methods=['POST'])
# def add_user_navigation():
#     """Add a users navigation directions to the database for their route."""

#     photo = request.form.get('photo')
#     directions = request.form.get('directions')

#     result = {'photo': photo, 'directions': directions}

#     return jsonify(result)


@app.route('/add_directions', methods=['POST'])
def add_user_navigation():
#     """Add a users navigation directions to the database for their route."""
#     from math import cos, asin, sqrt

    path_id = request.form.get('pathId')
    # route_id = request.form.get('routeId')
    # u_latitude = request.form.get('latitude')
    # u_longitude = request.form.get('longitude')
    # photo = request.files['imgFile']
    # direction_text = request.form.get('directions')
    
    # img_url = UPLOAD_FOLDER + photo.filename
    # photo.save(img_url)

    # route = Route.query.filter(Route.route_id == route_id).first()

    # #route_waypoints is a list of integers representing the waypoints
    # route_waypoints = route.waypoints
    # w_latlongs = []

    # for waypoint in route_waypoints:
    #     temp_dict = {}
    #     waypoint = Waypoint.query.filter(Waypoint.waypoint_id == waypoint).first()
    #     w_latitude = waypoint.latitude
    #     w_longitude = waypoint.longitude
    #     w_id = waypoint.waypoint_id
    #     temp_dict[w_id] = {'lat': w_latitude, 'lon': w_longitude}
    #     w_latlongs.append(temp_dict)

    # for i in range(len(route_waypoints)):
    #     temp = {}
    #     w_id = route_waypoints[i]
    #     waypoint = Waypoint.query.filter(Waypoint.waypoint_id == w_id).first()
    #     w_latitude = waypoint.latitude
    #     w_longitude = waypoint.longitude
    #     temp['lat'] = w_latitude
    #     temp['long'] = w_longitude
    #     w_latlongs.append(temp)

    # def distance(lat1, lon1, lat2, lon2):
    #     # haversine formula. calculating distances b/w points on the globe
    #     p = 0.017453292519943295
    #     a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    #     return 12742 * asin(sqrt(a))

    # def closest(data, v):
    #     #data is a list of dictionaries containing the latitude and longitude

    #     return min(data, key=lambda p: distance(1.0,1.0,float(p['lat']),float(p['long'])))
    # v = {'lat':u_latitude,'long':u_longitude}

    # #for w_latlong in w_latlongs:
    #     #tempDataList.append(w_latlongs[w_id])
    # closest = closest(w_latlongs, v)


    # if abs(closest['lat'] - v['lat']) <= 5.0 and abs(closest['long'] - v['long']) <= 5.0:
    #     # for w_id in w_latlongs:
    #     #     if w_latlongs[w_id] == closest:
    #     step = Step.query.filter(Step.path_id == path_id).first()
    #     setattr(step, 'end_point', w_id)
    #     session.commit()

    #     step_start = w_id
    #     path_id = path_id
    #     step = Step(path_id=path_id,
    #                 step_start=step_start
    #                 )
    #     db.session.add(step)
    #     db.session.commit()
    # else:
    # step = Step.query.filter(Step.path_id == path_id).all()
    # step_id = step[-1]

    # new_direction = Direction(step_id=step_id,
    #                           image_url=image_url,
    #                           direction_text=direction_text)

    # db.session.add(new_direction)
    # db.session.commit()


@app.route('/route_info.json', methods=['POST'])
def routes_info():
    """ forward route information to the google maps on the navigation route """

    route_id = request.form.get('id')
    waypoints = Route.query.filter(Route.route_id == route_id).all()
    waypoints = map(lambda x: x.waypoints, waypoints)
    ways = {}
    for x in waypoints:
        for y in x:
            waypoint_data = Waypoint.query.filter(Waypoint.waypoint_id == y).first()
            ways[y] = {
                'latitude': waypoint_data.latitude,
                'longitude': waypoint_data.longitude,
                'location': waypoint_data.location,
            }

    return jsonify(ways)


@app.route('/logout')
def logout_user():
    """Logout a user"""

    session.clear()

    return redirect('/')


@app.route('/waypoints_map')
def waypoints_map():
    """ display map containing all possible waypoints for route planning """
    return render_template('waypoints_map.html')


@app.route("/waypoints.json")
def jsonify_waypoints():
    waypoints = Waypoint.query.all()
    all_waypoints = {}

    while len(all_waypoints) < 350:
        for waypoint in waypoints:
            temp_dict = {
            "location": waypoint.location,
            "latitude": waypoint.latitude,
            "longitude": waypoint.longitude,
            }
            all_waypoints[waypoint.waypoint_id] = temp_dict
    return jsonify(all_waypoints)


@app.route('/finish_route')
def finish_route():
    route_id = request.form.get('compRouteId')
    tokens = queries.get_tokens(session['user_id'])
    user_id = session.get('user_id')

    # comp_route = Comp_Routes(route_id=route_id,
    #                          user_id=user_id
    #                         )
    # db.session.add(comp_route)
    # db.session.commit()

    return redirect('/profile')


@app.route('/json_output.json')
def json_output():
    result = jsonify_paths()
    return jsonify(result)


@app.route('/terms_of_service')
def terms_of_service():
    return render_template('/terms_of_service.html')


@app.route('/privacy_policy')
def privacy_policy():
    return render_template('/privacy_policy.html')


if __name__ == "__main__":
    # app.debug = True
    # app.jinja_env.auto_reload = app.debug

    connect_to_db(app)
    # app.run()

    app.run(port=5000, host='0.0.0.0')
