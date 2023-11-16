from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')         
def index():
    return render_template("index.html")


@app.route('/send_data_to_backend', methods=['POST'])         
def receive_data_from_frontEnd():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id']   =   request.form['student_id']
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['total_orderd_fruits'] = int(session['strawberry'])+int(session['strawberry'])+int(session['apple'])
    return redirect('/show')

@app.route('/show')
def show_only():
    return render_template("checkout.html", first_name = session['first_name'], last_name=session['last_name'],
        id_id = session['student_id'], strawberry=session['strawberry'], Raspberry=session['raspberry'], Apple=session['apple'], 
        total_orderd_fruits=session['total_orderd_fruits'])



@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    


    # at aech refresh its adding a new order (makes doube than before)