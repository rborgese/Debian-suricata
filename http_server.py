from http.server import BaseHTTPRequestHandler,HTTPServer
from Shell import shell_calls

PORT = 2890

# This class will handle cofigured incoming requests
class Handler(BaseHTTPRequestHandler):

	# Handler for the GET requests
	def do_GET(self):
		# User interface
		if self.path == "/home" or self.path == "/":
			self.path = "/Web/index.html"
		if self.path == "/help":
			self.path = "/Web/html/help/help.html"
		if self.path == "/help/gettingStarted":
			self.path = "/Web/html/help/gettingStarted.html"
		if self.path == "/help/userGuide":
			self.path = "/Web/html/help/userGuide.html"

		# Clean iframe
		if self.path == "/Shell/clean":
			self.path = "/Web/index.html"
			shell_calls.reset_soup()


		# Shell scripts
		if self.path == "/Shell/scripts/Start.sh":
			self.path = "/Web/index.html"
			shell_calls.call_start()
			shell_calls.call_deps()
			shell_calls.call_install()


		# Test paths
		if self.path == "/Shell/tests/ls.sh":
			self.path = "/Web/index.html"
			print("Starting ls test")
			shell_calls.call_ls()
			print("Done")
		if self.path == "/Shell/tests/cd.sh":
			self.path = "/Web/index.html"
			print("Starting cd test")
			shell_calls.call_bad_cd()
			print("Done")

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
