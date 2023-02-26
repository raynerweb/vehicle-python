from pprint import pprint

from flask import abort, Blueprint
from flask_apispec import marshal_with, use_kwargs, FlaskApiSpec
from flask_apispec.annotations import doc
from marshmallow import fields

from models.vehicle import Vehicle
from schemas.vehicle import VehicleSchema
from schemas.driver import DriverSchema

from app import db
import json
import requests

vehicles_bp = Blueprint("vehicles", __name__, url_prefix="/vehicles")


@vehicles_bp.route('/<int:vehicle_id>', methods=['GET'])
@doc(tags=['vehicles'], description='Get a single vehicle')
@use_kwargs({'vehicle_id': fields.Int()}, location='view_args')
@marshal_with(VehicleSchema)
def get_vehicle(vehicle_id):
    vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
    if not vehicle:
        abort(404, description=f"vehicle.py {vehicle_id} not found")
    return vehicle


@vehicles_bp.route('/', methods=['GET'])
@doc(tags=['vehicles'], description='Get all vehicles')
@marshal_with(VehicleSchema(many=True))
def get_all_vehicles():
    vehicles = Vehicle.query.all()
    return vehicles


@vehicles_bp.route('/', methods=['POST'])
@doc(tags=['vehicles'], description='Create a new vehicle.py')
@use_kwargs(VehicleSchema)
@marshal_with(VehicleSchema)
def create_vehicle(**kwargs):
    vehicle_schema = VehicleSchema()
    vehicle_schema.color = kwargs["color"]
    vehicle_schema.vin = kwargs["vin"]
    vehicle_schema.number_plate = kwargs["number_plate"]
    vehicle_schema.telemetry_profile_id = kwargs["telemetry_profile_id"]
    vehicle_schema.driver_id = kwargs["driver_id"]

    url = 'http://localhost:8082/tracking/drivers/{}'.format(vehicle_schema.driver_id)
    driver_result = requests.get(url)
    if not driver_result.ok:
        raise Exception("Driver Not Found")

    url = 'http://localhost:8081/tracking/telemetryprofiles/{}'.format(vehicle_schema.telemetry_profile_id)
    telemetry_result = requests.get(url)
    if not telemetry_result.ok:
        raise Exception("Telemetry Not Found")

    driver = DriverSchema().load(driver_result.json())
    telemetry_dict = json.loads(telemetry_result.content)

    vehicle = Vehicle()
    vehicle.telemetry_profile_id = telemetry_dict["telemetryprofileId"]
    vehicle.driver_id = driver['driver_id']
    vehicle.customer_id = driver['customer_id']
    vehicle.number_plate = vehicle_schema.number_plate
    vehicle.vin = vehicle_schema.vin
    vehicle.color = vehicle_schema.color

    db.session.add(vehicle)
    db.session.commit()
    return vehicle


@vehicles_bp.route('/<int:vehicle_id>', methods=['PUT'])
@doc(tags=['vehicles'], description='Update an existing vehicle.py')
@use_kwargs(VehicleSchema)
@marshal_with(VehicleSchema)
def update_vehicle(vehicle_id, **kwargs):
    vehicle = Vehicle.query.get(vehicle_id)
    for key, value in kwargs.items():
        setattr(vehicle, key, value)
    db.session.commit()
    return vehicle


def register_routes(api):
    api.register_blueprint(vehicles_bp)
