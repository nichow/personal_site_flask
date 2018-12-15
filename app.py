from flask import Flask
from flask import render_template
from templateVariables import navigation, subheading, stories, essays

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', navigation=navigation, subheading=subheading)


@app.route('/aboutsite')
def aboutsite():
    return render_template('aboutsite.html', navigation=navigation, subheading=subheading)


@app.route('/contact')
def contact():
    return render_template('contact.html', navigation=navigation, subheading=subheading)


@app.route('/experience')
def experience():
    return render_template('experience.html', navigation=navigation, subheading=subheading)


@app.route('/music')
def music():
    return render_template('music.html', navigation=navigation, subheading=subheading)


@app.route('/skills')
def skills():
    return render_template('skills.html', navigation=navigation, subheading=subheading)


@app.route('/writing')
def writing():
    return render_template('writing.html', navigation=navigation, subheading=subheading, stories=stories, essays=essays)


@app.route('/pot')
def pot():
    return render_template('pot.html', navigation=navigation, subheading=subheading)
# if __name__ == "__main__":
#     app.run()
