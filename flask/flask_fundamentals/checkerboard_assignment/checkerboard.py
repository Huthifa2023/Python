from flask import Flask, render_template
import math

checkerboardAPP = Flask(__name__)

@checkerboardAPP.route('/')
def eight():
    return render_template('checkerboard.html',rows=8, columns=8)

@checkerboardAPP.route('/<int:rows>')
def input_rows(rows):
    return render_template('checkerboard.html', rows=int(rows), columns=8)

@checkerboardAPP.route('/<int:rows>/<int:columns>')
def input_only(rows,columns):
    return render_template('checkerboard.html',rows=int(rows), columns=int(columns))

@checkerboardAPP.errorhandler(404)
def error_page(e):
    return "invalid URL, use x/y , or /x , or /"

if __name__ == "__main__":
    checkerboardAPP.run(debug=True)

