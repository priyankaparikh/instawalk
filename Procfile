web: gunicorn --bind 0.0.0.0:$PORT server:app
init: python db_create.py
upgrade: python db_upgrade.py