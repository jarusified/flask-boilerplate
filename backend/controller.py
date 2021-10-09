import os
import warnings

from flask import Flask, json, jsonify
from flask_cors import CORS, cross_origin

from logger import get_logger
from services import YourService

# Globals
FOLDER_PATH = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER_PATH = os.path.join(FOLDER_PATH, "app/")
LOGGER = get_logger(__name__)


# Create a Flask server.
app = Flask(__name__, static_url_path="", static_folder=STATIC_FOLDER_PATH)

# Enable CORS
cors = CORS(app, automatic_options=True)
app.config["CORS_HEADERS"] = "Content-Type"


class Controller:
    """
    HTTP Server Class.
    """

    def __init__(self, yourService: YourService):

        LOGGER.info(f"{type(self).__name__} mode enabled.")
        self.yourService = yourService
        self.handle_routes()

    def start(self, host: str, port: int) -> None:
        """
        Launch the Flask application.

        :param host: host to run API server
        :param port: port to run API server
        :return: None
        """
        LOGGER.info("Starting the API service")
        app.run(host=host, port=port, threaded=True, debug=True)

    @staticmethod
    def emit_json(endpoint: str, json_data: any, status: int) -> str:
        """
        Emit the json data to the endpoint

        :param endpoint: Endpoint to emit information to.
        :param json_data: Data to emit to the endpoint
        :return response: Response packed with data (in JSON format).
        """
        try:
            response = app.response_class(
                response=json.dumps(json_data),
                status=status,
                mimetype="application/json",
            )
            response.headers.add("Access-Control-Allow-Headers", "*")
            response.headers.add("Access-Control-Allow-Methods", "*")
            return response
        except ValueError:
            warnings.warn(f"[API: {endpoint}] emits no data.")
            return jsonify(isError=True, message="Error", statusCode=500)

    def handle_routes(self):
        @app.route("/")
        @cross_origin()
        def index():
            print("Test")
            return app.send_static_file("index.html")

        # Example GET and POST request.
        @app.route("/post_xxx", methods=["POST"])
        @cross_origin()
        def postXXX():
            return YourService.postJSON()

        @app.route("/get_xxx", methods=["POST"])
        @cross_origin()
        def get_xxx():
            return {}

      