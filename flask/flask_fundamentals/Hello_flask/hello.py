from flask import Flask , render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World! this is default route'  # Return the string 'Hello World!' as a response

@app.route('/ok')
def ok_page():
    return 'this same web server but another page, using ok route'

@app.route('/success')
def success():
    return 'success'

@app.route('/hi/<name>')
def hi_name(name):
    print(name)
    return('Hi ' + name)

@app.route('/registration')
def registration():
    return render_template('Registration_Form.html',value = 10 ,my_name='huthifa')


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
    {'name' : 'Michael', 'age' : 35},
    {'name' : 'John', 'age' : 30 },
    {'name' : 'Mark', 'age' : 25},
    {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
