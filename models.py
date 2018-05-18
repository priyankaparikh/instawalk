""" Holds all the models for the postgres SQL DB
    DB name : """

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

################################################################################

class User(db.Model):
    """ User of Instawalk."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True,
                                    primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    tokens = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.ARRAY(db.Integer), nullable=False)

    def __repr__ (self):
        """return user_information"""

        d1 = '<user_id={a}, user_name={b},'.format(a=self.user_id,
                                                b=self.user_name)
        d2 = ' password={c}, tokens={d},'.format(c=self.user_password,
                                                d=self.tokens)
        d3 = ' completed={e}'.format(e=self.completed)
        return d1 + d2 + d3

class Route(db.Model):
""" Curated routes of instawalk."""

    __tablename__ ='routes'

    route_id = db.Column(db.Integer, autoincrement=True,
                                    primary_key=True)
    waypoints = db.Column(db.ARRAY(db.String), nullable=False)
    route_type = db.Column(db.String, nullable=False)

    def __repr__ (self):
        """return route information."""

        d1 = '<route_id={a}, waypoints={b},'.format(a=self.user_id,
                                                b=self.waypoints)
        d2 = ' route_type={c}'.format(c=self.route_type)
        return d1 + d2

class Waypoint(db.Model):
""" Details and information about required waypoints by Google."""

    __tablename__ ='waypoints'

    waypoint_id = db.Column(db.Integer, autoincrement=True,
                                    primary_key=True)
    latitude = db.Column(db.String, nullable=False)
    longitude = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)

    def __repr__ (self):
        """return waypoint information."""

        d1 = '<waypoint_id={a}, latitude={b},'.format(a=self.waypoint_id,
                                                b=self.latitude)
        d2 = '<longitude={c}, address={d},'.format(c=self.longitude,
                                                d=self.address)
        d3 = '<image_url={e}, description={f},'.format(e=self.image_url,
                                                f=self.description)
        return d1 + d2 + d3

class Step(db.Model):
""" Information provided by the user within each step between two waypoints."""

    __tablename__ ='steps'

    step_id = db.Column(db.Integer, autoincrement=True,
                                    primary_key=True)
    start_point = db.Column(db.Integer, nullable=False)
    end_point = db.Column(db.Integer, nullable=False)
    directions = db.Column(db.ARRAY(db.Integer), nullable=False)

    def __repr__ (self):
        """return route information."""

        d1 = '<step_id={a}, start_point={b},'.format(a=self.step_id,
                                                b=self.start_point)
        d2 = '<end_point={c}, directions={d},'.format(c=self.end_point,
                                                d=self.directions)
        return d1 + d2

class Direction(db.Model):
""" Directions provided by users between two waypoints."""

    __tablename__ ='directions'

    direction_id = db.Column(db.Integer, autoincrement=True,
                                    primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    direction_text = db.Column(db.String, nullable=False)
    latitude = db.Column(db.String, nullable=True)
    longitude = db.Column(db.String, nullable=True)

    def __repr__ (self):
        """return direction information."""

        d1 = '<direction_id={a}, image_url={b},'.format(a=self.direction_id,
                                                b=self.image_url)
        d2 = '<direction_text={c}, latitude={d},'.format(c=self.direction_text,
                                                d=self.latitude)
        d3 = '<longitude={e}'.format(e=self.longitude)
        return d1 + d2 + d3

class Path(db.Model):
""" A path is a collection of different waypoints."""

    __tablename__ ='paths'

    path_id = db.Column(db.Integer, autoincrement=True,
                                    primary_key=True)
    start_point = db.Column(db.Integer, nullable=False)
    end_point = db.Column(db.Integer, nullable=False)
    steps = db.Column(db.ARRAY(db.Integer), nullable=False)

    def __repr__ (self):
        """return path information."""

        d1 = '<path_id={a}, start_point={b},'.format(a=self.path_id,
                                                b=self.start_point)
        d2 = '<end_point={c}, steps={d},'.format(c=self.end_point,
                                                d=self.steps)
        return d1 + d2

db.session.commit()

##################################################################################

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    db.create_all()
    print 'Connected to DB.'
