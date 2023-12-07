from typing import Dict, List

from flask import Flask, request, jsonify

from ServiceLayer.Service import Service
from ServiceLayer.Response import Response
from ServiceLayer.Objects.ServiceUser import ServiceUser
from ServiceLayer.Objects.ServiceProject import ServiceProject
from apiRequestBodies import addProjectBody, changePasswordBody, changeUsernameBody, deleteUserBody, getProjectBody, logOutBody, registerLoginBody

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
    
    body: registerLoginBody = registerLoginBody(request.get_json())

    response: Response[bool] = service.register(body["username"], body["password"])
    status: int = 201

    if response.isError():
        status = 400

    return jsonify(response.toDict()), status

@app.route("/api/log_in", methods=["GET"])
def logIn():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "password": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: registerLoginBody = registerLoginBody(request.get_json())

    response: Response[ServiceUser] = service.logIn(body["username"], body["password"])
    status: int = 200

    if response.isError():
        status = 400

    return jsonify(response.toDict()), status

@app.route("/api/log_out", methods=["GET"])
def logOut():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: logOutBody = logOutBody(request.get_json())
    
    response: Response[bool] = service.logOut(body["username"])
    status: int = 200

    if response.isError():
        status = 400

    return jsonify(response.toDict()), status

@app.route("/api/change_username", methods=["POST"])
def changeUsername():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "oldUsername": str,
        "newUsername": str,
        "password": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: changeUsernameBody= changeUsernameBody(request.get_json())
    
    response: Response[bool] = service.changeUsername(body["oldUsername"],
                                                      body["newUsername"],
                                                      body["password"])
    status: int = 200

    if response.isError():
        status = 400

    return jsonify(response.toDict()), status

@app.route("/api/change_password", methods=["POST"])
def changePassword():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "oldPassword": str,
        "newPassword": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: changePasswordBody = changePasswordBody(request.get_json())
    
    response: Response[bool] = service.changePassword(body["username"],
                                                      body["oldPassword"],
                                                      body["newPassword"])
    status: int = 200

    if response.isError():
        status = 400

    return jsonify(response.toDict()), status

@app.route("/api/delete_user", methods=["POST"])
def deleteUser():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "password": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: deleteUserBody = deleteUserBody(request.get_json())
    
    response: Response[bool] = service.deleteUser(body["username"],
                                                  body["password"])
    status: int = 200

    if response.isError():
        status = 400

    return jsonify(response.toDict()), status

@app.route("/api/get_project", methods=["GET"])
def getProject():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "projectName": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: getProjectBody = getProjectBody(request.get_json())
    
    response: Response[ServiceProject] = service.getProject(body["username"],
                                                            body["projectName"])
    status: int = 200

    if response.isError():
        status = 400

    return jsonify(response.toDict()), status

@app.route("/api/add_project", methods=["POST"])
def addProject():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "projectName": str,
        "description": str,
        "languages": List[str],
        "tools": List[str]
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: addProjectBody = addProjectBody(request.get_json())
    
    response: Response[bool] = service.addProject(body["username"], body["projectName"],
                                                  body["description"], body["languages"],
                                                  body["tools"])
    status: int = 200

    if response.isError():
        status = 400

    return jsonify(response.toDict()), status









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