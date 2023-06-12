#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__) # equal to the name of the module in question 


@app.route('/') # registers the function with the Flask application instance app
#@app.route() decorator - an instance method that modifies app, creating a rule that requests for the base URL (/) should show our index.
def index():
    return '<h1>Welcome to my page!</h1>' 

#Anything included in the route passed to the app.route decorator with angle brackets <> surrounding it will be passed to the decorated function as a parameter. 
@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>' 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
