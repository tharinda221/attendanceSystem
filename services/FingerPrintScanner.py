from __init__ import *


class FingerPrintScanner(Resource):
    def get(self, sign):
        return "User Authorized"
