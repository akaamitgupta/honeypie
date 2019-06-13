import requests
from chalice import Chalice
from bs4 import BeautifulSoup

app = Chalice(app_name='honeypie')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/google-forms', methods=['POST'])
def google_forms():
    # This is the JSON body the user sent in their POST request.
    payload = app.current_request.json_body
    form_response = requests.post(payload['url'], data=payload['inputs'])

    soup = BeautifulSoup(form_response.text, 'html.parser')

    validations = {}

    for name in payload['inputs']:
        tag = soup.find("input", {"name": name})
        par = tag.find_parent(
            "div", 'freebirdFormviewerViewNumberedItemContainer'
        )
        id = [item['data-item-id'] for item in par.find_all('div', attrs={'data-item-id' : True})]
        err = soup.find(id='i.err.%s' % id[0]).text
        if (err):
            validations[name] = err

    return {'validations': validations}
