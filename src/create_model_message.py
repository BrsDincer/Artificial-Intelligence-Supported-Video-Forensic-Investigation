from utils_general import CLASSINIT,NULL,DOCUMENTATION,PATH,ERROR,ErrorModule
from record_video import GetVideoCapture
from input_message_functions import CreateInputURL,CreateInputTEXT

class CreateModelMessage(object):
    def __init__(self)->CLASSINIT:
        self.promptDict = dict()
        self.promptDict["role"] = "user"
        self.promptDict["content"] = []
        self.defaultCommand = (
            "Analyze it from a historical perspective, "
            "and if there are points that do not match the facts, "
            "point out and explain them. "
            "Transfer all the details you see and identify surrounding objects. "
            "What do you see?"
            )
    def __str__(self)->str:
        return "Creating Model Message - Process Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return CreateModelMessage.__doc__
    def Get(self,videoPath:PATH,firstFrom:int=100)->list:
        baseFrame = GetVideoCapture().Record(videoPath=videoPath,firstFrom=firstFrom)
        self.promptDict["content"].append(CreateInputURL(baseFrame[0::10]))
        self.promptDict["content"].append(CreateInputTEXT(self.defaultCommand))
        return self.promptDict
    

        