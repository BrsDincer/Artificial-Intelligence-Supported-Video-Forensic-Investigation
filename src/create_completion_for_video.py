from utils_general import CLASSINIT,MODELVOICE,SAVEMODELVOICE,DEFAULTVOICE,MODELVISION,SAVEVOICEPATH,DOCUMENTATION,PATH,RESULT,ERROR,NULL,MODEL,ErrorModule
from create_model_message import CreateModelMessage
from read_yaml import ReadProjectFile
from openai import OpenAI
from voice_extraction import VoiceExtraction
import os

class CreateModelCompletion(object):
    def __init__(self)->CLASSINIT:
        self.openaiapi = ReadProjectFile().GetAPI()
        os.environ["OPENAI_API_KEY"] = self.openaiapi
        self.defaultMaxToken = 500
        self.defaultTimeout = 500
        self.temperature = 0
        self.frequency_penalty = 1.0
        self.presence_penalty = 2.0
        self.voicePath = SAVEVOICEPATH
    def __str__(self)->str:
        return "Creating Model Completion - Process Script"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return CreateModelCompletion.__doc__
    def GetModel(self)->MODEL:
        modelClient = OpenAI()
        return modelClient
    def RunVoiceExtraction(self,videoPath:PATH)->RESULT:
        try:
            VoiceExtraction().Get(videoPath=videoPath)
            return True
        except:
            return False
    def GetMessage(self,videoPath:PATH,firstFrom:int=100)->dict:
        modelMessage = CreateModelMessage().Get(videoPath=videoPath,firstFrom=firstFrom)
        return modelMessage
    def RunVision(self,modelClient:MODEL,videoPath:PATH,firstFrom:int=100)->RESULT:
        modelMessage = self.GetMessage(videoPath=videoPath,firstFrom=firstFrom)
        result = modelClient.chat.completions.create(model=MODELVISION,
                                                     max_tokens=self.defaultMaxToken,
                                                     temperature=self.temperature,
                                                     presence_penalty=self.presence_penalty,
                                                     frequency_penalty=self.frequency_penalty,
                                                     timeout=self.defaultTimeout,
                                                     messages=[modelMessage])
        if result.choices[0].finish_details["type"].lower() == "stop":
            message = result.choices[0].message.content
            return message
        else:
            return "[RESPONSE - NOT FOUND]"
    def RunTextToSpeech(self,modelClient:MODEL,initText:str)->RESULT:
        response = modelClient.audio.speech.create(model=MODELVOICE,
                                                   voice=DEFAULTVOICE,
                                                   response_format="mp3",
                                                   timeout=self.defaultTimeout,
                                                   input=str(initText))
        try:
            response.stream_to_file(SAVEMODELVOICE)
            return True
        except:
            return False
    def RunTranscription(self,modelClient:MODEL,videoPath:PATH)->RESULT:
        if not os.path.exists(self.voicePath):
            out = self.RunVoiceExtraction(videoPath=videoPath)
        else:
            pass
        audioFile = open(self.voicePath,"rb")
        transcript = modelClient.audio.transcriptions.create(model="whisper-1",
                                                             file=audioFile,
                                                             response_format="text")
        return transcript

            