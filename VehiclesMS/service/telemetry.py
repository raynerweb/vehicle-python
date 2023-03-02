import requests


def get_telemetry(vehicle_schema):
    # url = 'http://localhost:8081/tracking/telemetryprofiles/{}'.format(vehicle_schema.telemetry_profile_id)
    url = 'http://telemetry:8080/tracking/telemetryprofiles/{}'.format(vehicle_schema.telemetry_profile_id)
    telemetry_result = requests.get(url)
    return telemetry_result
