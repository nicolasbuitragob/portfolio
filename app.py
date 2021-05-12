from os import EX_TEMPFAIL
from flask import Flask,render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('app.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

@app.route('/submit_form',methods = ['POST'])
def submit_form():
    if request.method == 'POST':
        data =request.form.to_dict()
        write_csv(data)
        return redirect('thankyou.html')
    else:
        return  redirect('contact.html')

def write_csv(data):
    with open('messages.csv',mode = 'a') as msg:
        email = data['email']
        last_name = data['last name']
        first_name = data['name']
        subject = data['message']
        csv_write = csv.writer(msg,delimiter = ',',quotechar = "'",quoting = csv.QUOTE_MINIMAL)
        csv_write.writerow([email,first_name,last_name,subject])
