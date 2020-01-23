import json, requests


class OpenIE5:

    def __init__(self, server_url):
        if server_url[-1] == '/':
            server_url = server_url[:-1]
        self.server_url = server_url
        self.extract_context = '/getExtraction'

    def extract(self, text, properties=None):
        assert isinstance(text, str)
        if properties is None:
            properties = {}
        else:
            assert isinstance(properties, dict)

        try:
            requests.get(self.server_url)
        except requests.exceptions.ConnectionError:
            raise Exception('Check whether you have started the OpenIE5 server')

        data = text.encode('utf-8')

        r = requests.post(
            self.server_url + self.extract_context, params={
                'properties': str(properties)
            }, data=data, headers={'Connection': 'close'})
        
        return json.loads(r.text)
