from typing import Generic, Optional, TypeVar
from ServiceLayer.Objects.ServiceUser import ServiceUser
from ServiceLayer.Objects.ServiceProject import ServiceProject


T = TypeVar("T")

class Response(Generic[T]):

    # should be private
    def __init__(self, value: Optional[T], error: bool, message: str) -> None:
        super().__init__()
        self.__value: Optional[T] = value
        self.__error: bool = error
        self.__message: str = message

    def getValue(self) -> Optional[T]:
        return self.__value
    
    def isError(self) -> bool:
        return self.__error
    
    def getErrorMessage(self) -> str:
        return self.__message
    
    def toDict(self) -> dict:
        if isinstance(self.__value, ServiceProject) or isinstance(self.__value, ServiceUser):
            return {
                "value": self.__value.toDict(),
                "error": self.__error,
                "message": self.__message
            }

        return {
            "value": self.__value,
            "error": self.__error,
            "message": self.__message
        }
    
    

    @classmethod
    def makeValueResponse(cls, value: T) -> "Response[T]":
        return cls(value, False, "")
    
    @classmethod
    def makeErrorResponse(cls, errorMessage: str) -> "Response[T]":
        return cls(None, True, errorMessage)