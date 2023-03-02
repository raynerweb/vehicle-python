import requests


def get_driver(vehicle_schema):
    url = 'http://localhost:8082/tracking/drivers/{}'.format(vehicle_schema.driver_id)
    # url = 'http://people:8080/tracking/drivers/{}'.format(vehicle_schema.driver_id)
    driver_result = requests.get(url)
    return driver_result
