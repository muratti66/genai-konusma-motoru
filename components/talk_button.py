import threading
import tkinter
from components.answer_box import AnswerTextBox
from components.question_box import QuestionTextBox
from conf.static import StaticValues, FilePaths, Messages
from lib.component_lib import Others
from lib.genai_api import GenAI
from lib.microphone_api import MicrophoneAPI
from lib.ml_api import MLAPI
from PIL import Image
from tkinter import ttk


class TalkButton:
    __button: tkinter.Button = None
    __answer: str = None

    @staticmethod
    def init(root: tkinter.Tk) -> None:
        icon = Others.get_icon_image(FilePaths.VOICE_ICON, (24, 24), Image.LANCZOS)
        TalkButton.__button = ttk.Button(root, image=icon)
        TalkButton.__button.grid(row=2, column=2, padx=10, pady=4, ipadx=0, ipady=0, sticky='N')
        TalkButton.__button.image = icon
        print(Messages.COMP_INIT_DONE.format(TalkButton.__name__))

    @staticmethod
    def on_response_click_button(event=None) -> None:
        question = QuestionTextBox.get_question()
        if question.strip() == StaticValues.DEFAULT_QUESTION:
            return
        TalkButton.__answer = GenAI.talk(question.strip())
        AnswerTextBox.write_response(StaticValues.GEMINI_ANSWER_MSG, TalkButton.__answer)

    @staticmethod
    def to_voice_click_button(event=None) -> None:
        threading.Thread(target=Others.talk_now, args=(TalkButton.__answer,)).start()

    @staticmethod
    def on_button_press(event) -> None:
        MicrophoneAPI.start_recording()

    @staticmethod
    def on_button_release(event) -> None:
        MicrophoneAPI.stop_recording()
        TalkButton.__start_converting()

    @staticmethod
    def __start_converting():
        question = MLAPI.get_stt_w_file(FilePaths.REC_TMP_FILE_PATH)
        QuestionTextBox.write_response(question)
        answer_r = GenAI.talk(question.strip())
        AnswerTextBox.write_response(StaticValues.GEMINI_ANSWER_MSG, answer_r)
        threading.Thread(target=Others.talk_now, args=(answer_r,)).start()
        MicrophoneAPI.init()

    @staticmethod
    def get_button() -> tkinter.Button:
        return TalkButton.__button
