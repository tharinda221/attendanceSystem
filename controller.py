# libraries
from flask import Flask
from flask_restful import Api

from services.FingerPrintScanner import *

app = Flask(__name__)
api = Api(app)

api.add_resource(FingerPrintScanner, '/fingerPrint/<sign>')