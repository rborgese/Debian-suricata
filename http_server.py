from http.server import BaseHTTPRequestHandler,HTTPServer
from Shell import shell_calls

PORT = 8080

# This class will handle any incoming requests
class Handler(BaseHTTPRequestHandler):

	# Handler for the GET requests
	def do_GET(self):
		if self.path == "/home" or self.path == "/":
			self.path = "/Web/index.html"
		if self.path == "/help":
			self.path = "/Web/html/help/help.html"
		if self.path == "/help/gettingStarted":
			self.path = "/Web/html/help/gettingStarted.html"
		if self.path == "/help/userGuide":
			self.path = "/Web/html/help/userGuide.html"

		if self.path == "/Shell/Start.sh":
			self.path = "/Web/index.html"
			print("Test")
			find_factorial(77999)


		# Test paths
		if self.path == "/Shell/ls.sh":
			print("Starting ls test")
			shell_calls.call_ls()
			print("done")

		try:
			# Check the file extension and set mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype = "text/html"
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype = "image/jpg"
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype = "image/gif"
				sendReply = True
			if self.path.endswith(".js"):
				mimetype = "application/javascript"
				sendReply = True
			if self.path.endswith(".css"):
				mimetype = 'text/css'
				sendReply = True

			if sendReply == True:
				# Open the static file requested and send it with the correct mimetype
				open_file = open(self.path[1:])
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(bytes(open_file.read(), "utf-8"))
				open_file.close()
			return


		# Output error if the file doesn't exist
		except IOError:
			self.send_error(404,'File Not Found: {}'.format(self.path))

try:
	# Create a server and define the handler for requests
	server = HTTPServer(('', PORT), Handler)
	print ('Started httpserver on port ' , PORT)

	# Wait for incoming requests
	server.serve_forever()

except KeyboardInterrupt:
	# Disconnect on CTRL + C
	print (' ======> Disconnect received, shutting down the server')
	server.socket.close()
