from flask_restplus import Api


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


api = Api()
api.version = "1"
api.title = "Bokujo API"
api.description = "Farm Operations"
api.authorizations = authorizations

