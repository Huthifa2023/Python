from flask import Flask, render_template, request

server = Flask(__name__)

@server.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@server.route('/users', methods=['POST'])
def get_input():
    get_name = request.form['name']
    get_email = request.form['email']
    return render_template('display_data_from_user.html', name = get_name, email = get_email)


if __name__ == '__main__':
    server.run(debug=True)