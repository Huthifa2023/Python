from flask import Flask

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'hello world!'


@server.route('/dojo')
def dojo():
    return 'Dojo!'


@server.route('/say/<input>')
def say(input):
    return 'Hi ' + input.title() +'!'


@server.route('/repeat/<int:num>/<value>')
def repeat(num, value):
    return (f'{value} \n' *int(num))


@server.errorhandler(404)
def wrong_url(e):
    return 'Sorry! No response. Try Again.'

server.run(debug=True)