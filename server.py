from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('app.html')


@app.route('/projects')
def projects():
    return 'PROJECTS PAGE'

@app.route('/contact')
def contact():
    return 'CONTACT PAGE'