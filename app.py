from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kontakt')
def contact():
    return render_template('kontakt.html')

if __name__ == "__main__":
    app.run(debug=True)