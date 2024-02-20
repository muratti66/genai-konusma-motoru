import google.generativeai as genai
from conf.config import Config
from conf.static import Messages
from google.generativeai.types import generation_types
from google.generativeai import GenerativeModel


class GenAI:
    __gemini_model: GenerativeModel = None

    @staticmethod
    def init():
        genai.configure(api_key=Config.GEMINI_API_KEY)
        GenAI.__gemini_model = genai.GenerativeModel(Config.GEMINI_MODEL)
        print(Messages.COMP_STARTED.format(GenAI.__name__))

    @staticmethod
    def __talk_to_gemini(msg: str) -> generation_types.GenerateContentResponse:
        return GenAI.__gemini_model.generate_content(msg)

    @staticmethod
    def talk(msg: str) -> str:
        print('"{}" question sending to GenAI(Gemini)'.format(msg))
        out = GenAI.__talk_to_gemini(msg).text
        print('"{}" answer recived from GenAI(Gemini)'.format(out))
        return out
