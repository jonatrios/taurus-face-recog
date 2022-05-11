from flask import Flask
from services.face_recognition import face_recognition
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(face_recognition)

if __name__ == '__main__':
    app.run()
