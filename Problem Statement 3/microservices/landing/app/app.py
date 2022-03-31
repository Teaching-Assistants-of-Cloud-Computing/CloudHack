from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    request = requests.get('http://addition-service:5051' + '/' + n1 + '/' + n2)
    return request.json()['ans']

def minus(n1, n2):
    request = requests.get('http://subtraction-service:5052' + '/' + n1 + '/' + n2)
    return request.json()['ans']

def multiply(n1, n2):
    request = requests.get('http://multiplication-service:5053' + '/' + n1 + '/' + n2)
    return request.json()['ans']

def divide(n1, n2):
    request = requests.get('http://division-service:5054' + '/' + n1 + '/' + n2)
    return request.json()['ans']
    
def greaterthan(n1, n2):
    request = requests.get('http://greaterthan-service:5055' + '/' + n1 + '/' + n2)
    return request.json()['ans']

def exponent(n1, n2):
    request = requests.get('http://exponent-service:5056' + '/' + n1 + '/' + n2)
    return request.json()['ans']

def equal(n1, n2):
    request = requests.get('http://equal-service:5057' + '/' + n1 + '/' + n2)
    return request.json()['ans']

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
    elif operation=='greaterthan':
        result = greaterthan(number_1,number_2)
    elif operation=='exponent':
        result = exponent(number_1,number_2)
    elif operation=='equal':
        result = equal(number_1,number_2)

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )