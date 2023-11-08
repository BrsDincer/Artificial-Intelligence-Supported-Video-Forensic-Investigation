from utils_general import CLASSINIT,NULL,DOCUMENTATION,PATH,RESULT,ERROR,ENGINE,ErrorModule
import cv2 as cv,os,sys,base64

class GetVideoCapture(object):
    def __init__(self)->CLASSINIT:
        self.imcodeType = ".jpg"
    def __str__(self)->str:
        return "Video Frame Gathering - Process Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return GetVideoCapture.__doc__
    def CaptureEngine(self,videoPath:PATH)->ENGINE:
        if os.path.exists(videoPath):
            engine = cv.VideoCapture(videoPath)
            engine.set(3,1080)
            engine.set(4,720)
            return engine
        else:
            ErrorModule().Raise(FileNotFoundError,"FILE DOES NOT EXIST")
            sys.exit(1)
    def Record(self,videoPath:PATH,firstFrom:int=100)->RESULT:
        engine = self.CaptureEngine(videoPath=videoPath)
        frameList = []
        while engine.isOpened():
            success,frame = engine.read()
            if not success:
                break
            _,bufferEncode = cv.imencode(self.imcodeType,frame)
            frameList.append(base64.b64encode(bufferEncode).decode("utf-8"))
        try:
            engine.release()
        except:
            pass
        return frameList[:firstFrom]
