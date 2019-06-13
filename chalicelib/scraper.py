from bs4 import BeautifulSoup


class Scraper():

    def __init__(self, html, inputs):
        self.inputs = inputs
        self.soup = BeautifulSoup(html, 'html.parser')

    def handle(self):
        """Scrap and return the validations given by google forms"""
        validations = {}

        for name in self.inputs:
            input_tag = self.soup.find(
                'input', {'name': name}
            )

            if input_tag:
                parent = input_tag.find_parent(
                    'div', 'freebirdFormviewerViewNumberedItemContainer'
                )
                data_item_id = self.get_input_data_id(
                    parent.find_all('div', attrs={'data-item-id': True})
                )
                err = self.soup.find(id='i.err.%s' % data_item_id).text
                if (err):
                    validations[name] = err

        return validations

    def get_input_data_id(self, data_items):
        return [item['data-item-id'] for item in data_items][0]
