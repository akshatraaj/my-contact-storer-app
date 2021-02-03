from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Name': 'Akshat',
        'Contact': '6206763728',
        'done': False
    },
    {
        'id': 2,
        'Name': 'Arfa',
        'Contact': '8443874898',
        'done': False
    }
]


@app.route("/")
def hello_world():
    return "My Contact Storer App!"


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added succesfully!"
    })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })


if (__name__ == "__main__"):
    app.run(debug=True)
