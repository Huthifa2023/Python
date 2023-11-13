from flask import Flask, render_template

html_table = Flask(__name__)

@html_table.route('/')
def data():
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('html_table.html', users = users)

if __name__ == '__main__':
    html_table.run(debug = True)