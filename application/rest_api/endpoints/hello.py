from flask_restplus import Namespace, Resource
from utils import request_parser
from utils import representations
from utils.logger import logger

"""
Create a parser object locally
"""
parser = request_parser.parser


"""
The assignment of api changes
"""

api = Namespace('hello', description='Simple API that returns a greeting')

"""
We also need to re-assign the route ans other decorated functions to api
"""

@api.route("/")
class HelloClass(Resource):

    # Add documentation about the parser
    @api.expect(parser, validate=True)
    def get(self):
        logger.info("Received request to /hello endpoint")

        # Collect Arguments
        args = parser.parse_args()
        logger.debug(f"Parsed request arguments: {args}")

        content_type = args.get('content-type')

        # Overrides the default response route so that the standard HTML URL can return any specified format
        if content_type == 'application/json':
            logger.info("Responding with application/json")
            return representations.application_json(
                {"greeting": "Hello World"},
                200,
                None
            )
        elif content_type == 'text/xml':
            logger.info("Responding with text/xml")
            return representations.xml(
                {"greeting": "Hello World"},
                200,
                None
            )
        else:
            logger.warning(f"Unknown content-type '{content_type}', responding with default format")
            return {
                "greeting": "Hello World"
            }