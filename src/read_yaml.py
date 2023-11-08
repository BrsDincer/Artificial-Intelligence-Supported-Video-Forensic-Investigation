import yaml ; from utils_general import CLASSINIT,NULL,DOCUMENTATION,ERROR,ErrorModule,PROJECTYAML

class ReadProjectFile(object):
    def __init__(self)->CLASSINIT:
        self.directory = PROJECTYAML
    def __str__(self)->str:
        return "Reading Project YAML File - SubScript"
    def __call__(self)->NULL | None:
        return None
    def __getstate__(self)->ERROR:
        ErrorModule().Default()
    def __repr__(self)->DOCUMENTATION | str:
        return ReadProjectFile.__doc__
    def GetAPI(self)->str:
        safeLoad = yaml.safe_load(open(self.directory,
                                       "r",
                                       errors="ignore",
                                       encoding="utf-8"))
        return safeLoad["apikey"]["OPENAI_API_KEY"]

