# from flask import request
from flask import request

from flask import Flask, abort
app = Flask(__name__)

personnel = {
    "rachel": "Executive Vice President of Managerial Functions",
    "wallace": "Senior Vice President of Managerial Functions",
    "rosie": "Staff Vice President of Managerial Functions",
    "james": "Vice Vice President of Managerial Functions",
    "henri": "Junior Vice President of Managerial Functions"
}

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/information')
def info():
    return 'Flask is the micro-framework of choice for building Machine Learning API endpoints'

@app.route('/profile/<name>')
def profile(name):
    return f"This is the profile information for {name.upper()}"

@app.route('/personnel/<name>')
def get_personnel(name):
    if name.lower() in personnel:
        return personnel[name.lower()]
    else:
        abort(404)

if __name__ == '__main__':
    app.run(port=5001)

@app.route('/employee-search')
def employee_search():
    name = request.args.get('name')
    age = request.args.get('age')
    return f"I searched for employees named {name} who are {age} years old"
