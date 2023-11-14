from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    id_id   =   request.form['student_id']
    strawberry = request.form['strawberry']
    Raspberry = request.form['raspberry']
    Apple = request.form['apple']
    total_orderd_fruits = int(strawberry)+int(Raspberry)+int(Apple)
    return render_template("checkout.html", first_name = first_name, last_name=last_name,
        id_id = id_id, strawberry=strawberry, Raspberry=Raspberry, Apple=Apple, 
        total_orderd_fruits=total_orderd_fruits )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    


    # at aech refresh its adding a new order (makes doube than before)