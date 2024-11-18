from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return 'Hello, World! (GET request)'
    elif request.method == 'POST':
        data = request.get_json()  # Expecting JSON data in the POST request
        return jsonify({
            "message": "Hello, World! (POST request)",
            "received_data": data
        })

if __name__ == '__main__':
    app.run(debug=True)




