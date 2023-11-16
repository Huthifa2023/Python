from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = 'huthifa'

@app.route('/')
def mainpage():
    return render_template('Great_Number_Game.html')

@app.route('/guess', methods=['POST'])
def guess():
    if 'guess_counter' not in session:                      #first time guess button pressed
        session['random_number'] = int(random.random()*100)
        session['guess_counter'] = 1
    session['user_guess'] = int(request.form['guess'])
    if session['user_guess'] > session['random_number']:
        session['hint'] = 'Too High!'
        session['color'] = 'warning'
    elif session['user_guess'] < session['random_number']:
        session['hint'] = 'Too Low!'
        session['color'] = 'warning'
    elif session['user_guess'] == session['random_number']:
        session['congrats'] = 'You Got it!'
        session['hint'] = 'Well Done'
        session['color'] = 'success'
    session['guess_counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if(__name__) == '__main__':
    app.run(debug = True)