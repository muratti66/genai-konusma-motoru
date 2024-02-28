import threading
import tkinter
from components.answer_box import AnswerTextBox
from components.question_box import QuestionTextBox
from components.status_box import StatusTextBox
from conf.static import StaticValues, FilePaths, Messages
from lib.component_lib import Others
from lib.genai_api import GenAI
from lib.microphone_api import MicrophoneAPI
from lib.ml_api import MLAPI
from PIL import Image


class TalkButton:
    __button: tkinter.Button = None
    __answer: str = None

    @staticmethod
    def init(root: tkinter.Tk) -> None:
        icon = Others.get_icon_image(FilePaths.VOICE_ICON, (24, 24), Image.LANCZOS)
        TalkButton.__button = tkinter.Button(root, image=icon, width=40, height=40)
        TalkButton.__button.grid(row=2, column=2, padx=10, pady=10, ipadx=0, ipady=0, sticky='N')
        TalkButton.__button.image = icon
        print(Messages.COMP_INIT_DONE.format(TalkButton.__name__))

    @staticmethod
    def on_response_click_button(event=None) -> None:
        question = QuestionTextBox.get_question().strip()
        if question == StaticValues.DEFAULT_QUESTION or question == '':
            return
        StatusTextBox.write_response(Messages.TEXT_TO_GENAI)
        QuestionTextBox.write_response(question)
        TalkButton.__answer = GenAI.talk(question)
        AnswerTextBox.write_response(StaticValues.GEMINI_ANSWER_MSG, TalkButton.__answer)
        StatusTextBox.write_response(Messages.ANSWER_FROM_GENAI)

    @staticmethod
    def to_voice_click_button(event=None) -> None:
        StatusTextBox.write_response(Messages.ANSWER_TO_VOICE)
        threading.Thread(target=Others.talk_now, args=(TalkButton.__answer,)).start()

    @staticmethod
    def on_button_press(event) -> None:
        StatusTextBox.write_response(Messages.VOICE_LISTENING)
        MicrophoneAPI.start_recording()

    @staticmethod
    def on_button_release(event) -> None:
        StatusTextBox.write_response(Messages.VOICE_LISTENED)
        MicrophoneAPI.stop_recording()
        TalkButton.__start_converting()

    @staticmethod
    def __start_converting():
        StatusTextBox.write_response(Messages.VOICE_TO_TEXT)
        question = MLAPI.get_stt_w_file(FilePaths.REC_TMP_FILE_PATH)
        StatusTextBox.write_response(Messages.VOICE_TO_TEXT_DONE)
        QuestionTextBox.write_response(question)
        StatusTextBox.write_response(Messages.TEXT_TO_GENAI)
        answer_r = GenAI.talk(question.strip())
        StatusTextBox.write_response(Messages.ANSWER_FROM_GENAI)
        AnswerTextBox.write_response(StaticValues.GEMINI_ANSWER_MSG, answer_r)
        threading.Thread(target=Others.talk_now, args=(answer_r,)).start()
        MicrophoneAPI.init()
        StatusTextBox.write_response(Messages.ANSWER_TO_VOICE)

    @staticmethod
    def get_button() -> tkinter.Button:
        return TalkButton.__button
