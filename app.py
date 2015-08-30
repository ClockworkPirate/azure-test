import cherrypy

class AzureTest(object):
	@cherrypy.expose
	def index(self):
		return open("index.html", "r").read()

class AzureTestAPI(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	def POST(self, direction):
		print "Recieved control."
		if direction == "f":
			print "Moving forward."
			digitalWrite(l, HIGH)
			digitalWrite(r, HIGH)
			delay(100)
		elif direction == "l":
			print "Turning left."
			digitalWrite(l, LOW)
			digitalWrite(r, HIGH)
			delay(100)
		elif direction == "r":
			print "Turning right."
			digitalWrite(l, HIGH)
			digitalWrite(r, LOW)
			delay(100)
		else:
			print "Stopping."
			digitalWrite(l, LOW)
			digitalWrite(r, LOW)

conf = {
	'/': {
		'tools.staticdir.root': os.path.abspath(os.getcwd())
	},
	'/control': {
		'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
		'tools.response_headers.on': True,
		'tools.response_headers.headers': [('Content-Type', 'text/plain')],
	},
	'/static': {
		'tools.staticdir.on': True,
		'tools.staticdir.dir': './public'
	}
}

wsgi_app = cherrypy.Application(AzureTest(), '/', conf)

# if __name__ == '__main__':
# 	l = 4
# 	r = 2
	
# 	pinMode(l, OUTPUT)
# 	pinMode(r, OUTPUT)
	
# 	conf = {
# 		'/': {
# 			'tools.staticdir.root': os.path.abspath(os.getcwd())
# 		},
# 		'/control': {
# 			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
# 			'tools.response_headers.on': True,
# 			'tools.response_headers.headers': [('Content-Type', 'text/plain')],
# 		},
# 		'/static': {
# 			'tools.staticdir.on': True,
# 			'tools.staticdir.dir': './public'
# 		}
# 	}
	
# 	cherrypy.server.socket_host = '0.0.0.0'
	
# 	page = RobotControl()
# 	page.control = RobotControlAPI()
# 	cherrypy.quickstart(page, '/', conf)
