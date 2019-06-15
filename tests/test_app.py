import json
from unittest import TestCase

from chalice.config import Config
from chalice.local import LocalGateway

from app import app


class TestApp(TestCase):
    """Test the honeypie app"""

    def setUp(self):
        self.lg = LocalGateway(app, Config())
        self.google_form_url = 'https://docs.google.com/forms/u/1/d/e/1FAIpQLSfM54cLPNZk4mvMWTtiRWDUi2divL2cCtGG-byj05ttig1iVQ/formResponse'  # noqa

    def test_home(self):
        response = self.lg.handle_request(
            method='GET',
            path='/',
            headers={},
            body=''
        )

        assert response['statusCode'] == 200

    def test_valid_form_success(self):
        """Test valid payload google form successful"""
        payload = {
            'url': self.google_form_url,
            'inputs': {
                'entry.505110784': '3',
                'entry.1915963433': 'Female',
                'entry.948181294': 'Delhi',
                'entry.700448681': 'C'
            }
        }

        response = self.lg.handle_request(
            method='POST',
            path='/google-forms',
            headers={'Content-Type': 'application/json'},
            body=json.dumps(payload)
        )

        assert response['statusCode'] == 200

    def test_invalid_form_failure(self):
        """Test invalid payload google form failure"""
        payload = {
            'url': self.google_form_url,
            'inputs': {
                'entry.505110784': 'accepts nuber only',
                'entry.1915963433': '',
                'entry.948181294': '',
                'entry.700448681': 'C'
            }
        }

        response = self.lg.handle_request(
            method='POST',
            path='/google-forms',
            headers={'Content-Type': 'application/json'},
            body=json.dumps(payload)
        )

        assert response['statusCode'] == 422
        assert json.loads(response['body']) == {
            'errors': 'The given data was invalid.',
            'validations': {
                'entry.1915963433': 'This is a required question',
                'entry.505110784': 'Must be a number',
                'entry.948181294': 'This is a required question'
            }
        }
