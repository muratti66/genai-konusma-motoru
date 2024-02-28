import tkinter
from components.answer_box import AnswerTextBox
from components.question_box import QuestionTextBox
from components.status_box import StatusTextBox
from components.talk_button import TalkButton
from conf.config import Config
from conf.static import Messages, StaticValues, FilePaths, ShortCuts
from lib.component_lib import Others


class RootWindow:

    def __init__(self):
        self.__root: tkinter.Tk = tkinter.Tk()
        self.__init_mw()
        QuestionTextBox.init(self.__root)
        TalkButton.init(self.__root)
        AnswerTextBox.init(self.__root)
        StatusTextBox.init(self.__root)
        self.__init_shortcuts()
        print(Messages.COMP_INIT_DONE.format(RootWindow.__name__))

    def __init_mw(self):
        self.__root.title(StaticValues.MAIN_WINDOW_TITLE)
        self.__root.geometry(Config.MAIN_WINDOW_GEOMETRY)
        self.__root.resizable(False, False)
        self.__root.iconphoto(True, Others.get_icon_image(FilePaths.PROG_ICON, (0, 0), None))

    def __init_shortcuts(self):
        self.__root.bind(ShortCuts.RETURN, TalkButton.on_response_click_button)
        self.__root.bind(ShortCuts.CMD_C, AnswerTextBox.answer_to_clipboard)
        self.__root.bind(ShortCuts.CMD_S, TalkButton.to_voice_click_button)
        TalkButton.get_button().bind(ShortCuts.BTN_PRESS, TalkButton.on_button_press)
        TalkButton.get_button().bind(ShortCuts.BTN_RELEASE, TalkButton.on_button_release)

    def run(self):
        print(Messages.COMP_STARTED.format(RootWindow.__name__))
        self.__root.mainloop()
        print(Messages.COMP_STOPPED.format(RootWindow.__name__))
