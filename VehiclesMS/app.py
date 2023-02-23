from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
docs = FlaskApiSpec(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from routes.vehicle import register_routes

register_routes(app)
docs.register_existing_resources()

if __name__ == '__main__':
    app.run(debug=True)
