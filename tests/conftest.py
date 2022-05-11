import os
import pytest


@pytest.fixture(scope='function')
def image_mocker():
    image_path = os.path.join(
        os.getcwd(),
        'tests',
        'fixtures',
        'jonathan.jpeg',
    )
    return image_path


@pytest.fixture(scope='function')
def not_face_image_mocker():
    not_face_image = os.path.join(
        os.getcwd(),
        'tests',
        'fixtures',
        'WhatsApp Image 2022-04-10 at 12.20.56 PM.jpeg',
    )
    return not_face_image


@pytest.fixture(scope='function')
def not_image_mocker():
    not_image = os.path.join(
        os.getcwd(),
        'tests',
        'fixtures',
        'empty_records_xls.xlsx',
    )
    return not_image
