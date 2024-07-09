from flask import (Flask,render_template,redirect,request,url_for,render_template_string)
from datetime import datetime
import csv

app = Flask(__name__)

@app.route("/")
def base():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("base.html",current_time=current_time)


# Route to render the form
@app.route('/login')
def form():
    return render_template('login.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    with open('submissions.csv','a') as f:
                      writer = csv.writer(f)
                      writer.writerow([name,email])
    return render_template('submitted.html',info=[name,email])

# Route to read the submission file
@app.route('/submissions')
def submissions():
    submissions = []
    with open('submissions.csv', 'r') as f:
        reader = csv.reader(f)
        submissions = list(reader)
    return render_template('submissions.html', submissions=submissions)



