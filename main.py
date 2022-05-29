from flask import Flask
from services import (
    face_recognition,
    xml_response,
)
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(face_recognition)
app.register_blueprint(xml_response)

if __name__ == '__main__':
    app.run()
