#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_page(parameter):
    print(parameter)
    return f"{parameter}"

@app.route("/count/<int:number>")
def count_page(number):
    list = []
    for i in range(number):
        print(i)
        list.append(f"{i}\n")
    return "".join(list)

@app.route("/math/<int:num1><operator><int:num2>")
def math_page(num1, operator, num2):
    if operator == "+":
        return f"{num1 + num2}"
    elif operator == "-":
        return f"{num1 - num2}"
    elif operator == "*":
        return f"{num1 * num2}"
    elif operator == "div":
        return f"{num1 / num2}"
    elif operator == "%":
        return f"{num1 % num2}"
    else:
        return "Improper operator!"

if __name__ == '__main__':
    app.run(port=5555, debug=True)