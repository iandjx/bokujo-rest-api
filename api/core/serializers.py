from flask_restplus import fields
from api.restplus import api

vaccine = api.model('Vaccine', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a vaccine given'),
    'vaccine_name': fields.String(required=True, description='Vaccine Name'),
    'date_given': fields.DateTime,
    'cow_id': fields.Integer(attribute='cow.id'),
})

cow = api.model('Cow Make', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a cowy'),
    'pub_id': fields.String(required=True, description='Government ID'),
    'private_id': fields.String(required=True, description='Bokujo ID'),
    'heredity': fields.String(required=True, description='Heredity of Cow'),
})

cow_with_vaccine = api.inherit('Cow with vaccinations', cow, {
    'vaccines': fields.List(fields.Nested(vaccine))
})




#
# blog_post = api.model('Blog post', {
#     'id': fields.Integer(readOnly=True, description='The unique identifier of a blog post'),
#     'title': fields.String(required=True, description='Article title'),
#     'body': fields.String(required=True, description='Article content'),
#     'pub_date': fields.DateTime,
#     'category_id': fields.Integer(attribute='category.id'),
#     'category': fields.String(attribute='category.name'),
# })
#
# pagination = api.model('A page of results', {
#     'page': fields.Integer(description='Number of this page of results'),
#     'pages': fields.Integer(description='Total number of pages of results'),
#     'per_page': fields.Integer(description='Number of items per page of results'),
#     'total': fields.Integer(description='Total number of results'),
# })
#
# page_of_blog_posts = api.inherit('Page of blog posts', pagination, {
#     'items': fields.List(fields.Nested(blog_post))
# })
#
# category = api.model('Blog category', {
#     'id': fields.Integer(readOnly=True, description='The unique identifier of a blog category'),
#     'name': fields.String(required=True, description='Category name'),
# })
#
# category_with_posts = api.inherit('Blog category with posts', category, {
#     'posts': fields.List(fields.Nested(blog_post))
# })
