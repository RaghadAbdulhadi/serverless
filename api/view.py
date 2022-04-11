import logging
from http.server import BaseHTTPRequestHandler
from urllib import parse
class handler(BaseHTTPRequestHandler):
    def main(self):
        request_json = self.get_json()
        headers = {
            'Access-Control-Allow-Origin': '*'
        }
        if self.args and 'message' in self.args:
            logging.info(self.args.get('message'))
            logging.info('value is found in selfs.args')
            return (self.args.get('message'), 200, headers)
        else:
            return ('Hello World!', 200, headers)