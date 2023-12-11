import json
import sqlite3 as sql
from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS


from flask import Flask, render_template,request
app=Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.get('/contact')
def contact():
    return render_template('contact.html')

@app.post('/contact')
def contactform():
    print(request.form)
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True,use_reloader=True)