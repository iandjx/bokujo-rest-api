from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models.cowrelationship import CowRelationship
from models.cowrelationship import CowRelationship
from models.medication import MedicationModel
from models.sickness import SicknessModel
from models.vaccine import VaccineModel

from app import app
from db import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()