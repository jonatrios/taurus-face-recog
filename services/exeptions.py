import json

from flask import Response
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


class CustomFileError(APIException, FileNotFoundError):
    pass
