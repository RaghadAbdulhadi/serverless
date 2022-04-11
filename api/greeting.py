from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
from datetime import datetime


class Handler(BaseHTTPRequestHandler):

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
            language = f"Please choose the language you want to start your learning journey with!<br> Goodluck"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("<html><head><title>Title goes here.</title></body></head><body><h1>Start your Coding journey with us!</h1></body></html>".encode("utf-8"))
        self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode()) 

        self.wfile.write(language.encode())

        return

if __name__ == "__main__":
    try:
        server = HTTPServer(('localhost', 9000), Handler)
        print('Started http server')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()