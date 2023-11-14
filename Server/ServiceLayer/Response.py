from typing import Generic, TypeVar


T = TypeVar("T")

class Response(Generic[T]):

    # should be private
    def __init__(self, value: T, error: bool, message: str) -> None:
        super().__init__()
        self.__value: T = value
        self.__error: bool = error
        self.__message: str = message

    def getValue(self) -> T:
        return self.__value
    
    def isError(self) -> bool:
        return self.__error
    
    def getErrorMessage(self) -> str:
        return self.__message
    
    

    @classmethod
    def makeValueResponse(cls, value: T) -> "Response[T]":
        return cls(value, False, "")
    
    @classmethod
    def makeErrorResponse(cls, errorMessage: str) -> "Response[T]":
        return cls(None, True, errorMessage)