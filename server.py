# -----------------  Flask Server  ---------------- #
# author: Sayed Mohammad Rezaie -- 11.01.2020
# github: @cdied


from flask import Flask, render_template, request, url_for, redirect
import os
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# write data to txt files
# def write_to_data(data):
#    with open('database.txt', mode='a') as database:
#        email = data['email']
#        subject = data['subject']
#        message = data['message']
#        file = database.write(f'\n {email}, {subject}, {message}')


# write data to csv files
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# submit form to collect form data to a csv file
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Did Not Saved to Database!'
    else:
        print('Somethings went wrong, Try again!')
