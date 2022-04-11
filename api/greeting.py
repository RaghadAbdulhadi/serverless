from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #  request is successful and you will get your response
    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    name = dic.get('name')

    if name:
        message = f"Hello {name}"
    else:
        message = f"Hello No body"

    message += f"\n Hello to our website"
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = "Hello Amman"
    self.wfile.write(message.encode())
    return