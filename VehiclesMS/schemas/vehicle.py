from marshmallow import fields, Schema


class VehicleSchema(Schema):
    telemetry_profile_id = fields.Str()
    driver_id = fields.Str()
    number_plate = fields.Str()
    vin = fields.Str()
    color = fields.Str()
