# from jinja2 import StrictUndefined
from flask import Flask, render_template, session, redirect, request, jsonify
from models import connect_to_db, db
from models import User, Comp_Routes, User_Routes, Route, Waypoint, Step, Path
from sqlalchemy import func

app = Flask(__name__)
app.secret_key = 'ABCD'

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

        usr_routes = User_Routes(u_routes=[1,2,3,4,5,6,7]) #placeholder route_ids
        db.session.add(usr_routes)
        db.session.commit()
        user_routes_tup = db.session.query(func.max(User_Routes.ur_id)).first()
        user_routes = user_routes_tup[0]
        print("UR_ID:" + str(user_routes))

        user = User(user_name=user_name,
                    password=password,
                    tokens=0,
                    user_routes=user_routes,
                    completed=completed,
                )

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
    cr_id = user.completed
    comp_r = Comp_Routes.query.filter(Comp_Routes.cr_id == cr_id).first()
    completed_routes = comp_r.completed
    # user routes
    ur_id = user.user_routes
    user_r = User_Routes.query.filter(User_Routes.ur_id == ur_id).first()
    user_routes = user_r.u_routes

    from models import Route

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


@app.route('/navigation', methods=['GET'])
def navigate_user():
    """ display a map with basic pins of each route """

    route_id = request.form.get('route_id')
    return render_template('navigation.html')


@app.route('/add_directions.json', methods=['POST'])
def add_user_navigation():
    """Add a users navigation directions to the database for their route."""

    photo = request.form.get('photo')
    directions = request.form.get('directions')

    result = {'photo': photo, 'directions': directions}

    return jsonify(result)


@app.route('/route_info.json')
def routes_info():
    """ forward route information to the google maps on the navigation route """

    #return jsonify(route_info)


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

    while len(all_waypoints) < 50:
        for waypoint in waypoints:
            temp_dict = {
            "location": waypoint.location,
            "latitude": waypoint.latitude,
            "longitude": waypoint.longitude,
            }
            all_waypoints[waypoint.waypoint_id] = temp_dict
    return jsonify(all_waypoints)


@app.route('/json_output.json')
def json_output():
    


if __name__ == "__main__":
    # app.debug = True
    # app.jinja_env.auto_reload = app.debug

    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0', debug=True)
