from extensions import db


class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(36), nullable=False)
    telemetry_profile_id = db.Column(db.String(36), nullable=False)
    driver_id = db.Column(db.String(36), nullable=False)
    number_plate = db.Column(db.String(50), nullable=False)
    vin = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
