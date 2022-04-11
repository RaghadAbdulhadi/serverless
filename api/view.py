from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):

        # to open/create a new html file in the write mode
    f = open('GFG.html', 'w')
    
    # the html code which will go in the file GFG.html
    html_template = """<html>
    <head>
    <title>Title</title>
    </head>
    <body>
    <h2>Welcome To GFG</h2>
    
    <p>Default code has been loaded into the Editor.</p>
    
    </body>
    </html>
    """
    
    # writing the code into the file
    f.write(html_template)
    
    # close the file
    f.close()
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.wfile.write(html_template.encode())
    return