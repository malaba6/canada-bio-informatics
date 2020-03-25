from flask import Flask
from app.api.views import module

app = Flask(__name__)
app.register_blueprint(module)