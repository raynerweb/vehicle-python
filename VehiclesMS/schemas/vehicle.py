from marshmallow import fields, Schema


class VehicleSchema(Schema):
    id = fields.Int()
    telemetry_profile_id = fields.Str()
    driver_id = fields.Str()
    number_plate = fields.Str()
    vin = fields.Str()
    color = fields.Str()


def to_schema(kwargs):
    vehicle_schema = VehicleSchema()
    vehicle_schema.color = kwargs["color"]
    vehicle_schema.vin = kwargs["vin"]
    vehicle_schema.number_plate = kwargs["number_plate"]
    vehicle_schema.telemetry_profile_id = kwargs["telemetry_profile_id"]
    vehicle_schema.driver_id = kwargs["driver_id"]
    return vehicle_schema
