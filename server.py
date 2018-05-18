from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing_page():
    """Render landing page."""

    return render_template('landing.html')


@app.route('/register')
def register_user():
    """Add a user to the database."""


@app.route('/login')
def login_user():
    """Login an already registered user."""



if __name__ == "__main__":

    app.run(port=5000, host='0.0.0.0', debug=True)