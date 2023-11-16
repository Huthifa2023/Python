from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'keyKEY'


@app.route('/')
def main():
    if 'counter' in session:
        session['counter'] += session['value'] if 'value' in session else 1 
        session.pop('value',None)       #here it will always make a pop, when there is no 'value' in sessoin this pop function will return None (but not error)
    else: session['counter'] = 1 
    return render_template('/counter.html')

@app.route('/two')      #can be requested from <a>
def add_two():
    session['value'] = 2
    return redirect('/')

@app.route('/add_value', methods=['POST'])      #requested using form; submit type button 
def add_value():
    session['value'] = int(request.form['value'])
    return redirect('/')

@app.route('/destroy_session')      #requested from <a>
def clear_count():
    # session.clear() or:
    session.pop('value',None)
    session.pop('counter')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)