import sys
from components.root_window import RootWindow
from conf.config import Config
from conf.static import StaticValues
from lib.genai_api import GenAI
from lib.microphone_api import MicrophoneAPI
from lib.ml_api import MLAPI


if __name__ == '__main__':
    # for first run... (--first-run parameter will be downloaded the "speech to text" model from hugging face.)
    if sys.argv.__len__() > 1 and sys.argv[1] == StaticValues.FIRST_RUN_PARAM:
        Config.HUGGING_FACE_DOWNLOAD_ALLOW = True

    # api libraries init
    MicrophoneAPI.init()
    GenAI.init()
    MLAPI.init()

    # main window init and run.
    mw = RootWindow()
    mw.run()
