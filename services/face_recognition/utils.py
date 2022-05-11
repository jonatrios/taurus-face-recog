import inspect
import json
import cv2
from deepface import DeepFace
from typing import Any, BinaryIO, Dict
from flask import request, Response
from werkzeug.http import HTTP_STATUS_CODES


class APIException(Exception):
    default_status = 500

    def __init__(self, status_code=None, errors=None) -> None:
        self._status_code = self.default_status
        if status_code:
            self.status_code = status_code
        self.errors = [errors]
        self.error_code = HTTP_STATUS_CODES.get(status_code)

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        if value not in HTTP_STATUS_CODES:
            raise ValueError(f'Not valid HTTP Status Code: {value}')
        self._status_code = value

    def get_body(self):
        return {
            'error_code': self.error_code,
            'errors': self.errors,
        }

    def get_response(self):
        return Response(
            json.dumps(
                self.get_body(),
            ),
            status=self._status_code,
            content_type='application/json'
        )


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


TOKEN = 'ApiKey SU-799-115-572:2dee5abc7be8086ea720e95f6448b7dca7827677'


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
