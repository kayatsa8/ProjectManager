from Server.BusinessLayer.Facade import Facade
from Server.ServiceLayer.Response import Response


class Service:

    def __init__(self) -> None:
        self.__facade = Facade()

    def register(self, username: str, password: str) -> Response[bool]:
        try:
            self.__facade.register(username, password)
            return Response.makeValueResponse(True)
        except Exception as e:
            return Response.makeErrorResponse(str(e))