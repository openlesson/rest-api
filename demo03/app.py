from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


@app.route("/demo", methods=["GET", "POST"])
def demo():
    if request.method == 'POST':
        json = request.get_json()
        print(json)
        return jsonify({"created": "OK"}), 201

    return jsonify({"response": "OK"}), 200


if __name__ == "__main__":
    app.run(debug=True)
