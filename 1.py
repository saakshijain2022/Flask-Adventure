# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'saakshi hello'
app.add_url_rule('/', 'sam hello', hello_world)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	# app.run()
	app.run(debug = True)

# The route() function  -  is a decorator, which tells the application which URL should call the associated function.

# app.route(rule, options)

# The rule parameter represents URL binding with the function.

# The options is a list of parameters to be forwarded to the underlying Rule object.

# In the above example, ‘/’ URL is bound with hello_world() function. Hence, when the home page of web server is opened in browser, the output of this function will be rendered.

# Finally the run() method of Flask class runs the application on the local development server.

# app.run(host, port, debug, options)
# All parameters are optional

# Sr.No.		
# 1. host - Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally

# 2 port - Defaults to 5000

# 3	debug - Defaults to false. If set to true, provides a debug information

# 4	options - To be forwarded to underlying Werkzeug server.

#Debug mode

# A Flask application is started by calling the run() method. However, while the application is under development, it should be restarted manually for each change in the code.

# To avoid this inconvenience, enable debug support. The server will then reload itself if the code changes. It will also provide a useful debugger to track the errors if any, in the application.

# The Debug mode is enabled by setting the debug property of the application object to True before running or passing the debug parameter to the run() method.

# app.debug = True
# app.run()
# app.run(debug = True)

# The add_url_rule() function of an application object is also available to bind a URL with a function as in the above example, route() is used.

# A decorator’s purpose is also served by the following representation −

# def hello_world():
#    return ‘hello world’
# app.add_url_rule(‘/’, ‘hello’, hello_world)


#You can also add variables in your web app, well you might be thinking about how it’ll help you,
#it’ll help you to build a URL dynamically
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
return 'Hello %s!' % name

if __name__ == '__main__':
app.run()
#And go to the URL http://127.0.0.1:5000/hello/geeksforgeeks 
#the following output hello geeksforgeeks
