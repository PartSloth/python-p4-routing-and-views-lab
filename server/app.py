#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    string = ""
    for num in range(parameter):
        string += str(f'{num}\n')
    return string

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == 'div':
        return str(int(num1)/int(num2))
    else:
        answer = num1 + operation + num2
        return str(eval(answer))


if __name__ == '__main__':
    app.run(port=5555, debug=True)
