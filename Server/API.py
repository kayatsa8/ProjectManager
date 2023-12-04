from typing import Dict
from flask import Flask, request, jsonify

from ServiceLayer.Service import Service
from ServiceLayer.Response import Response

app: Flask = Flask(__name__)
service: Service = Service()


@app.route("/")
def welcome() -> str:
    return "Welcome!"

@app.route("/api/register_user", methods=["POST"])
def registerUser():
    userData: Dict[str, str] = request.get_json()
    response: Response[bool] = service.register(userData["username"], userData["password"])

    return jsonify(response.toDict()), 201











if __name__ == "__main__":
    app.run(debug=True)