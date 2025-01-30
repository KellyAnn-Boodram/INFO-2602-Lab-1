from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied


@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)
    return "Student not found"


@app.route('/stats')
def get_stats():
  
  result = { "Chicken": 0,
             "Computer Science (Major)": 0,
             "Computer Science (Special)": 0,
             "Fish": 0,
             "Information Technology (Major)": 0,
             "Information Technology (Special)": 0,
             "Vegetable" : 0
           }
  
  for student in data:
    if student.get("pref") in result:
        result[student["pref"]] += 1
    if student.get("programme") in result:
        result[student["programme"]] += 1

  return result
    

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
  result = a + b
  return str(result)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a,b):
  result = a - b
  return str(result)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a,b):
  result = a * b
  return str(result)

@app.route('/divide/<int:a>/<int:b>')
def divide(a,b):
  if b == 0:
    return "Error: Division by zero is not allowed"
  result = a / b
  return str(result)


app.run(host='0.0.0.0', port=8080)
