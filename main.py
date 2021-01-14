from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.csv', mode='a') as database:
        email = data['email']
        print(email)
        subject = data['subject']
        print(subject)
        message = data['message']
        print(message)
        database.write(f'\n {email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        print(email)
        subject = data['subject']
        print(subject)
        message = data['message']
        print(message)
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form
        write_to_csv(data)
        return redirect('success.html')
    else:
        return 'an error has occurred'
