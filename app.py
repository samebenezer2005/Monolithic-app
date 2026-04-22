from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}

# HOME ROUTE (FIX ADDED)
@app.route('/')
def home():
    return "Flask Monolithic App is Running"

# ADD student
@app.route('/add', methods=['POST'])
def add():
    data = request.get__son()
    sid = len(students) + 1
    students[sid] = data
    return jsonify({"id": sid, "data": data})

# GET students
@app.route('/students', methods=['GET'])
def get():
    return jsonify(students)

# DELETE student
@app.route('/delete/<int:sid>', methods=['DELETE'])
def delete(sid):
    students.pop(sid, None)
    return jsonify({"message": "deleted"})

if __name__ == '__main__':
    app.run(debug=True)