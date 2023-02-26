import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres_telemetry:postgres_telemetry@127.0.0.1:5432/vehicle'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

