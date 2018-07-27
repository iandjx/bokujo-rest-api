from flask_restplus import reqparse

heredity_arguments = reqparse.RequestParser()
heredity_arguments.add_argument('heredity', required=False, help='cow heredity', default='all', choices=['holstein', 'wagyu', 'f1', 'all'])


# pagination_arguments = reqparse.RequestParser()
# pagination_arguments.add_argument('page', type=int, required=False, default=1, help='Page number')
# pagination_arguments.add_argument('bool', type=bool, required=False, default=1, help='Page number')
# pagination_arguments.add_argument('per_page', type=int, required=False, choices=[2, 10, 20, 30, 40, 50],
#                                   default=10, help='Results per page {error_msg}')
