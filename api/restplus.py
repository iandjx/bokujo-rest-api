from flask_restplus import Api


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


api = Api(version='1.0',
          title='Bokujo API',
          description="Farm Operation",
          authorizations=authorizations)

