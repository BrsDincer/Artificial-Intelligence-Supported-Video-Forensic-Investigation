from utils_class import CLASSINIT,ERROR,DOCUMENTATION
class ErrorModule(object):
    def __init__(self)->CLASSINIT:
        self.error = NotImplementedError ; self.message = NotImplemented
    def __str__(self)->str:
        return "Error Module Creation - SubScript"
    def __call__(self)->ERROR:
        return self.error(self.message)
    def __getstate__(self)->ERROR:
        raise NotImplementedError(NotImplemented)
    def __repr__(self)->DOCUMENTATION | str:
        return ErrorModule.__doc__
    def Raise(self,errorClass:ERROR,errorMessage:str)->ERROR:
        raise errorClass(errorMessage)
    def Default(self)->ERROR:
        raise self.error(self.message)

