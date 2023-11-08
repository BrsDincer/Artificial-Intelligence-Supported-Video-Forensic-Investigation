from utils_general import CreateDirectory,CONTENTPATH,OUTPUTPATH,FILEPATH,PATH,RESULT,SAVEMODELVOICE,SAVEVOICEPATH,EXAMPLEVIDEO,ds__,ar__
from create_completion_for_video import CreateModelCompletion
import gradio as gr,os

CreateDirectory(OUTPUTPATH)
CreateDirectory(CONTENTPATH)


videoInput = gr.File(label="Video Path",
                      file_types=[".mp4"])

modelResponseOutput = gr.Textbox(lines=10,
                                  label="Model Answer",
                                  placeholder="Waiting...")

transcriptResponseOutput = gr.Textbox(label="Video Transcript",
                                      placeholder="Waiting...")

voiceOutput = gr.Audio(label="Model Audio")
videoOutput = gr.Video(label="Video",
                        visible=True,
                        interactive=False)
videoVoiceOutput = gr.Audio(label="Video Audio")

modelBase = CreateModelCompletion()
modelTarget = modelBase.GetModel()

if __name__ == "__main__":
    
    def GetAllContents(initPath:PATH)->RESULT:
        textResponse = modelBase.RunVision(modelClient=modelTarget,
                                            videoPath=initPath)
        if textResponse:
            out = modelBase.RunTextToSpeech(modelClient=modelTarget,
                                            initText=str(textResponse))
            if out:
                if (os.path.exists(SAVEMODELVOICE)) and (os.path.exists(SAVEVOICEPATH)):
                    transcript = modelBase.RunTranscription(modelClient=modelTarget,
                                                            videoPath=initPath)
                    return [initPath,textResponse,SAVEMODELVOICE,transcript,SAVEVOICEPATH]
                else:
                    return [None,None,None,None]
            else:
                return [None,None,None,None]
        else:
            return [None,None,None,None]
    
    iface = gr.Interface(fn=GetAllContents,
                          inputs=[videoInput],
                          outputs=[videoOutput,
                                    modelResponseOutput,
                                    voiceOutput,
                                    transcriptResponseOutput,
                                    videoVoiceOutput],
                          theme=gr.themes.Soft(),
                          examples=[EXAMPLEVIDEO],
                          description=ds__,
                          article=ar__)

    
    iface.launch(server_name="127.0.0.1",
                  server_port=8800,
                  inbrowser=False,
                  debug=True,
                  share=True,
                  max_threads=10,
                  show_api=False,
                  show_error=True)
        
