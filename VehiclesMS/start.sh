#!/bin/bash

flask db init
flask db migrate -m "Create Tables"
flask db upgrade
python3 -m flask run --host=0.0.0.0