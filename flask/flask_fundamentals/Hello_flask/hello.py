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


1- Home sweet home  10
2- fully experinced developper 5
3- own a bussniess localy   10
4- ramallah apartment   1
5-  new car     1
6- AWS Cloud Engineer   1
7- DevOps Engineer  1
8-  married     3
9-  childs or more  5
10- visited italy,  10
11- visited spain   10
12- visited USA     5
13- have specail place for gaming       10
14- a lovely life   5
15- a lovely wife   -
16- master digree in Bussniess  10
17- SANS (security for cloud)   5
18- bank account just like a phone number   10
19- visit makka   5
20- a fire place should be there in my home 10
21- at least 2 consultation positions   10
22- financialy free 10
23- start an investment just start  5
24- more investments work to do     5
25- R.I.P       -

1 > 2
3 > 4
5 > 7
10 > 12
---------------------------------------------


1- ramallah apartment   1
    1- find a good location
    2- finish the paper work
    3- prepare the designs and decotrations 
    4- the furniture
    5- move
      
    
2- new car     1
    1- get a new car
    

3- AWS Cloud Engineer   1
    1- cloud practionar
    2- network engineer AWS
    3- AWS Enginner full 
    
    
4- DevOps Engineer Cert.  1
    1- Ansible
    2- APIS 
    3- Git
    4- find a vacancy jops!
    5- keep pushing




1- married     3
    1- get married
    
2- visited spain   3
    1- prepare a visit to qadesh in spain 
    
    
3- SANS (security for cloud)   3
    1- new cert




1- start an investment just start  5
    1- any avaliable in that time

2- Home sweet home  5
    1- this must be done at some point
    
    
    
    
1- financialy free 10
    1- long term (bussniess or investments)