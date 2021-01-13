from http.server import HTTPServer, BaseHTTPRequestHandler
import pathlib


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):

        self.path = str(pathlib.Path().absolute()) + '\\file.html'
        print(self.path)
        try:
            file_to_open = open(self.path).read()
            print(file_to_open)
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()
