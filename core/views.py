from core import app
from flask import render_template


@app.route('/')
def index():
    greeting = "Good Afternoon, Tianhao!"
    return render_template('index.html', greet=greeting)
