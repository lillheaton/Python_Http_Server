from http.server import HTTPServer, BaseHTTPRequestHandler

IP = ''
PORT = 8000


class RequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		print('GET')
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()

		self.wfile.write(bytes("Hello World", "UTF-8"))
		return


def run(server=HTTPServer, handler=BaseHTTPRequestHandler):
	address = (IP, PORT)
	httpd = server(address, handler)
	httpd.serve_forever()


if __name__ == '__main__':
	run(HTTPServer, RequestHandler)