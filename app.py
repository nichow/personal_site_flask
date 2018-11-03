from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aboutsite')
def aboutsite():
    return render_template('aboutsite.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/writing')
def writing():
    return render_template('writing.html')

