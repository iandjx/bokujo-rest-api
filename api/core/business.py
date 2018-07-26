# from rest_api_demo.database import db
# from rest_api_demo.database.models import Post, Category
from db import db
from models.cow import CowModel
from models.vaccine import VaccineModel
from models.artificialinsemination import ArtificialInseminationModel


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
    vaccine = VaccineModel(vaccine_name, cow_id)
    cow = CowModel.query.filter(CowModel.id == cow_id).one()
    db.session.add(vaccine)
    db.session.commit()


def find_vaccine():
    return VaccineModel.query.all()


def find_artificial_insemination():
    return ArtificialInseminationModel.query.all()


def inseminate_cow(data):
    semen = data.get('semen')
    cow_id = data.get('cow_id')
    artificial_insemination = ArtificialInseminationModel(semen, cow_id)
    cow = CowModel.query.filter(CowModel.id == cow_id).one()
    db.session.add(artificial_insemination)
    db.session.commit()

