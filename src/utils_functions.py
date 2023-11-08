import os,shutil

CreateDirectory = lambda x: os.mkdir(x) if not os.path.exists(x) else None
DeleteDirectory = lambda x: shutil.rmtree(x) if len(os.listdir(x)) > 0 else None
ResizeFrames = lambda x: {"image":x,"resize":768}