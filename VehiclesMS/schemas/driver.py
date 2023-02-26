from marshmallow import fields, Schema


class DriverSchema(Schema):
    customer_id = fields.Str()
    driver_id = fields.Str()
    mail = fields.Str()
    name = fields.Str()
    phone = fields.Str()
