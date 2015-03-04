import web
import json

urls = (
    '/(.*)', 'mod'
)
app = web.application(urls, globals())

class mod:
    def GET(self, name):
    	web.header('Access-Control-Allow-Origin', '*')
    	web.header('Access-Control-Allow-Credentials', 'true')
        return "Hello, world!"
    def POST(self, name):
		web.header('Access-Control-Allow-Origin', '*')
		web.header('Access-Control-Allow-Credentials', 'true')
		data = web.data()

		word = 'fun'
		if word in data:
			return json.dumps({"action": "delete", "message": "NO FUN ALLOWED"})
		else:
			return json.dumps({"action": "none"})

if __name__ == "__main__":
    app.run()