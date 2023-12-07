from typing import Dict, List, TypedDict, get_type_hints
from uu import Error
from flask import Flask, request, jsonify

from ServiceLayer.Service import Service
from ServiceLayer.Response import Response
from ServiceLayer.Objects.ServiceUser import ServiceUser
from ServiceLayer.Objects.ServiceProject import ServiceProject
from api_helpers import addProjectHelper, registerLoginHelper

app: Flask = Flask(__name__)
service: Service = Service()

# API

@app.route("/")
def welcome() -> str:
    return "Welcome!"

@app.route("/api/register_user", methods=["POST"])
def registerUser():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "password": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400 
    
    helper: registerLoginHelper = registerLoginHelper(request.get_json())

    response: Response[bool] = service.register(helper["username"], helper["password"])
    status: int = 201

    if response.isError():
        status = 400

    return jsonify(response.toDict()), status

# @app.route("/api/log_in", methods=["GET"])
# def logIn():
#     userData: Dict[str, str] = request.get_json()
#     validation: bool = validateRequestSchema(userData, ["username", "password"])

#     if not validation:
#         return {"error": "bad request body"}, 400

#     response: Response[ServiceUser] = service.logIn(userData["username"], userData["password"])
#     status: int = 200

#     if response.isError():
#         status = 400

#     return jsonify(response.toDict()), status

# @app.route("/api/log_out", methods=["GET"])
# def logOut():
#     userData: Dict[str, str] = request.get_json()
#     validation: bool = validateRequestSchema(userData, ["username"])

#     if not validation:
#         return {"error": "bad request body"}, 400
    
#     response: Response[bool] = service.logOut(userData["username"])
#     status: int = 200

#     if response.isError():
#         status = 400

#     return jsonify(response.toDict()), status

# @app.route("/api/change_username", methods=["POST"])
# def changeUsername():
#     userData: Dict[str, str] = request.get_json()
#     validation: bool = validateRequestSchema(userData, ["oldUsername", "newUsername", "password"])

#     if not validation:
#         return {"error": "bad request body"}, 400
    
#     response: Response[bool] = service.changeUsername(userData["oldUsername"],
#                                                       userData["newUsername"],
#                                                       userData["password"])
#     status: int = 200

#     if response.isError():
#         status = 400

#     return jsonify(response.toDict()), status

# @app.route("/api/change_password", methods=["POST"])
# def changePassword():
#     userData: Dict[str, str] = request.get_json()
#     validation: bool = validateRequestSchema(userData, ["username", "oldPassword", "newPassword"])

#     if not validation:
#         return {"error": "bad request body"}, 400
    
#     response: Response[bool] = service.changePassword(userData["username"],
#                                                       userData["oldPassword"],
#                                                       userData["newPassword"])
#     status: int = 200

#     if response.isError():
#         status = 400

#     return jsonify(response.toDict()), status

# @app.route("/api/delete_user", methods=["POST"])
# def deleteUser():
#     userData: Dict[str, str] = request.get_json()
#     validation: bool = validateRequestSchema(userData, ["username", "password"])

#     if not validation:
#         return {"error": "bad request body"}, 400
    
#     response: Response[bool] = service.deleteUser(userData["username"],
#                                                   userData["password"])
#     status: int = 200

#     if response.isError():
#         status = 400

#     return jsonify(response.toDict()), status

# @app.route("/api/get_project", methods=["GET"])
# def getProject():
#     userData: Dict[str, str] = request.get_json()
#     validation: bool = validateRequestSchema(userData, ["username", "projectName"])

#     if not validation:
#         return {"error": "bad request body"}, 400
    
#     response: Response[ServiceProject] = service.getProject(userData["username"],
#                                                             userData["projectName"])
#     status: int = 200

#     if response.isError():
#         status = 400

#     return jsonify(response.toDict()), status

# @app.route("/api/add_project", methods=["POST"])
# def addProject():
#     userData: addProjectHelper = request.get_json()
#     # validation: bool = validateRequestSchema(userData, ["username", "projectName", "description",
#     #                                                     "languages", "tool"])

#     # if not validation:
#     #     return {"error": "bad request body"}, 400
    
#     response: Response[bool] = service.addProject(userData["username"], userData["projectName"],
#                                                   userData["description"], userData["languages"],
#                                                   userData["tools"])
#     status: int = 200

#     # if response.isError():
#         # status = 400

#     # return jsonify(response.toDict()), status
#     return {}










# helpers

def validateRequestSchema(request: dict, fields: Dict[str, type]) -> bool:
    for field in fields:
        if field not in request:
            return False
        
        typ: type = fields[field]

        if type(request[field]) is not typ:
            return False
        
    for key in request:
        if key not in fields:
            return False
        
    return True
    
    
    
    


if __name__ == "__main__":
    app.run(debug=True)