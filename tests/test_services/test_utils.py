import pytest

from services.face_recognition.utils import compare_faces


def test_compare_faces_success(mocker, image_mocker):
    mock = mocker.patch(
        'services.face_recognition.utils.DeepFace.verify',
        side_effect=lambda *args, **kwargs: {
            'detector_backend': 'opencv',
            'distance': 5.551115123125783e-16,
            'model': 'VGG-Face',
            'similarity_metric': 'cosine',
            'threshold': 0.4,
            'verified': True,
        },
    )

    result = compare_faces(image_mocker, image_mocker)

    mock.assert_called_once()
    assert result['verified']


def test_compare_faces_not_recognize_a_face_in_image(
    mocker,
    image_mocker,
    not_face_image_mocker,
):
    mock = mocker.patch(
        'services.face_recognition.utils.DeepFace.verify',
        side_effect=lambda *args, **kwargs: {
            'error': 'Face could not be detected.'
            'Please confirm that the picture is a face photo or consider to'
            'set enforce_detection param to False.'
        },
    )

    result = compare_faces(image_mocker, not_face_image_mocker)

    mock.assert_called_once()
    assert 'Face could not be detected.' in result['error']


def test_compare_faces_cv2_error(
    mocker,
    image_mocker,
    not_image_mocker,
):
    with pytest.raises(ValueError):
        result = compare_faces(image_mocker, None)
        print(result)

    assert 'Error while recieving image' in result['error']
