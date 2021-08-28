from os import EX_TEMPFAIL
from flask import Flask,render_template, request, redirect
from flask_pymongo import PyMongo

mongo = PyMongo()
app = Flask(__name__)

app.config["MONGO_URI"] = URI

mongo.init_app(app)


@app.route('/')
def home():
    return render_template('app.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)

@app.route('/submit_form',methods = ['POST'])
def submit_form():
    contact = mongo.db.contactDB

    data = request.form.to_dict()
    print(data)
    contact.insert_one({'text':data,'complete':False})
    return redirect('message.html')
