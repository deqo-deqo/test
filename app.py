from flask import Flask, request, jsonify

app = Flask(__name__)

# def validate_post_data(data: dict) -> bool:

# GET
@app.route('/items', methods=['GET'])
def hello():
    return "Hello, World!"

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return jsonify({'status': 'test'})
    elif request.method == 'POST':
        return jsonify({'status': 'OK!'})


if __name__ == '__main__':
    app.run(debug=True, port = 8000)