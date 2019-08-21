from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': 'Ankit',
        'location': 'KL'
    },
    {
        'id': 2,
        'name': 'Divya',
        'location': 'PJ'
    }
]


@app.route('/tasks', methods=['GET'])
def get_task():
    return jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def write_task():
    task = [
        {
            'id': 3,
            'name': 'Someone',
            'location': 'France'
        }
    ]
    tas = tasks + task
    return jsonify({'Tasks: ': tas})


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='127.0.0.1', port=1000)
