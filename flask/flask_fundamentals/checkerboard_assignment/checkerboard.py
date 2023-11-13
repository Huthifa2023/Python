from flask import Flask, render_template

checkerboardAPP = Flask(__name__)

@checkerboardAPP.route('/')
def eight():
    return render_template('checkerboard.html',rows=8, columns=8,colors=['red','black'])

@checkerboardAPP.route('/<int:rows>')
def input_rows(rows):
    return render_template('checkerboard.html', rows=int(rows), columns=8, colors=['red','black'])

@checkerboardAPP.route('/<int:rows>/<int:columns>')
def input_only(rows,columns):
    return render_template('checkerboard.html',rows=int(rows), columns=int(columns), colors=['red','black'])

@checkerboardAPP.route('/<int:rows>/<int:columns>/<color1>/<color2>')
def input_with_colors(rows, columns, color1, color2):
    arr = [color1,color2]
    return render_template('checkerboard.html',rows=int(rows), columns=int(columns), colors=arr)

@checkerboardAPP.errorhandler(404)
def error_page(e):
    return "invalid URL, use x/y , or /x , or /"

if __name__ == "__main__":
    checkerboardAPP.run(debug=True)
    