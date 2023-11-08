from utils_general import CLASSINIT,SAVEVOICEPATH,NULL,ERROR,DOCUMENTATION,PATH,RESULT,ErrorModule
import moviepy.editor as mp

class VoiceExtraction(object):
    def __init__(self)->CLASSINIT:
        self.directory = SAVEVOICEPATH
        self.codecType = "mp3"
    def __str__(self)->str:
        return "Voice Extraction - Process Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return VoiceExtraction.__doc__
    def Get(self,videoPath:PATH)->RESULT:
        inputFile = mp.VideoFileClip(videoPath)
        audioOut = inputFile.audio
        audioOut.write_audiofile(self.directory,verbose=False)

