import os

from flask import Blueprint
from flask import request, Response

from services.exeptions import APIException

xml_response = Blueprint('xml_response', __name__)


@xml_response.get('/xml-response/')
def retrieve_xml_file():
    dnic = request.args.get('dnic')
    try:
        with open(os.path.join(os.getcwd(), 'xml_files', f'{dnic}.xml')) as rf:
            return Response(
                rf.read(),
                status=200,
                content_type='application/xml'
            )
    except FileNotFoundError as ex:
        try:
            raise APIException(
                errors=str(ex),
            )
        except APIException as ex:
            return ex.get_response()
