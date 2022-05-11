from pathlib import Path
import tempfile

from flask import Blueprint
from flask import request
from services.face_recognition.utils import compare_faces, token_required

face_recognition = Blueprint('face_recognition', __name__)


@face_recognition.post('/compare/')
@token_required
def compare():
    id_image = request.files.get('id_image', None)
    selfie_image = request.files.get('selfie_image', None)
    if id_image is None or selfie_image is None:
        compare_result = {'error': 'Missing one image for recognition'}
    else:
        with tempfile.TemporaryDirectory() as td:
            id_temp_image = Path(td) / 'id_image'
            selfie_temp_image = Path(td) / 'selfie_image'

            id_image.save(id_temp_image)
            selfie_image.save(selfie_temp_image)

            compare_result = compare_faces(
                str(id_temp_image),
                str(selfie_temp_image),
                )
    compare_result = (
        (compare_result, 400)
        if 'error' in compare_result
        else (compare_result, 200)
        )
    return compare_result
