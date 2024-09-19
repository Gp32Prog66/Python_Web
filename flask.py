from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = 'Index Python File!'
    return render_template('index.html', title=title)

@app.route('/about/')
def about():
    title = 'Python Web Template'
    return render_template('about.html', title=title)