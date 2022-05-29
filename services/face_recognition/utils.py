import inspect
import cv2
from deepface import DeepFace
from decouple import config
from typing import Any, BinaryIO, Dict
from flask import request

from services.exeptions import APIException


def compare_faces(img_1: BinaryIO, img_2: BinaryIO) -> Dict[str, Any]:
    try:
        img_1 = cv2.imread(img_1)
        img_2 = cv2.imread(img_2)
        try:
            result = DeepFace.verify(img_1, img_2, detector_backend='opencv')
        except ValueError as e:
            result = {'error': f'{e}'}
    except TypeError:
        result = {'error': 'Error while recieving images'}
    return result


TOKEN = config('TAURUS_TOKEN')


def token_required(fn):
    params = tuple(inspect.signature(fn).parameters)

    def inner(*args, **kwargs):
        token_header = request.headers.get('Authorization')
        try:
            if token_header != TOKEN:
                raise APIException(
                    errors='Invalid token',
                    status_code=403
                )
        except APIException as e:
            return e.get_response()
        return fn(*params)
    return inner
