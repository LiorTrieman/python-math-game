from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is my Home page'


@app.route('/math_game')
def math_game():
    return '<h1> welcome to this math game!</h1>'


if __name__ == '__main__':
    app.run(debug=True)


#!/usr/bin/env python


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    APP.debug=True
    APP.run()