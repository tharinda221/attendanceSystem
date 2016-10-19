import os

from controller import *

app.config.from_object(__name__)
app.secret_key = os.urandom(24)
app.debug = True
app.root = os.path.abspath(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tharinda2221@gmail.com'
app.config['MAIL_PASSWORD'] = '920371230v'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)