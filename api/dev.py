from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
from datetime import datetime


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        language = dic.get('language')

        if language == "Python":
            language = f"<h2> Start with us to be a successful Python Developer</h2> <h3> Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems.</h3> <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png' alt='Python Logo' width = 250px/>"

        elif language == "Java":
            language = f"<h2>Start with us to be a successful Java Developer</h2> <h3> Java is a class-based, object-oriented programming language and is designed to have as few implementation dependencies as possible. A general-purpose programming language made for developers to write once run anywhere that is compiled Java code can run on all platforms that support Java.</h3> <img src='https://1000logos.net/wp-content/uploads/2020/09/Java-Logo.png' alt='Java Logo' width = 250px/>"
    

        elif language == "JavaScript":
            language = f"<h2>Start with us to be a successful Javascript Developer</h2><h3> JavaScript is a lightweight, cross-platform, and interpreted scripting language. It is well-known for the development of web pages, many non-browser environments also use it. JavaScript can be used for Client-side developments as well as Server-side developments.</h3> <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/480px-Unofficial_JavaScript_logo_2.svg.png' alt='C# Logo' width = 250px/>"


        elif language == "C-Sharp":
            language = f"<h2>Start with us to be a successful C-Sharp Developer</h2> <h3> C# is a general purpose object oriented programming language with multiple paradigms. It was designed for Common Language Infrastructure (CLI) in 2000 by Microsoft.for its .NET framework and also approved by ECMA and ISO. </h3> <img src='https://upload.wikimedia.org/wikipedia/commons/4/4f/Csharp_Logo.png' alt='C# Logo' width = 250px/>"


        else:
            language = f"<h2>Please choose the language you want to start your learning journey with!</h2> <h3>Available courses:</h3> - Python <br> - JavaScript <br> - Java <br> - C++ <br> <h2>Goodluck</h2>"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode()) 
        self.wfile.write("<html><head><title></title></body></head><body><h1>Start your Coding journey with us!</h1></body></html>".encode("utf-8"))
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