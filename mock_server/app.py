from flask import Flask , jsonify , request
import data_retrieve

app = Flask(__name__)




@app.route("/get_users",methods=["GET"])
def get_users():
    return jsonify(data_retrieve.get_users()) , 200


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    new_user = data_retrieve.add_user(data)
    return jsonify({"message": "User added", "user": new_user}), 201









if __name__ == "__main__":
    app.run(debug=True, port=5000)