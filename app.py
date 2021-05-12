from os import EX_TEMPFAIL
from flask import Flask,render_template, request, redirect
a
pp = Flask(__name__)


@app.route('/')
def home():
    return render_template('app.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

@app.route('/submit_form',methods = ['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('thankyou.html')
    else:
        return  redirect('contact.html')

def write_to_file(data):
    with open('messages.txt',mode = 'a') as msg:
        email = data['email']
        first_name = data['name']
        last_name = data['last name']
        subject = data['message']
        file = msg.write(f"\n{email},{first_name},{last_name},{last_name},{subject}")
