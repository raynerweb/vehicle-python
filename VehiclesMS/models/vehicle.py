from flask_sqlalchemy import SQLAlchemy

from app import db


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    telemetry_profile_id = db.Column(db.Integer, nullable=False)
    driver_id = db.Column(db.Integer, nullable=False)
    number_plate = db.Column(db.String(50), nullable=False)
    vin = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
