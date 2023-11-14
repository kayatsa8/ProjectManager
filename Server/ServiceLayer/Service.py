from Server.BusinessLayer.Facade import Facade


class Service:

    def __init__(self) -> None:
        self.__facade = Facade()

    