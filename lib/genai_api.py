import google.generativeai as genai
from components.load_window import LoadWindow
from conf.config import Config
from conf.static import Messages
from google.generativeai.types import generation_types
from google.generativeai import GenerativeModel, ChatSession


class GenAI:
    __gemini_model: GenerativeModel = None
    __gemini_chat_session: ChatSession = None
    __gemini_chat_count = 0

    @staticmethod
    def init():
        LoadWindow.update_loading_msg(Messages.COMP_STARTING.format(GenAI.__name__))
        genai.configure(api_key=Config.GEMINI_API_KEY)
        GenAI.__gemini_model = genai.GenerativeModel(Config.GEMINI_MODEL)
        GenAI.__gemini_chat_session = GenAI.__gemini_model.start_chat()
        LoadWindow.update_loading_msg(Messages.COMP_STARTED.format(GenAI.__name__))

    @staticmethod
    def __check_for_history_clean() -> None:
        if GenAI.__gemini_chat_count > 30:
            new_history = GenAI.__gemini_chat_session.history[14:]
            GenAI.__gemini_chat_session.history = new_history
            GenAI.__gemini_chat_count = GenAI.__gemini_chat_session.history.__len__()
            print('History cleared.., new history size {}'.format(GenAI.__gemini_chat_count))
            print(GenAI.__gemini_chat_session.history)

    @staticmethod
    def __talk_to_gemini(msg: str) -> generation_types.GenerateContentResponse:
        return GenAI.__gemini_chat_session.send_message(msg)

    @staticmethod
    def talk(msg: str) -> str:
        GenAI.__check_for_history_clean()
        GenAI.__gemini_chat_count += 1
        print('"{}" question sending to GenAI(Gemini)'.format(msg))
        out = GenAI.__talk_to_gemini(msg).text
        print('"{}" answer recived from GenAI(Gemini)'.format(out))
        return out
