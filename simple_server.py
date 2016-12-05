import SimpleHTTPServer
import SocketServer
import webbrowser

PORT = 8000

def start():
	HttpHandler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer(("", PORT), HttpHandler)
	print("Starting server at port 8000")
	webbrowser.open('http://localhost:8000') # open in a new tab
	httpd.serve_forever()