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


def to_model(driver, telemetry_dict, vehicle_schema):
    vehicle = Vehicle()
    vehicle.telemetry_profile_id = telemetry_dict["telemetryprofileId"]
    vehicle.driver_id = driver['driver_id']
    vehicle.customer_id = driver['customer_id']
    vehicle.number_plate = vehicle_schema.number_plate
    vehicle.vin = vehicle_schema.vin
    vehicle.color = vehicle_schema.color
    return vehicle
