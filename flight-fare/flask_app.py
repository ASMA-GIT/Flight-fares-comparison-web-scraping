import argparse
import io
import os
from flask import Flask, render_template, request, redirect, flash, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/cov')
def cov():
    return render_template('cov.html')

@app.route('/international')
def international():
    return render_template('international.html')

@app.route('/domestic')
def domestic():
    return render_template('domestic.html')

@app.route('/student1')
def student1():
    return render_template('student1.html')

@app.route('/creditcard')
def creditcard():
    return render_template('creditcard.html')

@app.route('/citizen')
def citizen():
    return render_template('citizen.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/user')
def user():
    return render_template('user.html')



    
if __name__ == "__main__":
    app.run(debug=True)  # debug=True causes Restarting with sta
