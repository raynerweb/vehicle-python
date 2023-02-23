from marshmallow import fields, Schema


class VehicleSchema(Schema):
    id = fields.Int()
    customer_id = fields.Int()
    telemetry_profile_id = fields.Int()
    driver_id = fields.Int()
    number_plate = fields.Str()
    vin = fields.Str()
    color = fields.Str()