# from rest_api_demo.database import db
# from rest_api_demo.database.models import Post, Category
from db import db
from models.cow import CowModel
from models.vaccine import VaccineModel


def create_cow(data):
    pub_id = data.get('pub_id')
    private_id = data.get('private_id')
    heredity = data.get('heredity')
    cow = CowModel(pub_id, private_id, heredity)
    db.session.add(cow)
    db.session.commit()


def find_cow(data):
    if data.get('heredity') == 'all':
        return CowModel.query.all()
    if data.get('heredity'):
        return CowModel.query.filter_by(heredity=data.get('heredity')).all()


def give_vaccine(data):
    vaccine_name = data.get('vaccine_name')
    # date_given = data.get('date_given')
    cow_id = data.get('cow_id')
    print(data)
    vaccine = VaccineModel(vaccine_name, cow_id)
    print(vaccine)
    db.session.add(vaccine)
    db.session.commit()


def find_vaccine():
    return VaccineModel.query.all()

