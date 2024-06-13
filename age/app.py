from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    name = request.form['name']
    dob = request.form['dob']
    dob = datetime.strptime(dob, '%Y-%m-%d')
    today = datetime.today()

    years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    months = today.month - dob.month + (12 * (today.year - dob.year))
    if today.day < dob.day:
        months -= 1

    age_in_seconds = (today - dob).total_seconds()

    return render_template('home.html', name=name, years=years, months=months, seconds=age_in_seconds)

if __name__ == '__main__':
    app.run(debug=True)
