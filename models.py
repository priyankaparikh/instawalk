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
