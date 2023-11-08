import os

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILEPATH = os.path.join(BASEPATH,"files")
OUTPUTPATH = os.path.join(BASEPATH,"outputs")
CONTENTPATH = os.path.join(BASEPATH,"content")
PROJECTYAML = os.path.join(FILEPATH,"project.yaml")
EXAMPLEVIDEO = os.path.join(CONTENTPATH,"example_video.mp4")
SAVEMODELVOICE = os.path.join(OUTPUTPATH,"save_model_voice.mp3")
SAVEVOICEPATH = os.path.join(OUTPUTPATH,"saved_voice.mp3")