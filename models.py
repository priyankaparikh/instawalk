""" Holds all the models for the PostgreSQL DB
    DB name : """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from manage import db, app
# db = SQLAlchemy()


################################################################################

class User(db.Model):
    """ User of Instawalk."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True,
                                      primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tokens = db.Column(db.Integer, nullable=True)
    terms_agreement = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__ (self):
        """return user_information"""

        d1 = '<user_id={a}, user_name={b},'.format(a=self.user_id,
                                                b=self.user_name)
        d2 = ' password={c}, tokens={d},'.format(c=self.user_password,
                                                d=self.tokens)
        d3 = ' completed={e}'.format(e=self.completed)
        return d1 + d2 + d3


class Comp_Routes(db.Model):
    """ Lists of routes completed by users. """

    __tablename__ = 'c_routes'

    cr_id = db.Column(db.Integer, autoincrement=True,
                                    primary_key=True)
    route_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    def __repr__ (self):
        """return comp routes information"""

        d1 = '<cr_id={a}, completed={b},'.format(a=self.cr_id,
                                            b=self.completed)
        return d1


class User_Routes(db.Model):
    """ Lists of routes completed by users. """

    __tablename__ = 'u_routes'

    ur_id = db.Column(db.Integer, autoincrement=True,
                                    primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    route_id = db.Column(db.Integer, nullable=False)


    def __repr__ (self):
        """return comp routes information"""

        d1 = '<ur_id={a}, u_routes={b},'.format(a=self.ur_id,
                                            b=self.u_routes)
        return d1


class Route(db.Model):
    """ Curated routes of instawalk."""

    __tablename__ ='routes'

    route_id = db.Column(db.Integer, autoincrement=True,
                                       primary_key=True)
    waypoints = db.Column(db.ARRAY(db.Integer), nullable=False)
    route_difficulty = db.Column(db.String, nullable=False)
    route_type = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

    def __repr__ (self):
        """return route information."""

        d1 = '<route_id={a}, waypoints={b},'.format(a=self.route_id,
                                                b=self.waypoints)
        d2 = 'route_difficulty={c}, route_type={d}'.format(c=self.route_difficulty,
                                                            d=self.route_type)
        d3 = ' image_url={e}'.format(e=self.image_url)
        return d1 + d2 + d3


class Interest_Point(db.Model):
    """ Details and information about curated waypoints. """
    __tablename__ ='interest_points'

    poi_id = db.Column(db.Integer, autoincrement=True,
                                          primary_key=True)
    latitude = db.Column(db.String, nullable=False)
    longitude = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=True)

    def __repr__ (self):
        """return point of interest information."""

        d1 = '<poi_id={a}, latitude={b},'.format(a=self.poi_id,
                                                b=self.latitude)
        d2 = '<longitude={c}, location={d},'.format(c=self.longitude,
                                                d=self.location)
        d3 = '<image_url={e}, description={f},'.format(e=self.image_url,
                                                f=self.description)
        return d1 + d2 + d3


class Waypoint(db.Model):
    """ Details and information about required waypoints by Google. """

    __tablename__ ='waypoints'

    waypoint_id = db.Column(db.Integer, autoincrement=True,
                                          primary_key=True)
    latitude = db.Column(db.String, nullable=False)
    longitude = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)

    def __repr__ (self):
        """return waypoint information."""

        d1 = '<waypoint_id={a}, latitude={b},'.format(a=self.waypoint_id,
                                                b=self.latitude)
        d2 = '<longitude={c}, location={d},'.format(c=self.longitude,
                                                d=self.location)
        d3 = '<image_url={e}, description={f},'.format(e=self.image_url,
                                                f=self.description)
        return d1 + d2 + d3


class Step(db.Model):
    """ Information provided by the user within each step between two waypoints."""

    __tablename__ ='steps'

    step_id = db.Column(db.Integer, autoincrement=True,
                                      primary_key=True)
    # path_id = db.Column(db.Integer, db.ForeignKey('paths.path_id'), nullable=False)
    path_id = db.Column(db.Integer, nullable=False)
    start_point = db.Column(db.Integer, nullable=False)
    end_point = db.Column(db.Integer, nullable=True)

    # path = db.relationship("Path",
    #                        backref=db.backref("paths",
    #                        order_by=path_id
    # ))

    def __repr__ (self):
        """return route information."""

        d1 = '<step_id={a}, start_point={b},'.format(a=self.step_id,
                                                b=self.start_point)
        d2 = '<end_point={c}, directions_id={d},'.format(c=self.end_point,
                                                d=self.directions_id)
        return d1 + d2


class Direction(db.Model):
    """ Directions provided by users between two waypoints."""

    __tablename__ ='directions'

    direction_id = db.Column(db.Integer, autoincrement=True,
                                           primary_key=True)
    # step_id = db.Column(db.Integer, db.ForeignKey('steps.step_id'), nullable=False)
    step_id = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String, nullable=True)
    direction_text = db.Column(db.String, nullable=True)

    # step = db.relationship("Direction",
    #                        backref=db.backref("steps",
    #                        order_by=step_id
    # ))

    def __repr__ (self):
        """return direction information."""

        d1 = '<direction_id={a}, image_url={b},'.format(a=self.direction_id,
                                                b=self.image_url)
        d2 = '<direction_text={c}, latitude={d},'.format(c=self.direction_text,
                                                d=self.latitude)
        d3 = '<longitude={e}'.format(e=self.longitude)
        return d1 + d2 + d3


class Path(db.Model):
    """ A path is a collection of different waypoints and steps."""

    __tablename__ ='paths'

    path_id = db.Column(db.Integer, autoincrement=True,
                                      primary_key=True)
    start_point = db.Column(db.Integer, nullable=False)
    end_point = db.Column(db.Integer, nullable=False)
    sent = db.Column(db.Boolean, default=False, nullable=True)

    def __repr__ (self):
        """return path information."""

        d1 = '<path_id={a}, start_point={b},'.format(a=self.path_id,
                                                b=self.start_point)
        d2 = '<end_point={c}, steps={d},'.format(c=self.end_point,
                                                d=self.steps)
        return d1 + d2



# def connect_to_db(app, db_uri='postgresql:///instawalk'):
#     """Connect the database to our Flask app."""

#     # Configure to use our PstgreSQL database
#     app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config['SQLALCHEMY_ECHO'] = True
#     db.app = app
#     db.init_app(app)


##################################################################################

# if __name__ == "__main__":
#     from server import app
#     connect_to_db(app)
#     db.create_all()
#     print('Connected to DB.')
