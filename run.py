import sys
from conf.config import Config
from conf.static import StaticValues


if __name__ == '__main__':
    # open load window
    from components.load_window import LoadWindow
    LoadWindow.init()

    # for first run... (--first-run parameter will be downloaded the "speech to text" model from hugging face.)
    if sys.argv.__len__() > 1 and sys.argv[1] == StaticValues.FIRST_RUN_PARAM:
        Config.HUGGING_FACE_DOWNLOAD_ALLOW = True

    # api libraries init
    from lib.microphone_api import MicrophoneAPI
    MicrophoneAPI.init()

    from lib.genai_api import GenAI
    GenAI.init()

    from lib.ml_api import MLAPI
    MLAPI.init()

    # close load window
    LoadWindow.destroy()

    # main window init and run.
    from components.root_window import RootWindow
    mw = RootWindow()
    mw.run()
