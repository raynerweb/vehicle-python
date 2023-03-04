import json

from extensions import db
from models.vehicle import to_model
from schemas.driver import DriverSchema
from schemas.vehicle import to_schema
from service.driver import get_driver
from service.telemetry import get_telemetry


def save(kwargs):
    vehicle_schema = to_schema(kwargs)

    driver_result = get_driver(vehicle_schema)
    if not driver_result.ok:
        raise Exception("Driver Not Found")

    telemetry_result = get_telemetry(vehicle_schema)
    if not telemetry_result.ok:
        raise Exception("Telemetry Not Found")

    driver = DriverSchema().load(driver_result.json())
    telemetry_dict = json.loads(telemetry_result.content)

    vehicle = to_model(driver, telemetry_dict, vehicle_schema)
    db.session.add(vehicle)
    db.session.commit()

    return vehicle
