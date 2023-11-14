from flask import Flask, render_template, request

survey_app = Flask(__name__)

@survey_app.route('/')
def mainPage():
    return render_template('dojo_survey.html')


@survey_app.route('/result', methods=["POST"])
def result():
    var = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    gender = request.form['gender']
    swear = request.form['swear']
    instruction = request.form['instruction']
    return render_template('result.html', name=var, location=location, language=language, comment=comment, gender=gender, swear=swear, instruction=instruction)

if __name__ == '__main__':
    survey_app.run(debug=True)