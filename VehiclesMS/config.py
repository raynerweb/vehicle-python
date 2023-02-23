import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgrespw@host.docker.internal:49155//vehicle'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

