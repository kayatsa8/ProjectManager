from typing import Dict, List

from flask import Flask, request, jsonify
from flask_cors import CORS

from ServiceLayer.Service import Service
from ServiceLayer.Response import Response
from ServiceLayer.Objects.ServiceUser import ServiceUser
from ServiceLayer.Objects.ServiceProject import ServiceProject
from apiRequestBodies import addProjectBody, changePasswordBody, changeProjectDescriptionBody, changeProjectLanguagesBody, changeProjectNameBody, changeProjectToolsBody, changeUsernameBody, deleteProjectBody, \
     deleteUserBody, getProjectBody, logOutBody, markProjectBody, registerLoginBody

app: Flask = Flask(__name__)
CORS(app)
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

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/log_in", methods=["PATCH"])
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

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/log_out", methods=["PATCH"])
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

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/change_username", methods=["PATCH"])
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

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/change_password", methods=["PATCH"])
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

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/delete_user", methods=["DELETE"])
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

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/get_project", methods=["POST"])
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

    # if response.isError():
    #     status = 400

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

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/delete_project", methods=["DELETE"])
def deleteProject():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "projectName": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: deleteProjectBody = deleteProjectBody(request.get_json())
    
    response: Response[bool] = service.deleteProject(body["username"], body["projectName"])
    status: int = 200

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/change_project_name", methods=["PATCH"])
def changeProjectName():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "projectName": str,
        "newProjectName": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: changeProjectNameBody = changeProjectNameBody(request.get_json())
    
    response: Response[bool] = service.changeProjectName(body["username"], body["projectName"], body["newProjectName"])
    status: int = 200

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/change_project_description", methods=["PATCH"])
def changeProjectDescription():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "projectName": str,
        "description": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: changeProjectDescriptionBody = changeProjectDescriptionBody(request.get_json())
    
    response: Response[bool] = service.changeProjectDescription(body["username"], body["projectName"], body["description"])
    status: int = 200

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/change_project_languages", methods=["PATCH"])
def changeProjectLanguages():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "projectName": str,
        "languages": List[str]
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: changeProjectLanguagesBody = changeProjectLanguagesBody(request.get_json())
    
    response: Response[bool] = service.changeProjectLanguages(body["username"], body["projectName"], body["languages"])
    status: int = 200

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/change_project_tools", methods=["PATCH"])
def changeProjectTools():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "projectName": str,
        "tools": List[str]
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: changeProjectToolsBody = changeProjectToolsBody(request.get_json())
    
    response: Response[bool] = service.changeProjectTools(body["username"], body["projectName"], body["tools"])
    status: int = 200

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status

@app.route("/api/mark_project", methods=["PATCH"])
def markProjectCompleteIncomplete():
    data: dict = request.get_json()
    fields: Dict[str, type] = {
        "username": str,
        "projectName": str
    }

    if not validateRequestSchema(data, fields):
        return {"error": "bad request body"}, 400
    
    body: markProjectBody = markProjectBody(request.get_json())
    
    response: Response[bool] = service.markProjectCompleteIncomplete(body["username"], body["projectName"])
    status: int = 200

    # if response.isError():
    #     status = 400

    return jsonify(response.toDict()), status







# helpers

def validateRequestSchema(request: dict, fields: Dict[str, type]) -> bool:
    for field in fields:
        if field not in request:
            return False
        
        typ: type = fields[field]

        if type(request[field]) is not typ:
            if typ is List[str]:
                if not stringListCase(request[field]):
                    return False
            else:
                return False


            
        
    for key in request:
        if key not in fields:
            return False
        
    return True
    

def stringListCase(l) -> bool:
    if type(l) is not list:
        return False
    
    for item in l:
        if type(item) is not str:
            return False
        
    return True
    
    


if __name__ == "__main__":
    app.run(debug=True)