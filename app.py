import requests
from chalice import Chalice, Response

from chalicelib.scraper import Scraper


app = Chalice(app_name='honeypie')


@app.route('/')
def index():
    return 'Keep Calm and Enjoy Honeypie'


@app.route('/google-forms', methods=['POST'])
def google_forms():
    # This is the JSON body the user sent in their POST request.
    payload = app.current_request.json_body
    form_response = requests.post(payload['url'], data=payload['inputs'])

    if form_response.status_code == 200:
        return {'message': 'Your response has been recorded.'}

    scraper = Scraper(form_response.text, payload['inputs'])

    response_body = {
        'errors': 'The given data was invalid.',
        'validations': scraper.handle()
    }

    return Response(body=response_body, status_code=422)
