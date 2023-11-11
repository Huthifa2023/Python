from flask import Flask, render_template

server = Flask(__name__)

@server.route('/play')
def level1():
    return render_template('playground.html', repeat=3,background='#9fc5f8')

@server.route('/play/<int:x>')
def level2(x):
    return render_template('playground.html', repeat=int(x), background='#9fc5f8')

@server.route('/play/<int:x>/<color>')
def level3(x,color):
    return render_template('playground.html', repeat=int(x), background=color)

if __name__ == '__main__':
    server.run(debug = True)

