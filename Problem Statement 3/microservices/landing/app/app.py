from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    return n1+n2

def minus(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = add(number_1, number_2)
    elif operation == 'minus':
        result =  minus(number_1, number_2)
    elif operation == 'multiply':
        result = multiply(number_1, number_2)
    elif operation == 'divide':
        result = divide(number_1, number_2)

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )