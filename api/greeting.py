from http.server import BaseHTTPRequestHandler
from urllib import parse
from html.parser import HTMLParser
class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    #  request is successful and you will get your response
    s = self.path
    url_components = parse.urlsplit(s)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    language = dic.get('language')

    if language == "Python":
        language = f"Start with us to be a successful pythoneir"

    elif language == "Java":
        language = f"Start with us to be a successful Javascripter"

    elif language == "JavaScript":
        language = f"Start with us to be a successful Javascripter"

    elif language == "C++":
        language = f"Start with us to be a successful Javascripter"

    else:
        language = f"Please choose the language you want to start your learning journey with! Goodluck"

    language += f"\n Hello to our website"
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(language.encode())
    self.wfile.write("<html><head><title>Title goes here.</title></head></html>".encode("utf-8"))
    return
