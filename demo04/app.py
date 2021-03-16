from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
cors = CORS(app)
app.config['JWT_SECRET_KEY'] = 'super secret key'
jwt = JWTManager(app)


@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({"access_token": create_access_token(identity=data['login'])})


@app.route("/demo", methods=["GET", "POST"])
@jwt_required()
def demo():
    user = get_jwt_identity()
    print("Access for user", user)
    if request.method == 'POST':
        json = request.get_json()
        print(json)
        return jsonify({"created": "OK"}), 201

    return jsonify({"response": "OK"}), 200


if __name__ == "__main__":
    app.run(debug=True)
