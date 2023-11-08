from utils_general import URL

def CreateInputURL(initialUrl:str | URL)->dict:
    return {"type":"image_url",
            "image_url":{"url":f"data:image/jpeg;base64,{str(initialUrl)}"}}
def CreateInputTEXT(initialText:str)->dict:
    return {"type":"text",
            "text":str(initialText)}