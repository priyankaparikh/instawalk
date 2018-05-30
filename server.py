# from jinja2 import StrictUndefined
from flask import Flask, render_template, session, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'ABCD'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xllajhyyvxmohg:586b67a7d8124b2dfbe064491e95b5c80e5042511be61108c393956923d3302a@ec2-54-225-107-174.compute-1.amazonaws.com:5432/d82mvtff7vnuge'
app.config['UPLOAD_FOLDER'] = './static/user_sourced_photos'
# db = SQLAlchemy(app)

from models import connect_to_db, db
from models import (User, Comp_Routes, User_Routes, Route, Waypoint, Step, Path,
                    Direction)
from sqlalchemy import func
import queries

import queries

# app.jinja_env.undefined = StrictUndefined


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
    terms_agreement = True

    # check if user already exists in database. if the do redirect to login
    if User.query.filter(User.user_name == user_name).all():
        return redirect('/')

    # if not in the database add them and redirect to home page
    else:
        c_routes = Comp_Routes(completed=[])
        db.session.add(c_routes)
        db.session.commit()
        completed_tup = db.session.query(func.max(Comp_Routes.cr_id)).first()
        completed = completed_tup[0]
        print("CR_ID:" + str(completed))

        usr_routes = User_Routes(u_routes=[]) #placeholder route_ids
        db.session.add(usr_routes)
        db.session.commit()
        user_routes_tup = db.session.query(func.max(User_Routes.ur_id)).first()
        user_routes = user_routes_tup[0]
        print("UR_ID:" + str(user_routes))

        user = User(user_name=user_name,
                    password=password,
                    tokens=10,
                    user_routes=user_routes,
                    completed=completed,

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
    step_end = route_waypoints[1]
    step = Step(path_id=path_id,
                start_point=step_start,
                end_point=step_end,
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
    """Add a users navigation directions to the database for their route."""

    path_id = request.form.get('pathId')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    photo = request.form.get('photo')
    # file = request.files.get('photo', None)
    # filename = secure_filename(file.filename)
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # image_url = 'static/user_sourced_photos' + str(filename)
    directions = request.form.get('directions')

    image_url = photo
    direction_text = directions
    step = Step.query.filter(Step.path_id == path_id).first()
    step_id = step.step_id

    new_direction = Direction(image_url=image_url,
                              direction_text=direction_text)

    db.session.add(new_direction)
    db.session.commit()



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
                'image_url': waypoint_data.image_url,
                'description': waypoint_data.description
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


# @app.route('/finish_route')
# def test():

#     tokens = queries.get_tokens(session['user_id'])
#     return redirect('/profile')


@app.route('/json_output.json')
def json_output():
    pass


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
    app.run(port=5000, host='0.0.0.0', debug=True)
